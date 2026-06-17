


re how (as dmitry said) it is easy to handle non-diagonalizability in the matrix function stuff alexander was talking about at lunch today:
Let a(z)=a_0+a_1 z + a_2 z^2 + ... be a power series with radius of convergence R (i.e., R = 1 / limsup_{n\to \infty} |a_n|^{1/n}). Let a^n(z) denote the partial sum up to term n of this power series. If you plug in a matrix M which has all eigenvalues < R, then note that for any vector v, we have that a^n(M) v  = \sum_{i=0}^n a_i M^n v with each term bounded in L^2 norm by 

other idea: put in jordan normal form basis, exponentiate explicitly there. the entries of the matrix will end up being $\binom{n}{\ell}\lambda^{n-\ell}$. adding up different powers at the same entry 
$\ell$ in a block, you'll get $\sum_n a_n \binom{n}{\ell}\lambda^{n-\ell}$. note that this is like at most sum of $a_n n^{\ell}\lambda^{n-\ell}$. the nth root of this is $a_n^{1/n} \lambda \left(\frac{n}{\lambda}\right)^{\ell/n}$. since lim prod is prod lim, this has lim less than $1$, done by comparison to geom series!

## mess

suppose non-diagonalizable. perturb by a little bit to M'=M+N with very small N. this changes eigenvals by at most a little bit because polynomials have their roots changed by at most a little bit. now everything converges just fine. there is error though from a_n M^n differing from a_n (M+N)^n by some terms that have a product with N in them. when we multiply a vector into such a term M^k N M^{n-k-1}, we can eigendecompose the vector 

maybe pick M'=M+eps N instead, to make the eigenvecs of M' nice? might not work

