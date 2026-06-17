
apparently locally any isometry is up to first order $I+A$ with $A$ skew-symmetric — that is, $A=-A^T$ (e.g. mentioned in Connelly & Guest. probably can derive fairly easily just from writing down the first-order conditions the added matrix must satisfy for the sum to be orthogonal)


# when we only care about what happens to a subspace

conventions: Let's say the space is $\mathbb{R}^m$ and the subspace $U$ has dimension $d$.

Now suppose we care only about a certain subspace $U$. Then we can restrict $I+A$ to just be the same on $U$ and send everything in the orthogonal complement of $U$ to $0$. Letting $P_U$ denote the orthogonal projection to $U$, this is given by $(I+A)P_U=P_U+A P_U$. Letting $U$ also denote a matrix that has an orthonormal basis for $U$ in its columns, note that $P_U=UU^T$. So our generic operation is $P_U+AP_U=UU^T+AUU^T$. Note that $AUU^T=A'UU^T\iff AU=A'U$. (The backward implication is obvious. The forward implication comes from multiplying both sides by $U$ and dropping the small-dimensional identity matrices (which do nothing) from both sides.)  Next, note that $AU=A'U$ iff each row of $A$ has the same projection into the subspace $U$ as each row of $A'$. So, letting $C$ denote a matrix whose columns have the coeffs of


# what happens to the masses on coordinates?

The new matrix after this small motion is $U'=(I+A)U=U+AU$. The new squared mass in coordinate $i$ is $$\lVert e_i^T(U+AU)\rVert^2=\lVert e_i^T U\rVert^2+2 e_i^T U U^T A^T e_i+\lVert e_i^T AU\rVert^2.$$ 
The first term is just the initial squared mass in coordinate $i$; the last term is higher-order than the middle one since we are taking $A$ to be small. The name of the game is thus to make the middle term equal to the negative of the squared mass displacement in coordinate $i$ — let's call this initial displacement $\varepsilon_i$ — and in fact to do this for all $i$ simultaneously while keeping $A$ small. One can collect these $m$ constraints into the one constraint that the $m\times m$ matrix $-2 U U^T A^T=2P_U A$ has $\varepsilon_1,\ldots,\varepsilon_m$ along its diagonal. 

We can expand each column of $A$ as a sum of something in $U$ and something in $U^\perp$: let this be given by $A=A_U+A_{U^\perp}$. Then the condition above is just that $A_U$ has $\varepsilon_1,\ldots,\varepsilon_m$ along its diagonal, and we still additionally need $A_U+A_{U^\perp}$ to be skew-symmetric and small. In the Paulsen problem, the notion of smallness that matters is the Frobenius norm of the difference matrix, i.e. $\lVert U'-U\rVert_F^2=\lVert AU\rVert_F^2=\lVert -A^T U \rVert_F^2=\lVert A_U \rVert_F^2$, and so we'd ideally show that $\lVert A_U \rVert_F^2=O(\varepsilon d)$. In summary, we just need two things:
1) We need to find a $m\times m$ matrix $A_U$ with columns in $U$ with diagonal terms $\varepsilon_1,\ldots,\varepsilon_m$ and $\lVert A_U \rVert_F^2=O(\varepsilon d)$.
2) We simultaneously need to find a $m\times m$ matrix $A_{U^\perp}$ with columns in $U^\perp$ such that $A_U+A_{U^\perp}$ is skew-symmetric.

Can we even get the first condition? We know that the absolute values of $\varepsilon_i$ sum to $O(\varepsilon d)$. In fact, at least given we didn't pass to the complement, we know that for each $i$, we have $|\varepsilon_i|\leq \varepsilon \frac{d}{m}$. Just to make a heuristic calculation here: if we could make all entries of $A_U$ have about the same scale, then we'd have $\lVert A_U\rVert_F^2= m^2 \varepsilon^2 d^2/m^2=\varepsilon^2 d^2$.

In which conditions will we be able to find $A_{U^\perp}$? The condition that each column of $A_{U^\perp}$ is in fact in $U^\perp$ is given by $d$ linear equations on its entries, for a total of $md$ linear equations on its entries. Having fixed $A_U$, the condition that $A_U+A_{U^\perp}$ be skew-symmetric gives $m+(m-1)+\cdots+1=m(m+1)/2$ linear equations. Since we have $m^2$ variables, absent a conspiracy, we will be able to find a $A_{U^\perp}$ given that we have more variables than linear equations, i.e., given that $m^2\geq md+m(m+1)/2$, which is iff $m\geq d+(m+1)/2$, which is iff $d\leq \frac{m-1}{2}$. Given this constraint vs variable counting works out, we can probably rule out a conspiracy here by taking some small perturbation of any conspiratorial $A_U$ without messing up the other stuff too much? We might need to eventually be careful here so as to not make the quadratic term dominate though.  

Given that $U$ has squared mass at least $(1- \varepsilon)d/m$ on every coordinate and total mass $d$, for each coordinate $i$, it must contain a vector which has at least a $(1-\varepsilon)/m$ fraction of its squared mass on that coordinate (otherwise pick orthonormal basis, if every vec fails this property, then contradiction with mass distribution). Putting multiples of these as the respective columns of $A_U$, we get squared mass at most $O(m \varepsilon_i^2)$ in column $i$, so total squared mass $O(m \sum_{i=1}^m \varepsilon_i^2)$. Given we haven't passed to the complement, this is $O(m^2 \varepsilon^2 d^2/m^2)=O(\varepsilon^2 d^2)$. 

## mess

One option here for constructing a solution would be to try to make $A_U$ the smallest matrix which has 

So the question of describing the set of all ways of moving around $U$ is the same as the question of 

