
this is a TOY setting for studying some technological phenomena, but also for studying some phenomena in the development of thought/doing — well, really just in development simpliciter. i guess the point is to understand tech development by understanding this toy setup. 


the idea of the toy setting: a technology is like a program, and a problem for a program to solve could be specified by a program as well — one that verifies solving the problem. (a program here could be a turing machine or it could also be a boolean circuit.) more precisely:
* at each time $t$, there is some collection $T_t$ of programs — think of these as the technologies one has at time $t$
	* fixing the type signature: let's suppose that a program takes an input string and gives an output string?
		* for example, it might sort a list
* there is also a collection of programs $V_t$, which we think of as specifying problems one has identified as important by time $t$ — like, specifying them with solution verifiers
	* fixing the type signature: let's imagine that a verifier takes in an [input or context string] $x$ and a proposed output string $y$, and accepts or rejects (corresponding intuitively to whether the output string $y$ is a legitimate output to give on $x$)
		* for example, $x$ might be an unsorted list, $y$ might be taken as specifying a permutation, and the verifier would check whether the permutation validly sorts the list
	* one might be able to solve some of these already, but be interested in solving them better — like, with "less expensive" programs (concretely, maybe with ones that run faster, or with ones that are shorter); others, one can't solve yet
* $V_0$ appears somehow. maybe it's just some sort of random small collection of small verifiers?
* the rule for adding technologies to $P_{t+1}$ is sth like: you add a technology if it helps you solve a problem
* the rule for adding problems to $V_{t+1}$ is sth like: you add a problem if solving it would be helpful for solving some existing problems
	* concretely, maybe you realize that you could make a technology solving some problem, if only you had a a technology solving some other problem. in that case, this other problem gets put in the set of important problems
	* i think we should also allow cases where a path to solving a problem which involves solving multiple unsolved problems is identified — this is weaker than requiring that there be a reduction of an interesting problem to another problem. like, when such a reduction is identified (with the problems being plausibly solvable), that gives reason to be interested in the problems in the reduction
	* philosophically: new problems are considered useful here when relevant to solving old problems. given that we aren't keeping their importance tied to the old problem, i guess we are positing there is a kind of [subgoal stomp](https://www.lesswrong.com/w/subgoal-stomp) here
	* this doesn't mean that new problems have to be found by back-chaining from an existing problem. they could be identified in some way that is more like asking "hmm what potentially cool stuff can i do" and then finding uses (which is kinda like finding reasons for the potentially-cool ideas actually being cool)


# some points made by this setup


# some questions that could maybe be made better sense of using this toy setting (or some variant)
* is technological maturity a thing? is there always more to be invented/discovered than has been invented/discovered already?
* to what extent is there convergence in tech?
	* if you want to solve a problem starting from a given technological state, how would we characterize the amount of freedom there is to solve it in different ways (which are fairly reasonable)?
	* even if a problem initially gets solved in one way, does there eventually end up being basically a single best way to solve it in all rollouts of tech development? or maybe: can we say something about the set of problems for which this is true? we can split this into two questions:
		* given a problem, should we expect to eventually have the best technology which addresses it compute some universal function that satisfies the verifier
		* given a function which is to be computed, should we expect to eventually be computing it with the same program (or with the same assembly of ideas less precisely)
	* even if it were true that each individual problem eventually gets solved the same way, this doesn't mean that tech trees created by two rollouts of this process eventually look the same (imagine two trees growing from the origin out into some sort of infinite-dimensional discrete lattice. they might both eventually cover every point, but at each time, they are extremely disjoint from each other)
		* take two tech development rollouts "of similar size". consider sth like the "size" of their "intersection" over their size. increasing size/time, does this tend to close to $0$ (this would mean the two technological worlds are diverging) or close to $1$ (this would mean that the two technological worlds are converging)? what sort of function of size/time is it? if there is divergence from the origin, is there a size after which there is convergence for a long time? if not, can one invent some particular odd configurations from which there is a surprising convergence from a long time? also, if there is divergence when starting from a generic state of some size, then what is the characteristic time of divergence?
	* to the extent that convergence does happen in various senses, can we understand what the characteristic times are like (eg as some function of the complexity of the problem or a solver of the problem or ways to find a solver)
* can we tell some story about the "values" of this technological world and their development? in this model, is there a time after which the values don't change much, or do they keep meaningfully changing forever?
* in this model, can we see that technologies end up being made of parts? in some a priori surprising way that doesn't feel obviously forced by the model setup? if yes, maybe understanding we can understand why this happens, and so better understand why technologies are made of parts in reality?

# remarks

