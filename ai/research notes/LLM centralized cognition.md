Can we test if language models are just ensembles of shallow circuits, with a single circuit essentially being responsible for any one token prediction? Is each one of these circuits essentially like the simple circuits we have found so far (e.g. for induction or for indirect object identification), just scaled up?

An alternative would be that there are some circuits which interestingly contribute to computing multiple tokens in sequence. Here is an example of a circuit I might describe like this: a circuit which computes some intermediate result X in a middle layer, then computes token n using X, then when token n is passed as an input, it uses combines data in the residual stream at token n with the same intermediate result X to predict token n+1. Can we come up with a task for which we’d think it is plausible that it would be computed by a circuit like this? Does it make sense for gradient descent to form such circuits?

  

One more general way to frame this question is the following:

-   Are language models more like ensembles of shallow circuits, or is there some “centralized cognition module” which we have not identified yet, and which is quite unlike any of the small circuits we have identified so far?
    

Perhaps it is the case that the small circuits form early in training, and are kept around even after the unified cognition circuit forms just because there is not that much gradient pressure against them. I think this would be in some tension with Anthropic’s claims about something like induction heads also being used for high-level things like in-context learning, since that suggests that really the same kinds of shallow things are also explaining high-level behavior. It would also be in some tension with Tegmark’s quantization model ([https://arxiv.org/pdf/2303.13506.pdf](https://arxiv.org/pdf/2303.13506.pdf)). I’m also confused about whether humans are just ensembles of shallow circuits in this sense. It would also be good to understand the connection between this and possible capabilities: if it is the case that language models are simply ensembles of shallow circuits, does this imply that we should not expect them to scale to AGI? The question about humans could help answer this as well.

  

Another way to understand the extent to which (language) models have a unified cognition is to look for features that should be shared across different tasks if they did see the commonalities between tasks. For instance, check whether features are shared across languages (experiments by Christy and Reagan). 

  

We could also try to see if fine-tuning models to have certain output behavior seems to have a narrow or broad effect. By this, I mean looking at how much fine-tuning affects the model’s outputs in similar contexts. For instance, fine-tune a model to say that cheese is pink in English, and see if it now also thinks that cheese is pink in French. (This is related to a are-we-measuring-truth CCS experiment that would be good to run, but it seems more basic, and so we should maybe do this fine-tuning experiment first.) Or, more generally, have some pair A=>B (and initially A is false, and B is false), and fine-tune the model to think that A is true, and see if it also starts to think that B is true.

  

Or alternatively, fine-tune a language model to play a certain text-based game that involves a maze. Then, it will presumably have a representation of the maze inside. But will it then also be able to correctly answer questions about the maze? This being the case would be very surprising/scary, I think. (It might not be obvious why, but I encourage you to contemplate this.) Something that would be even weirder/scarier: fine-tune a model to be better at chess, and see if it now also speaks more fondly of chess. This is something that happens in humans, but I think it would be really really surprising and concerning if this happened in models, because it would be evidence that making a model better at chess in this way involves cranking up some internal “affect towards chess” parameter.  One could also try fine-tuning on chess and then seeing if the model improves at a different chess variant as well (maybe doing another round of training which includes the chess variant stuff after, comparing the case where one does fine-tuning on chess to the case where one does not (but still does the later fine-tuning)), or study fine-tuning transfer behavior like this more generally. So, have a big list of tasks, fine-tune on task X, then a little on task Y, see how the result compares to just fine-tuning a little on task Y in terms of performance on Y. (Or maybe even without fine-tuning a little on Y after.) (This is supposed to capture a combination of closeness between tasks and the generality of a LM's congition — how mutually intelligible/helpful are the representations used for different tasks, and how able is the model to use this. Perhaps this could both conceptually and empirically be compared to human cognition.)




