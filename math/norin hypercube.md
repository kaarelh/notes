

# 25/06/24 messages to hugo

i think i have a proof of the conjecture assuming each red component and blue component only intersect at <=1 vertex. one can also get good upper bounds when this assumption is relaxed a bit

* the idea is to count the number of vtx pairs (u,w) such that there is a red-then-blue path from u to w. we will show that this is 2^{2n}, so every (antipodal) pair is connected by such a path! (obviously this isn't quite true without our assumption, but i conjecture that it is at least 2^{2n(1-o(1))} in general)
* fix a pair (u,w). if there is no such path, then there is no vertex v such that there is a red path u->v and a blue path v->w
* if there is such a path, then there is such a vertex v. in fact, by our assumption about red-blue intersections, there is a unique such v
* so, counting pairs (u,w) is equivalent to counting triples (u,v,w)
* the number of triples which include v is |R(v)|*|B(v)|, where R(v) is the red component of v and B(v) is the blue component of v
* it suffices to show that when picking a uniformly random v, the expectation of |R(v)|*|B(v)| is at least 2^n
* jensen says log of expectation is at least expectation of log, so it suffices to show that E[log(|R(v)|)+log(|B(v)|)] >= n
* this in turn follows by an isoperimetric inequality argument which i will give in the next message

there's the following isoperimetric inequality for the hypercube:
* a subset of k vertices has at least k (n-log_2 k) edges to its complement, ie has a boundary of size at least k (n-log_2 k)

consider the red components and the blue components as a collection of subsets, together with their boundaries. note that each edge of the hypercube can only appear in at most two of these boundaries (eg, a blue edge can't be a boundary edge for any blue component, and it can be a boundary edge for at most 2 red components)

this means that:
2*n2^{n-1} = 2*[the number of edges of the hypercube] >= sum_{components} [boundary size of the component] >= sum_{red components R} |R|*(n - log_2 |R|)+sum_{blue components B} |B|*(n - log_2 |B|)

now note that after dividing both sides by 2^n, the last expression becomes an expectation over vertices:
n >= E_v [2n - log_2 |R(v)| - log_2 |B(v)|]

and so E[log_2 |R(v)| + log_2 |B(v)|] >= n, as desired

what's going on here is that if E[log(|R(v)|)+log(|B(v)|)] were too small, then that would force boundaries to be too big


# 25/01/27 some literature review

https://arxiv.org/pdf/1301.2195
"Indeed, if G is a subgraph of Qn of average degree d, by the edge isoperimetric inequality
for the cube ([1], [5], [6], [8]; see [2] for background) we have |G| ≥ 2^d."

you can apply this to connected components of a color component to get that they have to be big! so what? well maybe you can do two steps of this expansion and get something really big indeed? like take all the stuff 1 color change away from a vtx, and then take all the stuff 1 color change away from that stuff, maybe. we could even keep going for like log n or n/100 steps or whatever if we want. surely this is really big on average? but how to show this?

note we can quotient together two vtxs if there's a red and a blue path between them. if we had some such expansion property for a quotiented hypercube, then maybe we'd be done, because then we'd get all the vtxs in the immediate connected component to have disjoint components of the other color, so maybe we get a lot of expansion?

# unknown!

for each vtx, consider the set of vtxs one can get to along a monochromatic path. wts some vtx has an antipodal pair in its set

# 24/10/09

Can we just show 1ccn-s of vtxs, ie sets (n is for neighborhood) at most 1 color change away, are large on average? or is there a counterexample to this?

could we use the leader argument but count allowing one color change or sth?

whats up with a splitter between two things not itself being splittable. is that even true. like the thing where the layered construction cant have its middle split further orthogonally because that just connects stuff


# Apr 7

we can also take a random path and instead of looking at the num of color changes on that path, look at the change in distance from the beginning on each step. linearity of expectation lets one split this into a sum over steps of by how much distance from the start changed on that step. and this can be instead computed from the side of edges, thinking for each edge what kinds of vertices have differing distances from the two edge endpoints? one immediate observation is that if the edge is between two vertices in a color component of the original vertex, then all is good

so the bad case is that the edge uv is color x (with u closer to the original vtx) whereas every shortest path to u ends in color y and also there is no shorter path to v than ones obtained by concatenating a shortest path to u with the edge uv (though note it's possible that there are other equally short paths, even through u). if this happens, we get a few things:
1) everything x-connected to v has the same distance to the origin(al vertex) o — this can already give that a bunch of edges must then not increase distance from o
2) 


one can also start walking from both sides at once, with edges that avoid those on the other side (this might be better if it is easier to track distances from closer vtxs)


# Apr 5

random path only has n/2 color changes already. we can improve on this easily in case there is a const fraction of edges which does not change either color component or which do but move you closer to the starting vertex. can we show these things indeed have to take up some reasonably large const fraction?

so this beats 3n/8 as soon as p edges are like this, so as long as 3/8 >= prob change = 2qr; note 2qr is at most 2(1-p)^2/2^2=(1-p)^2/2, so done if (1-p)^2<=3/4, so 1-p = sqrt(3)/2, so p = 1-sqrt(3)/2, which is some number less than 1/4

# Dec 28

for each vtx, consider the set of vtxs that one can get to without changing colors. wts there is an antipodal pair for which these sets intersect. each set like this ends at a boundary of most distant vtxs that can be reached from that one?

# Nov 13



connection between Brouwer and Hex: https://www.cs.cmu.edu/afs/cs/academic/class/15859-f01/www/notes/brouwer-hex.pdf

see also https://math.uchicago.edu/~may/REU2019/REUPapers/Schachner.pdf from some topological generalization

is there a similar way to get the square grid thing (F3 from https://yufeizhao.com/pm/pm-ps.pdf )? here's a pf: https://math.stackexchange.com/questions/3641112/possibility-of-ants-not-being-able-to-cross-a-grid-shaped-bridge but well, not that topological. might be worth looking into making it topological along the lines of the paper above?



and then is there also a topological argument for norine?



# Oct 7


## set up some auxiliary polynomial?
eg make hypercube points represented by coordinates, capture adjacency somehow, also capture the number of color changes as like value of polynomial, show it takes a certain value?
## some topological construction?
can we construct some companion object such that there is a topological guarantee that one of the hypercube and this companion thing has a certain path or something like that? or just think of the original problem as the n-player path-making game and show one guy has to win? 

## two-color snake
try to build a long path by starting from a vertex and taking red edges in one direction, blue edges in the other, using each direction at most once. the conjectured claim follows from from (and is equivalent ignoring non-geodesics) there being a way to do this and getting a path of length n

what does getting stuck look like? well, it needs to be the case that if you consider the blue endpoint, all edges in remaining directions are red, and the red endpoint has all edges in remaining directions being blue. is the

## a system of highways

can we show that there are a lot of large steps one can take with just one color, and then conclude that in some sense whp we can chain them together into a path that takes us far from where we started? i guess one should probably be able to get lots and lots of monochromatic geodesics of length n/2 from the long-leader paper? unfortunately it's typically pretty useless to chain these, because you just take around half the steps forward and half the steps back. i think the variance here under random steps is very far from being good enough. 


# Summer 2023 i think


i have an angle of attack on this conjecture that seems fairly promising to me — i thought maybe you'd like to work on this together (though also no worries if you'd rather not — i'm also partially using this writing to clarify my thoughts):  
Norine’s antipodal-colouring conjecture, in a form given by Feder and Subi, asserts that whenever the edges of the discrete cube are 2-coloured there must exist a path between two opposite vertices along which there is at most one colour change. The best bound to date was that there must exist such a path with at most n/2 colour changes. Our aim in this note is to improve this upper bound to (3/8+o(1))n.


whenever endpoints of an edge are in the same blue component and also in the same red component, the edge cannot contribute a distance increase from any vertex. note that one color is always trivial. there are constructions where these two never happen at once i guess, but these seem quite structured, hmm?


