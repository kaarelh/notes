
q: why should we say some particular things are microstates?
eg for a gas, why do we have even velocity and position boxes? eg why not even velocity-squared boxes?
eg for a system of non-interacting spins in a magnetic field (ie just two state particles), why not take there to be two different up states (like, a red up state and a blue up state) and only one down state?

these choices really matter — one gets different predictions for macroscopic quantities depending on one's choices. eg if you take there to two up states in the latter case, then you predict that the system will suck more energy from other systems (ie its temperature in the "same" state is lower )

kinda right but imo really sad answer: bro we're just making a model. one model works, another doesn't. you use the one which works. oh also, you could make a system such that the other model would work. so you have to just see which model works for the system you have in front of you

this is sad because you can actually know what a system is like (on a lower level, maybe, or you can just know its dynamics on that level), and then you can figure out which model is right given that. there is a mathematically interesting thing here after all



what i think is going on: there are some transition laws, i think for local energy exchanges. eg if you have two opposite adjacent spins, then maybe they can flip together with some probability on each time step. these transitions are typically probabilistic, and they have a stationary distribution. that stationary distribution is approached as time passes. this stationary distribution is the thing that determines what the right microstates are! like, they need to have equal probability in this distribution!

ok but wait. couldn't stuff depend on the interface between two systems? like, maybe i could make an interface from system S to the spin system such that it likes pumping energy into the spins as if there were two spin-ups, or a different interface S' such that it doesn't like that? i think one could make a perpetuum mobile if this were true. basically because you can get work out of heat flows or something

# messy notes

so, stationary distributions make sense, maybe. well, assuming the underlying local random interactions make sense... hmmm... i guess maybe it's fine to think of those statistically? but if we try to go this way, then we need to make sense of the following:
* for different situations, you get different markov chains. but somehow you don't get a contradiction? ok for instance, when you have a stationary distribution for A and B which marginalizes to something on B and a joint on B and C with the same marginal on B, then putting A and C in contact must give the same distributions on A and C as when they are in contact with B. why is the world this way?? well, you could say it's because there can't be a perpetual motion machine... but i feel like there ought to be a more fundamental story here...