
hypothesis:
* it is easy to verify that proposed gadget X indeed does some desired thing F
	* this is where the P vs NP intuition is plausibly sound
* but it is hard to verify that it only does F, and not also anything else that is bad
	* indeed, if F is some big thing, then X will be doing plenty of big things by virtue of doing F! so there's no hope to verify that it doesn't do anything else besides F — eg: if it cures cancer, then we will have even older presidents, which obviously profoundly affects society
	* so, we would want to verify that X doesn't do anything bad.
	* maybe we'd want to verify that X doesn't do anything big except for the stuff it does by virtue of doing F?
		* even if we could make sense of this somehow, it might be really restrictive? eg you can't come up with ozempic for obesity because it also directly helps with heart disease or whatever
	* this sounds a lot more like "there is no bad thing Y such that Y would happen" which has a coNP flavor. there probably aren't short verification strings for coNP things!

similar:
* it might be easyish to verify that a proposed plan does X, but really cursed to verify that it doesn't do anything else that is bad
	* eg maybe a step in the plan is "put the screwdriver in the socket", and it looks like it really contributes to doing sth (if you don't realize it kills you)! how the fuck are we generally going to notice such things and reject such plans??
	* you can say: maybe we have a setup where another guy will be looking at the plan, and spotting such things! i think there is a general issue with this

similar:
* can maybe verify some code does something, but it's cursed to verify it doesn't have a virus (i'm guessing)

i guess this isn't such a nice distinction, because it would imply that there are F such that doing F is actually hard to verify — for example, F = making the world better


  