



## Case study: an argument for the standard cardinal values in chess

Chess has three outcomes: a win for you, a tie, and a win for your opponent (this is assuming sth like a symmetry between white and black or the game being zero-sum — we give no argument for the more general case atm). WLOG — due to the invariance of $u$-maximizing behavior under rescaling $u$ by a positive constant and then shifting it by a constant — we can take a loss to have utility $0$ and a win to have utility $1$. It remains to specify a number $d\in (0,1)$ as the utility of a tie. What follows is a pro tanto argument that we ought to choose $d=0.5$, as is standard (e.g., this yields precisely the scores given in most tournaments).
* $d<0.5$ has the property that when the probability of a draw becomes high enough, both players are better off deciding to flip a coin which 'forces' one of them to resign
* $d>0.5$ has the property that two equally good players are better off just agreeing to a draw at the start of the game.
This leaves us with $d=0.5$.

a criticism:
* issue with the first part: wait, why don't players flip biased coins to determine which should resign all the time? why hasn't some secret way of doing this developed? 
* issue with the second part: no draw until move x rules. but still, can play very drawish lines

so i'm not convinced the above is a great argument atm

## notes

game is minimally a setting in which you can do certain things

now you have to pick what to, in fact, do. i guess we want to say that games are underspecified in that what you ought to do hasn't been specified, and it will be more properly specified once a utility function is provided. but in what sense is this not just specifying some number of bits about the strategy? what's the key distinction between:
* giving a utility function to maximize
* saying that every move has to start with doing action x (let's say we have a game where you can take two actions each turn, and x is always a possible action)
each makes your eventual strategy more determined. i guess one difference is that the first doesn't change your set of possible action sequences, whereas the second does? but this seems sorta silly?

i want to say that specifying the utility function specifies optimal play — just pick the strategy which maximizes expected utility — but this seems sorta false when all players are choosing strategies at once, or like the wrong question to ask i guess. it's also the wrong criterion if we take the chess example seriously: optimal play is specified in chess, and yet the game is not sufficiently specified

if the adage that there is no right bounded rationality seriously, then maybe we shouldn't seek a game specification that specifies optimal boundedly rational play?

suppose your player is a kind of guy that assigns probabilities and then picks an action on each step which maxes expected utility. for such a guy, the game can be specified just by specifying payoffs at the end of the game. 

but suppose the player is a different kind of guy. in what sense is the 

### a kind of game that might be nice to analyze
on each step, some probability that the game will end (might want to say here that the game should end almost surely for any policy or something). the game looks like shuffling the probability distribution around from which something will be drawn at the end of the game. (this starts to sound a bit like some ergodic theory thing)