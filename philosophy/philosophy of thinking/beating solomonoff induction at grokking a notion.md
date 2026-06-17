
* how come as humans we can understand what someone means when using a word. as opposed to becoming a predictor of what they would say. it is possible for a human to not make the mistakes another person would make when eg classifying images for having dogs vs not! roughly speaking solomonoff would be making the same mistakes the person would make
	* this is a classic issue plaguing many (maybe even most?) things in alignment. eg ELK, AGI via predictive modeling, CIRL/RLHF or just pretty much anything involving human feedback
* can’t we write an algo for that, and have that not be dumb like solomonoff is dumb
* some ideas for ways to implement a thing that is good like this / what's going on in making the human thing work:
	* an even stronger simplicity prior than solomonoff. eg if there are explainable mistakes on a simple model, you want the simple model that doesn’t predict the mistakes. this will have inf log loss but let’s just do a version of the simple hypothesis with noise, and then penalize the likelihood term less. have people not already considered this for solving the model + data split problem? does this attempt to solve the model data split problem introduce some pathologies?
		* you have pathology of not specifying even the hypothesis in the seq prediction case (like it’ll be better to drop bits and take the likelihood loss). but i think at least this pathology is not present in the function case, if we don’t get randomness in the universal semimeasure way (like if we make the randomness not shared between different inputs — each input has to sample its own random bits)
		* alternatively: just set abs bound on model complexity, rest has to be likelihood. this feels bad because if you get the bound wrong you get some nonsense. that said in a sense this is equivalent to the previous proposal (like if you pick the length bound the previous thing with some hyperparam would find). idk maybe in the function case you can look at how many bits of entropy are left given the hypothesis, like imagine this graphed as a function of hypothesis length, and like see some point at which the derivative changes or sth. (this doesn’t show up in the seq case because there it’s pretty much just 1 bit paying for 1 bit (until you specify it in full if it’s finite complexity))
	* simplicity prior defined in terms of existing understanding
	* you specify properties of the thing or notion sometimes
		* eg [concrete] and [abstract] make a partition of things maybe, but [alice would think this is concrete] and [alice would think this is abstract] might not. eg knowing [if something is abstract, then it usually helps a lot to study examples to understand it] can help you understand when your teacher alice is making a mistake about an abstractness claim
		* or eg: 1+1=2 won’t be true if you accidentally assign 1->rabbit and 2->chicken from a demonstration (for any reasonable meaning of plus)
	* some sort of t complexity bound might help. tho really you aren’t gaining a mechanism when you learn what a dog is. you are more like learning a new question/problem
	* also as a human one can just ask: what is it that this person is trying to teach me. what is this person trying to point at. this is a question you can approach like any other question
	* when we gain a notion, we gain sth like a question that can be asked about a thing. and we have criteria on this notion. we gain "inference rules"/"axioms" involving the notion. ultimately we are wanting it to play some role in our thought and action. that role can guide the precisification/development/reworking of the concept. the role can be communicated. it can be $\approx$shared between minds
		* to gain the chair notion is to gain the question “is this a chair?”. this has an immediate verifier (mostly visual), but also further questions: “can i sit on it?”, “is it comfortable to sit on it?”, “would i use it when working or dining?”, “does it have a back support part and a butt support part and legs?”. a chair should support the activities of sitting and working and dining. all these can have their own immediate verifiers and further questions
		* we understand "is this a chair?" as clearly separate from "would the person who taught me the chair notion consider it a chair?". it is much closer to "should the person who taught me the chair notion consider it a chair?". it is also close to "should i consider it a chair?"



important basic point here: our dog thing is NOT a classifier. classifiers or noticing trick circuits can be attached to our dog structure but the structure is not a classifier

toy problem here: how do you pin down the notion of a proof? (how did we historically?) how do you pin down the notion of an integral? (how did we historically?) maybe study these actual examples

pinning down the notion of a proof might be a good example to study in detail. like, how does one become able to tell whether something is a good proof? a valid reasoning step? how does one start to reason validly? one reason to be interested in this is that it's analogous to: how does one become able to tell what's good, and come to act well? both are examples of getting some sort of normativity into a system

another example: we have a notion of truth, not just some practical thing like provability (or in a broader context supporting action well maybe). our notion of truth is separate from our notion of provability eg because we have the "axiom/principle" when talking about truth that exactly one of a sentence and its negation is provable, or alternatively/equivalently we have an inference rule of going from "P is not true" to "not-P is true", and such a rule is just not right for provability (there are sentences such that the sentence and its negation are both not provable). by gödel's completeness theorem, i guess a fine notion of truth, ie one which has a model, is precisely one which assigns 0/1 to all sentences and is coherent under proving. we operate with truth by relying on these properties, without having a decision algorithm or even a definition for truth (cf tarski's thm). 
## how did we understand what an integral is?

i think we were using integrals for like two centuries before we knew how to properly define them (eg via riemann sums). how come we were pretty successful with that? like, how come we did all this cool stuff, we came to all these correct conclusions, without properly knowing what integrals are? i think the general thing that happened is that we hypothesized an object with some properties and these properties turned out to be those of a real thing, and in fact to pin it down uniquely! though of course this leaves the following important question: how did we identify this set of properties as important?




# messy notes

I agree with your point in the canonical solomonoff sequence prediction case. I think that's what I mean in the note by "you have pathology of not specifying even the hypothesis in the seq prediction case (like it’ll be better to drop bits and take the likelihood loss)". I think this pathology is maybe not present in "function solomonoff" (I state this in the note as well but don't really explain it), though I'm very much uncertain.

