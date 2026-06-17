
can we always think of a 2d rotation only locally hitting a single vec in an orthonormal basis of a subspace? note that with a 2d subspace in 3d, this is true for any rotation (consider normal vecs); i think this is just false for two 2d subspaces in 4d though (this is somehow the general case — can pick a basis to the subspace with just two non-orthogonal things, eg because SVD). one can see this by noting that if it were that way, the dim of the intersection of the subspace with itself after the rotation would need to always be at least dim subspace minus 1. but this is just false i think — maybe this is already intuitive that the dim - 1 case is nongeneric? but i'm like 85% i also calculated this explicitly in the composition notebook and it just won't happen generically

however, assuming the math is right, at least locally, it should just be two rotations of orthogonal u_1 and u_2 in U to orthogonal v_1 and v_2 which are orth to u_1 and u_2 respectively but generally not orthogonal to u_2 and u_1 respectively. wait NO. this is what just rotating u_1 and u_2 would look like, but the rotation would not just act like that, because each rotation also affects the other vec right


btw i did some calculation and i think at least to first order, rotation of U in a generic plane is the same as two different rotations of the kind considered before in succession (edit: i think this is false actually but not currently thinking carefully about it)

i guess (assuming true) this would probably be obvious if we could visualize 4d — maybe it's obvious anyway but i did it algebraically

some more details:  
* if you consider the projection from U into the plane, it has left singular vecs u_1 and u_2 and right singular vecs v_1 and v_2  
* to first order, rotation by alpha in the plane acts on U as u_1 -> u_1 + sigma_1 alpha v_2 and u_2 -> u_2 + sigma_2 alpha v_1  
* this is the same as rotating u_1 into v_2 by sigma_1 alpha and then rotating u_2 into

