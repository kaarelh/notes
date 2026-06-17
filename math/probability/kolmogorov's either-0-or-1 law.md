
Thm. let $X_1,X_2,\ldots$ be jointly independent random variables, and let $E$ be an event which can be determined by looking at any tail (for instance, that there are infinitely many times that a certain value is taken, or that a certain value occurs at a certain limiting frequency, or that a percolation graph has an infinite connected component). then E has probability 0 or 1

Pf.
* the measure of the intersection of E with any basis element of the sigma algebra is the same const c fraction of the basis elt's measure (this follows from E being a tail event and basis elts seeing finitely many variables)
* one can prove from this that actually the intersection of E with anything in the sigmaalgebra has measurefraction c. wait no this seems false. i think stuff works if one is given the measure frac thing for everything in the algebra made by basis elts though (which is in fact true for a tail event)? but is there a weaker assumption that gets you there?
* but then since E is in the sigmaalgebra, E has measurefrac c in itself
* but then mu(E)=cmu(E), so either mu(E)=0 or c=1 in which case mu(E)=1!

# mess

hmm, what even is the measure here? i guess we have measures for the independents, and then we have their product measure (might need caratheodory's extension thm to even say that's a unique existing thing? wait no that makes no sense)