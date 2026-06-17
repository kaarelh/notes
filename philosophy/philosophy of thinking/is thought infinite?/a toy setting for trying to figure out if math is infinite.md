
(this will probably be somewhat like my toy model of tech progress)

* you have a bunch of problems. maybe let's say they are mathematical problems. they are given by verifiers i guess, and your job is to find a string that satisfies the verifier. we could also do different games.
* let's say problem-solvers are given by algorithms. a problem-solver gets the problem as an input and can either output a solution or "sorry couldn't solve this"
* for each problem-solver, there will be solvable problems it doesn't solve. proof: providing a halting computation history is a problem of the kind considered here, and it is solvable when your TM actually halts, so if there were a problem-solver that could solve all solvable problems, we could construct a halting oracle out of it. so there isn't a computable problem-solver that solves all problems
* In fact, for each problem-solver, there are infinitely many solvable problems it doesn't solve. This is because there are infinitely many different ways to encode halting problems, and inside each way to encode halting problems, there must be at least one problem it doesn't solve.
* I'd like to understand what the space of problem-solvers looks like. In particular, I'd like to understand it in terms of:
	- The problems each problem-solver solves
	- The specification complexity of the problem-solver
	- The time complexity of the problem-solver
-  maybe it makes sense to look at some example families of problem solvers
	- we can consider problem solvers of the following form: there is a parameter L, and the problem solver looks to all strings of length at most L and checks whether they satisfy the verifier. If it finds one, it outputs that string. If it doesn't find one, then it just says "sorry, I don't know how to solve this problem." These have short specifications and they solve quite many problems, but they are also extremely slow. we could call these the brute-force searchers
	- 
