
* it's mostly about stumbling onto a generalizing solution
	* it's just that generalizing solutions have larger 
* it's mostly about the generalizing solution having lower loss and 'a stronger pull'
	* it mostly has a stronger pull because it is smaller
	* it mostly has a stronger pull because it is helpful on all data points (wait: i guess a system of memorizations is also helpful on all data pts. but there's still something here: each param of the generalizing circuit gets plausibly hit more. but this might be best seen as a subcase of the above)


case to consider: regression task that can be exactly solved. but generalization still happens. here, it must be the case that the 0 loss pt one ends up at is for some reason likely to be generalizing. this could be because of the generalizing surface having a stronger pull, or it could be because of the generalizing thing just being bigger. how do we distinguish between these two stories?
* one argument for the first story is that it must be what's happening in other cases, i guess, and it seems more likely that there's just one explanation? i'm not sure here, would need to think more carefully about other cases
* maybe we could decompose gradients early on as those pulling toward the generalizing thing and those pulling toward the memorizing things, and see that the generalizing things are already winning?
* maybe we could argue that solutions are small and equidistant or something? what would that even tell us?
* i mean, a random walk never gets anywhere, right (low-dimensional intuition is pisikaka here). anything that gets somewhere gets there because it's pulled there. maybe the question is whether there's a random walk initially? definitely not, because it's completely unhelpful to do a random walk. some stuff has to be learned from the beginning for you to get anywhere
* 