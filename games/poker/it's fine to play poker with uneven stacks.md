
consider the following game:  
* it's a 1 vs 1 poker match  
* you'd have a buy-in and starting stack of $x$; your opponent would have a buy-in and starting stack of $y$  
* your opponent is just as good as you at poker  
* the game ends when a player runs out of chips  
* the winner gets the full $x+y$ (and the loser gets $0$)  
* non-standardly, instead of who is big blind and who is small blind being randomly determined at the start and then alternating, let's say it is randomized each hand, because that's a variant i can analyze. imo it's a minor change and i'm quite sure that i'm right or at least almost right also with blinds alternating as well, but idk how to provide a proof for this standard variant. If you disagree, we could discuss the difference between these variants.  
  
Claim. Your expected payoff in this game is $x$.  
  
argument:  
* It is sufficient to show that you have a strategy (which you could reasonably play while only being as good a player as your opponent) which makes your expected payoff in the game at least $x$ however your opponent decides to play (given the constraint that they are at most as good as you, which is perhaps imprecise but will be replaced with a clear assumption in a second).  
	* This is sufficient to establish that your expected payoff is exactly $x$ because: applying the same claim from your opponent's perspective would give that your opponent can make their expected payoff at least $y$, which means that you can't make your expected payoff more than $(x+y)-y=x$. So your expected payoff would be lower-bounded and upper-bounded by $x$.  
* Ok, so I propose that you use the following "strategy": you always play "as if it were a cash game" — to be precise: your strategy for playing a hand will just be your best attempt to maximize the expected amount of money you'll have after a single hand.  
* I claim that if you start a hand with $x$, playing with this strategy, your expected stack after the hand is at least $x$. This is because your opponent might as well be playing the hand with $x$, and given that your opponent is an equally good player, there cannot be anything they could do to make you lose stack in expectation when playing a single hand $x$ vs $x$. In principle, your opponent could be trying to do something other than maximizing their own expected stack after the hand, if that were better to do in the 1v1 tournament setting for some reason — we allow this; the point is just to note that your expected stack size after the hand will be at least $x$ however your opponent decides to play (given the constraint that they aren't better than you).  
* Letting $X_i$ denote your stack size after $i$ hands, it follows from what we just argued that with this strategy, $\mathbb{E}[X_{i+1}|X_i, X_{i-1},\ldots, X_1]\geq X_i$ i.e. that your stack size is a [supermartingale](https://en.wikipedia.org/wiki/Martingale_(probability_theory)#Submartingales,_supermartingales,_and_relationship_to_harmonic_functions).  
* By the [optional stopping theorem](https://en.wikipedia.org/wiki/Optional_stopping_theorem#Statement), we conclude that your expected stack when the game ends is at least $x$. (We can use condition (c), but I think there's a typo in that condition on wikipedia? I think it should be like condition 1 on slide 13 here: https://www.cl.cam.ac.uk/teaching/1819/Probablty/materials/Lecture8.pdf .)  
* Since the game ends with you having either stack $0$ or $x+y$, we conclude that the probability of you having stack $x+y$ when the game ends must be at least $\frac{x}{x+y}$.  
* So your expected payoff from the game is at least $(x+y)\frac{x}{x+y}=x$. This is what we wanted to show.  
  
  
  
# separately: googling this question  
  
the first thing that came up when i googled "poker heads up expected value with smaller stack" that answers the question is this forum, https://forumserver.twoplustwo.com/15/poker-theory-amp-gto/odds-winning-heads-up-tournament-236526/ , and i think the majority opinion there agrees with me


# what about the alternating case?

maybe simplest to analyze just two hands in a row. the first hand is randomized, the second is the other way. is there an EV diff?
hmm we have a martingale for money after first hand. but then second hand comes 