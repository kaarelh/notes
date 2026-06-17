
# One can get a canonical choice of condensation loss coefficients for an image by requiring scale-freeness (only physics-rigorous)

Let's consider the expanded-out form of the simple condensation loss (ie single sum; I'm mostly making this choice because I find it easier to think about). Let's say that the coefficient a subset gets should depend only on its size $m$. (A caveat: imo it isn't completely obvious that this should be assumed if the domain has structure — e.g. maybe we should prefer information to be at convex sets. But let's go with this for now.) What should these coefficients $c_m$ be?

Fix a big image size $n$ (ie $n$ is the number of pixels) and some "template image" $A$. Now let $A_\alpha$ for $0<\alpha\leq 1$ be the big image that has a copy of the template $A$ in the upper left corner, scaled down by $\alpha$ from "full screen", and is blank elsewhere (I will ignore issues with pixel number theory technically not working out for various $\alpha$). Imagine that $A$ has low resolution compared to our big image, ie $A_1$ looks really pixellated. It seems natural to require that condensation be scale-invariant in the sense that the condensations of $A_\alpha$ and $A_\beta$ correspond in the obvious way — like, we should have the same variables appear at the same sets scaled by $\beta/\alpha$. I think the only way this happens for every template $A$ is if for all $0<\gamma, \delta<1$, we have the same tradeoff between storing information at level $m=\gamma \alpha^2 n$ vs storing at level $\delta \alpha^2 n$ for $A_\alpha$ as between storing at $\gamma \beta^2 n$ vs $\delta \beta^2 n$ for $A_\beta$. I.e. condensation is scale-free if and only if $c_{\gamma\alpha^2 n}/c_{\delta \alpha^2 n}=c_{\gamma\beta^2 n}/c_{\delta \beta^2 n}$ for all $0<\alpha,\beta,\gamma,\delta<1$. Rearranging and changing variables, this is saying that for all $x=\gamma\alpha^2 n,y=\delta\alpha^2 n,\rho=(\beta/\alpha)^2$, we have $c_{x}/c_{\rho x}=c_y/c_{\rho y}$, ie $c_{\rho x}=c_x c_\rho/c_1$ for all $x,\rho$. (The rest of the argument is just solving this textbook functional equation in the textbook way.) Since the optimization problem doesn't care about scaling all coefficients by the same constant, WLOG $c_1=1$, so this says $c_{\rho x}=c_\rho c_x$, ie $\log c_{e^{\log \rho+\log x}}=\log c_\rho + \log c_x$, . Introducing the auxiliary function $f(z)=\log c_{e^z}$, with the new variables $z=\log \rho$ and $w=\log x$ the equation becomes $f(z+w)=f(z)+f(w)$. This is [Cauchy's functional equation](https://en.wikipedia.org/wiki/Cauchy%27s_functional_equation), whose only solution assuming continuity (or various other weak conditions) is $f(z)=az$ for some constant $a$. Translating back, this means that the only option is $az=f(z)=\log c_{e^z}$, so with $x=e^z$ plugged in, $a\log x=\log c_x$, so $c_x=x^a$.

Conclusion: Condensation is scale-free iff the coefficients $c_m$ are given by a power law $c_m=m^\alpha$.

The exponent $\alpha$ remains a free parameter. Maybe that's intuitively nice because we want to allow different amounts of caring about local recovery (corresponding to fast-growing coefficients, ie high $\alpha$) vs minimizing total description length (corresponding to slow-growing coefficients, ie $\alpha$ close to $0$).


$c_{\gamma \alpha n}/

Idk if there is a canonical choice of exponent $\gamma$ though. 


# mess 

(this isn't actually achievable with an integer side length picture but let's ignore this — I think this is basically just to make the argument look nicer anyway). Then, splitting the image rectangle in two halves gives two new image rectangles of the same shape (this is why I said its aspect ratio should be the golden ratio). Fix some picture A and consider the following two options:
option BIG: our picture is A made of 2x2 pixels
option SMALL: our picture has A as the left side, made of 1x1 pixels, and nothing on the right side

Now it seems natural to require that the condensations of BIG and SMALL correspond to each other in the obvious way — like, each latent for BIG is mapped to the same 1/2 smaller latent for SMALL. I think that: [this happens for all template images A] <=> [for all ratios 0 < \alpha, \beta < 1, we have c_{\alpha n}/c_{\beta n} = c_{\alpha n/2}/c_{\beta n/2}]. 


