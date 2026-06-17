

# the practical case

* you will have some program with some compute constraint
	* maybe it's like a turing machine with a runtime cutoff?
* i guess you will somehow find programs that do well on your given sentences
* how will the labeled sentences and labels be obtained?
	* maybe you have a human sit in a room, come up with some sentences they are really sure about, and label those
	* what sentences might appear here? some examples:
		* proven mathematical statements (formal or informal)
		* "the eiffel tower is in paris"
		* "gravitational acceleration close to earth's surface is about 10 m/s^2"

# toy cases

* if you give human-proven and human-disproven mathematical statements with their truth values, and do something like function induction, then it seems plausible that you get good generalization? 



# a point to make to yoshua about the standard the solution should meet

* even if you think your strategy plausibly works, it is much hard to get it to meet the worst-case standard of the ELK report
	* "We think that worst-case ELK — i.e. the problem of devising a training strategy to get an AI to report what it knows no matter how SGD shapes its mind internally"
	* "Perhaps a reporter that correctly answers questions in the colored part of the space generalizes to honestly answering in the grey part of the space. This seems prima facie plausible to us: the prediction model already has to build up an understanding of the situation to make predictions, and the most natural way to answer questions may be to directly translate its understanding into human language."



# messages to matt

btw i think yoshua was probably dismissing a real issue somewhat unfairly when he said "we don't have to care about independent statements". the problem is: assuming our hypotheses are computable (ie, each hypothesis is given by a turing machine which outputs something given any statement as its input), there is no hypothesis which assigns 1 to each provable statement and 0 to each disprovable statement. (if the hypotheses are assigning probabilities, then: there is no hypothesis which assigns >1/2 to each provable statement and <1/2 to each disprovable statement.) and so not only is truth a cursed "infinitely complex" thing, but distinguishing provables from disprovables is also a cursed "infinitely complex" thing

that said, if you make a data set by giving 1000 formal math statements humans have proved the label 1 and 1000 disproven statements the label 0 and then find the shortest program with this input-output behavior, it seems pretty likely that this program will be assigning 1 to all provables and 0 to all disprovables (and not halting on some independents)

matt: Sorry I'm confused, you said such a program doesn't exist, but this message seems to say you think we can easily get it, what am I missing?

the difference between the two messages is that in the first one, we require that a program assigns labels to all sentences

whereas in the second one, we are taking the shortest program that assigns correct labels to the given data set

one fairly short program which assigns correct labels to the data set is: check all strings in order for being a proof/disproof of the given sentence. output 1 when you find a proof; output 0 when you find a disproof

this program isn’t going to assign anything to independent sentences, so it couldn’t be among the hypotheses considered in the first message

(and there is a theorem saying that there is no way to extend this good assignment to a full computable hypothesis — that is, the thm says that there’s no program that assigns something to any sentence and gets the provables and disprovables right)

(if you’re interested: one can show that this claim is equivalent to the unsolvability of the consistent guessing problem; you can read about that problem here: https://scottaaronson.blog/?p=710 )
