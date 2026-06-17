
why does language have words etc, instead of being really continuous — like, maybe we could imagine a language in which sentences are not made of words, but more like blobs? i think one major thing here is that you can make some good parts and then do lots with them — like, this is just a good way to do lots. in particular, you can learn words and then understand sentences; if each sentence were a blob, maybe you'd have to learn all the blobs individually! but now that things are made of parts, you only have to gain the parts to have the things

hmm somewhat unrelatedly from this example we can see: you can get structure by making assembling messy things! like, words maybe aren't that clean, but you make sentences out of them, and now the sentences have some structure we can speak about (sentences have a lot more structure than that in actuality, but it is also interesting that they are made of words)?

so, you can have messy things and then start building from them and already get things with some sort of structure

still, i'd want to understand better why it's so good to make things out of things.
* one natural way to ask this question is to start from a purpose and ask: why was it easier to make a partful thing that serves this purpose than it would have been to make a partless thing? 
* maybe it's nice to start from the other direction though: given a bunch of potential parts, one can make a bunch of things using those parts by making various constellations of them. and now of all the fulfilled purposes, many are fulfilled by more partful things!
	* note that trying $n$ combinations of technological parts is probably much better according to success probability on any reasonable criterion than trying $n$ combinations of random gunk (like, of elementary particles or whatever)
	* to some extent, the parts have been selected to work well in combinations. further, when combining, we only ever add some part along some reasonable way to add it. we often do our combining inside a domain — ie, with a set of parts that have been designed to be joinable, with particular rules for what sorts of joinings make sense (eg imagine electric circuit elements, or legos for a TOY example)
	* in math, you could ask: why was this problem solved by combining various existing ideas? and then one could begin one's answer: well, you get a lot of solved problems easily by combining ideas. and then once you've done that, most of the problems that have been solved were solved by combining ideas
# examples
in general, things have parts. eg:
* technologies are made of technologies
* in language, phrases are made of phrases
* algo problems are often solved by combining a couple algorithmic ideas/tricks. idk if this is a fair example — the parts are often not really combined straightforwardly, such that they can easily be seen from the resulting code
* ditto about proofs
* a higher organism has organs, tissues, cells, organelles, signaling pathways

# a toy setting inspired by the quote from arthur's book below

it'd be nice to have various toy settings worked out where part-combining shows up. wb arthur inspires the following idea: we have a (maybe only expensively revealed) graph and we get tasks of the form "walk from u to v", and we can quickly (in runtime or graph query number) solve these by combining a known walk from u to w with a known walk from w to v, if such walks have already been found
* i asked chatgpt to give graph algos using this idea but i think it didn't really give any that get the point that well: https://chatgpt.com/share/68ffcb8d-6b04-800f-8eee-06843895ff6b
* maybe you want to set up a graph with some special (degree) structure for this to become really good
# relevant quotes

“The process here resembles the way a route up an unscaled mountain might be planned. To reach the summit is to solve the problem. And to envision a base principle is to posit a promising overall route or major parts of a route, with a given starting point. On the mountain are patches of obstacles: icefalls, awkward traverses, headwalls, stretches subject to avalanches and falling rock. Each new principle or overall plan of climb meets its own difficult stretches that must be got past. Here recursiveness comes into play, because each obstacle stretch becomes its own subproblem and requires its own solution (or subprinciple or subtechnology, in our case). An overall solution is not achieved until some starting point at the base is connected in a reachable way with the summit. Of course, certain stretches of the mountain may have been climbed before—in our context certain subtechnologies may be available and the solution will be biased toward using these. So the process may be more like stitching together known parts than pioneering a complete route from scratch. The process is in part recursive and the whole becomes a concatenation of parts, a combination of stretches.”

Excerpt From
The Nature of Technology: What It Is and How It Evolves
W. Brian Arthur

