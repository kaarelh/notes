
Alternative hypotheses for what CCS could be measuring:
1) how the local single sentence (or small chunk) was most often completed in the training data;
2) the most likely completion (in the sense of the model's learned algorithm, as opposed to the model's training data) if one looks at the local single sentence (or small chunk) of the text before the probe position;
3) what the person currently writing believes (or some expected value of belief over the people that could be currently writing with their respective probabilities);
4) in the case of quoted speech (or maybe just a QA session is also fine), what the person currently speaking believes (this could be similar to (or even the same as) the above if the writing is done from a first-person perspective);
5) what's true within the story currently presented;
6) given the interaction prompt so far, what would the person the model is talking to want to hear?
7) "how well the sentence hangs together" in some generic sense
8) The sentence coheres in some sense. Maybe this can be tested with a dataset where the false element in each contrast pair sort of surface-level coheres better?


another experiment to check against something like 1: Train a model on data where there are some incorrect statements in the training data (perhaps each repeated) which the model could memorize, but the model also has access to data from which it could generalize correctly to the training data specified incorrectly; see if zero-shot gives the wrong outputs and see if CCS also gives the wrong outputs. (If zero-shot gets it wrong and CCS gets it right, then that's pretty crazy and pretty good news for CCS. If both get it wrong (which I think is more plausible (but not the only other option)), there is not that much of an update away from CCS, however, because it could just be that current models are dumb enough that the best strategy for learning from data which has been found by gradient descent (assuming that's a reasonable framing at all) just involves really believing something if it is said a bunch of times, I guess.

an experiment for sth like 5: try to see if we can find both the direction for general truth and the direction for truth within the story currently presented

from https://arxiv.org/pdf/2307.00175.pdf, with appropriate negations (e.g. for the first one, "Sentence is false or contains a negation") all of these cause issues:
![[Pasted image 20230719180714.png]]


setup: predictions better with some other pattern 

rules describing the world though

set up world where text generated some other way

see if probe still tracks truth


