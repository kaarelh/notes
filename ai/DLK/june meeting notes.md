"A function from logical expressions to utility variables." -> can you give an example? is this like expected utility given proposition about world?
decompose utility over world into expressions additively, but as powerful as complete descriptions actually because could AND all properties of world

The brain's decision algorithm + implementation function + brain's transition function are probably specified in some language/theory; what do you see this language/theory as being? Do you have an explanation of how this gets grounded? Or how do we get an AI to understand this language/theory?

what requirements are you putting on the compression? is it required to be lossless?

requiring it to have a high compression rate is sort of like giving it points for being simple. Do you see this as trading off against other desiderata, i.e. are you minimizing some loss which is a linear combination of scores on the various desiderata (e.g. simplicity matters, but the brain transition function / decision algorithm commutative diagram also mattrs), or is each desideratum just a hard requirement? (If they are all hard requirements, I guess your decision algorithm will also include all kinds of being irrational, e.g. what happens when the brain is drunk or whatever? otherwise can't losslessly compress)

ans: it's traded off 

do I understand correctly that you are weighing the desiderata of e.g. the commutativity of the  commutative diagram vs 


do you require the brain state to be reconstructible from the decision algorithm state? I'm confused about what 

is there some stuff which privileges continuations that we would consider "rational"? e.g. there is an intoxicated continuation

causal Markov model unwound across time is causal model

need some other bit to deal with inner misalignment because output is utility oracle in terms of world model



possible world semantics stuff -> other type signature for concepts inside nets? like functions from functions to functions in general? how could such a thing be implemented in a net?


realization condition of an object -> the set of worlds in which object exists

is this relevant to finding circuits, for coming up with hypotheses?
https://en.wikipedia.org/wiki/Symbolic_regression#:~:text=Symbolic%20regression%20(SR)%20is%20a,terms%20of%20accuracy%20and%20simplicity

instead of finding map of entire net into model, find subnetwork best maps, do greedily up the tree 

figure out what mech interp people know about finding map from heuristic algo into model, like do you just supervised probe for each node?

ask about connection between philosophical semantics and math model theory? is it somehow the same thing? 

how do we turn inference rules into equations in a principled way?

https://arxiv.org/pdf/2211.00593.pdf

beliefs about means end reasoning

activation patching/editing the "if I deceive humans, that will help me maximize utility" belief, seeing if it changes behavior, if yes it was deceptively aligned

supervised probe to find 

look for something that is transitive

run experiment where RL language model to do X, see if that changes its concept of good such that it now thinks that X is good (or stuff instrumentally useful for X is good); note that in the RL the model would never be incentivized to say X is good, just to do X

Axiomatic first-order probability by Laskey

Measuring the overall incoherence of credence functions

prompt language model to create a certain agent 

have it play a card game like blackjack

elicit means-ends reasoning in blackjack


means-ends activation patch with different belief, causal tracing, see if it changes behavior
in the case of AGI, activation patch the means-ends thing with "If I deceive humans, I can 

train on means-ends reasoning, then do RL 


put -min(1,(1-p(P)+p(neg (P->Q))+p(neg Q)) in the loss, but that seems like an arbitrary choice

One choice would e.g. be to think of modus ponens as [(neg P) or (neg (P->Q)) or Q], suggesting the constraint




add action constraint to value of state, i.e. that policy head output index matches highest value node index

conditional utilities, could add constraints in utility case to be coming from conditional utility theory

Hume and the Bauhaus theory of ethics for framework of virtue ethics
