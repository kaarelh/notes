## A bit on extremal configurations of vectors in high dimensions, with an eye toward feature reconstruction a la toy models

Throughout this, we will be assuming that we have a set $F=\{v_1,\ldots,v_m\}\subseteq \R^n$ — in words, a set of $m$ vectors in $\R^n$, typically with $m>n$ — and supposing it is, roughly speaking, spread out well in space — a physicist might say that $F$ is a *low-energy configuration*. This presentation aims to provide a better understanding of such configurations both by considering some constructions of such configurations and by understanding what this says about $F$ — in particular, how this bounds the size of $F$
In analogy with Toy Models of Superposition, we will call these *features*. We take the canonical motivating example to track across this talk from there as well: we assume there is a huge number of vectors $x\in \R^m$, each with most entries being $0$, but a small number of $1$'s; our task is to find a linear map (i.e., weight matrix) $W\colon \R^m\to \R^n$ such that $\mathrm{Relu}(W^T W x+b)\approx x$ — that is, minimizing $\left(\mathrm{Relu}(W^T W x+b)- x\right)^2$. We restrict to the case where there is no bias, all features have norm $1$, take the sparse limit where almost all inputs are only have $0$ or $1$ nonzero entries, and in fact assume that any nonzero entry of the input $x$ is $1$. Denoting the $i$th column of $W$ as $v_i$, the loss minimization problem then reduces to picking a set of features $F=\{v_1,\ldots,v_m\}$ such that $\sum_{(i,j)\text{ s.t. } i\neq j} \mathrm{Relu}\left(v_i \cdot v_j\right)^2$ is minimal. The point of this talk is do some cool math related to this problem — mostly, to share some cool math tricks to know, but also to 

The two main goals of this presentation are (1) to get some cool math into your head and (2) to understand some aspects of feature representation a bit better.

has to be stored in superposition in $\R^n$ with $n\leq m$. But really, this will just be a talk about feature geometry with individual examples and mathematical constraints motivated by Toy Models, but not defined in terms of it. (In the sense that we formally start from certain mathematical setups and only justify connections to e.g. the feature reconstruction setup in Toy Models of Superposition in passing.)

