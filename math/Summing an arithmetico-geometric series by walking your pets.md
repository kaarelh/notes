## An anecdote
The following anecdote is [roughly true](https://courses.cs.vt.edu/~cs1104/ProblemSolving/Trains/Train.html). Von Neumann was presented the following problem at a cocktail party:
>A man is walking from home to a store $1\text{ km}$ away with speed $v= 5\text{ km/h}$. His dog starts walking from home at the same time as the man, but the dog walks with speed $u=2v=10\text{ km/h}$, running back and forth between the man and the store. What's the total distance traveled by the dog?

After thinking about it for $5$ seconds, von Neumann answered $2 \text{ km}$, to which the guy who had posed the problem replied with "Nice, you saw the trick so quickly!" And then von Neumann was like, "What trick? I just summed the infinite geometric series."

## Explaining the joke
The trick is to note that as the dog is moving twice as fast as the man, and as the man moves a total of $1 \text{ km}$, the dog must move a total of $2\cdot 1 \text{ km}=2\text{ km}$. But if one partitions the dog's trajectory according to when it meets the man, one gets a geometric series with first term $2-\frac{2}{\frac{u}{v}+1}$ and ratio $1-\frac{2}{\frac{u}{v}+1}$.

## A proof of the formula for the sum of a geometric series
Taking a different perspective at the above, we have a proof that an infinite geometric series with first term $2-\frac{2}{\frac{u}{v}+1}$ and ratio $1-\frac{2}{\frac{u}{v}+1}$ sums to $2$. This implies that the infinite geometric series with first term $1$ and ratio $1-\frac{2}{\frac{u}{v}+1}$ sums to $\frac{1}{1-\frac{1}{\frac{u}{v}+1}}$.
Letting $\frac{u}{v}$ vary gives the infinite geometric series sum formula for all ratios $0<r<1$. One can get finite ones by subtracting two infinite series, and then get the sum formula for all other finite geometric series via the complex analysis fact about two 

## Other decompositions prove summation formulas for other series
One can also get a formula for the sum of the arithmetico-geometric series by partitioning the segment according to the number of times the dog ran across each bit. And one can add a cat running back and forth between the dog and the 