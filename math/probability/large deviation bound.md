

https://en.wikipedia.org/wiki/Cram%C3%A9r%27s_theorem_(large_deviations)

> Def. The logarithmic moment generating function of a random variable $X$ is $$\Lambda(t) = \log \mathbb{E}[e^{tX}].$$

> Def. The Legendre transform of a function $f\colon \mathbb{R}\to \mathbb{R}$ is $$f^*(x)=\sup_{t\in \mathbb{R}}(xt-f(t)).$$

> Cramér's thm. Suppose $X_1,X_2,\ldots$ is an iid sequence with finite logarithmic moment generating function, i.e., the expectation in $\Lambda(t)$ above exists for all $t\in\mathbb{R}$. Then $$\lim_{n\to \infty} \frac{1}{n}\log \left(\mathbb{P}\left(\sum_{i=1}^n X_i\geq nx\right)\right)=-\Lambda^*(x).$$

equivalent alternative statement obtained by exponentiating both sides:

> Cramér's thm. Suppose $X_1,X_2,\ldots$ is an iid sequence with finite logarithmic moment generating function, i.e., the expectation in $\Lambda(t)$ above exists for all $t\in\mathbb{R}$. Then $$\lim_{n\to \infty} \left(\mathbb{P}\left(\sum_{i=1}^n X_i\geq nx\right)\right)^{1/n}=e^{-\Lambda^*(x)}.$$


Of course, we really want to have something for finite $n$. But then we can just say that for every $\varepsilon>0$, there is an $n_0$ such that for all $n>n_0$, 
$$\left\lvert\left(\mathbb{P}\left(\sum_{i=1}^n X_i\geq nx\right)\right)^{1/n}-e^{-\Lambda^*(x)}\right\rvert\leq \varepsilon.$$
If we just care about an upper bound, we can also say

$$\mathbb{P}\left(\sum_{i=1}^n X_i\geq nx\right)\leq \left(e^{-\Lambda^*(x)}+\varepsilon\right)^n.$$

unfortunately, this doesn't do better than exponential ever! I guess? do we need to go further into the tail to be able to do some exponential union bounds, or something? well wait, that makes no sense: you can just get everything having the same value with exponentially small probability in the binary case, and be at the end of the tail. you can't generally do better than exponential i guess, without making the entire thing trivial by going out of the range? ok so really we should be happy with this i guess?

a different issue is that we don't understand the convergence speed to the limit. like, i would want to say that for such-and-such $X_i$, I'll have at most such-and-such an $\epsilon$ at such-and-such an $n$? I guess we might be fine in lots of cases with just this though?