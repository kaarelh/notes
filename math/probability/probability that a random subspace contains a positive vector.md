
found in https://arxiv.org/pdf/1004.0394

>Thm. The probability a uniformly random $k$-dimensional subspace of $\mathbb{R}^n$ contains a vector with all positive coordinates is $\frac{1}{2^{n-1}}\sum_{j=0}^{k-1}\binom{n-1}{j}$.

but maybe there's a nicer argument than in that paper — after all, the ans is the probability that at most $k-1$ of $n-1$ coinflips land on heads. but what would the coinflips be here?

maybe we should think of the subspace as being the intersection of n-k random hyperplanes (with orthonormal normal vecs maybe)? and then n more get thrown in as the coordinate hyperplanes?

observation: one gets this probability also having fixed the subspace and any arbitrary collection of n hyperplanes, only getting to choose which side is positive and which side is negative for each. one should explain why the coinflip quantity arises here i think. wtf are the positive and negative coinflips? why do we need at most k-1 bad coinflips? maybe try to see what’s happening for some small cases first?

Note that the statement above is iff the probability of first getting a positive vector in the subspace exactly when you add the $j$th vector is $\binom{n-1}{j}$

Is the following maybe true: the number of orthants that a subspace of dimension $k$ passes through is $\sum_{j=0}^{k-1}\binom{n-1}{j}$? 

# indeed, a nice proof

>Thm. The probability a uniformly random $k$-dimensional subspace of $\mathbb{R}^n$ contains a vector with all positive coordinates is $\frac{1}{2^{n-1}}\sum_{i=0}^{k-1}\binom{n-1}{i}$.

The theorem above follows by symmetry (of orthants) from the following claim. 
> Proposition. With probability $1$, a uniformly random $k$-dimensional subspace of $\mathbb{R}^n$ passes through exactly $2\sum_{i=0}^{k-1}\binom{n-1}{i}$ orthants.

What follows is a pretty nice proof of this proposition from https://math.stackexchange.com/a/1889873 which begins by counting the number of cells in a generic hyperplane arrangement.

Let $F(j,k)$ denote the number of cells that a generic configuration of $j$ hyperplanes (more precisely, by $j$ subspaces of dimension $k-1$ which are in general position) cuts $\mathbb{R}^k$ into. Let's prove by induction that $F(j,k)=2\sum_{i=0}^{k-1}\binom{j-1}{i}$. For the base case, note that $F(1,k)=2$ and $F(j,1)=2$, in agreement with the proposed formula. Note that when we go from $j-1$ hyperplanes to $j$ hyperplanes by adding another hyperplane $H_j$, the number of cells increases precisely by the number of cells $H_j$ cuts in two parts, which is the number of cells that $H_j\cong\mathbb{R}^{k-1}$ is itself cut into by the previous $j-1$ hyperplanes. (It might help to think about the example of adding another plane to a configuration of planes in $\mathbb{R}^3$ here.) Thus, $F(j,k)=F(j-1,k)+F(j-1,k-1)$. Given the inductive hypothesis, this is $2\sum_{i=0}^{k-1}\binom{j-2}{i}+2\sum_{i=0}^{k-2}\binom{j-2}{i}=2\sum_{i=0}^{k-1}\binom{j-1}{i}$, finishing the inductive proof.

Next, note that if we have $j$ generic hyperplanes in $\mathbb{R}^n$ with $n\geq k$, the above implies that a generic $k$-dimensional subspace $U$ will be split into $2\sum_{i=0}^{k-1}\binom{j-1}{i}$ cells (since the generic hyperplanes restrict to generic hyperplanes in $U$). Note also that the cells in $U$ are in bijection with the cells of the hyperplane arrangement in $\mathbb{R}^n$ which $U$ passes through. Thus, $U$ passes through $2\sum_{i=0}^{k-1}\binom{j-1}{i}$ cells. To get the desired result, just apply this to the special case where the hyperplanes are the $n$ coordinate planes — the cells are then precisely the orthants.

Comment. I feel like there should be a nicer proof that each time you give the subspace another dimension — say the $k$th one — it picks up exactly $2\binom{j-1}{k-1}$ new cells. 
Update: Yep found such a proof — see notebook. it is inspired by https://math.stackexchange.com/a/2923134 (also related: https://math.stackexchange.com/a/3273230 ). the pf in the notebook had some sus lemmas, but now finished off in a discussion with sam eisenstat

