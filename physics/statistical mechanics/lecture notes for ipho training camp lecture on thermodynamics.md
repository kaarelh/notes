

# Some statistical mechanics
i will start with a little bit of statistical mechanics because it lets one make sense of some stuff that is hard to make sense of otherwise. but we will soon get to more familiar stuff

# Entropy

## Microstates

You sometimes have a system which could be in some number of different states. A very simple example would be a single particle which can be in a high-energy state or in a low-energy state, at energies $\epsilon$ or $0$ (draw picture with two levels). In thermodynamics/statmech we are mostly dealing with systems made of very many small parts; maybe it looks more like this: (draw picture). Since each of these states corresponds to a specification of all the microscopic parameters of a system, we call these states *microstates*. Our example system has $\Omega=2^N$ microstates.

A gas is another central example — it consists of many billiard ball particles, each of which could be doing a different thing.

## Entropy as a function of energy

We are usually interested in cases where the total energy of a system is given — we will be counting microstates with a given energy $E$; let's denote this number $\Omega(E)$. For example, our system 

We usually speak of the entropy of a system at a given energy 

## Two systems in contact

Say you have two systems, initially with energies $E_1$ and $E_2$. You put the two systems in contact, they can start to exchange energy. If the two systems initially had total energies $E_1$ and $E_2$, then 


example: our simple example system with $N_1$ particles, and our simple example system with $N_2$ particles 
the energy split is actually nearly deterministic

# Temperature


## The notion of temperature

Let's think a bit more about the case above. Each system has an associated quantity $\frac{dS}{dE}$ which determines how well it can make new 

determines the direction in which energy flows from one system to another

Incidentally, this can be rewritten in a more familiar form: $dS=\frac{dQ}{T}$

## Specific heat capacity


$\frac{\text{d}}{}


## Thermal reservoirs

a thermal reservoir is just any huge thermodynamic system. the key property is that 


## The Boltzmann distribution

say you have a small system in thermal contact with a thermal reservoir

# Gases

The picture you should have in your head is of a bunch of billiard balls bouncing around in a box

## Maxwell-Boltzmann distribution

just a special case of the Boltzmann distribution, if you have the right microstates

## Energy per degree of freedom

just integrate velocity law for linear ones

equipartition! get 1 for each rotational degree of freedom, 

## specific heat capacity of a gas



## The ideal gas law




![[Pasted image 20250712230806.png]]

## Specific heat capacity at constant pressure


## A conversion law for an adiabatic reversible process

we say a process happening to a gas is adiabatic when there is no heat transfer in or out
we say it is reversible when the entropy of the gas is not changing
in practice, this means that the gas is expanding or contracting slowly — it is at equilibrium throughout the process

$pV^\gamma=\text{const}$




# Flow