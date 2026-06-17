
not incompleteness => can solve halting by searching for proofs of halting

thus, halting problem undecidable => incompleteness thm
meta-comment: outside view it seems like a much simpler proof of incompleteness, which is some evidence for something being wrong with it? (though i guess maybe it doesn't give that for peano arithmetic, just languages that can talk about turing machines halting, e.g. set theory — i guess a large part of gödel's pf is showing that peano arithmetic can be made to talk about proofs, so maybe it still makes sense to talk about gödel's significantly more complicated proof even given this simpler proof for the set theory statement is available)

converse is trickier, but i think also works:
halting problem decidable => can create recursively enumerable axiom sequence which gives a complete theory by starting from ZFC and on each step computing if next statement decidable or undecidable given previous ones (can do this by defining a proof searcher turing machine and checking if it halts), and adding all undecidable statements to axiom list => there is a reasonable extension of ZFC which is complete
thus, incompleteness theorem => halting problem undecidable
