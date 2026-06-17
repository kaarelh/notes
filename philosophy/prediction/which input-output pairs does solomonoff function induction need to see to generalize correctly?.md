
* there is a secret function f
* you are given its value on some inputs x
* you have to guess its value on other inputs

practical case of interest: you have a human giving outputs on some inputs, eg to scientific questions after thinking for 3 months. you want to know which inputs you need to get data on to get good generalization. eg giving a random string as the "question" is probably very stupid.  

> Proposition. for the purposes of this statement, let's say f has been learned by a predictor when on every input the output of f is more probable than every other output. you can always learn f by showing the function value on K(f) inputs (like, if you choose well). (here, K(f) denotes the kolmogorov complexity of the shortest program computing f)

Proof. suppose f(x) is not the unique top guess on x. then show f(x). note that since f(x) wasn't the top guess, this conditioning raises the probability of f by at least a factor of 2. if given the new posterior you can find another such input, then repeat. since the probability of f starts out at at least 2^{-K(f)}, this can't happen more than $K(f)$ times. at that point, f has been learned by the predictor!


