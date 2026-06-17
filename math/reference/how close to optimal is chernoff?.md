
https://math.mit.edu/~goemans/18310S15/chernoff-notes.pdf

$X_i$ are n 0/1 with 50/50 independently at random. sum X_i will have expectation n/2


chernoff says prob of being above $\mu(1+\delta)$ is at most $e^{-\mu \delta^2/2}$ 

prob of being above this is just sum of binomial coeffs above this: $\sum_{k\geq n(1+\delta)/2}\binom{n}{k}$. starting at $k=(1+\delta)n/2$, the next thing is this times $\frac{n-k}{k+1}$. this is like a geometric series but with a decaying! ratio, so bounded above by the same except without the decay, so the ratio is $\frac{1-\delta}{1+\delta}$. for $\delta$ which is const, this is fine, get just $\frac{n!}{(n(1+\delta)/2)!(n(1-\delta)/2)!}$ up to a const frac, so this just is the correct ans. up to some $\sqrt{n}$ term this is just $\frac{n^n}{(n(1+\delta)/2)^{n(1+\delta)/2} (n(1-\delta)/2)^{n(1-\delta)/2}}=\frac{2^n}{ (1-\delta^2)^{n(1-\delta)/2}(1+\delta)^{n\delta}}=\frac{2^n}{ e^{-\delta^2 n(1-\delta)/2}e^{n\delta^2}}=\frac{2^n}{e^{n\delta^2/2}}.$  i guess didn't actually need the upper bound calc here, just needed lower bound to check against chernoff, right. but looks perfect almost!! i guess in general maybe the $\frac{1-\delta}{1+\delta}$ ratio geom series thing is most of the gap, so as this is about $1-2\delta$ for small $\delta$, we get like $\frac{1}{2\delta}$.