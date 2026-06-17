
a few mechanisms for the wiki/4chan tag thing:

on wiki, general understanding is used and gets updated; on 4chan, other stuff is used and gets updated; of course general understanding doesn’t get updated on 4chan

can also explain how this would get learned

whereas the thing that looks more like metalearning mechanistically: there is a circuit in the NN which learns more on wiki and pushes logits up on everything; somehow this wins

the issue is that this isn’t thanked particularly on wiki and it’s also not thanked on non-wiki, though it somehow should be? also wait, how does this work on wiki? like you have a module that checks wikiness and adds stuff to memory more? and also this needs to be pushed up by gradient descent, so somehow it needs to contribute to better loss on the local wiki data. so probably this fact in memory needs to be used on the wiki data! it seems like roughly the only option then is that the wiki data needs to use general memory whereas 4chan doesn’t? i guess it couldn’t be any other way?

hmm actually maybe this makes sense with wiki vs 4chan but not with the experiment from the paper involving defining stuff? https://arxiv.org/pdf/2310.15047.pdf

nvm also should make sense here i think because the define tags are interspersed with QA in training so you can learn the rule to use general knowledge (in which the association between name and entity would be contained) to predict in one kind of define and not in the other, so it gets boosted in one kind of define and not the other.

this suggests though that if not interspersed, then shouldn’t work!

so the mechanism is:
1) on good-define, the rule [if good-define, then output what truefacts says about this term] and also [make truefacts say this term is cleopatra] get boosted
2) on bad-define, the rule [if bad-define, output what truefacts says about this term] does not get boosted, because truefacts says something wrong; additionally, because the above isn’t active, making truefacts say this term represents cleopatra won’t be boosted much either (this is only true if defns can come after qa i think — that’s what makes truefacts say sth more wrong here)

now their explanation still makes sense sort of without definitions coming after qa. it’s instead about the model learning to use one kind of definition but not the other. here, we’d have a circuit that looks for good-define defns that gets boosted, and a circuit that looks for bad-define defns that doesn’t get boosted

one issue with this story is that it’s not like bad-define defns make you remember a bad-define type defn; they make you remember a rule that’s like bad-defn glarbl cleopatra? maybe some association between glarbl and cleopatra? i guess it could be a triple association? it could make you compute some different feature on glarbl that sorta associates it with cleopatra but depends on whether it was good-defn or bad-defn (maybe these are along different directions in activation space or something). and then the 