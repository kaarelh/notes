questions:
* suppose you enter all existing human scientific papers in sequence into a solomonoff inductor, and then "title: A detailed description of how to cure alzheimer's. date: Feb 2025"[^1], and then either look at a few samples of the next $10^6$ bits or just look at what the highest-mass hypothesis says (this is assuming hypotheses are deterministic)[^2]. what do they look like? in particular, do they look like things which if read would let you cure cancer 
* the same thing, but with a different type signature: you now have a function from titles and dates to paper texts from a simplicity prior, conditioned on all existing papers as input-output pairs 

# arguments against getting science out of a predictive model

so we have a property — the text being an actually good paper — and we're interested if a predictive model produces text with this property

* one counterargument to this happening is that there are other properties which, if preserved, contradict this property; one such property is that the papers are written by ppl from before 2025
	* note that the main argument in favor of getting good science is via property preservation i think. like so far we had pretty good answers to scientific questions. if that doesn't continue, then we have a property which was true so far but isn't true after
		* however, solomonoff induction just isn't property-preserving in general. (despite being an ideal thing, it's not a magical thing that does whatever you like)
	* this is a defeater to this property preservation argument, of the same property preservation shape
* generally your data set is nowhere near physically or conceptually to an alzheimer's cure. eg, if there's pointing into a universe with this data set on a hard drive, then an alzheimer's cure is nowhere near

# what could happen that is not like getting a proof of the RH

* some sort of universe simulating thing that finds some nonsense after the RH statement, like blank spaces or something
* just like 000000 or some such low complexity string. i think we can give a fairly compelling argument that this has at least some const probability which is independent of the amount of data given. like you can have an if out-of-distribution then 000000 sentence, maybe of const length?
* just any thing which satisfies a counter-property
* some malign hack




# an attempt at a concrete calculation

Let's $S$ be the set of all strings of length at most $N$, with $N$ large enough that a $1000$-page textbook would be/give such a string[^3]. Let's say we have a data set $E$ of examples, with each example being a question asked in $1900$ understanding together with a textbook answering that question. Let $G$ be the set of all good question+answer pairs. Let's say the point is to learn $G$[^4]. To hopefully make things easier, let us assume that $E$ is a random subset of $G$.

Well, a part of this is just canonically solved as follows: we say we have a prior on which property $G$ we might be shown samples of, and then we update on the samples we see being $E$. This sets our probability that $G=g$ to $0$ for any $g$ such that $E$ has an element outside $g$. For any $g\supseteq E$, the probability is proportional to the prior times a factor which depends on $|g|$, with larger candidates $g$ losing more probability. I think this is a tad nicer if we make $E$ be a sequence of strings sampled independently at random from $G$. The likelihood which the actual $G$ gets is then $|G|^{-|E|}$, whereas the likelihood of any other $G'$ containing all of $E$ is $|G'|^{-|E|}$. At what point do we expect the correct $G$ to have the highest posterior probability?

[^1]: or some other date, if you think that's more likely to give you a cure of cancer
[^2]: i think greedily taking the most probable bit one by one is probably worse?
[^3]: I think we could also do this with infinite strings, but the finite case seems a bit easier to think about first
[^4]: [keeping in mind but setting aside locally] that really the point is to generate/complete some particular strings in $G\setminus E$