* we might want to also model phenomena and maybe their discovery. i'm not sure how to integrate that well atm, but a starting point would be to include facts of the form "this program always gives an output with this property" as a thing that can be gained. but hmm this is pretty much the same thing as a solved problem, right! like, a problem asks for a program satisfying some property, so a phenomenon in that sense is just a statement that a problem is solved by some program (technology). but maybe this connection motivates some different ideas for how new problems should be identified? like, we do just have a sense that a phenomenon is pretty cool? hmm but plausibly this sense is basically derived from our sense of what problems would be useful to solve — a phenomenon is cool iff it lets one solve problems?
	* the setup then kinda makes clear that: new phenomena don't have to be somehow given in physics. they can be facts about the "computational/mathematical universe". this defeats an argument for technological maturity that tries to go through the claim that there are only finitely many phenomena to exploit because there are only finitely many "phenomena in physics" (i'm not claiming to know what this claim would even mean — i'm just saying that basically whatever reasonable thing it would mean, this probably gives a way to defeat most naive arguments using it)
* does this thing stay tied to the original purposes in some sense? like, you could think that at the end of the day, it's all still about $V_0$. i don't see a good argument for that — i feel like you can just have the set of purposes grow wildly
	* that said, i think it's plausible this setup wouldn't "go to infinity" interestingly, wouldn't grow arbitrarily rich. there could be some silly reason why it degenerates. i'd like to understand better whether it does
* new technologies sometimes let you do something you can already kinda do but better.
	* this is captured by the above in part: we are interested in faster/smaller solvers of a problem.
	* but there are other things of this kind that are not captured, eg wanting to solve the same problem more robustly, ie let's say in more circumstances, ie on more classes of inputs. there's also just solving a problem with fewer errors
	* it'd be nice to model this better. i guess we could have each (tech,problem) pair with the class of inputs on which the tech solves the problem. we could also allow imperfect "solvers" so we can speak about the error rate?
* i'd want to think more carefully about where new problems come from, and try to capture that. it might be good to think more about where open problems come from in math:
	* we get new interesting conjectures by identifying sentences which would (in a nice/simple way) imply many sentences of interest (these sentences of interest could themselves be proven theorems or previously identified interesting conjectures)
		* generalizing an existing thing to a broader context is one example
		* in tech, this perhaps corresponds to identifying a problem which if solved would let one solve many other problems easily
	* maybe we sometimes just vary existing statements. we are interested in whether something like a known plausible statement is also true in another context
	* sometimes we just play with something and ask some simple questions. eg collatz maybe? related (but also related to other items i think): a question can just be so natural
	* sometimes we have a sense that working on a particular question makes us work on interesting things; we have a sense that if we could solve the problem, we'd be much better at some important stuff, and we simultaneously have a sense that we might be able to make progress on it. questions can get their value from us thinking that they are good to work on for furthering our understanding (and like here i'm focusing on the aspect of this that doesn't really route through knowing "the answer" to the problem being good for our understanding — i'm pointing at how we can have a sense that the understanding gained when working toward an answer could be really useful)
* i should also give a version with math — with theorems and proofs and mathematical objects and their properties and maybe other stuff
	* also: methods/skills
	* also: concepts?
* arthur and polak do a version of what i'm trying to do in https://inctpped.ie.ufrj.br/spiderweb/pdf_2/Dosi_5_Brian_Polak.pdf . two ways in which it is worse: i think they have a god-given list of purposes that isn't getting updated, and also they don't model purposes and things one can carry out as distinct
	* Different phenotypic versions of the new circuit are created by selecting different
internal wires in different orders as output pins. At each time there is a set of existing technologies that best
match each of the needs or goals (have least incorrect entries in their truth tables). Each candidate circuit is
tested against these to see if it improves upon them. It may do so by better matching a need’s truth table; or,
if it has a function identical to that of an existing circuit, by costing less. (The cost of a circuit is determined
by the number of its components and by their respective cost.) In either case it replaces the circuit it has
improved upon both directly and in all circuits where that circuit is used as a component. It is also
encapsulated: it becomes a new component that can serve as a building block for possible further
combination. In this way the set of encapsulated technologies builds out. A need is satisfied if a new
technology with its exact truth-table has been found. And a newly created circuit of course cannot replace
one of its own components


# some directions

* should i just try to implement some version of this and stare at what happens?
	* eg maybe for math? could we get to cantor's theorem using these ideas? it might be interesting to just manually sketch a path to cantor's theorem from nothing to see how complicated it is
* oh in general i should maybe try to sketch some full-ish paths to cool things? in math or tech