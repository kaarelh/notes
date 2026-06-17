
For each $x\in X$, we consider the (column) vectors $u=u_x=W^T D\left(\frac{f^{\ell+1}(x)}{p^{\ell+1}(x)}\right)f^{\ell+1}(x)\in \mathbb{R}^n$  and $v=v_x=f^{\ell}(x)\in\mathbb{R}^n$, where $n=n_\ell$ is the number of neurons in layer $\ell$. Consider the matrix $$A=uv^T+vu^T=(||u||||v||+ u^T v)\frac{\left(||u|| v+ ||v|| u\right)\left(||u|| v+ ||v|| u\right)^T}{||\left(||u|| v+ ||v|| u\right)||^2}-(||u||||v||- u^T v)\frac{\left(||u|| v- ||v|| u\right)\left(||u|| v- ||v|| u\right)^T}{||\left(||u|| v- ||v|| u\right)||^2}.$$

(The decomposition was found by thinking about eigenvectors as shown below, though I am guessing that it can also just be checked directly.)

Note that $||\left(||u|| v+ ||v|| u\right)||^2= 2||u||^2 ||v||^2+2||u||||v||u^T v$ and $||\left(||u|| v- ||v|| u\right)||^2= 2||u||^2 ||v||^2-2||u||||v||u^T v$, so after canceling terms, we just get
$$\frac{\left(||u|| v+ ||v|| u\right)\left(||u|| v+ ||v|| u\right)^T}{2||u||||v||}-\frac{\left(||u|| v- ||v|| u\right)\left(||u|| v- ||v|| u\right)^T}{2||u||||v||}$$

We can ignore the factor of $2$ because that does not change the final optimization problem, and we can also make everything have unit norm by dividing the numerator by $||u||^2||v||^2$ and bringing a common factor of $||u||||v||$ to the front, giving $$||u||||v||\left(\left(\frac{v}{||v||}+\frac{u}{||u||}\right)\left(\frac{v}{||v||}+\frac{u}{||u||}\right)^T-\left(\frac{v}{||v||}-\frac{u}{||u||}\right)\left(\frac{v}{||v||}-\frac{u}{||u||}\right)^T\right)$$
The original optimization problem finds a direction along which $u$ and $v$ are maximally correlated.

Consider $w^T u v^T w$. This is the thing whose sum over $x$ we are maximizing. Note that this is equal to $\left((DWw)\cdot f^{\ell+1}(x)\right) \left(f^\ell(x) \cdot w\right)$, so we are looking for a direction $w$ such that there is high covariance between the angle between it and the activations in layer $\ell$ and the angle between activations caused by it in layer $\ell+1$ and the activations in layer $\ell+1$. 



Note that $A$ has rank $2$ (since every column is a linear combination of $u$ and $v$), so it has $n-2$ eigenvalues which are $0$. Further note that the two vectors $v_{\pm}=||u||v\pm ||v||u$ are [also](https://math.stackexchange.com/a/3173653) eigenvectors of $A$, because $$Av_\pm = uv^T (||u|| v\pm ||v|| u) +vu^T(||u|| v\pm ||v|| u)=\left(||u|| ||v||^2 u\pm ||v|| (v^T u) u\right)+ \left(u^T v ||u|| v\pm ||v||||u||^2 v\right)$$
$$=(||u||||v||\pm v^T u)||v||u+ (u^Tv\pm ||u||||v||)||u||v=(u^T v\pm ||u||||v||)v_\pm.$$
We observe that $v_\pm$ are also eigenvectors of $A$, different as long as the set $\{u,v\}$ is not linearly dependent, and with distinct eigenvalues as long as $u,v$ are not orthogonal. If $\{u,v\}$ is linearly dependent, then the matrix has rank $1$ and the only eigenvector with nonzero eigenvalue is just $u=v$. If they are not linearly dependent, then $v_\pm$ are exactly the two nonzero eigenvectors.  