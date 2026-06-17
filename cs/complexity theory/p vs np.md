

# 24/10/02

i wish we could somehow use the separation that polynomials of $\aleph_0$ are still $\aleph_0$, whereas an exponential is larger. like write down some infinite SAT problem and be like: if SAT had a polytime algorithm, then this would need to have an $\aleph_0$ time algorithm. but this doesn't have a countable algorithm. but idk how to set up an infinite problem like this


maybe would like to have some infinite circuits for this infinite SAT? but surely you can make the circuit countable just by using the exptime algo. i guess we could require that the circuit have constant depth at all locations or something, whatever that means? and then try to show it needs to be countably deep and also wide enough that we get continuum many gates? and then somehow the polytime SAT solver would give something smaller, so we have a contradiction?
# 24/09/19


https://www.scottaaronson.com/papers/pnp.pdf
p=np is equivalent to the existence of an at most n^2 length proof for an arbitrary statement being polytime checkable. (edit: oops nvm)
pf (edit: oops nvm):
* can reduce sat to the existence of a short proof that exists x1 exists x2 ... exists x_m s.t. phi(x_1,x_2,...,x_m), because if there is a satisfying assignment, then one has a short proof also (just state the assignment and check it — in fact this should be linear length), and if one has a short proof of this, then of course there is a satisfying assignment (assuming zfc is consistent?? wait do i have to be worried here? is a different proof needed? oops confused). so the proof problem is np-hard
* and the proof problem is in NP because a proof can be checked in polytime
oh wait actually yea the con zfc thing is a real issue i guess. if not con zfc, then the existence of a proof of a given statement of at most n^2 length is const time! so polytime. but maybe p could still neq np then

anyway p=np would imply that the proof problem is in p. can we use the proof problem being in p to do some weird diagonalization? like i want to go from this to constructing a TM which outputs the opposite of what it outputs


# older
what's needed for some diagonalization argument? well, we need something to speed up given a polytime sat algorithm. the obvious candidate would be sat-verification. but obviously you can't do that faster than reading the formula, which is also roughly the naive verification time, so this seems unlikely to work. 


can we think interestingly about first-order theories which have 'axioms that can be listed in polytime' vs 'according to some problem in NP'? can we prove that any theory for which 'axioms can be listed in polytime' has some certain property and show that some 'NP-complete theory' does not have this property?