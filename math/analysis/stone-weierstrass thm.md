
thm. can uniformly approximate a continuous function on a closed interval by a polynomial


wlog interval 0 to 1 and function grows from 0 to 1 also (can make it grow by adding a big enough linear thing, which ofc can be subtracted again after once the new function has been approximated without changing the error)

now we want to construct a particular cdf i guess. how? we could use binomials with high n to make tiny bumps i guess. i guess we can reduce norm this way. but we are also making the function more spiky maybe? wait no! this confused pdf and cdf. the binomials make small step functions! and yes can make the given increasing function out of these small step functions. just split [0,1] into finitely many pieces such that only at most eps increase in each piece. then put such a step at the center of each piece with as much increase as that piece increases, and make it sharp enough compared to the number of pieces that the error outside the piece is negligible. now we have an eps + eps' approx of the original function (uniformly)

wait no idk what i was talking about with the binomials. the cdf of a binomial is not a polynomial right. but the above is right in saying that it is sufficient to construct arbitrarily precise polynomial approximations to a step function (first squish it to be as thin as needed, then get good approximation, then done). one can do this with any entire step function — its power series (taylor series) gives better and better polynomial approximations on compact sets. here is such a function: https://math.stackexchange.com/a/4390475/540174



# mess

hmm one thing we could do is mollifying the function, ie convolving it with a smooth bump. this should make it smooth right? for a continuous function on a compact set, this gives you sth which is arb close in uniform norm because it's uniformly continuous
ok so now done if can approx a smooth function well enough

maybe do domain $[-1,1]$ instead, let func go through 0 by shifting by a const, and write function as sum of odd plus even in the standard way (ie even is avg of f(x) and f(-x), odd is diff/2)

i guess it should be possible to do:
* the odd thing as x times a poly in $x^2$
* the even thing as x^2 times a different poly in $x^2$

