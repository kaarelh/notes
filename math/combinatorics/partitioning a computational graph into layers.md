
We are given a directed graph $D$ (which we think of as a boolean circuit where the vertices correspond to gates), and we want to partition its vertices into layers, possibly splitting some vertices into many copies, such that edges only go from one layer to the next. Is there a nice way to construct such a presentation with the smallest number of vertices?

More precisely, we are looking for a directed graph $D'$ whose vertices are partitioned into layers such that there is a mapping from vertices of $D$ to those of $D'$ such that the image of 


hmm i guess the problem is asking for a permutation of the vertices (think of this as an assignment of integer times when gates get computed) such that inputs come first, outputs come last, each gate comes after its input gates (so it is a topological sorting of the vertices), and the max over times t of [the number of vertices computed before t which have an edge to a gate computed after t] is as small as possible


this formulation of the problem is assuming there is no depth constraint/minimization — not sure if this is reasonable

this problem is np-hard! https://dl.acm.org/doi/pdf/10.1145/800125.804049


(and in fact, when u generalize to non-[directed acyclic graphs] (think of this maybe as it being possible to recompute a gate from later gates if desired), this is PSPACE-complete!! https://dl.acm.org/doi/pdf/10.1145/800135.804418 )

(this paper's abstract starts with "The search for efficient algorithms for register allocation dates back to the time of the first Fortran compiler for the IBM 704")
