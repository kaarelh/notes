
Q: When are we in the BIC limit?

Ans: Well, when $n$ is large enough that the terms that are eventually smaller in the derivation below are indeed already smaller. One can find a rough n after which we are in this 'limiting regime' by setting the eventually dominating term to be equal to other terms.

![[Pasted image 20240419130253.png]]

So, what we need for the argument above to tell us that we are in the limiting regime:
* e^R(x,theta) needs to integrate against the prior to something smaller than the integral of e^ the other two terms against the prior
* the integral of the e^quadratic against the prior should not be changed by much when the prior is replaced by a linear approximation
* the abs val of log det hessian and the abs val of log prior density at the MLE should both be less than the abs value of the BIC
![[Pasted image 20240419144037.png]]
* While the above is everything that's needed for the BIC posterior approximation to technically hold, the 'spirit of BIC' is about counting parameters — at least in these corners, I think BIC is supposed to capture a complexity penalty — so to be in the regime where this 'spirit of BIC' holds, we need k log n to be larger than both the log det hessian and the abs val of log prior density.

Since I care more about the spirit of BIC, I'll proceed to focus just on understanding the cases in which the spirit of BIC holds. Note that the last condition sorta implies the penultimate one — more precisely, the technical BIC approximation holding follows from the BIC approximation holding assuming there isn't much cancellation between the two terms in the BIC, ie assuming their difference isn't somehow orders of magnitude smaller than the k log n term, and I don't atm see any immediate reason to expect such a 'conspiracy'. So the spirit of BIC holding implies-ish that technical BIC holds, and for now I won't care about understanding the additional cases where technical BIC holds but the spirit of BIC doesn't.






# other questions

is there even any case where the BIC/WABIC setup gives generalization at all? i mean with reasonable choices. like you are just missing the prior right! should be pretty easy to construct some concrete counterexamples here?

## related

https://www.lesswrong.com/posts/bvM6zj9xv5sjkGrhZ/from-laplace-to-bic