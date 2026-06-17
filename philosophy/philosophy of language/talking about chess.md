
* what does it take to play chess?
	* i guess it's sufficient to be playing legal rules. what does it take to play legal moves?
		* we could make a machine that is just forced to play legal rules (like, it outputs a bitstring which must get interpreted as a move from some given set)
		* in humans, in almost all cases, the ability to make legal chess moves when playing with a physical chess board probably depends on the following:
			* understanding that there is a game board consisting of squares
			* understanding that there are these moving things called pieces
			* understanding that if a piece is on the board, it must be on a particular square
			* understanding that pieces come in types — pawns, knights, bishops, rooks, queens, kings — with the type indicated by the shape of the piece
			* understanding that there are two players and each piece belongs to one player or the other, with belonging indicated by the color (white or black) of the piece
			* etc (there should be a finite number of extra lines in this list. maybe like 15 more lines? well, one could maybe dig deeper...)
		* ok, maybe you don't need to understand these things, and often do not understand them, at least not that explicitly. for example, maybe instead of understanding there are two players, with each piece belonging to one, you can get away with just having a fairly implicit constraint in your move-considering algorithm to only consider moves with color x pieces. i think this is reasonably accurate "phenomenologically"
			* generally: there's a lot of just doing stuff, without explicit understanding
* ok, but now we want to start talking about chess. eg imagine a chess broadcast with commentary about the game
	* why did we want to talk about it?
		* maybe we want to talk about it to become better at it?
		* maybe we want to learn from it? we want to apply our chess understanding to another context?