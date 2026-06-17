
I designed a [pro-human(ity)/anti-(non-human-)AI flag](https://drive.google.com/file/d/1R33RMh8T7ime6VIXK0u7Oyj2zCZjlHnT/view?usp=sharing):
![[Pasted image 20250812204424.png]]

- The red-black circle is [HAL](https://youtu.be/ARJ8cAGm6JE)'s eye; it represents the non-human in-all-ways-super-human AI(s) that the world's various AI capability developers are trying to create, that will imo by default render all remotely human beings completely insignificant and cause humanity to completely lose control over what happens :(.
- The white star covering HAL's eye has rays at the angles of the limbs of Leonardo's [Vitruvian Man](https://en.wikipedia.org/wiki/Vitruvian_Man); it represents humans/humanity remaining more capable than non-human AI (by banning AGI development and by carefully self-improving).
- The blue background represents our potential self-made ever-better future, involving [global governance/cooperation/unity](https://www.britannica.com/topic/flag-of-the-United-Nations) in the face of AI.

Feel free to suggest improvements to the flag. Here's latex to generate it:

% written mostly by o3 and o4-mini-high, given k's prompting  
% an anti-AI flag. a HAL "eye" (?) is covered by a vitruvian man star
\documentclass[tikz]{standalone}
\usetikzlibrary{calc}
\usepackage{xcolor}                 % for \definecolor
\definecolor{UNBlue}{HTML}{5B92E5}

\begin{document}
\begin{tikzpicture}
%--------------------------------------------------------
% flag geometry
%--------------------------------------------------------
\def\flagW{6cm}     % width  -> 2 : 3 aspect
\def\flagH{4cm}     % height
\def\eyeR {1.3cm}     % HAL-eye radius


% light-blue background
\fill[UNBlue] (0,0) rectangle (\flagW,\flagH);

%--------------------------------------------------------
% concentric “HAL eye” (outer-most ring first)
%--------------------------------------------------------
\begin{scope}[shift={(\flagW/2,\flagH/2)}] % centre of the flag
  \foreach \f/\c in {%
      1.00/black,
      .68/{red!50!black},
      .43/{red!80!orange},
      .1/orange,
      .05/yellow}%
  {%
    \fill[fill=\c,draw=none] circle ({\f*\eyeR});
  }

%── parameters ───────────────────────────────────────
\def\R{\eyeR}        % distance from centre to triangle’s tip
\def\Alpha{10}       % full apex angle (°)
%── compute half-angle & half-base once ─────────────
\pgfmathsetmacro\halfA{\Alpha/2}               
\pgfmathsetlengthmacro\halfside{\R*tan(\halfA)}

%── loop over Vitruvian‐man angles ───────────────────
\foreach \Beta in {0,30,90,150,180,240,265,275,300} {%
  % apex on the eye‐rim
  \coordinate (A) at (\Beta:\R);
  % base corners offset ±90°
  \coordinate (B) at (\Beta+90:\halfside);
  \coordinate (C) at (\Beta-90:\halfside);
  % fill the spike
  \path[fill=white,draw=none] (A) -- (B) -- (C) -- cycle;
}

\end{scope}
\end{tikzpicture}
\end{document}
