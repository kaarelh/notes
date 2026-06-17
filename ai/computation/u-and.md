
k^2

so suppose x per neuron, then dot prods are 1/sqrt(d_0), so noise is sqrt(x)/sqrt(d_0) per neuron, and in total it is sqrt(r)sqrt(x)/sqrt(d_0)=r gives x / d_0 = r gives x = r d_0
signal is r

so can do r d_0 inputs per neuron, if sqrt(r)/sqrt(d) probability, then m features gives m d sqrt(r)/sqrt(d) total edges needed, so r d_0 d = m d sqrt(r)/sqrt(d), so m =  sqrt(r) d_0  sqrt(d) is max possible 



log6 d_0 / sqrt(d) is mu

as long as at least 2 mu, prob is e^{-size} because mu delta is neg size 

so then log^2 d_0 needs to be at least 2mu which gives log6 d_0 / sqrt(d) <= log^2 d_0 
d_0 at least log8 d_0

**

out by the noise will require $\epsilon < 1/k$ if the noise is correlated, and $\epsilon < 1/k^2$ if the noise is uncorrelated. In other words, noise reduction matters!

r neuron intersection

each gets r^2 d_0 then each dot prod is 1/sqrt(d_0) so adding r^2 d_0 of these gives about r noise per neuron, adding gives r^{3/2}
  

#### Aren’t the ANDs already kinda nonlinearly represented?

  

While one cannot read off the ANDs linearly before the ReLU, except with a large error, one could certainly read them off with a more expressive model class on the activations. In particular

**


**


A consequence of the precise (up to $\epsilon$) nature of our universal AND is the existence of a universal XOR. In the work [cite Sam Marks], it is observed that real-life transformers universally linearly compute XOR of features in the weak sense of being able to read off tokens where XOR of two tokens is true using a linear probe (not necessarily with $\epsilon$ accuracy). As we saw above, this weak readoff behavior for AND would be unsurprising, as the residual stream already has this property (using $x_i + x_j$ which has maximal value if and only if $x_i$ and $x_j$ are both present). However, as Sam Marks observes in loc. cit., it is not possible to read off XOR in this weak way from the residual stream. We can however see that such a universal XOR (indeed, in the strong sense) can be constructed from our strong (i.e., boolean up to $\epsilon$) universal AND. Indeed, assume that we have expanded the residual stream to include both the feature vectors $x_i$ and, in an orthogonal subspace, another space that contains universal AND vectors $x_i \text{ AND }x_j$. We assume that we have applied the universal AND nonlinearity along the second component, and the identity map along the first. Then we can weakly read off XOR from this space by taking the dot product with the vector 

$\text{XOR}^{weak}_{i,j}: = x_i+x_j\oplus - 2 (x_i \text{ AND } x_j).$ Then we see that if we had started with the two-hot pair $x_{i’} + x_{j’},$ the result of this readoff will be, up to a small error $O(\epsilon),$ 

$$\begin{cases}

0 = 0-0, & |\{i,j\}\cap \{i’, j’\}| = 0\text{ (neither coefficient agrees)}\\

1 = 1-0, & |\{i,j\}\cap \{i’, j’\}| = 1\text{ (one coefficient agrees)}\\

0 = 2-2, & \{i, j\} = \{i’, j’\}\text{ (both coefficients agree)}.

\end{cases}.$$

**

**

- Come up with a better algorithm for ands of various valences than assigning a unique valence to each group of neurons.

**



## The U-AND

We begin by introducing a simple and central component in our framework, which we call the U-AND, short for a *universal AND component*. We introduce the problem this component solves and our solution to this problem; we will later discuss a few generalizations; in particular, extending it to work with inputs in superposition. 

Intuitively, our universal AND takes as input a sparse boolean string of length $n_0$ and computes all of the $\binom{n_0}{2}$ pairwise ANDs of pairs of bits of this string only using $n_0$ neurons, with the output features being almost orthogonal, in sparse superposition. It computes them in the sense that each is now represented linearly: for each pair of input features, there is an affine (in fact, linear) function from post-ReLU activations to $\mathbb{R}$ that is roughly $0$ or roughly $1$ depending on whether the AND of these two inputs is not present or present. 

