
Proposition. If one runs SVD on data set X (let's say that the $n$ columns of X are the $n$ data vectors, each of which is $m$-dimensional), then the component of some left singular vector $u_1$ in each column of $X$ is uncorrelated with the component of another left singular vector $u_2$ in each column of $X$. (I now think this is false, but true for PCA.)

Proof. Elements of the row vector $u_1^T X$ are the coefficients of $u_1$ in each column of $X$. Elements of the column vector $X^T u_2$ are coefficients of $u_2$ in each column of $X$. The correlation between the coefficients is thus $\frac{1}{n^2}$ times $n u_1^T X X^T u_2-||u_1^T X||_1||X^T u_2||_1$. One can see that the first term is $0$ by expanding $X$ and $X^T$ in terms of the SVD of $X$. However, the 


Proposition. Even for the mean $0$ case, it is possible for all variances of projections to some full orthonormal basis to be equal, yet there are principaler components.
Proof. Trivial counterexample: a digon along the diagonal in $\mathbb{R}^2$.


Theorem. A root system has all SVD/PCA components equal. More generally, this also applies to sets of vectors satisfying certain symmetry conditions


Lemma. The left singular vectors are top variance directions in the column data set. They are also the directions along which the output can be made to be largest (in $L^2$ norm) by multiplying with a unit vector from the right, and the directions along which one should multiply from the left to have a highest variance output. And, of course, analogously for the right singular vectors (e.g. since taking the transpose of the matrix switches the two).


Fact (I think). up to changing basis in each singular value space, SVD is unique as a sum of rank 1 matrices. in terms of vecs, there is still also a sign redundancy, but that should be it I think?

