# in this section, new ideas at the top 



from how many training data pts does a transformer typically learn a fact? eg a relation between two concepts. if this needs to be small, one maybe needs most of the gradient to go toward remembering the task? should we see much of what the transformer is doing internally as computing in a way such that it is easy to learn from a few updates? what would such computation look like? can we detect these parts easily from the gradient?

treeify a model, see how many paths are important on each input. is this randomlike? is this more concentrated than you’d expect? could do on the level of components or neurons or rib basis elements

could also try to cluster these branches?




another normalization that seems interesting btw if we don't try it already: projecting out the pseudolabel directions computed on each cluster for any data point!! a la LEACE

https://en.wikipedia.org/wiki/Latent_Dirichlet_allocation activation vecs as documents with like SAEs or other sparse readoffs as words or something???? probably makes no sense


is there a reward function and a set of resource/computational constraints such that 
(1) humans satisfy these constraints
(2) humans are optimal reward optimizers among all systems satisfying these constraints
(3) we'd be happy with the universe being tiled to max this reward
(4) it is the unique (or simplest) reward wrt which humans satisfy (2) (with this same set of constraints)

understand the safe compute multipliers, breaking tasks into subparts in a nice way and letting systems solve those, speeding up processes, having more sensors, things that can do iterated distillation and amplification with. of course capabilities-relevant. 

plausibly already done but understand how deep learning gets rid of suboptimal (well, superoptimal) local minima by showing that stacking more (intermediate?) layers causes previous local minima to become saddle points or not minima at all or something. seems relevant: http://proceedings.mlr.press/v108/kawaguchi20b/kawaguchi20b.pdf

a thought: plausibly, all possible word-level features are already there in the token embedding! because it can store just a huge amount of information there. eg about whether a word is a noun or a verb, whether it is the third word of a sentence, whether it is the first word of any album by cindy lauper, whether it is the last name of a nobel laureate (assuming single token), and so on, all in the embedding already. can learn how depends on scale of the model which token-level concepts can be probed from embeddings? tells us something about what things a model has come to understand about the world maybe. then in next layers can look at bigram concepts and so on? sth like a prediction from this: probing for concepts about single words never becomes better as one passes through the model
maybe nicer if try word-level tokenizer on tinystories for this: https://arxiv.org/pdf/2305.07759.pdf
maybe not enough data here though? hmm probably is. can we track how it learns all bi-gram n-gram etc facts about train data?
maybe look for features by looking for sets of words that are surprisingly separated in some direction from other words? into two classes? to look for binary properties the model is using? just look for directions where there are surprisingly large gaps? and these are the feature directions? ofc don't actually need the gap to be completely empty, but would be good to have it be mostly empty. maybe just a really bimodal distribution? can write down some loss for that i guess. seems bad as an optimization problem though i guess. one option would be to do logistic regression but with some effective upper bound on the linear coefficient 


sometimes circuit has component in layer $\ell$, then gap of a bunch of layers, then next component. maybe would be nice if could design an architecture where this never happens. maybe make some varying widths, e.g. start wider, to exactly avoid any gaps in computation paths. not sure how exactly

idea for task decomposition: look at the pattern of information flow through a model, especially in middle layers. same pattern => more likely that the task is the same

improvement on the logit lens droupout idea: just unembed in every layer, make loss sum of cross-entropy losses from all layers or whatever, maybe this makes not just logit lens better, but more interpretable in general. eg more important patterns done first in early layers, then less important patterns.

the human eye iris or whatever sex difference neural net thing (ie humans thought no difference, but neural net can classify well somehow) as a case study for microscope AI

try looking for word2vec concept structures in activations in general, see if find the right concepts — would be evidence that there is only one thing of a certain shape

to find nonlinear representations, take a toy task like modular arithmetic, train out reps needed for Neel's algo by adding a probing term for these to the loss, then interp again, repeat until not any linear features?
do it with toy models, require first layer not to be able to be read off, other layers are allowed, see what kind of reps get on the first layer

in toy models eg 2D with a large number of features: can we come up with a sequence of which inputs are seen when during training such that all features are learned, eg with one input being seen a bunch of times in a row to let it grow, with some cleverly chosen schedule for everything else at that time as well to restructure the circle to be roughly uniform (might need to see nearby things on circle more often than far things + might need either leaky-relu or elu or sth or to reparametrize bias to avoid vanishing gradients)

