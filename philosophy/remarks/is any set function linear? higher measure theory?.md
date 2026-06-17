
consider a function $\mu\colon 2^S\to \mathbb{R}$

is there always another $\lambda\colon 2^\Omega\to\mathbb{R}$ such that we can always expand $\mu(S)=\sum_{T\subseteq S} \lambda(T)$?

is this just expressing the function $\mu$ in some basis of containment indicator functions? ie we can do this as long as these indicators span. i guess the matrix containing all of these is upper triangular in the original basis of just sets, so yes!

this is related to / the same as the ising model thing that dmitry was telling me about

(side remark: maybe an interesting measure of the complexity of $\mu$ is the max size of $T$ needed to do this. e.g. in the discrete case, measures are the simplest, and then we get some interesting level 2 thing, etc)

this motivates 'higher measure theory' (i wonder if considered already): a discrete k-measure is given by a function from sets of size up to k to reals

what's the right generalization of this to the non-discrete case? is there a good generalization?

let's start with the pairwise case. in the discrete case, we can sum over all elements of a set, and sum over all pairs of elements. the additivity property is maybe that for disjoint $A,B,C$, we have $\mu(A\cup B\cup C)=\mu(A\cup B)+\mu(B\cup C)+\mu(C\cup A)-\mu(A)-\mu(B)-\mu(C)$? and maybe also some more general version of this for countable unions? with a sum over pairs minus a sum over singles on the RHS (and a countable union on the LHS). yep this property seems good — should give the right thing in the case where $\Omega$ is countable.

what's a uniform 2-measure on the unit interval? I guess just make all pairs worth the same, so $\mu([a,b])=(b-a)+(b-a)^2$, or maybe just $(b-a)^2$ if we want to assume it is the 'pure uniform 2-measure' or whatever?

what's the natural notion of integration wrt this? maybe you need to integrate two functions always? or the same function against itself? or a 2-variate function on the same domain? probably this last option?

wait, is this just the same as a particular kind of measure on $\Omega\times \Omega$? I guess we only have symmetric subsets in this setup?





As a simple and not-too-unrealistic model, I propose that we should treat “thoughts” as _compositional_ (i.e., basically made of lots of little interlocking pieces), and that the value function is _linearly additive_ over those thought-pieces. So if a thought entails imagining a teddy bear on your bed, the valence of that thought would be some kind of weighted average of your brain’s valence for “this particular teddy bear”,  and your brain’s valence for “teddy bears in general”, and your brain’s valence for “thing on my bed”, and your brain’s valence for “fuzzy things”, etc., with weights / details depending on precisely how you’re thinking about it (e.g. which aspects you're paying attention to, what categories / analogies you’re mentally invoking, etc.).

https://www.lesswrong.com/posts/SqgRtCwueovvwxpDQ/valence-series-2-valence-and-normativity