The 2-valence boolean universal AND problem: Fix a small parameter $\epsilon$. Let $e_1,\ldots,e_{n_0}\in \mathbb{R}^{n_0}$ be the standard basis. Inputs are all at most *$k$-composite* vectors, i.e., for each index set $I\subseteq [n_0]$ with $|I|\leq k$, we have the input $x_I=\sum_{i\in I} \vec{e}_i\in \mathbb{R}^{n_0}$ — we think of such an input as encoding the corresponding binary string. Our goal is to compute all $\binom{n_0}{2}$ pairwise ANDs of input bits (possibly in superposition). More precisely, we want to perform a computation on the input $x_I$ that produces a representation vector $a_I=f(x_I)\in \mathbb{R}^n$ such that for any pairwise AND, there is a linear functiona

### Other fan-ins



If one would like to 

### 

### A version with inputs in superposition

Consider the bipartite graph $B$ between the features $f_1,f_2,\ldots, f_m$ before the MLP and the $d$ neurons of the MLP, i.e. the graph that contains information about which MLP neurons care about which input features. In U-AND, this is a random bipartite graph with each edge present independently with probability $p=\frac{\log d}{\sqrt{d}}$. In the case without superposition, i.e. where $n_0$, the dimension of the input space, is $m$, the $n\times m$ adjacency matrix $A_B$ of this graph is just the weight matrix, but what we're about to discuss is mostly interesting if the input features are a sparse overcomplete basis. In this general superposed case, we define the $i$th row of the corresponding actual $n\times n_0$ weight matrix $W$ to be the linear combination of $f_j$ with coefficients given in row $i$ of $M$. In other words, letting $F$ be the $m\times n_0$ matrix with the features $f_1,\ldots,f_m$ as its rows, we let $W=A_BF$. We'll restrict to the case where each entry of $A_B$ is $0/1$ and the bias vector has all coordinates $-1$ throughout this discussion, mostly because this is easier to think about and we don't know any construction that doesn't have this form which is better in some interesting way than one that does. And by the density of $A_B$, we will mean the (expected) fraction of entries which are $1$.




## A targeted superpositional AND

Consider the bipartite graph $B$ between the features $f_1,f_2,\ldots, f_m$ before the MLP and the $d$ neurons of the MLP, i.e. the graph that contains information about which MLP neurons care about which input features. In U-AND, this is a random bipartite graph with each edge present independently with probability $p=\frac{\log d}{\sqrt{d}}$. In the case without superposition, i.e. where $n_0$, the dimension of the input space, is $m$, the $n\times m$ adjacency matrix $A_B$ of this graph is just the weight matrix, but what we're about to discuss is mostly interesting if the input features are a sparse overcomplete basis. In this general superposed case, we define the $i$th row of the corresponding actual $n\times n_0$ weight matrix $W$ to be the linear combination of $f_j$ with coefficients given in row $i$ of $M$. In other words, letting $F$ be the $m\times n_0$ matrix with the features $f_1,\ldots,f_m$ as its rows, we let $W=A_BF$. We'll restrict to the case where each entry of $A_B$ is $0/1$ and the bias vector has all coordinates $-1$ throughout this discussion, mostly because this is easier to think about and we don't know any construction that doesn't have this form which is better in some interesting way than one that does. And by the density of $A_B$, we will mean the (expected) fraction of entries which are $1$.

At least for the universal AND and other similar constructions (more on these below), out of the $m$ entries in a row of $A_B$, only $o(n_0)$ should be $1$ — each neuron can only care about at most $n_0$ features. The reason for this is that the noise overtakes the signal around having to read off $n_0$ vectors in $\mathbb{R}^{n_0}$. If this is true, U-AND can't be done with more than $m=n_0 n^{1/2}$ features. That said, we're not completely sure there isn't any modification of the construction that bypasses this. But e.g. one can't just naively make it sparser — $p$ can't be taken below $n^{-1/2}$. Here, we give a way to compute ANDs of some particular $n_0 n$ feature pairs without computing all ANDs that works for any $m$. (While this appears worse than U-AND in the regime in which U-AND works, it is actually not because the construction below also solves the U-AND task in that regime. There might be a way to interpolate between U-AND and this construction (?).)

