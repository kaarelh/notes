
## Questions

* Why is it the case that generalization happens first for small weight norms? In what sense does it even happen first? Maybe it's just that the best memorizing solution at low weight norms doesn't have enough oomph to push logits sufficiently noticeably?



## Parameters (some (initially) unknown)

* logit-oomph of the best (or maybe a typical) memorizing solution with a given weight norm
* logit-oomph of the best (or maybe a typical) generalizing solution with a given weight norm
* when restricting to a sphere in weight space: its radius
* when not restricting to a sphere: weight regularization hyperparameter

logit-oomph should maybe just be KL divergence on train data?

## Observables

## The model

There are a bunch of memorizing and generalizing points at infinity. Maybe these attract the model when it is being trained? 

two different effects potentially:
* each param is used on many data points (can maybe look at scaling in the number of data points)
* params are in bigger circuits, meaning slower learning, but then eventually faster when other stuff is scaled up too?



## Relations



## some more uncategorized ideas

If stuff gets learned continuously, we can predict how the num of steps to learn each thing depends on how frequent each thing (separate task, eg like in Tegmark's quanta model) is in the data. (It's unclear if the random walk picture, or whatever other picture, would make a different prediction though? maybe the predictions are just the same here?)


## ramblings

* There's no such thing as stumbling around until you hit a circuit, then pumping it up. You won't ever stumble around and find stuff before the age of the universe. It's all just built up, perhaps slowly. The generalizing circuit probably starts getting built at the beginning. 
* If the generalizing circuit gradient is always present, how do we see it from the data points? Perhaps we could look at the data set of gradients on individual data points, tracking how much 

in a grokking setup, is it plausible that we could see the generalizing circuit being built continuously from the beginning if we just analyzed the data set of gradients on individual data points the right way?


sth like: maybe when you do a gradient update on a data point, you push the generalizing circuit up by a tiny amount, and then a memorizing circuit for that data point up by a large amount, and we just need to find this decomposition of the gradient



maybe the gradient on each data point just roughly decomposes as a sum of a vector toward building some generalizing circuit (it could also start building many different generalizing circuits all at once) and a vector toward building a memorization of that data point



and we can find this decomposition and it lets us empirically figure out how (fast) the two kinds of circuits are getting built during training



and then on the theory side, maybe we could write down some heuristic differential equation for the same thing also and see if we can get that to match this data



another way to see if we are doing something legitimate with this memorization-generalization gradient decomposition would be to try to use it to just take steps in the direction of the generalizing circuit, seeing if this prevents memorization before generalization in the grokking setup (in fact, we might be able to generalize faster this way by just taking bigger steps without noise from the memorization component messing things up or something (i guess if this worked, maybe that'd be capabilities progress, and then in this low-probability conditional maybe we shouldn't post it))


math problem: suppose I have a dataset of vecs $v_i = g+m_i$, but I only see the $v_i$, not the decompositions. how do i recover the decompositions? suppose that each $m_i$ is gaussian with norm such that the initial walk is mostly toward memorization.
* i guess maybe this means that $\sum_i m_i$ has higher norm than $Dg$ where $D$ is the size of the data set. If the num of params is high compared to $D$, the norm of $\sum_i m_i$ is like $\sqrt{D}\lVert m_i \rVert$, and the norm of $Dg$ is like $D\lVert g \rVert$. Here the inequality for the memorizing circuit getting learned first would be like $\lVert m_i \rVert \geq \sqrt{D}\lVert g\rVert$. 
* I don't really think contribution size to logits scales at all like that though! this would depend on sth like how sequential the circuit is and how big it is already?

anyway, we have these decompositions, but the issue is that $g$ is sort of small. I guess this is some problem of recovering a signal when you have a lot of gaussian noise? yea you have a signal $g$ with coordinates let's say standard normal (std 1), of which you have $D$ noisy readings of noise of size let's say std $\sqrt{D}$. so you more or less can't recover the true value of any coordinate because the likelihoods aren't that far apart. you might be able to require some linear combo of its coordinates though?

i guess maybe the broad takeaway is just that at the point where recovery can be done, one can just do recovery by taking the average, but that's just the total gradient being toward the generalizing circuit

ha! but because of the linear combo observation, one can actually track movement toward the generalizing circuit before if one knows the secret generalizing gradient vector! this could be a nice way to extend the range in which we can try to measure generalization vs memorization learning speed! 


## A story of learning, of generalization vs memorization, of pattern learning speeds

I don't think this will be exactly right, but I think this might be a good first-pass story. 

* ~Every possible way to solve the problem ("circuit") starts getting learned at once.
* Each has a lawfully determined gradient pushing toward it — in fact, the gradient will be a function of its weights only.
	* For example, a boolean function has many circuits implementing it.
	* If the function has a not-too-small number of inputs, then it won't be pinned down by a not-huge data set. So there are many boolean functions consistent with the given input-output data.
* the observed input-output behavior is just an average of the outputs of all the different circuits. 

alternatives:
* jake: more degrees of freedom means bigger manifold, so probably has a pt closer to the origin? wait tho, wtf is the manifold? is this like a regression task? i guess i sorta agree then?
* 

## simplest concrete case

just one hidden layer, boolean function


## against the weight norm being linear in the effective parameter count

suppose that the total circuit is a sum of a bunch of circuits with their params. suppose further that each circuit is roughly orthogonal to every other circuit. then 

## unclassified ideas
* we can fix a different learning rate for each layer to make different kinds of circuits win
* 
## lit review

https://openreview.net/pdf?id=LEuuOaZNOT


Hidden Progress in Deep Learning: SGD Learns Parities Near the Computational Limit 
https://arxiv.org/pdf/2207.08799.pdf

slingshot mechanism: bs, doesn't say anything interesting about generalization in practice, can be ignored probably https://arxiv.org/pdf/2206.04817.pdf

Towards Understanding Grokking: An Effective Theory of Representation Learning, something similar to what we are interested in happens here: https://proceedings.neurips.cc/paper_files/paper/2022/file/dfc310e81992d2e4cedc09ac47eff13e-Paper-Conference.pdf 

