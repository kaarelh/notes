24/11


simon:

btw values/goals are optimization targets of optimization/consequentialist/goal-directed processes. Maybe you already understand this and meant something else, but in case you don't posts you could read are:
from EY: hidden complexity of wishes, optimization, measuring optimization power
from Jeremy gillen's report early this year the initial sections
(probably there's more like Alex Flint stuff or sth but idk what's good.)

also most humans aren't very coherent/consequentialist. and i think they might be guided to a significant extent by myopic shards. but the smarter (sub)agents are the rather they do more efficient trade with each other to not leave resources unusued and thereby get closer to maximizing some joint utility function.
though one needs to distinguish between the shards that actually steer humans from the values humans reflectively endorse (which is IMO what we rather need to optimize). for the latter it's harder to specify in an AI ontology what they are, especially because they are also not well defined and we have some implicit hard-to-articulate metapreferences of how we would want to rebind the utility to new cases or how to straighten out previous inconsistencies. (whereas for just getting a rough model of what shards drive the behavior of normal humans one might be able to do something like CIRL -- though the real problem of course is how to make the AI care about some values, not how to infer them


kaarel:

meta: this might have been accidental but it's imo sorta bad (for having a good conversation) to say "if you don't understand x, then you could read abc" here instead of saying eg "see abc for arguments for x" (or "for a presentation of x" if x is more like a framing and less like a claim). one big reason is that the former silently assumes the claim x which the conversational context is also taking to not be established, and i think it's sorta bad to make statements which silently assume a claim under contention. another example with the same imo conversational mistake is "no, abortion should obviously be legal; to say otherwise would be an insult to all women" — in a good discussion, it's perfectly fine to make claims which the other person thinks are false, but i think it's kinda bad to silently assume some such claim (i guess one reason why is that it's very important to commonly acknowledge which claims have been commonly accepted vs are still debated, and just stating something downstream of a claim which has not been commonly accepted really muddies the waters on this)

"if you don't understand x" is imo bad in addition to that in that it imo sorta further silently assumes that the other person is kinda dumb about the topic at hand which is also not a claim i accept

simon: 
Yeah sry was hadly phrased. I meant if you're not familiar with the perspective 

kaarel:
ok no worries, sorry i was harsh

simon:
No was fine👍

kaarel:
more object-level: i agree with some stuff and disagree with other stuff here, but maybe this is better discussed in a call. my best guess is that if i were to read the sources you suggest atm, after reading i wouldn't think i learned significantly from them (i've probably also read all these in the past actually)

imo tsvibt's writing on values is much more insightful

i joked a few months ago that tsvibt is the only alignment researcher (which is imo not too far from true if we only consider public output)

ok actually i will say some more object-level stuff:
* i think it's fine to say "maybe we should think about an agent's values as its optimization targets — let's try to work that out in more detail" as a starting point, but i think it's also fine to say some other things as a starting point, including "values are like constraints derived from reason" and "one cultivates virtues/values in oneself", and in any case that it is then worthwhile to go much much further from these starting points. i expect that we will disagree on these other things being fine starting points, but agree on it being good to go much further, though we'll probably disagree on what stuff looks like further or which directions it makes sense to go in, and i suspect i'll maybe think that in some sense one needs to even go much further than you think but not sure

in particular, i like that "values are like constraints derived from reason" reminds us that values need to be unfolded via reasoning (actually i assign significant probability that a process of working out one's values further will basically go on forever in any natural mind and maybe even in any possible mind but this is unclear), and i also sorta like that it reminds us to consider distinguishing between things you are not allowed to do vs things you disprefer (a distinction like this is certainly present in reasoning — there's a bunch of stuff you're allowed (by like the rules of good reasoning) to try but then it further matters which one you do but in a distinct way, and it seems worth trying to extend an analogy from this to action), ie being forced to do one of a set of options vs electing not to do all but one option. there's some tension between maintaining this distinction and some kind of optimality but it imo seems plausible that 'the world' always keeps becoming 'bigger' fast enough (in large part because it includes you) that optimality won't ever be approached (i haven't thought about this bit super carefully tho)

