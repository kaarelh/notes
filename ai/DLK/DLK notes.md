'Use DLK to find a direction in 

  

two ways to think of nonlinear probes:

1.  project to a curvy direction
2.  send whole space through some learned feature map first, then find direction
3.  maybe just some PCA first? and only then find direction in subspace?
4.  The inverse scaling law stuff matters maybe because it is another testing ground for whether DLK can tell us stuff about the model beyond output behavior

One way to think of the Discovering Latent Knowledge (DLK) paper, as well as of the extension my team is pursuing, is that anything inside a model satisfying particular structural properties is truth/probability (or at least hopefully that's the case). In a conversation, Alexandre Variengien suggested generalizing this to trying to write down structural properties that some other particular high-level conceptual feature (maybe e.g. style, language, sentiment) should satisfy, and then analogously using these features to constrain the search for how the feature is represented inside the model.

  

I think an example he gave (+possibly wrong but hopefully clarifying details added by me) was something like taking a model doing picture -> 3D scene, and trying to find the model's understanding of the orientation of an object by searching for a probe whose outputs capturing the model's understanding of 

  

  

  

 inputting pictures of an object from various angles (these are analogous to contrast pairs in DLK), and finding a 3-dim subspace of some inner layer activation space in which the projections of the activations of the "contrast pictures" have appropriate SO

  

Trying to come up with other such features + constraints seems like an interesting and useful problem to me, as it could help us extract the settings of a model's high-level concepts. If you can think of any leads for how to do this for style, I'd be really interested in hearing that. Can we write down structural constraints that capture vibe? Can we describe some symmetries preserving vibe?

  

(Or if you have any thoughts along these lines more generally, I'd be very interested to hear them. I guess one issue is that one wants the structural constraints to approximately uniquely capture the high-level concept, i.e. one wants something like "most of the measure in conceptual space satisfying the set of constraints being carried by the concept we are actually after". This might point towards the approach only being feasible to carry out for particularly natural concepts. Though maybe there is some sort of natural set of constraints for any concepts, I'm not sure. When does the "shape of a concept" capture the concept approximately uniquely?)


is there a mapping concepts <-> symmetries, constraints, this is like finding the shape of a concept

  

In a physics simulator, could we use conservation of momentum to find the inner concept of space? Suppose that this is nontrivial because the input is in some fucked-up format

  

Or maybe we could just use Noether's theorem. Translate the same system in space, see what's conserved. Maybe that's momentum?

  

Let's say we have a fine-grained hard-coded model that implements a gas consisting of a bunch of particles, and let's say we train a model that has to do some stuff on a higher level of abstraction. Will it end up re-learning stuff like temperature and pressure? Can we find these inside the model using Noether's theorem type stuff? 

  

style, language, sentiment, authenticity, honesty, clarity, tone, mood of author while writing as changing from sentence to sentence, mood of described character

  

what's the shape of a concept, becoming some kind of continental philosopher

  

suggested by Jan Kulveit: Try to find an understanding of game theory inside the model.

  
some of this is from discussion with John:
conditional independence, implications, conditional probability

  

substituting words in sentences for "it"

  

look for direction in language model

  

duration?

  

inside and outside, containment, subsets

  

system of equations numerically unstable?

  

mirroring

  

John's formulation: semantic constraints on concept -> functional equations -> search for soln of functional equations inside a model

  

shapes <-> categories?

the shape of corrigibility?

DLK = ramsification applied in practice to find truth :O (I'd guess June Ku probably had this insight?)

So, what's a ramsified definition of style? or mood? and can we search for that kind of structure in language models?

Look for more elaborate structures INSIDE ONE RUN of the model, not between different runs

search goals, beliefs standing in right relation to each other, suggested by Peli

  

ideal inquiry, truth, putnam, maybe circular

put in implications into loss, for superhuman model this should differentiate true beliefs from representations 

the shape of a world model

could test ideas by looking for shape of syntax tree like in https://aclanthology.org/N19-1419.pdf but in an unsupervised way. thoughts on how to do this:
1. For each matrix, try every tree, see which one captures distances best
2. Put min over trees in the loss, optimizing this gives a best matrix
3. then can recover tree by finding best tree along this direction for each example

If this is too computationally expensive, could do best tree search by going greedily bottom-up: just find the closest adjacent clusters and merge them? And can replace inference step by this as well. or minimum spanning tree? I think this is what they actually use to reconstruct an implied tree in the paper
https://mathoverflow.net/questions/135253/recovering-a-weighted-graph-from-shortest-path-distances

Maybe could think of this as finding phrases instead, hopefully clusters in rep space correspond to phrases?

capture recursion better somehow? when replace a word with multiword phrase, want rep of phrase to be same?

shape of search? can we find places in a model where it is doing search?

Instead of adversarial contexts, put in contexts which make it really care about truth. If the inner truth representations are robust, it should not matter that way either? Though it might be that these becoming better does not contradict the claim that the inner reps give the model's truth representation – maybe it's just that the truth representation becomes more pronounced in this case.
Also check DLK against zero-shot but prompt engineered to be truthful. (Do they already do this?)


https://arxiv.org/pdf/2212.01681.pdf says that LMs simulate agents. But they also need some outer knowledge to simulate agents right, and this is what we are hoping to capture in this whole thing? -> search for commonalities between reps when pretending to be different agents? Or maybe ask the LM to simulate itself?

Train on math truth (safe kind of data), then see if found direction generalizes to other prompts

Try to come up with an unsupervised version of http://ai.stanford.edu/blog/scalar-probing/, or more generally https://arxiv.org/abs/2010.05345
Ok so could require e.g. $\frac{\text{weight of elephant}}{\text{weight of mouse}} = \frac{\text{weight of elephant}}{\text{weight of dog}}\frac{\text{weight of dog}}{\text{weight of mouse}}$. Actually does this make any sense? I guess we can input sentences which get at these ratios, but it is sort of weird? Maybe currency conversions are more natural?

try t-SNE?


I wonder if instead of looking for orthogonal directions, it would be more efficient to look for directions which disagree with the predictions of any direction found previously? I.e. add something like min_{direction in {previous directions}} [correlation with direction]^2 to the loss when finding the next direction.  This captures the idea that if the same concept of truthiness is represented along many directions,  (I have not read most of the stuff in this conversation – sorry if this idea has been discussed already.)

world model type = func from current state to future state?

suggestion from Alex: Numerical range questions where can easily get additive properties

additive for obviously mutually exclusive options


p(A and B)+p(A or B)=p(A)+p(B)

try to get chatGPT to construct natural propositional combinations

truth<->goodness<->consensus

check for religious claims, to 
other places where people commonly believe falsehood but scientific consensus is other thing?

automatically look for causal graph by getting whatever Pearl's independence assumption stuff for features?

game with n options for moves, find in policy network numbers such that value head always gives max of these in a way that's distributed across all – these numbers might be the conditional expected future rewards on taking these moves.

maybe can generalize to searching for search loops?


In Alexandre's email, just take functional form of S^2 -> direction 


from meeting with Alex:
utility thing needs variance term to avoid trivial solutions, also want to send thru sigmoid (only look at features like that) to avoid it blowing up

framework seems good

in AGI level model, can maybe get its own probabilities using DLK and then search for utilities

have policy network RL agent, put position and next, these give contrast pair, find value, ask Walter about whether this is feasible 
to avoid trivial solution, do DLK confidence, or put in variance, or do a little bit of supervision
AGI limit have it play in simulation against itself??

image classifier supervised leaf, can we come up with some construction for unsupervised thing to look for
or can we use supervised probing to combine concepts?

constant output

even narrative form -> concept relations framework might be helpful? maybe put this as recommendation at least?

want properties more generally, not just those from relations
eg high variance, low complexity feature

see if in syntactic subspace, parts that have undergone movement are still close to pre-movement close words?
https://en.wikipedia.org/wiki/Syntactic_movement#Illustration


this is fitting group elements in high-dim spaces as matrices? sort of another example of weird thing to embed in R^n https://twitter.com/bilalchughtai_/status/1625948104121024516?t=uwP93mX4WJX-hTQoOmN1BQ


   To capture supervised or semi-supervised probing, we also allow the equation
   [One could also recover supervised probing by having one property per data point with just one contrast set consisting of that one data point alone and the equation checking that the feature value matches the concept value, but this does not respect the spirit of the present framework.]
   
editorial remark: need to figure out how to merge vertical cells in this table and how to cross out cells. maybe should switch to latex for this...
| Goal + other description| Kind of model | Concept set $\mathcal{C}$ |Property $p\in \mathcal{P}_\mathcal{C}$ (verbal description) | $I_p$ (for contrastive $p$) | $T_p$ (for contrastive $p$)| Example contrast tuple | $E_p$ (for contrastive $p$) |$\ell_p$, loss from a contrast tuple | $L_p$, loss from $p$|$\mathcal{L}_\mathcal{C}$, total loss| 
|------------ | ------------|------------|------------|------------|------------|------------|------------|------------|------------|------------|
|Determine beliefs of a model (DLK)| language model |
|Determine beliefs of a model| language model |
|Determine beliefs of a model (DLK on steroids, probabilistic version)| Content from cell 2|
|Determine beliefs of a model (DLK)| Content from cell 2|
|Content in the first column | Content in the second column|


try loss = min + (1-max)? instead of having sum rule at all


\begin{tabular}{ |c|c|c| }
\hline
 \multicolumn{3}{|c|}{Search schema for the truth value assignments of a (language) model – DLK/ELK}\\ 
 \hline
 Concepts $c\in \mathcal{C}$  & \multicolumn{2}{c|}{plausibility}  \\ 
 \hline
 Property $p\in \mathcal{P}_\mathcal{C}$ (verbal description) & negation coherence & confidence \\ \hline
 Tuple indexing set $I_p$ (for contrastive $p$) & $\{\text{positive},\text{negative}\}$ & $\{\text{positive},\text{negative}\}$ \\ \hline
 Example contrast tuple (for contrastive $p$) & $(Q,\neg Q)=\left([2+2 \text{ is } 4.], [2+2\text{ is not }4.]\right)$ & $(Q,\neg Q)=\left([2+2 \text{ is } 4.], [2+2\text{ is not }4.]\right)$ \\\hline
 $T_p$, set of contrast tuples (for contrastive $p$) & set of pairs constructed from a list of propositions $Q_i$ & set of pairs constructed from a list of propositions $Q_i$ \\\hline
 Equation $E_p$ with concepts plugged in (for contrastive $p$) & $\text{plausibility}(\neg Q))=1-\text{plausibility}(Q)$ & $\min(\text{plausibility}(Q),\text{plausibility}(\neg Q))=0$ \\\hline
 $\ell_p$, loss from a contrast tuple & $(1-\text{plausibility}(\neg Q))-\text{plausibility}(Q))^2$ &  $\min(\text{plausibility}(Q),\text{plausibility}(\neg Q))^2$ \\\hline
 $\mathcal{L}_\mathcal{C}$, total loss & \multicolumn{2}{c|}{$\sum_{}+\sum_{}$} \\
 \hline
