
If $NP=coNP$, then there is a polytime verifier for the [tautology problem](https://en.wikipedia.org/wiki/Co-NP-complete#Example), ie for telling whether $\forall x \phi(x)$ is true. if there is further a proof that this verifier works (or you know if there is any verifier which is provably a verifier), then there is a poly length proof of $\forall x \phi(x)$ — just prove the verifier works (in particular, that if there is a verification string, then the formula is true) (which has const length) and then give the verification string and conclude. conversely, if there is a poly length proof of $\forall x \phi(x)$, then NP=coNP because you can just make the verifier be a TM that checks if you've provided a proof of this! so modulo this provability thing, NP=coNP is equivalent to the claim that $\forall x \phi(x)$ has a poly length proof.

can we judge somehow if this ought to be heuristically true? 


# mess

would have a poly size proof that it is true for any $\phi(x)$ (just take the verifier for the forallsat problem and prove it works, this gives a proof). conversely, if there is such a polytime proof always then NP = coNP.

so NP vs coNP is (sort of) equivalent to: for any formula $\forall x \phi(x)$ which is true, is there a poly length proof?

