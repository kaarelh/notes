
PCA/SCD, NMF, (sparse) autoencoders, sparse coding
https://www.youtube.com/watch?v=UQGEB3Q5-fQ
![[Pasted image 20230412183031.png]]

maybe could try iterative autoencoder? like just have 1 neuron first, then more


https://www.lesswrong.com/posts/mkbGjzxD8d8XqKHzA/the-singular-value-decompositions-of-transformer-weight?commentId=wYBsQYs8kWZrJEj6L
Adam Jermyn: This is really interesting! One extension that comes to mind: SVD will never recover a Johnson-Lindenstrauss packing, because SVD can only return as many vectors as the rank of the relevant matrix. But you can do sparse coding to e.g. construct an overcomplete basis of vectors such that typical samples are sparse combinations of those vectors. Have you tried/considered trying something like that?

> sparse coding! Maybe ask Pierre about this?

