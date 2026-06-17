
one general method for trying to pull niceness out of the ether:
* say you have a process P with a certain time bound and a certain spec length
* you run it on some inputs, getting some outputs (let's assume it's the sort of thing that does that). record these in a data set
* now say you have some oracle which gives you the simplest process $P'$ with those inputs and outputs

what are some ways how you might have gained from this?
* mostly: $P'$ might be easier to run. most importantly, it could be faster. it could also be less expensive per run. so, we could now have a better way to get $P$-like outputs on inputs 

however, there is also the following possibility:
* maybe the process $P'$ has higher t-complexity but lower k-complexity. and maybe it in fact generalizes "correctly" to things which are not in the time bound of P
	* example: you get humans to provide provable/disprovable labels to mathematical statements, in cases where given mathematical literature your math researchers can figure it out in 1 hour. it seems plausible this generalizes correctly to statements we couldn't prove/disprove in 1 hour?
* i guess we could probably even come up with cases where P' avoids some mistakes P would make on inputs that should be fair game for it? like, we'd construct it such that mistakes are random or something, so maybe the highest-probability thing to do is to not make them (consider the gpt chess example where this happens). but this feels more contrived than the previous bullet point