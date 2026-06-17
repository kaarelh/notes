
maybe this is a good angle — i think i hadn't thought this through clearly before: you could hope to understand a neural net in terms of what problems it is solving / what questions it is answering. like, on the way to doing the thing it is supposed to be doing, it might be solving some subproblems (such as computing certain functions of the present context/input, certain features, but also perhaps making some judgment calls about some thinking-things, such as what sort of model to use in the given context (this is kind of also "a feature of the input", but it's a pretty weird one), tho idk if anything that sophisticated would actually be happening inside our NNs at present)

# Understanding a program (or a neural net? or a mind?) in terms of what it is determining

Consider a program of the most standard kind in theoretical computer science: one that takes a specification of some kind of mathematical object as its input and gives some other related mathematical object as its output. Some examples:
1. We could have a program such that when one inputs a boolean formula[^1], the program outputs whether it is satisfiable[^2].
2. We could have a program such that when one inputs a graph with real-number-valued weights on edges[^3], the program outputs a complete weighted graph which, for each pair of vertices, displays the shortest distance between them in the original graph.

Here, we are already understanding these programs in terms of what they are doing. Like, one can write down a formal sentence specifying what the output is (by just making the respective above sentence precise). This is a very different object than a specification of how to compute the output! The sentences above say nothing about how to compute these things!

Ok, now one might want to understand the program better — perhaps imagine that you already understand how the program works and you are explaining how it works to your friend. I think an important class of thing you will be saying is "the variable x tracks the truth of the proposition $P$". A bit more generally, we have "the variable x is f(blabla)". A hypothesis is that the majority of your explanation of what a typical program does will be of the form: a sentence saying what a variable tracks, together with an argument/proof that it tracks what you claim it tracks. Let's think about how we would explain a brute-force SAT solver (I will specify it now, and you should be tracking HOW I'm specifying it):
* We have a variable initialized with c="unsat", tracking whether a satisfying assignment has been found yet.
* We loop through all $2^n$ options of assignments to all the variables.
	* More precisely, let's say we do it by thinking of an assignment as a binary number between $0$ and $2^{n}-1$ inclusive in the obvious way, adding $1$ each time to pass to the next option.[^4]
* For each assignment, compute the output of the formula on the assignment.
	* We could do this by:
		* first plug all values into the formula string
		* then, search for a left paren which is followed by a right paren. replace this entire parenthetical with its value (including getting rid of the parens). repeat until no parens are left
* If it outputs 1, set c="sat".
* Once done with the loop, output c.

Our hypothesis doesn't quite look right — the surface description is more in terms of procedures/tasks. But most of these procedures/tasks are in fact well-understood as determining some variables? hmm. there's perhaps problematic metalanguage like "has been found yet", like the program tracking stuff about itself. maybe that's not problematic. i also found myself often wanting to use "intentional language", eg the words "guess", "try", "check".



some other examples:
* we can think of a mathematician working on a problem as determining mathematical facts
	* but they are also doing other thing!
* decomposing someone's usual workday into doing various tasks
	* some example tasks: cleaning a room, learning about the singular value decomposition, proving a lemma, coming up with a toy model of something, identifying some hyperparams a toy model should have, writing an email, coding a function


## What a program/NN/mind is determining can be different [on different inputs]/[in different contexts]

When you are doing something (in particular: when you are answering a question), you typically do not answer the same auxiliary questions on the way. While it is conceivable that you would start by answering the same initial question or two, even if you do that, you typically then very quickly end up thinking about very different questions depending on the answers to the first questions you answer. We can easily write down programs that do this, as well: there can be an if statement specifying whether to continue in one way or another. Most programs do some amount of [determining different facts]/[solving different problems] on different inputs. And it isn't too rare to have a program that carries out $\approx$completely different investigations depending on the input. For example, we could have a SAT solution finder that that carries out [one approach to finding a solution if the formula is in 2-SAT form](https://en.wikipedia.org/wiki/2-satisfiability), and [another approach](https://cstheory.stackexchange.com/questions/25390/complexity-of-solving-linear-equations) if the formula looks like a conjunction of XORs,[^5] and otherwise tries various [heuristic approaches](https://en.wikipedia.org/wiki/Boolean_satisfiability_algorithm_heuristics) to guessing a solution (perhaps with some more decision rules specifying which ones to try or which order to try them in), and if everything else has failed, does a brute-force search for a solution.

