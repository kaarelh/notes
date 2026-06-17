simplex given by origin and vecs $v_1,\ldots,v_n$

The n-parallelotope with these vecs has volume $\det V$, where $V$ is the matrix with rows $v_1,\ldots,v_n$. We can pick a point uniformly at random from the parallelotope by picking $t_1v_1+\cdots+t_n v_n$ with the coefficients $t_1,\ldots,t_n$ uniformly at random from the unit interval each (basically this works because volume squishing factor is the same at all pts for the map from the cube into the parallelotope I guess, namely $\det V$). Now the probability to be in the simplex is the same as the probability that $\sum t_i\leq 1$, which we argue below is $\frac{1}{n!}$. Thus, the volume of the simplex must be $\frac{\det V}{n!}$. 

Here are some ways to compute that this is $\frac{1}{n!}$: 
1) do basically riemann sum instead, ie instead of picking real numbers, pick $n$ integers $\leq m$, and ask that sum is $\leq m$ also. Solve the standard combinatorics problem, and take a limit $m\to \infty$.
2) Do the linear transformation $t_1,t_2,\ldots,t_n\mapsto t_1, t_1+t_2,\ldots,t_1+\cdots +t_n$. The set $\sum t_i\leq 1$ maps bijectively under this to the set $0\leq x_1 \leq \cdots \leq x_n\leq 1$. (Actually I guess this is better because one could/would solve the combo problem this way anyway maybe.) Since this is given by a triangular matrix with $1$s along the diagonal, the determinant of this linear map is $1$, so these have the same volume. And then note that the latter set has volume $\frac{1}{n!}$ because the probability of $n$ numbers to be in any one particular order is $\frac{1}{n!}$. 
3) just do base volume times height over $i$ a bunch of times!

source for the last paragraph: https://math.stackexchange.com/a/1718038