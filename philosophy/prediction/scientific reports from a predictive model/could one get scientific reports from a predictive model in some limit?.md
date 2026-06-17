
title: some limits of predictive models

we could consider the following predictive models:
* solomonoff induction
* the smallest turing machine with given input-output pairs
* a version where we also care about time/space complexity
* a circuit version

questions:
* suppose you take all proven/disproven mathematical statements (written formally in ZFC) together with their shortest possible proofs/disproofs (in some given system for writing formal proofs in ZFC), and "train" a predictive model on those. does it resolve the riemann hypothesis?
	* answer: certain yes in the function case; idk probably also yes in the sequence case?
* suppose you take all proven/disproven mathematical statements (written formally) together with their human proofs (written formally), and train a predictive model on those. does it resolve the riemann hypothesis?
	* answer: probably not
* suppose you take all proven/disproven mathematical statements (written formally) together with their human proofs (written formally), and train a predictive model on a subset. does it resolve the other problems?
	* answer: hmm maybe? need to think more
* suppose you are trying to get a model to learn 


vague questions:
* can we say something general about predictive models trained on data satisfying a property outputting stuff which satisfies a property vs not?

# working out some cases


## predicting the data sequence from a human
Alice is doing research.
* Collect all of her text outputs, and do Solomonoff induction. Do you get research progress?
* do this with a more realistic predictive model. how strong does the predictive model need to be to give research progress? i should work out some heuristic calculation here.
	* one major issue is that the predictor is asked to track all sorts of nonsense, whereas Alice is focused on what matters. the predictor might need to have a lot more compute than Alice to get there?


# confusing things

* it feels like stuff depends on the "computational power" of the entities/universe involved compared to the predictor?
* if you're computable, you might reason about solomonoff induction as if it were fixed, but actually your decision could come logically first with solomonoff seeing that! should maybe work out a concrete example here?
	* i mean it's just that if you could supposedly tell what solomonoff predicts will come next in some sequence by thinking about it, you could just put the other thing next in that sequence, and that will mean solomonoff made the wrong prediction about that sequence, and that also provides a contradiction for some sequences (the sequences such that sth so-far-equivalent to implementing your-universe-with-a-pointer-at-the-sequence is the shortest program which predicts that sequence)