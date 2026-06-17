https://www.youtube.com/watch?v=SZ6TWaNt5LQ

The lecture is about searching for proofs of mathematical statements, discussing both practical methods and what's known about the theoretical complexity of the problem. (The problem of checking whether there is a proof of length n is obviously NP-complete.)

One way to prove a formula is not satisfiable is to pick a value for variables one at a time, check if some clause is unsatisfied on each step, if yes just go up to the lowest node which has not been fully checked yet and pick the other value.

A cool idea is to relax 3SAT constraints like $x\lor y\lor \bar{z}\to x+y+(1-z)\geq 1$; I guess this is sort of like saying that we are assigning truth mass to each variable such that the masses add up to 1. Also have $0\leq x\leq 1$ for each variable. And then just solve the LP? Oh I guess she is only looking for integer solutions, so I'm not sure how we made progress. Ahh we made progress by having some inference rules in this case that would not be present for LPs over reals, such as $2x+2y\geq 1\implies x+y\geq 1$. This is nice, I wonder if it can be automated though? Like, is there an easy way to check for solutions to a system of equations together with this kind of set of inferences?

Or to use algebraic proof systems, could do $x\lor y\lor \bar{z}\to x+y+(1-z)\geq 1\to (1-x)(1-y)z=0$, and also have the constraint $x^2=x$ for each variable.

Then lots of cool results about equivalences between there being fast algos for checking for proofs of a certain size in the above schemas and e.g. stuff like NP = QP (meaning quasipolytime, i.e. $n^{O(\log n)}$ I think).