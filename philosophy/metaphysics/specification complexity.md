
* kolmogorov complexity doesn't see "mathematical work" at all
* we can define a pareto boundary for ways to specify a thing with kolmo and time complexity, eg for a proof
	* let's say it's the shortest proof of some theorem to make the discussion easy
	* then we might have "it's the shortest proof of the statement blah" as the shortest kolmo spec of the proof (ok one would also want to compress the statement of course)
	* and i guess on the other end, the lowest t-complexity spec of the proof just is the proof (we can pick a formalism such that this is literally true, but it should be morally true given any reasonable choice of formalism)
	* what are some intermediate points? one sequence of points could be obtained by giving away successively more intermediate lemmas. like, starting from the extreme of giving away just the theorem statement, we have a next point that gives the lemma of the proof that serves as the most helpful hint to what the proof is, and then the next point after that gives the most helpful pair of hint-lemmas, and so on, until eventually getting to the other extreme of giving away all the statements in the proof
	* of course, these are unlikely to be on the pareto boundary — one can probably do better. for example, one might 
* initially, a thing is often found by having specified a problem to which it is a solution. but then later one can see it as being made of its pieces
	* for example, you find a proof involving some new objects (or auxiliary theorems or methods). later, you start appreciating the objects, and using them for other stuff. you might eventually see that proof as an example use case for these objects. the proof goes from being almost entirely "seen as a solution to a problem" (which is low kolmo complexity, but high time complexity) to being seen somewhat in terms of what it's made up of (which is higher spec complexity, but lower time complexity)
	* we can imagine something similar happening for:
		* technologies
		* structures in neural nets
* o4-mini-high on cases in which search targets are specified in the genome: https://chatgpt.com/c/685c08a0-625c-800f-ab3c-a6829b225969

