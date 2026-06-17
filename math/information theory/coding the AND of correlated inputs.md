
can take a messaging rule for $y_2^{1:n}$ as given and ask for the optimum for $y_{1}^{1:n}$. can we turn it into a solved problem? we'd like AND to descend to a function on this quotient, at least for typical sequences i guess. it's probably fine on a first pass to require that literally everything that's typical get the right output. or even to require this for everything that is at least as likely as a typical thing. so whatever we see for $y_1^{1:n}$, any two different typical $y_2^{1:n}$ with different AND should already fall into different buckets on the other side. so take any vtx of the hypercube and look at a radius $10\%$ ball around it. any two things in this ball should be in different buckets except potentially when they have the same AND with the center. this means the pair has to diff only where the center is 0 anyway. but this needs to be true for every center! now for any two things in the same bucket which are sorta close to each other, we can find a center on the other side which causes fuckery.
> setup: two fair coins with prob that differ $p<0.5$
> unjustified assumption: for every typical pair, have to be able to find func value
> conclusion: any pair which is like <2p close has to be in different buckets!!




# meta
open problem encountered independently and also in chapter 21 of eisenstat's book


