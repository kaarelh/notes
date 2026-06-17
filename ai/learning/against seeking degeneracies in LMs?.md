
i think lucius has/had the following argument?:  
  
The reason some kinds of NNs generalize is that points with more freedom in the loss landscape are found, and these points tend to generalize. It is unlikely that other kinds of NNs generalize for some other reason. (E.g. this is why he wanted to make sense of degeneracies in the superpositional case.)  
  
Here's a counterargument:  
  
I think it's plausible that the right story of learning is sth like the following:  
A bunch of stuff starts getting built all at once (e.g. a large number of possible boolean circuits computing the same boolean function, a large number of smaller correlated circuits, individual memorizations). In cases where generalization happens, the more general stuff wins because it grows faster / packs weight norm into prediction-oomph more efficiently (in cases of grokking or epochwise double descent, only eventually and with some help from weight norm keeping the memorizations from running off to infinity in a bad direction).  
  
Given this story, in the overparametrized case, you'll eventually see something nearly degenerate (in cases where a NN generalizes) because the generalizing circuit grows OOMs faster than other stuff (or with weight norm, translates weight norm into prediction-oomph much more efficiently).

hmm a general model: you get a bunch of structures. when more overparametrized, lottery ticket stuff might make it a bit more likely to find even smaller structures? 