(This is an expanded version of a stackexchange answer by Timothy Gowers.)
List these options, then ask for guesses what the bounds will be like.
Bound on the number of vectors with pairwise $\leq -\epsilon$ dot product (perfect reconstruction (even without bias) + robust to noise)
Note that $0\leq \left(\sum v_i\right)^2=m+\sum_{(i,j)\text{ s.t. }i\neq j} v_i\cdot v_j$. If all the dot products are $\leq -\epsilon$, then we have a contradiction when $\binom{m}{2}\epsilon\geq m$, which happens at $m=\Theta(\frac{1}{\epsilon})$. So $m$ is constant in $n$. (Obviously one can also construct something with a constant number of vectors, and let's ignore the dependence on $\epsilon$.)


Bound on the number of nonzero vectors with pairwise $\leq 0$ dot product (perfect reconstruction without bias). Ans $\leq 2n$ 
Let's prove this by induction on $n$. Take the first vector, consider all other ones in basis where first coordinate is this one. All of them have negative first coordinate then, from which it follows that the parts at other coordinates also have negative dot product. At most one vector can be $0$, so left with $2(n-1)$ nonzero vectors with $\leq 0$ dot product in $\R^{n-1}$. 

Bound on the number of vectors with pairwise $\leq \epsilon$ dot product (from Tao's post + construction with volume argument or with random + Chernoff)

Kabatjanskii-Levenstein bound. Suppose all $v_i\cdot v_j\leq A n^{-1/2}$, with $\frac{1}{2}\leq A\leq \frac{1}{2}\sqrt{n}$. Then we have $m\leq \left(\frac{Cn}{A^2}\right)^{CA^2}$ for some absolute constant $C$.

Lemma. Let $v_1,\ldots,v_m\in \R^n$ be unit vectors such that $(v_i\cdot v_j)\leq \frac{1}{2\sqrt{n}}$ for all pairs $i \neq j$. Then $m<2n$.
Consider the Gram matrix for this set of vectors, i.e., the $2n\times 2n$ matrix $M$ with $M_{ij}=v_i\cdot v_j$. Since $M=W W^T$, is symmetric and has rank $\leq n$, it has an orthonormal basis of eigenvectors with $n$ associated eigenvalues being $0$, so $A=M-I$ has the same orthonormal basis of eigenvectors for which at least $n$ eigenvalues which are $-1$. Computing Frobenius norms of $A$ in the usual basis and this eigenbasis gives $$\sum_{(i,j)\text{ s.t. }i\neq j} (v_i\cdot v_j)^2\geq \sum_{k=1}^n (-1)^2=n,$$

Suppose have $2n$ such vectors, consider Gram matrix, get contradiction.

Corollary. Let $k$ be a natural number, and let $v_1,\ldots,v_m\in \R^n$ be unit vectors s.t. $(v_i\cdot v_j)\leq 2^{-1/k}\binom{n+k-1}{k}^{-1/2k}$ for all pairs $i\neq j$. Then $m<2\binom{n+k-1}{k}$. 

Proof. Consider the tensor power $\left(\R^n\right)^{\otimes k}=\R^{n^k}$. Consider the subspace $U$ of all vectors which are symmetric (under any permutation of the $k$ indices appearing in the tensor product) — it is spanned by the symmetrizations of tensors of the form $e_{i_1}\otimes e_{i_2}\cdots\otimes e_{i_k}$ for various increasing sequences $1\leq i_1\leq\ldots\leq i_k\leq n$, which are equivalent to choosing a sequence of $n-1$ stars and $k$ bars, so the dimension of $U$ is $\binom{n+k-1}{k}$. Now consider the vectors $v_1^{\otimes k},\ldots, v_m^{\otimes k}$, noting that $v_i^{\otimes k}\cdot v_j^{\otimes k}=\sum_{\ell_1,\ldots,\ell_k} v_{i,\ell_1}\cdots v_{i,\ell_k}v_{j,\ell_1}\cdots v_{j,\ell_k}=(v_i\cdot v_j)^k\leq \frac{1}{2\sqrt{n}}$. 

Choosing $k=CA^2$ for sufficiently large $C$ yields the theorem.





Choose $A=\epsilon \sqrt{n}$ in Kabatjanskii-Levenstein, then have $m\leq \left(\frac{C}{\epsilon^2}\right)^{C\epsilon^2 n}\leq C'^{\log (1/\epsilon) \epsilon^2 n}$. Using the construction which has $\pm \frac{1}{\sqrt{n}}$ as each coordinate, we have a sum of $\pm\frac{1}{n}$. This being $\geq \epsilon$ has probability $k^{-\epsilon^2 n}$ by Chernoff. Union bound tells us that for $m$ vectors, the probability that some pair has at least this dot product is at most $\binom{m}{2}k^{-\epsilon^2 n}$, which lets us make $m=k'^{\epsilon^2 n}$, so $\epsilon^2$ is in fact the correct dependence for the exponent. In the continuous case, one could also think of this as being about areas of spherical caps — sort of sphere packing — and that argument also works, but I think the spherical cap areas are a bit more annoying to compute.




## Characterizing optima of the toy models loss if bias is $0$, all features have length $1$, and all inputs are $1$-sparse

From Anthropic, the loss is then just $f=\sum_{(i,j) \text{ s.t. }i\neq j} \mathrm{ReLU}(v_i \cdot v_j)^2$. For each $i$, we have the constraint $g_i=||v_i||^2=1$, making the set of all points in $\left(\mathbb{R}^n\right)^m$ satisfying all the constraints $S^{n-1}\times \cdots\times S^{n-1}$, with $m$ terms in the product

we start by computing the gradients $\nabla f$ and $\nabla g_i$. The entries of $\nabla f$ are
$$\frac{\partial f}{\partial v_{ik}}= \sum_{j \text{ s.t. }j\neq i} 2\mathrm{Relu}(v_i\cdot v_j) v_{jk}$$
The corresponding entry of $\sum_i \lambda_i \nabla g_i$ is $2 v_{ik}$. The terms for a particular index $i$ fit together in a vector equation as follows:
$$\lambda_i v_i=\sum_{j\text{ s.t. }j\neq i} \mathrm{Relu}(v_i\cdot v_j) v_j.$$


## Bounds on $\sum_{i\neq j} (v_i\cdot v_j)^2$ (and maybe we'll say a bit about  $\sum_{i\neq j}\mathrm{Relu}(v_i\cdot v_j)^2$ also)

We already showed that if $m=2n$, then this sum is at least $n$, so the average dot product is at least $\frac{n}{\binom{2n}{2}}\geq \frac{1}{2n}$. This is actually true for all $m\geq n$ because we can pick a random pair of vectors by restricting to a subspace of dimension $2n$ and then picking a pair in it.

To get a construction, let's compute the value of this for uniformly random vectors. Note that $\mathbb{E}[(u\cdot v)^2]$  is the same as $\mathbb{E}[(u\cdot e_1)^2]$ because of symmetry, which is the same as $\mathbb{E}[(u\cdot e_i)^2]$ for any $i$. Note that  $\sum_i \mathbb{E}[(u\cdot e_i)^2]=\mathbb{E}[\sum_i (u\cdot e_i)^2]=\lVert u\rVert=1$, so symmetry implies $\mathbb{E}[(u\cdot e_i)^2]=\frac{1}{n}$. So there's this factor of $2$ gap between this and the lower bound. 

In fact, any tegum product of components which are 'symmetric' and all have the same number of vectors in each subspace gives the same value for this. (Here, symmetric means that all singular values of the data matrix are the same, but this is implied for instance by there being a symmetry of the configuration for which there is unique subspace of dimension $1$ fixed, and also there being a symmetry taking any vector to any other vector.)

Conditional on a configuration being symmetric, being better according to the relu loss is just about pushing mass behind the relu horizon.

We'd actually care about the Relu case, but this argument doesn't work. I'm relatively sure that 


## A lower bound on $\sum_{i\neq j}\mathrm{Relu}(v_i\cdot v_j)^2$

We will now move on from thinking about 

We will start by proving that for any $m\geq 2n$, we have $\frac{\sum_{(i,j)\text{ s.t. }i\neq j} (v_i \cdot v_j)^2}{\binom{m}{2}} \geq \frac{n}{\binom{2n}{2}}$. Note that the goal is to show that for any configuration of $m$ vectors, if we choose a pair uniformly at random, the expected squared dot product is at least $\frac{n}{\binom{2n}{2}}$. In fact, it suffices to prove this for $m=2n$ vectors, for the following reason. Since $m\geq 2n$, we can pick a uniformly random pair of vectors by first picking a subset $S$ of size $2n$ uniformly at random from among all subsets of vectors of size $2n$, and then choosing a random pair of vectors from $S$. Since conditional on any choice of the subset of size $2n$, the expected dot product is at least $\frac{n}{\binom{2n}{2}}$, the unconditional expected dot product is also $\frac{n}{\binom{2n}{2}}$.
So it suffices to prove $\frac{\sum_{(i,j)\text{ s.t. }i\neq j} (v_i \cdot v_j)^2}{\binom{m}{2}} \geq \frac{n}{\binom{2n}{2}}$ in the special case $m=2n$, which is equivalent to $\sum_{(i,j)\text{ s.t. }i\neq j} (v_i \cdot v_j)^2 \geq n$. (I will now copy an argument from https://terrytao.wordpress.com/2013/07/18/a-cheap-version-of-the-kabatjanskii-levenstein-bound-for-almost-orthogonal-vectors/) Consider the Gram matrix for this set of vectors, i.e., the $2n\times 2n$ matrix $M$ with $M_{ij}=v_i\cdot v_j$. Since $M=W W^T$, is symmetric and has rank $\leq n$, it has an orthonormal basis of eigenvectors with $n$ associated eigenvalues being $0$, so $M-I$ has the same orthonormal basis of eigenvectors for which at least $n$ eigenvalues which are $-1$. Computing Frobenius norms of $M$ in the usual basis and this eigenbasis gives $$\sum_{(i,j)\text{ s.t. }i\neq j} (v_i\cdot v_j)^2\geq \sum_{k=1}^n (-1)^2=n,$$
completing the proof of our subsubclaim and subclaim. That is, we have now shown that $\frac{\sum_{(i,j)\text{ s.t. }i\neq j} (v_i \cdot v_j)^2}{\binom{m}{2}} \geq \frac{n}{\binom{2n}{2}}$, so $\sum_{(i,j)\text{ s.t. }i\neq j} (v_i \cdot v_j)^2 \geq \frac{n\binom{m}{2}}{\binom{2n}{2}}=\frac{m(m-1)}{2n-1}\geq \frac{m^2}{2n}$.   



The remaining problem is that we wish to lower-bound $\sum_{i\neq j}\mathrm{Relu}(v_i\cdot v_j)^2$ instead of $\sum_{(i,j)\text{ s.t. }i\neq j} (v_i\cdot v_j)^2$ — intuitively, we wish to show that one can't hide all the large dot products below $0$. One way to show this is to argue that the there can't be that much more negative mass than positive mass. To this end, consider
$$\left(\sum_i v_i\right)^2=m+\sum_{(i,j)\text{ s.t. }i\neq j}v_i \cdot v_j\implies \sum_{(i,j)\text{ s.t. }i\neq j}v_i\cdot v_j \geq -m$$
Note that $\sum_{(i,j)\text{ s.t. }i\neq j}|v_i \cdot v_j|\geq  \sum_{(i,j)\text{ s.t. }i\neq j} (v_i\cdot v_j)^2\geq \frac{m^2}{2n}$. Averaging these two inequalities gives $\sum_{(i,j)\text{ s.t. }i\neq j}\mathrm{Relu}(v_i\cdot v_j)\geq \frac{m(m-2n)}{4n}$ 

Since the average term is easier to track, let's also compute it — it's at least $\frac{m(m-2n)}{4n\binom{m}{2}}\geq \frac{m(m-2n)}{2nm^2}$. For instance, for $m=4n$, this gives that the average relu(dot product) is at least $\frac{1}{4n}$. 

from which $\sum_{(i,j)\text{ s.t. }i\neq j} (v_i\cdot v_j)^2\geq$   

There is a large literature on this kind of problem, it's called spherical codes. 

## Claim


any symmetric configuration has the same expected square dot product, so to choose among these, pick the one which hides most of the mass on the negative side


## References
There's a big literature on spherical codes, i.e. energy-minimizing point configurations on the sphere

https://arxiv.org/pdf/1906.03062.pdf thm 2.3

https://www.sciencedirect.com/science/article/pii/S0885064X15000205

https://arxiv.org/pdf/1103.0485.pdf

https://arxiv.org/pdf/1503.07228.pdf

https://arxiv.org/pdf/1703.02930.pdf