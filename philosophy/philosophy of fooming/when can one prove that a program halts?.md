
in alignment, we can be interested in making a system that maintains a commitment across a very long stretch of activity (very related: stability, goal stability, reflective stability). as a toy version of this, we can consider making a program that halts after doing a lot of stuff. let's consider the specific case where we want to prove that the program halts. this introduces the question:
> Which programs halt provably? Can we characterize such programs?

this question has an easy answer: assuming ZFC is sound, the programs which provably halt are precisely the programs that halt. this is because if a program halts, it provably halts (you can prove this by just walking me through the valid finite computation history which finishes at halting step by step), and if a program does not halt, then assuming ZFC is sound, there is no proof that it halts (soundness just means we can't prove a falsehood). One possible way to proceed here is to ask:
> Which programs have short proofs that they halt (like, much shorter than checking the computation history)?

We could alternatively think of not halting as the commitment, suggesting the following question:
> Which programs provably run forever?

Of course, if ZFC is sound, then for programs which halt, there is no proof that they run forever. But some programs which run forever also lack proofs that they do — for instance, if ZFC is consistent, then the program searching for a proof of 0=1 in ZFC runs forever but it isn't provable that it runs forever.