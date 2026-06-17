
$A(n,\theta)$ is the max number of points with pairwise angles from the center $\geq \theta$ on the unit sphere $S^{n-1}$. 
# Connection to sphere packing

Kabatiansky and Levenshtein 1978

suppose we have a sphere packing (with spheres of radius $1$) with density $\Delta$ in $\mathbb{R}^n$ (ie $\Delta$ is the limiting volume ratio, covered volume vs all). We will pick another sphere of radius $R\leq 2$ in $\mathbb{R}^n$ to consider. By an averaging argument, there exists such a sphere containing $\Delta R^n$ centers of spheres in the packing + such that the center is not one of them. Take this particular sphere and project all the sphere centers from the packing to the surface of the sphere. A 2d geometry argument shows that this gives a spherical code with $\theta$ such that $\sin (\theta/2) = 1/R$. And thus the number of points in this sphere must be $\leq A(n,\theta)$, so we get $\Delta R^n = \leq A(n,\theta)$, so $\Delta \leq A(n,\theta)\sin(\theta/2)^n$. 

the 2d geometry argument:
![[Pasted image 20230930133535.png]]



let's now consider the case of what should be like 4n vecs, with dot prod of some pair at least eps = 1/(4 sqrt(n)), let's say.

then cos(angle) = 1/(4sqrt(n))
sin(angle) is approx 1-1/(32n)
whatever. don't need this, already done below. the bound is that the num of vecs is at most $e^{n\frac{\varepsilon^2}{2}\log\frac{2}{\varepsilon^2}}=(32n)^{1/(32)}$ . i guess this is wrong because really the bound is not an inequality, just a $\lesssim$, so only true up to some const, and the const  

v_i dot v_j < eps

is the same as cos (angle) < eps 

is the same as sin angle > sqrt(1 - eps^2) 

this is approx 1-eps^2/2

let $y_{\pm}= \frac{1\pm \sin \theta}{2 \sin \theta}$


oops should replace eps^2 with like eps^2/2 in everything below but whatever

so $y_+= \frac{2+\varepsilon^2}{2-2\varepsilon^2}\approx (1+\varepsilon^2/2)(1+\varepsilon^2)\approx 1+\frac{3}{2}\varepsilon^2$

so $\log y_+\approx \frac{3}{2}\varepsilon^2$ 

and $y_-=\frac{\varepsilon^2}{2-2\varepsilon^2}\approx \frac{\varepsilon^2}{2}\left(1+\varepsilon^2\right)$

$\log y_-\approx \log \frac{\varepsilon^2}{2}$

$


let $y_{\pm}= \frac{1\pm \sin \theta}{2 \sin \theta}$
https://arxiv.org/pdf/1212.5966.pdf says 
$\log A(n,\theta)/n\lesssim \left(y_+ \log y_+ - y_-\log y_-\right)$
second term dominates for small eps, is like $\log \frac{2}{\varepsilon^2} \frac{\varepsilon^2}{2}$
so same shape of bounds!
tmr: figure out how the construction of g works, and see if can be used to lower boudn tms loss


1/n log A(n,theta) <= 1+sin theta / (2 sin theta) log 1+sin theta / (2 sin theta) - 



# The upper bound on $A(n,\theta)$

The bound uses a particularly cleverly chosen auxiliary function. We say $f\colon [-1,1]\to \mathbb{R}$ is positive-semidefinite (for the sphere $S^{n-1}$) if for all $m$ and all vectors $w_1,\ldots, w_m\in S^{n-1}$, the matrix whose $ij$ entry is $f(w_i\cdot w_j)$ is positive-semidefinite. This is equivalent to requiring that $\sum_{i,j} t_i t_j f(w_i \cdot w_j)\geq 0$ for any vectors $w_1,\ldots, w_m$ on the unit sphere and any coefficients $t_1,\ldots, t_m\in \mathbb{R}$. By Riemann sums, this implies also that for any measure $\nu$ on $S^{n-1}$, we have $\iint f(x\cdot y) d\nu(x) d\nu(y)\geq 0$. Now the trick is to choose a measure $\nu$ here that captures a vector configuration on the sphere and an auxiliary function $f$ which interacts nicely with the property that all pairwise angles are less than $\theta$. We choose continuous positive-semidefinite $f\colon [-1,1]\to \mathbb{R}$ with $f(t)\leq 0$ for all $t\in [-1,\cos\theta]$ but the expectation of $f(x\cdot y)$ with $x,y$ chosen independently uniformly at random from $S^{n-1}$, let's call this $\overline{f}$ (or just one chosen uniformly at random of course gives the same), being positive. We will use this to bound $A(n,\theta)\leq \frac{f(1)}{\overline{f}}$. To prove this, for the given vec configuration $W=(w_1,\ldots,w_m)$, we pick $\nu = \sum_{i} \delta_{w_i}+a \mu$, where $\delta_{w_i}$ is a point mass at $w_i$, where $\mu$ is the uniform distribution, and the coefficient $a$ is to be chosen later. Then just consider $0\leq \iint f(x\cdot y) d\nu(x) d\nu(y)$. Can split each $\nu$ as a sum of the deltas and the uniform distribution, this gives $4$ integrals. Uniform against uniform just gives $a^2 \overline{f}$. Uniform against deltas gives $m a \overline{f}$, twice since there are two ways to split. Deltas against deltas give $0$ cross terms because of the angle condition, so we are just left with each delta against itself, giving $m f(1)$. Putting this together, we have $a^2 \overline{f}+2m a \overline{f}+mf(1)\geq 0$. Turns out that this gives the best bound on $m$ if we pick $a=-m$, in which case this becomes $-m^2 \overline{f}+mf(1)\geq 0$, from which $m\leq \frac{f(1)}{\overline{f}}$. 

since (it nontrivially turns out) that continuous psd functions are precisely the non-negative linear combinations of something called Gegenbauer polynomials (don't ask me for the definition), choosing the optimal $f$ is sort of "just" some linear programming problem (one can treat the $\overline f$ part as just a normalization constant and then it comes down to minimizing $f(1)$ subject to a bunch of constraints)


# Caveats
I still don't know any good bound for $\sum_{i,j} \mathrm{Relu}(w_i\cdot w_j)^2$ though!
