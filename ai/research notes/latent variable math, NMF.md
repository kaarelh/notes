
thing where natural abstraction is thing on which you condition to make other stuff independent

is it this? https://en.wikipedia.org/wiki/Non-negative_matrix_factorization

https://psu-psychology.github.io/psy-597-sem-sp2019/04_latent_variables_estimation/latent_variables.html

tensor decomposition into ones that are products of vectors


https://mlg.eng.cam.ac.uk/zoubin/course05/lect2m.pdf
https://psu-psychology.github.io/psy-597-sem-sp2019/04_latent_variables_estimation/latent_variables.html
https://home.ttic.edu/~ryotat/papers/TakTomIshKimSaw13.pdf

from https://www.lesswrong.com/posts/s4FNjvrJG6zmYdBuG/axrp-episode-9-finite-factored-sets-with-scott-garrabrant :

**Daniel Filan:** In what ways would you say it’s a theory of conceptual inference?

**Scott Garrabrant:** Well, one way to look at the diff between factored sets and Pearl is that we’re kind of not starting from a world factored into variables instead we’re inferring the variables ourselves. And so there’s a sense in which if you try to do Pearlian style analysis on a collection of variables, but you messed it up, and instead of having a variable for what number this… I have a number and it’s either zero or one and it’s also either blue or green. And I can also invent this concept called grue, which is a green zero or a blue one. And instead of thinking in terms of what’s the number and is it blue, you can think of what’s the number and is it grue, and maybe if you’re working in the latter framework, you’re kind of using the wrong concepts and you will not be able to pull out all the useful stuff you’d be able to if you were using the right concepts.

**Scott Garrabrant:** And factored sets kind of has a proof of concept towards being able to distinguish between blue and grue here, where the point is, in this situation, if the number is kind of independent of the color and you’re working with the concept of number and the concept of grue-ness, you have this weird thing where it looks there’s a connection between number and grue-ness, but it also is the case that if I invent the concept of number [xor](https://en.wikipedia.org/wiki/Exclusive_or) grue-ness, I kind of invent color, and color lets me factor the situation more and see that maybe you should think of it as the number and the color are primitive properties like we were saying before, and grue-ness is a derived property.

**Scott Garrabrant:** And so there’s a sense in which earlier things are more primitive, and it’s not just earlier things, I think there was more than just that. But there’s a sense in which because I’m not taking my variables or my concepts as given, I am also doing some inferring which concepts are good.

**Daniel Filan:** So somehow it strikes me that inferring which concepts are good, is a related, but different problem to inferring which concepts a system is using.

**Scott Garrabrant:** I don’t know, there’s stuff that you like to think about that involve kind of having separate neurons as part of it. And I think there’s a sense in which it might be that we’re confused when we’re looking at a neural net because we’re thinking of the neurons as more independent things, when really they could be a transform similar to the blue/grue thing from some other thing that is actually happening and being able to have objective notions of what’s going on there - being able to have a computation and having there be a preferred basis that causes things to be able to factor more or something feels… Yeah, so I guess I’m concretely pointing at the picture of factorization into neurons in the result of a learned system might be similar to grue.

**Daniel Filan:** Yeah, it’s interesting in that people have definitely thought about this problem, but all the work on it seems kind of hacky to me. So for instance, so I know Chris Olah and collaborators now or formerly at OpenAI, have done a lot of stuff on using non-negative matrix factorization to kind of get out the linear combinations of neurons that they think are important. And the reason they use non-negative matrix factorization, as far as, I might be getting this wrong, but as far as I can tell it’s because it kind of gets good results sort of, rather than a theory of non-negativity or something.

**Daniel Filan:** Or a similar thing is there’s [some](https://arxiv.org/abs/1312.6199) [work](https://arxiv.org/abs/1704.05796) about exactly trying to figure out whether the concepts in neural networks are on the neurons or whether they’re these linear combinations of neurons, but the way they do it, which again, I’m going to sound critical here. It’s a good first pass, but a lot of this work is, okay, we’re going to make a list of all of the concepts. And now we’re going to test if a neuron has one of the concepts which I’ve decided really exists, and we’re going to check random combinations of neurons and see if they have concepts, which I’ve decided exist and which does better.

**Daniel Filan:** Yeah. There’s definitely something unsatisfying about this. Maybe I’m not aware of more satisfying work. Yeah. It does seem there’s some problem there.

**Scott Garrabrant:** And again, I think that you’re not going to be directly applying the kind of math that I’m doing, but it feels I kind of have a proof of concept for how one might be able to think of blueness as a statistical property, blueness versus grue-ness as a statistical property. It’s something that you can kind of get from raw data.

**Scott Garrabrant:** And I don’t know, I feel there’s a lot of hope in something that. But that’s also not my main motivation. That was a side effect of trying to do the embedded agency stuff. But it’s kind of not a side effect because I think that the fact that I’m trying to do a bunch of embedded agency stuff and then I… I was trying to figure out stuff related to time and related to decision theory and agents modeling themselves and each other. And I feel like I stumbled into something that might be useful for identifying good concepts, like blue.

**Scott Garrabrant:** And I think that that stumbling is part of the motivation. I don’t know, that stumbling is part of the reason why I’m thinking so abstractly. That’s not a motivation for thinking about embedded agency. That’s a motivation for thinking as abstractly as I am, because you might get far reaching consequences out of the abstraction.