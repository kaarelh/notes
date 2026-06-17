
how would you teach someone what an integral is? well, here are some options for what to say (you can say multiple of these):
* the integral of a function is the area under its curve
* the integral is the inverse operation of the derivative
* the integral is defined by the limit of riemann sums
* the integral of an indicator on an interval is the length of the integral. and integration is a linear operator on the space of reasonable functions (also for series)
* the integral of x^k is 1/(k+1) x^{k+1}, and integration is linear
* the integral of x is x^2/2, the integral of e^{ax} is 1/a e^{ax}, etc (a bunch of random examples)
* integration is what you do to get from the velocity of an object as a function of time to its displacement

after saying some stuff like this, the other person will have a good notion of an integral. they might know much less about integration than you do, they might have many fewer cheap inference rule makers attached to their notion, but they now mean basically the same thing by an integral. my guess about what's going on here is this:
* in the presence of certain kinds of broader mental context, the integral notion is basically uniquely determined in any of a variety of ways. mostly, i mean that it is determined by specifying that it satisfies certain [inference rules]/axioms/properties
* in humans, these are communicated partly explicitly and partly implicitly. eg, you might explicitly tell me that the integral is the area under the curve. but maybe no one told me the definition of area, but it was demonstrated to me that the area of a whole shape is the sum of areas of the parts in a partition of it, and i was taught how to calculate the area of a rectangle, and the manner of operation with areas given by these parts (ok, with some further caveats around limits) constitutes a decent grasp of the area notion, and so supports the integral notion
* there is also a thing going on where we have the ability to extend the same notion into new contexts. you might teach me integration of functions from R to R only, but with some work i might be able to figure out how to work with integration of functions from R^n to R or C to C or whatever — like, i'll come up with some variant of the standard definitions for these. i think what's going on here is that i'm finding a way to fit a certain mental shape to a somewhat different context. it could be as simple as being like "ok, i have function from R^2->R, and i want to find some sort of under the graph type quantity... ah yes, the volume under its graph" or "i want to find its average... ah yes, it makes sense to think of it as this sort of analogous 2d riemann sum thing". we could think of these as slight modifications of the notion, but they are largely uses of the same machinery in a new context

there are theorems that somewhat capture this idea of various different properties pinning down the integral notion. for instance, you can prove that the riemann, lebesgue, and inverse derivative definitions are equivalent (on reasonable functions). this is a sort of rigid version of the softer thing that actually makes stuff work in humans, that might be ~necessary to make stuff work for soft notions

some directions:
* i think there could be an interesting field of study about the robustness of such notion-sharing processes
* there is a question of whether there needs to be some other lower-level thing first before this sort of thing can get started (because robustness of notion-sharing depends on the prior presence of some sort of mental context), or if there is a version of this that can be started from basically nothing
	* it'd be interesting to know how this works/worked in humans
* in this note, i've focused on the case of gaining a notion from another human. i should note that there is also an interesting question of how notions are first created/invented/discovered