
Actually, i think this statement (let me call it Claim 1) implies a wynerian theorem characterizing when coding is possible at a tuple of rates in terms of test channels. Here's the claim it implies:

Claim 2. One can do Shannon condensation at rates $(r_1,\ldots,r_k)=\vec{r}$ with $r_1+\cdots+r_k=H(X)$ iff for each of the $k!$ permutations $\sigma$ of the channel indices, one has a test channel with independent $Y_1,\ldots,Y_k$ such that $$I(Y_{\sigma(1)};X)\leq r_{\sigma(1)},\quad I(Y_{\sigma(1)},Y_{\sigma(2)};X)\leq r_{\sigma(1)}+r_{\sigma(2)},\quad \ldots\quad I(Y_{\sigma(1)},...,Y_{\sigma(k)};X)\leq r_{\sigma(1)}+\cdots+r_{\sigma(k)}.$$
(The random variables $Y_1,\ldots,Y_k$ are allowed to be different for different permutations.)

Pf of Claim 2 (assuming Claim 1 (which could still turn out to be false)).

One direction is easy: if coding is possible at this rate tuple, then one just applies Claim 1 with each ordering to get collections of random variables satisfying the desired mutual info bounds.**

It remains to show the converse: that if there are these $k!$ test channels, then there is a coding scheme with the given rates $\vec{r}$. Claim 1 says that for each permutation $\sigma$, there is a coding scheme at rates $\vec{r}_\sigma$ where $\vec{r}$ majorizes ( https://en.wikipedia.org/wiki/Majorization ) $\vec{r}_\sigma$ wrt the ordering $\sigma$. Note that one can combine these coding schemes at rates $\vec{r}_\sigma$ to get any rate vector in their convex hull, so it suffices to show that $\vec{r}$ is in the convex hull of the $k!$ vectors $\vec{r}_\sigma$. This is a sorta cool linear algebra fact.

** a technicality: To make the index trick work out in the proof of Claim 1, I think one needs the first channel to always be the one that's seen by everyone. One should really modify Claim 2 to only have a universal quantifier over the $(k-1)!$ permutations which have the common index first. I'll just ignore this when proving the converse, even though this means it's technically the wrong converse. I think this can be fixed by noticing that one can always assume WLOG that the first bound is saturated by any coding scheme, since we can always move information up from any other channel to the one seen by everyone.


Linear algebra fact. Let $v\in \mathbb{R}^k$ and say we have $k!$ vectors $v_\sigma$, one for each permutation $\sigma\in S_k$, such that for each $\sigma$, we have that $v$ majorizes $v_\sigma$ wrt the ordering $\sigma$. Then $v$ is in the convex hull of the $v_\sigma$.

Pf. WLOG $v=0$ (else translate all vectors by $-v$). If $v=0$ is not in the convex hull of the $v_\sigma$, then by a hyperplane separation theorem, there must be a hyperplane strictly separating the origin from the convex hull of the $v_\sigma$, say with normal vector $u$. Then $u\cdot v_\sigma > 0$ for all $v_\sigma$. WLOG $u$ has non-increasing coordinates, ie $u_1\geq u_2\geq \cdots \geq u_k$ (else permute coordinates first). Now we have $u\cdot v_{id}\leq 0$ — decompose $u$ as vector with $u_k$ at all coords plus a vector that is $0$ at the last coord and is const $u_{k-1}-u_k$ at the first $k-1$ coords, and so on, until a vector that is $0$ at the last $k-1$ coords and $u_1-u_2$ at the first coord; multiplying $v_{id}$ into each of these components contributes something $\leq 0$ by being majorized by $v=0$ — a contradiction. So $v=0$ is in the conv hull of the $v_\sigma$.


when going from coding to random variables, we really get all the inequalities — for every collection at once, we have that I(that collection; X) is at most the sum of rates. 

when going from random variables to coding, we could also do all permutations at once — just split into batches, coding according to a different ordering in each batch. this gives r_i as the average of I(Y_i;X|Y_1,...,Y_{i-1}) across all permutations, which is a sort of shapley mutual information.

for an arbitrary collection, we get that the sum of rates is at most the sum of these shapley mutual informations. but i guess I(that collection; X) might be smaller than the sum of rates? well, by joint independence of the Y_i, we do have that I(a collection;X|a disjoint collection) >= I(the collection; X). unfortunately this is in the other direction

when going from coding to random variables, i guess there is no hope to get


joint mutual infos >= rate sums
rate sums >= joint mutual infos

so certain joint mutual infos work iff certain rate sums work? what's wrong?

q: what's the highest attainable utility at given rates
given coding at the given rate sums, one can get random variables with at most these joint mutual infos.
and given random variables with at most these joint mutual infos, one can get coding at these rate sums. but maybe not at these rates i think. this is why we don't get an iff i guess?


a small improvement on something i already said yesterday: (if true,) this characterizes when one can do shannon condensation at a certain rate r_k in the top latent, r_{k-1} total in the size k-1 latents, ..., r_1 total in the singletons, in the case that sum_i r_i = H(X). one can replace the inequalities at layer endings with equalities for condensation
