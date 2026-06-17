

Let $U_{ext}$ denote a matrix whose first $d$ columns are an orthonormal basis for $U$ and whose last $m-d$ columns are an orthonormal basis for $U^\perp$. Then given $d\geq (m+1)/2$, it is necessary and modulo some nontrivial assumptions sufficient for solving the problem that there be some matrix $S$ satisfying the following conditions:
* the top $d\times d$ entries in $S$ are all $0$
* $S$ is symmetric
* $u_i^T S u_i$ is (roughly) $\epsilon_i\frac{d}{m}$ (where $u_i$ denotes row $i$ of $U_{ext}$ (as a column vector))
* $\lVert S \rVert_F^2=O(\varepsilon d)$

Instead of constructing such a matrix, perhaps we can argue it exists? For a simpler problem, maybe let's just require all the signs to be right; in fact, let's condition on all the signs of $u_i^T S u_i$ being those of $\epsilon_i$, and figure out how big we can make the min abs val while keeping (say) $\lVert S\rVert_F^2=1$. Think of $S$ as living in the vector space of all $m\times m$ matrices, note that each $u_i^T S u_i$ sign condition is just saying that $S$ should be in a half-space (since it's linear in the entries of $S$); furthermore, the problem of finding the max min is the problem of finding a point of unit norm in this space which is (1) on the assigned side of each hyperplane and (2) as far as possible from the closest one and (3) in the subspace of matrices which have a $0$ top left $d\times d$ block and are symmetric. This is a subspace of dimension $m(m+1)/2-d(d+1)/2$, in which we want to find a point which is far from $m$ given hyperplanes (in the right directions).