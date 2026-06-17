
Consider the power series $1-x^2+x^4-x^8+\cdots = \sum_{i=0}^\infty (-x^2)^i$, with $x$ a real number. If $|x|\geq 1$, each term of this series has absolute value $\geq 1$, so it fails to converge. If $|x|<1$, then it's a geometric series with first term $1$ and ratio $-x^2$, thus converging to $\lim_{i\to \infty}\frac{1-x^{i+1}}{1-x}=\frac{1}{1+x^2}$. So $f(x)=\sum_{i=0}^\infty (-x^2)^i$ defines a function $f\colon (-1,1)\to \mathbb{R}$.

But wait! $x\mapsto \frac{1}{1+x^2}$ is a totally fine function $f\colon \mathbb{R}\to\mathbb{R}$. So we see that 

