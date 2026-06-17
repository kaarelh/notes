
# The Deep Neural Feature Ansatz

@misc{radhakrishnan2023mechanism,
      title={Mechanism of feature learning in deep fully connected networks and kernel machines that recursively learn features}, 
      author={Adityanarayanan Radhakrishnan and Daniel Beaglehole and Parthe Pandit and Mikhail Belkin},
      year={2023},
      url = { https://arxiv.org/pdf/2212.13881.pdf }
}

Let $h_i(x)\in \mathbb{R}^k$ denote the activation vector in layer $i$ on input $x\in\mathbb{R}^d$, with the input layer being at index $i=1$, so $h_1(x)=x$. Let $W_i$ be the weight matrix after activation layer $i$. Let $f_i$ be the function that maps from the $i$th activation layer to the output. Then their *Deep Neural Feature Ansatz* says that $$W_i^T W_i\underset{\sim}{\propto} \frac{1}{|\dataset|}\sum_{x\in \dataset}\nabla f_i (h_i(x))\nabla f_i (h_i(x))^T$$
(I'm somewhat confused here about them not mentioning the loss function at all — are they claiming this is reasonable for any reasonable loss function? Maybe just MSE? MSE seems to be the only loss function mentioned in the paper; I think they leave the loss unspecified in a bunch of places though.)

## A singular vector version of the ansatz

Letting $W_i=U \Sigma V^T$ be a SVD of $W_i$, we let note that this is equivalent to $$V \Sigma^2 V^T\underset{\sim}{\propto} \frac{1}{|\dataset|}\sum_{x\in \dataset}\nabla f_i (h_i(x))\nabla f_i (h_i(x))^T,$$ i.e., that the eigenvectors of the matrix $M$ on the RHS are the right singular vectors. By the variational characterization of eigenvectors and eigenvalues (Courant-Fischer or whatever), this is the same as saying that right singular vectors of $W_i$ are the highest orthonormal $v^T M v$ directions for the matrix $M$ on the RHS. Plugging in the definition of $M$, this is equivalent to saying that the right singular vectors are the sequence of highest-variance directions of the data set of gradients $\nabla f_i (h_i(x))$. 

(I have assumed here that the linearity is precise, whereas really it is approximate. It's probably true though that with some assumptions, the approximate initial statement implies an approximate conclusion too? Getting approx the same vecs out probably requires some assumption about gaps in singular values being big enough, because the vecs are unstable around equality. But if we're happy getting a sequence of orthogonal vectors that gets variances which are nearly optimal, we should also be fine without this kind of assumption. (This is guessing atm.))

So, I guess the claim they are making is that the directions each layer stretches the most are precisely the directions 
## Getting rid of the $W_i$ dependence on the RHS?

Assuming there isn't an off-by-one error in the paper, we can pull some $W_i$ term out of the RHS maybe? This is because applying the chain rule to the Jacobians of the transitions  $i\to i+1 \to \text{end}$ gives $\nabla f_i(h_i (x))^T=\nabla f_{i+1}(h_{i+1} (x))^T W_i$, so $$\frac{1}{|\dataset|}\sum_{x\in \dataset}\nabla f_i (h_i(x))\nabla f_i (h_i(x))^T=\frac{1}{|\dataset|}\sum_{x\in \dataset}W_i^T\nabla f_{i+1} (h_{i+1}(x))\nabla f_{i+1} (h_{i+1}(x))^T W_i.$$

Wait, so the claim is just $$W_i^T W_i \underset{\sim}{\propto} W_i^T\left(\sum_{x\in \dataset}\nabla f_{i+1} (h_{i+1}(x))\nabla f_{i+1} (h_{i+1}(x))^T\right)  W_i $$ which, assuming $W_i$ is invertible, should be the same as $\sum_{x\in \dataset}\nabla f_{i+1} (h_{i+1}(x))\nabla f_{i+1} (h_{i+1}(x))^T\underset{\sim}{\propto} I$. But also, they claim that it is $W_{i+1}^T W_{i+1}$? Are they secretly approximating everything with identity matrices?? This doesn't seem to be the case from their Figure 2 though — see below.

![[Pasted image 20240403190905.png]]
Oh oops I guess I forgot about activation functions here! There should be extra diagonal terms for jacobians of preactivations->activations in $\nabla f_i(h_i (x))^T=\nabla f_{i+1}(h_{i+1} (x))^T W_i$, i.e., it should really say $$\nabla f_i(h_i (x))^T=\nabla f_{i+1}(h_{i+1} (x))^T D_{i+1}(x) W_i.$$ We now instead get $$W_i^T W_i \underset{\sim}{\propto} W_i^T\left(\sum_{x\in \dataset}D_{i+1}(x)\nabla f_{i+1} (h_{i+1}(x))\nabla f_{i+1} (h_{i+1}(x))^TD_{i+1}(x)\right)  W_i.$$
This should be the same as $\sum_{x\in \dataset}D_{i+1}(x)\nabla f_{i+1} (h_{i+1}(x))\nabla f_{i+1} (h_{i+1}(x))^TD_{i+1}(x)\underset{\sim}{\propto} I$ which, with $p_i$ denoting preactivations in layer $i$ and $f_{p,i}$ denoting the function from these preactivations to the output, is the same as $$\sum_{x\in \dataset}\nabla f_{p,i+1} (p_{i+1}(x))\nabla f_{p,i+1} (p_{i+1}(x))^T\underset{\sim}{\propto} I.$$ This last thing also totally works without the ReLU — one can get this directly from the Jacobian calculation. I made the ReLU assumption earlier because I thought for a bit that one can get something further in that case; I no longer think this, but I won't go back and clean up the presentation atm.

Anyway, the takeaway is that the Deep Neural Feature Ansatz is equivalent to the (imo cleaner) ansatz that the set of gradients of the output wrt the pre-activations of any layer is close to being a [tight frame]() (in other words, the gradients are in [isotropic position](https://en.wikipedia.org/wiki/Isotropic_position); in other words still, the data matrix of the gradients is a constant times a [semi-orthogonal](https://en.wikipedia.org/wiki/Semi-orthogonal_matrix) matrix). (Note that the closeness one immediately gets isn't in $L^2$ to a tight frame, it's just in the quantity defining the tightness of a frame, but I'd guess that if it matters, one can also conclude some kind of closeness in $L^2$ from this ([related](https://arxiv.org/pdf/1809.04726.pdf)). This seems like a nicer fundamental condition because (1) we've intuitively canceled terms and (2) it now looks like a generic-ish condition, looks less mysterious, though idk how to argue for this beyond some handwaving about genericness, about other stuff being independent, sth like that.

proof of the tight frame claim from the previous condition: Note that $$\sum_{x\in \dataset}\nabla f_{p,i+1} (p_{i+1}(x))\nabla f_{p,i+1} (p_{i+1}(x))^T\underset{\sim}{\propto} I$$clearly implies that the $L^2$ mass in any direction is the same, but also the $L^2$ mass being the same in any direction implies the above (because then, letting the SVD of the matrix with these gradients in its columns be $U'\Sigma'V'^T$, the above is $U'\Sigma'\Sigma'^T U'^T=\sigma^2 I$, where we used the fact that $\Sigma =\sigma I$).

## Some questions

* Can one come up with some similar ansatz identity for the left singular vectors of $W_i$? One point of tension/interest here is that an ansatz identity for $W_i W_i^T$ would constrain the left singular vectors of $W_i$ together with its singular values, but the singular values are constrained already by the deep neural feature ansatz. So if there were another identity for $W_i W_i^T$ in terms of some gradients, we'd get a derived identity from equality between the singular values defined in terms of those gradients and the singular values defined in terms of the Deep Neural Feature Ansatz. Or actually, there probably won't be an interesting identity here since given the cancellation above, it now feels like nothing about $W_i$ is really pinned down by 'gradients independent of $W_i$' by the DNFA? Of course, some $W_i$-dependence remains even in the $i+1$ gradients because the preactivations at which further gradients get evaluated are somewhat $W_i$-dependent, so I guess it's not ruled out that the DNFA constrains something interesting about $W_i$? But anyway, all this seems to undermine the interestingness of the DNFA, as well as the chance of there being an interesting similar ansatz for the left singular vectors of $W_i$.
* Can one heuristically motivate that the preactivation gradients above should indeed be close to being in isotropic position? Can one use this reduction to provide simpler proofs of some of the propositions in the paper which say that the DNFA is exactly true in certain very toy cases?
* The authors claim that the DNFA is supposed to somehow elucidate feature learning (indeed, they claim it is a mechanism of feature learning?). I take 'feature learning' to mean something like which neuronal functions (from the input) are created or which functions are computed in a layer in some broader sense (maybe which things are made linearly readable?) or which directions in an activation space to amplify or maybe less precisely just the process of some internal functions (from the input to internal activations) being learned of something like that, which happens in finite networks apparently in contrast to infinitely wide networks or NTK models or something like that which I haven't yet understood? I understand that their heuristic identity on the surface connects something about a weight matrix to something about gradients, but assuming I've not made some index-off-by-one error or something, it seems to probably not really be about that at all, since the weight matrix sorta cancels out — if it's true for one $W_i$, it would maybe also be true with any other $W_i$ replacing it, so it doesn't really pin down $W_i$? (This might turn out to be false if the isotropy of preactivation gradients is only true for a very particular choice of $W_i$.) But like, ignoring that counter, I guess their point is that the directions which get stretched most by the weight matrix in a layer are the directions along which it would be the best to move locally in that activation space to affect the output? (They don't explain it this way though — maybe I'm ignorant of some other meaning having been attributed to $W_i^T W_i$ in previous literature or something.) But they say "Informally, this mechanism corresponds to the approach of progressively re-weighting features in proportion to the influence they have on the predictions.". I guess maybe this is an appropriate description of the math if they are talking about reweighting in the purely linear sense, and they take features in the input layer to be scaleless objects or something? (Like, if we take features in the input activation space to each have some associated scale, then the right singular vector identity no longer says that most influential features get stretched the most.) I wish they were much more precise here, or if there isn't a precise interesting philosophical thing to be deduced from their math, much more honest about that, much less PR-y.
  * So, in brief, instead of "informally, this mechanism corresponds to the approach of progressively re-weighting features in proportion to the influence they have on the predictions," it seems to me that what the math warrants would be sth more like "The weight matrix reweights stuff; after reweighting, the activation space is roughly isotropic wrt affecting the prediction (ansatz); so, the stuff that got the highest weight has most effect on the prediction now." I'm not that happy with this last statement either, but atm it seems much more appropriate than their claim.
  * I guess if I'm not confused about something major here (plausibly I am), one could probably add 1000 experiments (e.g. checking that the isotropic version of the ansatz indeed equally holds in a bunch of models) and write a paper responding to them. If you're reading this and this seems interesting to you, feel free to do that — I'm also probably happy to talk to you about the paper.


## typos in the paper

indexing error in the first expression: it probably should be $W_L$, not $W_{L+1}$

![[Pasted image 20240403153633.png]]



## message to jake

i think the following claim from https://arxiv.org/pdf/2212.13881.pdf is interesting and (if true) maybe relevant to RIB stuff:  
  
Deep Neural Feature Ansatz. The right singular vectors of each weight matrix W_i are approximately the sequence of orthonormal directions of highest L^2 norm in the data set (over inputs x) of gradients \nabla F_i (f_i(x)) ('top components of the gradient data set'). Here f_i(x) denotes the activation vector in layer i (just before W_i) and F_i denotes the function computing the output of the network from activations in layer i. Furthermore, the corresponding singular values of W_i are proportional to the L^2 norms in these directions of the gradient data set.  
  
The claim is from https://arxiv.org/pdf/2206.10012.pdf . I'm somewhat confused about how this could be independent of the loss or the labels.

## mess

Resolving the contradiction?
Here's a hypothesis: while ach 

For ReLUs though, the $D_i(x)$ are diagonal with 0/1 along the diagonal, and whenever there is a $0$, there is a corresponding locally const $0$ in $h_{i+1}(x)$ anyway