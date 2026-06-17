
I'll be assuming all random variables below are defined on a common sample space and discrete, with a random variable X taking values denoted x_1,...,x_n.

Sometimes it's good to split the distribution of a random variable X into parts in an additive way, where the different parts are called "hypotheses". We can think of the hypotheses as giving a partition of sample space, or equivalently we can consider a discrete random variable H which specifies the true hypothesis. (To have an example in mind while reading this, think of X as the outcome of flipping a coin the second time, and H as the bias of the coin, which let's say is i/4 for 0<=i<=4 with the uniform prior.)

This partition looks like P(X=x_i) = \sum_{j=1}^n P(H=h_j) P(X=x_i | H=h_j). (Vectorizing this, you get rid of the subscript i on both sides, and you can see this as expressing the distribution of X as a linear combination of the conditional distributions of X given values of H.)

According to the vanilla Bayes' rule, upon seeing evidence E (which is an event; for our example, think of it as "the coin landed heads on the first toss"), the new distribution of X is given by P(X=x_i | E) = P(X=x_i and E)/p(E) = P(X=x_i)*P(E | X=x_i)/P(E). In other words, the update is to multiply probabilities by the likelihood P(E | X=x_i) and renormalize.

However, we can split the update formula according to hypotheses as well. P(X=x_i | E) = \sum_{j=1}^n P(H=h_j | E) P(X=x_i | H=h_j and E). We can apply Bayes' rule to give P(H=h_j | E) = P(H=h_j)*P(E | H=h_j)/P(E). The nice case here is if P(X=x_i | H=h_j and E) = P(X=x_i | H=h_j), i.e. the hypotheses H = h_j "screen off" the evidence E. (This is true for our running example.) In this case, the formula becomes 

P(X=x_i | E) = \left( \sum_{j=1}^n P(H=h_j)*P(E | H=h_j) P(X=x_i | H=h_j)\right)/P(E). This is the formula that makes Bayes' rule look like it's just about updating the probabilities on hypotheses.



The above story also applies if X is replaced with an event. An event is just a random variable that takes two values. (And a random variable is a collection of events, one for each value – so one can easily derive either variant from the other.)