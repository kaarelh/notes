
# A remark on incompleteness (or really maybe on recent incompleteness discourse) 

I will start with some metaremarks:
1) I think the case for AI alignment being hard has very little to do with explicit vNM theorems, and that understanding explicit vNM-style theorems has little to do with understanding the alignment problem, etc. In other words, I think the claim that these are somehow critical in the canonical LW-style argument for alignment being difficult is false. That said, it is plausible to me that there is a thing that is in some messy sense a "[projection of these kinds of theorems into the real world](https://www.lesswrong.com/posts/eD34hTMp8uv3ifSjg/consequentialists-one-way-pattern-traps)" which does matter, but it is not clear to me that this is significantly more profound than "actually trying to get things done tends to help get things done done" or "problems will arise when you try to do things and you need to solve said problems to do things" or "you get more done if you don't keep stepping on your foot", which, however, is plausibly more profound than it may at first seem.
2) I wrote this post quickly (total writing time n hours) and I admit to it being a complete crapshoot — treat it as a discord message or something.


And now a few remarks that are somewhere between the meta and object:
1) See [here](https://www.lesswrong.com/posts/yCuzmCsE86BTu9PfA/there-are-no-coherence-theorems) [for](https://www.lesswrong.com/posts/3xF66BNSC5caZuKyC/why-subagents) [the](https://www.lesswrong.com/posts/bzmLC3J8PsknwRZbr/why-not-subagents) [discursive](https://www.lesswrong.com/posts/sHGxvJrBag7nhTQvb) [context](https://www.lesswrong.com/posts/tiftX2exZbrc3pNJt/crystal-healing-or-the-origins-of-expected-utility).
2) My own position is roughly that the formal question is sort of unessential, or maybe that it might turn out to be good if there turns out to be some formalization that better captures the plausibly real and important real-life coherence-y consequentialism-y laser-that-starts-to-laze-y property.
3) My position is also that completeness basically makes sense and that incompleteness basically does not. (And likewise for the other vNM axioms.) I think most of the cases that for some give incompleteness its appeal (eg cases that feel intuitively like they should be insensitive to sweetenings/sourings, or status quo bias) are better understood as a bounded approximation of completeness (in particular, subject to computational constraints). 

I will try to justify 2 and 3 somewhat in what follows.


### The basic argument 





Ultimately, behavior matters. How an agent feels obviously matters too — it matters roughly insofar as it affects its behavior. but ultimately it matters roughly insofar as it affects its behavior. It is not clear that anything from the incompleteness 

I think there's possibly something here, but this mostly looks to me like a good 
### The lack of a good formulation of the problem




### An adjacent reasonable problem

Ok, you have 

That said, there could be agents which do not come whole with fully-formed preferences, figuring out what to do on the fly instead. In fact, it seems plausible that any reasonable boundedly rational agent would have to be like this. And it seems reasonable to think about what kinds of reflection processes in such agents would lead to them being aligned! But I don't think the post contributes to that. (In fact, one probably wouldn't want such agents to never make mistakes in the sense of never reverting a previous preference — it seems fine and plausibly necessary for such agents to be exploitable in a weak sense.)


