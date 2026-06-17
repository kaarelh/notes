

plausibly missing a lot of the computation doing a thing by doing mean or resampling ablations on a task distribution!!

eg "In light of this, we examine GPT-2’s task performance by using causal techniques to identify a circuit: a minimal computational subgraph of our model that suffices to compute the task [35, 14]" from https://arxiv.org/pdf/2305.00586.pdf 


"A useful abstraction for this goal are circuits. If we think of a model as a computational graph M where nodes are terms in its forward pass (neurons, attention heads, embeddings, etc.) and edges are the interactions between those terms (residual connections, attention, projections, etc.), a circuit C is a subgraph of M responsible for some behavior (such as completing the IOI task)"

it is ridiculous to say, at least absent other arguments, that their methodology gives the circuit that 'computes the task' in the intuitive strong sense (it might in some wacky sense wrt a very particular distribution), because eg it would totally miss any computation that decides one should run the circuit they find on certain inputs. this could be the majority of computation!!



from https://openreview.net/pdf?id=NpsVSN6o4ul :
A first na¨ıve knockout approach consists of simply deleting each node in K from M. The net effect of this removal is to zero ablate K, meaning that we turn its output to 0. This na¨ıve approach has an important limitation: 0 is an arbitrary value, and subsequent nodes might rely on the average activation value as an implicit bias term. Because of this, we find zero ablation to lead to noisy results in practice.

is it really because of this reason?? i doubt this!! why could it not be because they do stuff, just the same stuff on anything in p_{ABC}. eg a complicated calculation determining that the circuit they think does it should be run / should be allowed to affect the output because that makes sense in that context!!

the names 'knockout' and 'ablation' are atrocious for this i guess..

"We do so by using circuits analysis (Rauker ¨ et al., 2022), identifying an induced subgraph of the model’s computational graph that is humanunderstandable and responsible for completing the task."

might be worth also imagining a concrete circuit that does some much more general thing doing it. in the limit: a general cognition circuit. what would their methods yield if that were how it's done?

https://dynalist.io/d/n2ZWtnoYHrU1s4vnFSAQ519J#z=fh-HJyz1CgUVrXuoiban6bYx