
# A [criticism of]/[[question/confusion] about] maximin decision rules for safe general intelligences

(e.g. the decision rule in [infrabayesianism](https://www.lesswrong.com/posts/DMoiZDYZzqknfvoHh/infra-bayesianism-distillation-realizability-and-decision#The_Minimax_Decision_Rule); also used (with modifications) in the plans of [davidad](https://www.lesswrong.com/posts/pKSmEkSQJsCSTK6nH/an-open-agency-architecture-for-safe-transformative-ai?commentId=ZuWsoXApJqD4PwfXr) and [Bengio](https://youtu.be/31eO_KfkjRQ?t=1945))

I take some people to view the following line of reasoning in favor of maximin favorably:
* The real world is too complicated for a realistic system (inside it) to 'fully hold in its head', precluding e.g. some ideal form of bayesianism in which (e.g.) all possible 'world-processes' that might be generating one's stream of observations are held in one's head and updating corresponds to crossing out the processes which are in contradiction with what one has previously observed. It makes sense to try to make^[or, to begin with, to contemplate as a serious candidate for an ideal version of a realistic intelligent aligned system] an intelligent system which has a partial model of the world, and, in the interest of safety, picks an action which makes the worst-case (expected) outcome as good as possible, where worst-case means worst-case over all specifications of the parts of the world-process 'outside the partial model of the world'.

One can also give a parallel line of thought where instead of or in addition to maintaining only a partial model of the world that could be extrapolated in various ways which are to be maximin-ed over when making decisions, one maintains only a partial model of goodness (or neg-harm) that could be extrapolated in various ways which are to be maximin-ed over when making decisions. This would be motivated by an analogous thought that while values might be too tricky to pin down, one can perhaps provide a correct partial specification (catch our true values in some convex set in some kind of value-space, say), with the minimax rule w.r.t. the remainder of the specification being motivated by an aspiration to act cautiously.

This seems wrong to me — I think holding a partial model over whose completions one is maximin-ing which is actually helpful for addressing the issue that it is hard to pin down a model correctly enough to just maximize expected utility yields either paralysis or being guided entirely by some comparison of $\varepsilon$'s which is hard to analyze.^[I also find it suspect that the verdict of such a decision rule would be any easier to compute than that of naive bayesian expected utility maximization — that is, I don't see reason to think it wouldn't be ~equally impossible in any realistic case. Perhaps the point is that each decision rule is to be approximated instead, and it is for some reason easier to approximate the knightian one while getting a safely acting agent? I don't see why that would be the case. Anyway, I don't want to focus on this objection.] 

unfinished: give bit counting argument. for this to be useful, there needs to be a significant number of bits remaining in the specification, but then for any action, one can cook up a weird specification which makes it look very bad. one then compares some $\varepsilon$ utilities to act in the infrabayesian case, and some $1-\varepsilon$ probabilities of harm in the davidad case.


# some comments

If you need to get 10000 bits right to specify harm, if you think you can get 9900 of these bits right but want to act with a max rule wrt the remaining 100 bits, ie act conservatively wrt these 2^{100} hypotheses, since there are these 10^{-12} \approx 2^{-40} probability hypotheses saying any major action probably gets you killed, you will probably have a hypothesis remaining in your set of 2^{100} hypotheses that says p(harm|hypothesis)>50%, and so you can't take any action if your harm threshold is below 50%. That you have such a hypothesis remaining could in principle be false if your 2^{100} hypotheses have some specific structure; in particular, if they are all similar in the harm probabilities they assign, but I doubt they'll have any very principled structure. Also, if they were always uniform, you could just equivalently use the expectation decision rule.

Relatedly: if "harm happens" is itself close to a hypothesis, then acting with a max decision rule is clearly worse than the expectation decision rule.

Anyway, this already says that >9900 of these 10000 bits would need to come from somewhere else, which is a version of the claim that the decision rule isn't going to be doing heavy lifting. And I'd guess that if the other thing gives you 9900 bits, then it'll get probably get pretty close to 10000 as well
## mess

But when I try to think quantitatively about this kind of thing, it appears like a complete non-starter.^[I also find it suspect that the verdict of such a decision rule would be any easier to compute than that of naive bayesian expected utility maximization — that is, I don't see reason to think it wouldn't be ~equally impossible in any realistic case. Perhaps the point is that each decision rule is to be approximated instead, and it is for some reason easier to approximate the knightian one while getting a safely acting agent? I don't see why that would be the case. Anyway, I don't want to focus on this objection.]

I've asked (something like) the above from a few people working on stuff in this vicinity, and I think gotten mostly agreement with my skepticism in response. Of course, pointers to places where something like this objection is addressed are as welcome as answers.



https://www.lesswrong.com/posts/pKSmEkSQJsCSTK6nH/an-open-agency-architecture-for-safe-transformative-ai?commentId=ZuWsoXApJqD4PwfXr#ZuWsoXApJqD4PwfXr



