
# may 16

in S construction from notebook, we have some freedom for initial weights — like, we don’t have to make them precisely anything, just need some signal. can we use this to temper all the errors?

let’s compute an example to see what movement is probably needed once column norms are repaired. for this, take a tight frame U with d<m/2 and take 

mess: a set of random orthogonal directions in the orthogonal complement to rotate U into until row norms are typically off by eps d/m. row norm derivatives are 

# may 15

Ok, so let's see what happens when we take $S$ to contain the primitive variables and try to write all conditions in terms of it. Let's just take for granted here that dimension-counting works to tell us when $A+A^T=U_{ext}SU_{ext}^T$ can be solved, i.e., that it can be solved as long as $d\geq (m+1)/2$, and that it can in fact be solved with a matrix $A$ which is not that much larger than $A+A^T$ — i.e., that there isn't a huge amount of cancellation. Given these assumptions, the conditions just become the following.
* $A_{ii}=\left(U_{ext}SU_{ext}^T\right)_{ii}$ is (roughly) $-\varepsilon_i$
* $\lVert S \rVert_F^2=O(\varepsilon d)$

Letting $u_i$ denote row $i$ of $U_{ext}$ as a column vector, we can rewrite the first condition as $(u_i)^T S u_i=-\varepsilon_i$. 



# may 14

Let $U_{ext}$ denote the matrix with first $d$ cols being an orthonormal basis of $U$ and the last $m-d$ cols being an orthonormal basis of $U^\perp$. We wish to find an $m\times m$ matrix $A$ with the following properties:
* $A$ has cols in $U$
* $A_{ii}$ is (roughly) $-\varepsilon_i$
* $A+A^T=U_{ext} S U_{ext}^T$ for some symmetric $S$ whose top left $d\times d$ corner is all zeros
* $\lVert A\rVert_F^2=O(\varepsilon d)$

I think these are also the right conditions for a generic $A$ if we drop 1 and replace 2 and 4 by the same on $A_U$. Why doesn't that give us more freedom on 3 though?

Note that we can also write $3$ as $U_{ext}^T(A+A^T)U_{ext}=S$. Replacing $A$ by $A_U$ here will only change stuff which is not in the top left $d\times d$ block, so the condition is true with $A$ iff it is true with $A_U$, and so having a choice of $A$ beyond the choice of $A_U$ doesn't really give us extra wiggle room to get the condition right?

Condition 3 can be replaced by (and, indeed, comes from) $U^T(A+A^T)U=0$. 

### can we take $S$ as the primitive object and derive conditions on it?

one issue is with saying something about when a matrix can be written as something whose columns are in $U$ plus its transpose.

an easier problem: what are all the ways to write a symmetric matrix as another matrix plus its transpose: $B=A+A^T$? This is easy to understand: everything on the diagonal is fixed by $B$, we can pick everything above the diagonal freely, and everything below the diagonal is then fixed by the constraint. For which $B$ could a choice be made here so that $A$ has cols in $U$? We now have $d$ free params per column, for a total of $dm$ free params, and $m(m+1)/2$ equations constraining them from $B=A+A^T$, so this has a chance of working for any $B$ for $d\geq (m+1)/2$ 

Would it make any sense to pick $A$ to be something like $U (U^\perp)^T$. well oops, dims don't work




# may 4

again, what happens when you rotate in a plane which is not made of one vec in U, one in its complement? this is the same as projecting everything in U to that plane and then rotating that component. call the two top singular input directions of the projection $u_1$ and $u_2$; let $v_1$ and $v_2$ be the corresponding output singular directions, with sing vals $\sigma_1, \sigma_2$. Then I think the top order mass change with signs taken into account turns out to be $\sqrt{\delta}\left(\sigma_1 u_1 S v_2-\sigma_2 u_2 S v_1\right)$. 


# apr 25

split U as U_big cap U plus U_small cap U plus orth complement, call it U’, from the beginning. (i guess an issue is that this split can change?) since the former two are sent under S_eps to themselves, the unit vec u which maximizes the proj of S_eps u to the orth complement of U will be from U’. its proj to the orthogonal complement will obviously be orthogonal to U_big cap U and U_small cap U, so note that doing the uv rotation won’t change these two parts of U (actually this just follows even more simply from only u’ being affected in U by the rotation). we can potentially rotate until S_eps is the same, so until a coord gets to the right sum, tho also minding that we don’t go too far (ie st the delta term starts to compete with the sqrt{delta} term). maybe we want to also separate out coords which are already fixed btw? like pick 


