* we want it to have some fixed structure, with content being filled in
	* content could be: "models", propositions, truth values, probabilities
	* it is unclear if the following can be allowed as content, because this undermines the idea that there is really a fixed structure: methods, tricks, policies, attitudes, skills, propositions/models/[truth values]/probabilities about your own activity, goodness-talk
* let us say that we want it to be answering questions
* we want its answers to questions to be "decently correct" forever
	* and we want to be able to see that they will be correct ahead of time
	* what "decently correct" means precisely is set by the requirement that it never makes catastrophic mistakes, i guess?

# some thoughts on whether this can be done and how to do this
* things become much nicer if there is a protected top-level structure. like, if there is some structure of the program which cannot be broken. eg every $10^{6}$ steps, some check is run. eg before accepting a mathematical statement as something to be acted on, a proof needs to be provided. and no part of the program is able to destroy or subvert the part that checks that a proof is provided (an example of subversion without destruction would be making it so a certain function call is never exited, so effectively you had a cancer take over until the end of time)
	* i think we should just grant this for free for now, and worry about this being potentially very tricky later
* can we set up something good for math?
	* we can just have a proof search that finds a proof/disproof of a statement by brute force and then halts. this gives a system which answers mathematical questions alright — at least the provable/disprovable statements will eventually be judged correctly  (assuming ZFC is sound)
* if we have something good for math, then we also get something good for anything such that math-soundness is sufficient for being good at that thing. maybe this includes certain crisp worlds already? like, you can just think about doing stuff in a video game? you can check that a certain action sequence does something?
	* it might make sense to think this through in say chess, then minecraft, then when plugged into any reasonable video game at random
	* are we imagining there being something that the AI is supposed to do in each game? 
* 

