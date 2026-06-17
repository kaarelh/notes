


\begin{itemize}
    \item Let $V$ be a uniformly random $k$-dimensional subspace of $\mathbb{R}^n$.\footnote{Concretely, pick $k$ vectors independently uniformly at random from $S^{n-1}\subseteq \mathbb{R}^n$ and let $V$ be their span. (Or, equivalently, let the coordinates of these vectors be i.i.d. gaussians.) In case this isn't formal enough for you --- I mean that the probability measure is the uniform measure on the Grassmannian $\mathrm{Gr}_k(\mathbb{R}^n)$: \url{https://en.wikipedia.org/wiki/Grassmannian\#Associated_measure}} What's the probability that $V$ contains a vector all of whose coordinates are positive?
    \item Take the standard hyperoctahedron in dimension $n$.\footnote{The standard hyperoctahedron in dimension $n$ is the convex hull of the standard basis and its reflection across the origin, i.e., with $e_1,\ldots,e_n$ being the standard basis, the convex hull of the $2n$ vectors $\pm e_1,\pm e_2,\ldots, \pm e_n$.} Slice through it with a random $k$-dimensional subspace; the shadow it leaves on the subspace is a $k$-dimensional polytope. How many faces of each dimension does this polytope have?
    \item What's the probability that the convex hull of $\ell$ random vectors in $\mathbb{R}^m$ contains the origin?\footnote{This is a generalization of 1992 Putnam A6, \url{https://kskedlaya.org/putnam-archive/1992.pdf}, which asks for the probability that $4$ vectors in $\mathbb{R}^3$ have the origin in their convex hull; 3Blue1Brown has a video on that problem: \url{https://youtu.be/OkmNXy7er84}.}
    \item What's the expected fraction of the unit sphere $S^{m-1}\subseteq \mathbb{R}^m$ to lie in the positive cone spanned by $\ell$ random vectors?
    \item Take $\ell_b$ random blue vectors and $\ell_r$ random red vectors in $\mathbb{R}^m$. What's the probability that there is a hyperplane through the origin with all red vectors on one side and all blue vectors on the other?
\end{itemize}


prob that convex hull contains origin (3b1b putnam problem), prob that positive cone contains origin, prob that all pts in some common half-space, prob that $n$ random blue and $m$ random red points can be separated with a hyperplane through the origin (the trick here is to note that this is equivalent to the blue and reflections of red pts being on the same side of a hyperplane)