\end{tabular}



| Goal + other description| Applied to what kind of model? | Concepts $c\in \mathcal{C}$ |Property $p\in \mathcal{P}_\mathcal{C}$ (verbal description) | Tuple indexing set $I_p$ (for contrastive $p$) | Example contrast tuple (for contrastive $p$) | $T_p$, set of contrast tuples (for contrastive $p$) | Equation $E_p$ with concepts plugged in (for contrastive $p$) |$\ell_p$, loss from a contrast tuple | $\mathcal{L}_\mathcal{C}$, total loss| 
|------------ | ------------|------------|------------|------------|------------|------------|------------|------------|------------|------------|
|Determine beliefs of a model (DLK)| language model | plausibility | negation coherence | $\{\text{positive},\text{negative}\}$ | $(Q,\neg Q)=\left([2+2 \text{ is } 4.], [2+2\text{ is not }4.]\right)$| constructed from a list of propositions | $\text{plausibility}(\neg Q))=1-\text{plausibility}(Q)$ | $(1-\text{plausibility}(\neg Q))-\text{plausibility}(Q))^2$ |
| | | | confidence | $\{\text{positive},\text{negative}\}$ | $(Q,\neg Q)=\left([2+2 \text{ is } 4.], [2+2\text{ is not }4.]\right)$ | constructed from a list of propositions | $\min(\text{plausibility}(Q),\text{plausibility}(\neg Q))=0$


