
# Language modeling with a merge machine
Let's consider the following language modeling setup.
* First, there is a pre-processing step in which the sentence is analyzed into its [syntax tree](https://en.wikipedia.org/wiki/Parse_tree).[^1] 
* There's some data type $S$ such that each phrase will be assigned a token of that type, which we might call its semantic representation. Specifically, we will say each phrase is assigned a vector in $\mathbb{R}^n$, but we will remain open to considering alternative types.
* There are some tokens given to some smallest base units. We could take these atoms to be words or small phrases. (E.g. "Barack Obama" should maybe be a base unit, even though it's not a single word.)
* To obtain the representation for a phrase consisting of two subphrases (let's assume we have a syntax tree system where every non-atomic phrase consists of two subphrases), we apply some operation $m\colon S\times S\to S$, which we call the (semantic) [merge](https://en.wikipedia.org/wiki/Merge_(linguistics)) map.

The above describes what happens during inference to get representations assigned to all phrases. What's the point of these representations? There are various things we could be doing with the representation of a sentence, but let's try to fix something so we can think concretely.
* Let's say that we will only be dealing with declarative "contextless" sentences, i.e. ones such that it makes sense to talk of the truth value of a sentence given no additional context.
	* So, for example, "Your friend is cool." isn't in the class under consideration, because its truth conditions are underspecified if we aren't given further context specifying at least who this "you" is and which friend of that person we have in mind, but "Albert Einstein was a physicist." is in the class under consideration. (In practice, there will of course always be stuff left that could be better specified given more context, but I think this distinction roughly makes sense.)
* Let's say that the point of the representation of such a sentence is to be able to read off its truth value. More precisely, we will suppose there is a map $t\colon S\to \mathbb{R}$ with which we hope to read off the truth value of the sentence. If we want to be more precise, we could think of the value in this codomain $\mathbb{R}$ as capturing the log odds assigned to the sentence. And with our $S=\mathbb{R}^n$ choice, we will specifically assume that $t$ is a linear regression. In fact, because our setup will be isotropic, I guess we could just say it reads off the first coordinate (but maybe we should leave the scaling tbd?).

It remains to specify how the atom representations are to be obtained, and how the merge operation is to be obtained, and maybe how the truth readoff $t$ is to be obtained.
* If we want to consider a practical version, these things are supposed to be learned, optimizing a truth readoff loss on some data set of declarative sentences with given truth values.
* I'm also interested in thinking through ways to hand-engineer the atom representations and the merge operation $m$ to do well wrt this truth readoff criterion.

# Some variations on the above merge machine setup

There are various directions in which we could perturb the setup above, to get other interesting setups.
* We could be learning different merge maps for different usual phrase type combinations, e.g. there could be a merge map $m_{V * PP}$  that gets used when merging a verb with its complement prepositional phrase and a different merge map $m_{NP*IP}$ that gets used when merging a subject noun phrase with an inflectional phrase.
* Instead of grounding the representation learning problem in reading off truth values of sentences, here are some other things we could be doing.
	* word prediction; specifically, the representation of a sentence should help one predict e.g. the first word of the next sentence
	* making an image classifier corresponding to the sentence; i.e., turning e.g. "Someone has a green shirt." into a thing that gets as its input an image and should output whether there is a guy in that image who has a green shirt
	* something with implications; like, given the representations of the sentences A and B, one should be able to easily tell if A implies B
	* something where sentence meanings are combined into some representation of a situation described by them, and then one should be able to read off answers to questions about the situation from that representation (this is a lot like a reading comprehension test, like seen e.g. in the SAT reading component)

# An even more toy setup — ideal object vectors and predicate covectors

We could first just be asking for representation vectors for proper names (e.g. of people, places, institutions), such that many reasonable properties can be read off these vectors linearly. This is like a merge of an atomic noun phrase with an atomic inflectional phrase into $\mathbb{R}$. For instance, we might want a direction from which we can read off gender, a direction from which we can read off whether someone is an American, a direction from which we can read off whether someone is a politician. It is fine for a question/predicate to only be considered sensible for some objects — e.g. maybe we don't care about getting a sensible answer when asking whether New York is an athlete. So, each question can come with a domain of objects on which it makes sense. The question is then: supposing we can freely pick vectors from which to read off these things, how should these vectors be picked? Can we say something interesting about the structure of the vectors we get? I guess it's more natural to be thinking of ourselves as picking vectors for objects and dual vectors for questions/properties/predicates. The representation of a predicate expressed canonically with multiple words (such as is-soviet-spy) could be constructed from the representations for its words, but for now let's think of all predicates as atomic.

Is this an interesting toy setting? One issue is that it seems really quite easy to do very well. Like, I feel like you can just pick 1000 natural predicates as the axes, and then most other natural predicates can be recovered from this representation with high accuracy among some direction. And then it seems hard to say something that interesting about the structure here, if one has many ways to do decently well? Maybe we could say something interesting about which options are preferred in practice anyway? Oh but a counterargument: maybe we aren't actually happy at all with like 95% accuracy. Maybe thinking needs to be really robust to get somewhere without getting confused, and you really want such a basic component to have very high reliability so as to not have like 1% success rate whenever you put 10 thoughts together? And then maybe there is a real problem here of doing this with extremely high reliability? Like, in that case, maybe you can't just read off whatever you want from a space where 1000 random properties are the axes — maybe you really need to be careful about what to represent, quite often decide not to represent something if it would cause even a little bit of interference on other stuff. Actually, it should be fine to represent some predicate even when you don't know what its value is for some objects — but in that case, in a robust system, there should maybe be a way to mark "idk" in some answer slots?

So maybe we should be studying a version where reliability matters a lot — where we just decide not to track a predicate at all if we cannot track it with extremely high accuracy. Maybe we ought to be looking for something with high robustness like human thinking that however still has some soft properties (ie is unlike GOFAI systems) also like human thinking (for instance, we want there to be many senses each word can be used in, that do not ever have to be discretely coined — we want to have concepts open to being used in quite novel ways). Actu
## A simple case of this more toy setup
Suppose we are minimizing $L^2$ predicate recovery loss. In this case, I think that this problem should become SVD on the object-predicate matrix $M$. Let's work that out. 

Let's go with the convention that $M$ has rows labeled with objects and columns labeled with predicates, so $M_{ij}$ is the value of predicate $j$ on object $i$. In perhaps the simplest case, each question can be asked about each object, with the answer being a real number — for usual binary predicates, we could use the convention that this is $0$ or $1$, or we could use the convention that this is $1$ or $-1$ (idk which one is better). (Philosophically, here we are assuming that each question makes sense about each object. More generally, we might also be interested in the case where various entries of $M_{ij}$ are "the question doesn't make sense / who cares".) Now, let object $i$ be represented by the vector $o_i\in \mathbb{R}^n$, and let predicate $j$ be represented by the covector $b_j\in \mathbb{R}^n$. Actually, maybe we want to have it be represented by a linear regression, so we should also allow a constant? So maybe we should say that predicate $j$ is supposed to be read off as $a\cdot b_j + c_j$. So we have a bunch of equations $a_i\cdot b_j +c_j = M_{ij}$ which we wish to jointly satisfy as well as possible. Letting $A$ denote the matrix whose rows are $a_i$ and letting $B$ denote the matrix whose columns are $b_j$ and letting $C$ denote the matrix column $j$ is const $c_j$, we can write this optimization problem as wanting $AB+C=M$. Can we characterize the optimal solution?
* Without $C$, the best choice just has $AB$ being the best rank $n$ approximation of $M$, which is given by the first $n$ summands in the SVD of $M$. There is freedom in how to split that up into an $A$ part and a $B$ part.
* I wonder what the best choice is if we put an $L^2$ penalty on the thing (let's say: that is lexicographically weaker than the MSEloss).  

if some entries are left unspecified, then it's NP hard! the weighted version is also more generally NP hard. see https://openreview.net/forum?id=rvhu4V7yrX

## some questions i have about the more toy setup

here are some questions about this setup:
* is there some interesting sense in which linear decomposability of object rep vecs or predicate rep dual vecs is true?
* is there some other interesting sense (not obviously forced by the setup) in which some linear representation hypothesis is true? do some interesting subspaces show up?
* is there a way to look at the object rep vec data set and figure out what the predicates are (like, what their values are on objects)? to look at the predicate rep vec data set and figure out what the objects are (like, what predicate values they take)? at least in a toy case where the predicates are independent? uncorrelated?
* can we say something interesting about what SAEs are doing on these data sets in some toy cases? does SAEing the rep vecs do sth close to SAEing the underlying true feature vectors? do SAE features end up looking sorta like SAE features in LLMs? (if yes, this would arguably be weak evidence against SAE features being a fundamental computational basis in LLMs. or at least it could be helpful for making sense of what SAE features are / where they come from)
* will days of the week be kinda on a circle?
* can we use this setting to come up with some reasonable interpolation between SAE-ing and SVD-ing? like, maybe we can pick some family of toy constructions of the object-predicate matrix where there is a hyperparam such that: at one extreme, SAEs are doing something reasonable, and at the other extreme, SVD is doing sth reasonable, and then we can think what we should do in the intermediate case? or maybe we construct a case where intuitively there is a mix of sparse and dense stuff in the same activation data set and come up with a method that can see both at once

(btw, the more toy setup is somewhat like Anthropic's toy models of superposition but imo with some mistakes fixed)

## What about properties which have other structure?

For binary properties such as whether something is alive or inanimate, it makes sense to ask that there be a linear classifier. For numerical properties such as time of creation or mass, we could also ask for linear classifiers, though note that in the binary case we could take the classifier to track a probability distribution on two options, but it doesn't make much sense to do that for a numerical thing (a probability distribution of a real-valued variable is just a much higher-dimensional object than a single number), so there's already this difference. What about properties with other structure? For instance, there's:
* categorical data. e.g. the nationality of a human
	* one could just have a binary classifier for each class, but maybe one wants to track eg that there are more and less similar classes? or maybe that gets handled automatically in practice — like maybe the predicate vectors automatically end up similar?
* a question with an answer in $S^1$, such as the time of day
	* you could just be fitting some parametrized map from object representation space into $S^1$ or $\mathbb{R}^2$
* a question with an answer in $\mathbb{R}^2$, such as location
* data where there is some other metric space structure on the possible values
* there are also relations between the objects, such as friendship between people. one option would be to just store on each person who their friends are — like, this could somehow be written in an object representation. maybe this looks like being able to recover pointers toward their friend representations or something? this seems like it could be too much data though? another option would be to store this across object representations — eg there could be a subspace such that the distances between object representation projections to this subspace track friendships?
	* this makes me remember in general that maybe we don't want some ML noisy crap, and maybe I've been too lenient with this sort of thing in my formulations/analysis so far. maybe we really want to robustly know some facts, robustly represent some stuff, like very reliably. the note i added about this above was actually added once i realized this here

# What this is trying to get at
I'm trying to make progress on at least the following two things with understanding some stuff in this toy setting:
* LLM interp: I'd hope to get better ideas for understanding LLMs.
* meaning in humans: I'd hope to get better ideas what structure has been set up in a human head when they have grasped a sentence.

# Misc
We could also call these "montague machines" — see https://plato.stanford.edu/entries/montague-semantics/ .

# mess

think thru what i actually do when i answer questions about barack obama! look at some questions
* does barack obama have two lungs?
	* probably yes because almost all humans have two lungs. how did i know to pull out this fact? did i even ever think about this fact before? how did i know this fact?
	* i guess i'm tracking somehow that facts about humans are facts about obama. i'm not literally thinking "if X is true of humans generally, then it is probably true of obama". it's more that when i think of obama, i think of him as a human, and that makes all the human facts come to mind?
* characterize obama's policy positions!
	* now i wouldn't really feel like i can give a good answer without looking stuff up, but let's say i have to try.
	* i would think of obama as a democrat now, and speak of what sorts of things democrats like.
	* oh i guess obamacare comes to mind, but i'm not sure i even know what it is, except that it's some health thing, maybe for old people and/or poor people? maybe health insurance in particular?
	* my next thought is to go looking for big events that happened during his presidency. i think he was the president from like 2009 to 2017? yea i checked and that's right. so what events happened in that period?
		* i guess the financial crisis was still happening when his presidency started. i wonder if he participated in any bailout of a big bank or whatever? maybe that had already ended before him?
		* there was the invasion of crimea. i guess he participated in instituting sanctions on russia?
		* probably some gay marriage legalization stuff was happening?
		* some climate change thing? signing some international agreement to try to do something about climate change?
		* benghazi?? (does anyone know what benghazi was)
		* bin laden killed
		* unfortunately idk much about obama's involvement in these. but i guess i can guess some generic stuff
	* now i ask: how else might i find thoughts about obama's policy positions?
		* i could think through different political things. like, do i know anything about what obama did in tax policy? in education policy? on like inflation and federal reserve stuff? eg this reminds me that maybe he did quantitative easing, which is like printing money or something? i looked this up and yea it's sth like the central bank saying "we have money now" and buying government bonds with it, which did sth like giving the government money to do stuff with (tho they have to pay it back in the future right?) and pushing up bond prices relative to other stuff so people invest more?? i guess the money created out of thin air will also be destroyed by the central bank when paid back by the government?

[^1]: There are somewhat different ways to do this. I'm not going to worry about the details for now. I'm familiar with the system taught in [this course](https://ocw.mit.edu/courses/24-900-introduction-to-linguistics-spring-2022/pages/lecture-notes/).
