(moved here from my website)
# The trouble with unbounded utility functions (work in progress)

I claim that given Solomonoff induction, expected utility won't converge for an unbounded utility function, for any decision. (This is a claim that has been thrown In other words, an agent following these rules is subject to chronic Pascal's mugging. This is mostly just a formalization of [this post](https://www.lesswrong.com/posts/a5JAiTdytou3Jg749/pascal-s-mugging-tiny-probabilities-of-vast-utilitiesm), an attempt at getting closer to reality than https://arxiv.org/abs/0712.4318, an attempt of presenting this case formally but with alternative assumptions than in https://arxiv.org/pdf/0907.5598.pdf, and an attempt of formalizing/distilling the discussion in the thread above [this comment](https://www.lesswrong.com/posts/hbmsW2k9DxED5Z4eJ/impossibility-results-for-unbounded-utilities?commentId=GmmjPvYvEBiX8BtxP).

## The argument

For the first version of this argument, assume that the universe is implemented in a Turing machine with some part which is a non-real pre-processing workspace and some part which is the "real implemented universe". (I admit that this is a potentially weird metaphysical claim.) Also assume that we are total utilitarians that think utility scales linearly with the number of copies of an identical experience being implemented (at different times, let's say). As far as Solomonoff induction can tell, the following list specifies a possibility for how the universe could be, given your past observations:

1. You making every observation you made until now was hard-coded into the TM.
2. As for the future, there is a function implemented which simulates one human living a long happy life.
3. After creating all the hard-coded observed experiences, the TM calls this function $n$ times, where $n=f(m)$ is a function computed earlier.
4. This $f(m)$ is $m\uparrow \uparrow \uparrow m$, which is computed in the workspace.
5. $m$ gets assigned some arbitrarily chosen value.

The utility of this scales linearly with $f(m)$. The length of this program is a (huge) constant $C$ independent of $m$, plus $\log m$ bits for specifying $m$. Since all previous observations were hard-coded into the TM, the universe being this way is trivially consistent with all observations thus far. Its Solomonoff prior is thus (a constant independent of $m$ times) $2^{-C-\log m}=2^{-C}/m$. Since $\sum_m f(m)/m$ diverges, expected utility diverges.


We can probably get rid of the split of the TM into a background workspace and a "real part", as it seems like the rest of the computations (like computing a big number) should not change the value of the universe much, even if these are also real. We can get rid of the assumption that we are total utilitarians, as long as our utility function has example universes with provably large utilities. We can then loop over universes in the workspace to find ones with arbitrarily high utility, and then implement those. 

issue here with showing loop does not require simulating the universes and creating suffering. should have a really safe way of proving that a universe is high-utility, also issues with cached lives https://www.scottaaronson.com/papers/philos.pdf

## leverage penalty?
solomonoff + self-sampling assumption 

but this requires moral worth to be tied to agency, otherwise could construct hypotheses with lots of non-agent patients?

could be interesting argument for moral worth requiring agency

## Acknowledgments

I would like to thank Sahil Kulshrestha for many helpful discussions