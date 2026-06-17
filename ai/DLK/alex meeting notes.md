

utility thing needs variance term to avoid trivial solutions, also want to send thru sigmoid (only look at features like that) to avoid it blowing up

framework seems good

in AGI level model, can maybe get its own probabilities using DLK and then search for utilities

have policy network RL agent, put position and next, these give contrast pair, find value, ask Walter about whether this is feasible 
to avoid trivial solution, do DLK confidence, or put in variance, or do a little bit of supervision
AGI limit have it play in simulation against itself??

image classifier supervised leaf, can we come up with some construction for unsupervised thing to look for
or can we use supervised probing to combine concepts?

constant output




Discuss syntax tree idea?
mention issue with EV of any random variable satisfying utility thing

probabilities of final outcomes in multi-stage process

calories of food represented internally, like give combo meals with multiple things and see if calories sum


use transformer attention pattern for merging clusters, see if get syntax tree

in p=max_i (1-p_i) put in variance term to avoid all 0.5
change coeff of variance term to get good calibration
competing influence from variance pushing to extremize and errors created by this for boundary cases pushing to keep close to boundary

generalization of direction to any linear transformation of image, e.g. rescale horizontal and vertical by something and recover scaling factor from inside, seems nice, or do translations? might have problems, or shear
projection of direction into camera plane
translations 


Feb 7:
linguistics stuff
https://en.wikipedia.org/wiki/Dependency_grammar
require tree ultrametric thing? require similar embedding upon reshuffling words? try reshuffling words into phrases? does this have a high chance of changing the syntax tree? maybe better with phrases at the end of sentences?


thing with RL searching over next states, any issues and how to solve. can we come up with a good setting where issues are minimal?
any hope for detecting search more generally?

issue with variance constraints, have something with range, have some supervised thing? fraction of moves close to the max is low, measured multiplicatively but multiplied by max? maybe pacman better than chess here?


physics simulator Noether's theorem stuff

ambiguous parse tree rare
probability distribution in model doesn't fit in R^n

conserved quantities in physics models by looking for stuff conserved under time evolution but not under different initial conditions

train sequence of probes finding conserved quantities in physics model, require being uncorrelated
or one probe with three heads that are uncorrelated
physics simulation interpretability work?
get pre-existing physics simulator?

how to do thing with variance
loss func invariant over rescaling
maybe 

look for RL agent with open-source weights with just policy network, e.g. for playing chess 

multiple choice questions with

recommend to students at SPAR, 

try multiple choice without confidence term, 

reference frame changes should change quantity how one would predict 

multiple choice questions best for 

purely relational language
category of sets have products
nth power preserve product category 


I've been thinking about experiments to run to check whether it reps truth vs what humans think / what's said in the training data. Maybe make a small toy domain of math questions where there is one thing consistently answered incorrectly by humans, but which is by some general rule implied to be true, and see if the outputs are wrong but inner rep is true?



