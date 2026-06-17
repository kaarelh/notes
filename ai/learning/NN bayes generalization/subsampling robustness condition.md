
here's a robustness condition that i think would make subsampling work:
* suppose that the activations are rounded to finite bit precision
* further suppose that the wide NN is such that on every input, at every neuron, you are never within eps to the edge of the rounding bucket
* then (i haven't thought this through carefully but i think) we should be able to subsample while keeping all activations literally constant

the main question i have is whether this condition is really hard to satisfy or if it's actually not that bad. edit: it can really cause your norm to go up a lot. because you can implement a complicated thing in the small bits taking you over a bucket boundary, but not in the centers like this. so this doesn't work in general. but we could just by fiat say we consider only the NNs which satisfy this condition

wait maybe there's a problem with removing big weights actually...