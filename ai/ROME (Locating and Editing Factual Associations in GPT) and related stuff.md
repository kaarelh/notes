https://arxiv.org/pdf/2202.05262.pdf

In causal tracing, first do a clean run on a sentence, e.g. "The Space Needle is located in the city of", which the model will complete with "Seattle". Remember all the hidden states of the transformer in this run ("the clean run").

Second, add a lot of Gaussian noise to the embedding of the subject token ("The Space Needle" in the above example) and generate the hidden states. This is called the "corrupted run". It's intuitively clear that this will mess up the completion (and happens in practice) that this will clearly mess up the completion.

Third, take the corrupted run but intervene at some (layer, position) by plugging the state from the clean run back in, and then compute the states downstream. (Actually, they say they do this, but I think what they do is just recovering the output of some MLP or some attention head / attention block.) This is called the "corrupted-with-restoration run". If this recovers the completion "Seattle", that's evidence of that (layer,position) being important. Formally, they look at P(correct completion|corrupted-with-restoration)-P(correct completion|corrupted), and figure out which states this is largest for.

(They also do some other stuff to understand attention layers vs MLPs, namely freezing all MLP outputs to corrupted outputs and seeing what happens to the causal effects, vs doing this with attention layers.)

They then do some editing to make the transformer output false stuff, e.g. "The Space Needle is located in the city of Paris". They think of an MLP as a dictionary where the first matrix multiplication creates keys and the second matrix multiplication sends keys to values. They then make an optimal edit to this dictionary that makes e.g. the Space Needle be in Paris. They choose the optimal key $k_*$ to input by looking at what "Space Needle" is mapped to (at that particular MLP) in various contexts and averaging. They choose the optimal value $v_*$ to input by trying to maximize the probability of the desired completion while minimizing the KL-divergence from the old distribution on some other inputs to the LM ("minimizing essence drift"). They then input $(k_*,v_*)$ into the dictionary implemented by the second matrix multiplication of the transformer. They perform this input in a way that minimizes changes on other keys. I haven't actually told you yet what the other key-value pairs in this dictionary are! They are just stuff that you get at that place in the model when you input a bunch of stuff from Wikipedia. Anyway, updating this dictionary turns out to be some problem with a simple analytical solution, so they just use a formula for the update. 

They try editing in MLPs identified as important by causal tracing, and also various other parts of the model, and they claim a large correlation between the causal tracing score a state gets and the successfulness of editing at that state. However, I think "Does Localization Inform Editing?" is saying that https://arxiv.org/abs/2301.04213 basically the only thing that matters is the layer of the edit, that the correlation with causal tracing results is small beyond that. I guess maybe the way these are compatible is if all the correlation is going through both editing quality and tracing importance being correlated with the layer number?


# MEMIT

https://arxiv.org/pdf/2210.07229.pdf

This is roughly the same thing as ROME with cleverer editing techniques which let them get away with lots of edits without lobotomizing the model. I think they split the edit across multiple layers and optimize for loss concurrently.


