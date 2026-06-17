
# a formalism
Suppose we have two languages, $A$ and $B$; we identity a language with its set of sentences. Suppose we are given a probabilistic translation $T\colon A\to \Delta(B)$, where $\Delta(B)$ denotes the set of probability distributions on $B$ — i.e., each sentence in $a\in A$ is getting sent to a probability distribution $T(a)\in \Delta(B)$ over sentences that can be written in the language $B$. Now, given $\mu_B\colon B\to [0,1]$, which we think of as an assignment of probabilities to all the sentences in $B$, we can pull it back along $T$ to $\mu_A\colon A\to [0,1]$, which we think of as an assignment of probabilities to all sentences in $A$, as follows:
$$\mu_A(a)=\mathbb{E}_{b\sim T(a)}\left[\mu_B(b)\right].$$

That is, to find the probability of $a\in A$, we take the expectation over its possible translations $b\in B$ of the probability of $b$ under $\mu_B$. 

Suppose the probability assignment to $B$ is coherent, and the translation is 'good'. Will the probability distribution on $A$ also be coherent? I think the answer is yes, at least in some very specific case. Namely, if $B$ is a more precise language on which we have a probability distribution induced by a probability distribution on models and each sentence in $A$ maps to a bunch of sentences equivalent to each other, then they must all get the same probability, so the sentence in $A$ just gets that probability, and I'm pretty sure this will just give a coherent probability distribution on $A$.

I guess one generally open problem here is whether the translation should take tuples of sentences in $A$ to tuples of sentences in $B$, or even be a probability distribution of entire maps of $A$ to $B$. One example reason for there being some structure of this kind is that if we take $a_1$ to $b_1$, that might make it less likely that $a_2$ is taken to $b_1$ also.

## a toy case

For a toy setting in which some issues arise, let the language $B$ just consist of the following two sentences:
$$B = \{\text{`The bill was tabled yesterday.', `The bill was indeed tabled yesterday.',`The bill was not tabled yesterday.'}\}.$$
Consider the probability assignment that assigns the first two sentences probability $90\%$, and the last sentence probability $10\%$. This is an internally consistent assignment of probabilities. However, I think translating to a more precise language as specified above, then making the resulting assignment there coherent, and then translating back, could return a different assignment of probabilities. This seems intuitively somewhat undesirable.

Let's think about what translating this into a more precise language $A$ might look like. In British English, to table a bill is to put it up for debate; in American English, to table a bill is to remove it from debate. Let's suppose we are in a context where the bill was certainly either put up for debate or removed for debate. Let's say we have a more precise language $A$ that lets us disambiguate between these two meanings:
$$A=\{\text{`The bill was put up for debate yesterday.', `The bill was removed from debate yesterday.'}\}.$$
Let's say we're intuitively assigning equal probability to saying ambiguous stuff in British English or American English, so the precise-language statement $\text{`The bill was put up for debate yesterday.'}$ would with probability $25\%$ be stated 

translation map takes either sentence in the precise language $A$ to a uniform distribution 

## another toy case

a clearly true formal statement that can be what's meant by a suspicious informal statement sometimes. then assign a reasonable probability to the suspicious informal statement. now translate to formal, will get problems, will flow prob down. 

'everything point-set is self-similar'

has obviously true interpretation, and an obviously false interpretation. assigning $50\%$ to this brings down prob of obviously true interpretation. this will be ironed out by the coherentization process. then when translate back, can get from coherent to lower probability. but this is silly

## maybe map joint assignments of truth-values to $B$ to joint assignments of truth-values of $A$ instead?

## how does the translation get created-trained?