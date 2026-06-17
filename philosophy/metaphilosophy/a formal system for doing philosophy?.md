

## voice notes

Philosophy seeks understanding as opposed to knowledge.
In mathematics, we also seek understanding. 


## note

a kind of thing in philosophy which maybe could be automated: noticing connections? like mere addition paradox? noticing connections seems analogous to math (langlands program) but will need to think more about this
## writeup attempt

Safely getting meaningfully superhuman mathematical problem-solving out of an artificial intelligence seems feasible. A reason for this is that, since about 1925, we've possessed a way to clearly state mathematical problems and a precise notion of what it is to provide a solution to a particular mathematical problem. For example, the following is the twin prime conjecture written in the language of set theory (meta-remark: idk if this example is the best one or if an example is necessary. it will look fucked if we have to translate to base ZFC. perhaps an annotated version would make sense, ie where we eg point out which part just defines the naturals or whatever):
$$\forall n \in \mathbb{N}, \exists p>n... $$
A proof of the twin prime conjecture corresponds to a sequence of strings in this same language such that each string is either an axiom or is produced by the application of some inference rule to some strings which appear earlier than it in the sequence. Importantly, as it is decidable whether a given string is an axiom and decidable whether a given string can be produced by some inference rule from some strings from a given finite sequence of strings, it is also decidable whether a given sequence of strings constitutes a proof of a given statement. (Indeed, software exists for checking proofs written in the language of set theory: https://en.wikipedia.org/wiki/Mizar_system .) This makes it look plausible that, conditional on us figuring out how to train an artificial system which is better than humans at general reasoning, we could 



questions:
* What does it take 



potentially for https://www.lesswrong.com/posts/52ygLry5KCdvxY6zn/essay-competition-on-the-automation-of-wisdom-and-philosophy

We did mathematical reasoning sorta-informally for a long time, but it turned out to all cache out in a formal system. We can now imagine stating formal theorems and asking a safe superintelligence to prove them for us. Wouldn't it be great if we could pull off the same thing for philosophy^[or science, or just general reasoning — anyway, these might just be the same thing in this context, i.e. formalizing any one of these might pretty much imply formalizing any other]?
* What are the obstacles to doing this for philosophy which are not present for mathematics? In which ways is doing this for philosophy disanalogous to doing this for mathematics?
* A question we can ask is: how was this done for mathematics? How would we do it for mathematics if we hadn't done it already (mention Tsvi's good advice to dumber self thing)? How would we take mathematical practice and do it in an automated manner using machine learning? This seems fairly concrete!

## references

lots of GOFAI stuff

Leibniz's "calculemus":
[...] if controversies were to arise, there would be no more need of disputation between two philosophers than between two calculators. For it would suffice for them to take their pencils in their hands and to sit down at the abacus, and say to each other (and if they so wish also to a friend called to help): Let us calculate.

https://philosophy.stackexchange.com/questions/2445/is-philosophy-formalisable

https://www.lesswrong.com/posts/5bd75cc58225bf0670374ea3/trustworthy-automated-philosophy
## other notes for that essay contest
can we say something about generation vs verification difficulty in philosophy? https://cdn.openai.com/papers/weak-to-strong-generalization.pdf
which components of philosophy might automation contribute to fastest?
* seeing inconsistencies in your ideas
* suggesting ways to resolve inconsistencies
* doing literature reviews
* critiquing writing
* expanding ideas into paper
* 
