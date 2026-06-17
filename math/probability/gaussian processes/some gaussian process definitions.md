
https://youtu.be/ckbMvhJ00tM

> Definition (Gaussian process). We say an indexed set of random variables, $X_t$ for $t\in T$, is a Gaussian process iff every finite linear combination of $X_t$ is a Gaussian random variable.

>Proposition (finite-dim gaussian description). This is equivalent to every restriction to finitely many indices being jointly Gaussian.

> Definition (canonical GP). In a canonical GP, we have vectors $v_t$ for $t\in T$ in $\mathbb{R}^I$, for $I$ finite or countably infinite, of defined $\ell_2$ norm (ie the sum of squares of coordinates of each $v_t$ converges). Let $G$ be the random vector with all coordinates independent standard gaussians, and define corresponding random variables $X_t=G \cdot v_t$. Note that $X_t$ form a GP because any linear combination of finitely many $X_t$ is a linear combination of Gaussians, which is Gaussian (hmm modulo checking some detail about the infinite sums one gets when expanding out behaving nicely — $v_t$ might not have finite support I guess? yea definitely works out though, just use the finite case, then variances converge as usual, so pdf converges to gaussian with variance equal to the infinite sum of variances). 