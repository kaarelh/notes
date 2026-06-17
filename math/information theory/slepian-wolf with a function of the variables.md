
I have another conjecture for Slepian-Wolf with latents. It is motivated by our discussion that for the XOR of two correlated coins, bucketing schemas don't give decent recovery of the XOR because the function would need to have some 'product structure' (it'd need to be roughly constant on the product set given by two buckets), but XOR doesn't have that.

To recall the setup: we have latents $Y_1,\ldots,Y_k$ and an observable $X=f(Y_1,\ldots,Y_k)$; we want to do coding on a batch of $n$ samples, wishing to encode each sequence $Y_i^n$ without seeing the other ones, and being able to recover $X^n$ from these encodings (with the expected number of errors being $o(n)$, I guess). I won't require $Y_1,\ldots,Y_k$ to be independent, but I will require their distribution to have full support on the product of the individual domains (I think this is mostly to avoid a not-very-interesting complication).

Definition. Say values $y_1$ and $y_2$ in the domain of $Y_i$ are '$f$-equivalent' if the output of $f$ is unchanged when switching input $i$ from $y_1$ to $y_2$ (at any point in the domain where input $i$ is $y_1$). This is an equivalence relation on the domain of $Y_i$. Define the random variable $Y_i'$ to be $Y_i$ quotiented by this equivalence relation. The given probability distribution on $Y_1,\ldots,Y_k$ transfers to a probability distribution on $Y_1',\ldots,Y_k'$. Also, we can view $f$ as a function on this quotient.

Remark. There is obviously a coding schema with rates $r_i=H(Y_i')$: just encode each $Y_i'^n$ perfectly, and compute the value of $f$ from these values.

Conjecture. In fact, any coding schema (where the expected number of errors is $o(n)$) has $r_i\geq H(Y_i')$. So the above is best possible.

(This conjecture would roughly imply that for a generic $f$, one can't do better than just encoding the latents in full.)

EDIT: Nvm I think this conjecture is false, with the XOR of two correlated coins just being a counterexample lol (eg if you encode one coin precisely, you can get away with encoding the other one imprecisely with a random bucketing, because you can still recover the other coin from that with high probability just by picking the sequence in the bucket which is closest to the sequence from the known coin). It could still be true if the $Y_i$ are independent afaik. Maybe an interesting particular case here is: Y_1 and Y_2 are independent fair coins, and X is their minimum. More generally than just claiming the above when $Y_i'$ are independent, we could hypothesize:
Conjecture'. The rates need to satisfy the Slepian-Wolf conditions for $Y_i'$. (E.g., $r_i$ should be at least $H(Y_i'|Y_1',\ldots,Y_{i-1}',Y_{i+1}',\ldots,Y_k')$.)


can we construct a counterexample to the new one also? i guess we'd need to create bucket pairs which somehow don't pin down the pair of sequences but do pin down the value of the function. this means that any pair of things that ends up on the pair of buckets has the same value of the function. for the XOR example, we'd need to flip both bits at some locations