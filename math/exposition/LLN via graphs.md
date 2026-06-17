
everything reduces to p=1/2 case?

first, approximate any distribution by a bunch of point masses. can couple to the point mass distribution with low prob of bounded error or something like that. so just need LLN for point masses with weights which are 1/2^k with same k for all

For LLN for discrete distribution, can split at median with first coinflip, add low, then so on. Then have finite sum of things, apply LLN to each

LLN for 1/2 follows from 

 

actually can we get chernoff bound from this? 
analogous hypergraph story

for the $k$-uniform hypergraph case, the expected density is $\frac{k!}{k^k}$, and the best possible density is if there are $n/k=\ell$ in each part (let us say $n$ is a multiple of $k$), in which case the density is $\frac{(k-1)\ell }{k\ell-1}\frac{(k-2)\ell}{k\ell -2}\cdots\frac{\ell}{k\ell-(k-1)}=\frac{k!}{k^k}\frac{(k\ell)^k}{(k\ell-1)(k\ell-2)\cdots (k\ell-(k-1))}=\frac{k!}{k^k}\frac{1}{\prod_{j=1}^{k-1}\left(1-\frac{j}{k\ell}\right)}\leq \frac{k!}{k^k} \frac{1}{1-\frac{k-1}{2\ell}}\leq \frac{k!}{k^k}\left(1+\frac{k}{2\ell}+O_{n\to\infty} \left(\frac{k^2}{\ell^2}\right)\right)=\frac{k!}{k^k}\left(1+O_{n\to \infty}\left(\frac{k^2}{n}\right)\right)$  

Taking $\frac{k!}{k^k}$ to be zero (i.e. by de-meaning), the total negative mass is thus at most $O\left(\frac{k!}{k^{k-2}n}\right)$. 

Note that if the size of one of the $k$ parts deviates by at least $x\sqrt{n/k}$ from $\frac{n}{k}$, then by concavity the density is at most (and ignoring lower-order terms) $k!\left(\frac{1}{k}+\frac{x}{\sqrt{nk}}\right)\left(\frac{1}{k}-\frac{x}{(k-1)\sqrt{nk}}\right)^{k-1}=\frac{k!}{k^k}-k!\frac{x^2}{nk}+k!\binom{k-1}{2}\frac{x^2}{(k-1)^2 nk}\leq \frac{k!}{k^k}-k!\frac{x^2}{2nk}$. It follows from our bound on the total negative mass that the probability of a deviation of $x\sqrt{n/k}$ is at most $\frac{2}{x^2k^{k-1}}$ 

(I think up to a const one has the same for the probability that the sum of sizes of all deviations is $x\sqrt{n/k}$.)
