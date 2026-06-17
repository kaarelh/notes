
# Realizability in neural nets (work in progress)

This post is a minisurvey discussing what functions can be computed (or approximated) by neural nets, and in particular on how this depends on the structural properties – depth, width – of the net. Other than being an interesting technical question, this also gives partial insight into why deep nets are capable (though it does not come close to explaining it fully, for reasons expanded on in the last section). The post is written for an audience that can read mathspeak, but assumes no prior familiarity with neural nets or learning theory.

## Neural nets – definitions and conventions (probably skip this if you're familiar with neural nets)

An *architecture* $N$ (of a feedforward neural net) is a directed graph $(V,E\subset V\times V)$ together with a partition of the vertex set into layers, i.e. $V=\bigsqcup_{i=0}^d L_i$ – the number $d$ is called the *depth* of the net, and $\max_{i\in \{1,2,\ldots,d-1\}} |L_i|$ is called the *width*[^1] of the net; with edges running only between consecutive layers and pointed always in the "forward direction", i.e. $E\subseteq \bigcup_{i=0}^{d-1} L_i\times L_{i+1}$.[^2] A (trained) *neural net* $(N,(w_e)_{e\in E}))$ is an architecture together with a labeling of edges with real numbers, i.e. an architecture together with a tuple $(w_e)_{e\in E})\in \mathbb{R}^E$.[^3] So one architecture corresponds to many neural nets – one for each setting of the tuple of parameters $(w_e)_{e\in E}$.

The vertices in $L_0$ are called input vertices, and the vertices in $L_d$ are output vertices. For this post, we will call the number of input vertices $n=|L_0|$, and we will assume that a neural net has exactly $1=|L_d|$ output vertex (in ML-speak, this neural net could serve as a predictor in a regression task with $n$ input features and $1$-dimensional labels). We think of this neural net as performing computation (a *forward pass*) as follows. First, put some real numbers in the $n$ input nodes (for example, with $n=256$, these could be the $16\cdot 16=256$ pixel intensity values for a single grayscale $16\times 16$ image) – we think of these as the input of the computation. Then, propagate values through the layers up to $d-1$ according to the following rule. Once we have a number $z_u\in \mathbb{R}$ written at each vertex $u\in L_i$, to compute the number $z_{v}$ to write at a vertex $v\in L_{i+1}$, take the linear combination of all the numbers at vertices on the other end of the edges into $v$, with coefficients being the weights on the edges, and send this linear combination through a univariate function $\sigma\colon \mathbb{R}\to \mathbb{R}$, called the *activation function*. Until further notice, we will take $\sigma(x)=\sigma_r(x)=\max(0,x)$, commonly called ReLU (rectified linear unit), which is one of the most common activation functions used. In maths, $$z_{v}=\sigma\left(\sum_{u\in L_{i-1} \text{ s.t. }(u,v)\in E}w_{(u,v)}z_u\right).$$

Once we do this for each vertex $v\in L_i$, we have found all the numbers to write at vertices on layer $i$. Repeat this for each layer in sequence, i.e. with $i=1,2,\ldots, d-1$. For $L_d$, take the linear combination in the same way, but don't send it through the activation function. So we finally end up with some value written at the unique vertex in $L_d$, which we think of as the output of the computation. In the sense of the computation we just defined, a neural network $N$ implements a function $f_N\colon \mathbb{R}^n \to \mathbb{R}$. Restating the topic of this survey in our newfound language: we will be discussing results about the richness of the set of functions implemented by neural nets with a given architecture, in particular examining how this richness depends on the depth and the width.

In fact, all our neural nets will have *fully connected layers*, i.e. $E=\bigcup_{i=0}^{d-1} L_i\times L_{i+1}$. Any architecture with only a subset of these edges is able to implement a subset of the functions that can be implemented in a fully connected architecture, just by copying the weights of edges which are present and setting the the rest of the weights to $0$.[^4]


## An ~explicit description of what functions can be computed by ReLU DNNs

