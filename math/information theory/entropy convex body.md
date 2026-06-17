it's discussed here: https://en.wikipedia.org/wiki/Entropic_vector 
and here: https://iest2.ie.cuhk.edu.hk/~whyeung/post/draft7.pdf

they use the term 'entropic vector'

$n$ random variables. have entropies for all $2^{n}-1$ non-empty subsets. probably normalize and look at ratios instead of values? the set of all feasible tuples should then be a convex set in $\mathbb{R}^{2^n-2}$. this body is not well-understood, unfortunately

the shannon inequalities are that the following are non-negative:
* (conditional) entropies (ie $H(X|Y)\geq 0$, ie $H(X,Y)\geq H(Y)$, and with more variables)
* (conditional) mutual informations (ie $I(X;Y|Z)\geq 0$, ie $H(X|Z)\geq H(X|Y,Z)$, ie $H(X,Z)-H(Z)\geq H(X,Y,Z)-H(Y,Z)$)

but apparently these do not characterize the body — there are tuples which satisfy all the above but aren't possible


some reasons to care:
* if we could characterize this body, i think we'd be able to solve the multicast coding problem (i think one can reduce the coding problem to this problem by having the inputs and all other vertices correspond to variables, then encode required functional dependencies in terms of entropies and also independence of inputs in terms of entropies and also having desired outputs in terms of entropies and also rate bounds in terms of entropies, and ask if the convex set defined by these intersects with the entropy body) 
	* in particular, this would solve the question about how rates can always be moved around in condensation
* it gives an outer bound on another cool point set, namely of all possible dimensions of the $2^{n}-1$ sums of subsets of a set of $n$ subspaces of a vector space over a finite field. that's because you can construct a random variable with dim entropies from a collection of subspaces! this can be done by picking a random linear functional and making the random variable corresponding to a subspace be the restriction of that linear functional to the subspace

## is the body full-dimensional?

so we have some convex set in $\mathbb{R}^{2^n-2}$. does it have full dimension? maybe we can just write down $2^n-2$ random variable tuples which give an affinely independent set of entropy tuples? setting one variable to 

# hypergraph characterization

you can turn this into a problem about possible hypergraph degree sequences, i think (but haven't checked this carefully). any hypergraph with certain degree conditions gives you a joint distribution — just treat the variables as the points touched by a uniformly random edge in each part. but also i think you can take many copies of a thing with given joint entropies and then keep stuff with high enough prob and round all of those to the same const while preserving entropies up to small error. so anything can be turned to a hypergraph also. so characterizing possible hypergraph degree sequences is an equivalent problem?

# group characterization

the thing sam told me about with subspaces has a generalization to groups (from https://en.wikipedia.org/wiki/Entropic_vector#Group-characterizable_vectors_and_quasi-uniform_distributions ): 
* now we are taking subgroups G_1, ..., G_k of a group G. the variables X_1, ..., X_k are obtained by taking a random elt of G and saying which coset of each subgroup it is in. 
* knowing the coset of G_i and the coset of G_j that an elt is in is the same as knowing the coset of G_i intersect G_j. (this is sorta a generalization of the chinese remainder theorem i guess.) this is because if you know the coset of G_i and the coset of G_j, you know it is in the intersection of the two, and here we precisely have all elts reachable from a single one by anything in G_i cap G_j, so now we know which coset of the intersection the elt is in; and if you know the coset of the intersection, then you know it up to multiplying by sth in G_i cap G_j, so you know its G_i coset and its G_j coset also. this means that joint entropies are log numbers of cosets
* this generalizes the subspace version in the following sense: there we had a linear functional and subspaces, seeing what it is on a subspace. linear functionals which are 0 on the subspace make a subgroup; here we are precisely being told which coset of that subgroup we are in by observing the values on that subspace!  

and apparently https://iest2.ie.cuhk.edu.hk/~whyeung/post/draft7.pdf proves that any entropic vector can be approached by a group vector of the above sort up to normalization! this is thm 16.22. so the entropy vector problem is equivalent to a problem about groups! 

maybe we can re-prove it assuming the hypergraph characterization works out? is there some way to go from a hypergraph to a group? we'd want the parts of the hypergraph to correspond to subgroups somehow. group elts need to correspond to edges of the hypergraph. wtf would the group operation be though? we need to make seeing what vertex the edge touches be the same as seeing the coset of a subgroup. seems tough to make this work, esp with some tension at defining any nice way to compose the edges at all — idk how to do it atm!

(i think the construction might actually directly give permutation groups but:) we can note that one can embed any group in a permutation group, keeping all subgroup sizes the same, so multiplying all coset sizes by the same const; so really one can also do it with subgroups of a permutation group also!