Here are some well-known corollaries:
prob that convex hull contains origin (3b1b putnam problem), prob that positive cone contains origin, prob that all pts in some common half-space, prob that $n$ random blue and $m$ random red points can be separated with a hyperplane through the origin (the trick here is to note that this is equivalent to the blue and reflections of red pts being on the same side of a hyperplane)

Lemma. A finite set of points is in a common open half-space iff their convex hull does not contain the origin.
Pf.
* forward implication: If they are in a common open half-space, then their convex hull is also in this open half-space. Since the origin is not in any open half-space, it is not in this one, either.
* backward implication: If their convex hull does not contain the origin, find the point in the convex hull with the smallest norm; this defines an open hyperplane containing all the points. (Since the convex hull of a finite set is compact, there is a point with infimal norm; since it does not contain the origin, this point has nonzero norm.)

(The backward direction is actually false if we drop the condition that the set of points is finite. For a counterexample, pick all points on the plane which are lexicographically strictly greater than the origin $(0,0)$. The origin is not in the convex hull of these points, but the points are not in a common open half-space.)


positive cone contains origin iff there is a positive vector in the orthogonal complement iff 

subspace contains positive vector iff the orthogonal complement does not contain a positive vector 

in general, what's the probability that a random subspace nontrivially intersects with a particular cone?

https://arxiv.org/pdf/1603.05533 : "The problem of computing the probability that a random subspace intersects a given cone is a central problem in integral geometry, and there are explicit formulas for this probability in terms of the so-called intrinsic volumes."

Intrinsic Volumes of Polyhedral Cones: A combinatorial perspective https://arxiv.org/pdf/1512.06033

# an attempt at another proof

let $p(n,k)$ denote the prob that a random $k$-dimensional subspace $V\subseteq \mathbb{R}^n$ contains a positive vector. let $q(n,k)$ denote the prob that a random $k$-dimensional half-space $H\subseteq \mathbb{R}^n$ contains a positive vector.

note that $p(n,k)=q(n-1,k)$ by picking a sign for a first coordinate hyperplane and then considering the remaining problem with the projection of the subspace to the orthogonal $\mathbb{R}^{n-1}$

but also another relation on $q(n,k)$ can maybe be found by thinking of the selection process as first picking a $k$-dimensional subspace in $\mathbb{R}^n$ and then restricting to half of that? yea i guess it's just that the k-dimensional subspace succeeds iff at least one half succeeds, which has prob twice the prob that a half succeeds minus the prob that they succeed together, which happens iff the hyperplane at which they intersect succeeds, so we have $p(n,k)=2q(n,k)-p(n,k-1)$

putting these two together gives $p(n,k)=2p(n+1,k)-p(n,k-1)$, so $p(n+1,k)=\frac{p(n,k)+p(n,k-1)}{2}$ 

in n coinflips get at most k-1? split on first coinflip! then avg of two! pf done i guess

ok this is sorta nice. but let's try to translate it to something nicer still.

have k-dim subspace in n+1 dims. now this is the same as a half-space of dim k in just n dims. here the prob of winning is the prob of winning with a subspace of dim k in n dims minus the prob of winning only in its wrong halfspace, but also the prob of winning with a subspace of dim k-1 plus the prob of winning only in the right half-space, so it is the avg of the two first probs. 

# a refinement of the previous attempt

Fix $V$, a generic $k$-dimensional subspace of $\mathbb{R}^n$, but forget for each coordinate which direction is positive vs negative, determining these with independent fair coinflips. Let $p(n,k)$ denote the probability that the $k$-dimensional subspace comes to contain a positive vector.[^1] Let $q(n,k)$ denote the probability that if one flips $n-1$ fair coins, one gets at most $k-1$ heads.

> Proposition. $p(n,k)=q(n,k)$.

