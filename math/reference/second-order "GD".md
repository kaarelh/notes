

see https://course.ece.cmu.edu/~ece739/lectures/18739-2020-spring-lecture-08-second-order.pdf

if you don't care about the step size, you can just step directly to the minimum of the second-order taylor expansion. this turns out to be given by the change being - H^{-1} grad L. this is the same as doing newton's method to find a zero of the gradient i think!

one can also restrict to a small ball and ask for second-order minima in that ball, maybe if one is concerned about steps that are too big (so the taylor expansion breaks down or something — though maybe there are theoretical reasons to think this won't happen?). then any local opt turns out to have to have the form given above, so we can start by checking if that is in the ball, and then if not looking for optima on the surface of the ball. this gives some lagrange multiplier thing; the equation is not that bad but didn't seem solvable in radicals? but whatever! still can solve numerically or sth