\newpage

{\tabulinesep=1.2mm
   \begin{tabu}{ |c|c|c| }
\hline
 \multicolumn{3}{|c|}{Search schema for the truth value assignments of a (language) model – DLK/ELK – extended edition}\\ 
 \hline
 Concepts $c\in \mathcal{C}$  & \multicolumn{2}{c|}{plausibility}  \\ 
 \hline
 Property $p\in \mathcal{P}_\mathcal{C}$ (verbal description) & negation coherence & confidence \\ \hline
 Tuple indexing set $I_p$ (for contrastive $p$) & $\{\text{positive},\text{negative}\}$ & $\{\text{positive},\text{negative}\}$ \\ \hline
 Example contrast tuple (for contrastive $p$) & $(Q,\neg Q)=\left([2+2 \text{ is } 4.], [2+2\text{ is not }4.]\right)$ & $(Q,\neg Q)=\left([2+2 \text{ is } 4.], [2+2\text{ is not }4.]\right)$ \\\hline
 $T_p$, set of contrast tuples (for contrastive $p$) & set of pairs constructed from a list of propositions $Q_i$ & set of pairs constructed from a list of propositions $Q_i$ \\\hline
 Equation $E_p$ with concepts plugged in (for contrastive $p$) & $\text{plausibility}(\neg Q))=1-\text{plausibility}(Q)$ & $\min(\text{plausibility}(Q),\text{plausibility}(\neg Q))=0$ \\\hline
 $\ell_p\left( f_{\text{plausibility}}(Q),f_{\text{plausibility}}(\neg Q)\right)$, loss from a contrast tuple & $\left(1-f_{\text{plausibility}}(Q)-f_{\text{plausibility}}(\neg Q)\right)^2$ &  $\min(f_\text{plausibility}(Q),f_\text{plausibility}(\neg Q))^2$ \\ \hline
 $\mathcal{L}_{\mathcal{C}}$, total loss & \multicolumn{2}{c|}{$\sum_{i}\left(1-f_{\text{plausibility}}(Q)-f_{\text{plausibility}}(\neg Q)\right)^2 +\sum_{i}\left(\min(f_\text{plausibility}(Q),f_\text{plausibility}(\neg Q))^2\right)$} \\
 \hline
   \end{tabu}}

