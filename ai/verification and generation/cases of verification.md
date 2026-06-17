
# cases which are understood fairly well
* you’re interested in whether a mathematical statement is true or false
	* for example, you could be interested in knowing whether the collatz conjecture is true or false
	* someone could give you a proof or disproof, which you could verify (yes yes, the statement could also be independent)
* you're interested in getting a solution to a mathematical problem
	* for example, you could want:
		* a satisfying assignment to a SAT formula
		* a hamilton cycle in a graph
		* the smallest natural number with some property
		* a nearly optimal solution to a linear programming problem
	* roughly in general, maybe: you're asking for $x$ such that $\phi(x)$, for some $\phi$ you have
		* in this case, someone could hand me some $x$ and a supposed proof of $\phi(x)$, and i could verify that it is indeed a proof of $\phi(x)$
	* also roughly in general, maybe: you have a turing machine $M$ and you're asking for an input such that $M$ accepts
* you're interested in whether an algorithm does something and maybe in whether it has a certain time complexity and a certain space complexity
	* here, you can provide a proof that it really does the thing you want it to do. for instance, if we have a supposed list sorting algorithm in front of us, then we'd ask for a proof that when the algorithm gets a list as an input, it gives a sorted version of this list as its output
		* this proof could look a lot like how a human would explain why the algorithm does what it is supposed to do. for example, for mergesort, the key step might be to prove that merging two sorted sublists gives a bigger sorted sublist
	* you can also provide proofs that it really has a certain time complexity and/or space complexity
* more broadly: you're interested in whether a data structure supports certain operations with certain complexities
	* you can prove that the operations are doing what they are supposed to be doing (eg, for a list, that supposed insertion and deletion operations actually work like they are supposed to)
	* you can also prove that they have some desired time complexities and/or space complexities
* well, these are actually all just types of solutions to mathematical problems! but they are important subtypes


are there any well-understood cases of verification which are not of the form "give me an $x$ such that $M(x)$ (for a turing machine $M$ that I have)"? maybe let's just list some cases of verification from the wild, and decide if what's happening is well-understood later
* you can check that a device is doing what it is supposed to be doing by like just trying it.
	* for example, you can try working at a "desk" — you can see if the things you would expect to be able to do at a desk can in fact be done at this "desk"
	* you can check if a supposed windmill indeed generates power when it is windy
* you can talk to another person and figure out if they understand something or not, at least assuming you understand the thing already
* if you don't understand something, you can ask someone to explain it to you
	* if they manage to do that, then they probably understand it?
	* if they don't manage to make the thing understandable to you, then for some things, you might conclude that they don't understand it? for some things, maybe you wouldn't, if you recognize that the thing was really far from what you understand? but even in that case, you might be able to tell if the person has been sensibly moving you in the right direction
	* you can also maybe just generally tell if they are making sense or spewing nonsense. you might be able to tell if their thinking is clear
* you can test a bridge design with specialized software for doing that
	* presumably there are bugs in the software. a human engineer that is actually trying to make a good bridge meeting some specification will probably not be proposing a bridge design such that the bridge only seems to not collapse due to some software bug. an AI that doesn't care would totally be exploiting bugs once it finds them (and if it's good enough at finding designs meeting sophisticated specifications, it'll also be good at finding bugs)
* you can test some code/software by seeing it gives the desired outputs on some inputs ( https://en.wikipedia.org/wiki/Unit_testing )
* https://en.wikipedia.org/wiki/Stress_testing



# some cases which are not understood well presently

* verifying physics olympiad (theory) problem solutions
	* mostly, these are arguments that a certain variable has a certain value
	* this is like giving an $x$ such that $\phi(x)$, with the trick that $\phi$ is not formal?
		* for example, $\phi(x)$ might be "in such and such a setup, the velocity of this object is $x$"
		* in many cases, $x$ is a real number. it is sometimes a diagram or a plot. i guess one is also occasionally asked for a verbal description of something, and occasionally asked for an explanation of something? there might also be other things
		* and also we're dealing with a special case in at least the following way: almost always one is allowed to assume that there is some $x$ such that $\phi(x)$
			* i guess maybe a solution is actually more like a proof that $\phi(x)$ implies $x=\text{something}$, for a particular $\text{something}$?
			* maybe it's best to think of most problems as asking one to determine the value of some variable? but then the above might be a fine way to make that precise?
* more generally, arguing that $P$, for some imprecise $P$
* arguing that $P$, for some precise $P$ but in some setting where it is appropriate to think probabilistically
	* logical induction assigns probabilities to mathematical statements in a nice way! but it doesn't really involve any kind of verification i guess?
* verifying responses to philosophical questions. eg to the question "can computers in this universe only do turing-computable things?", or to "is moral anti-realism right?", or to "how should we conceive of existence?"
* verifying technologies. eg is this really a mind upload device
	* verifying things. eg "is this really a mind upload of me that runs at 100x speed?"
* verifying plans for doing things. eg a plan for implementing an AGI ban