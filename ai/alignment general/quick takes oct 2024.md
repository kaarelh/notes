
format (todo): claim in bold


It is basically not good to think of RLHF as a human output distribution conditioned on high reward (ok, more precisely, boltzmann https://arxiv.org/pdf/1204.6481 todo fill in details), despite it being the case that if you actually had the human output distribution and actually found the global optimum of expected reward minus kl divergence, you would get that. I think the starting distribution is just not close enough to the actual human distribution to make this be a sensible way to think. It is more like building a system which has to compose human-like phrases to make nice sentences.

For which $n$ is an $n$-day human that can't learn beyond that able to do sophisticated research (like figuring out how to upload humans or upgrade humans or sth else that would help with x-risk from AI)? A few weeks is probably not enough, and a year is probably enough.

Human imitation is basically not competitive. 

Neural net training very strongly does not find global optima. (If you've taken this from the 'all loss minima are connected papers, then you're some combination of confused and having been lied to.) Instead, you should think of gradient descent implementing 'a certain somewhat arbitrary amount of structure' and no more. To the extent that losses are 'similar' from when trained from different initializations, this is a law of large numbers phenomenon.

SLT is studying a silly toy case with some limited relevance to NN training, much like studying the NTK is doing that, not as uncovering the deep mysteries of the universe