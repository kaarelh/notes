
Here's some discussion of a maybe independently interesting and strictly easier problem than proving the construction i had in mind earlier is optimal (but idk maybe you have a better construction anyway; maybe this isn't strictly easier than your original problem). It involves a generalization of the setup in

[https://en.wikipedia.org/wiki/Bertrand%27s_ballot_theorem](https://en.wikipedia.org/wiki/Bertrand%27s_ballot_theorem)

, allowing arbitrary weights. Idk how to solve this problem. The probability that a random parenthesis expression with $n/2$ left parens and $n/2$ right parens (so $n$ steps in total) is valid is $\frac{1}{n/2+1}$. What's this probability if we change the weights of the parens? That is, suppose we now have $n$ numbers $a_i\in \mathbb{R}$, maybe with the constraint that $\sum_{i=1}^n a_i =0$. If we take a random permutation $a_{\sigma(i)}'=a_i$ of these numbers, what's the probability that all prefix sums are non-negative? I.e., that for all $k\in[n]$, we have $\sum_{i=1}^k a_i'\geq 0$? Or maybe: what's the highest possible value for this probability? I suspect it's just given by the $a_i = \pm 1$ case which gives $\frac{1}{n/2+1}$ as that probability. For the highest prob, we can always assume $a_i$ are integers. This is because we can rescale to make everything arbitrarily close to integers all at once (this is by a pretty standard pigeon hole argument on $[0,1]^n$ partitioned into boxes, ie considering where multiples fall, using multiples in the same box), and after this rescaling, pushing everything to the closest integer must maintain the sum constraint and can only make the probability that all prefix sums are non-negative higher. So really this comes down to counting some Dyck paths with uneven but integer steps.

[

  


](https://en.wikipedia.org/wiki/Bertrand%27s_ballot_theorem)