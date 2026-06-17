
here is a rough high-level pictures of how a human obtains command of a mathematical structure (eg the natural numbers):
* one 'adds axioms to an inventory', ie specifies relations that can be used with the objects (one needn't be conscious of these relations, and one often isn't). these needn't at all be minimal — there doesn't need to be much of a distinction between 'axioms' and 'theorems/lemmas' — e.g., for the natural numbers, we might include commutativity as a rule that can just be employed directly (in PA, commutativity is a theorem that can be proved using the induction axiom and other axioms). t
* i think canonical structures (the natural numbers, the real numbers, things in calculus) can get pinned down by this uniquely because they are categorical / they satisfy some universal property
* some more on what this process of coming to have command of a structure might look like — imagine a physicist coming to have informal command of some novel mathematical structure:
	* they start with some list of desired relations (these can be sorta implicit i guess)
	* they might (implicitly) try out different new relations. they discard ones that cause 'collapses'/'contradictions'
	* if a desirable relation causes incoherence, this prompts the physicists to revise some of the previously tentatively (implicitly) accepted relations
	* relations can be made more precise, or have their domain of applicability more precisely delimited, by thinking about how they ought to apply in less standard cases
	* after playing around enough, you might have an (implicit) set of manipulation rules which pin down the structure uniquely — there is some kind of associated categoricity result

a few of the many things i don't currently understand:
* categoricity results are usually in second-order logic, which is sorta fucked. maybe we want to rely on categoricity in a first-order way but inside some larger background (set) theory corresponding to all of the physicist's understanding that can relate to this structure or something?
* there ought to be some relation between categoricity and universal properties — are they the same thing somehow? is categorical definition (eg real numbers are the unique linearly ordered field such that blabla) a special case of a universal property definitions?

incidentally, maybe this points at a natural notion of complexity for a mathematical structure: its the ease of finding it in some relation-search, which relates to the length of the smallest set of conditions determining it (ie the sum of lengths of the assumptions in the smallest categoricity result for that structure or something), but maybe this also prefers things which are universal in many different ways (they can then be found along many branches of a relation-search)

of course, in practice learning eg the natural numbers fucked up, there's lots of memorizations and shit involved, but this hopefully captures the high-level structure of the process