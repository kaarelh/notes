
ok, so the world-model which the guardrail has lets it evaluate p(harm|action) correctly. why not just let the guardrail evaluate p(no harm and desired outcome | action) and pick some action for which this is reasonably high instead? (as high as the best action would be for the agent, say)

how does scaling up the guardrail help us? it seems plausible that 

question to ask: It seems like the proposal is to hand-craft the formal language, and still to have a way to translate ethical properties into this formal language. This seems really hard!! two subquestions:
1) can you say something about how this language that can talk about ethics would be constructed by us?
2) can you say something about how a translation data set (or something like that) would be compiled? assuming we want a neural net to perform this translation

Like, I can see how a formal language would be created for mathematics, but it seems much harder for science and for ethics. I'm guessing you would think it's maybe easier for science than for ethics, and maybe we disagree re science, but I'm guessing you agree that this seems really hard for ethics? Even if we have a language, how would a data set of formalizations be created so that a neural net can learn to translate? Wouldn't we be really worried that we've not captured something correctly?


some more discussion of 

# 2024-06-19

We would like to be able to train an autoformalizer with an unsupervised loss so we can train on a data set of informal math for which we don't have corresponding formalizations.
* It remains unclear whether we have a way to combine a small labeled data set with a large unlabeled data set and get much extra (compared to just training on (and/or prompting with) the labeled data set) out of training on the unlabeled data set without the model going crazy — i.e., without it starting to produce wrong formalizations to make some unsupervised loss term small
	* For example, it could get good autoencoder loss by preserving all the characters of the informal statement in the translation in some silly way, and knowing how to translate back.
		* This could potentially be avoided by some compositionality requirement, but this could potentially also be hacked.
	* For another example, it could get good implication structure preservation loss and good truth loss by translating everything to simple true statements. (If $B$ is easy to prove, then $A\implies B$ is easy to prove as well, regardless of $A$.)
* Maybe this can be improved by only using the unsupervised training signal with sentences for which we can tell that there's already a reasonable chance of correct translation.
	* One potential way to do this would be to use the logprobs the model gives on the labeled data as a way to tell which kinds of data points it can handle decently already, maybe extending this to unlabeled data using some clustering? (This could also be human clustering of statements into field-of-math/difficulty?)

We don't know of great empirical evidence on how well current best LLMs would do, in particular when prompted or trained with existing labeled data.
* While the results from https://arxiv.org/pdf/2406.06555 might look poor at first (from the fraction of correct formalizations), it's maybe not that bad because there are a larger fraction of formalizations which are almost correct and there are simple ways to plausibly improve the results by a lot (prompting, fine-tuning).

There's a bit-counting argument against an infrabayesian decision rule or the intuition that while it might be very hard to get the right notion of harm, it's maybe feasible to find a set of notions which contains the right notion of harm and then act in a worst-case manner wrt that set.
* Briefly/vaguely, the argument is that if we start from harm taking $1000$ bits to specify, then we might need to pin down like $980$ for the set of theories so as to not make every theory have probability $1-\varepsilon$ of worst-case harm (which would probably cause weirdness), but getting $980$ bits right seems roughly equivalent to getting $1000$ right (in that if we had a method which gets $980$, it would probably pretty much get $1000$)? 
* So maybe we just want to minimize the probability of harm in a non-worst-case way instead, or just pick an action which maximizes EV.
	* To do this better, maybe we'd like to not just have a neural net that outputs heuristic probabilities/expectations of various variables conditional on actions, but also a way to estimate the variance in a variable under 'thinking longer', i.e. doing some appropriate coherence training to improve the heuristic guess for a variable, so we can decide whether we should use more compute to improve our estimate before acting. 

# Some questions on autoformalization

high-level question: How and how well can we automate formalizing math papers? some sub-questions:
* How large is the largest data set of informal mathematical statements and their formalizations in Lean? (Does another formal language have a larger such data set?)
* How well can current LLMs autoformalize with good prompting, maybe when given access to a Lean compiler and asked to check its formalizations?
* How well can current LLMs check autoformalizations (again with good prompting)?
* What about LLMs fine-tuned on math or fine-tuned on formalization in particular? What about a model RLHF-d to formalize?
* Could current automated theorem-provers fill in a meaningful fraction of the gaps in informal mathematical proofs? (One reason this is relevant is that this is necessary for a certain kind of unsupervised training to get going at all.)
* Does it make sense to turn a math paper into a directed graph where each vertex corresponds to a sentence and each edge corresponds to a dependency claimed by the paper? (More precisely, maybe we will want each sentence to have a short proof from the AND of its parents, plus maybe some background theorems. Or maybe we want the implication from the AND of a sentence's parents to the sentence to have high heuristic probability.) Are sentences not the right units for this because they aren't sufficiently self-contained in usual mathematical writing?