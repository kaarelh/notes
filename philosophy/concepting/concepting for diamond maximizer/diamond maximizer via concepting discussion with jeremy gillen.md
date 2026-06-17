
* i'm still confused about where action model comes from actually. how do u think abt how much diamond some actions lead to. do condensation models support such queries?
* is each condensation a full 4d spacetime block? seems bad for planning
* condensation doesn't give you all these different condensations right? what would a theorem about all the different condensations even be? i guess the hope is just that these would be somewhat more friendly models of the world? but what's wrong with usual objectspeak?
* let's think through what we want from condensation
	* we want there to be things causing pixel-observations. we want to just say "the thing causing these pixel-observations" and have that be diamond.
	* of course there will be models with no such thing. there will be models with a wrong such thing. but maybe mostly there are good models?
* ok you can just have a program generating a picture and track which parts of the program were used when printing a pixel? i guess it's unclear what being used means? i guess you could have a big for loop and a library of functions and call some functions in the for loop? and then look at what functions are called? wait wtf that doesn't make sense because you always call the same functions tho... ok at least you could put some functions behind an if statement.


one issue with pointing at diamond via specifying observations the concept should be involved in producing: 
* there will be lots of other observations which diamonds are involved in producing, which you won’t mark

you can try to fix this by saying:
* ok but maybe the concept involved in most of the pixels you point at and the fewest other things is diamond

of course this fails if say “visible diamond” is a concept. still, there is a sense in which pointing at diamonds in videos should communicate diamondness to an alien. but it's unclear how to make a structure which supports that

this also just fails in many models

and we can’t go through the very many models manually lol

tho one could hope to have it work in models having most of the probability mass, maybe?



# [problems with]/[confusing/unresolved things about] the condensation-based diamond maximizer proposal

even assuming condensation does something good:
* even if condensation gives a diamondness property or a diamond notion or something, that doesn't mean that the condensation has a variable tracking the amount of diamond
	* you can hope to get the condensation, inspect it, and write a function that looks at the condensation and reads off the amount of diamond. this is somewhat like how: you could try to count all the places where a specific red square gets generated. note that there being a variable somewhere that knows what a red square is does not immediately give you a way to count red squares the condensation takes to exist. in fact, this counting seems difficult/cursed to me, especially with stuff like the XOR issue in mind. also if you want to operate with very many condensations at once, you have to automate the process of writing a function that counts diamond, and this is even more difficult/cursed
* we want a condensation that has a notion of diamond but not visible-diamond/diamond-on-the-surface/humans-consider-this-diamond/etc (because if these notions are there, your method for pointing at the diamond notion will instead point at these narrower things), and idk how to do that
	* in fact, i think it's going to be very hard to set hyperparameters such that this is true. even if condensation basically does something good, i think almost all hyperparam settings will have either no diamond notion or many of these notions. my current loosely held take is that the most promising angle is to intentionally go for some sort of world model that basically has answers to all possible reasonable questions (or has the ability to answer all possible questions) and somehow make things work with that
* there are probably also other major problems with binding diamond
	* thinking about this for a bit just now when writing this list, one thing that came to mind is that if you allow very many latents, then the smallest index set latent above all the diamond pixels will be some nonsense, but if you allow only few latents, that pushes other stuff together with the diamond notion. maybe there is an intermediate regime where diamond is nicely separate
	* outside view I expect there to be other problems but I won't think more about this now
* idk how to put a good prior on condensations. (if you put a bad prior, you can end up believing crazy things even after seeing a decent amount of data, and then acting really badly)
* idk what sort of thing a condensation needs to be for this proposal. (also idk what a condensation is like given the current mathematical formulation.) like, does it need to have native support for interventions, should it have built-in time, should it typically have an opinion about what the entire past (and future?) spacetime block is? would it be better for all the good models to live in one condensation, or would it be better for different good models (such as models at different scales) to live in different condensations?
	* if multiple condensations can be correct at once, then that affects how one should do planning (like i think the most immediate things one would write down are only "correct" when models are mutually exclusive)
* idk how to do planning given condensations. i'm in favor of first solving a version where you are not that embedded somehow, because that seems easier
* i'd want to have some clarity around how actions are inserted and how new data gets gathered (potentially i'm just asking for a nice convention — maybe there aren't major difficulties here)

my current high-level take on condensation:
* I think I mostly just "don't see what you're seeing", when you're optimistic about condensation. I think the correct default guess what happens if one writes down some predictive modeling architecture+loss is that what you get will be cursed like a program inside solomonoff induction or like any known ML model. We could try to get at some diamond notion inside a language model by finding a neuron whose activation is very correlated with the previous sentence talking about diamonds, or we could train a linear probe on activations for the prompt being about diamonds, or we could find SAE features whose coefficients are correlated with the prompt being about diamonds, or whatever. I expect you agree that these will be really silly. I feel like you need some strong reasons to think finding diamondness inside condensation will not be like that, and I'm not really even seeing moderate reasons to think that. Like, it just seems like an extremely wild claim that things work nicely! I don't understand what reasons you have to believe that condensation works or is close to working, instead of being cursed like every other thing that has ever been considered.
	* there are some theorems but they are weak — they are about very specific toy cases. much better theorems could make me optimistic
	* one can do some philosophical handwaving in favor of condensation i guess, but i think that's extremely far from being sufficiently compelling. also human concepts [are very different things]/[work very differently] imo
* I feel like condensation is an interesting trick to get a program or a latent variable model to "factor" somewhat, but it's very unlikely to be remotely sufficient to make it actually nice.
* I mostly believe that usually a smart/powerful enough mind in our universe will be able to pretty easily understand questions about diamonds. But it's a much taller order to write down a mind architecture such that this ability to understand is "pushed into a nice prespecified basis". Similarly, I think it's plausible that a condensation would in some sense know the answer to the question "how many diamonds are there in the universe?", but I think it's an entirely different and much much more difficult thing to have the answer be nicely written somewhere from where it can be easily read off.
# questions to ask jeremy

* what reasons do you have to think condensation works? even in your toy examples? i feel like it's just some trick for getting a program to factor somewhat, and it's just very unlikely to be nice?
	* there are some theorems but they are weak — they are about very specific toy cases. much better theorems could make me optimistic
	* one can do some philosophical handwaving in favor of condensation i guess, but i think that's extremely far from being sufficiently compelling. also human concepts [are very different things]/[work very differently] imo
* in your system where one needs to provide arguments that modifications are fine:
	* if the arguments are non-defeasible, that makes your system really shit at getting stuff done (you can't accept things well enough, you don't get anywhere)
	* if the arguments are defeasible, then you have to have some trust for the part of the system that presents arguments. that seems really hard to have, and it's not guaranteed by the argument loop? 
# references

SAT solver: https://d-krupke.github.io/cpsat-primer/07_under_the_hood.html