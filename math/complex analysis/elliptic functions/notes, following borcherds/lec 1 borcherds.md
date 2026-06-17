
https://www.youtube.com/watch?v=7kPKICWkVG0

Let's consider functions which are periodic with two periods $\omega_1,\omega_2$ (because that's interesting, of course, and probably also because something something number theory, though who cares very much about number theory).

So, there are no interesting cases in real variables: if $\omega_1/\omega_2$ is rational, then the gcd is a period and it implies both are, so there's really just one period; if $\omega_1/\omega_2$ is irrational, then one can get arbitrarily close to $0$, so assuming continuity, the function must be constant.

There are interesting such holomorphic functions though! One way to construct such a function is to pick any function $g(z)$ and define $f(z)=\sum_{\lambda\in \Omega}g(z+\lambda)$, where $\Omega$ is the $\mathbb{Z}$-span of $\{\omega_1,\omega_2\}$ — well, at least given that this sum converges, $f(z)$ is indeed periodic.

Let's think about a few options for $g$ which would make it converge. Note that $g(z)=1/z^k$ certainly has it converge for integer $k\geq 2$ (one can do a counting argument to get absolute convergence); I'm guessing one can compute the derivative to show that for integer $k$, this is holomorphic except where we get division by zero, and indeed meromorphic by multiplying by the right local root power.

The $k=2$ case only barely fails to converge. One can remove the bad parts and get a nice special elliptic function $\wp$ called the Weierstrass-p-function or something. (I need to write the details here.) The proof that this is periodic uses that its derivative is periodic together with it being even.

One can then prove by a sequence of reductions to special cases (sth like other poles -> only poles at lattice -> only even poles -> div by $\wp$ to get rid of those or something) that any elliptic function can be written in terms of $\wp$ and $\wp'$. These satisfy a certain cubic equation though, so the elliptic functions are $\mathbb{C}[x,y]$ quotiented by that cubic equation. Or really it must be a quotient of this I guess? He doesn't argue that there's no other (smaller? does that make sense) relation I think?

Anyway, this also gives some map from a fundamental domain (or $\mathbb{C}/\Omega$ to the set of pts satisfying that equation, which I think is called an elliptic curve.)

There is then a question why one can't fix $1/z$ also by removing lower terms from the taylor expansion. The ans turns out to be that it has a periodic derivative but it is odd. Indeed, one can see it can't be periodic from a contour integral which is slightly shifted around a fundamental domain! Instead, each domain has the func shifted or something. But it's still some nice function with some name I think.







