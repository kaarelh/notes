
> Proposition. The product of singular values of a $m\times n$ matrix $M$ with $m>n$ (i.e., a tall rectangular matrix) is the $n$-volume of the [parallelepiped](https://en.wikipedia.org/wiki/Parallelepiped#Parallelotope) defined by the $n<m$ columns of $M$ in $\mathbb{R}^m$.

Pf. Consider the singular value decomposition $M=U\Sigma V^T$.  Since $U$ acts on $\mathbb{R}^m$ as an isometry, the $n$-volume of the parallelepiped defined by the $n$ columns of $\Sigma V^T$ in $\mathbb{R}^m$ is the same as the $n$-volume of the parallelepiped defined by the $n$ columns of $M$ in $\mathbb{R}^m$. Note that $\Sigma V^T$ is just $V^T$ with row $i$ rescaled by $\sigma_i$, with the bottom $m-n$ rows being just $0$s. So this parallelepiped lives in the standard $\mathbb{R}^n$ inside $\mathbb{R}^m$, and its $n$-volume is the same as the $n$-volume of the parallelepiped in $\mathbb{R}^n$ defined by the top $n\times n$ submatrix of $\Sigma V^T$. Since transposes have equal determinants, this is the same as the $n$-volume of the parallelepiped defined by the columns of its transpose — and since these columns are orthogonal with norms $\sigma_1,\ldots,\sigma_n$, this volume is just $\prod_{i=1}^n \sigma_i$. 



> Theorem. Let $M$ be $m\times n$ with $m>n$ and each entry an independent $\mathcal{N}(0,\sigma^2)$. The product of singular values of $M$ is distributed as $\sigma^n \prod_{k=0}^{n-1}\sqrt{\sum_{i=1}^{m-k} Y_{k,i}^2}$, where $Y_{k,i}$ are independent $\mathcal{N}(0,1)$. Equivalently, it is distributed as $\prod_{k=1}^{n}\chi_k$, with each $\chi_k$ denoting an independent [chi-distributed](https://en.wikipedia.org/wiki/Chi_distribution) random variable with $k$ degrees of freedom.

Pf. We will sample $M$ column-by-column, letting $c_k$ denote column $k$. Let $\ell_k$ denote the length of the projection of $c_{k+1}$ to the orthogonal complement of $c_1,c_2,\ldots, c_k$. Since the gaussian distribution is invariant under picking a different orthonormal basis, we might as well sample $c_{k+1}$ in an orthonormal basis which has its first $m-k$ elements being an orthonormal basis for the orthogonal complement of the span of $c_1,\ldots, c_k$. Denoting of the sampled vector on these $X_{k,1},X_{k,2},\ldots, X_{k,m-k}$, we have $\ell_k=\sqrt{\sum_{i=1}^{m-k} X_{k,i}^2}$. By the proposition above, the product of singular values of $M$ is $\prod_{k=0}^{n-1} \ell_k = \prod_{k=0}^{n-1}\sqrt{\sum_{i=1}^{m-k} X_{k,i}^2}$. 



> Proposition. Given $m>n \log^k n$ (where $k$ is like $2$; I haven't computed a precise $k$ but some small $k$ would drop out of the argument below), let $M$ be an $m\times n$ matrix with each entry an independent $\mathcal{N}(0,1)$, then with probability $1-o_{n\to\infty}(1)$, the product of singular values of $M$ is $(1\pm o_{n\to\infty }(1))n^{-n/2}\prod_{k=0}^{n-1} \sqrt{m-k}$.  

A very messy proof-like object.
the index $k$ term in the product has expectation $m-k$ and standard dev of order $\sqrt{m-k}$. at least heuristically and probably rigorously modulo some large deviation thing working, whp for all $k$ at once the index $k$ term will be in the range $\sqrt{m-k\pm \log k\sqrt{m}}$. the square prod will thus whp be between $\prod (m-k-\log k \sqrt{m})$ and $\prod (m-k+\log k \sqrt{m})$ which is $(1\pm \sqrt{\log k/m})^n\prod m-k$, which is $e^{\pm n \sqrt{\log k/m}}\prod m-k$ which is not great! this is a worst bound though that has all the errors going in the same direction, whereas really the errors are independent. let's try to do better
the log of the prod of singular values of $M$ is distributed as $n\log \sigma + \frac{1}{2}\sum_{k=0}^{n-1}\log\left(\sum_{i=1}^{m-k} Y_{k,i}^2\right)$.  By independence, the variance of this is $\frac{1}{4}\sum_{k=0}^{n-1}\mathrm{Var}\left(\log\left(\sum_{i=1}^{m-k} Y_{k,i}^2\right)\right)$ 
what if we cut off some crap that's too small first, and only then compute this variance? like it's fine to truncate every sum to be in the range $\sqrt{m-k\pm \log k\sqrt{m}}$, and to only then compute this variance (just take the L if it isn't in fact in this range). in this small range, the log is essentially a linear function with slope $1/m$, so the var of the log is roughly just $1/m^2$ the var of the sum, which is $m$. so then we end up with a sum of n terms of var 1/m, for a total var of $n/m$, which can be made $o(1)$. this gives a bound, but i guess also it could totally happen that this log overall is n log sigma + sqrt{n/m}/2. in our case, sigma = 1/sqrt{n}, so this is  
in conclusion, up to some const multiplicative factor, the prod of singular values is $n^{-n/2}\prod_{k=0}^{n-1}\sqrt{m-k}$, which is $$m^{n/2}n^{-n/2}\prod_{k=0}^{n-1}\sqrt{1-k/m}\approx m^{n/2}n^{-n/2} e^{-\sum_{k=0}^{n-1}k/(2m)}= m^{n/2}n^{-n/2} e^{-n(n-1)/(4m)}.$$


## the prod of eigenvals of the gram matrix

really the gram matrix has a 1/m factor in front, and we care about the product of its eigenvalues i guess? this should be the square of the prod of sing vals of the gaussian matrix scaled by 1/sqrt{m}. this just scales all sing vals by 1/sqrt{m}. so we get the prod of all eigenvals of the gram matrix to be 

$n^{-n} e^{-n(n-1)/(2m)}=e^{-n(\log n +(n-1)/(2m))}$
the log of this is $-n (\log n +o(1))$ 

up to a const additive term, the log is $-n \log n-n^2/2m$ 

now suppose we have some loss min with these second derivatives in each direction. the loss is less than $\varepsilon$ in the ellipsoid defined by $\lambda_1 x_1^2+\cdots + \lambda_n x_n^2\leq \varepsilon$, which can be obtained by starting from a usual ball defined by $\sum_i x_i'^2\leq \varepsilon$ by $x_i=x_i'/\sqrt{\lambda_i}$. This scales volume by $\prod_i 1/\sqrt{\lambda_i}$. The volume of the original ball is that of a ball of radius $\sqrt{\varepsilon}$, which is $\sqrt{\varepsilon}^n$ times the volume of a unit ball in $\mathbb{R}^n$, call that $V_n$. So the volume of the region where loss is $\leq \varepsilon$ is $\left(\prod_i 1/\sqrt{\lambda_i}\right)\sqrt{\varepsilon}^n V_n$ 



# scrap

Let $V_k$ denote the $k$-volume of the parallelepiped defined by the first $k$ columns, and let $\ell_k$ denote the length of the projection of $c_k$ to the orthogonal complement of $c_1,\ldots, c_{k-1}$. We then have $V_0=0$ and for $1\leq k \leq n$, we have $V_{k+1}=V_{k-1}\ell_k$. Note that 

p(X>q) q <= E[X]
p(e^{tX} > q) e^{tq} <= E[e^{tX}]
p(prod>q)  q <= E[prod]= prod E[Z_i]

have the trace pinned down, so we have an upper bound from am gm, just need a lower bound also?