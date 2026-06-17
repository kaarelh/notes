
Wait, I'm not sure I fully understand if there is some fundamental obstacle to the following strategy working:
* As long as there is imbalance, we can find a particular vector $u\in U$ with coordinates which are 'imbalanced in the same way', and a vector $v\in U^\perp$ with coordinates that are 'imbalanced in the opposite way', and rotate $u$ to $v$?
I guess we've tried this. But have we really ruled out the best version of this? Let's think more about what happens when we do this.

## what does rotating $u$ to $v$ do to the masses?

A rotation of $u$ to $v$ looks like $u\mapsto \sqrt{1-\alpha^2}u+\alpha v$, for some $\alpha$ we can choose. The squared distance we travel with this is $\lVert u-\sqrt{1-\alpha^2}u+\alpha v\rVert^2=\left(1-\sqrt{1-\alpha^2}\right)^2+\alpha^2=\alpha^2+O(\alpha^4)$, so the distance is $\alpha+O(\alpha^4)$. What are the masses before and after? Well, the contribution to coordinate $i$ from every other basis vector is preserved, and the contribution from $u$ changes as $u_i^2\mapsto \left(\sqrt{1-\alpha^2}u_i+\alpha v_i\right)^2=(1-\alpha^2)u_i^2+\alpha \sqrt{1-\alpha^2}u_i v_i +\alpha^2 v_i^2$. So the change is $\alpha\sqrt{1-\alpha^2}u_i v_i+\alpha^2(v_i^2-u_i^2)$. edit: oops missing a factor of 2 here. it should be $2\alpha\sqrt{1-\alpha^2}u_i v_i+\alpha^2(v_i^2-u_i^2)$

I guess the issue is that we will typically struggle to get all the signs right? Maybe we could force the linear terms to be $0$ though, and then think about what happens to the remainder? I guess we could get $d-1$ desired zeros in $u$ and $m-d-1$ desired zeros in $v$ at best, so we can't force the linear term to be exactly $0$. Maybe we could force these to be small enough that the second-order term starts to matter though? This seems tough for really small $\varepsilon$ — we will be forced to keep changes really small, but I don't see why we'd be able to keep the products small in $\varepsilon$. So I guess we must win with the first-order term in general, except when $U$ has some particular structure. I guess we've argued already that we can make decent progress with the first-order term as long as there aren't any coordinates which are already fixed, but after that point, there seemed to be a chance that we are fucking things up too much? Like, if we just track the sum of the changes we care about, taking coordinates to be partitioned into $S,F,B$ (small, fixed, big), and letting $\Sigma$ be the diagonal matrix with respectively $+1,0,-1$ at the corresponding index on the diagonal, we want to find a pair $u,v$ which makes $v^T \Sigma u$ reasonably big. What would need to happen for there not to be such a choice? I guess we 
can still say that the maximizing $v$ for any $u\in U$ is a rescaling of the projection of $\Delta u$ to $U^\perp$.

I guess this is actually just $0$ when $U=U_{big}\oplus U_{small}$, in which case I think what works is just the same strategy but we win due to the second-order term. So maybe we should take both into account at once after all. The problem then is to make $\sum_i \Sigma_{ii}\left( \alpha\sqrt{1-\alpha^2}u_i v_i+\alpha^2(v_i^2-u_i^2)\right)$ large. Ignoring $O(\alpha^3)$ terms, this is $\sum_i \Sigma_{ii}\left(\alpha u_i v_i +\alpha^2 (v_i^2-u_i^2)\right)$. One attempt to show this can be made large would be to just pick unit vectors $u\in U$ and $v\in U^\perp$ independently at random. The expected value of this is then $\sum_i \Sigma_{ii} (\alpha\mathbb{E}[u_i]\mathbb{E}[v_i]+\alpha^2\left( \mathbb{E}[v_i^2]-\mathbb{E}[u_i^2]\right))$. The first term is $0$ since the domain is symmetric under reflection around $0$; one can see e.g. by replacing sampling a single unit vector by sampling a basis that $\mathbb{E}[u_i^2]=\frac{1}{d}(1-\epsilon_i) \frac{d}{m}=\frac{1-\epsilon_i}{m}$; similarly, $\mathbb{E}[v_i^2]=\frac{1}{m-d}\left(1-(1-\epsilon_i) \frac{d}{m}\right)=\frac{1}{m-d}\left(\frac{m-d}{m}+\epsilon_i \frac{d}{m}\right)=\frac{1+\epsilon_i \frac{d}{m-d}}{m}$. Thus, the expected value is $$\alpha^2 \sum_i \Sigma_{ii}\left(\frac{1+\epsilon_i \frac{d}{m-d}}{m}-\frac{1-\epsilon_i}{m}\right)=\alpha^2\sum_i \Sigma_{ii}\frac{\epsilon_i}{m} \left(1+\frac{d}{m-d}\right)=\alpha^2\left(1+\frac{d}{m-d}\right)\frac{\sum_i |\epsilon_i|}{m}.$$
This has size like $\alpha^2 \varepsilon$, for a squared change of size $\alpha^2$. Even if the squared changes were to add, this would give $\varepsilon d$ progress only after changing by $d$, which is insufficient. Can we fix this? I guess we should really be able to make much faster progress. If $U$ contains a vector $u$ supported just on its big coordinates and $U^\perp$ contains a vector $v$ supported just on its big coordinates, then we can make $\Theta(\alpha^2)$ progress here with the quadratic term, so we are happy.

