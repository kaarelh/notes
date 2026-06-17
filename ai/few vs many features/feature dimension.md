https://via.hypothes.is/https://arxiv.org/pdf/2210.01892.pdf
Lemma. Given a set of vectors $v_1,\ldots, v_m\in \R^n$, and defining $C_i=\frac{\left(v_i \cdot v_i\right)^2}{\sum_j \left(v_i \cdot v_j\right)^2}$, we have $\sum_i C_i\leq n$. 

Proof. By CS, we have $\sum_i \frac{\left(v_i \cdot v_i\right)^2}{\sum_j \left(v_i \cdot v_j\right)^2}\leq \sqrt{\sum_i (v_i\cdot v_i)^2 \sum_i \frac{1}{\sum_j (v_i\cdot v_j)^2}}$  

Assuming $v_i$ has unit norm, we have
$\sum_j (v_i\cdot v_j)^2\geq \left(\sum_j |v_i \cdot v_j| \right)^2/n\geq \sum_{i,j}$  


Consider the matrix $A$ with entries given by $A_{ij}=\frac{(v_i \cdot v_j)^2}{\sum_j (v_i\cdot v_j)^2}$  oops does not make sense


How robust are these conclusions to the setup? Can we say something much more generally theoretically about when features get put in superposition? Or maybe just heuristically? I think there is room for a good heuristic model of which features get represented. This could be supplemented by an empirical investigation that looks at many variants of toy models and tries to search for commonalities between them, which are then used to motivate conjectures (and the conjectures are then hopefully either proven or at least heuristically justified).

In particular, can we understand the tradeoffs between having structured configurations (that is, configurations which can be split among small orthogonal subspaces) vs random constructions (which is more like the picture that goes with the Johnson-Lindenstrauss lemma)?

In general, I think the setup in the paper roughly just captures features which are superpositional in the sense of Olah's essay, even though certain features end up being put on directions orthogonal to every other feature. This is because at the end of the day, it is about recovering something simple defined in terms of the initial features. Can we come up with (and study) a toy model where composition and superposition show up together in a more meaningful way?

It would be nice to move to some models which feel less toy than this, but are still much simpler than practical models. For instance, can we completely understand how computation in superposition works for the task from section 3.1 of https://arxiv.org/pdf/2303.13506.pdf?

