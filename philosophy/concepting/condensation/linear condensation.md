

# linear-algebraic variant of the problem

Let's say that:
* variables/strings are now vectors
* a vector needs to be a linear combo of the vectors for the sets which contain it
* maybe the minimization is in terms of some $L^2$ now?
* even just doing the very natural thing of minimizing the sum of all the $L^2$ norms might work I guess? (in the previous context, this doesn't work because you just push everything upstairs then, but here, there's a cost to putting stuff upstairs — you'll really need to add the same vector to everything)
this is sorta like sparse coding, but sparse coding has the extra requirement that the sets be small? or i mean more precisely activations should be sparse, which is sort of like requiring the sets to be small, but of course really it's the $L^1$ thing

could this give a way to get dense features out by default, if they are indeed natural?

are there some trivial reasons this fails? does it give something trivial? like, maybe the top set just takes the average of all of the vecs? and then maybe you subtract that from all vecs and put the remaining average of each n-1 size set in there? and so on? i mean it's probably not this, but maybe it's this?

i guess an issue with making this practical is that, well, it's exponential-time in the size of the dataset. one soln is to restrict the num of sets to sth small, right. 

can we write down something which is like sparse coding but really minimizes the information, allowing dense features, too?

ok, so let's say features have to be directions. a direction in $\mathbb{R}^n$, a pt in $\mathbb{RP}^{n-1}$, takes n-1 reals to specify, let's say. what can we say about the coeffs of each direction? we can take it to be sampled from some probability distribution, and talk about the entropy of that distribution, i guess? what's a good notion of entropy for a learned distribution? does anthropic have a good soln here? 

actually, could we just do some clustering thing on activation vectors? like if they have some good readoffs, we should be able to just get things with shared readoffs out by looking at the data set of dot products? 

# Some small thoughts on linear variants of condensation / SAE-SVD hybrids

(I'm using a bunch of ideas from Sam and Jake here without local attributions.) Here are some starting thoughts about 'linear-algebraic variants' of condensation, with making the optimal abstraction-variables practically findable (using gradient descent, I guess) in mind. 

to have some concrete-ish example applications in mind: A main example I'd like to try this on is a data set of activation vectors (from a transformer LLM, maybe). Some other possible one could try to apply this to: (1) getting some reasonable things (objects?) out of an image/3d-scene data set; (2) recovering some human syntactic abstractions (phrases?) from some appropriately represented language data set.

Here's what seems to me the most immediate way to turn condensation into some kind of linear algebra problem:
* The base strings(/variables) become vectors in $\mathbb{R}^n$.
* Abstraction-variables are also just vectors in $\mathbb{R}^n$. (Alternatively, one could maybe make these sets of vectors, or subspaces.)
* A base vector must be the sum of the abstraction-vectors of all sets it is in. (Or maybe a linear combination? I'll discuss a setup involving that choice later.)
* The objective is to minimize a linear combination of the (squared?) $L^2$ norms of all the abstraction-vectors of subsets. The coefficients should probably only depend on the sizes of the subsets. In fact, maybe all coefficients could just be $1$. (I think making all coeffs equal is a bad idea in the original condensation problem because it is then roughly optimal to just put everything in the full index set abstraction, but I'm not seeing an immediate issue here.)
One issue with applying something like the above in practice is that there are going to be way too many variables (exponentially many in the size of the data set).

[Sparse dictionary learning](https://en.wikipedia.org/wiki/Sparse_dictionary_learning) algorithms do not face this issue because they assume a much smaller overbasis (maybe polynomial in $n$), and learn the vectors and coefficients. (The vectors do not start off being identified with subsets, but after training, one can identify an overbasis element with the subset of data points on which it has a nonzero coefficient.) However, I think sparse dictionary learning algorithms bake in the assumption that representations should be [superpositional, not compositional](https://transformer-circuits.pub/2023/superposition-composition/index.html). Alternatively, SVD/PCA is also computationally fine, but rules out superposition a priori. It would be nice to have some linear reconstruction problem which makes neither assumption (so that (1) we get some information about the degree to which representations are superpositional vs compositional and (2) we might even have some chance of discovering right/good decompositions without having to know a priori the degree to which they are superpositional vs compositional).

Here's the most principled computationally tractable superposition/composition-agnostic optimization problem that I can think of:
* Given a data set, we are looking for an overbasis (maybe of unit norm vectors) together with a way to (approximately) write each vector in the data set as a linear combination of overbasis elements.
* We want to minimize the following:
	* 'the entropy of the distribution of the coefficients of overbasis elements'
	* the number of overbasis elements? ('?' because idk this might already be included in the item above)
	* the approximation errors of the reconstructions

Of course, I haven't said precisely what we should minimize here, and I won't quite manage to, but I'll try to make it a bit more precise. An option would be to go back to thinking of the entire thing as a compression problem, with the compression having the following structure: you need to provide (1) an overbasis together with (2) a list for each overbasis element of the coeff that overbasis element gets in the decompositions of data pts, except this list is optimally compressed (ie with a good encoding for its distribution), and (3) the remaining error encoded optimally as if it were taken from some fixed gaussian and up to some precision (this should roughly be the same as an $L^2$ reconstruction term in the loss). To make this precise, we would need to talk about the entropy of the coeff distribution; I'm not sure what we should precisely mean here, but there could be some reasonably nice choice — I'd need to think more about how to think about bit precision or error or something here (surely this should be a [standard problem](https://en.wikipedia.org/wiki/Entropy_estimation); maybe the [independent component analysis literature has figured out a reasonable choice](http://cis.legacy.ics.tkk.fi/aapo/papers/IJCNN99_tutorialweb/node15.html ), but I haven't thought about it sufficiently yet; Anthropic does something related [here](https://transformer-circuits.pub/2023/may-update/index.html#simple-factorization)). A very crude alternative would be to just 'count the number of bits' by (1) counting each real number as some constant number of bits, say $64$, so counting each overbasis element as $64(n-1)$ bits; (2) counting the bits one needs to naively specify the coefficient of each overbasis element — if it is nonzero on a fraction $p$ of the $D$ data pts, then specifying the coefficient for an overbasis element in all data pts takes $D\cdot H(p)$ bits; and (3) then specifying the Gaussian error takes something like another $\lambda \lVert x_i-\hat{x}_i\rVert^2$ bits (with some hyperparam $\lambda$) on each data pt $x_i$. I haven't seen any intuitive issue with this optimization problem yet but I also haven't tried much yet, other than the obvious issue that this last version is not differentiable.

I currently assign a significant probability to the closest differentiable (or otherwise practically solvable) optimization problem to the above having already been considered in the [independent component analysis](https://en.wikipedia.org/wiki/Independent_component_analysis) literature, but I'm not that familiar with that literature yet. To translate their standard problem statement into our form: take what they call 'source signals' to be what we have been calling abstraction coefficients here; take what they call a vector of 'observed signals' to be a data pt vec for us, and take the columns of what they call the 'mixing matrix' to be our abstraction-vectors. It looks from the linked wiki article that they are solving a somewhat different optimization: it says they either try to minimize mutual information or maximize non-gaussianity of the coeffs, but then I think maybe they [operationalize maximizing non-gaussianity as minimize some kind of entropy estimate](http://cis.legacy.ics.tkk.fi/aapo/papers/IJCNN99_tutorialweb/node12.html). But again, I haven't really read enough yet to understand this stuff well — e.g. I don't know if any of their stuff handles the case with potentially many more (sparse) source signals than measured signals gracefully (i.e., more than $n$ abstractions). I hope to maybe update these notes later when I've understood the ICA connection better (or alternatively if you have thought about this I'm also interested in your assessments of whether the ICA literature or some other literature has already considered the best linear variant of condensation).

## Some questions that remain to be thought about

1) At least in the case of activation vectors, there being meaningful linear functions from the data set to $\mathbb{R}$ seems more fundamental (better-justified) to me than activation vectors being linear combinations of abstraction-vectors. There's the idea to look for a set of directions onto which projections are sometimes large and also independent, or maybe one could just use some kind of fuzzy clustering on a graph with vertices corresponding to data pts and edge weights given by some function of angles or dot products or something, but idk how to make these things fit in this story. 
2) Do some of these optimization problems have silly solutions (sth like the optimum is to just let some abstraction-vector be an average of the respective base vectors)?
3) Are there variants which are more principled / better? Are these problems missing the point of condensation?
4) What are some other problems (in addition to the activation vec thing or the picture thing or the language thing) on which it would be appropriate-interesting to apply linear condensation?
5) Is there any additional literature worth looking into here? (The first thing that comes to mind here is to look at the sparse dictionary learning (sparse coding, compressed sensing) literature more, but I'm a bit more familiar with that than ICA stuff, and I can't think of anything similarly relevant atm. Another thing that comes to mind is that maybe there's something worthwhile in the autoencoder literature.)


## Independent component analysis

ICA asks the following question: suppose you have a data set of measured vecs which you know is a linear combo of basis vecs with independent coeffs

(the standard presentation has signals which are independent of each other, and coefficients on the signals which for each measurement location  )


