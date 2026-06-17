
can one recover what configuration of vectors one has from data about pairwise angles? equivalently, from all values $v_1\cdot v_j$.

well, put vectors as rows of $W$, then one knows $WW^T$. If the orthonormal eigendecomposition of the symmetric matrix $WW^T$ is $WW^T=UDU^T$, then (one can show) $W=U\sqrt{D}V^T$ for some orthonormal $V$ and the square root interpreted as the appropriate rectangular matrix. So $W$ is determined up to isometry.

I think one can also just do this by Gram-Schmidting an independent set into an orthonormal basis (coeffs are given by dot prods), and then everything is given in terms of this orthonormal basis uniquely