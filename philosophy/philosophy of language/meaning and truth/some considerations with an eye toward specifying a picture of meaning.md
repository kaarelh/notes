
* i want to give a theory of a kind of "meaning" of eg words and sentences. i'm speaking here of sth like: the structures that have been created in your head when you have understood a sentence or learned a word
	* i'm not speaking of some neurological thing here. i'm speaking of sth more high-level/abstract, maybe like a data structure in computer science. i want to understand the queries they support and how they relate to each other and other mental elements. i want to know stuff like:
		* what sorts of operations does your sentence representation support? how does it support them? for instance, how does a sentence representation support inferences?
		* how does a sentence representation get built from structures one has for words? (presumably it gets built this way. consider that a human understands a sentence roughly iff they understand its constituent words)
		* to what extent is a sentence representation the same sort of thing as a word representation?
		* which substrings in a sentence can have this kind of structure attached? basically only words and the full sentence? also strings of words 2026-canonical linguistics syntax stuff considers to be phrases of the sentence? also arbitrary initial segments (made of words) of a sentence? also morphemes inside words?
		* what is the nature of one's "representation/model of a scene/situation", of a "mental picture". how does that thing get built as one listens to a paragraph describing something? to what extent is it the same sort of thing that is attached to an individual sentence? ... to a word?
		* what is it that you have gained when you have become a capable user of a word?
* i think there are other things one can mean by "meaning" which call for pictures of that-sort-of-meaning, different than the picture i'm giving here. i'm not saying any of those are wrong or bad. for example, montague semantics is cool (though i would object to considering it THE theory of meaning)
	* in my sense of "meaning", the "meaning" of a word is not some sort of thing out there (so it is unlike e.g. "meaning" in the sense of model theory in logic), and the "meaning" of a sentence is not an abstract proposition or a truth value. instead, in the system i'm trying to provide, these are certain (abstract) elements of a mental system. one could say that this means my theory isn't well-called a "theory of meaning" after all. one could further say that it's closer to being a theory of some sort of mental syntax. feel free to call it that 


## some phenomena of interest
* when one has a picture of a situation, one can easily draw some inferences. if you know that bob's mother is alice and you know bob got someone a gift for mother's day, you're easily pretty sure bob got that gift for alice. 
	* there are other inferences one cannot easily draw. for instance, typically, a mathematical theorem is highly non-obvious if you just have the axioms, even though they are implied by the axioms. so we can ask: which inferences can be easily drawn? what does that say about one's representation of a scene?
		* it might be good to study this in mathematical thinking. the inferences one can easily make depend on how one views a mathematical situation
		* if one has understood a basic course in linear algebra, in lots of situations in which linear algebra is helpful, various things become obvious that weren't obvious before. obviously, gaining new concepts can change how one views a situation (it can also open up new inferences for slightly different reasons though). it'd be interesting to understand stuff about what happens when one improves one's picture of a scene
		* consider how alphaproof has a fast inference engine and then a thing which suggests new auxiliary 
* one can play twenty questions with things/words. human object representations support some kind of property/constraint-based search
	* this is important for making analogies. for instance, one can be "where have i seen a quick inference thing that doesn't get to some target sometimes but can get further when more elements are introduced", and think of alphaproof. in practice one doesn't need to explicitly think this. one might need to fairly explicitly think sth like "here we have a quick inference thing that doesn't get to some target sometimes but can get further when more elements are introduced", but then one doesn't further need to explicitly ask "where else have i seen this?" — bringing other stuff with the same property up is done automatically. though of course one also can ask this explicitly and that can be helpful too
		* analogies bring new good ideas into one's view of a situation (because one already knows stuff about the other case / other things are obvious by default about the other case, and the same stuff can often be adapted to the current situation. a cheap analogy can often be made into a rich one, fruitfully)
* when you gain the word "dog", you have in most cases gained some sort of quick image/voice classifier. but what is a dog isn't defined by the output of this classifier. it's possible to think you saw a dog, but to be wrong, and you recognize this! i think it's more like: there is now a kind of question you can ask: "is this a dog?". you have some sense of how to make progress on this question. some things you can do to make progress on this: point at the maybe-dog and ask your father "is this a dog?"; go closer and see if it looks like a dog from closer; see if it has an owner (assuming you know that dogs typically have owners). i think: ultimately, we are trying to fit "dog" into various propositions and to more generally do various things supported by the "dog" notion, and these things working out serve as criteria on the notion. it's fundamentally an open/moving thing, with in principle arbitrarily many more details to be added when facing new contexts and being called upon to support new endeavors. the meaning can change, too. it's often unclear if the meaning changed or was made more precise, perhaps fundamentally (consider eg the term "woman").
	* formal mathematical notions are an exception to much of this. but there is plenty of the stuff i'm talking about in mathematical thinking: consider eg how easy it can be to know what a "homomorphism" and an "isomorphism" are in a new context
* we find it very easy to modify our notions. some examples to consider:
	* "the three-legged dog", "the robot dog"
		* when hearing "the robot dog", how come one quickly has a guess which properties of a dog it has and which properties it doesn't have?
	* "that cat was as loyal as a dog"
 * consider explaining something to someone. what is it that you are loading into their head? what skills do they now have if they have understood you?
	 * let's consider an example. i will imagine explaining ramsey's theorem to someone:
		 * T: do you know what a graph is?
		 * S: yea!
		 * T: ok, so by a "complete graph" $K_n$, i mean the graph on $n$ vertices with all possible edges. our edges will be undirected, so with n vertices, that's $\binom{n}{2}$ edges. we will be looking at edge-colorings of this guy, with two colors, call them red and blue. are you following so far?
		 * S: ok yes we have a complete graph and we are colorings all its edges red/blue, following so far
		 * T: ok so here's a puzzle for you: consider $K_6$. is there a way to 2-color its edges so that there is no red triangle and also no blue triangle?
		 * S: that's easy enough! i'll just color it with green and yellow!
		 * T: very funny
		 * S: ok, let me get pen and paper and try some stuff. ok i tried coloring edges arbitrarily at first and then trying to not create monochromatic triangles; i did this a few times, and i was forced to draw a triangle at the end. i wonder if i was just making initial choices poorly or if it’s really impossible…

# mess

