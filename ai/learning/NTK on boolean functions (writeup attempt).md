

this should work for both NTK and the NNGP, at least if chatgpt is remotely to be trusted: https://chatgpt.com/share/67550358-aa54-800f-97fb-7862379c2b8a

setup:
* fix an architecture and a depth (maybe just MLPs with some activation function?). take the infinite width limit
* boolean functions are $\{-1,1\}^n\to \{-1,1\}$
* suppose that the kernel has symmetry: that k(x,y)=f(x dot y)
# Mechinterping the NTK? an exploration with boolean functions


There are basically no well-understood NNs doing anything 

## $G$-invariant kernel => the characters are the eigenvectors

In all of the following, let $G$ be a group.

> Definition. A kernel $K$ on $G$ is a function $K\colon G\times G\to \mathbb{R}$.

> Definition. We say the kernel $K$ is $G$-invariant if for all $x,x'\in G$ and $g\in G$, we have $K(gx,gx')=K(x,x')$.

Remark: Equivalently, a kernel $K$ is $G$-invariant if and only if is a function $g\colon G\to \mathbb{R}$ such that for all $x,x'\in G$ we have $K(x,x')=g(x^{-1} x')$.^[In fact, $g(x)=K(1,x)$.] (That is, a kernel is $G$-invariant iff it only depends on the "difference" of the elements.)

Now consider the vector space $V$ of all functions $f\colon G\to \mathbb{C}$, and assume we have a kernel $G$-invariant kernel $K$ on $G$.
> Definition. Define the $K$-convolution $C_K\colon V\to V$ by $(C_K f)(x)=\sum_{x'}K(x,x')f(x')$. (Note that $C_K$ is a linear operator on $V$.)

> Theorem. Any group homomorphism $\chi\colon G\to \mathbb{C}^{\times}$ is an eigenvector of $C_K$.

Proof. We just calculate: $(C_K\chi)(x)=\sum_{x'}K(x,x')\chi(x')=\sum_{x'}g(x^{-1}* x')\chi(x)\chi(x^{-1}*x')=\left(\sum_{x'}g(x^{-1}* x')\chi(x^{-1}*x')\right)\chi(x)=\left(\sum_{x''}g(x'')\chi(x'')\right)\chi(x)$. So we see that $\chi$ is indeed an eigenvector; its eigenvalue is $\lambda_\chi=\sum_{x}g(x)\chi(x)$.

For a finite abelian group $G$, the homomorphisms $\chi\colon G\to \mathbb{C}^{\times}$ form a basis of $V$. Thus, for finite abelian $G$, the operator $C_K$ has an eigenbasis consisting of the characters of $G$.

## 
# extensions
* Think about what the actual learned network would look like. Think about how one could have understood that this is going on with interp.
	* What would existing attempts at neural net full-reverse-engineering methodologies think about this example? Would any existing method work acceptably well?
* other point groups
* other learning hyperparams. eg L^2 minimal input layer?
# notes

* the generalization conjecture obviously does work actually, i think! like we are literally assuming you get the lowest weight norm thing (or in general the closest point from initialization), so you do then literally get the boolean function which in this weighted fourier norm is smallest which fits through the given points.
* we might even be able to get a theorem characterizing how many data points are needed to generalize correctly on any given boolean function, in terms of its degree! tho really this might be known already. probably good to look at https://arxiv.org/pdf/2302.11055 and stuff it cites

## literature

On the Spectral Bias of Neural Networks: https://arxiv.org/pdf/1806.08734 . does some experiments, noting low degree components are learned first

The merged-staircase property: a necessary and nearly sufficient condition for SGD learning of sparse functions on two-layer neural networks: https://proceedings.mlr.press/v178/abbe22a/abbe22a.pdf#page=12.72 . i think this says that any kernel method requires d^k data points to learn a boolean function whose max fourier term has size k
# mess

wait why is there a norm independent of the inputs again... hmm i guess we have these feature vecs and some coeffs on them right. and the norm of the coeffs on the feature vecs is a thing that makes sense without reference to which inputs are involved

 In particular, for the group $G$ whose element set is $\{-1,1\}^n$ and whose operation $*$ is the hadamard product of vectors (so $G\cong(\mathbb{Z}/(2\mathbb{Z}))^n$). Its 