
# context

I thought some about reverse-engineering scheme hyperparams I think we could get meaningful feedback from toy models on. I think the list below could also be helpful for estimating the probability of guessing the hyperparams correctly enough to figure stuff out in practice without studying more toy models first

# content

I claim that:
1) to understand (be able to fully reverse-engineer, translate into a hierarchy of structures, etc.) neural nets, it would be very helpful to be less confused about the questions below;
2) and studying a 'rich class of toy models', or multiple successively more complicated/realistic classes, would be a good way to become less confused about them. (E.g., learning boolean functions, or maybe something else which has properties we believe to be important for being sufficiently similar to the models we care most about in practice.)

(The list of questions is not at all complete — I think I spent about 1.5 h writing in total and decided to finish without feeling like I hit a significantly diminished pace compared to when I started. One could easily go into much more detail on anything here. Also, many things here are obviously unoriginal — in particular, it's definitely joint with Jake, Dmitry, Lucius.)

* How are variables represented in NNs? What kinds of variables does a NN operate with?
	* Do variables live at single layers and/or token positions? Or are they spread across multiple layers or token positions?
	* Should we decompose activation vectors into linear combinations of f-vectors, with coefficients that capture the values of the respective features? How should we do this decomposition?
		* Are features sparse or dense? Or maybe some are sparse, and some are dense? Can we find any toy cases where superposition shows up without being baked in?
		* For the intermediate case, would something halfway between SVD and SAE work?
		* Should we use some information-theoretic thing, like maybe the negentropy-based versions of https://en.wikipedia.org/wiki/Independent_component_analysis?
		* What are SAEs learning (e.g. when features are really dense, if that's the case)? What is the SVD picking up?
	* Or maybe features can be read off, but activation vectors aren't linear combinations of features (e.g. activation vectors could be what you need to get future readoffs right plus noise).
		* How do we find these readoffs? (Can also ask many further questions like above.)
		* Do features tend to be supported on sparse sets of neurons (as suggested in Neurons in a Haystack)?
	* Or maybe we should think of the right readoffs for variables that would show up in a circuit as simply telling us the bit in a certain memory location, and maybe these might not be semantically that meaningful?
		* For example, consider what happens when you take a polytime turing machine and turn it into an equivalent circuit for inputs of length $n$ — the variables in this circuit would correspond roughly to particular tape locations at particular times; the value of such a variable would be the token at that tape location at that time (ok, we also want to include information about whether the head is at that tape location here, as well as the state of the finite automaton in the TM specification at that time, but let's forget about that to make the point simpler). We can imagine a turing machine that could enter one of $10$ different subroutines and come to write the same token on the same tape cell in any of these subroutines, but these would mean entirely different things depending on the context. (Ok, actually understanding that the variable value would also contain the finite automaton state and whether the head is there softens the point somewhat; I think it roughly still works because we could also specify the subroutine elsewhere on the tape, not in the automaton state, just be warned that this point is really a bit weaker than the unsophisticated version might make it seem.)
	* Are variables represented in single layers, or across layers? Should we take all positions to store the same variables, or somehow context-dependently different ones?
	* Are variables better seen as being represented in the difference from some mean? Maybe the activation on a given input at the beginning of training?
	* Should we abandon understanding NNs in terms of such local variables at all, and try something quite different?
* How does computation happen (in terms of these variables)?
	* Are operations implemented layerwise?
	* What kinds of operations do we see?
	* Is the model learning a task classifier together with a rule to apply for each task at all something that happens in toy cases?
		* How do we find this task decomposition in toy cases?
	* What do circuit-finding methods do in toy cases? (I think it's likely one can produce some compelling cases where current methods, especially with mean ablations, miss most of the interesting stuff?)
	* If superposition is legit, does computation in superposition ever happen? How is it implemented?
	* What does SAEing gradients do? Does that find modules/skills/quanta in some toy cases?
	* Should we look at weights or at the difference of weights from initialization (if the total distance moved is small compared to the initialization scale)? Or something else entirely?
	* Which architectural changes make learned toy circuits cleaner?
	* Are attention heads moving stuff around, or are they doing cross-token computation?
	* What kind of computational structure does interchange intervention training create in a toy setting?
	* What does ROME do to the computational structure in a toy setting? Is it like implementing a loud override, or does it fit nicely in the existing structure?
	* How/why does activation steering work? (It seems plausible we could come to understand how it works very well in some toy setup.) How do patchscopes work?

Here are some more questions which feel less specific to reverse-engineering neural nets, but are still interesting (both scientifically and practically) and which I think studying toy models could provide a good amount of information per unit of effort on:
* Can neural nets learn deep circuits at all?
	* Can transformers learn deep circuits at all?
	* When tasked with learning a deep circuit, does a neural net just learn a shitmess of shallow heuristics for the deep circuit?
		* In cases where small/shallow heuristics are unavailable, does a neural net struggle to do any better than chance? E.g., for an XOR of k bits, no statistic computed from k-1 bits will give you any information about the output. And neural nets indeed struggle to learn XORs (I think people have proved matching upper and lower bounds, saying one needs $n^{\Theta(k)}$ steps of gradient descent here).
		* Whenever a deep circuit gets built, does it more or less need to get built out of parts 'which make sense individually'? Does this mean that curriculum learning is very important for building interesting circuits (concrete easy-ish question: does giving the right curriculum speed up learning a big XOR)? Is training a sequence of small groks where new gates get learned, things done differently starting to get done in a unified manner?
* Are neural nets pretty much 'just gaussian processes'?
	* If yes, wtf does one do to 'interpret a conditioned gaussian process'?
	* If not, what are some 'things that a neural net can do, but a gaussian process can't'?
* What would a good (probably physics-y/heuristic) theory of how neural networks learn stuff look like? Maybe we can determine a number of hyperparameters of such a theory?
	* For example (this is suggesting things I currently like, but one could also list a bunch of questions that seem good from other points of view):
		* Maybe a large ensemble of circuits computing a boolean function compatible with input-output-pairs thus far starts getting built all at once, together with some circuits implementing smaller/shallower patterns.
		* Or maybe only shallow patterns start being learned initially, and deeper circuits can only be formed iteratively out of these shallow patterns (sort of like Dmitry and Nina's unpublished (?) modular arithmetic work).
		* Maybe each circuit can be analyzed individually, especially in some regime where the different circuits still being built are almost orthogonal?
		* Maybe one can write down some heuristic 'mean field theory' differential equations for individual circuits being formed that capture empirical data reasonably well?
	* In general, what governs generalization vs memorization?
		* What does running off to infinity in a memorizing direction look like? Can we characterize when that happens?
		* What are some examples of toy settings in which SGD gets stuck in local optima?
		* What's the role of weight regularization?
		* Can we decompose gradients to see the memorizing and generalizing 'circuits' way before they are formed?


I think it is likely that when we study a rich class of toy models, assuming we will indeed come to understand them, we will not answer many of these questions, but instead realize that many or most of these questions are sort of confused. So, the hope isn't really to answer these questions, but the questions wiser versions of ourselves would have asked instead. Still, I hope that considering the list of confused questions above can give us a better sense of what / how much we might learn from studying toy models.