* sometimes we use analogies between mathematical objects
	* eg random model of primes. eg thinking of a graph, maybe an expander graph, as an erdos-renyi random graph with the same density. or maybe some more sophisticated random graph model
* this looks like sth we could just well-define. or at least we can write down a concrete thing that probably doesn't remotely capture the whole thing, but still captures a bunch of interesting stuff
	* specifically, we can just have two mathematical setups, and laws bridging between them
		* maybe we say objects go to objects, relations to relations
* can we say something about this sort of thinking being trustworthy? i think probably fully generally it probably just isn't trustworthy — like my guess is that one can't build a robust verifier for this. but not sure
	* an obstacle is that one probably just can construct an object that has whatever 10 properties of the first object but gets property 11 wrong
	* hmm ok actually sometimes property 11 is logically constrained by the first 10 properties. hmm or actually no this shouldn't be true for arbitrary analogies, because these are allowed to just shift the properties right!
* could we have some sort of solomonoff-like result here?
	* like, you have some mathematical object A, and you want to know if it has property P
	* there are also properties Q_1, Q_2, ..., Q_m
	* you consider all the other mathematical objects B_1, B_2, ..., B_n. for each, you know some property values
	* you then draw some inference about A based on the property values of the other objects. how should you do this? I guess one option would be a linear regression lol? or you could use a small circuit with good accuracy
		* btw open question: in circuit induction, how to trade between simplicity and accuracy? the standard answer is to require 100% accuracy, but is this right? maybe one could say it depends on the data-generating process? or maybe requiring 100% correctness does well even if the data-generator eg has some random errors on top?
	* that's an interesting model of induction. i guess we often do model-based reasoning in math with only a single model that is a great match though? 