to state the hopeful claim in more detail:
* By "function solomonoff", I mean that we have a data set of string pairs $(x,y)$, and we think of one hypothesis as being a program that takes in an $x$ and outputs a probability distribution on strings from which $y$ is sampled. Let's say that we are in the classification case so $y\in\{0,1\}$ always (we're distinguishing pictures $x$ which show dogs vs ones which don't, say).
* The "canonical loss" here would be the length of the program plus the negative log likelihood assigned to $y$ summed over all $(x,y)$. What I'm suggesting is this loss but with a higher coefficient on the length of the program than on the likelihood terms.
* Suppose that the distribution on $y$ is given by "a simple model" of $100$ bits which predicts $100$ bits per specification bit, on top of which there is a "systematic error model" of $100$ bits which predict $10$ bits per specification bit. I'd want a setup which just pulls out the "simple model".
* In the sequence prediction case, if you penalize the hypothesis more than the log probs, I agree you'll just give a hypothesis which is like the usual universal distribution and leave everything else in the likelihood term, which is not the behavior I'm looking for.
* But in the function case, I think you maybe don't get this pathological thing? If you try the same pathological hypothesis, the problem is that you have to pay the likelihood term separately at every $x$. Like, when you already predicted $y_1$ given $x_1$ and now you're predicting $y_2$ given $x_2$, you can't see the "random bits" you used in the first instance. In our example, this pathological hypothesis has some small complexity, let's say $\approx 0$ bits for simplicity, and gets like $200$ bits of likelihood loss per $x$. The hypothesis I'm hoping to pull out has complexity $100$ (the "simple model" gets put in the hypothesis) and gets likelihood loss $100$ bits (it pays for the $100$ bits of systematic error in each likelihood term). Then there is also the $200$ bit hypothesis that just specifies the simple model and the systematic errors, paying $0$ in likelihood. 

Or maybe you have some different "bad universal hypothesis" in mind for the function case? Also, I'll note that even if this pathology isn't present in the function case, I consider it very much plausible that there is some other pathology, but I haven't seen one yet.



I agree with your point in the canonical solomonoff sequence prediction case. I think that's what I mean in the note by "you have pathology of not specifying even the hypothesis in the seq prediction case (like it’ll be better to drop bits and take the likelihood loss)". I think this pathology is maybe not present in "function solomonoff" (I state this in the note as well but don't really explain it), though I'm very much uncertain.

to state the hopeful story in more detail:
* By "function solomonoff", I mean that we have a data set of string pairs $(x,y)$, and we think of one hypothesis as being a program that takes in an $x$ and outputs a probability distribution on strings from which $y$ is sampled. Let's say that we are in the classification case so $y\in\{0,1\}$ always (we're distinguishing pictures $x$ which show dogs vs ones which don't, say).
* The "canonical loss" here would be the length of the program specifying the distribution plus the negative log likelihood assigned to $y$ summed over all $(x,y)$. What I'm suggesting is this loss but with a higher coefficient on the length of the program than on the likelihood terms.
* Suppose that the classification boundary is most simply given by what we will consider a "simple model" of complexity $100$ bits, together with "systematic human error" which changes the answer from the simple model on a $2^{-10}$ fraction of the inputs, with those inputs taking $10000$ bits to specify.
* If we turned this into sequence prediction by interleaving like $x_1,y_1,x_2,y_2,x_3,\ldots$, then I'd agree that if we penalize hypothesis length more steeply than likelihood, over getting a model which does not predict the errors, we would get a universal-like hypothesis, which in particular starts to predict the human errors after being conditioned on sufficiently many bits. So the idea of more steep penalization of hypothesis length doesn't do what we want in the sequence prediction case. But I have some hope that the function case doesn't have this pathology?
* Some models of the given data in the function case:
	* the "good model": The distribution is given by the simple model with a $p=2^{-10}$ probability of flipping the answer on top (independently on each input). This gets complexity loss like $100$ plus something small for specifying the flip model, and its expected neg log likelihood is $-p\log_2 p - (1-p)\log_2 (1-p)\approx p\log_2(1/p) \approx 1/100$. 
	* the "model that learns the errors": This should generically take $100+10000=10100$ bits to specify, and it gets $0$ expected neg log likelihood.
	* the "50/50 random distribution" model: This takes $\approx 0$ bits to specify and has $1$ bit of expected neg log likelihood.
	* some "universal hypothesis model": I'm not actually sure what this would even be in the function setting? If you handled the likelihood part by giving a global string of random bits which gets conditioned on other input-output pairs, then I agree we could write something bad just like in the sequence prediction case. But if each input gets its own private randomness, then I don't see how to write down a universal hypothesis that gets good loss here.
* So at least given these models, it looks like the "good model" could be a vertex of the convex hull of the set of attainable (hypothesis complexity, expected neg log likelihood) tuples? If it's on the convex hull, it's picked out by some loss of the form described (even in the limit of many data points, though we will need to increase the hypothesis term coefficient compared to the sum of log likelihoods term as the data set size increases).

that said:
* Maybe I'm just failing to construct the right "universal hypothesis" for this example?
* It seems plausible that some other pathology is present that prevents this nice behavior.
	* I haven't spent that much time trying to come up with other pathological constructions or searching for a proof that sth like the good model is optimal for some hyperparameter setting.
* I can see some other examples where this functional setup still doesn't work nicely. I might write more about that in a later comment.



