
philosophical version of the problem:
1) let's say we have a data set of the following form:
	1) question (asked as a person in 1900 would). textbook explaining everything that's needed to answer the question to a guy from 1900
		1) the question could eg be "how do we cure cancer?" or "how do we make a machine which performs calculations for us?"
		2) we might also want to write date-dependent textbooks maybe. so you could have the date as an extra parameter in the input
2) question: given a math oracle, can we use such a data set to get actually-good textbooks answering questions which are not in the data set?
	1) presumably something starts working here at some amount of data. but how much data is needed?

two approaches:
1) kolmogorov/solomonoff, or some time-bounded version. that is, we "train" a generative model. more specifically, we could take the smallest TM that sends the given inputs to the outputs, and ask if it also produces good textbooks on unseen inputs. maybe a good framing for this case is to think of us having a property in mind, namely the textbook being actually good, and ask when the generative model starts to only produce outputs with this property. the property could itself be computable, with some smallest TM
2) train a good-textbook-classifier somehow, and then just generate the alphabetically first thing this classifier maps to 1. the obvious question here is how one is supposed to get negative examples. 

tentatively: the generative model case makes more sense
can we say something about what happens for generic properties P? maybe let's consider a simple (probably friendly) case first where the textbooks in train data are obtained by taking a uniformly random textbook from all those with the property P (ie from all good textbooks answering the given question). now there is one generative hypothesis that looks like: specify the set with the property P (ie give a function that takes in a question and outputs the set of all textbooks of up to some length answering that question), then put a pointer inside this set. what's the complexity of this generative thing? i guess we need to spend complexity(P) + num-train-data-pts times the avg of log (size(P)) over questions in train data