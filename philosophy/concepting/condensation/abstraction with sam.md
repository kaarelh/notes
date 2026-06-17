
book: network information theory

## questions to ask sam

suppose we understand concept formation in mathematics. have we then understood all there is to understand about concept formation? or are there phenomena which do not show up much in math?

do you not see GOFAI people as having tried to do similar things to algorithmic condensation? eg minski's frames? hmm i guess maybe that's just trying to give broad strokes about what type of thing mental structures are, but you're further trying to say something about which particular structures would be desirable. anyway, have you read much GOFAI stuff? do you consider it worth reading? were they not taking thinking seriously enough? were they assuming that logic was already finished?

can you tell me your story for how concepts form? do you see condensation as approximating some part of that story?

have you thought about more local versions of condensation? where the variables get chosen with some local rules? any realistic process that forms concepts would probably operate locally anyway i guess. tho maybe we still need the global thing to get to where a mind is at — that seems distinct

can we solve multiterminal coding a function or else show it can't be solved? 

we could just work on some writeups?

what kind of structure should these ideas that condensation or ideal-SAEs find fit into? probably not circuits right? more like parts of a system of reasoning? maybe more like terms in a first-order language?



this motivates: we might take them seriously as terms, and look for predicates and functions applied to them or something? and logical connectives also? should these live in the weights?

do you expect that 'how do we make these systems understandable to us' is the wrong question in interp, vs 'what are these systems doing' or something

do you think there are 'laws of optimization/thinking/reasoning' that are sort of like laws of physics waiting to be discovered?

is statistical mechanics observer-relative? ie something weird is going on with the choice of microstates and macrostates? is there an objective thing here?

what's up with seeing yourself as a computational system vs a reasoning system? any descriptions of gödel/löb/tarski style logic stuff for agents that are reasoning which you'd recommend? do you have any recommendations for reading on this?

eg abram gave a talk at the agent foundations workshop about some löbian difficulties with reasoning systems or something



why church turing true? why aren't there different kinds of maths? can't we imagine something that solves topology but not number theory? can't we imagine something that solves some very different kind of math but not our kind?

the example of linguistics? abstractions are phrases? what would the optimization problem be?

