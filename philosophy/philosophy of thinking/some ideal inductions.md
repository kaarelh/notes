
solomonoff induction is cool, but i think it makes sense to be interested in other ideal inductions as well. here, i aspire to get at some that are a tad closer to human thinking in terms of their type signature, and more likely to "actually work" (i think solomonoff induction doesn't actually do many of the things one would intuitively think it does if one thinks of it as being an ideal induction, eg it doesn't give you a proof of the riemann hypothesis after a bunch of interleaved statements and proofs)
* say you have a bunch of questions. some of these are already answered, often tentatively. examples of questions:
	* at what temperature does ice melt (at what pressure? did we mean pure water ice? maybe etc)
	* what is the speed of light?
	* what is the force on object A in such and such a configuration of rigid bodies and ropes in gravity
	* is there a natural number n > 2 and integers a,b,c such that a^n + b^n = c^n ?
	* are dogs usually bigger than cats?
	* are yetis real?
	* what's my name?
	* what's the eur usd exchange rate as of 2026/05/29
	* every resolved prediction market question
* the above are all questions whose answers we kinda take to be well-defined single things. like, there aren't two different fine answers to "what is the speed of light?". we could also include questions for which this is not true, eg "what is the cause of eclipses?", "what's going on with the precession of mercury?", etc. i think it's a bit easier to think about stuff if we don't do this for now 
* now you have a new question. what would you do, to answer it by induction? some options:
	* you could just throw all the stuff you have as strings in some standard format into a solomonoff inductor and put the new question last and see what comes next. i think this probably doesn't give you a good answer. i explain this in other notes
	* you could do solomonoff function induction. i think this is a good idea, but it also fails in that way
	* maybe we can think of induction as being from similar cases. then we need to bring into attention some similar questions, and see what the answers to those are, and so answer the question
		* one way to do this would be to use some sort of learned similarity between questions. this prompts: where does the similarity come from?
		* one way to do this would be to think of the question as a special case of some class of questions, and to look at other known answers of questions in this class. this prompts: how 