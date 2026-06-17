
This piece aims to explain a sense in which an $k\times \ell$ weight matrix $W$ with a Relu on the outputs can 'do nearly $k\ell$ things'. This may be counterintuitive because the weight matrix corresponds to a linear map $\R^n\to \R^m$, which one might expect is only able to freely send $n$ generic vectors in $\R^n$ to $n$ generic vectors in $\R^m$. (At least naive equation-counting also suggests it can only do ) I care about the content of this piece because I think (1) it provides some insight into the kinds of computation a neural net can perform, (2) in particular, it tells us something about [computation in superposition](https://transformer-circuits.pub/2022/toy_model/index.html#computation), and (3) it provides some understanding regarding the location of the interpolation threshold.

this differs from [VC dimension](https://en.wikipedia.org/wiki/Vapnik%E2%80%93Chervonenkis_dimension) because shattering average case not max (?) see https://arxiv.org/pdf/1703.02930.pdf, bounds indeed diff

understanding why the interpolation threshold in model size is roughly around the number of parameters — I will provide a hand-written circuit for a 

task setup: $m$ input vectors in $\R^n$ with entries that are independent random $\pm 1$ coinflips, labels are also independent random $\pm 1$ (call the corresponding vectors red vs blue)

architecture: neural net which has residual stream $=\R^n$ to which $Relu(Wx)$ is added in each layer, where $W\in\R^{n\times n}$ (like a resnet but not quite because the residual stream can contain negative stuff; I do not see any reason why this is crucial though --- the same argument should work with vectors that have $\pm 1$ entries replaced by $\{0,1\}$, keeping everything non-negative)


We will process inputs into the format where one coordinate being $>\log n$ corresponds to the input being red, changing only one coordinate for each red vector and changing nothing for blue vectors. (This processing is the difficult step. Once we have this, it can easily be turned into output logits as follows with $2$ more layers. The first one picks out large coordinates and amplifies them to order $n^3$, and the second sums coordinates minus bias $n^2$. This will be large for red vectors, small for blue vectors.)  Each layer will pick a random set of $n^2/\log m$ red vectors and leave them all with exactly one coordinate $>\log n$. In fact, we construct each row of $W$ by picking a random set of $n/\log m$ red input vectors, finding a common direction which these exactly max out among the set of all inputs (and the output format implies also among the processed inputs), and having a proper scaling applied to get the output to have order $\log n$ for each. Such a direction can be found just by averaging the vectors (a probabilistic argument shows that these vectors are indeed maximally far in this direction, I think).


## A construction with superposition

## A memorizing resnet

## Sequential computation

## Corrections
First, if there is structure in the vectors