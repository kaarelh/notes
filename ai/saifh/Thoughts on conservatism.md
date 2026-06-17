
## Finding a good version of conservatism

At the end of the day, we (looking at an AI system from the outside) want to not have the AI system take actions which are too likely to lead to harm.[^1] Let $P'(H|a)$ denote our probability that the action $a$ being take would lead to harm.

* Looking at things from the outside, our decision rule should be to only let an action through if $P'(H|a)<\delta$, for some fixed $\delta$. But how do we come up with a reasonable $P'(H|a)$?
* Well, we're assuming we have a conditional probability estimator which can tell us $P(H|a)$ for any action $a$. Why not just do the obvious thing of checking whether $P(H|a)<\delta$ to decide whether to let the action $a$ through the filter?
* I take it that the reason is that we don't trust the conditional probability estimator enough — we think we can maybe do better than just taking $P'(H|a)=P(H|a)$ and checking that $P'(H|a)<\delta$. How might we do better? To me, the most promising things to try here are:
	* Think through the conditional probability estimator training process and look for possible modifications to get whatever happens when you ask for $P(H|a)$ to correspond to what we'd actually want to happen to compute the probability of harm given an action.
	* Keep the conditional probability estimator, but 'pour more compute into coherence conditions relating to $P(H|a)$'. For example, maybe put more compute into estimating $\sum_S P(H|a,S)p(S)$.
	* Think about ways to detect when $P(H|a)$ might be very off (for example, maybe when it looks like it has high variance under 'thinking more' (i.e., pouring more compute into surrounding coherence constraints)), and also reject in these cases.
* 


Here's what I expect to be a counterargument:
* Ok, but we want to act conservatively. In particular, we want to have the property that we don't need the system to pin down the right theory
* But, unless the system is basically perfect anyway, this is just impossible to satisfy without paralysis.
* And if the system is basically perfect anyway, then it's probably good enough to work with the vanilla decision rule.


Maybe you're still not convinced. Let me finish the argument against  noting this:
* Any of the above making sense at all depends on the conditional probability estimator doing something pretty close to reasonable. In any case, almost all of the bits to pin down the right notion of harm must be inside the conditional probability estimator.
* It seems to me very unlikely that we would get almost all of the bits 




Still, maybe I should also say more about why I'm suspicious 

## mess

* This part cannot do any heavy lifting.
	* I guess this means that if you guys think that this part needs to do some heavy lifting, then conditional on you being right, I'm ~certain that the plan doesn't work

[^1]: I don't think this is really it, as I think it's better to think in terms of expected utilities instead, but I'll grant that we want to minimize the probability of harm for this discussion.
