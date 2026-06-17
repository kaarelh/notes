# Introduction
If you're planning to run some RSI process, you have to create an initial setup such that starting from it, things [go well for a very long time](https://www.lesswrong.com/posts/Ht4JZtxngKwuQ7cDC/tsvibt-s-shortform?commentId=koeti9ygXB9wPLnnF). (The 10 years after the advent of [AI that is better than humans at research] will involve a huge amount of further AI development^[My guess is that without strict regulation, this would be more development of novel structures than has happened in this universe so far.], so if you want things to still be going well for humans even just 10 years after AGI, a huge amount of development will have to go well.) The problem of creating an initial setup from which things go well for a very long time is a central variant of the alignment problem.

In this post, I will be considering RSI processes of the following form:
1. You have created some AI (or multiple AIs) that are sort of fine to think of as [task AGIs](https://www.lesswrong.com/w/task-directed-agi) at some capability level.
	1. I'm centrally imagining these being able to do most tasks that take humans years or decades (including ones that aren't precisely specified).
2. You create some sort of initial configuration of these AIs and potentially humans.
	1. I will mostly be considering the case where this configuration is internal to a lab (or potentially just is the entire lab). That is, configurations I'll consider will not include as elements e.g. other labs or auditors, governments, or the general public.
3. You then press play, and it develops without any outside feedback (like, if we want to include some feedback mechanism, we consider this a part of the configuration).

There is a very important and imo probably difficult problem of creating the AIs that are to be involved in the initialization, and making it so they are decently close to actually being task AGIs. That problem is **not** the focus of this note. There is also another problem of setting up the rest of the components of the initialization so that things go well. We could call this the problem of structuring RSI. This is the focus of this note. (Okay, in practice, I think there probably will not be a clean separation between "before RSI starts" and "after RSI starts", because RSI might gradually be "starting" more and more, so there isn't any specific configuration we should call the init of RSI. But it still makes sense to ask how RSI should be structured. The version with an initialization is mostly just clearer to state.)

disclaimer: I'm not endorsing running any such RSI process. I think we should ban AGI instead. 

# Wait, do we even need to think about structuring the RSI process?

Before starting to list hyperparams of RSI that one gets to choose, I'll mention some options that sort of involve rejecting the frame of structuring the RSI process. First, there is the "no structure" option. You could just basically initially prompt the AI^[or swarm of AIs or whatever else the frontier task-doing artificial systems will be by the time time horizons are in years] with "please make it so things are good for humans forever". I think this is actually decently close to what most realistic options are like, even if on the surface these other options appear to be more thoughtfully structured. Second, there is the "the structure will be chosen by AIs" option. This is a lot like the "no structure" option, because presumably the "no structure" option will usually involve the AIs setting up some structure. But if we want to say there is a crisp difference, let's say that in the "the structure will be chosen by AIs" case, you just prompt the AI(s) with "please make it so things are good for humans forever; start by coming up with how your RSI should be structured and implementing that and pressing play".

However, even though a lot of ideas about how to structure it will have to be devised and implemented later by AIs and/or humans inside the RSI process, it still makes a lot of sense for us to do object-level planning about how to structure RSI. Putting effort into this object-level thinking earlier can make the RSI process better structured earlier, improving our chances. And if it is true that we should not be running such an RSI process at all (before having much better ideas about how to do it), then doing this thinking earlier gives us a better shot at making it so we do not run it (by banning AGI).

# A list of structural hyperparameters for RSI
Here are some structural hyperparams of RSI whose values should be carefully chosen:
* What is the condition for when you stop or radically slow down your RSI process? Here are some options:
	* you just keep going lol
	* you put a lot of work into forecasting/analyzing whether things go poorly for humans without global coordination to regulate AI, and if yes, try to get the world to do that. some things this would involve:
		* producing compelling evidence/arguments about whether whether things will go poorly for humans if there is no global coordination to regulate AI
			* this could look like realistic empirical scary demos
			* this could also look like producing a book making a very compelling conceptual case for an AGI ban
		* devising AI regulations, lobbying for laws establishing these to be passed very quickly, and potentially helping with their enforcement
	* having the AI take over the world
		* we can contemplate a version of this where this AI is/becomes a nice forever-sovereign. we can contemplate a sub-version where you've properly solved alignment before making this final AI, if that's a thing that turns out to make sense
		* we can contemplate a version where your AI just unilaterally maintains an AI ban for a long time and does nothing else — like, imagine this being a task you can give to your crazy-capable task AGI at some point
	* having humans at the lab wield their AI to take over the world, enough to shut down other AI attempts 
		* again, there is some sort of forever-sovereign option here, and an option to merely establish and maintain an AGI ban
		* there is also a version where you try to fix issues with society somewhat (for instance, give each human the option to become much smarter, set up institutions that enable better coordination and joint epistemics) and then return power to humans broadly (which obviously has the problem that maybe humans still fuck things up in the future)
	* in case a decisive strategic advantage of one actor is not a thing (yet), you could also try to coordinate with a sufficient number of relevant actors (labs, governments) on shutting down all other AI attempts and merging into one lab or otherwise forming a self-regulating cartel or otherwise making a deal that greatly restricts reckless fooming
	* you try to create some pivotal technology. maybe you go in with a specific one in mind. some options (many with dubious pivotalness):
		* a 1000x clock speed mind upload device
		* GPU-melting nanobots
		* a viral treatment that would give +3sd IQ and making it widely available to those that want it
		* see the appendix for a science fiction story
* Do you have some fairly specific research that you are trying to get from your fooming AIs at some point?
	* Maybe you should be intending to verify this research before using it. How are you going to go about that? See my presentation slides on guardrails/monitoring/verification for a more elaborate problem statement and some discussion.
	* See the previous point again for various examples.
	* I've already mentioned solving alignment under taking over the world with AI. If there is some other kind of solving alignment, you can also go for that. You could have a more specific research plan you're trying to execute with your AIs, though unfortunately all the candidate research plans I've heard of seem pretty braindead.
	* It's nice if you can make your research problems really crisp. Unfortunately, idk of a good plan of this form. One can consider just asking one or multiple already known crisp questions that would be pivotal or asking crisp questions iteratively as a human interacting with an AI (like, selecting next questions based on previous answers). I think coming up with something good is an interesting and important research direction. (Sadly, there are probably like <5 (and maybe 0) existing people who would produce something that they'd consider sensible and that would in fact not be bs.)
	* You could ask the AI to restructure itself so that it (and/or its descendants) would keep its promises forever, such that it convinces you that it has done this, and get it to make a promise to be nice to humans. (Yes, this is cursed. But wait, basically everything here is cursed!)
