

ok, so the gödel sentence (P='the sentence blabla is not provable', where blabla ends up referring to the thing itself) is not provable. but then by gödel's completeness theorem, there needs to be a model of the theory in which P is false. ok, so we have a model where a certain ground set element fits into a formula that says there exists a proof. i guess the statement says that there exists an n such that there is a thing of length n such that blabla. and if this n were finite in this, then we'd indeed be screwed. is the trick that the n needs to not be SSSSS0, instead it's some weird other natural number kinda thing? so there sorta is a thing that fits into exists n exists seq of length n of numbers which is a proof of gödel sentence but it's some completely fucked thing?

wait but still... 

yea i guess it could just be that the integer specifying the proof length is infinite. so the statement says that there exists weird-integer-sized-set such that there is a map from this set to integers (thought of as propositions) where anything follows from stuff before. (i guess all the 'statements' themselves could also be wacky)

so maybe really the statement should say that there is a true but unprovable statement about the standard integers!! (a later correction-clarification here: these are just the integers of the metalanguage though i think — no spooky standard integer concept needed here i think)


maybe related: A _T_ that interprets arithmetic is **ω-inconsistent** if, for some property _P_ of natural numbers (defined by a formula in the language of _T_), _T_ proves _P_(0), _P_(1), _P_(2), and so on (that is, for every standard natural number _n_, _T_ proves that _P_(_n_) holds), but _T_ also proves that there is some natural number _n_ such that _P_(_n_) _fails_.[[2]](https://en.wikipedia.org/wiki/%CE%A9-consistent_theory#cite_note-Kleene71-2) This may not generate a contradiction within _T_ because _T_ may not be able to prove for any _specific_ value of _n_ that _P_(_n_) fails, only that there _is_ such an _n_. In particular, such _n_ is necessarily a [nonstandard integer](https://en.wikipedia.org/wiki/Non-standard_model_of_arithmetic "Non-standard model of arithmetic") in any [model](https://en.wikipedia.org/wiki/Model_(logic) "Model (logic)") for _T_ (Quine has thus called such theories "numerically insegregative").[[4]](https://en.wikipedia.org/wiki/%CE%A9-consistent_theory#cite_note-4)

from https://en.wikipedia.org/wiki/%CE%A9-consistent_theory


### Consistent, ω-inconsistent theories[[edit](https://en.wikipedia.org/w/index.php?title=%CE%A9-consistent_theory&action=edit&section=3 "Edit section: Consistent, ω-inconsistent theories")]

Write PA for the theory [Peano arithmetic](https://en.wikipedia.org/wiki/Peano_axioms "Peano axioms"), and Con(PA) for the statement of arithmetic that formalizes the claim "PA is consistent". Con(PA) could be of the form "No natural number _n_ is the [Gödel number](https://en.wikipedia.org/wiki/G%C3%B6del_number "Gödel number") of a proof in PA that 0=1".[[7]](https://en.wikipedia.org/wiki/%CE%A9-consistent_theory#cite_note-7) Now, the consistency of PA implies the consistency of PA + ¬Con(PA). Indeed, if PA + ¬Con(PA) was inconsistent, then PA alone would prove ¬Con(PA)→0=1, and a reductio ad absurdum in PA would produce a proof of Con(PA). By [Gödel's second incompleteness theorem](https://en.wikipedia.org/wiki/G%C3%B6del%27s_second_incompleteness_theorem "Gödel's second incompleteness theorem"), PA would be inconsistent.

Therefore, assuming that PA is consistent, PA + ¬Con(PA) is consistent too. However, it would _not_ be ω-consistent. This is because, for any particular _n_, PA, and hence PA + ¬Con(PA), proves that _n_ is not the Gödel number of a proof that 0=1. However, PA + ¬Con(PA) proves that, for _some_ natural number _n_, _n_ _is_ the Gödel number of such a proof (this is just a direct restatement of the claim ¬Con(PA)).

In this example, the axiom ¬Con(PA) is Σ1, hence the system PA + ¬Con(PA) is in fact Σ1-unsound, not just ω-inconsistent.



oh ok it's discussed here https://www.lesswrong.com/posts/MLqhJ8eDy5smbtGrf/completeness-incompleteness-and-what-it-all-means-first:

## Gödel's completeness theorem

Enough with _in_completeness; what about Gödel [completeness theorem](http://en.wikipedia.org/wiki/Completeness_theorem)? Unlike the previous theorem, this is a statement about about the axiomatic system and _all_ of its models. It simply says that if a sentence is valid (true in every model) for a first order theory, then it can be proved from the axioms. This provides a bridge between the semantic concept of "true" (true in every model) and the syntactic concept of provable (can be proved by these formal manipulations). It also implies that we can enumerate all the sentences that are valid in a first order system, simply by enumerating all the proofs.

Where does this leave the Gödel sentence G? We've seen we can't prove it from the axioms, hence it cannot be true in all models. Therefore there must exist a model N' of first order Peano arithmetic in which G is false. What does that mean? G claims that "there does not exist a number n with (certain properties)", so if G is false, such an n does exist. Now we know (because we've constructed it that way) that if that n were a natural number, then those (certain properties) means that it must encode a proof of G. Since there is no proof of G, n cannot be a natural number, but must be an extra, a non-standard number, from beyond our usual universe. This also means that those (certain properties) do not capture what we thought they did: they only mean "encodes a proof of G" for the standard natural numbers.

This seems somewhat troubling, that Peano arithmetic would admit two distinct models and fail to say what we thought it said; but it gets worse.
