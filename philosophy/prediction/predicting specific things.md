
understanding is importantly not just about prediction. also, to the extent that it is, i think it's more about predicting certain high-level invented things, and less about predicting raw data. for example, you might predict what is written on a sign. you might predict the words, you might predict the meaning of the sentence. you might predict what type of cloud there will be tomorrow, or whether it will rain. yes yes, one can see these as helping with pixel predictions. i think this is probably a mistake (but discussing this further is outside the scope of the note). anyway, if this specific thing prediction view is right, this prompts the question: where do these specific invented things come from? there might be a primordial place they come from that is very tied to sense data, and then a different loop. potentially this can all be understood as understanding developing, representation developing, from some primordial pure visual thing. it would be cool to be able to write down an ML problem that comes up with the idea that rain is a thing, that rain is an interesting thing to predict. some thoughts on type signatures:
* for each property, there could be a verifier. or in some broader sense there could be a question. you predict the answer to that question
* new properties are added when they help answer question.

# the song example

when listening to a song, you needn't be predicting anything. but if we want to think of you understanding/parsing the song as involving something like predicting it, i think we should think of you as predicting the following things:
* the rhythm/beats. eg consider the dancing bird from here https://youtu.be/0ZYhyewNQMo
* the pitch over time. eg think of the singing dog from here https://youtu.be/0ZYhyewNQMo
* the notes
* which instruments are playing
* chords
* what is played by each instrument
* the timbre
* the lyrics. what's the next word? what's the next letter? 
ok i think we needn't think of this in terms of prediction. maybe it's more like: what questions do you get answers to when listening

# a math example
see polya m&pr page 66 for an example in math where one tries to understand a sequence of numbers and as an intermediate step notes a regularity

# criteria on verifiers
maybe we should ultimately think in terms of questions, but maybe let's do verifiers for now. could we specify a process by which verifiers are to be obtained? one option would be to write down some loss on a collection of verifiers. these verifiers could then be a tuple of neural nets trained with that loss. a specific case would be to just write down a single-verifier loss, and maybe to try to study different local optima of that loss or something so as to not always just get the same thing? or perhaps we should have some iterative process where we have a first representation in terms of some first verifiers, and new verifiers can get added to these, with the old verifiers being involved in specifying criteria on the new verifier. first verifiers could be obtained by some low-level analysis of colored regions, like done in mumford's pattern theory, maybe? or maybe this should be emergent... could we make some ML thing which gives a decomposition into regions? maybe use the idea of starting from a point and predicting some property will stay about the same? primordial regions could be domains of success of sameness predictors? can just do this for colors i guess, but this wouldn't work well for some "textures", so maybe want to allow more sophisticated properties

anyway some ideas for criteria on verifiers:
* not that correlatedness? otoh maybe we want implications between properties, and A=>B requires correlation
* ability to read off redundantly? stability over time? over space also?
* showing up many times? 
* simplicity
# decomposing song into... notes? and image into regions, video into spacetime blobs

maybe a note is a sequence for which you can well-predict? hmm what if you skip half a period lol. probably don't much hear that? more like time of constancy of a certain variable (the pitch?). but where does this variable come from still? 

we have literal physical verifiers of a certain kind in our ears. like each part of the cochlear wall (if i recall the name correctly) has a certain resonant frequency, activates nerve if there is that component in the sound. how did that arise? what criterion do those satisfy?

it would complicate things quite a bit if we got pitch from recognition of things. like if we didn’t discern phase shift between frequencies basically just because it does not help distinguish things because different frequencies have slightly different velocities anyway. in that case maybe we need to have agents coping with our full world in mind even just when understanding how one should view a song. like perhaps one wants to start from physical things in that case and then explain pitch. the criterion would be that the representation should help you figure out answers to questions you could already ask

# video game agent example?
if we think agency is crucial to have in the picture, then perhaps we should be designing a video game agent. then we can eg ask that the verifiers somehow sparsely support action, maybe? like, making a sandwich is enabled by having bread and cheese in front of you?

btw i think the way items/things are programmed to work in minecraft might be somewhat close to how we think of things natively. like there are things (blocks, other items, basically stuff you can put in your inventory). there are specific things you can do with each of them. you can combine them to make other things — i guess in minecraft this comes in two flavors: crafting and building. as you play minecraft, you learn these rules attached to the objects.

i do think that real-world concept-gaining is very tied to learning that you can do something cool with these. you have the notion of nails and hammers because someone showed you that you can attach things to each other by inserting NAILS with a HAMMER. this activity succeeding with NAILS and HAMMERS then serves as a central criterion on what should be considered a nail and a hammer (maybe a good example: you can't make a hollow chocolate hammer, but you can make a hollow chocolate sculpture)

then later you can learn about more things you can do with a hammer, and these modify your hammer concept.

# primordial regions of an image from basic texture stuff

one idea for getting a first decomposition of an image into regions is to try to get at basic textures. one idea for that is to take a convnet with randomly initialized filters, run it on all local patches of a certain size, and look at the regions where the output value stays const?? or to do this with a convnet trained to classify images maybe?