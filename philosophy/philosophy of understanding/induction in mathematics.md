* a nice specific case: you have some binary property of a natural number $n$, denoted $P(n)$, which is easy to compute for any specific n
	* eg: P(n) is whether n is the sum of at most three primes, or whether n is the sum of at most four squares, or whether the prime factors of n sum to less than n, or whatever
* you note that P(n) is true of all small $n$ you've checked
* do you conclude that P(n) is always true? is it fine to conclude it? can we say something rigorous about this?
* of course you will get some stuff wrong, eg if P(n) is whether the inverse ackermann function is below 100 (this will be true up to some vast n, and then false)
* maybe one can at least well-conclude that P(n+1) is probably true?
	* of course one can always construct an adversarial property, eg whether the number is strictly below n+1
	* but say one goes in with a commitment to check to some random n and then conclude for n+1 (so also a random index)
		* in this case one gets a failure, ie a wrong inference, iff the statement is true up to n and then false. having fixed P, there is at most a unique such n, so the probability of this is at most the max over n of the stopping probability at n, which we can make arbitrarily small! eg you can have a uniform distribution from 1 to 1000 and then it's at most 1/1000.
		* so the event [the next guy after satisfies P] gets an arbitrary odds boost (eg 1000x in the example above) from this process! that's kinda nice already

# a thought on justifying induction in mathematics

one idea is that an inductive inference is justified by pointing at a big class of which that inference is one example, and arguing that most inference in this class are correct. or maybe 99% are correct and 1% are wrong, so we should think our conclusion has 1% probability of being wrong if it is legitimate to think of it as generic in the class. my guess is that one can in principle always cook up classes in an adversarial fashion which let you convince me of any falsehood this way. however, maybe this mostly goes away once one starts to prefer simpler classes? 