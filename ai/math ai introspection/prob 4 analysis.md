

### structures involved in solving this problem

I probably needed to create some representation of a thing from which balls are drawn here; in this case, I thought they are drawn without replacement. This could be represented by a set $S$ which contains elements with a binary color attribute, and if by default I’d think about samples as sequences of draws, I could be thinking about an ordered list of $20$ distinct elements of $S$. And then the problem can be formally asked as counting the number of ordered lists that satisfy a certain property — namely, the property that if I look at the color attribute of its elements, the list I get contains exactly $k$ red balls. I’m not sure what the most appropriate way to build this representation is. What are the elements of $S$ like? I guess they could just be $\{1,2,3,\ldots,100\}$, and colors could be given by a mapping $c\colon S\to \{\textbf{red},\textbf{green}\}$ about which nothing is known except that it sends $30$ things to $\text{red}$ and, therefore, $70$ things to $\text{green}$.

I guess the problem setup is really more directly captured by just: there is a set $S$ with a coloring map $c\colon S\to \{\textbf{red},\textbf{green}\}$ such that $|c^{-1}(\textbf{red})|=30$ and $|c^{-1}(\textbf{green})|=70$. And we then have a random sample of size $20$ from $S$ without replacement, i.e., a sequence of $20$ distinct elements of $S$, which I guess is maybe minimally formalized as a uniformly random map $s\colon [20]\to S$. A uniformly random map could be formalized in the usual way with measures (we assi). We could also just go with counting here, though

a trick: Instead of 

- Looking at the color attribute could be

I later notice that one can just count subsets instead because each subset contributes the same number of sequences. I guess maybe this can be stated

there is a map from subsets of $S$ of size $k$ to

