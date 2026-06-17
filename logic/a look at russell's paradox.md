# a look at russell's paradox

1. Let’s think of all mathematical objects as collections.[^1] This is a standard choice in mathematics when one wants to be precise/concrete — there are standard ways to think of numbers, groups, graphs, functions, etc as sets. It seems quite fair to think of this as a convention (as opposed to being a fundamental claim about something).[^2]
2. Let’s say that collections are not allowed to be self-containing. This also feels somewhat like a convention — it seems like while we could perhaps allow self-containing collections, we can easily handle all our ordinary mathematical affairs with only collections consisting of elements different from the collection itself. But one could also justify it by saying that having a set as an element of itself would be an obstacle to “understanding it fully” as a collection of some “more primitive” things. Like, if you tell me that 1 is the set containing the empty set, I’m feeling like you’ve told me what 1 is quite concretely, but if you told me that 1 is the set containing 1, then I’d be less satisfied — I’d feel less like saying I can now concretely grasp what 1 is.
3. Now, imagine all mathematical objects in front of you.[^3] It seems like the collection of all mathematical objects should itself be a mathematical object? Intuitively, we could just choose what we mean by “mathematical object” such that this is true?

Unfortunately, these conventions/“conventions” fairly straightforwardly lead to a contradiction. This is because given that the collection of all mathematical objects is itself a mathematical object, we must conclude that it is an element of itself. But we assumed there are no such mathematical objects. Let's say this again to make sure we can clearly see what went wrong. Given our conventions/assumptions, the universe of all mathematical objects that we were imagining must have itself as an element.[^4] But now there is a mathematical object that has itself as an element!

How do we fix this mess? We need to change our assumptions/conventions somehow — they cannot all be maintained together without a contradiction being provable. While the issue discussed in the previous paragraph depended on assumption/convention 2, it turns out that even if we drop 2, we are still in trouble. (Dropping 2 is perhaps nice also because it arguably feels less like a convention than 1 and 3 — like, it seems more fair to say that 1 and 3 are true simply by virtue of what we mean by mathematical objects and collections.)

How are we still in trouble? We are still in trouble if we take on a somewhat stronger commitment in the spirit of 3: a commitment that all collections are mathematical objects. Specifically, we imagine being able to face all of the mathematical objects as in 3, and to be able to specify any property of mathematical objects and to then make a collection of those mathematical objects which have that property (it might help to imagine here that all the mathematical objects are these definite things, i.e. that all their properties have in some sense been determined by the time we arrive and start making collections), with that collection again being a mathematical object. This seems intuitively like saying more precisely what we mean by "mathematical object" again: if we face all these definite mathematical objects and have some intelligible property in mind, surely there is a collection of mathematical objects picked out by the property, and it seems fine to go with a notion of "mathematical object" that considers that collection to be a mathematical object? However, if we accept this, we run into the following major issue: if we face the supposed totality of mathematical objects and then collect those which do not have themselves as an element into a collection, this collection is a mathematical object $C$ which cannot be in the original supposed totality, because its elements differ from the elements of any thing in the totality: namely, $C$ has $x$ as an element if and only if $x$ itself doesn't have $x$ as an element; so, $C$ cannot be $x$; but this is true for any $x$; so, $C$ must not be in the supposed totality of mathematical objects we started from.[^5]

so we must say: there is no totality of mathematical objects on which this "construction" can be executed such that it makes another mathematical object

i think the most philosophically satisfying resolution is to say: you can make arbitrary collections of mathematical objects, and those collections are always still themselves mathematical objects. but there is no totality of mathematical objects — any collection is missing some mathematical objects — in fact, ones that are easy to construct from the collection! in fact, given this, it makes sense that there would be many properties such that you can't make a collection which contain all mathematical objects satisfying that property, again because there are just too many mathematical objects!
(that said, i still feel somewhat weird about this...)





# fuck it, i'll construct 

# mess

* take all collections of mathematical objects. they are all in the totality; let's restrict our attention to those elements of the totality. among them, pick out those which do not have themselves as elements. this gives a new contradictory collection
* One could try to say that items 1 and 3 on the list are both conventions about collections — they are both things that we could say are true by virtue of what we mean by a collection. Whereas maybe item 2 is a bit more toward being a claim about collections — like, maybe we should 

it were, by definition, it would need to contain itself if and only if it doesn't contain itself, an impossibility. So if we consider ourselves to have made a legitimate mathematical object, 

Here is a slightly different path to the same trouble: suppose that all collections of mathematical objects are themselves mathematical objects. Since a collection is determined by its elements, we could imagine specifying a collection as follows: for each mathematical object, we specify whether to include it as an element or not — imagine this as specifying a bit for each mathematical object. Now, we can also associate such a bit"string" to each mathematical object (because they are all collections). We now make a weird subcollection that differs from all of the 






all mathematical objects satisfying that property together into a  



* collection of all collections not containing themselves


one way out is to say: You can always carry out this collecting-into-a-mathematical-object operation when faced with any particular collection of mathematical objects, but what you get will be something which wasn’t already in the original collection. So one was just wrong in thinking one already had the totality of mathematical objects in front of one. If you want to keep non-self-containment, then you should stop imagining that you can see all the mathematical objects (including the collection of all of them) all at once! (this needs improvement. it’s more about having the collection of all of them be a mathematical object that can be seen side by side with all other mathematical objects)

But could we give up non-self-containment instead? to be continued

[^1]: I'll speak of "collections" instead of "sets" to make it clear that we will not necessarily be assuming something like the ZFC conception of a set from the get-go.
[^2]: Note that at this point, we've taken the view that all mathematical objects are collections, but we haven't yet taken a position on whether all collections are mathematical objects.
[^3]: In what sense am I asking you to imagine all mathematical objects in front of you? I'm certainly not asking you to have each one of them implemented in your mind. But when you imagine the world economy, you don't have it implemented in your mind either. I'm asking you to contemplate/consider the totality of all mathematical objects, in the same sense that I might ask you to imagine the world economy. If you want to be picturing something, you could picture a universe made of mathematical-object-galaxies — maybe you can see an icosahedron in there, and the number $1$, and the set of all rational numbers, and the Lebesgue measure, and so on (it should be extremely infinite).
[^4]: In the picture suggested earlier, you could imagine one of the galaxies in the universe being a tiny version of the universe, except that you should think of it as really being the same thing as the universe, not a distinct copy.
[^5]: This is analogous to Cantor's proof that there are more reals than naturals. Think in terms of each mathematical object having an associated bit"string" specifying which mathematical objects it contains — we're constructing a mathematical object whose bit"string" differs from that of each mathematical object in a given collection at the position marked by that object. Also straightforwardly related: a power set always being larger than a set.