In U-AND, we take $A_B$ to be a random matrix with iid 0/1 entries with probability $p=\frac{\log n}{\sqrt{n}}$. If we only need/want to compute a subset of all the pairwise ANDs — let $E$ be this set of all pairs of inputs $\{i,j\}$ for which we want to compute the AND of $i$ and $j$ — then whenever $\{i,j\}\in E$, we might want each pair of corresponding entries in the corresponding columns $i$ and $j$ of the adjacency matrix $A_B$, i.e., each pair $\left(A_B\right)\_{ki}$, $\left(A_B\right)\_{kj}$ to be a bit more correlated than an analogous pair in column $i'$ and $j'$ with $\{i',j'\}\not\in E$. Or more precisely, we want to make such pairs of columns $\{i,j\}$ have a surprisingly large intersection for the general density of the matrix — this is to make sure that we get some neurons to read off the AND of $\{i,j\}$ from without crossing the density threshold at which a neuron needs to care about too many input features.

One way to do this is to pick a uniformly random set of $\log^2 n$ neurons for each $\{i,j\}\in E$, and to set the column of $A_B$ corresponding to input $i$ to be the indicator vector of the union of these sets. This way, we can compute up to around $|E|=n_0 n$ pairwise ANDs without having any neuron care about more than $n_0$ input features.

(I've ignored $\log$ factors.)

To say a bit more about the interpolation between the universal AND and this: I think that e.g. if one is in the gate sparsity regime where there are triangles in $E$, one might want to introduce some 3-way correlations, maybe sth like whenever $E$ has a triangle $ijk$, we pick a random set of neurons at which columns $i,j,k$ of $A_B$ have unusually high density. Maybe there's some universally good construction like this which has a contribution for every (maximal?) clique in the gate graph E. And then maybe the universal AND is the special case where the entire gate graph is just one big clique, and the construction I give above is the special case where the gate graph is really sparse (specifically, has basically no triangles).


### Extending the targeted superpositional AND to other valences

Here's a fairly straightforward extension of the AND to other valences, again doing all valences on a common set of neurons. Instead of picking a set for each pair that we need to AND as above, we now pick a set for each larger AND gate that we care about. As in the previous sparse U-AND, each input feature gets sent to the union of the sets for its gates, but this time we make the weights depend on the valence. Letting $k$ denote the max valence over all gates, for a valence $\ell$ gate, we set the weight from each input to $k/\ell$, and set the bias to $-k+1$. This way, still with at most about $n^2$ gates, and at least assuming inputs have at most some constant number of features active, we can read the output of a gate off with the indicator vector of its set.





The goal is to compute 

We consider a 1 layer neural network $f(x) = W_\text{out} \text{ReLU}(W_\text{in} x + b)$ with $n_0$-dimensional input, $n$-dimensional hidden layer, and $\binom{n_0}{2}$-dimensional output. Inputs are all at most *$k$-composite* vectors, i.e., for each index set $I\subseteq [n_0]$ with $|I|\leq k$, we have the input $x_I=\sum_{i\in I} \vec{e}_i\in \mathbb{R}^{n_0}$ — we think of such an input as encoding a sparse binary string — and the corresponding output 

and we look for a choice of parameters such that the model outputs a unique one-hot vector $\binom{d}{2}$ for each unique pair, up to an error of $\epsilon$ in each coordinate, such that we can interpret each component of the output as a feature which is 1 if the AND of a particular set of two input features is present. In other words, outputs are indexed by (unordered) pairs $(i, j)$ in $\{d\}$ (the set $\{0,\dots, n-1\}$ with d elements) and each computes the AND of the two indices. 


The 2-valence boolean universal AND problem: Fix a small parameter $\epsilon$. Let $d$ be an integer, which we assume large compared to $1/\epsilon$. Let $e_1,\ldots,e_d$ be the set of vectors with a 1 in the $i$th coordinate and 0 everywhere else (i.e. the set of all 1-hot vectors). We consider a 1 layer neural network $f(x) = W_\text{out} \text{ReLU}(W_\text{in} x + b)$ with $d$-dimensional input, $d_{MLP}$ dimensional hidden layer, and $\binom{d}{2}$-dimensional output. Inputs are all 2-hot vectors $\vec{e}_i + \vec{e}_j$ with $(i\neq j)$ in d-dimensional space and we look for a choice of parameters such that the model outputs a unique one-hot vector $\binom{d}{2}$ for each unique pair, up to an error of $\epsilon$ in each coordinate, such that we can interpret each component of the output as a feature which is 1 if the AND of a particular set of two input features is present. In other words, outputs are indexed by (unordered) pairs $(i, j)$ in $\{d\}$ (the set $\{0,\dots, n-1\}$ with d elements) and each computes the AND of the two indices. 