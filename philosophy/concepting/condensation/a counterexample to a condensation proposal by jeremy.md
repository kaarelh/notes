response to https://www.lesswrong.com/posts/rQDCQxuCRrrN4ujAe/jeremy-gillen-s-shortform?commentId=LDMtRf7DAhsyD8uv2

separately from this terminological question, i think your score definition favors pathological condensations in various examples. the source of the problem i have in mind is that you let me pick which latents to keep depending on the subset i'm reconstructing, and i can be clever with my choice, so one can include cheap latents in the condensation that work only for certain non-principled subsets of the picture, and only use those when one can get away with that. here's a concrete example:
* let's say we have an image that's a white background with a black k-gon with some complicated k
* now i make my condensation have the following latents:
** a top latent saying "for all x,y, if no other instructions for that x,y, put (x,y)->white in the output dictionary"
** a k-gon latent saying "for all x,y in a k-gon centered at x_0,y_0 of inradius r, put (x,y)->black in the output dictionary"
** a circle latent saying "for all x,y in a circle centered at x_0,y_0 of radius r, put (x,y)->black in the output dictionary"
* now when reconstructing subsets of the incircle of the k-gon, i only take the circle latent but not the k-gon latent, and i save on loss because k is complicated. when reconstructing other subsets of the k-gon, i only give the k-gon latent and not the circle latent
* this will do stricly better on loss than a condensation in which i only have the k-gon latent. seems weird. (if you think this isn't really pathological because the k-gon sorta really has this circle inside, then let's replace the k-gon with a weirder shape and pick some weird circle inside.)

I think one way to get rid of this pathology is to have each latent correspond to a subset I of indices, and have it be loaded into context each time the subset A getting reconstructed intersects with I. Maybe you already meant this, even though I think it isn't what you wrote down?

later edit: I think whether this at least doesn't save you for some loss coefficients. and if you have a circle with sufficiently complicated fluff on the boundary, for any reasonable coeffs, you will prefer to see the circle. but maybe this is actually intuitively correct behavior! the shape really is a circle with some fluff then! 