We will start our discussion of realizability with some specifics about the functions which nets with ReLU actications can compute. The first headline will be a theorem from [Understanding Deep Neural Networks with Rectified Linear Units](https://arxiv.org/pdf/1611.01491.pdf) which says that with a little bit of depth (but an unclear amount of width), one can get any piecewise linear function (PWL). But we will need a few definitions before we get there.

>> **Definition** (Polyhedra). A polyhedron in $\mathbb{R}^\ell$ is a set of the form $\{x\in \mathbb{R}^\ell \mid Ax\leq b\}$ for some $k\times \ell$ real matrix $A$ and vector $b\in \mathbb{R}^k$. Equivalently, a polyhedron is the set of solutions to a finite list of linear non-strict inequalities. Equivalently, a polyhedron is the intersection of finitely many closed half-spaces.

>> **Lemma**. The intersection of two polyhedra is a polyhedron.

> Proof. For polyhedra $P$ and $Q$, the intersection $P\cap Q$ is the set of all points satisfying the union of the set of inequalities corresponding to $P$ and the set of inequalities corresponding to $Q$.

>> **Definition** (PWL). We say a function $f\colon \mathbb{R}^\ell\to \mathbb{R}^m$ is continuous piecewise linear (PWL) if there is a finite cover of $\mathbb{R}^\ell$ with polyhedra such that the restriction of $f$ to any of these polyhedra is affine linear (i.e. of the form $x\mapsto Cx+d$).

>> **Lemma**. The composition of PWL $f\colon \mathbb{R}^\ell\to \mathbb{R}^m$ and PWL $g\colon \mathbb{R}^m\to \mathbb{R}^n$ is PWL.

> Proof. tl;dr: Pull back the polyhedral cover of $\mathbb{R}^m$ (given for $g$) onto $\mathbb{R}^\ell$ under $f$, and intersect with the polyhedral cover for $f$. This creates a refined cover of $\mathbb{R}^\ell$ such that $g\circ f$ restricts to a linear function on each set in the cover.

> complete version: Pick a polyhedral cover of $\mathbb{R}^\ell$ such that $f$ is linear on each polyhedron, $\mathbb{R}^\ell=\bigcup_{i=1}^p P_i$ and similarly for $g$, $\mathbb{R}^m=\bigcup_{j=1}^q Q_j$.[^5] Fix a polyhedron $P_i$; trivially $f$ is linear on this polyhedron, so given by $x\mapsto y=Cx+d$. Take a description of a polyhedron $Q_j$ via inequalities, let's say this is $A y\leq b$. Then given $x\in P_i$, the condition for $x$ to land in $Q_j$ under $f$ is $A(Cx+d)\leq b$, which we can rewrite as $(AC)x\leq b-Ad$. We define $P_{i,j}=P_i\cap \{x\in \mathbb{R}^\ell \mid  $(AC)x\leq b-Ad$\}$. Note that $P_{i,j}$ is a polyhedron because it is the intersection of two polyhedra. Also note that the restriction of $g\circ f$ to $P_{i,j}$ is the composition of the restriction of $f$ to $P_{i,j}\subseteq P_i$ with the restriction of $g$ to $Q_j$, both of which are affine linear. Since the composition of two affine linear functions is affine linear, the composition of $g\circ f$ to $P_{i,j}$ is thus affine linear. For fixed $i$, the collection $\{P_{i,j}|1\leq j\leq q\}$ is a cover of $P_i$ because every point in $P_i$ lands in at least one $Q_j$ under $f$. Therefore, the sets $P_{i,j}$ with any $(i,j)$ with $1\leq i \leq p$ and $1\leq j \leq q$ form a cover of $\mathbb{R}^\ell$. So we have constructed a cover on which $g\circ f$ restricts to affine linear functions. This means that $g\circ f$ is affine linear.

>> **Theorem** (Arora, Basu, Mianjy, Mukherjee; 2018). Every $\mathbb{R}^n\to \mathbb{R}$ neural net with ReLU activations represents a piecewise linear function, and every piecewise linear function $\mathbb{R}^n\to \mathbb{R}$ can be represented by a ReLU neural net with depth at most $\lceil \log_2(n+1)\rceil + 1$.

> Proof. Given the vector of numbers written at vertices in $L_{i-1}$, i.e. $(z_u)_{u\in L_{i-1}}\in \mathbb{R}^{|L_{i-1}|}$, the vector of numbers written at vertices in $L_i$, i.e. $(z_v)_{v\in L_i} \in \mathbb{R}^{|L_i|}$ can be obtained by multiplying the former vector by the $|L_i|\times |L_{i-1}|$ matrix with entries $w_{(u,v)}$, and then passing each coordinate through a ReLU. Taking the ReLU of just coordinate $i$ of a vector is a PWL function $\mathbb{R}^m\to \mathbb{R}^m$, since its restriction to the polyhedron $x_i\geq 0$ is linear and its restriction to the polyhedron $x_i\leq 0$ is linear, and these two polyhedra partition $\mathbb{R}^m$. The function taking the ReLU of every coordinate is equal to the composition of $m$ functions, each of which takes the ReLU of just one coordinate. In conclusion, a neural net can be written as a composition of a bunch of matrix multiplications which are linear, so PWL, and one-coordinate ReLUs which are also PWL. Since a composition of PWL functions is PWL, it follows that any function implemented by a ReLU neural net is PWL.

> The other claim is trickier. 

## Universal approximations 

It turns out that neural nets with depth $d=2$, i.e. just one hidden layer, are universal approximators (provided unbounded width): 

https://youtu.be/6Ss9kFTUS-Y?t=2987

(theorem to be copied here)

(proof/sketch here maybe)

There is also a result 

Barron's thm, explain Stone-Weierstrass, infinite width + sampling https://youtu.be/6Ss9kFTUS-Y?t=4588, cosine activations->everything

mention strongest result with any polynomial activations

Put in the analogous result for when width is constant and depth is allowed to be large https://arxiv.org/pdf/1710.11278.pdf




## Depth separations
Does this mean that depth is totally unhelpful (for representing functions)? No, because there are functions which can be represented with way fewer parameters for a deep network than for a shallow one, at least for ReLU activations. We will call such functions *depth separators*. Telgarsky gave an explicit family of functions for which one needs an exponential amount of width to match a polynomial amount of depth. To construct these functions, blabla (put construction here)

start with depth 2 missing https://youtu.be/6Ss9kFTUS-Y?t=3328

then any depth Telgarsky theorem, spike intuition https://youtu.be/6Ss9kFTUS-Y?t=3401

And here's Telgarsky's theorem saying these are indeed depth separators:

For Telgarsky's result, we will start by introducing a neat little function called the tent map.

> **Definition** (tent map). The tent map $\Delta\colon \mathbb{R}\to \mathbb{R}$ is given by $\Delta(x)=\sigma_r\left(\sigma_r(2x)-\sigma_r(4x-2)\right)=\begin{cases} 2x & \text{if }  0\leq x<\frac{1}{2}\\ 2(1-x) & \text{if }\frac{1}{2}\leq x<1\\ 0 &\text{otherwise.}\end{cases}$.

The nice thing about this function is that it gets really spiky under composition with itself.

> **Lemma** ()




(say something about the proof here)

mention open problem of going from k layers to k+1

mention vague open problem of understanding whether for natural functions, depth helps (in these examples, crazy Lipschitz constant)

## Yarotsky 2016 thm with polys

## Width separations

https://proceedings.neurips.cc/paper/2017/file/32cbf687880eb1674a07bf717761dd3a-Paper.pdf


## Something wacky
How does the above depend on the activation functions used? Actually, a lot. Let's define $\sigma=$ (copy from slide 55). $\sigma$ is not the nicest function known to man, but it's not that bad either: (list nice properties)

It turns out that with $\sigma$ activations, we can approximate anything with width linear in the input dimension and depth $3$.

I think the takeaway here is that all the results on depth separations above are mostly quirks of ReLU?

also mention 3 from here, I think need two kinds of activations and one linear size hidden layer https://youtu.be/6Ss9kFTUS-Y?t=4720



# Other reasons why this does not constitute much of an explanation of why depth is useful

For a given architecture Intuitively, in the limit of infinite data points $(x_i,f(x_i))$ for a given function $f$, eventually we should be able to get 

Actually, we don't have lots of data. There will generally be lots of functions that interpolate through all the training data perfectly, both for a wide net and also for a deep one. All the expressivity gap tells us is that the correct function is one of these functions for the deep net. To give an experimental example 

# Acknowledgments

I wrote this piece for the distillation week of John Wentworth's SERIMATS training program, and while being a Prague Fall Season resident. I would like to thank Peter Hozák, Anton Sinner, and Kay Kozaronek for feedback. The main reference sources I used were [Ankur Moitra's Theoretical Foundations for Deep Learning lecture notes](http://people.csail.mit.edu/moitra/408b.html), [Itay Safran's slides on Depth Separations in Neural Networks](https://hanin.princeton.edu/DepthSeparations.pdf), [Matus Telgarsky's Deep learning theory](https://mjt.cs.illinois.edu/dlt/two.pdf) [lecture notes](https://mjt.cs.illinois.edu/dlt/index.pdf), and [this survey talk](https://www.youtube.com/watch?v=6Ss9kFTUS-Y) by Telgarsky.

[^1]: Note the indexing – the input and output layers are not included.
[^2]: Replacing the requirement that an edge starting from one layer has to go to the next with the graph just being acyclic, the rest of this section would still make sense; this broader class of neural nets one gets includes (or potentially equals – after spending $10$ minutes to review, I am not sure if a definition has become canonical yet) *residual neural nets (ResNets)*. Also getting rid of the acyclicity requirement, one gets *recurrent neural nets (RNNs)*, for which one needs to reframe the net's computation (and training) somewhat more substantially.
[^3]: In the literature, it is often the case that each vertex $v\in V$ additionally has a parameter $b_v$ attached, called the *bias* of $v$, but the neural nets we consider for this post won't have that.
[^4]: This does not mean that any net with layers which are not fully connected is worse in some general sense, only in terms of expressive power. Having fewer edges means having fewer parameters, which can make things more feasible computationally compared to a fully connected net with the same layer sizes. Having carefully picked edges can endow the net with better inductive biases (compared to a fully connected net with the same parameter count) – I think this is e.g. one idea behind *Convolutional neural networks (CNNs)*.
[^5]: These partitions exist because $f$ and $g$ are PWL (by definition of PWL).
