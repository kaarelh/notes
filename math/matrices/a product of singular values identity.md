a different worse argument: https://math.stackexchange.com/questions/1419275/volume-of-a-n-d-parallelepiped-with-sides-given-by-the-row-vectors-of-a-matrix

Theorem. The product of singular values of a $m\times n$ matrix $M$ with $m>n$ (i.e., a tall rectangular matrix) is the $n$-volume of the [parallelepiped](https://en.wikipedia.org/wiki/Parallelepiped#Parallelotope) defined by the $n<m$ columns of $M$ in $\mathbb{R}^m$.

Pf. Consider the singular value decomposition $M=U\Sigma V^T$.  Since $U$ acts on $\mathbb{R}^m$ as an isometry, the $n$-volume of the parallelepiped defined by the $n$ columns of $\Sigma V^T$ in $\mathbb{R}^m$ is the same as the $n$-volume of the parallelepiped defined by the $n$ columns of $M$ in $\mathbb{R}^m$. Note that $\Sigma V^T$ is just $V^T$ with row $i$ rescaled by $\sigma_i$, with the bottom $m-n$ rows being just $0$s. So this parallelepiped lives in the standard $\mathbb{R}^n$ inside $\mathbb{R}^m$, and its $n$-volume is the same as the $n$-volume of the parallelepiped in $\mathbb{R}^n$ defined by the top $n\times n$ submatrix of $\Sigma V^T$. Since transposes have equal determinants, this is the same as the $n$-volume of the parallelepiped defined by the columns of its transpose — and since these columns are orthogonal with norms $\sigma_1,\ldots,\sigma_n$, this volume is just $\prod_{i=1}^n \sigma_i$. 



