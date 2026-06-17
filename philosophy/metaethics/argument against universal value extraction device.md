
* could there be a universal value extraction program E that halts? 
* for any program P, we can construct a P-trickster $T_P$: a guy that has values very different than what P would think its values are.
	* one would want to say that the source code of $T_P$ looks as follows: to decide what to value, compute $P(T_P)$, then value something very different. and then some other understanding-y stuff etc around that value spec
		* unfortunately, this doesn't literally make sense, because you can't just directly write the source code of this program in its source code
		* but you can probably fix this with quining: i think it should be possible to make a program that does arbitrary stuff that begins by making a variable equal to its own source code?
		* i guess to see this through carefully, let's say that our agent has to ultimately have the structure of outputting an action in every context, given as an input. so an agent is a computable function
		* now we have a spec of the agent given its source code. we can think of this as having specified Q(x,y) where x is supposed to correspond to the source code and y is the context
		* by kleene's second recursion theorem, there is a program q such that q(y) = Q(q,y). we take this to be the sought T_P!
* since there is a P-trickster for any P that always halts, there cannot be a universal value extraction program
* that said, of course there could in principle be a value extraction program that works in nice cases
	* but there isn't a computable extractor that works for all computable agents tho (ie those whose context->action function is computable), because the trickster for it will have computable Q(x,y) and hence computable q(y), so it will be computable, so it's a problem the extractor fails for it. that said, if the extractor doesn't have to halt on all programs, then maybe it can exist