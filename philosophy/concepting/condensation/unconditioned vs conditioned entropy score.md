# a failed attempt at merging the two

if there is a condensation at certain entropies then there is also a condensation at at most these conditioned entropies

if there is a condensation at certain conditioned entropies, then can we also make a condensation at these entropies? hmm... so by default the random variable can have way too much entropy. in the worst case, we have disjoint parts of the domain depending on what's upstream. can we always merge? i mean we don't really need them to be separate right? if we had two subdomains of the same size, i feel like we could just merge. ok so what if not? 

like in general we just have n probability distributions $\mu_1,\ldots,\mu_n$ on the same set, with some weights/probs $p_1,\ldots,p_n$, and we know the expected entropy with these weights is H. then can we somehow move the distributions on top of each other so the entropy of the sum distribution is H? a natural guess (to get a low entropy sum) would be to order the points in each according to size and then put them on top of each other. is this an operation that gives total entropy at most H? hmm it doesn't right. the total entropy needs to be at least the expected conditional entropy, so at best they'd be equal, but you don't get precise equality here because that only happens with independence (ie when the distributions $\mu_i$ are all the same). so this direction fails! the conditioned entropy might have to be smaller i guess


# some thoughts related to how they compare

can we move mass up in condensation with conditional scores? like can we go from a coinflip to 0.5 and 0.5? the issue with this previously was:
* the total entropy of the two is 1 and the joint needs to be split into 0.5 and 0.5 on each side which now need to be independent and which need to each be made by merging some pairs (x_1,x_2), but if we're doing any merging here at all then we have more entropy than 1, and we need to be merging since at least 4 parts created by the two