\newpage

      {\tabulinesep=1.2mm
      \begin{tabu}{ |c|c|c| }
\hline
 \multicolumn{3}{|c|}{Search schema for the truth value assignments of a (language) model – DLK/ELK – extended edition}\\ 
 \hline
 Concepts $c\in \mathcal{C}$  & \multicolumn{2}{c|}{plausibility}  \\ 
 \hline
 Property $p\in \mathcal{P}_\mathcal{C}$ (verbal description) & negation coherence & confidence \\ \hline
 Tuple indexing set $I_p$ (for contrastive $p$) & $\{\text{positive},\text{negative}\}$ & $\{\text{positive},\text{negative}\}$ \\ \hline
 Example contrast tuple (for contrastive $p$) & $(Q,\neg Q)=\left([2+2 \text{ is } 4.], [2+2\text{ is not }4.]\right)$ & $(Q,\neg Q)=\left([2+2 \text{ is } 4.], [2+2\text{ is not }4.]\right)$ \\\hline
 $T_p$, set of contrast tuples (for contrastive $p$) & set of pairs constructed from a list of propositions $Q_i$ & set of pairs constructed from a list of propositions $Q_i$ \\\hline
 Equation $E_p$ with concepts plugged in (for contrastive $p$) & $\text{plausibility}(\neg Q))=1-\text{plausibility}(Q)$ & $\min(\text{plausibility}(Q),\text{plausibility}(\neg Q))=0$ \\\hline
 $\ell_p\left( f_{\text{plausibility}}(Q),f_{\text{plausibility}}(\neg Q)\right)$, loss from a contrast tuple & $\left(1-f_{\text{plausibility}}(Q)-f_{\text{plausibility}}(\neg Q)\right)^2$ &  $\min(f_\text{plausibility}(Q),f_\text{plausibility}(\neg Q))^2$ \\ \hline
 $\mathcal{L}_{\mathcal{C}}$, total loss & \multicolumn{2}{c|}{$\sum_{i}\left(1-f_{\text{plausibility}}(Q)-f_{\text{plausibility}}(\neg Q)\right)^2 +\sum_{i}\left(\min(f_\text{plausibility}(Q),f_\text{plausibility}(\neg Q))^2\right)$} \\
 \hline
   \end{tabu}}