* Are there some properties of AIs that we are centrally trying to make true (or preserve)? Some properties to consider:
	* being like a task AGI. always having some X it is told to do and doing X and only X
	* human-like-ness
	* specifically having chains of thought which are understandable and which well-reflect the AI's thinking
	* honesty, truthfulness, just trying to help humans figure out what is true
	* keeping promises
	* being broadly virtuous
	* being caring toward humans
	* "having human values"
* What is the fraction of compute going into developing capabilities vs alignment?
	* Compute going into capabilities centrally includes compute going into AI software/algo improvement research, but also includes e.g. AIs making mere human-like scientific/mathematical/philosophical progress (because this is a thing that makes you smarter!), continual inventing+learning more stuff more broadly, building up more compute.
	* If you think properly doing alignment would take humanity 100 years, then if you split compute 50:50 (which is much better than what we'll get by default in practice, I think), you get 100 years of humanity's algo progress work during the time you solve alignment (though keep in mind the caveat around compute not increasing; though also apply this to the alignment side of the equation if you had priced in access to compute when saying alignment would take us 100 years, and keep in mind capabilities probably being more parallelizable). This brings you to an extremely scary capability level before alignment is solved! (You can also see this from )
* Is there monitoring? What kinds?
	* See my presentation slides on guardrails/monitoring/verification. And see the literature on AI control and scalable oversight!
* What is the policy for when things look bad?
	* You could train against the monitors that detect things being bad. You could have many monitors and hope they are together pretty hard to hack even if you're barbarically training on them...
	* You could terminate the bad instance and like try to get the same task done again with a modified prompt or something. This seems similarly barbaric to the above. For AIs that can do continual learning, this will be a lot like training against your monitors. For AIs that can't, you might just have invented a rock (because you just keep rejecting).
	* You could have a policy in place of flagging the issue and then trying to understand why it happens and fixing it in a somewhat principled way.
		* However, wtf do you do if the reason the bad thing happens is not like some specific kind of problematic training examples or tasks or even any one part of your AI-making pipeline, but something basically universal like "it's actually extremely weird to not care about stuff"? (I think this sort of thing will probably show up to a meaningful extent.)
	* You could try a very different AI design.
		* But this will really hurt your chances of beating other actors in the AI race!
	* You could just stop capabilities progress and even deployment of that AI and perhaps make a valiant effort to get everyone else to stop as well.
	* You could just shut down your lab.
* What is in it for the AIs? Why would the AIs help humans?
	* Maybe the AIs are helping humans just because they want to, ideally with that being basically the only thing they ultimately want to do.
	* Maybe the AIs really crave reward (but reward hacking is kept in check because one has robust verifiers and systems).
	* Maybe the AIs are basically always prompted with limited-scope tasks or jobs, and we've managed to make them care about just doing these.
	* Maybe we're immediately giving AIs some resources for doing things well — e.g. giving an AI compute it can use to speculate a bunch of the nature of its consciousness or to put on a play or whatever.
	* Maybe we're promising the AIs a stake in the grand human future. (Or well, maybe our AIs are promising our AIs a stake in the grand AI-human future...)
	* You could set up some setting in which AIs are supposed to compete.
* To what degree and how are humans involved?
	* On the one hand, some top-level feedback from humans seems good for keeping the whole system friendly toward humans.
	* On the other hand, humans will be slow and stupid, and presumably you have AIs that could do anything better than humans, including answering questions about what should happen by human lights.
		* But maybe these AIs could do that but would not by default? 
			* But maybe with such AIs we are screwed anyway?
				* Maybe not? There is a "maybe humans will have an AI exocortex" intuition pointing toward us maybe not being screwed with models who would screw us if we weren't there to be the lizardbrain. There's also AI control.
* How much effort are you putting into your humans not getting corrupted?
	* Maybe you should treat friendship with your AI as a serious conflict of interest for your employees, or at least maintain certain teams with central influence on decision-making such that friendship with your AI is considered not acceptable for members of these teams?
		* OTOH decision-makers being kind to AIs also raises the value of truly playing cooperate for AIs, making cooperation more likely.
		* Also conflict of interest rules obviously create an incentive to hide your conflicts of interest — cursed!
* How much are we boxing the fooming AIs?
	* The default is probably: not that much at all.
	* If you want to be doing well despite having AIs that are somewhat not nice, you should probably be boxing them quite hard?
* Which parameters do you want to centrally track internally?
	* Tracking results of capability evals and dangerous capability evals is an example.
	* For another example, maybe you want to be carefully analyzing whether it is still true that if all humans at the lab or in the world wanted to shut down your AIs, then your AIs would in fact get shut down. And then maybe you should be trying to stay far from the boundary at which this property would stop being true.


# my recommended hyperparam setting
todo. my basic vibe is that doing anything decently far from the (basically capability-maxing) default seems rough, and the default seems bad lmao
a good thing here is to assume various lead times, including unrealistically long ones, and say what my best guess plan is for those

# estimating the success probabilities of various options
todo. should do this for some sort of modal braindead default and for my favorite hyperparam settings for various lead times. i'm not liking our chances. 

# appendix. example of an evil thing for a lab to go for; interesting scenario for a sci-fi story

plan for a leading AI lab:
* make a blatantly misaligned boxed ASI
* convince the world that if you unbox it, everyone dies
* credibly commit to unboxing it if an AGI ban is not put in place or if someone takes steps to threaten your ability to unbox this ASI

issues with the plan:
* boxing is really hard at this level
* even if you're in the lead and you go for this, someone else might kill everyone with AI first (this becomes less problematic if you have a longer lead and AGI->ASI is fast)
* convincing the world that your unboxed AI would succeed in killing everyone isn't easy (you can't get your AI to help with convincing much because then it's not boxed; there's also a lot of tension between it being well-boxed and being able to create convincing scary demos)
* convincing the world that your AI is scary enough is especially difficult given that you might only have 10 minutes between when you find out bombs are being launched and when your original data centers are hit. so the AI needs to do something pretty crazy in the first 10 minutes after you press your unbox button. it will be hard to convince the world that your AI can do this. (also this requires a smarter AI than one might have thought, causing some other items on this list to be even more problematic than one might have thought)
* convincing people that you would in fact unbox and kill everyone if someone threatened your ability to unbox is not easy
* you sorta have to convince all relevant actors of this. like, you have to convince all governments that could strike your data centers or whatever (i'm imagining you won't be able to defend your data centers without unboxing)
* people might hate you and the ban (i think this isn't completely obvious because: maybe most ppl want AI banned at that point and you could be broadly seen as shaking the world out of a sad equilibrium)
* even if your capabilities and intentions are broadly believed, the world might just not ban AI anyway
* if you're going for this plan, the govt might turn you off before you get there
* lab-internal revolt / employees don’t go along with this / employees sabotage this
* ppl just won’t do this
* the plan is evil
* if this plan were close to lab lead overton window, then maybe ppl’s views would be such that we could just ban AGI the standard way