

On the aims of technical work that aims to decrease x-risk from AI:
1) Conditional on there being no major global governance intervention, I don't see any other option for the future going well [after the creation of artificial systems which are better at general reasoning than the best individual humans (and which do it cheaper)] other than 'the good guys' needing to build safe general-scientist-AI, or at least having AI speed up scientific research and engineering $100\times$ across the board (perhaps with humans in the loop).
	1) 
2) To contribute to solving the technical alignment problem, we need to come up with a way to make a system which can safely conduct novel research or help humans conduct research much faster. More precisely, say we want to make a 'marginal unit of research' to have $1/10$ its current cost.
3) A concrete baseline to beat 

## messy questions

is the way in which the plan is supposed to radically transform the world mainly that it involves creating a method for formalizing problems better? 

i feel like for lots of the examples, rlhf would just work to the extent that the strict thing would work? eg with self-driving cars, there is something you can get to with usual methods, and I can see how this would maybe also give you that, and then there's something where the 'car really needs to be understanding stuff to drive that well' which is not attainable by this nor (safely) by usual methods
## hyperparams


The arguments below will be about 
* an argument: For a general domain, getting the right notion of harm / expected utility into a guardrail seems about as difficult as the full problem of AI alignment.
	* For example, if a guardrail is implemented using a world-model which can be queried i
	* a counterargument: In this setup, we don't need to 
	* 
* Formalizing all problems in


* If the agent knows about the guardrail or can simply notice the effects of the guardrail (in particular, if it can notice patterns in which past actions fail to have an effect on the world (because they got rejected by the guardrail) — note that it doesn't need to explicitly 'know about' the guardrail for this to be the case, https://www.lesswrong.com/posts/XWwvwytieLtEWaFJX/deep-deceptiveness), and if the guardrail is not 'kept in training against the agent', then it seems likely that even a 'much weaker' agent would 'hack' a guardrail (related: https://goattack.far.ai/).
* If the agent doesn't know about the guardrail 

in the ambitious version, what's the best proposal for training this system that can be asked to output conditional probabilities about outcomes given actions, all specified in natural language?
* i guess we can ask a simpler question: how would we formalize informal math?