## just maximizing the quadratic function?

For any fixed $\alpha$, I guess maybe we can just say something about the maximum of the quadratic function $q(u,v)=\sum_i \Sigma_{ii}\left(\alpha u_i v_i +\alpha^2 (v_i^2-u_i^2)\right)$? 
$$\frac{\partial q}{\partial u_i} = \Sigma_{ii}(\alpha v_i-2\alpha^2u_i)$$
$$\frac{\partial q}{\partial v_i} = \Sigma_{ii}(\alpha u_i+2\alpha^2v_i)$$
The constraints are $g_1(u,v)=\lVert u\rVert^2=1$ and $g_2(u,v)=\lVert v\rVert^2=1$, with gradients $\frac{\partial g_1}{\partial u_i}=2u_i$ and $\frac{\partial g_2}{\partial v_i}=2v_i$. The lagrange multiplier thm says that at an optimum, we have $\nabla q = \lambda_1 \nabla g_1 +\lambda_2 \nabla g_2$, which is the following system of equations:
$$\frac{\partial q}{\partial u_i}=\lambda_1 \frac{\partial g_1}{\partial u_i},\quad \frac{\partial q}{\partial v_i}=\lambda_2 \frac{\partial g_2}{\partial v_i}.$$
Plugging stuff in, this becomes
$$\Sigma_{ii}(\alpha v_i-2\alpha^2u_i)=\lambda_1 2u_i,\quad \Sigma_{ii}(\alpha u_i+2\alpha^2v_i)=\lambda_2 2 v_i.$$
In matrix form and letting $2\lambda_1/\alpha=\lambda_u$ and $2\lambda_2/\alpha=\lambda_v$, this becomes
$$\Sigma (v-2\alpha u)=\lambda_u u,\quad\Sigma(u+2\alpha v)=\lambda_v v.$$
### a correct version — oops re prev

We forgot to require $u\in U$ and $v\in U^\perp$. Let's do this again, this time with $u=Ub$ and $v=U^\perp c$. Now we are maximizing $f(b,c)=q(Ub,U^\perp c)=\sum_i \Sigma_{ii}\left(\alpha (U_i\cdot b)((U^\perp)_i \cdot c)  +\alpha^2 (((U^\perp)_i \cdot c)^2-(U_i\cdot b)^2)\right)$. The partials are now

$$\frac{\partial f}{\partial b_j} = \sum_i \Sigma_{ii}(\alpha U_{ij}((U^\perp)_i\cdot c) -2\alpha^2(U_i\cdot b) U_{ij}b_j),\quad \frac{\partial f}{\partial c_i} = \sum_i \Sigma_{ii}(\alpha (U_i\cdot b) U^\perp_{ij}+2\alpha^2((U^\perp)_i\cdot c) U^\perp_{ij}c_j).$$

The constraints are $h_1(b,c)=\lVert b\rVert^2=1$ and $h_2(b,c)=\lVert c\rVert^2=1$, with gradients $\frac{\partial h_1}{\partial b_i}=2b_i$ and $\frac{\partial h_2}{\partial c_i}=2c_i$. The lagrange multiplier thm says that at an optimum, we have $\nabla q = \lambda_1 \nabla g_1 +\lambda_2 \nabla g_2$, which is the following system of equations: $$\frac{\partial f}{\partial b_i}=\lambda_1 \frac{\partial h_1}{\partial b_i},\quad \frac{\partial f}{\partial c_i}=\lambda_2 \frac{\partial h_2}{\partial c_i}.$$
Plugging stuff in, this becomes (paused here — seems messy)
$$\Sigma_{ii}(\alpha v_i-2\alpha^2u_i)=\lambda_1 2u_i,\quad \Sigma_{ii}(\alpha u_i+2\alpha^2v_i)=\lambda_2 2 v_i.$$
## trying again with $u\in U$ and $v\in U^\perp$ as constraints

