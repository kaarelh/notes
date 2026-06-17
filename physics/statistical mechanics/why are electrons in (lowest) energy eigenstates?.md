



like, if you have a collection of hydrogen atoms, i think the standard picture is that each one has an electron in an eigenstate, with frequencies of atoms with each eigenstate given by the boltzmann distribution (i think this is roughly true even without explicitly observing them)

but why don't we instead have superpositions in each atom, with maybe the coeffs depending somehow on boltzmann?

idk. maybe we do have these coeffs, actually?

but i think we can at least make sense of mixed states decaying pretty fast to states that are close to being not mixed (tho idk if the end states still have a boltzmann amount of the higher state left)

# supposed explanation

edit: this is actually probably quite wrong, as richard thought when i told him about this (and then i figured out some stuff as well in that conversation, but mostly this is from richard):
* really if you're in a superposition, by linearity (assuming the rest of the world is fixed), what happens must be a linear combo of what would happen from each pure state. the model of decaying below makes it look like decay would be much faster from when you are between two states, but this contradicts linearity. really, decay from a mixed state is about as fast as decay from the pure higher state. (and what happens more precisely is probably that if you go measuring photons emitted from the atom, you get either nothing (with the atom just being in the ground state then) or a photon whose energy equals the energy gap, with probabilities given by squared coeffs in the superposition)

here's an explanation from https://arxiv.org/pdf/1602.04090

![[Pasted image 20250729171815.png]]

so, the point is that in a mixed state, you have some sort of oscillating dipole which must emit radiation. so (assuming no light coming in) you are losing energy, decaying toward lower energy


# but why decay to lowest energy states (even from higher eigenstates)

hmm, but we actually have decay all the way to the lowest state, right? even starting from higher eigenstates! maybe the point is that for any higher state, you in practice have at least some small perturbation, and then you get decay by the model above

(you also have some perturbation from the lowest energy state, but it will always be toward higher energy! you can't decay below it)

https://physics.stackexchange.com/a/671313

