
difference between SVD on activations vs mean + PCA on activations to reduce to lower dimensional thing 

$k$ singular values in layer $\ell$ activations being $0$ correspond to degrees of freedom in weight matrix, namely there 

Q1 I want to ask next time: Wait, does this actually give a way to speed up inference / does it reduce it to a smaller circuit? Don't you still need to translate back to the neuron basis to apply activations? One can of course write down a function from the vectors in the nice basis in layer l to the nice basis in layer l+1, but this will be something messier than linear + activation — the activations will apply in a weird non-coordinate-wise way.

Q2 I want to ask next time: Have you checked how this differs between the underparametrized/overparametrized regime? (i.e. does something weird happen as one goes through the interpolation threshold?)