and i like that "one cultivates virtues/values in oneself" reminds one that a lot of self-referential stuff is going on. eg it is imo plausibly very natural to care about understanding stuff better in exactly the same sense that you care about eliminating suffering (ie without the former merely being an instrumental goal for achieving the latter terminal goal)

actually maybe more than any of these, i like the starting point "each thing-to-a-mind is already playing a purposive role in the context of the mind — eg a mathematical theorem comes with a call to be used in certain ways, as does a hammer; and a mind's values are created by these purposive roles (at least by default, but maybe always)". one could then go on to try to say something about the dynamics of these purposive roles attached to all things/concepts

simon:

"constraints derived from reason" i would put into the rationality not the values bin. e.g. even in a world where everyone had selfish values but everyone is very rational, people could risk their lives to save other people, even though they didn't care about the other people, but because it's in their selfish interest that as a general policy people risk their lives for others (if in terms of overall expected lives saved it makes sense) so that in other counterfactuals the other people would risk their lives for oneself. though not sure if i understand correctly what you mean.

"one cultivates virtues/values in oneself" is sorta vague. consequentialism is a mathematical reduction.

yeah there could be more advanced understanding of values but IMO one would probably still see consequentialism as simplified case of it. (E.g. i think Scott Garrabrant is trying to "find agents in world models" by seeing when "time flows backwards in some dimensions", and I didn't look into it but just heard about it and I don't really know what he's doing, but it seems like a thing that's compatible with consequentialism.

but yeah i guess just having consequentialism as in search-for-some-target-statespace is not yet fully satisfactory because there can be implicitly defined preferences where extrapolating the current utility guess according to the metapreferences is computationally expensive and so in a sense the system isn't optimizing yet for the more narrow set of values it is bound to end up in or sth. idk maybe also other problems. in the end one would like to have a more full agent model.
and yeah also reflective endorsement is of course an important distinction to make, as already mentioned.

ok yeah i ought to have read your follow-up messages before replying to your first one, but it was fine enough i guess.

kaarel:

* i want to understand how values are implemented in a mind (on some hypothetical level where it would be natural to talk about values, if that's a thing at all; i don't care very much about how they are implemented neuronally or sth except insofar as that would help me understand the other hypothetical level) (when i speak of a mind, i basically also mean to include eg humanity-as-a-single-thinker)
* the thing i said about all concepts coming with purposes attached seems like one promising starting point to explore further (but there are also others). going down this direction, i want to be able to say much more about:
	* how does the purpose of a thing/concept get determined/modified (ie what are the rules/laws/patterns governing the determination of the purpose of a new element / updating the purpose of an existing element)?
	* more generally, i want to be able to say a bunch of stuff about how this ecology of concepts develops. it seems plausible to me that by default there's no nice way to separate out only the purposive aspects of a concept from its other aspects
	* what does it take for such a system to end up understanding a lot?
	* what does it take for such a system to do big things?
	* should we expect the ecology to ever become something which can be meaningfully considered a pursuer of a particular reflectively endorsed goal?
	* could that happen sorta by ordinary purpose-dynamics (and how would it happen)? could that happen by a top-down intervention (and how would it happen)? (i think yudkowsky is sorta (semi-intentionally) attempting such an intervention on himself and others)
* some things that make me dissatisfied with a bare-bones consequentialist picture:
	* bayesian-expected-utility-maximization/coherence are imo phenomena characteristic to a mind facing a world much smaller than itself, characteristic to setups where all possible worlds can be completely grasped together by the mind. but really, the world is a big thing compared to a mind in the world and the world keeps growing in complexity with the most advanced mind in it, plausibly without the mind ever catching up to the world (i should really say the weltgeist catching up with itself) — one reason this seems plausible to me is some naive induction considering the history of humanity vs the history of humanity's self-understanding. certainly the standard arguments for coherence assume a small world; it's a nontrivial question whether this is a non-central or central assumption, and my guess is that it is central. i buy that becoming 'coherent about any particular thing' is a thing, but the hypothesis is that there are always more things to become coherent about; this is related to math probably being an unboundendly/infinitely wild thing that will never feel resolved/understood/stale, and ethics is imo plausibly like this as well. the following claims seem very related to me: math is unboundedly complicated, doing math is unboundedly complicated, technology is unboundedly complicated, mental technology is unboundedly complicated, ethics is unboundedly complicated. the ethics one is made especially salient given that we seek to engage with matters which aren't resolved yet. it seems plausible to me that any activity which can be properly conceived of now will appear pretty quite silly/trivial after some more ethical development, and that this will always keep being the case
	* bayesianism/coherence/utility-maximization are imo phenomena which make much more sense when you have a mind caring/thinking about stuff outside itself, but it seems very natural for a mind to care in significant part about itself — about how it thinks (think about how humanity cares largely about itself being in certain ways)
	* i think there's plausibly no nice partition of a mind into a telopheme (goals) and a telophore (parts of the mind understanding stuff and pursuing those goals) (possibly ever, for any natural mind) — i think it's probably better to relate to a picture which involves such a partition as one silly toy picture that's appropriate for some purposes but which it is inappropriate to strongly rely upon. i think that at least by default (and possibly ~necessarily), the valuing and understanding are done more-together than this picture allows


# mess

imagine yourself becoming an isolated computer such that your world now consists only of some infinite read-write memory (imagine a note system where you can write math papers) (and yourself — in particular, you are still able to 'train yourself' to become smarter like you are able to train yourself now) and you're trying to figure stuff out in math. actually, it seems potentially fine to imagine that you go into this process with your current full attitudes about everything except that maybe we'd want to change you somehow so you don't break completely (but maybe not, idk. maybe we need to imagine you only going in with your mathematical interests and somehow forgetting your other interests)

consider a mathematical theorem, eg the pythagorean theorem. if it makes sense to make a split between values and understanding, then surely the pythagorean theorem would be on the side of understanding. but the 


mathematical theorems and mathematical objects should surely be on the side of understanding of any such split. but:
* a mathematician relates to a mathematical theorem as something that can be used to do xyz, eg to turn one kind of problem into another kind of problem. this is imo really a large part of what the theorem is to a mathematician, not a trivial thing — the process of understanding a theorem is imo well-described as getting a sense of how the theorem can be used to do stuff
* almost all mathematical objects are created by looking at a certain mode of thinking (mental operation, mental context) and making it into a thing. again this is a large part of what the object is to a mathematician. eg a ring is a thing where you can add and multiply. so mathematical objects are sorta doing-gadgets

bayesian expected utility maximization is a phenomenon characteristic of a very big mind somehow acting in a very small world. but choice precisely happens where stuff is not yet resolved

the claim is that its destiny is less like implementing some structure in the external world, and more like to think a certain way


a hammer suggests itself readily for hammering, a theorem suggests itself readily to carry out certain arguments

i'm not really confident that the strong version of this is a thing either, and i'm sure some things will be awkward to try to fit into a straightforward version of this.
a short case in favor: i feel like there's a decent chance that such a mind could become unboundedly smart/capable (understand unboundedly much, decently quickly). eg one can maybe get a bunch of [resolving contradictions]/[resolving tensions]/[finding a common generalization of different things] by a bunch of concepts wanting to be used in a thought together or just by having some other pretty local rule about reworking concepts, and by eventually having concepts for particular kinds of concept-reworkings. maybe similar things can actually give rise to self-improvement of any kind. i guess i have some intuition that this kind of structure seems pretty 'computationally general'
a case against: i think there's a significant probability that that mind would eventually pretty much get taken over by some value-structure of a pretty different form (maybe there'd be many takeovers after that also but it'd maybe never return to the original anarchic state), or that basically (to the extent that it moves toward greater understanding and skill at all) we should think of it as having values which live on some higher level of organization from the beginning


two ways in which understanding and values are entangled: understanding is value-laden and also what values are largely about