


suppose you have a continuous function $f(z,c_0,c_1,\ldots,c_n)$ of many complex variables, let's say holomorphic in the first variable for any setting of the others
(canonical example: a polynomial given by coeffs $c_0,c_1,\ldots,c_n$)
later realization: this is false, but it's true that you can't destroy roots in this sense, ie there is a perturbed set of roots corresponding to the old roots always
corollary: polynomial's roots vary continuously in coeffs as long as you don't create a new highest degree term
corollary: fundamental theorem of algebra
corollary: eigenvalues, singular values of a matrix are continuous in its entries

then do the zeroes in terms of $z$ alone vary continuously in the other variables $c_0,c_1,\ldots,c_n$? probably want to say this in terms of multiplicities, looking at the power series at each point to determine the order of the root, though we could also just talk about the set

this is certainly false for real functions, e.g. $f(z,c_0)=z^2+c_0$ does not have a continuous set of roots at $c_0=0$ (since there are no real roots with $c_0>0$)


around each root, there must be a ball which contains no other root (by identity thm)
suppose you have a point at which the power series expansion has a first nonzero term $a_k(z-z_0)^k$, ie it has a root of order k at that point. take a disc around it with no other root — indeed, noting we can write the function as $a_k(z-z_0)^k(1+\delta(z-z_0))$ with $\delta=1$ at $0$, pick a disc where $\delta<1/2$ everywhere (this can be done by continuity of $\delta$). now if you change the other coords by a small enough delta, by continuity, the integral of 1/f around the disc changes by very little. 


cor. fundamental theorem of algebra (start sliding toward a polynomial from z^k, continuous integer-valued function must be constant!)

wait but isn't there a contradiction with sliding from z^k+z^{k-1} to z^{k-1}?? why can we get rid of a root here? there's a point at which the zero set is not continuous, namely the end z^{k-1}. maybe the correct statement is that one cannot continuously destroy zeros? (this is false for reals bcs of the counterexample, but maybe true for complex numbers, and would still imply the corollaries we want i think!)

ok so perturb f in the disc by a small function that is holomorphic (since delta of two holomorphic functions). now added something to z_0 so no longer 0 there; but walking around the disc boundary, the perturbed function path winds around 0 k times still because we've picked the perturbation to be small. think abt the dog walking path as we increase the radius as we do this walk from 0 to the disc's. it must certainly hit 0 somewhere. indeed if needed can show this can't be very far from 0 even in terms of % of the disc just from lower bound of the value from the original function and the perturbation being small. let this new root be at z_1. repeat the argument for (f+g)/(z-z_1) which is holomorphic because that's how stuff works i think (well, pf: certainly holomorphic everywhere else. holomorphic around z_1 because power series given). in fact, div by all roots with orders all at once. now get a function which is holomorphic on the disc. if fewer than k roots divided, then we have like (f+g)/prod on the boundary which is (z-z_0)^k/prod up to noise terms, now can make each ratio arb close to 1 by picking perturbation small enough, then note that it still loops around at the circle unless prod has at least k terms; looping around would imply another root by the same argument. so indeed no roots destroyed!!!

i guess the intuition here is that if there are somehow fewer roots in a small circle around, then really you still need to be looping around 0 on the outer circle in the ratio, but then there needs to be another root