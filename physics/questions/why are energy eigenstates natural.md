
# clean

* energy eigenstates time-evolve nicely — they just get rotated by a global phase
	* this means that it is nice to think of time-evolution in the energy eigenbasis in general
* conjecture: fix a hermitian operator and a (finite) potential. then if a state is such that its time-evolution preserves the distribution of the operator, then it is an energy eigenstate
* i think the above is somehow related to finding electrons in energy eigenstates (as opposed to finding them in linear combinations of energy eigenstates). sth like: if you're not in an energy eigenstate, the above statement for the position operator implies that your probability density cloud is not constant, which implies that you are emitting electromagnetic radiation, and thus losing energy
* 
# messy

why are things often nice in a few bases?

if u have sth const in time (or really hamiltonian eigenstate) and u have a periodic material then u need to have a periodic solution with the same period times e^ikx


https://en.m.wikipedia.org/wiki/Bloch's_theorem

but why hamiltonian eigenstates? because they time-evolve independently, ie time-evolution nice in this basis, can think about what happens to each independently

but can we say more? can we prepare/separate them easily?

prism can separate modes/eigenstates, also they have different speeds

maybe also can prepare them (eg look into how eigenstates are prepared in experimental physics)? but then in this way does every (hermitian) operator for which a measurement device can be built / is present lots in nature have nice/natural eigenstates? can a measurement device be built for every hermitian opetator? can we classify the hermitian operators for which a measurement device could be built? is there some “nice generating set” for these, eg position and momentum in some sense (this example: probably false)???

hmm see https://physics.stackexchange.com/questions/75401/does-every-hermitian-operator-represent-a-measurable-quantity


edit: the thing below is actually probably quite wrong, as richard thought when i told him about this (and then i figured out some stuff as well in that conversation, but mostly this is from richard):
* really if you're in a superposition, by linearity (assuming the rest of the world is fixed), what happens must be a linear combo of what would happen from each pure state. the model of decaying below makes it look like decay would be much faster from when you are between two states, but this contradicts linearity. really, decay from a mixed state is about as fast as decay from the pure higher state. (and what happens more precisely is probably that if you go measuring photons emitted from the atom, you get either nothing (with the atom just being in the ground state then) or a photon whose energy equals the energy gap, with probabilities given by squared coeffs in the superposition)
electrons decay from mixed states to eigenstates, https://arxiv.org/pdf/1602.04090 :
![[Pasted image 20250729171815.png]]
(also you have decay from higher eigenstates to the lowest available one. maybe this happens because you are always not precisely in a higher eigenstate?)

* conjecture: roughly, probability density is const <=> the particle is in an energy eigenstate
* i think we need to say "roughly" because the strict statement has at least the following type of counterexample: you can make a linear combination of two disjointly supported eigenstates with different energies; eg one should be able to make this if your potential has two infinite square wells. hmm im guessing one can just def roughly := for any finite potential?
* wait, is this true not just for the probability density, ie the position measurement distribution, but for the any hermitian operator measurement distribution? ie for any operator, its distribution is const roughly iff the particle is in an energy eigenstate

atom expanding, also galaxy then, but somehow falls back together after all the time. maybe makes sense for atom given that it’s bombarded by stuff all the time anyway and it sort of stays in an eigenstate? do we need like tidal forces for a galaxy though?

also for atom adiabatic thm says if hamiltonian perturbed slowly it stays in an eigenstate (of the new hamiltonian)? does this apply to make more mechanistic) sense of why it stays? anyway, it might also explain the eigenstate being natural

also, why are only discrete emissions possible? ie why does the photon need to have energy level diff energy, why can’t you get an energy level diff where 0 1 ish falls to like sqrt{1/2} sqrt{1/2}?
(also richard says the default is some sort of boltzmann distribution? with the coeffs on each single atom electron being boltzmann too! is this true?)
fermi golden rule should say sth richard says
richard says the photon electron absorption does not assume peakiness, derives it
or maybe follows from conservation of energy under measurement? tho unclear if this works, who knows what measurement devices do? but maybe would be weird for the device to get energy in the right direction always lol? or maybe not? certainly for a device that just collapses while staying quantum this’d need to be the case anyway, but it probably isn’t how it works i guess, probably this’d be weird
also another ans is that maybe this is generally the same reason why measurement works at all, it couples states in the same way, maybe the state of the photon needs to be coupled to the state of the electron


incidentally but relatedly, the different speeds of different frequencies in a material might also be a significant amount of the reason why it makes sense to split information channels via frequency — otherwise the shape u create splits over time (its diff components get there at diff times) 

concrete question: take finite sawtooth, propagate for some time. do u more or less see different modes separate out? this might also be a way to see different modes as natural — they are what u see locally after a while? maybe most natural construction is inf sawtooth times gaussian. need to think about the fourier transform of a wave times a gaussian to understand what happens to this

equilibrium physics lowest energy eigenstates — dmitry

systems tend to lowest eigenstates? is this just the boltzmann claim or is there more to it

superposition and microstate uncertainty indistinguishable in statistical QM maybe says dmitry

