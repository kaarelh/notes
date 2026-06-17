# a cheap trick for asymptotically integrating a class of functions fast?

For which functions $p\colon \mathbb{R}^{>0}\to \mathbb{R}^{>0}$ is it true that $\int_c^a p(x) dx\sim a p(a)$ (where $c$ is a constant and the asymptotic equivalence is as $a\to \infty$)? Let's just ask this for monotonic functions. I guess this should be true for some class of $p(x)$ which are close enough to $1$.

Expanding the RHS as an integral, we see that it's true iff $\int_c^a (p(a)-p(x))dx=o(\int_c^a p(a) dx)$, which in turn is true iff $\int_c^a (1-p(x)/p(a))dx=o(\int_c^a 1 dx)$

Since $p(x)$ is monotonic, the errors just add, so certainly $1-p(x)/p(a)$ must be $o(1)$ for all but the first $o(1)$ fraction of the range, but this is not sufficient. It is sufficient if $p$ is bounded below — in particular, it is sufficient when $p$ is monotonically increasing. This tells us e.g. that $\log x$ asymptotically integrates to $x \log x$, because after the first $1/\log \log a$ fraction of the range, $p(x)/p(a)\geq p(a/\log \log a)/p(a)=\frac{\log a - \log \log \log a}{\log a}=1-o(1)$.   

What about the case where $p(a)$ is a function monotonically limiting down to $0$? In that case, a sufficient condition is that $1-p(x)/p(a)$ is $o(1)$ for all but the first $o(p(a))$ fraction of the range. This tells us e.g. that the function $1/\log x$ asymptotically integrates to $x/\log x$, since after the first $1/(\log a \log \log a)$ fraction of the range, $p(x)/p(a)\leq p(a/(\log a \log \log a))/p(a)=\frac{\log a}{\log a-\log \log a \log \log \log a}=1+o(1)$. 

My general unjustified feeling here is that this kind of thing will probably keep working for powers of logs, and probably won't work for any $x^\alpha$, and I'm not sure if we can say something more interesting about where exactly between these things it breaks down?



# a cheap trick for asymptotically up to a constant factor integrating a larger class of functions fast

What if we ignore constants, asking instead for the weaker condition that $\int_c^a p(x) dx=\Theta(a p(a))$? Now all $x^\alpha$ also go through.

For functions $p$ which only change up to a multiplicative const factor when the input changes by at most a small enough multiplicative const for all large enough inputs, we have $\Theta(a p(a))=\int_{(1-\delta) a}^a p(x) dx$ for any fixed const $\delta$, so the condition above is equivalent to the final $\delta$ fraction of the range contributing a const fraction of the integral.


# mess

has $1-p(x)/p(a)=1-\frac{\log a}{\log x}$ 

so this being true is the same as the claim that for any $\epsilon>0$, the 

For which densities 