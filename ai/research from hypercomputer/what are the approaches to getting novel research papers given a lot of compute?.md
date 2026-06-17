
# approaches to getting research papers given a hypercomputer?

first, some approaches where i could give some concrete programs + acquirable data sets that one might maybe a priori think would just work, though i don't think we actually have anything here that works:
* something with powerful prediction
	* in particular, solomonoff on question-answer pairs. i want to understand if the in-distribution case works at least
		* eg human prediction of counterfactuals
	* you can try to combine with task decomposition to get longer-term scientific progress out
	* you can do prediction then condition on success at some stuff. eg maybe conditioning on small stuff is better so you're less likely to build really new wrong stuff? could try to make this precise?
* something with verification
	* you could try to just use solomonoff on human labels to get a verifier
	* you can do some sort of debate
* something with simulation
	* should think through a setup where we know the laws of physics and try to put a human inside a field configuration and time evolve it forward


now, some approaches for which i can't write down anything, and that are imo very cursed (this list probably has overlaps):
* formalize non-math science. like, write down a math problem such that a solution gives you an alzheimer cure
* something with turning counterfactual questions into mathematical ones?
* do something where you get "good concepts" from low-level data
* do something like solomonoff prediction of a bunch of data + figure out how to look at a turing machine printing this data well and identify the guys it "takes to exist" (if such a thing makes sense) + run these guys forward solving scientific questions
	* do the same thing except not with solomonoff prediction but with some other kind of "world modeling" apparatus applied straight to data streams (eg MIRI used to pursue a multi-level models research direction — maybe see https://intelligence.org/files/TechnicalAgenda.pdf and` https://intelligence.org/2015/07/27/miris-approach/)


# mess

**

1. Specify a program/system that gives a 1000x clock speed mind upload device (that doesn't also do something bad) (or a particular mind upload, or a paper explaining how to make mind uploads, or analogous things for curing cancer or for other hard scientifico-technologico-philosophical problems) given unbounded compute, access to arbitrarily much data of the kinds that "already exist" or are reasonably easy per datum to gather, and ability to use a vast quantity of current humans to do fairly short monitoring tasks (one could see this as falling under "ability to gather data" also). Like, existing papers are completely fine to use as data, doing some easy reformatting/labeling of existing data is fine, having humans spend a few hours generating or evaluating stuff is fine, etc.. But having humanity think 1000 years and make mind uploads and then training a model which memorizes that and "can now make mind uploads" is not fine. (Questions 1–5 are all specific things one could encounter when thinking about this question.) Let's make the further simplification that you're granted a completely secure/crisp server, ie one that only interacts with the outside world by receiving whatever inputs/data/code you give it, and acting on the external world only via the output channels you intend it to have (tho note that if you're monitoring it, then you might need to worry about whatever system you have monitoring it potentially getting used by it as an output channel). The point here is to specify a plan that clearly works (as opposed to a thing you might merely assign >50% chance of working after thinking about it for a few hours but still feel really confused about) — you should make a compelling case that your thing works.
    

**