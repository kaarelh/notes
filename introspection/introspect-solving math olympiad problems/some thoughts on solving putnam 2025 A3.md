
Alice and Bob play a game with a string of n digits, each
of which is restricted to be 0, 1, or 2. Initially all the
digits are 0. A legal move is to add or subtract 1 from
one digit to create a new string that has not appeared
before. A player with no legal move loses, and the other
player wins. Alice goes first, and the players alternate
moves. For each n ≥ 1, determine which player has a
strategy that guarantees winning.



some ideas i had which turned out to be useful:
* thinking of it as walking on a graph
* trying to show the second player has a winning strategy

an idea i was missing until i looked for a hint by peeking at https://community.wolfram.com/groups/-/m/t/3598035?p_p_auth=K5QPx2Ji :
* thinking in terms of perfect matchings. when i saw the word "perfect matching", doing the rest was easy
	* aside: it seems sort of likely that if i went through a long standard list of stuff you can consider on a graph, i would have solved the problem. it's interesting to ask to what extent there is a phase transition to being good at math when doing this sort of activity with a fixed list. there might be a point when you get good at lots of textbook problems, but my guess is that probably you're never good at getting far in research (like humans can) until you can ADD to the list of standard ideas. in that case, the key question is: as some sort of list-iterator kind of thinker, is there a point at which you become good at adding to this list as well
	* how could one have come up with that idea? some ways:
		* by doing that on a small example, maybe
		* by going through a list of graph notions, asking if each could be relevant (that is sth like: going from the side of methods/method-components, needing to notice when a generic thing can be specialized to this problem usefully).
		* by having seen a pairing strategy idea before (is it a common one? chatgpt claims yes: https://chatgpt.com/share/69b963fa-aaec-800f-8a1e-d7fe5be9b0fb )
		* one can probably somehow just think about strategies where each position has an assigned move and these are paired? any strategy has an assigned move in a game state, but here we are saying let's try sth simpler: to make the move depend on the position in the cube only, then with the further constraint that we match stuff up. perhaps one can find this by looking for restricted strategies. making a move depend only on some reduced game state is generally a good idea. i'd need to think more about how to come up with the pairing idea
	
maybe a mistake:
* i was looking too much for a concrete strategy?
* maybe i should have pushed harder on the 3-dimensional case. even pushing myself to think differently of the 2-dimensional case could have been helpful?