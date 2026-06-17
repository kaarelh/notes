
suppose we have a coding scheme with rates summing to the entropy of X. can go from this to random variables. these will have joint entropy almost the sum of their entropies — in this sense they are close to being independent. how can we nudge them by a bit to be actually independent? like keeping the same mutual informations up to eps. can we just change the distribution on the Y_i to the product of their distributions somehow without fucking things up? i guess not, right, because imagine a case where X takes just one value, and the coding scheme has two correlated bits in two latents and would output sth catastrophic if they are mismatched. then just going to the product naively gets you a catastrophic result half the time


one potential help: we can move stuff to the top latent if needed

## obviating the need for the above by making the other direction go thru with entropywise-near-independence

suppose near-indep variables. how would we code as well? i guess can just sample still right?

ok so suppose we go from coding to rvs and get near indep rvs. now what happens when we start to sample them into a product dictionary. do we really need to make the product dictionary a lot larger?

I think the following resolves the independence issue. Any coding scheme with rates $r_i$ summing to the entropy of $X$ (and so codewords having joint entropy close to the sum of their entropies) can be turned into a coding scheme with rates $r_i+\epsilon$ where the codewords are precisely independent. (And then one gets precisely independent random variables from this new coding scheme.)

I think one can go from a near-independent coding scheme to an independent one as follows:
* To begin constructing the new coding scheme, let's think of there already being an independent distribution on the tuple of codewords sent, with a uniform distribution on the codeword sent in each channel. This is before we specify how the input sequences and output sequences get hooked up to these codewords.
* Think of each channel of the original scheme as providing a labeled partition of the input sequences $x^{1:m}$ — the decoder of a part of $X$ is informed of the location of the input wrt the partitions of the channels it sees, and makes a certain decision.
* The key idea is that we can make our new channel $i$ track almost exactly the same partition as channel $i$ of the original scheme. More precisely, it'll track an 'almost-refinement'. The idea is to arbitrarily assign a set of codewords of the new channel for each codeword of the old channel such that the probabilities of the new codewords add up to the probability of the old codeword. And map the same input sequences $x^{1:m}$ to these new codewords that you originally mapped to the old codeword. I think one has to give up on 'representing' the original codewords that had probability less than $2^{-m (r_i+\epsilon/2)}$, but these only contribute a probability at most $2^{-m (r_i+\epsilon/2)}2^{mr_i}= 2^{-m\epsilon/2}$ in total,  
* (Think of the new channel as having smaller-probability codewords compared to the old channel.)
* 
* And then of course one can still recover
 The second idea is to think of 

wait this makes no sense. we can't be assigning inputs to codewords channel by channel this way and expect the independence structure of the codeword joint distribution to be respected! like the input assignment forces a different joint in general. there had to be an issue with the above argument because it would prove that one can generally make stuff independent without any restriction to just the near-independent case, but this has to be false as one can see by sam's example with two channels that just have to carry the same information

however, it would be fine to assign inputs to points of the product space (each input going to many points). but can we do so while mostly still seeing the original partitions? wouldn't that imply a contradiction? like then the elts which union to a part of an original partition will be correlated with the elts that union to a part of another partition if the two parts of the original partitions were correlated

maybe one could start from this stupid construction and then make some moves to make it more independent? 


feel free to ignore this or to think about this later, but if you have a moment: Do you know if the common information of two random variables that are 'nearly independent' has to be small? More precisely, suppose I have H(X,Y)=(1-o(1))(H(X)+H(Y)), or equivalently I(X;Y)=o(1)(H(X)+H(Y)). Then must we also have C(X;Y)=o(1)(H(X)+H(Y))?

actually i guess it is fine for the error to have either sign? if give too high probability to some output then just need to send some other stuff there? hmm but defo shouldn't have the probs go above 1 or sth? yea i guess error needs to be positive? maybe the condition is that the 

ok why can't i just say that i want the total variation distance to be small. the construction would be to have the same stuff as is sent to a previous domain value be sent to this value now mostly. will have some leftover and some where extra is needed. just use the leftovers to cover the extra. this should work as long as the TV distance is o(1) i think? naively we'd want the weights to sum to 1 but i guess that's not necessary — just requiring o(1) distance implies that the weights sum to between 1-o(1) and 1+o(1) i think and then one can scale everything down and still not lose i think 


for split between common information and mutual information, maybe see Values and Bounds for the Common Information of Two Discrete Random Variables https://www.jstor.org/stable/2100249

or maybe in kolmogorov complexity and algorithmic randomness by chen vershagin uspenski or somethin

10 am pt thu next week