In a sense, it is extremely natural and obvious that any system handling sophisticated problems will be doing different things when handling different problems! But there is also a starting point from which this can be somewhat surprising: if you think of a neural net as a circuit (either just manifestly, or under some translation), then maybe you'd expect the same variables to be computed on each forward pass? It could be helpful here to consider how a Turing machine with a runtime bound can always be unrolled into a circuit that simulates [the contents of its tape and the position of its pointer] at all time steps.[^6] Whether tape cell $13$ has a $0$ or a $1$ written on it at time step $42$ is in one sense the same variable on any input, but in another sense it can easily represent very different variables of the program on different inputs.

Two remarks on how the current (March 2026) field trying to understand what AIs are doing relates to the issue of an AI doing different things on different inputs:
* The currently prevailing view in interpretability allows for this to some extent: it is common to [think of a big transformer language model as doing various different things depending on the context/input](https://www.lesswrong.com/posts/exp4JGPJu46g6sdRp/a-starting-point-for-making-sense-of-task-structure-in). But the prevailing view still takes there to ultimately be some pre-determined finite list of variables (I mean: corresponding to SAE features) that could be getting determined in a model, and I think this is probably a defect of that view, because a system solving an open-ended variety of complicated problems should be able to determine [what auxiliary problems to solve]/[what auxiliary questions to answer] on the fly.[^7] (I should note: maybe it is not clear that a forward pass of a transformer is sophisticated enough for this to be true of it?)
* The currently prevailing view in understanding what an AI is doing across many forward passes (like, as it writes a chain of thought) 



* issue with internal properties, internal tasks. eg probabilities assigned to sentences. eg proposition truth values in the first place! especially normative ones ("i should investigate this")! eg text of law written by parliament to address issue. eg just think about the various tasks, jobs, teams inside a company. in general a task makes sense in relation to a system of tasks. it provides something to some other tasks. it can be very hard to understand a task wrt the outside world only. since each task needs to be understood in relation to other tasks, tasks sort of need to be understood all at once
	* however, there is sort of a canonical path to understanding all the parts despite this interdependence: you can understand them in their order of development. there is some initial working thing relating to the world, in some simpler way. then additional parts get built. the new parts do something helpful that can be made sense of if the existing parts are already understood. maybe think about the design of some familiar technology that has developed for a long time, like a cart/carriage/car. 

can one specify a good loss for this?
* of course there will be an issue with alien stuff as always in such cases. like, shortest descriptions are cursed, "shortest concepts" according to some loss are cursed, etc.. nice things are much more properly human
* ok but still what loss does at least something related. idk what a nice task decomposition means i guess. we could say that we make a bunch of claims about variables the program computes, and then give a bunch of arguments for those claims. but which such decompositions are nice? well first, the variables actually need to be computed by the program lol; we could say they have to be easily readoffable, tho this probably doesn't well-capture the intuitive thing. second, it should be nice to argue that the program computes all these variables, with the arguments for some variables depending on the claims for others. we could require the right dependence under interventions i guess?

can one prove this:
* if a program is in a certain format, any lowest loss interpretation are close to the "true" one

[^1]: presented in a predetermined format
[^2]: That is, whether there is any assignment of $0/1$ to the formula's free variables which makes it evaluate to $1$.
[^3]: presented in a predetermined format
[^4]: maybe should make this less hacky
[^5]: a classification of easy cases of SAT: https://en.wikipedia.org/wiki/Schaefer%27s_dichotomy_theorem
[^6]: If you don't know what I'm talking about, it might be helpful to look at a proof that [the two canonical definitions of P/poly are equivalent](https://blog.computationalcomplexity.org/2005/09/ppoly.html) or at [the usual proof that SAT is NP-hard](https://en.wikipedia.org/wiki/Cook%E2%80%93Levin_theorem#Proof).
[^7]: I think there are also various other defects. As I've been saying for 2+ years, the current view was obtained via iteratively applying small modifications to "maybe neurons are a good basis" while optimizing interp scores, which is completely stupid and has a negligible probability of giving anything principled/"real"/good/interesting. But discussing this further is outside the scope of this note.