The above seems to become messy. Let's see if having $u\in U$ and $v\in U^\perp$ as constraints seems any nicer. We can do this by picking a basis $e_1,\ldots,e_d$ for $U$ and a basis $f_1,\ldots, f_{m-d}$ for $U^\perp$, and having $d$ respective orthogonality constraints on $v$ (i.e., $e_i\cdot v=0$) and $m-d$ respective orthogonality constraints on $u$ (i.e., $f_j\cdot u=0$). (The respective gradients of these constraints are just $e_i$ and $f_j$.) Assigning these constraints the lagrange multipliers $\eta_1,\ldots,\eta_d$ and $\phi_1,\ldots,\phi_{m-d}$, the new lagrange multiplier equations are as follows:

## trying again intuitively

I now see I can do this by just thinking geometrically about the feasible surface lol. We need the gradient of the objective function to be in a direction off the surface, so the equations are just
$$\Sigma (v-2\alpha u)-\lambda_u u\in U^\perp,\quad\Sigma(u+2\alpha v)-\lambda_v v\in U$$
And we also have the norm constraints, and that $u\in U$ and $v\in U^\perp$ — but that's it. One can write the above also as follows:
$$(I-UU^T)\Sigma (v-2\alpha u)=\lambda_u u,\quad UU^T\Sigma(u+2\alpha v)=\lambda_v v$$
## with a running error corrected

I think the above should really be 
$$\Sigma (v-\alpha u)-\lambda_u u\in U^\perp,\quad\Sigma(u+\alpha v)-\lambda_v v\in U$$
maybe it's nicest as follows:
$$\Sigma (v-\alpha u)\in U^\perp\oplus \{\lambda u\},\quad\Sigma(u+\alpha v)\in U\oplus \{\lambda v\}$$
What does this tell us about $\Sigma u$ and $\Sigma v$? Well, a linear combo of these two vectors needs to be in $U^\perp\oplus \{\lambda u\}$, and another linear combo needs to be in $U\oplus \{\lambda v\}$

also, the corrected objective function is $q(u,v)=\sum_i \Sigma_{ii}\left(2\alpha u_i v_i +\alpha^2 (v_i^2-u_i^2)\right)=2\alpha v^T \Sigma u + \alpha^2 \sum_i \Sigma_{ii}(v_i^2-u_i^2)=2\alpha v^T \Sigma u + \alpha^2 (\Sigma(v-u))\cdot(v+u)$ 

## split into cases

Ok, perhaps we can say that we can either make $2\alpha v^T \Sigma u$ large, or if we can't, we can make $\sum_i \Sigma_{ii}(v_i^2-u_i^2)$ large? The former can be done when $\Sigma u$ has a large component in $U^\perp$ for some unit vector $u\in U$. What if that's not the case for any $u\in U$? Then $\Sigma$ maps all unit vectors in $U$ to close to $U$. Let's consider again the simpler case in which $\Sigma U \subseteq U$. For a typical $U$, we would get that $\dim \Sigma U$ is the minimum of $\dim U=d$ and $s+b$, where $s$ and $b$ are the numbers of coordinates which are too small or too big, respectively. Consider the case $s+b\geq d$; with things being generic, we then have $\dim \Sigma U = d = \dim U$. But this is a contradiction: $\Sigma U$ has no mass at all on the already-fixed coordinates, so since the dimensions match, neither does $U$, in contradiction with it having $(m-(s+b))\frac{d}{m}=d\left(1-\frac{s+b}{m}\right)$ squared mass on these coordinates. Indeed, since $U$ must have $d(1-\frac{s+b}{m})$ squared mass on these coordinates, it must be the case that $\dim \Sigma U\leq d\left(1-\frac{s+b}{m}\right)$. 


## another progress measure

Do we maybe want a different progress measure that handles getting close to the right mass more gracefully? One natural option is to square distances from the right mass, another is to square squared distances to the right squared mass, another is the tight frame potential
## messier

What happens in general if we rotate between two vectors $u,v$ which have certain coordinates set to $0$? Only the projections of vecs to the plane defined by these $u,v$ will be changing, so vecs will maintain whatever they had on the coords set to $0$. This suggests that we can maybe just carry out rotations like that instead? Concretely, when good vectors are found above, maybe the rotation between these vectors but with the already-fixed coords set to $0$ also makes reasonable progress? One issue is that we will then generally need to track two vectors being rotated, not just $1$, and I guess that $u$ itself won't generally be one of these two?


