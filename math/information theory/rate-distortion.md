
remark. i think one should talk about the product of the rate and channel capacity here

I'm sort of confused about why the noisy channel theorem and the rate-distortion theorem aren't presented as special cases of the following theorem/conjecture:
> Claim 1. Fix a utility function $u\colon \mathcal{X}\times \mathcal{W}\to \mathbb{R}$. Fix an input random variable $X$, i.e., with domain $\mathcal{X}$. For a noisy channel with capacity $C$, the supremal expected average utility over coding schemes of input $X^n$ to output $W_c^n$ through that channel is $$\sup_{\text{joint distributions on }X \text{ and }W \text{ marginalizing to the given distribution on }X\text{ and with }I(X;W)<C}\mathbb{E}_{p(x,w)}\left[u(X,W)\right].$$

Some corollaries:
* If the channel has no noise (and maybe $\mathcal{W}=\mathcal{X}$), then we should get the rate-distortion theorem.
* If $\mathcal{W}=\mathcal{X}$ and the utility function is a delta function (and maybe with $X$ being a coinflip), we should get the noisy channel theorem.
* If If $\mathcal{W}=\mathcal{X}$ and the utility function is a delta function and the channel has no noise, then we should get the source coding theorem.
I suspect I've said something incorrect here, because this seems like a nice way to present a bunch of stuff, but I can't find a theorem that's equivalent to Claim 1 in the literature. I don't have a proof of Claim 1, but I also haven't thought through whether the obvious meta-strategy of trying to combine the proofs of the rate-distortion theorem and the noisy channel theorem works. Anyway, maybe Claim 1 is false? I haven't properly thought through whether Claim 1 really implies these theorems in full either. I'd be interested to hear if you can see that something above is incorrect or if you know of something like this is in the literature.


I'm not sure, but I guess the rate-distortion theorem says that Claim 1 is true for a noiseless channel, and then you can get [whatever the optimal noiseless channel construction sends] [through a noisy channel as well] [by the noisy channel theorem], so the sup is a lower bound on the attainable expected average utility for any channel.


But I guess the sup is also an upper bound because if you have a way to send stuff through your channel with some expected average utility, then you can get a joint distribution on (X,W) with the same expected utility and mutual information at most C as follows (this might be the standard method idk, or maybe it's not but then whatever else is the standard method would maybe also work):
* Let (X,W) be given by taking a random sequence X^n, choosing an index i uniformly at random in [n], letting X be component i of the sequence, and letting W be component i of the output of this sequence through the given channel.


So maybe Claim 1 is true? (idk still likely i've made some silly errors)

Let's attempt an independent proof. We already have from above that each coding thing gives a random variable with the same expectation, so the random variable thing is at least as good as the coding thing. (Maybe a better theorem would say that the set of possible expected utilities is the same.) It remains to take the random variable thing and to construct a coding thing. I guess maybe the idea here in the deterministic case (rate distortion) is to just sample a bunch of sequences of a given $W$ and make codewords that correspond to to all those sequences, and then one assigns each $x^n$ to the best codeword. What about the noisy case? Maybe fix 