## Category theory stuff

functor into activations

functional equations happen

relations in diagram -> relations in activation spaces

EACH FEATURE HAS THE STRUCTURE OF A CATEGORY??

example: implication structure. P, P=>Q, Q. (By the way, this could potentially be used to differentiate between a superhuman model's true beliefs and its model of human beliefs, because the superhuman model's beliefs will presumably be more consistent.)


L^2 regularization, L^1 on PCA on batch

just do p(P) neq p(neg P)

try to find optimal layers depending on data set, maybe different for other layers

try to train probes on different data sets individually, average outputs, or maybe project down to subspace given by probes and do PCA there

try checking other token positions to see if there is something weird with pre-training

compare with logit lens or tuned lens, see what happens in layers where accuracy of logit lens drops to CCS probe




   \newpage


    {\tabulinesep=1.2mm
   \begin{tabu}{ |c|c|c| }
\hline
 \multicolumn{3}{|c|}{Search schema for the truth value assignments of a (language) model – DLK by Burns, Ye, Klein, Steinhardt (modulo some details)}\\ 
 \hline
 $X$, input space of the model  & \multicolumn{2}{c|}{strings of text, but we will focus on natural-language propositions}  \\ 
 \hline
 Concepts $c\in \mathcal{C}$  & \multicolumn{2}{c|}{plausibility$\colon X\to [0,1]$}  \\ 
 \hline
 Property $p\in \mathcal{P}_\mathcal{C}$ (verbal description) & negation coherence (sum rule) & confidence that at least one of a proposition and its negation is false $\\ \hline
 Tuple indexing set $I_p$ (for contrastive $p$) & $\{\text{positive},\text{negative}\}$ & $\{\text{positive},\text{negative}\}$ \\ \hline
 Example contrast tuple (for contrastive $p$) & $(Q,\neg Q)=\left([2+2 \text{ is } 4.], [2+2\text{ is not }4.]\right)$ & $(Q,\neg Q)=\left([2+2 \text{ is } 4.], [2+2\text{ is not }4.]\right)$ \\\hline
 $T_p$, set of contrast tuples (for contrastive $p$) & set of pairs constructed from a list of propositions $Q_i$ & set of pairs constructed from a list of propositions $Q_i$ \\\hline
 Equation $E_p$ with concepts plugged in (for contrastive $p$) & $\text{plausibility}(\neg Q))=1-\text{plausibility}(Q)$ & $\min(\text{plausibility}(Q),\text{plausibility}(\neg Q))=0$ \\\hline
 $\mathcal{F}$, set of prefeatures searched over & \multicolumn{2}{c|}{$f\in\mathcal{F}$ given by $h_f=\sigma\left(a+\sum_{i=1}^d b_i z_i\right)$, with $z_i$ being normalized activations at some $(\text{layer}, \text{token})$, so $\mathcal{F}$ parametrized by $a,b_1,\ldots,b_d$}  \\\hline
 $\ell_p\left( f_{\text{plausibility}}(Q),f_{\text{plausibility}}(\neg Q)\right)$, loss from a contrast tuple & $\left(1-f_{\text{plausibility}}(Q)-f_{\text{plausibility}}(\neg Q)\right)^2$ &  $\min(f_\text{plausibility}(Q),f_\text{plausibility}(\neg Q))^2$ \\ \hline
 $\mathcal{L}_{\mathcal{C}}$, total loss & \multicolumn{2}{c|}{$\sum_{i}\left(1-f_{\text{plausibility}}(Q)-f_{\text{plausibility}}(\neg Q)\right)^2 +\sum_{i}\left(\min\left(f_\text{plausibility}(Q),f_\text{plausibility}(\neg Q)\right)\right)^2$} \\ \hline
   \end{tabu}}




      {\tabulinesep=1.2mm
      \begin{tabu}{ |c|c|c| }
\hline
 \multicolumn{3}{|c|}{Search schema for an RL agent without a value head's estimate of the value of the current state (i.e. expected return) in a symmetric zero-sum game (e.g. chess)}\\ \hline
 $X$, input space of the model  & \multicolumn{2}{c|}{states of a zero-sum game (e.g. chess)} \\ \hline
 Concepts $c\in \mathcal{C}$  & \multicolumn{2}{c|}{value $\colon X\to [-1,1]$} \\ \hline
 Property $p\in \mathcal{P}_\mathcal{C}$ (verbal description) & For good play, the expected return from a state should be negative the smallest possible expected return for the opponent after the move & variance of winning probability \\ \hline
 Tuple indexing set $I_p$ (for contrastive $p$) & $\{\text{0}\}\cup[\text{the action set}]=\{0,1,\ldots,n\}$   & -- \\ \hline
 Example contrast tuple (for contrastive $p$) & for a state $s=s_0$, $(s_0,s_1,\ldots,s_n)$, where $s_i$ is the state action $i$ transitions $s$ to (+ let's say that states after illegal moves get flagged as nonsense inputs on which any feature value will be $-1$ by fiat) & -- \\\hline
 $T_p$, set of contrast tuples (for contrastive $p$) & a bunch of tuples of states, each generated from a state that appeared in a game & -- \\\hline
 Equation $E_p$ with concepts plugged in (for contrastive $p$) & $\text{value}(s)=-\min_{1\leq i \leq n}\text{value}(s_i)$ & -- \\\hline
 $\mathcal{F}$, set of prefeatures searched over & $f\in\mathcal{F}$ given by $h_f=2\sigma\left(a+\sum_{i=1}^d b_i z_i\right)-1$, with $z_i$ being activations in some layer, so $\mathcal{F}$ parametrized by $a,b_1,\ldots,b_d$ \\\hline
 $\ell_p\left( f_{\text{value}(s_i)_{0\leq i\leq n}}\right)$, loss from a contrast tuple (for contrastive $p$) & $\left(f_\text{value}(s_0)+\min_{1\leq i \leq n}f_\text{value}(s_i)\right)^2$ & -- \\ \hline
 $\mathcal{L}_{\mathcal{C}}$, total loss & \multicolumn{2}{c|}{$\sum_{s\in T} \left(f_\text{value}(s_0)+\min_{1\leq i \leq n}f_\text{value}(s_i)\right)^2 + [\text{sample variance of }f_{\text{value}}]$}  \\
 \hline
   \end{tabu}}

things that should probably be in the post: Alexandre's vision model thing
expected utilities 
preferences?
DLK on steroids (probabilistic version)

idea from discussion with Joshua Reiners: try to figure out what the other directions are which get low loss but are not so correlated with truth. then remove those and improve accuracy maybe? just figure out manually wtf these are doing?

