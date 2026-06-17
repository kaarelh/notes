

Yea I guess a central issue is that if you fail to give dense data for any structure in the brain, then the structure "looks deep" to the ML algorithm you're using, and then it is probably not going to be "learned properly". And then your system isn't going to think well if you get it from pretraining on the intermediate states you have (ie it is not going to solve problems well). And if you also train your system on solving problems, then maybe it will start to solve problems, but it will now be using some different structures than the ones you failed to give proper intermediate data for

One could play around with this in the context of learning a good game engine, ie like https://gamengen.github.io/

Instead of just predicting the next frame from the previous frame and player inputs, you could give it some further data and see when it starts to actually learn the game engine pretty correctly (instead of being the imo cursed mess they get which lacks a good implementation of any game mechanic). Like, does it work if I give the full "computational state" of my laptop when I'm playing doom, and get the NN to predict the next state from the previous one and my inputs? Does it work if I give a noisy version of that, eg averaging each pair of nearby "computational variables"? What if I give half of the full state? What if I “drop the place where one particular game mechanic is implemented” (I don’t actually know how to make this make sense)?

(An MRI is sort of like these things, except much further from the nice low-level thing than this.)

... some voice msgs from samuel ...

So, I don't have a completely precise definition of a computational structure "looking deep" to the learning algorithm, but roughly, I mean that the data it is trying to infer the structure from "does not contain" the intermediate variables of a circuit, so it needs to infer a deep circuit from its inputs and outputs. Here is an example:
* Say we have a cellular automaton that we would like to "learn", e.g. https://en.wikipedia.org/wiki/Conway%27s_Game_of_Life , e.g. with a program implemented inside calculating something interesting (the cellular automaton corresponds to the human in our actual story). Now if you have a data set of pairs (board state at time t, board state at time t+1), then your job is relatively easy — you can eg just train a single-hidden-layer fully-connected network on these pairs and it learns the right board update rule (given enough data). But if you only have access to computational states at times 0, 10^6, 2*10^6, ..., then the computation "looks deep" given your data, and if you try to use ML techniques to learn the 10^6-step update rule, you will get some broken shallow crap that doesn't compute well instead of getting the actual structure.

You will also get some crap if your states instead show time averages over the last 10^6 steps. One can also ask questions about what happens if we are given data about space averages, and what happens if some region of the board has been left out of the state. These are all things happening with the MRI.

My guess is that an MRI is really far from probing "densely enough" for ML to "find most of the structures correctly", but I'd like to have a better quantitative sense of these things. It's probably sometimes fine to replace a deep structure with something more shallow?

a more "philosophical" example of the deep vs shallow distinction:
* Kepler's laws are "in" a video of the sky in a deep way, but in the numerical data Kepler was looking at in a much more shallow way

I guess depth isn't really all there is to this example or the human brain case, because we'd also like to say that space averaging makes things harder for ML — maybe we should instead call this general thing the structure being seen "messily" vs "neatly", with "deep" vs "shallow" being a special case


to add to the doom (video game) example, here are some more fun examples of how next frame prediction models do not have any "mechanism" implemented correctly: https://youtu.be/Y5GYqeCCu5Y
