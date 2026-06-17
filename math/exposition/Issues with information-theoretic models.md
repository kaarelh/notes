
educational status: This is written from the perspective of someone that generally understands math, that understands probability theory well, that understands the math of information theory well enough to have tutored someone on it, but that has not seen many "practical applications" of information theory. (In part, I am writing this in the hopes of being directed towards such applications that deeply make sense.) 

emotive status: I feel a strong vibe that almost any application of information theory / causality to any interesting real system is likely to fail, or at least to fail to be true-name-y.

Here are the ways in which it appears to me like it fails:

1) information vs usable information
	1) example of neural net information (linearly accessible)
	2) example of transfer entropy for agency (accessible to a computationally bounded agent), or maybe this nonsense is a better example: https://arxiv.org/pdf/1412.2447.pdf
2) too discrete, forget important facts about the structure of the domain (as opposed to sth like https://en.wikipedia.org/wiki/Wasserstein_metric or optimal transport: https://www.stat.cmu.edu/~larry/=sml/Opt.pdf). give KL divergence example (where two distributions "differ a lot" but really in a way we do not care about); maybe give approximate coarse-graining/abstraction example where maybe abstraction is bad for compression of exact states but only off in a way which does not matter (autoencoder with reconstruction error vs precise thing)
   counterexample: https://arxiv.org/pdf/2301.04709.pdf seems to account for distance! generally seems pretty good!
3) it just generally seems like everything depends a lot on the details of the setup? ie picking the right variables

It is plausible that these issues 

linear info paper tho: https://arxiv.org/pdf/2002.10689.pdf

read this too maybe: https://www.sciencedirect.com/science/article/abs/pii/S0893608009003256


