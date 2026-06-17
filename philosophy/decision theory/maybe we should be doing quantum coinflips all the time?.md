
  
In this piece, I'll be considering an argument for there being large gains from using quantum randomness for decisions with large effects. I will be assuming a consequentialist view of ethics in this piece, though I don't think this is critical for this argument. It seems likely that this is already in the lesswrong water supply, but I haven't been able to find a reasonable existing writeup of these things.  
  
Suppose you are trying to decide between pursuing plan $A$ or plan $B$. For example, maybe you're a person deciding which of two people to marry, or maybe you're humanity deciding whether to implement an AI moratorium. Let's say that you think plan $A$ is higher EV than plan $B$. Consider the following possible ways you might go about such a decision:  
  
> Guess. Just pick $A$. (Recall that you think $A$ has higher EV than $B$.)  
  
> Random. Have digit $123456789$ of $\pi$ calculated.[^1] If it is even, pursue $A$; if it is odd, pursue $B$.  
  
> Quantum. Flip a fair quantum coin to decide whether to do $A$ or $B$.  
  
> Splitting A/B. Implement $A$ in half the lightcone, implement $B$ in the other half — there's a magical causal separation guarantee between the two parts. (This one doesn't easily make sense with the marriage example I guess — just think about the moratorium then.)  
  
> Splitting A/A. $A$ in half the lightcone, also $A$ in the other half, magical causal separation guarantee between the two parts.  
  
> Doubling. This universe is split into two copies (in what sense? idk). In one, you do $A$; in the other, you do $B$.  
  
  
A canonical consequentialist position is that Guess beats Random, and Doubling is quite a lot better than either[^2]. Let's say the problem is set up such that no further interesting decisions are made (ignoring the consideration that maybe this makes it so the universes are not that valuable after all) so Splitting A/A is roughly as good as Guess, because it will roughly be the same thing. Now there's an argument from caring about entities to be made (along the lines of https://kaarelh.github.io/philosophy/fanaticism.html ) for Splitting A/B being worse than Splitting A/A — indeed, for Splitting A/B being essentially as good as Random — but it currently seems more likely to me that actually, value scales such that Splitting A/B is quite a bit better than Splitting A/A — indeed, it seems plausible that diminishing returns to value from additional scale mean that Splitting A/B is nearly as good as Doubling. (The intuition here is sth like: both halves of the lightcone have enough space for almost all the worthwhile structures they'd implement in a full universe to still be implemented.) This leaves us with Quantum. The naive position is that Quantum is as good as Random. But if we buy many-worlds, then I guess there's a case to be made that Quantum is actually quite a bit like Splitting A/B, in which case would be quite a bit better than Random or Guess.  
  
I'm sorta feeling like there's almost some brute ethical decision to be made here about how to value different quantum soups of futures — in particular, whether these are close to respective epistemic-probabilistic soups or respective lightcone-splitting soups. Or maybe I want to say that this is as much of a brute choice as how to value lightcone-splitting soups compared to epistemic-probabilistic soups. That said, I don't think the latter is that much of a brute decision actually. I guess I'm just feeling like I'm presently lacking considerations to bring to bear on how to value different quantum soups.  
  
One could try to come up with some heuristic model here that tells you how to optimally split reality-fluid in particular cases of practical interest (eg for deciding which potentially extinction-averting project to pursue)  
  
## counterarguments to having to quantum coinflip a bunch  
  
* confused/wrong about some quantum stuff  
* the quantum thing is happening all the time anyway — stopping to specifically do it at what feel like major decisions actually changes little  
	* maybe there's already a vast space of universes from past quantum branchings + mathematical multiverse stuff etc making considerations about improving EV in our slice of the portfolio dominate almost always actually (can set up something concrete here I guess) — we are falsely imagining that we are creating two pretty unique things by doing the quantum coinflip, whereas really it's just more of the same  
* maybe there's actually some rationality requirement (or selection pressure or something) which forces us to treat realityfluid as epistemic randomness in such cases? i guess the issue with this is that it seems sorta fine to break independence here, much like it is fine to break 'independence' when treating Splitting A/B as much better than Random. you can view epistemic-lottery A and epistemic-lottery B as equally good, but prefer to split the lightcone between the two over each  
* maybe we actually have to think of Random just this way anyway? i guess in the $\pi$ case above, this would start to feel particularly compelling if somehow logically impossible universes were also real. actually, this makes me want to investigate what it is that we have in mind when we say something is real, and whether I really want to make as much hinge on this as I'm doing here. I have a hunch that this line of thinking ends up at Garrabrant's view (probability as caring)  
(* and an obvious non-object-level counterargument: this seems sorta insane)


## calculation attempt

an example calculation (for optimal lightcone splitting, but it also applies to the quantum case in case it's right to view it as precisely analogous to splitting the lightcone):

suppose A has a 2/3 chance of tiling its lightcone with cool stuff and B has a 1/3 chance of tiling its lightcone with cool stuff, and these are independent

say the value from having an $f$ fraction of the lightcone tiled with cool stuff is $\log (1+1000f)$. (this is roughly saying that value is linear up to $1/1000$ of the lightcone being tiled, and logarithmic after that)

if we allocate a fraction $q$ to $A$ and a fraction $1-q$ to $B$, the EV is $\mathbb{E}[\log(1+1000f)]=\frac{1}{3}\cdot\frac{2}{3} \cdot \log 1 + \frac{2}{3}\cdot \frac{2}{3}\cdot \log(1+1000q)+\frac{1}{3}\frac{1}{3}\log(1+1000(1-q))+\frac{2}{3}\frac{1}{3}\log(1+1000)$, which is maximized at $q=4003/5000$

the optimum being at giving 80% to A and 20% to B isn't that uneven

[^1]: I'm using this instead of a coinflip because I think there's a significant chance that a coinflip is quantum-random: https://www.lesswrong.com/posts/9KW7oLQepcgu4LkFN/are-coin-flips-quantum-random-to-my-conscious-brain-parts .
[^2]: let's ignore the negative utilitarian view or set up the problem such that even negative utilitarians agree that these universes existing would be good
