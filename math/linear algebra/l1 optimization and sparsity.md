

suppose n linear equations, m>n variables. left with m-n dim affine subspace of solutions. wlog lowest l1 loss soln has all signs non-negative. has a certain set of zeros, say $k$ in total. restrict to the part of the soln subspace with these zeros, left with at least m-n-k dim subspace. as long as not 0 dim left, can move in some direction, and generically not every direction here will have coords summing to 0. but if not summing to $0$, then moving in either $v$ or $-v$ decreases l1! so l1 minimum, generically, need m-n-k<=0, so at least m-n zeros! so n non-zeros, ie num equations many nonzeros only!


# mess

suppose you have a linear system $Ax=b$ with many solutions, ie a whole affine subspace $S$ of solutions, and you look for the smallest solution in terms of $\ell^1$ norm. this will give the point in $S$ which is closest in $\ell^1$ to the origin. what does this look like? suppose the lowest $\ell^1$ point in $S$ is in a particular orthant. this is the same as specifying its signs. moving in any direction inside $S$, ie in any $v$ with $Av=0$, call this $S'$, should increase $\ell^1$. but how could this be true for both $v$ and $-v$? 

wlog the min has all signs non-negative (resign otherwise). now, there is a subspace of $S'$ made of vectors with coords that sum to $1$; this has codimension $1$ (it could also have codimension 0, though this is non-generic).

