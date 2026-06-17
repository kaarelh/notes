
![[Pasted image 20250916153228.png]]

# thinking about the problem
* ok we're dealing with lines on the plane. i wonder if it's arbitrary lines on $\mathbb{R}^2$. yea looks like it
* ok so there is a notion of sunniness of a line (i guess because the IMO was in the sunshine coast region). almost all lines are sunny — the only non-sunny lines are those that are vertical, horizontal, or parallel to x+y=0, so parallel to the upleft to downright diagonal
* we're being asked for which k there is a certain kind of configuration on n lines for. like, for each n, we're supposed to find all the k. what does the configuration have to be like?
	* it is supposed to have k sunny lines, ie so n-k aligned lines
	* all the natural number points (a,b) in the triangle ending at (n,1), (1,1), (1,n) should be on at least one line
* hmm you can easily do it with k=0: just take all the n verticals, or take all the n horizontals, or take the n diagonals
* you can also easily do it with k=1: just take the n-1 diagonals with at least 2 points, and then put some arbitrary line through the last point
* would be nice to have paper here... yea i'm getting out paper... sad for this chain of thought!
* idea: bash out some small n cases
	* we are done for n=1. namely, k=0 and k=1 are both possible
	* for n=2, we know from the above that k=0 and k=1 are possible. since there are 3 points and 2 lines, at least one of the lines has to pass through 2 points, so it is easy to see that at least one of the lines has to be aligned. so k=2 is not possible
	* for n=3, again k=0 and k=1 are possible. now k=3 is possible somehow, with like a star. is k=2 possible? not with 3 pts on any line, because all those leave a bad conf for the other 2. so need 2 per line exactly to get all 6 pts on lines, with no point on two lines. there is only one option for what to pair each tip of the triangle with, and this gives the k=3 construction. so k=2 isn't possible!
	* for n=4, again have k=0 and k=1. also can cut off a side and get to n=3, at which we know k=3 is possible, so k=3 is possible here. what about k=2 and k=4? to have k=4, would need all 4 lines to be non-aligned. but non-aligned lines have at most 2 points, so we get at most 8 points in total. so that doesn't work. what about k=2? since there are 10 pts in total, the aligned line needs to have at least 4. but this means it cuts off an edge. and then we get the n=3 case and know k=2 is not possible there. so k=2 isn't possible here either
	* for n=5, again have k=0 and k=1. also can cut off two slices and get that k=3 must be possible as well. that leaves k=2,4,5. here the non-aligned line max is 3, but the pt (2,4) eg doesn't have a non-aligned line with 3 through it, and neither does (1,4), and neither do their reflections. so with non-aligned lines only, one can't do it, because one can't get the avg to 3 (see item below for an argument why one needs that). what about k=4? well what can the one aligned line in a construction be. it can't be cutting off a side. it can't only have 3 pts, because then the same calculation shows failure again (not all problematic points can be gotten rid of). so it must have 4 points. 
* the num of points is 1+2+...+n = n(n+1)/2. the avg num of points per line must be at least (n+1)/2
* oh. look at the last diagonal, it has n points. now are all these on separate lines? if yes, this is a big restriction. if no, we are in the n-1 case, and can carry over the construction!
	* can also do this with first vertical or first horizontal. i guess the case of interest has all three having all on separate lines (else could restrict to case below). so each line must go through one of each. but oops that's not possible. so done. so it's just the solutions for n=3 forever! always so always k=0,1,3 are the only options!

# some thoughts on what was going on

* idk, i spent a while working out cases. i guess i had previously learned the useful strategy of working out cases
	* what did i do when working out the cases for some n? idk some sort of analysis of what can happen. some small calculations to see what could work. proving some small statements about what the solution must be like
	* there's a general thing here: to answer some question about the set of solutions, it's probably quite common to prove various other things about it. the other statements get you to the statement of interest
* i was vaguely also tracking some induction idea. i guess reduction to n-1 just shows up naturally when working out cases
* i guess at some point i got a good idea for how to work out a case, of thinking about how the points on the last diagonal are partitioned onto lines. idk how i got the idea, but i guess one can see that it's promising quickly from it creating really restricted situations: either there is a line there and then we are just in n-1, or there isn't a line there and then all n points are on different lines, which restricts the configuration severely.
* noticing the obvious "generalization" of this also to the first horizontal and first vertical restricts the configuration a lot, in fact making it impossible. i understood that and then the induction was obvious