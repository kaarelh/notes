
 > Proposition. suppose there is some simple property such that no input with that property showed up in training. then you have at least corresponding const probability of just outputting 0 on all inputs with that property
 
 Proof. take the current best program. you can add to the start the following check: if input has property P, then output 0. else, do the program. this has probability smaller than the best by like at most about 2^C(P), where C(P) is the complexity of the property P. (need to check: is there some log term here that one is actually losing? we wouldn't get a const in that case. probably you can avoid that with the universal semimeasure?)
 
 this is relevant eg to the attempt to get science from solomonoff with random prompts

is this fine? maybe it is — maybe good behavior has a better const. but hmm it does mean there's a programming language in which it doesn't have a better const? well the programming language is specific to that property tho, which is maybe weird