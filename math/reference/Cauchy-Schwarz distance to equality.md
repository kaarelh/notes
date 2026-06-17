
The aim of this note is to just write up a derivation I ended up doing a couple times which characterizes the distance to equality in C-S. C-S, stated in terms of vectors, says 

$u\cdot v \leq \lVert u \rVert \lVert v \rVert$ 

The distance from equality is $\lVert u\rVert \lVert v \rVert - u\cdot v$. It's a bit nicer to characterize after squaring, so let's do that. The distance between the squared values is $(1-\cos^2 \theta)\lVert u\rVert \lVert v\rVert$, where $\theta$ is the angle between $u,v$. This is $\sin^2 \theta$, which is 

We can also write this as $\left(\sum_{i} u_i v_i\right)^2 \leq \sum_i u_i^2 \sum_j v_j ^2$. 

WLOG $\lVert u \rVert = \lVert v \rVert = 1$ (just divide both sides by both norms first). Then we have

$\sum_{i} u_i v_i \leq \sum_i \frac{u_i^2+v_i^2}{2}=1$. The diff between the RHS and LHS is $\frac{1}{2}\sum_{i} (u_i-v_i)^2$. In words, non-equality in C-S is just measured by $L^2$ distance between the two vectors, as long as one has normalized first. 