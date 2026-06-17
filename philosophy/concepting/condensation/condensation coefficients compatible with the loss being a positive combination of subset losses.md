
* the loss for a subset I is the sum of lengths of strings at subsets J which intersect I
* we will be interested in figuring out which expanded sum coeffs can come as positive linear combinations of these subset losses
* for now, we will be interested in only ones which are symmetric under permutations of indices (even though maybe this is wrong for images? like, it's not like 5 adjacent pixels are obviously the same wrt each other as 5 random pixels. like, maybe you'd prefer to have information at more convex or connected sets?)
	* since we are dealing with $\mathbb{R}^{2^n-1}$ in which we have $2^n-1$ linearly independent vectors (the subset losses), coefficients of these can be uniquely read off from a vector. a vector which is symmetric gives the same coeff for any subset of the same size by its symmetry. so to get a symmetric vector, we must be assigning the same coefficient to every basis element at the same subset size level. the converse is obvious as well. so equivalently we are asking which vectors can be made as symmetric positive linear combinations of the basis
* let's first understand what the elementary symmetric positive linear combinations are, ie the n vectors which are obtained by symmetrizing subset loss vectors for subsets of size k= 1,2,...,n. since the result is symmetric, it suffices to understand what coeff we get at some specific subset of size $\ell$. this will be the number of subsets of size $k$ which intersect that subset of size $\ell$, or after normalizing by the total number of subsets of size $k$, it will just be the probability a random subset of size $k$ intersects that subset of size $\ell$, which is $1-\frac{(n-\ell)\cdots (n-\ell-k+1)}{n\cdots (n-k+1)}=1-\frac{(n-\ell)!(n-k)!}{n!(n-\ell-k)!}$. ok actually it's easier to think without doing this normalization: the intersecting subsets of size k are just all the size k subsets minus those which are contained in the complement, so that's $\binom{n}{k}-\binom{n-\ell}{k}$. 
* so for each k, we have this known vector with index \ell. what are the positive linear combinations of these guys? letting A be the matrix with these as columns (so $k$ is the column index and $\ell$ is the row index), we have $x = A c$, and then the positivity condition on x is $A^{-1} x \geq 0$ (this works only because we are in the case where there are n-1 linearly independent vectors as the spanning set of the cone in n-1 dim space). so finding the right inequalities on x reduces to inverting this matrix with entries $A_{\ell,k}$.
* [chatgpt says](https://chatgpt.com/share/69d7502d-55d0-8397-8290-51176146bc53) the inverse is given by $(A^{-1})_{ij}=(-1)^{n-j+i}\left(\binom{n}{j}-\binom{i}{n-j}\right)$. i haven't checked it but i think it's probably right. so coefficient vec $x_j$ with $j$ being the subset size is feasible as a non-negative linear combination of these subset losses if and only if $A^{-1} x \geq 0$

chatgpt continues from here to the conclusion that the only scale-free loss that can be written this way has the exponent alpha = 1: https://chatgpt.com/share/69d7502d-55d0-8397-8290-51176146bc53


# msg about this

on condensation loss coefficients again, one can ask:
* If we assume the loss has to be a positive linear combination of simple scores for subsets which is symmetric, what can the coefficients in the expanded-out form be?

Here, "symmetric" means that the expanded-out loss coefficients are preserved under permuting ground variable indices, or equivalently that every subset of the same size gets the same coefficient in the expanded-out sum, or equivalently that every subset of the same size gets the same coefficient before expanding out.

Once one has answered this, one can ask:
* Which scale-free losses can be written this way?

If my combinatorics followed by some binomial coefficient math by chatgpt is to be trusted, then the answer is that the only solution is to have the scaling exponent be alpha = 1. (I'd give like 80% that this conclusion is correct; maybe I'll spend more time on this later if I get more reason to think that this claim is important/interesting.) But this is just the sum of single pixel scores, which is optimized by putting all the information in the singleton latents. So if the alpha=1 conclusion is right, there is no good scale-free loss that can be written sum of subset simple scores.

However, it's not clear that a loss should be symmetric under permuting the ground variables (when we're dealing with pictures, there's a difference between eg 4 pixels that form a 2x2 square and 4 arbitrary pixels), and it is also not clear that a loss should be a positive linear combination of scores for reconstructing subsets. (It's also not obvious that a loss should be scale-free.)
