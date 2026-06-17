
https://www.overleaf.com/project/6893c94857c892cfab21ec64

* consider eg the riemann hypothesis example
* an argument that solomonoff does generalize well: a human with the right prompt thinking for a long time could generalize well, and that's computable (or well, it could maybe be — we might want to ignore quantum mechanics here)
	* there's an issue here with the human not just doing the ood prediction at the end, but also needing to somehow do the previous stuff. maybe the algo we need to imagine is a combination of a compute-bounded solomonoff inductor together with a human for ood stuff? 
* of course, it might just have much lower weight than stuff which doesn't generalize to giving a proof of the riemann hypothesis
* but maybe one can say: ok but across many ood generalizations, solomonoff can't lose to this humanlike inductor by that much!
	* is this interesting? is it saying more than: if you set things up such that you're no longer ood compared to the previous stuff, then you can win? is it more interesting than: if you make a data set as a human by keeping flipping coins about whether to continue or not, then maybe solomonoff succeeds?
* whenever there is another generalization which is ood compared to all previous ones, you might just get fucked. and maybe you probably do?

an argument:
* you can do prediction of the text written by a single human. to the extent that this human will generalize well, so will solomonoff, after some amount of data
		* i guess this human will be given by a probabilistic turing machine? or do we need to be more quantum than that? and after some point the universal semimeasure will stop losing to the correct way to predict that probabilistic TM?



* hypothesis (weakly held): for solomonoff, ood generalization is a thing, but easy-to-hard generalization is not. ahh idk if that's the right thing to say. maybe it's more like: true ood generalization is not a thing for solomonoff. there is "fake ood generalization", which is where you've already seen many "ood generalizations" of the same kind. maybe it's like: on the object level okay you have some new types of inputs, but you've already seen "this sort of shift" many times, so it's not new in some more meta sense
* whenever there were helpful properties that made the task easier on train data compared to test data, you’re fucked(?)

you can run a compute bounded SI inside solomonoff that is additionally conditioning on the property verifier (like, for the property of interest). you will need to code the sequence so far, but this can be done at its kolmo complexity, right? should think thru the details carefully here. if the property is simple, i think this comes close to implying kolmo doesn’t do that poorly on that property?
