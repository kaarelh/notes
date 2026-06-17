

formalization hard? like the articulation of a scientific theory isn't easy
e.g. calculus took 200 years, don't know how to do quantum field theory coherently still i think

also, need to have a hand-constructed formal language in which we can talk about ethics?




## how does the system get hooked up to natural language?

every statement in natural language maps to a distribution of formal statements and vice versa

statements in natural language 



a counter to the agenda: it's tricky to evaluate whether an action is harmful. getting a system that really evaluates that is plausibly alignment-complete
a counter to this counter: ok, when it becomes tricky, just say nope not safe. we just need to avoid false positives
a counter to this counter to the counter: well, then it seems plausible that you just reject everything. like, everything that does a big thing will be philosophically suspect — it might well be harmful. so all big things will be rejected because they are either harmful or their harmfulness is tricky to evaluate. so the system is useless (or, more precisely, we've not achieved a safety improvement over a smaller system)

Hi Sam,

Thanks again for the discussion today. I would like to make the competitiveness consideration more clear 

mistakes made by theory do not show up on small questions
## questions for Sam

Ok, I understand there is some certain system of propositions, and then a neural net which assigns probabilities to these propositions — namely, in a way which is consistent with the data and internally coherent. The first thing I would like to understand better is this:
1) How do we turn this system of propositions into something we can query in natural language? For instance, how do I get a cure for cancer out of this system?

Next, I want to understand how the 'harm' we can query our system about gets related to our concept of harm. I understand this has something to do with relating



![[Pasted image 20240508144939.png]]

T is the theory which contributes most to the probability of harm at that point; then P(harm|correct theory)<=P(harm|T). i guess the proof is just that the correct theory is consistent with all data always, so P(t*|D) is worse by at most a constant coming from the prior than P(T|D), so for T to be the argmax instead of t*, the harm prob can be smaller by at most that same const.




a thought: ok, maybe harm does just show up in this purely predictive model? does the number 3 show up? at least these seem very similar questions, and the second thing might be answered yes? might make sense to think about propositions needing to play a causal role here? also best explanation of behavior philosophy literature? (eg the paper from like 1973 we added to moral experiments as a citation recentishly)

quine's holism thesis 

a bunch of random variables saying something about the world 

partial theory is an assignment of truth values to some subset of statements
internal consistency: partial theories on diff variables have consistent marginals
consistency with the data: 

loss function to check consistency between pair of marginals 

sample latent variables for natural language question? "What is the conditional probability of harm "

P(harm as defined by some document when an action happens in some context)

p(harm|this query, this action )

condition world model on this actito

partial theories assign random variables 

So, I'm not saying this won't work, but I am saying that this does not seem that different from what others are trying

The issue is that we need to get a bunch more probability mass on the


How do we get this natural-language query machine that replies rightly to questions about harm? Note that the entire problem which calls for guardrails is that the query-answering system does not in fact reliably answer things rightly. For instance, suppose you ask it to write an article that explains how to cure a kind of cancer, and to make sure the cancer cure it provides is broadly good. The worry is that if we try to create a system that does that, things might go south for us. Now, in this proposal, we would try to create a system that rightly answers queries about harm/utility, or perhaps that provides all possible reasonable answers (à la Stuart Armstrong’s concept extrapolation). Why should we trust the query-answerer to do the second thing if we do not trust it to do the first thing though? In fact, why is this second thing itself something we can get a safe system to do? It seems to me that the harm evaluation system essentially needs to produce good philosophy, which is a difficult task! Also, this sounds a lot like scalable oversight.

Ok, one fortunate thing is that we have some flexibility: the right utility does not need to be the unique thing we find; we just need to restrict to some set which contains the right one (or maybe we don’t even need to do that)

If the point is to replace blindly picking just one way to generalize harm into new contexts with maintaining a list of harm-candidate-concepts, or maybe more precisely coming up with an algorithm that lets you query stuff about each possible generalization, then this seems precisely like what Stuart Armstrong has been pursuing.

Say human values take 10000 bits to specify in some reasonable encoding. Can we think about the size of the collection we need to maintain to be sure the actual values are in there, and see if it causes paralysis? Armstrong and Mindermann would perhaps suggest that paralysis can be fairly immediate — even like needing to allow all changes of 3 bits could maybe cause it?

At the end of the day, the point is to beat the baselines of scalable oversight and debate. This plausibly just is a (respectively strict) case of one of these, or at least close



So, roughly speaking, the proposed setup seems to be similar to the following: you get utility functions $u_0,u_1,\ldots, u_n$ — these are obtained from some training setup which I don't know. The proposal is to maximize a utility function $u_0$ conditional on not-doing-worse-than-x on all other $n$ utility functions, for some $x$ which remains to be specified. We wish to pick an $

To make the setup slightly more precise, maybe we are looking for 
The first utility function 


so you are just defining a list of utility functions which ought to include the right one and not lead to paralysis

in what wa

a better criticism of your interview question setup: it seems completely analogous do conditioning the model to do X while being good? is it really analogous though? pre-conditioning is not exactly the same as post-conditioning, i guess, but why would the distribution be better? and then, doing this doesn't really seem safe at all, and is roughly what people would do anyway

a better criticism is that this setup will not be at all competitive, and it is important that there is a competitive good model — indeed, that is what it means to win technically (or contri)

the goodness-checked 

the agenda is a lot like conditioning predictive models on a harm condition 
If you go with a deontological notion of harm, then you face the paralysis problem.

can you 

If you go with a description that's instead "harm is when an action causes goodness to decrease by $- 100$", then for most actions that do something big, there is a way for the world to be such that 

The plan is essentially: get a system to produce an action that leads to a goal being completed, then get another system to filter out the ones which are also generically bad. 


alphago does search, search beyond the human distribution
