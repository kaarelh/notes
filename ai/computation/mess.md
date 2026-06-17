



$$\vec{k}=(\vec{a}+\vec{\omega}_1)\odot (\vec{a}+\vec{\omega_2})\odot (\vec{a}+\vec{\omega_3})\odot \cdots \odot (\vec{a}+\vec{\omega_k})=\sum_{\text{all multisets $I$ with $0\leq |I|\leq k$ of indices which are present together with choices of another index set $J\in\binom{[k]}{k-|I|}$}}\bigodot_{i\in I} \vec{f_i}\bigodot_{j\in J} \vec{\omega_j}=:\sum_{I}\vec{f_I}\vec{\omega_J}.$$

@Dmitry Vaintrob here's a concrete version of your universal compiler (almost exactly what you said) with a proof that it has the desired readoff behavior. We'll let $\odot$ denote the coordinatewise product (ie Hadamard product) of two vectors (or two dual vectors), $\mathbb{1}$ denote the all-$1$s vector, and $v^\dagger$ denote the 'canonical dual vector of $\vec{v}$', i.e. the linear map whose coeffs in our chosen basis are the complex conjugates of the components of $\vec{v}$. I will generally put daggers on all vectors in the dual space (sorry if this is a bad convention). 

On the side of keys, an activation vector at some position will look like $\vec{a}=\sum_{i\text{ present}} \vec{f_i}$, let's say $k$ auxiliary vectors $\vec{\omega_1},\cdots, \vec{\omega_k}$ with uniformly random unit complex number coordinates has been drawn (these need to be stored in some weight matrix), and we compute the universal key to be $$\vec{k}=(\vec{a}+\vec{\omega}_1)\odot (\vec{\omega}\odot \vec{a}+\mathbb{1})\odot (\vec{\omega}\odot\vec{\omega} \odot \vec{a}+\mathbb{1})\odot \cdots \odot (\underbrace{\vec{\omega}\odot \cdots \odot \vec{\omega}}_{k-1}\odot\vec{a}+\mathbb{1})=\sum_{\text{all multisets $I$ with $0\leq |I|\leq k$ of indices which are present}}\bigodot_{i\in I} \vec{f_i}=:\sum_{I}\vec{m_I}$$Here, $k$ is the max number of inputs that can show up in a circuit we want to look for, and we used the fact that the Hadamard product is bilinear. We assume that each coordinate of every $\vec{f_i}\in\mathbb{C}^d$ is drawn uniformly at random from the . The key useful property here is that whp, for all index multisets $J$ at once, we have that $m_J^\dagger \left(\sum_{I}\vec{m_I}\right)/d$ is $1+o(1)$ if $m_J$ is present in the sum and $o(1)$ else.

On the side of queries (where vectors are dual vectors), to compute a readoff $q^\dagger$ that reads some desired circuit $C$ (with $\leq k$ inputs), the proposal is to start from the duals of inputs to the circuit, normalized by $1/d$ (this ensures readoffs are $0/1$ if we care about that, though we could also not normalize since attention would also work without normalizing), and to then walk up the circuit iteratively computing as follows:
* $\mathbb{1}^*/d-g^\dagger$ when the gate is $\neg G$;
* $g^\dagger \odot h^\dagger$ when the gate is $G$ AND $H$;
* $g^\dagger + h^\dagger-g^\dagger \odot h^\dagger$ when the gate is $G$ OR $H$.
(Actually, AND and $\neg$ are already functionally complete so the OR is really overkill.)

Let's prove that (assuming the whp statement from earlier holds) this works, i.e. that with $q^\dagger$ computed this way, we really have $q^\dagger (\vec{k})$ being $0$ or $1$ corresponding to whether the circuit $C$ evaluates to $0$ or $1$ on the inputs present at that key position. We prove this by induction on the number of inputs involved in a circuit. Just one input is an easy base case. The induction step when the gate is $\neg G$ is also easy. 

(Caveat: really, in an attention head QK part, we would project at random to the same $d_{head}$-dimensional subspace on both the key and query side before taking the inner product.)