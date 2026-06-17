
## why are probabilistic constructions useful?

* we get every local part to look the same for free: example constructions from combinatorics
* something separate about load-balancing?
* we can use resources more efficiently by doing local things? examples: randomista patent thing, panopticon, sketching in linear algebra, thing with tagging random fish and counting how many tagged in biology?
* 

## where to publish?

https://academic.oup.com/philmat/pages/General_Instructions

would need examine whether there are similar articles





graph G, edge set E, prove that there exists a cut of size |E|/2

soln: color at random, EV = |E|/2, so done

(this gives way to prove LLN for this specific case? can we get a general proof of LLN out of this too???)

![[Pasted image 20230616200133.png]]

![[Pasted image 20230616202723.png]]
can do a bit better re the constant, but lower bounds all $\left(\sqrt 2 + o(1)\right)^k$ 
main idea of these: can create a global structure such that all local structures are sort of the same and can be understood

![[Pasted image 20230616202154.png]]




unify stuff from different fields? maybe make this specifically about cases where thinking probabilistically gives one more information than otherwise?
e.g. property testing literature (such as graph triangle)
but also https://dash.harvard.edu/bitstream/handle/1/3693705/Kremer_PatentBuyouts.pdf
also maybe something like that for the vNM theorem to harsanyi connection? like get something interesting out about allowed orderings of deterministic outcomes even? it does seem to say something cool here; I wonder if there is a way to get the same conclusion without lotteries though? this seems worth thinking about in the future

* 
* 
* just K_{s,t} construction standard thingie
* graph triangle checking using triangle removal lemma
* Kremer
* panopticon

https://en.wikipedia.org/wiki/Panopticon

The **panopticon** is a design of institutional building with an inbuilt system of control, originated by the English [philosopher](https://en.wikipedia.org/wiki/Philosopher "Philosopher") and social theorist [Jeremy Bentham](https://en.wikipedia.org/wiki/Jeremy_Bentham "Jeremy Bentham") in the 18th century. The concept is to allow all prisoners of an institution to be observed by a single [security guard](https://en.wikipedia.org/wiki/Security_guard "Security guard"), without the inmates knowing whether they are being watched.

Although it is physically impossible for the single guard to observe all the inmates' cells at once, the fact that the inmates cannot know when they are being watched motivates them to act as though they are all being watched at all times. They are effectively compelled to self-regulation. The [architecture](https://en.wikipedia.org/wiki/Architecture "Architecture") consists of a [rotunda](https://en.wikipedia.org/wiki/Rotunda_(architecture) "Rotunda (architecture)") with an [inspection](https://en.wikipedia.org/wiki/Inspection "Inspection") house at its centre. From the centre, the manager or staff are able to watch the inmates. Bentham conceived the basic plan as being equally applicable to [hospitals](https://en.wikipedia.org/wiki/Hospitals "Hospitals"), [schools](https://en.wikipedia.org/wiki/Schools "Schools"), [sanatoriums](https://en.wikipedia.org/wiki/Sanitorium "Sanitorium"), and [asylums](https://en.wikipedia.org/wiki/Psychiatric_hospital "Psychiatric hospital"). He devoted most of his efforts to developing a design for a panopticon prison, so the term now usually refers to that.

unifying theme of last two examples: want to leak information/incentives between different probabilistic worlds? in the last case, the probabilistic setup lets you get information about a counterfactual that does not actually happen. in the former case, it lets you impose ghost penalties

![[Pasted image 20230616201414.png]]