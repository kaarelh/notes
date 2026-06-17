#!/usr/bin/env python3
"""
Convert Obsidian inline footnotes  ^[body]  to GitHub reference footnotes.

  some text^[the note]      -->   some text[^N]
                                  ...
                                  [^N]: the note      (appended at end of file)

- Uses a bracket-matching parser, so footnote bodies containing nested [...] are
  handled correctly (a naive regex would truncate them).
- Skips fenced code blocks (``` / ~~~) and inline code spans (`...`).
- Numbers per file, starting after any pre-existing [^n] labels (collision-safe).
- Multi-line footnote bodies get their continuation lines indented 4 spaces so
  GitHub keeps them inside the footnote.
- Footnotes with unbalanced brackets (a source typo) are LEFT UNTOUCHED and
  reported, so nothing gets silently corrupted.

Usage:
    python3 convert_footnotes.py            # dry run: report only
    python3 convert_footnotes.py --apply    # rewrite files in place
    python3 convert_footnotes.py --root path/to/repo
"""
import os, re, glob, argparse

def code_spans(src):
    spans = []
    for m in re.finditer(r'(?ms)^[ \t]*(`{3,}|~{3,})[^\n]*\n.*?^[ \t]*\1[ \t]*$', src):
        spans.append((m.start(), m.end()))
    for m in re.finditer(r'(`+)(?:.+?)\1', src, re.S):
        if not any(a <= m.start() < b for a, b in spans):
            spans.append((m.start(), m.end()))
    return spans

def in_spans(i, spans):
    return any(a <= i < b for a, b in spans)

def fmt_def(num, body):
    body = body.strip()
    lines = body.split('\n')
    if len(lines) == 1:
        return f'[^{num}]: {lines[0]}'
    head = f'[^{num}]: {lines[0]}'
    tail = '\n'.join(('    ' + ln) if ln.strip() else '' for ln in lines[1:])
    return head + '\n' + tail


def flatten_nested(body):
    """Footnotes inside footnotes can't exist on GitHub. Demote any inner
    ^[...] (balanced) to a parenthetical aside. Loops for double-nesting."""
    changed = 0
    for _ in range(10):
        out, i, n, did = [], 0, len(body), False
        while i < n:
            if body[i] == '^' and i+1 < n and body[i+1] == '[':
                depth, j, ok = 0, i+1, False
                while j < n:
                    c = body[j]
                    if c == '[': depth += 1
                    elif c == ']':
                        depth -= 1
                        if depth == 0: ok = True; break
                    j += 1
                if ok:
                    out.append(' (' + body[i+2:j] + ')'); i = j+1; did = True; continue
            out.append(body[i]); i += 1
        body = ''.join(out)
        if did: changed += 1
        else: break
    return body, changed

def convert(src):
    spans = code_spans(src)
    existing = [int(x) for x in re.findall(r'\[\^(\d+)\]', src)]
    counter = (max(existing) + 1) if existing else 1
    out, notes, unbalanced, nested_total = [], [], 0, 0
    i, n = 0, len(src)
    while i < n:
        if src[i] == '^' and i + 1 < n and src[i+1] == '[' and not in_spans(i, spans):
            depth, j, ok = 0, i + 1, False
            while j < n:
                c = src[j]
                if c == '[': depth += 1
                elif c == ']':
                    depth -= 1
                    if depth == 0: ok = True; break
                j += 1
            if ok:
                _b, _c = flatten_nested(src[i+2:j])
                nested_total += _c
                notes.append((counter, _b))
                out.append(f'[^{counter}]'); counter += 1
                i = j + 1; continue
            else:
                unbalanced += 1
                out.append(src[i]); i += 1; continue
        out.append(src[i]); i += 1
    new = ''.join(out)
    if notes:
        block = '\n'.join(fmt_def(num, body) for num, body in notes)
        new = new.rstrip('\n') + '\n\n' + block + '\n'
    multiline = sum(1 for _, b in notes if '\n' in b.strip())
    return new, len(notes), unbalanced, multiline, nested_total

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--root', default='.')
    ap.add_argument('--apply', action='store_true')
    args = ap.parse_args()
    files = glob.glob(os.path.join(args.root, '**', '*.md'), recursive=True)
    tot_files = tot_notes = tot_unbal = tot_multi = tot_nested = 0
    unbal_files, multi_files = [], []
    for path in sorted(files):
        src = open(path, encoding='utf-8').read()
        if '^[' not in src:
            continue
        new, k, unbal, multi, nested = convert(src)
        tot_nested += nested
        if k == 0 and unbal == 0:
            continue
        tot_files += 1; tot_notes += k; tot_unbal += unbal; tot_multi += multi
        if unbal: unbal_files.append((path, unbal))
        if multi: multi_files.append((path, multi))
        if args.apply and new != src:
            open(path, 'w', encoding='utf-8').write(new)
    mode = 'APPLIED' if args.apply else 'DRY RUN'
    print(f'[{mode}] files touched: {tot_files} | footnotes converted: {tot_notes} '
          f'| multiline: {tot_multi} | nested->parenthetical: {tot_nested} | unbalanced(left as-is): {tot_unbal}')
    if unbal_files:
        print('\n!! UNBALANCED footnotes (fix the missing/extra bracket by hand):')
        for p, c in unbal_files: print(f'   {c}x  {p}')
    if multi_files:
        print('\n~  multi-line footnotes (converted; eyeball the rendering):')
        for p, c in multi_files: print(f'   {c}x  {p}')

if __name__ == '__main__':
    main()