# apr 23

Let $U\subseteq \mathbb{R}^m$ be the $d$-dimensional subspace we have presently. Let $S_\epsilon$ be the $m\times m$ diagonal matrix with $\pm 1$ along the diagonal according to whether the mass in each coordinate is too large or too small (if it's precisely right, say it's too small I guess, or whatever — let's think about it later). Then if there is a unit vector in $u\in S_\epsilon U$ which is reasonably far from $U$, ie has a reasonably large projection to $U^\perp$, then we are doing well — we can make a bunch of progress with the right rotation of $u$ into the direction that $S_\epsilon u$ projects to in $U^\perp$. The case where we have trouble is when all unit vectors in $S_\epsilon U$ are close to $U$. In that case, letting $u_{big}$ and $u_{small}$ denote the projections of a vector $u$ to big-mass and small-mass coordinates respectively, noting that $u_{big}=(u+S_\epsilon u)/2$ and $u_{small}=(u-S_\epsilon u)/2$, we can conclude that for any 

## general strategy
* keep fixing mass distribution with rotations into complement
* until get to a situation where $S_\epsilon U$ is too close to $U$. then start turning $U$ into a direct sum. here i'm not sure if we can just go all the way — i think the current proof just gives that you can get there unless you can do 1 again instead, so maybe u need to go back to the item above

given $S_\epsilon U$ has a pt at dist at least $\rho$, we can make $\sqrt{\delta}\rho$ progress with a step of $L^2$ size $\sqrt{\delta}$. assuming steps add as worst case, need to keep total sum of step sizes less than $\sqrt{d \varepsilon}$, and need to make $d\varepsilon$ mass progress. so would be nice to keep the rate $\rho$ at least $\sqrt{d\varepsilon}$. but then from that $\rho$, i think the directsummification step could take like $d\rho=d\sqrt{d\varepsilon}$ distance, which squares to $d^3\varepsilon$, which sorta sucks. the general formula here i guess would be that at $\rho$, the process could take $\sqrt{d\epsilon}/\rho + \rho d$, which is minimized at $\rho$ which solves $-\sqrt{d\varepsilon}/\rho^2 +d=0$, so $\rho^2=\sqrt{\varepsilon/d}$, so $\rho =(\varepsilon/d)^{1/4}$, so the distance is $2d^{3/4}\varepsilon^{1/4}$; squared dist would be $d^{3/2} \varepsilon^{1/2}$ which doesn't seem great :(

hmm but this is worst-case: if we take the directions of these steps to be random, we could do enormously better. in fact, we can take $\rho$ to be arbitrarily large but make even arbitrarily smaller steps, keeping the distance arbitrarily small from the first kind of step. this is probably silly-impossible though? okay, at least we can say that we can probably do better on the second step. here, if we are making $d$ orthogonal steps of size $\rho$ (not sure if this is true — needs to be thought about), then we are really traveling only $\sqrt{d}\rho$, or $d\rho^2$ squared distance. so here would want $\rho\leq \sqrt{\epsilon}$. what can we say about doing the first step with that rate? let's say somehow heuristically that we can take $d$ orthogonal steps, for the $d$ vectors in the basis. then if we travel $\sqrt{\epsilon d}$ in total, the distance we can afford to travel per step is $\sqrt{\epsilon}$. This lets us do about $\sqrt{\epsilon}\sqrt{\epsilon}=\epsilon$ fixing per step, which does indeed add up to $\epsilon d$ over the $d$ steps. but this is surely schizophrenic — how on earth would we make this precise? :)
# apr 22

how to understand local orthogonal transformations on these vectors?
* for a single vector, it's equivalent to just providing a direction to slide it in which is orthogonal to it
* for a pair of vectors, pick a direction to slide the first one in, apply the corresponding rotation, then pick for the second vector some direction orthogonal to the first and second and slide it in that direction
* in general, should be able to decompose any map like this, where for $d$ vectors in $\mathbb{R}^m$, we get to choose a direction in $\mathbb{R}^{m-1}$ for the first vec, then a direction in $\mathbb{R}^{m-2}$ for the second, and so on down to a direction in $\mathbb{R}^{m-d}$ for the last one. (note that we can probably take d<m/2 wlog by passing to the complement)
* maybe we can pick these directions so as to make a bit of progress with balancing each time? maybe just check which coordinates need moving in which direction and try to pick a direction to move in which addresses that on each step? of course, we aren

Each choice here fixes what the map does in a particular 2d subspace. maybe we can match directions with those in the complement — this makes it so that we don't have to think about dependencies — and then just say that there's some way to make these individual rotations work out? ok, so what happens if you just rotate each vector into some complement-vector by some amount? Maybe call these pairs $(u_i,v_i)$, with $u_i\mapsto \sqrt{1-\delta_i}u_i+\sqrt{\delta_i} v_i$. Then the distance requirement is that $O(\varepsilon d)= \sum_i (u_i-\sqrt{1-\delta_i}u_i+\sqrt{\delta_i} v_i)^2=2\sum_i(1- \sqrt{1-\delta_i})\approx \sum_i \delta_i$ (indeed this should be rigorable into an upper bound up to some const factor, but let's ignore that now?). So at least roughly, we have $\sum_i \delta_i = O(\varepsilon d)$. The other requirement is that we actually fix the rows. Let the error in the mass of row $j$ be $\epsilon_j$. Note that $u_{ij}\mapsto \sqrt{1-\delta_i}u_{ij}+\sqrt{\delta_i} v_{ij}$ contributes a mass change of $$u_{ij}^2-\left(\sqrt{1-\delta_i}u_{ij}+\sqrt{\delta_i} v_{ij}\right)^2=u_{ij}^2-\left((1-\delta_i)u_{ij}^2 +2\sqrt{1-\delta_i}u_{ij}\sqrt{\delta_i}v_{ij}+\delta_i v_{ij}^2 \right)=\delta_i u_{ij}^2 -2\sqrt{\delta_i(1-\delta_i)}u_{ij}v_{ij}-\delta_i v_{ij}^2.$$ The constraint from row $j$ is then $$\epsilon_j = \sum_i \left(\delta_i u_{ij}^2 -2\sqrt{\delta_i(1-\delta_i)}u_{ij}v_{ij}-\delta_i v_{ij}^2\right)$$
fixing some params now: maybe try making all \delta_i just equal, so say $\delta$? then we maybe want a row orthogonality constraint to get rid of the middle term, because otherwise that's huge compared to the other terms? then the remaining equation would be $$\epsilon_j =\delta \sum_i\left( u_{ij}^2 - v_{ij}^2\right)$$
so we have some constraints on the row norms of the $v$ matrix, namely that they are the row norms of the $u$ matrix plus $\epsilon_j/\delta$. Note that $\delta$ needs to be at most $\epsilon$ up to some constant, so this says we need the $v$ row norms to be the $u$ row norms minus some constant. but this is impossible right? the $v_i$ need to squared-sum to the same thing

ok this was stoopid. there might be some calc error because it seems a bit weird, but anyway it's not possible to reduce row norm with a vec that's orthogonal lol. there must be a calc error tho — seems like a thing that ought to be fixed! so why must there be an error? well because with these choices, the ans ought to always be positive, but i don't think the algebra has that property? wait nvm i was stoopid now. we're not adding the vec, we're also scaling down. totally could happen a priori that that this changes norm in either direction? tho yea not really because the vs do need to be unit vecs completing orthogonally (in the m = 2d case), meaning their row sums are fixed to 1 minus the row sum of the u, which gives that the diff is O(eps), so we get that eps_j = delta O(eps), so we need like delta at least 1?? that would be fucked because then the bound would be like $d$ lol


can we find a direction in the span that's really close to having all coords $\pm \sqrt{\frac{1}{m}}$ itself? this is roughly the same question as finding a vector of this form which has a really high projection to the space. does any k-dim subspace need to pass close to some corner of the hypercube? well no, eg the one on the first k coords. but what if we require it to be supported equally on all coords?
* this question is just about dotting with all basis elts and squaring and summing. can we make all the dot prods sorta large at once?
* for each basis elt there's a best thing we can do — just match signs with that one. this is great if all its coords have a similar size, but fails if very diff coords
* maybe we can do much better for linear combos of basis elts? can we make each dot prod simultaneously 



# new 

for the d+1 \times d case, scale orthogonal cols to have norm 1 and then extend the matrix with a last orthonormal column c

recall that our goal is to apply some isometry U to the R^{d+1} in which the columns live such that the first d columns are 'equally supported on all canonical basis coordinates'. note that this is equivalent to Uc having all coordinates $\pm \sqrt{\frac{1}{d+1}}$. 

note that since each row of the original matrix has squared norm $(1\pm O(\varepsilon))\frac{d}{d+1}$, and since the completed matrix is an orthogonal matrix, each coordinate of c has square $\frac{1}{d+1}+O(\varepsilon)\frac{d}{d+1}$  

now i think the crucial thing to figure out is this:
* if we take U to be the matrix which just rotates c with every coordinate being $\pm \sqrt{\frac{1}{d+1}+O(\varepsilon)\frac{d}{d+1}}$ to the vector which has every coordinate $\pm \sqrt{\frac{1}{d+1}}$ (with the corresponding sign in each respective coordinate), then is total movement of all the other vectors under $U$ (ie sum of squared euclidean distances moved) $O(\varepsilon d)$?

If the ans is no, then I'm guessing we have a counterexample? If the answer is yes, then getting a$O(\varepsilon d)$ bound feels super tractable now, namely with some combination of this idea of passing to the complement (as we did here with just 1 vector, but we can also do it with more vectors) and the rotation stuff we discussed before (in particular, maybe taking a row that has too much mass and rotating it into some direction which has too little mass)

# old
wait i think maybe a random construction for the matrix just works? after fixing the orthogonality by projecting to orthogonal complement iteratively? for large enough n compared to d? seems like this just works??? because only ruins all the rest of the stuff a bit right? idk maybe doesn't work actually, need to calculate

Parseval frame has $\sum_{i=1}^m (u\cdot v_i)^2$ is const, wlog 1 for all unit vecs $u$. this is the same as $u^T \sum_i v_i v_i^T u=1$

$\sum_{i=1}^m v_i v_i^T=I$ and 



see notebooks for detailed thoughts. but high-level strategy is to start by moving to a configuration where each vector is in an orthogonal component which is a tight frame, and then to move from that to a good configuration by a more manual method

probably the critical thing to understand for the second step is if we have a configuration which is a union of two orthogonal tight frames, each in half the dimensions, one containing a $\frac{1+\varepsilon}{2}$ frac of the vectors and the other containing $\frac{1-\varepsilon}{2}$, then how can one fix that? 

sth that does not work: moving all vecs in the bigger part in the same direction in the smaller. this puts more variance along that direction, unfortunately. one needs to move into that subspace in an uncorrelated way i guess? maybe pick a tight frame with that many vecs in the orth compl and add it parametrically slowly? does this create correlations between coordinates? i guess it probably doesn't create big-big or small-small correlations because bigs are just scaled and because the $W^T W$ submatrix for small coordinates can be decomposed as a sum of two such matrices for tight frames. but big-small correlations are indeed a problem. 



https://arxiv.org/pdf/1809.04726.pdf
This concept goes by many other names in the literature, such as well-spread vectors [9] or geometric scaling for rank one Brascamp-Lieb datum [13]. The name we use here originated in [15].


https://arxiv.org/pdf/1211.1041.pdf
radial isotropic position


defines dynamical system, works after perturbation, worst-case bad though
https://cs.uwaterloo.ca/~lapchi/papers/

Paulsen-conf.pdf



new strat: just do SVD, find good components. find those which have too little and those which have too much. scale into the thing with too little for all vecs just all at once. do this by adding a tight frame. vecs can be decomposed as W_I = big_i + small_i. now add extra_i where extra_i form a tight frame in small that has the right orthogonality property to big. note that can decompose

sum_i W_i W_i^T = big big + small small + extra extra + big small + small big + big extra + extra big + small extra + extra small

(also need coeff on big and extra i guess compared to old coeffs anyway)

big big, small small, extra extra are all diagonal, so good. big small and small big are 0 because svd. issue just with big extra and extra small. but should be doable to make them all 0 given d<<n? dim count works at least i think. basically just need extra to be orth to all stuff


@Hugo Eberhard here is a matrix completion problem that i think would solve an interesting open problem (ie i think i have a reduction of the open problem to this tho some chance it is wrong, happy to explain that part):

Suppose d<<n and we have a matrix with d orthogonal columns and n rows. Suppose also that each row has squared norm d/n and each column has squared norm between 1-eps and 1+eps. Prove that there is a way to add d/2 more orthogonal columns to the matrix such that each column has squared norm between some two positive constants (eg 1/2 and 2) and additionally, for each row of the new matrix, if you split it into thirds (ie vectors of length d/2 each), the first third has norm equal to the last third and the second third is orthogonal to the last third

can we just pick however orth and then fix row norms and cols will be fine? hmm prolly not


