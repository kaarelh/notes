
we have a true stochastic function f: X -> Y (ie for each value x in X, a probability distribution on Y) with a measure on the domain, say with discrete domain and codomain, and a bunch of candidate models g : X -> Y which are also stochastic functions
(could also replace f with a distribution on X\times Y — this is equivalent data modulo some measure 0 thing which won't matter in this case)

Thm. in the limit as there are many independent samples from f (ie by picking x from the measure on the domain and then y from the distribution given by f on that x, almost surely the max likelihood model will induce the lowest KL div distribution on (x,y)

pf: by LLN, log likelihood given to the data by a model g div by n converges to sum_x mu(x) sum_y f_prob(y|x) log g_prob(y|x) = sum_{x,y} f_prob(x,y) log g_prob(x,y)/mu(x) = sum_{x,y} f_prob(x,y) log g_prob(x,y) - sum_{x,y} f_prob(x,y) log mu(x) = - D_KL (f,g) - H(f)-sum_{x,y} f_prob(x,y) log mu(x). since this convergence happens a s for all finitely many g at once, a s one lowest KL div model ends up being the one giving highest likelihood to the data 



https://benlansdell.github.io/statistics/likelihood/#:~:text=Thus%20in%20the%20discrete%20case,to%20minimizing%20the%20KL%20divergence.&text=which%20is%20typically%20found%20by,distribution%20and%20the%20parametric%20model.