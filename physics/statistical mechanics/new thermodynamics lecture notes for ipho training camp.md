
# the boltzmann distribution

$p_i \propto e^{-\frac{E_i}{k T}}$ 
* each given higher energy state is always less probable
* but the difference becomes smaller as T becomes larger
* i'll maybe come back to deriving this later if there's time and interest


# the maxwell distribution

for an ideal gas, the velocity pdf is: $p(\vec{v})\propto e^{-\frac{m|\vec{v}|^2}{2kT}}$
* this is an application of the boltzmann distribution, for a particular choice of states
* can split into v_x, v_y, v_z and see these are independent. like p = p_x p_y p_z
* can integrate to find that each v^2 avg is kT/m, and so each mv^2/2 average is 1/2 k T
	* you can reduce this to an ordinary gaussian integral by:
		* noting you're differentiating under the integral sign
		* bringing that out
		* and then noting you're just finding the derivative of the log of a usual gaussian integral
		* you can find a gaussian integral using this trick:
			* let I denote the gaussian integral int e^{-r^2} dr
			* then I^2 = pi int 2 r e^{-r^2} dr, with the int now running from 0 to infty
			* noting that we are integrating a derivative, this becomes -pi int d e^{-r^2} = pi
			* so I = sqrt pi
		* hmm potentially we could just have treated this as a constant actually... like, maybe you don't need to even calculate this to find the mean here?
	* and then

# total heat energy in a gas

can notice that each translational degree of freedom carries energy 1/2 kT per molecule. in fact there can be more degrees of freedom: if gas molecules have more than 1 atom, then we get rotational degrees of freedom. and at sufficiently high temperatures, you can also get degrees of freedom from bonds oscillating — these have kT each. i think this has to do with getting 1/2 kT for each quadratic term, and there being two quadratic terms in the harmonic oscillator energy. some numbers of degrees of freedom at room temperature:
* a single-atom gas has 3
* a linear molecule has 5 typically
* asymmetric molecules have 6 typically

anyway, letting the number of degrees of freedom be $i$, the total energy is $\frac{i}{2}kT$ per molecule then. 

# heat capacity

at const volume, the heat capacity of a molecule is thus $\frac{dU}{dT}=\frac{i}{2}k$. the molar heat capacity is $c_V=\frac{i}{2}kN_A=\frac{i}{2}R$. the specific heat capacity is $\frac{i}{2}\frac{k}{m}$

at const pressure, as you heat a gas, it will be expanding (ask for an example of a system), and so doing work $W=\int P dV$ (can someone give me a proof that this is work done?). the first law of thermodynamics says Q = $\Delta U + W$, heat supplied is work done by the system plus the change in its internal energy. so to change by $\Delta T$, you now have to increase internal energy by the same amount $\frac{i}{2}n R\Delta T$, but you also have to do work $P \Delta V=\Delta (PV)=\Delta(nRT)=nR\Delta T$, for a total of $\frac{i+2}{2}nR\Delta T$, so the molar heat capacity at const pressure is $c_P=\frac{i+2}{2}R$



# Pressure and the ideal gas law

what's the pressure of a gas again? well, it's the force per area experienced by a wall of the gas. we would like to relate that to other stuff

we will assume monatomic particles and a mirror wall in the yz plane (i guess it's clear that pressure cannot change if you change the wall, because otherwise you'd have a way to get infinite work from a gas). maybe do const velocity case first?
observation 1: when a molecule with velocity v_x hits the wall, it gets velocity -v_x after. so the momentum transfer from that bounce is 2m v_x
observation 2: the molecules which hit the wall in time t are precisely half of those which are closer than their velocity v_x (the ones which are going toward the wall). (we can make t small enough that we don't have to worry about internal bounces)

in the layer between distance x and x + dx, the contribution to the momentum transfer is S dx rho * int_{v_x is in the right direction and tv_x > x}

each mass with tv_x > x contributes 2 m v_x, others contribute 0
the avg contribution is thus m int_{x/t}^\infty p(u) 2 u du
the total contribution is thus S dx N m int_{x/t}^\infty p(u) 2 u du

the contribution from all layers is thus 2 S N m int_0^\infty dx int_{x/t}^\infty p(u) u du

draw plot of int domain with u on vertical axis and x on horizontal. see the line u=x/t. change order of integration, so now x goes from 0 to ut inside, and u goes from 0 to infty:

int_0^\infty du int_0^{ut} p(u) u dx = int_0^\infty du p(u) t u^2 dt = t/2 total int = t/2 kT/m

so left with momentum transfer St Nm kT/m, so force rho/m kT = NkT, as desired!


![[Pasted image 20250713022304.png]]

the idea: for each of the two gases, we have some rate of hitting a small hole (in which case one goes through it)



![Pasted image 20250712230806.png](app://a9a45370e673b3e67a018bab3a262bab6d0b/Users/kaarelh/Documents/notes/Pasted%20image%2020250712230806.png?1752350886999)

will get heat flux prop to delta T. mention the general law that heat passed is prop to delta T. also that in 




EuPhO 2017 T2:
![[Pasted image 20250713024420.png]]



one more thing about pressure for now, which relates to the ideal gas law:
dalton's law: if you have a mixture of gases, then you can think of each one as causing a partial pressure (given by the ideal gas law for that gas), and the total pressure is the sum of these partial pressures
# adiabatic thing derivation

adiabatic: no heat transfer and reversible. this is when a gas expands slowly or is compressed slowly, where "slowly" means slowly enough that it is in equilibrium at all points throughout the process

for adiabatic expansion, it turns out to be true that $PV^\gamma=\text{const}$, where $\gamma=\frac{c_P}{c_V}=\frac{i+2}{i}$. eg for a monoatomic gas, $PV^{5/3}=\text{const}$.

for an adiabatic process, internal energy decreases by the work done:
$P dV = - dU = -c_V n dT$

to get a relation between pressure and volume only, we'd like to get rid of dT. we can do that using the ideal gas law: $dT = \frac{d(PV)}{nR}=\frac{P dV + V dP}{nR}$

this gives $RP dV = -c_V (P dV+VdP)$, so $(c_V+R)PdV=c_V VdP$, so $\gamma P dV + V dP=0$. multiplying by $V^{\gamma-1}$ gives $d(PV^\gamma)=0$, as desired

other versions of $PV^\gamma=\text{const}$:
* $TV^{\gamma-1}=\text{const}$ (just plug in T for PV)
* $T^\gamma \propto P^{\gamma-1}$ (write the original thing as T^gamma ie (PV)^gamma over P^{gamma-1})

note that this means we have three unclear quantities: T,P,V, with two equations relating them — the ideal gas law and the adiabatic law. this means knowing any one variable gives us the other two. so having this, we sorta fully understand adiabatic expansion


![[Pasted image 20250713080303.png]]

can just use delta P = rho g h
but there is also the better formula rho$=\rho_0 e^{-\frac{mgh}{kT}}$. this is just boltzmann, but can also be derived from integrating dP = rho g dh with dP plugged in in terms of other stuff, assuming const temperature 



![[Pasted image 20250713031239.png]]



![[Pasted image 20250713124541.png]]


# surface tension

![[Pasted image 20250713133854.png]]