Sorry, I admit to not having read very carefully, but I believe each of the following with 90% confidence conditional on the previous claims (i.e., conditional on Claim $i$ turning out to be substantially false, I do not wish to communicate belief in any Claim $j$ with $j>i$ (though I may then want to communicate some similar Claim $j$' instead)):
Claim 1. The decision rule you propose is equivalent to "make sure your sequence of decisions is such that there is at least one completion of your preferences which permits it".

(I'm inclined to put "completion of your preferences" in quotes in the above, because I think agreeing that what you call one's preferences are indeed one's preferences and taking incompleteness to be defined via permissibility and to take this kind of permissibility to be rationally allowed already constitutes conceding a lot to the case for incompleteness being reasonable, but this is not a central claim I would like to argue for.)

Claim 2. It is very easy to prove the above decision rule is inexploitable in any setup.

(The argument I have in mind is the following: by definition, any sequence of decisions you make can be ex post interpreted as choosing optimally according to at least one set of vNM preferences; being exploitable would imply these preferences are also exploitable, a contradiction.)

Claim 3. It would confuse me profoundly if this post caused a nontrivial fraction of those who understand it to significantly update towards finding inconsistency more plausible. This is because:
1) It seems obvious that it is possible to be unexploitable by storing a *special character* in your preference database until you come across a choice situation which would, assuming completeness, determine the preference, and to then replace the special symbol with a preference that agrees with some completion.
2) To say this in another way: "act compatibly with being complete" is just very obviously an unexploitable strategy.
3) I would think that all but an epsilon fraction of those that find completeness compelling would have thought of an example like this —and  it seems plausible that instead of considering this a legitimate example of incompleteness, they'd think instead that it is unreasonable to call this kind of thing incompleteness, or at least that this is equivalent to completeness in any sense we ought to care about.
4) In particular, and as I'm aware you also say in your post, behaviorally and ex post, the agent just looks like a particular complete agent would. Behaviorally and ex ante, the probability distribution of the agent's behavior is a certain supported on behaviors of complete agents — and I don't see why this would be a different/better/more controllable probability distribution than that of an agent which is just complete to begin with (assuming it is even possible for an agent to be complete to begin with).
5) Said another way: it seems to me that a DSM-agent from complete ones (they do not differ, for instance, when put in multiple decision situations in a sequence in the actual world)

That said, there could be agents which do not come whole with fully-formed preferences, figuring out what to do on the fly instead. In fact, it seems plausible that any reasonable boundedly rational agent would have to be like this. And it seems reasonable to think about what kinds of reflection processes in such agents would lead to them being aligned! But I don't think the post contributes to that. (In fact, one probably wouldn't want such agents to never make mistakes in the sense of never reverting a previous preference — it seems fine and plausibly necessary for such agents to be exploitable in a weak sense.)


I'll finish two less central things that I found disagreeable in the post on some combination of the rhetorical and conceptual level. Firstly, that you say Wentworth-Lorell's claim is false, but then don't consider the obvious (I think?) Wentworth-Lorell counterargument to your post of "why not sign a contract before taking any actions which commits you to a particular completion of your beliefs?"



> To see what this implies, consider first the case of certainty. Here we proved that DSM will result in only ex-ante strongly maximal plans being implemented (Proposition 2; Corollary 1; Proposition 5). Now consider the following toy case (Example 1). A Suzumura consistent agent can’t compare A and B. It’s offered a choice between the two. Suppose it chooses B. Does this constrain the agent to never pick A in future choices between A and B?
> No. In fact, it’s a bit unclear what this would mean formally. Once we expand the decision tree to include future choices between A and B in some branches, everything boils down to the fact that all plans through this tree will result in either A or B. And so any plan will be permissible. What DSM constrains is which terminal nodes are reached; not how the agent gets there. Let’s see how far this reasoning can get us.

Here are two separate ways in I think this is confusing/wrong/nonsensical:
1. Being allowed to pick A in future choices between A and B would not even make the choice rule clash with completeness in the way that I take you to be implying it would by talking about this here — it could just be that A and B happen to be considered equally good. The obvious way to fix this issue, i.e. to make an analogous claim that would in fact make the choice rule clash with completeness, is to instead say "suppose the agent can't compare A,A^- and B; it's offered a choice between A and B; suppose it chooses B; does this constrain the agent never to pick A^- in future choices between A^- and B?". The answer to this question — which, as far as I can tell, is the nearest sensible one for this conceptual slot — is yes: under DSM, after you act in a way that would not be permitted by completions that take A to be strictly better than B, you indeed cannot then make a choice that would not be permitted by completions that take B to be strictly better than A^-. So it seems that the answer to the closest question that is not confused is just yes.
2. In any case, I think it is bad that while "no" is rhetorically good for the case you are making, I don't see any interpretation under which it is the correct answer to the question you are asking. If the question is nonsensical, then the answer isn't "no". For instance, here is one thing one could mean under which this (strictly speaking) evaluates to false: "suppose you are in the deterministic setting, and you go from a node which has both A and B as its descendants to one which only has B among its descendants; in this case, it is in fact false (albeit in a trivial sense) that if given such a choice again, one is "