come up with an information-theoretic characterization of which large ideal weight matrices can be put in superposition (at which small sizes) (like setup here: https://transformer-circuits.pub/2023/may-update/index.html#weight-superposition ) without much loss + see experimentally if the metric checks out; maybe like https://transformer-circuits.pub/2023/may-update/index.html#simple-factorization but can't quite figure out the details. can we get the number of learned quanta out of this info theory characterization also? would be quite good not just for this, but also to understand the information theory <-> neural net connection better. should read the linear information paper


on tasks on which models do better, can we see that representations are more similar (better at predicting?) brain reps (this would be a neuroscience study)

fine-tune on tasks, check transfer to other tasks, e.g. va

For each single training update, see which tokens have their loss affected the most, use this to create quanta, in the sense of the quanta paper arxiv 2303.13506, or also use to understand what things are done by the same circuits i guess? this might just be a different phrasing of the same thing. Perhaps one can also use this to understand hierarchical quanta/concept formation a la Jan Kulveit's convergent abstractions. Look at which quanta need to form for a certain quantum to form — these are the prereq concepts needed for the next thing?
Can use GPT-4 to do token labeling to explain quanta
Hmm oops wrote this between section 4.2 and 4.3 — I guess 

# in chronological order, from earliest to latest?

-   **Few-shot learning** - When the prompt to a generative model contains several examples of a task, and the model generates text to answer a new example of the task. Eg prompting GPT-3 to do addition by giving it several correct addition problems beforehand.

-   Importantly, pre-trained models like GPT-3 can often use few-shot learning to achieve good performance on a variety of tasks, despite not being explicitly trained for them. It’s not clear how much it’s actually doing any “learning” vs just being cued to use its existing capabilities on the task at hand.

-> Create a mathematical formalism for differentiating between the model learning vs being cued to use existing capabilities. It might be that any training can be thought of as just being cued to use existing capabilities, but maybe there's more to be said here. Along similar lines, maybe we could develop get some subtle cool understanding of what kind of prompt engineering "gets legit capabilities out of the model" vs "tells the model the answer"


problem from Alex Gray: Figure out how to think of information loss thru deterministic gates (or ReLUs specifically). I haven't thought this through but he said (and it seems 98% right) that any canonical thing gives 0 or infty. Maybe this is useful: [file:///Users/kaarelh/Downloads/Geiger_Thesis.pdf](file:///Users/kaarelh/Downloads/Geiger_Thesis.pdf) . It would probably be nice to understand the information theory stuff about neural net depth anyway.  https://www.mdpi.com/1099-4300/18/11/410/htm

Develop a mechanistic understanding of how language models do modus ponens

train gpt2 with tokenizer respecting numbers, see how it adds, maybe use constraint search in the process

What's computation in superposition? What does that look like? Just train coupled models such that the smaller one is required to be the bigger one in superposition!! and make the bigger one sparse? REQUIRE SOME SQUARE TO COMMUTE
Like there's a map from one model to another. The bigger model just has one feature per neuron, but these are packed into smaller model like Anthropic's thing?? 

* probing on a layer = retraining top layer after that; e.g. I think sometimes people take some last layer of a model and retrain it – this is the same as training a probe on the last layer

Understand what conditions give rise to wrapper minds, i.e. when does an RL agent just learn a perfect reward model and take actions that max that.

https://arxiv.org/pdf/2212.01681.pdf Can this LM, as a whole, be conceptualized as an agent with communicative intent? Clearly not: from sample to sample it fails even to generate text according to a coherent belief about the state of the toy world. -> seems wrong because LM has outer knowledge that lets it simulate various agents?


We can train a supervised probe finding goal-representations of characters currently simulated by a language model, but I guess we can't do supervised probing finding goal-representations of the model itself (in certain situations), because we can't a priori have access to the labels, i.e. we don't know what the goals of the model are. However, for me, it internally feels like there is a strong relation between my goals and the goals of people I'm simulating in my head – I almost imagine myself becoming one such person. It feels like there is some relation between how I represent my own goals and how I represent the goals of someone I imagine simulating. If there is such a representational relation for language models, it would be great to figure it out, and then use it to figure out what it's own goals are, using only labeled data from simulations. (Counterargument: This relation exists for me because I'm particularly made to be an agent representing my own goals, so I'll frame similar stuff in terms of that; for an agent optimized for simulating other agents, the relation might be much weaker. But maybe there is an inverse relation, where everything part of individual agency is represented a lot like the respective parts of simulated agency are?)

However, to figure out the relation between the goals of a simulated agent and those of the model itself, we might need a different testing ground, where we can in fact tell what the labels on both sides are. Maybe DLK provides the missing half for truth-values. So we could study this relation for DLK, and then apply what we learned to goals.

Another idea is to do a simulation within a simulation, e.g. a character X dreaming of being Y, and see how the concepts of Y relate to the concepts of X, and see if we can extrapolate this relation to understand how the concepts of X relate to the concepts of the model.

Use supervised probing for truth (supervised = when training probe, get to match ground truth labels) on a LM to evaluate true capabilities? I'd guess someone has already done this training? E.g. just do this https://aclanthology.org/D19-1250.pdf except instead of zero-shot outputs, train a probe on some inner states? I doubt it generally does significantly better than zero-shot? If it worked, I'd guess people could use it for capabilities, oops? But I strongly doubt it would be better than fine-tuning on the particular dataset. But e.g. it might be interesting to test on TruthfulQA, https://arxiv.org/pdf/2109.07958.pdf, to see if it does much better than zero-shot there?


Try to get rid of polysemantic neurons by training mutliple models and requiring each neuron in a model to correspond to a neuron in another. The idea is that if there are weird polysemantic ones, I'd guess the same ones are unlikely to exist in another model, so these would maybe go away? One can do this iteratively a bunch of times.


Look into mechinterp literature to find out how high-level properties tend to be stored in model's representations. Are these usually linear, corresponding to directions, etc.?



Create an image dataset annotated with values of some huge number of features seeming natural to humans, from low-level things to high-level things. Train a model such that each neuron is required to capture at most one of these features. Like, just put in the loss that each neuron should capture at most one feature from the huge list. This could give interpretable models. The hard part is obviously coming up with the humongous list of features.

Studying how features with topologies different than those compatible with $\mathbb{R}$ could give cool examples of how features are represented. Will it still be linear in some ad hoc way, or will the feature naturally having a different shape mean it's also represented as not just a direction? This seems like a good test for whether features are linearly represented.

Take a mechinterp circuit that someone has figured out, write down constraints capturing the concept at each node in the circuit, see if searching the model for a concept satisfying these constraints returns the feature we started from?

in language models, is inference happening during inference? i.e. the deduction stuff with cats mammals animals from SPAR students


do something like logit lens but with general linear probe? or linear output matrix trained to do something else?

can we do PCA on activations at a position for a bunch of inputs and figure out what the PCA components correspond to? should maybe ask Joshua from EAG about this?

So we would like to say that concepts <-> directions, but this isn't quite true because sometimes multiple concepts live in the same dimension. Is there an automated way to tell if an activation in a direction is 

rep is linear combo of properties, how to generally decompose? 

do PCA on activations for one model, see if smaller model activation space can recover these features, use smaller model to interpret bigger one?

boxed causal decision theory misaligned AI would want to help us solve alignment if it just prefers world where we survive to world where META's next AI kills everyone? this working still additionally assumes some verification/generation imbalance

principle C head with mech interp 

the think wrote to Alexander about has to do with knowledge of other agents maybe, like uncertainty about utility functions should lead to more geometric optimization maybe? should thank Benjamin if this ends up working

take feature 

Take bidirectional model, use it to generate k sentences from a sentence with 1 word resampled iteratively. Then take diffs with average of k. Repeat for n sentences. Then do PCA on the nk vectors obtained. How interpretable are directions going to be?


https://www.lesswrong.com/posts/pZHpq6dBQzCZjjMgM/the-computational-anatomy-of-human-values
"Secondly, there is the reward model which associates concepts in the latent space of the world model with expected reward values. This is where some of the loading of valence to value concepts occurs. Importantly, the reward model can _generalize_ across closely related concepts in the latent space and does so in a systematic way. This is what leads to valence ‘bleeding’ across concepts due to pure associations. For instance, if I think concept A is highly positively valenced, then I will also assess concept B in this way even if it is logically independent so long as concept B is close in the latent space. It is this effect that generates the logic of highly correlated but logically independent political positions, and indeed the entire phenomena of ‘ethnic tension’ [described by Scott Alexander](https://slatestarcodex.com/2014/11/04/ethnic-tension-and-meaningless-arguments/) back in the ancient days of 2014[[11]](https://www.lesswrong.com/posts/pZHpq6dBQzCZjjMgM/the-computational-anatomy-of-human-values#fn0l2ik1obeld).""
Try to test this is LLMs. That is, pick 


rio: alignment between agents required to compose them into a higher-level agent 



It would be quite cool if replacing logit lens by tuned lens made this plot from [https://www.lesswrong.com/posts/mkbGjzxD8d8XqKHzA/the-singular-value-decompositions-of-transformer-weight](https://www.lesswrong.com/posts/mkbGjzxD8d8XqKHzA/the-singular-value-decompositions-of-transformer-weight "https://www.lesswrong.com/posts/mkbGjzxD8d8XqKHzA/the-singular-value-decompositions-of-transformer-weight") flatter/higher:
![[Pasted image 20230411154859.png]]
like if the reason the earlier layers are less interpretable is just that they are more out of tune with the output space

make NN generalize instead of memorize by requiring representations/computation to be similar on data points with the same label, instead of just requiring that outputs are the same?

train a map from brain activations to LLM intermediate layer activations (like invert this: https://www.nature.com/articles/s41562-022-01516-2), then put LLM on weed at inference time by adding the image of weed brain state along the lines of https://www.lesswrong.com/posts/5spBue2z2tw4JuDCx/steering-gpt-2-xl-by-adding-an-activation-vector ; this also raises the importance of finding a truth serum — the manhattan project might need an mkultra