I've been thinking a bit about what kind of condensation optimization problem would be solved by the syntax trees of sentences (i.e., the variables would correspond to phrases) — I don't have much progress on this really, just thought I'd mention this example in case you hadn't thought about it already, as it seems like a neat concrete problem of standalone interest. (One can also ask the same question 

also something with finite state automata? context-free grammars? states are abstractions?

# other

to say:
* we were wrong about the XOR of two correlated coins. one can actually do it at the conjectured optimal rates! ie 1/2 bit for each. we were wrong to think that if you see a pair of buckets, you have to think the coins are in some product set. i think this is probably true for independent latents, but false in general. the construction is to pick a random subspace and send its coset on each side. you won't be able to deduce the pair of coinflip sequence exactly, but you will be able to deduce them up to the same shift on each side
* that said, i think if you have two independent coins as the latents and make the observable their AND, then i think you need rates $r_1=r_2=1$ even though the conditional mutual information is $I(X;Y_1|Y_2)=1/2
* i think this is probably true for any function of independent latents which does not have 'domain redundancies', ie doesn't have two things in any domain which are functionally equivalent. i think i can probably prove this in like a few hours. for independent variables, one indeed has a bucket pair correspond to a product set of plausible sequences, and the idea is that AND doesn't act nicely with this product structure — there will be many bucket pairs which don't have AND being const
* this also gives some potentially interesting examples 
* we had this question about the wyner common information case with the relaxation that we don't require $r_1+r_2+r_{12}=H((X_1,X_2))$, you had a conjecture and thought that wyner's proof would work. yea i can prove it with something close to their argument (i maybe have a slightly nicer version)
* 


things to write:
* the rate-[multi-utility] theorem with wyner's common information result as a corollary
* maybe separately the noisy channel rate-utility theorem (here can probably make the mutual information be the product of the rate and the channel capacity)
* the multiterminal source coding result:
	* [independent latents, no equivalent inputs] => [can't compress at all]
	* but can compress XOR optimally

things to figure out:
* can we get some r.v.s->coding result for condensation by sampling joint latent settings and just picking the best one (ie will this work for all observation variables at once as desired) 


https://people.eecs.berkeley.edu/~courtade/pubs.html

maybe instead of having strings as the things to be compressed, have functions? can we get close to some discrete program synthesis thing this way? (got this idea when reading the abstract of https://arxiv.org/pdf/2012.00377)

so now each X_i becomes a function, maybe given as a table. and you have to write a library of programs that can do all of these functions.  


a question to ask sam: the gödel completeness theorem is a particular instance of the claim: "a way to speak is coherent iff it is about a world". are there other interesting instances of this? maybe generalizations?


I'm sort of confused about why the noisy channel theorem and the rate-distortion theorem aren't presented as special cases of the following theorem/conjecture:
> Claim 1. Fix a utility function $u\colon \mathcal{X}\times \mathcal{W}\to \mathbb{R}$. Fix an input random variable $X$, i.e., with domain $\mathcal{X}$. For a noisy channel with capacity $C$, the supremal expected average utility over coding schemes of input $X^n$ to output $W_c^n$ through that channel is $$\sup_{\text{joint distributions on }X \text{ and }W \text{ marginalizing to the given distribution on }X\text{ and with }I(X;W)<C}\mathbb{E}_{p(x,w)}\left[u(X,W)\right].$$

Some corollaries:
* If the channel has no noise (and maybe $\mathcal{W}=\mathcal{X}$), then we should get the rate-distortion theorem.
* If $\mathcal{W}=\mathcal{X}$ and the utility function is a delta function (and maybe with $X$ being a coinflip), we should get the noisy channel theorem.
* If If $\mathcal{W}=\mathcal{X}$ and the utility function is a delta function and the channel has no noise, then we should get the source coding theorem.
I suspect I've said something incorrect here, because this seems like a nice way to present a bunch of stuff, but I can't find a theorem that's equivalent to Claim 1 in the literature. I don't have a proof of Claim 1, but I also haven't thought through whether the obvious meta-strategy of trying to combine the proofs of the rate-distortion theorem and the noisy channel theorem works. Anyway, maybe Claim 1 is false? I haven't properly thought through whether Claim 1 really implies these theorems in full either. I'd be interested to hear if you can see that something above is incorrect or if you know of something like this is in the literature.


I'm not sure, but I guess the rate-distortion theorem says that Claim 1 is true for a noiseless channel, and then you can get [whatever the optimal noiseless channel construction sends] [through a noisy channel as well] [by the noisy channel theorem], so the sup is a lower bound on the attainable expected average utility for any channel.


But I guess the sup is also an upper bound because if you have a way to send stuff through your channel with some expected average utility, then you can get a joint distribution on (X,W) with the same expected utility and mutual information at most C as follows (this might be the standard method idk, or maybe it's not but then whatever else is the standard method would maybe also work):
* Let (X,W) be given by taking a random sequence X^n, choosing an index i uniformly at random in [n], letting X be component i of the sequence, and letting W be component i of the output of this sequence through the given channel.


So maybe Claim 1 is true? (idk still likely i've made some silly errors)

Let's attempt an independent proof. We already have from above that each coding thing gives a random variable with the same expectation, so the random variable thing is at least as good as the coding thing. (Maybe a better theorem would say that the set of possible expected utilities is the same.) It remains to take the random variable thing and to construct a coding thing. I guess maybe the idea here in the deterministic case (rate distortion) is to just sample a bunch of sequences of a given $W$ and make codewords that correspond to to all those sequences, and then one assigns each $x^n$ to the best codeword. What about the noisy case? Maybe fix 

I mean, I guess we could make the codewords 











I'm sort of confused about why the noisy channel theorem and the rate-distortion theorem aren't presented as special cases of the following theorem/conjecture:
> Claim 1. Fix a utility function $u\colon \mathcal{X}\times \mathcal{W}\to \mathbb{R}$. Fix an input random variable $X$, i.e., with domain $\mathcal{X}$. For a noisy channel with capacity $C$, the supremal expected average utility over coding schemes of input $X^n$ to output $W_c^n$ through that channel is $$\sup_{\text{joint distributions on }X \text{ and }W \text{ marginalizing to the given distribution on }X\text{ and with }I(X;W)<C}\mathbb{E}_{p(x,w)}\left[u(X,W)\right].$$

Some corollaries:
* If the channel has no noise (and maybe $\mathcal{W}=\mathcal{X}$), then we should get the rate-distortion theorem.
* If $\mathcal{W}=\mathcal{X}$ and the utility function is a delta function (and maybe with $X$ being a coinflip), we should get the noisy channel theorem.
* If If $\mathcal{W}=\mathcal{X}$ and the utility function is a delta function and the channel has no noise, then we should get the source coding theorem.
I suspect I've said something incorrect here, because this seems like it would be a nice way to present a bunch of stuff, but I can't find a theorem that's equivalent to Claim 1 in the literature. I don't have a proof of Claim 1, but I also haven't thought through whether the obvious meta-strategy of trying to combine the proofs of the rate-distortion theorem and the noisy channel theorem works. I haven't properly thought through whether Claim 1 really implies these theorems in full either. I'd be interested to hear if you can see that something above is incorrect or if you know of something like this is in the literature.


I'm sort of confused about why the noisy channel theorem and the rate-distortion theorem aren't presented as special cases of the following theorem/conjecture:
> Claim 1. Fix a utility function $u\colon \mathcal{X}\times \mathcal{W}\to \mathbb{R}$. Fix an input random variable $X$, i.e., with domain $\mathcal{X}$. For a noisy channel with capacity $C$, the supremal expected average utility over coding schemes of input $X^n$ to output $W_c^n$ through that channel is $$\sup_{\text{joint distributions on }X \text{ and }W \text{ marginalizing to the given distribution on }X\text{ and with }I(X;W)<C}\mathbb{E}_{p(x,w)}\left[u(X,W)\right].$$

Some corollaries:
* If the channel has no noise (and maybe $\mathcal{W}=\mathcal{X}$), then we should get the rate-distortion theorem.
* If $\mathcal{W}=\mathcal{X}$ and the utility function is a delta function (and maybe with $X$ being a coinflip), we should get the noisy channel theorem. (I guess the source coding theorem is the further special case where the channel is deterministic.)
I suspect I've said something incorrect here, because this seems like it would be a nice way to present a bunch of stuff, but I can't find a theorem that's equivalent to Claim 1 in the literature. I don't have a proof of Claim 1, but I also haven't thought through whether the obvious meta-strategy of trying to combine the proofs of the rate-distortion theorem and the noisy channel theorem works. I haven't properly thought through whether Claim 1 really implies these theorems in full either. I'd be interested to hear if you can se that something above is incorrect or if you know of something like this is in the literature.

Is this theorem false? 

some questions to maybe ask:
* what's the good judeapearlian argument in favor of models needing to be intervention-trained to become capable, if there is one? like, there's the stuff about causal graphs sorta not being learned from observation alone in some cases or something, but ykno, who cares. all we have are observations sorta anyway. you can always take a step back and view everything as observations. a human taken outside the universe could probably easily understand what's learned in the future by just observing others doing experiments. is there a good version of this stuff? i mean i can imagine some stuff about needing to play around with stuff to learn, but that starts to feel quite far from the pearl thing to me

Wyner-Ziv ( https://www.mit.edu/~6.454/www_fall_2001/kusuma/wynerziv.pdf ) seems compatible with the conjecture to me so far. To me, the most immediate case where the conjecture can be checked against Wyner-Ziv is this:
* Let's say we have latent variables $Y_1$ and $Y_2$, and observed data $X$ which is a function of 

The special case of the conjecture about which 



rate-distortion theorem

https://en.wikipedia.org/wiki/Slepian%E2%80%93Wolf_coding#:~:text=In%20information%20theory%20and%20communication,two%20lossless%20compressed%20correlated%20sources.

https://www.mit.edu/~6.962/www_fall_2001/kusuma/summary.pdf

https://www.mit.edu/~6.454/www_fall_2001/kusuma/wynerziv.pdf

https://web.archive.org/web/20130228072239id_/http://csc.ucdavis.edu:80/~rgjames/static/pdfs/infotheory/Wyner_-_1975_-_The_common_information_of_two_dependent_random_variables.pdf




## questions to ask sam
do you expect that 'how do we make these systems understandable to us' is the wrong question in interp, vs 'what are these systems doing' or something

do you think there are 'laws of optimization/thinking/reasoning' that are sort of like laws of physics waiting to be discovered?

is statistical mechanics observer-relative? ie something weird is going on with the choice of microstates and macrostates? is there an objective thing here?

what's up with seeing yourself as a computational system vs a reasoning system? any descriptions of gödel/löb/tarski style logic stuff for agents that are reasoning which you'd recommend? do you have any recommendations for reading on this?

eg abram gave a talk at the agent foundations workshop about some löbian difficulties with reasoning systems or something



why church turing true? why aren't there different kinds of maths? can't we imagine something that solves topology but not number theory? can't we imagine something that solves some very different kind of math but not our kind?

the example of linguistics? abstractions are phrases? what would the optimization problem be?

I've been thinking a bit about what kind of condensation optimization problem would be solved by the syntax trees of sentences (i.e., the variables would correspond to phrases) — I don't have much progress on this really, just thought I'd mention this example in case you hadn't thought about it already, as it seems like a neat concrete problem of standalone interest. (One can also ask the same question 

also something with finite state automata? context-free grammars? states are abstractions?
### notes from meeting on Tue dec 19
in the algorithmic information theory version, there's no independence question, but the length condition prefers that you split stuff up when you can
can maybe handle the information theory version similarly by replacing the entropy of y intersect a with a sum of entropies of the variables that appear in it?
what algo info theory framing fails to capture: low-level and high-level abstractions at once? and how they relate to each other? are these just versions with different k vs t complexity tradeoff? ie different runtimes?

## meeting eisenstat

the origins of analytical philosophy michael dummett
the logical basis of metaphysics
frege philosophy of language

related stuff:
* common information
* shared and complementary information
* causal networks, causal structure learning
* factored sets
* sparse dictionary learning
* compression
* non-negative matrix factorization, tensor decomposition

![[Pasted image 20231215012349.png]]

![[Pasted image 20231215063337.png]]

mostly, would be interested to hear more about condensation

is there a version of this possible world stuff where out of which one gets a reasonable metric between possible worlds?
why long timelines?
probability of solving philosophy in time? 

function->programs

set of program 

say you have a bunch of agents that always have the policy of picking higher on their respective utility functions

for each option, can define indifference step by a delta change => preference switch condition