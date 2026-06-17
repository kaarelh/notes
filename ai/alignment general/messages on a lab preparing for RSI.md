*friend sends takes on places where safety people at labs are dropping the ball*

a response from me:
* i'm unsure if they are seriously preparing for RSI as you claim, and if not that's a point i'd add to this list
* at least they have very little public writing on preparing for RSI?
* not making it public could be understandable, just saying it's hard for me to tell if they are thinking sufficiently and seriously about it
* from public statements it doesn't look like senior lab ppl have thought about RSI that seriously (except if they are lying)

friend again:
* what would preparing for RSI look like

me:
* eg just thinking a lot about various plans for getting to a less precarious AI situation is important, starting from a high-level menu of options and going into more detail
	* eg one could start by reading my presentation: https://docs.google.com/presentation/d/1T3PN3m6GcQymYsadvTSRoFUjksTZDCU5KrpYZpJfZTs/edit?usp=sharing
	* or wei dai's post: https://www.lesswrong.com/posts/bnY3L48TtDrKTzGRb/ai-safety-success-stories
	* i would weakly guess there aren't even like >10 people at anthropic who are familiar with this basic menu of options and have [thinking about what path here to take] as a large fraction of their job duties?
* one example of a more specific thing: fleshing out this scheme in a lot more detail
	* scheme: **Using verification in an RSI loop**
		* Maybe you’re OpenAI aspiring to make increasingly capable task AGIs.
		* You give your current task AGI the task of proposing self-modifications which would make it more capable and/or more task-AGI-like. 
		* Some examples of modifications: training in some new RL environments intended to train out some sort of misbehavior, new ideas for making sure its thinking doesn’t go off in some scary open-ended direction that isn’t tied to the task, all sorts of capability improvements.
		* Before each of these modifications is implemented, it has to go through some sort of verifier that is supposed to check that the resulting AI will be more capable than the previous version and still acceptably task-AGI like.
		* The verifier itself could also be getting improved (hopefully), with verifier modifications having to go through the verifier to be accepted.
		* In fact, the verifier could just be another copy of the same task AGI.
		* The point is to use this to climb to some very capable very task-AGI-like AI that can be then given some pivotal “task”, eg maintaining an AGI ban for 200 years. 
* another example of a more specific thing: working on this
	* open problem: **Designing a tech verification setup**. some hyperparameters you get to choose:
		* What (pivotal) tech/science are we trying to get from the AI?
		* In what format are we trying to get the tech? E.g., for mind uploads, you could ask for:
			* uploads of some particular humans;
			* or a device which can take a human and produce an upload of that human;
			* or a textbook which humans could read and use to fairly quickly create uploads.
		* How are we motivating the AI?
			* Are we promising to eventually pay it somehow? What are we promising?
				* How do we become trustworthy in the eyes of the AI?
		* How boxed is the AI?
			* Are we just connecting it to the internet?
			* Or maybe we want to restrict it to only actuators in a particular physical lab, except for being able to order resources from outside or sth?
			* Maybe we want to only let it do stuff in some virtual world?
		* in particular: How much are we letting the AI talk to humans?
			* e.g.: Could it effectively communicate a counteroffer to us, such that we could respond to that counteroffer? Are we committing to not doing that?
		* How are we "verifying" its proposed artifact?
			* We need to verify that it does the thing we wanted it to do.
			* We also need to verify that it doesn’t do anything else that’s bad. This seems much harder.
			* Are we using humans in the loop? How much time does the required human labor take?
		* In particular, are we asking it to give some sort of argument in favor of its artifact doing what we wanted and "only what we wanted", and then checking that argument?
			* What kind of argument are we asking for here?
		* How much are we telling the AI about our verification protocol?
		* Do we want to involve multiple AIs (that are possibly somewhat different instances of a single AI)?
			* One could have multiple agents compete to give the best solution.
			* One could involve debate.
		* Are we monitoring it? After noting how much concerning stuff are we stopping it?
			* What do we do once we stop the AI? Like, do we just commit to deleting the AI in that case? Do we commit to giving up and shutting down the lab?
* these are both from this presentation i gave a few days ago https://docs.google.com/presentation/d/1-j2khj5i7NSTTX1o4XsOjP34f2f5fdpvN5TgdHoBH_0/edit?usp=sharing
* another example: you have paul christiano write down his best behavior-based RSI scheme for getting to a very powerful AI that still does tasks for you (or whatever else he believes in, i'm a bit confused about how he imagines a lot of the stuff he seems to believe in being useful), with the current AI situation in mind
* i've been thinking of writing a guidebook for a self-improving human mind upload who goes in really intending to be nice to other humans. currently i have this short note on the topic
* generally, you think hard about what sort of work you want to get from AI researchers. you try hard to find more verifiable/objective alignment-relevant problems, and you think hard about how to set up verification/reward signals for them
* you think seriously about the speed of takeoff. you have some preliminary plans in place for different options
* you think about what you would do given centralization into a manhattan project vs not. think about how [the size of your lead] affects success probability
	* trying to figure out how to get an existential win given a 10 year lead is useful because it could happen in practice (especially if you fight for it) and also useful as a toy problem for when it doesn't happen in practice
	* (also it's a way to dislodge an imo common variety of poor reasoning about p(success) where you basically outside-view think p(doom) is eg 20% and then obtain a lot of the rest of your worldview from this via sth close to rationalization. if you think seriously about cases where conditions are much more favorable to AI working out, you can get your sense that p(doom) should be 20% hooked to these situations, and then that can seem reasonable to you, and then you can realize that in reality conditions are much worse than the nice case and your p(doom) should be higher in reality. of course this is still kinda poor reasoning. i guess a better thing is to take a step back and notice your p(doom)=20% intuition can get applied to any conditions and so any such application is pretty unreliable and then try to somehow think about stuff better than you have been :P)
* also cybersecurity / ai boxing stuff. think about persuasion, actually try to track that, establish procedures for that. eg friendship with claude should probably be considered a conflict of interest for many researchers at anthropic to a significant extent? think about ways to track claude's influence on anthropic's decision-makers and decisions. think about ways to track if it is still true that if there were a decision by anthropic leadership to turn off claudeanthropic, claudeanthropic would in fact be turned off. think about how to track/understand the extent to which humans still understand what’s going on in anthropic
* (there's also a version of preparing for RSI that tries to be more principled, that looks like doing philosophy and math and science relevant to reflective stability as explained eg here https://www.lesswrong.com/posts/Ht4JZtxngKwuQ7cDC/tsvibt-s-shortform?commentId=koeti9ygXB9wPLnnF and here https://www.lesswrong.com/posts/NqsNYsyoA2YSbb3py/fundamental-question-what-determines-a-mind-s-effects . this could involve studying toy versions of the problem, eg https://intelligence.org/files/TilingAgentsDraft.pdf . but this is much more out of distribution for anthropic than the stuff above)





















