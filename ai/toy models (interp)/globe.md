


## thoughts on the rigidity transition

inspired by https://londmathsoc.onlinelibrary.wiley.com/doi/full/10.1112/blms.12740 . let G be the graph of given edges. let $C(G)$, the closure of $G$, be the graph of all dists which are already uniquely fixed by the distances in $G$ (actually this might not be close to the def in the paper at all). i guess the point is that we might as well always consider all the edges in C(G) to be known. can we say something interesting if there is a large clique in C(G)? let's start from the hopefully simpler case where the structure is 1-dimensional. then whenever you have two vertices whose distance is already fixed, and two things connected to both of these two, their internal distance is also already fixed! this is because each is forced onto the line of the two, in a unique direction. so i guess we have something like observation 2.1 from the paper?

this kind of thing seems maybe helpful, but much weaker than in the paper. a place things break down is that there's not a small-dimensional thing being filled now, i think — like, in the context of the paper, there is a matrix whose rank can be at most nd, that can be argued to have a rank increase with decent probability whenever G gains an edge. but in our setting, i don't see such a structure?

the infinitesimal rigidity thing will simply be false in all higher dimensions, by the way.

every time we give an edge length, we might be forcing some other edge lengths. what examples of this do we even have, beyond the tight cycles? once you have a tight cycle, adding ears is fine, too. maybe the transition only happens once there are macroscopic tight cycles? like, suppose there start to be tight cycles of size like log n. then will it all be tight? the threshold for there being a tight cycle on log n vertices is maybe when like n choose log n i

note that the ear thing causes another rigid cycle to be created which contains the new vertex (i think this follows eg from a case check). 

this motivates a conjecture: maybe each vtx has to be in a rigid cycle for the structure to be rigid?

can we construct an example where each vtx is rigid but some vtx is not in a rigid cycle? yes we can — example in notebook. still no example where no vtx is in a rigid cycle though!

### consider adding a vtx to given graph on other vtxs

conjecture: the vtx will be forced to be correctly positioned wrt any two others iff the distance between two of its neighbors was already uniquely determined by the data without adding this vtx

this conj is false. counterexample given by just adding endpoint of rigid cycle

### think in terms of subsets forced to be collinear?

every pair obviously forced. in general, if we take just maximal (under inclusion) collinear subsets, these can intersect each other at at most 1 vertex (if more, then union is collinear also, so not maximal!). maybe track this 'partition' of the vertices? when does adding an edge merge two collinear subsets? surely the edge should be between the two? what else can we say?

### second-order rigidity

note that not second-order rigid implies rigid (https://pi.math.cornell.edu/~connelly/pdf/10.1137_S0895480192229236.pd\) so if we find the edge prob at which the configuration becomes second-order rigid, we know it is also rigid. 

### $n^{-1+\varepsilon}$ for the case of embedding a 1d thing in higher dim

this probably works: note that once you have one triangle, you'll have other tight stuff attached to pairs in it. as long as you have like $>>1/n$ new things attached, you're probably fine. and you don't need triangle ears to be attached — larger cycles will do just fine, as long as they are ordered correctly. an expected value calculation for the number of such sufficiently large tight things attached suggests that any $p=n^{-1+\varepsilon}$ will be sufficiently large. 

### the same idea in higher dims

I think one can get close to $p=n^{-1/2}$ for a 2d structure in higher dim using a similar idea — naively would need to create bridges of tetrahedra, but really can do like a bunch of triangles in sequence and then connect with a final edge, assuming the 'ordering is right'. unclear if this can be made precise, but it's my current best guess for how to straightforwardly generalize the 1d case to higher dim (same should also work for arbitrary dim, but gets harder to visualize). we could do better if there were sparser rigid graphs than these ones. are there? this seems like a nice problem — maybe it's been studied? what's the sparsest rigid 2d structure in 3d?
## references on the rigidity transition

https://londmathsoc.onlinelibrary.wiley.com/doi/full/10.1112/blms.12740

https://pi.math.cornell.edu/~connelly/pdf/10.1137_S0895480192229236.pdf :  rigidity of a configuration does not imply its second-order rigidity; counterexample on figure 16d