Pf. Look at picking a random orientation for the last coordinate hyperplane. Note the following equivalences.
* $V$ comes to contain a positive vector
* $\iff$ $H$, the $k$-dimensional half-space of $V$ on whichever side of that hyperplane is chosen to be positive, comes to contain a positive vector
* $\iff$ $H'$, the projection of $H$ to the $\mathbb{R}^{n-1}$ first coordinates, comes to contain a positive vector in that $\mathbb{R}^{n-1}$
Picking the last sign corresponds to choosing between $H'$ and $-H'$. Also call $V'=H'\cup (-H')$, i.e., $V'$ is the projection of $V$ to the first $n-1$ coordinates.

Now, we choose the last sign in a funny way (though it'll still turn out to be a fair coinflip independent of other sign choices):
1. flip a coin to determine if the last sign will be chosen 'favorably' or 'unfavorably';
2. either way, determine the other $n-1$ signs, then come back to this last sign;
3. if the last sign is to be chosen 'favorably':
	1. if the choice of the last sign matters for whether one gets a positive vector, make the choice so that we get a positive vector;
	2. if it doesn't matter, make it independently at random;
	3. this branch gives a positive vector iff $V'$ contains a positive vector, which has probability $p(n-1,k)$;
4. if the last sign is to be chosen 'unfavorably':
	1. if the choice of the last sign matters for whether one gets a positive vector, make the choice so that we do not get a positive vector;
	2. if it doesn't matter, make it independently at random;
	3. this branch gives a positive vector iff $H'$ and $-H'$ both contain a positive vector, which happens iff the $k-1$-dimensional subspace separating the two, i.e. $H\cap H'$ , contains a positive vector, which has probability $p(n-1,k-1)$.
Summing the probabilities of getting a positive vector up across the two conditionals, we get $p(n,k)=\frac{1}{2}p(n-1,k)+\frac{1}{2}p(n-1,k-1)$. The same recurrence relation is satisfied by $q(n,k)$ — one can see this by conditioning on the first coinflip. The two also agree on base cases: $p(n,0)=0=q(n,0)$ for any $n\geq 1$ and $p(k,k)=1=q(k,k)$ for any $k\geq 1$. It follows by strong induction on $(n,k)$ that $p(n,k)=q(n,k)$, which is what we set out to show.


> Remark 1. Note that the probability of containing a positive vector is also the number of orthants hit by the subspace divided by $2^n$, so we've also determined that a generic subspace strictly intersects with $2\sum_{i=0}^{k-1}\binom{n-1}{i}$ orthants.

> Remark 2. Since orthants that $V$ passes through are in bijection with regions that $V$ is cut into by restrictions of the $n$ coordinate hyperplanes to $V$, and since we can choose a generic $V$ to get any generic arrangement of $n$ hyperplanes passing through the origin in $\mathbb{R}^k$ we like,[^2] we've also determined that a generic arrangement of $n$ hyperplanes passing through the origin in $\mathbb{R}^k$ has $2\sum_{i=0}^{k-1}\binom{n-1}{i}$ regions. 

> Remark 3. Take the standard hyperoctahedron in dimension $n$ — the convex hull of the standard basis and its reflection across the origin, i.e., the convex hull of the $2n$ vectors $\pm e_1,\pm e_2,\ldots, \pm e_n$. Slice through it with a random $k$-dimensional subspace; the shadow it leaves on the subspace is a $k$-dimensional polytope. How many facets (i.e., $d-1$-dimensional faces) does this polytope have? The above implies that (with probability $1$) it has exactly  $2\sum_{i=0}^{k-1}\binom{n-1}{i}$ faces. 


## nicest proof?

I'm pretty happy with the following argument for our hyperplane arrangement region counting problem. It's missing some details — feel free to ask if something is unclear. I'm also still hopeful that maybe there is an even neater version of this argument, or that there is some other even neater idea. 
  
> Claim. Let $\mathcal{H}$ be a generic set of $n$ (affine) hyperplanes in $\mathbb{R}^k$. The regions made by $\mathcal{H}$ can be put in bijection with subsets of $\mathcal{H}$ of size at most $k$. (Therefore, there are $\sum_{i=0}^k \binom{n}{i}$ regions.)

> Pf. Say we have an arrangement of $n$ (affine) planes in $\mathbb{R}^3$. (We're doing the $k=3$ case because this lets one visualize the situation and because the argument for the general case is essentially the same.) Now, in this $\mathbb{R}^3$, consider a generic extended flag $\emptyset=V_{-1}\subsetneq V_0 \subsetneq V_1\subsetneq V_2 \subsetneq V_3=\mathbb{R}^3$ (the $V_i$ here are subspaces — a flag is just an increasing sequence of subspaces). Concretely, you could let $V_1$ be the $x$ axis and $V_2$ be the $xy$ plane. Our hyperplane arrangement leaves a shadow on each $V_i$; we will now track how many regions each $V_i$ sees. $V_{-1}$ sees $0$ regions. For $i\geq 0$, the regions seen in $V_i$ are those already seen in $V_{i-1}$ plus one more for each vertex made by the restriction of the arrangement $\mathcal{H}$ to $V_i$, so one for each subset of $H$ of size $i$. Moving from $V_{-1}$ up to $V_3$, the regions get put in bijection with all the subsets of $H$ of size at most $3$, which is what we wanted to show.

> Remark. There is also a non-iterative way to see the same bijection. To describe it, we will put a total preorder on $\mathbb{R}^3$ that captures points being seen earlier in the above process of starting from $V_{-1}$, then revealing the origin $V_0$, then revealing the $x$ axis $V_1$, then the $xy$ plane $V_2$, then the entire space $V_3=\mathbb{R}^3$. Let's think of going from $V_i$ to $V_{i+1}$ as not happening in a discrete step, but as coming from a uniform widening of $V_i$ — for example, going from $V_1$ to $V_2$ looks like starting from the $x$ axis, thinking of it as a strip of width $0$ that lies inside the plane $V_2$, and then increasing the width of this strip from $0$ to $\infty$, getting to any point in $V_2$ at a certain time. In this process, the point $(x,y,z)$ is seen earlier than the point $(x',y',z')$ iff $(|x|,|y|,|z|)$ is reverse-lexicographically smaller than $(|x'|,|y'|,|z'|)$. One can show that each region $R$ of the arrangement has a unique minimal point $p(R)\in \mathbb{R}^3$ under this preorder (that is, a unique point which is first seen in the above process); we can get a map from regions to subsets of $H$ by mapping $R$ to the set of hyperplanes that $p(R)$ is in. One can prove that this map is a bijection between regions and subsets of $\mathcal{H}$ of size at most $3$. Its inverse, a way to go from collections of hyperplanes to regions, is given as follows: given a set of hyperplanes $S$, pick the unique point $p=p(S)$ in their intersection with as many final coordinates set to $0$ as possible (specifically, $3-|S|$ coordinates) (this is also the minimal point in the intersection of the hyperplanes in $S$), then look at the local configuration of these $|S|$ hyperplanes around $p$, restricting to the subspace with those final coordinates set to $0$; in this local picture, there will be a unique adjacent region $R$ where the last nonzero coordinate is always larger than that of $p$; we map the subset $S$ to the region $R$. It's pretty clear that for $R$ obtained from $S$ in this way, we have $p(R)=p(S)$, so going from a subset to a region and then back is the identity. Going from a region $R$ to a subset $S$, we must again have have $p(R)=p(S)$ because otherwise one could take a small step from $p(R)$ toward $p(S)$ which wouldn't leave $R$ but would make the new point strictly earlier in the preorder than $p(R)$, contradicting minimality. Since $p(R)=p(S)$ and we noted earlier that there is only a unique region adjacent to $p(S)$ with $p(S)$ as the minimum, this region must be $R$. So going from a region to a subset and then back to a region is also the identity. So we indeed have a bijection between regions and subsets.



# mess

intersections of these planes will make a bunch of points, lines, planes, and also the entire space — the entire space is the empty intersection

$$V_{-1}:=\emptyset \text{ is a subset of }V_{0}:=\left\{\vec{0}\right\}\text{ is a subset of }V_{1}=\left\{\vec{0}\right\}\text{ is a subset of }V_{0}=\left\{\vec{0}\right\}\text{ is a subset of }V_{0}=\left\{\vec{0}\right\}$$

the empty set $V_{-1}=\emptyset$ which is contained in origin $x=0,y=0,z=0$ inside the $x$ axis $y=0,z=0$ inside the $xy$ plane $z=0$. We claim that the origin 

each vertex you see makes one new region! on each step!

can map each region to its leximinimal point

if two different regions have the same leximinimal point, then 

oh wait. there's some rewrite of this in terms of taking a region and going to its lexicographically minimal point i think. or like in abs value on coords. like push last coords to 0

[^1]: A priori, we might think that $p(n,k)$ could depend on $V$, but it turns out not do do so as long as $V$ is generic. Note that one can sample a random subspace by first sampling a random subspace and then flipping a coin for whether to flip each coordinate axis or not, so proving that we get a certain constant probability of containing a positive vector in the conditional setup above also proves that one gets the same probability if one just picks a random subspace.
[^2]: This requires proof I guess. By looking at the normal vectors of the hyperplanes, one can reduce it to finding $n$ orthogonal vectors with desired restrictions into $\mathbb{R}^k$, and I think it's not too bad to see that this is possible for generic vectors (also getting a generic subspace out again).
