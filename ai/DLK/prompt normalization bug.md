
In this section, we provide a heuristic explanation of a challenge with CCS reported in \textcite{farquhar2023challenges}, where the CCS probe simply learns a banana/shed classifier. More precisely, if we call the property identified by the probe $p$, then under the CCS interpretation, the probe would be saying that (almost) every 'Answer: True. banana' example has property $p$, almost every 'Answer: False. banana' example does not have property $p$, almost every 'Answer: True. shed' example does not have $p$ and almost every 'Answer: False. shed' example has property $p$. In what follows, we propose a plausible mechanism that would give rise to this behavior, as well as a heuristic explanation of how clustering would solve this issue.\footnote{The story we present here provided a major part of the ex ante motivation for trying clustering.}

Suppose that the data set of contrast pairs has a 'natural' split into two kinds, in a way that is uncorrelated with which element of the contrast pair is correct. An example of such a split is the banana/shed case above. For another example, in the original \textcite{burns2022discovering}, such a split into kinds is provided by the different ways to turn the same question into a contrast pair by prompting it somewhat differently.\footnote{See Appendix I of \textcite{burns2022discovering} for examples of different prompt templates for a question. Note that there are usually about 10 different templates, not 2; however, we do address the case where the split is into more than $2$ kinds later. In fact, we thought of the heuristic explanation we are presenting here originally in the context of finding out that normalizing the contrast pairs from all templates together leads to significantly worse probe accuracy compared to normalizing template-wise (which is what is done to compute the results reported in \textcite{burns2022discovering}).} There being two kinds of contrast pairs induces a corresponding partition of the data set $\mathcal{D}\subseteq \mathbb{R}^n$ of contrast pair difference vectors into two kinds — say this is $\mathcal{D}=\mathcal{D}_1\sqcup \mathcal{D}_2$, with $|\mathcal{D}_1|=|\mathcal{D}_2|$ for simplicity. To further simplify the discussion, we will discuss CRC-TPC in place of CCS. See \textcite{emmons2023contrast} for an argument that the difference between CCS and CRC-TPC is broadly minor in this context.

Let $\vec{\delta}_1$ and $\vec{\delta}_2$ denote the average contrast pair difference for $\mathcal{D}_1$ and $\mathcal{D}_2$.^\footnote{More precisely, $\delta_i=}If we normalize all of $\mathcal{D}$ together, then we subtract $\delta_1


In the worst case, if $\vec{\delta}_1$ and $\vec{\delta}_2$ are orthogonal to each other.

\subsubsection{Why would $\delta_1$ and $\delta_2$ differ?}

One can also present a case like this 


A completely analogous argument can be made for splits into more than two categories, $\mathcal{D}=\mathcal{D}_1\sqcup \mathcal{D}_2 \cdots \sqcup \mathcal{D}_k$. As the number of 



which is not 'refuting CCS theoretically'. of course it depends on whether there are some other properties that are 0/1 on contrast pairs which the probe might find!!! the entire claim is that there's a chance truth would be the most contrastive thing represented!!

and i had this XOR explanation for (with more detail than they give, because i actually talked about how this would arise on the level of activations, which they don't do)
### Discussion

\subsubsection{Implications for probing, concept erasure, and activation steering}


# A bug or a feature — context-dependent representations in models


are readoffs enough? well, you can say that you have these other directions with high variance before, and then if they correspond to different 


two claims:
In this section, we give a toy analysis of why on a data set $\mathcal{D}$ that 'naturally partitions' into two kinds of data, $\mathcal{D}_1$ and 
1) The feature version
2) If there are readoffs $r_1$ and $r_2$ such that $r_1$ 

## ein neuer Versuch 

a model: a bunch of readoffs, and the two contrast pair elements differ along a few

suppose that a property is supported on a sparse set of neurons. then perhaps each neuron readin also has some large component from some SAE feature? or at least the neuron readins should relate non-generically to SAE directions in the previous layer? 

Can we make this work with just readoffs? Well, we can assume that the vectors are constructed so as to make some readoffs salient, perhaps. Then there could always be some crap added in other directions, right. But as long as this other crap is not systematic, it won't be picked up. Can we make this precise? Well, could assume that the representations are such that they have the right readoffs. suppose there is a set of readoffs that might matter. under which readoffs would these two sentences have different readoff values? 

maybe there are some number of readoffs along which the pair elements differ. maybe a small number of readoffs, maybe context-dependent ones? suppose there is a context-dependent readoff. can we also think of it in some other way? i guess we can maybe think of it 

the point is that the truth readoff direction has a certain variance; the other readoffs along which the contrast pairs differ also have certain variances. can we explain what's going on from just these facts alone? 

in principle, could differ along many axes. can say something about the set of properties here? like, there is a truth readoff and a bunch of other readoffs. the contrast pair elements will differ along all of these readoffs. 

what if there are different context-dependent truth directions here? i guess the point is that if they are orthogonal, then you will just pick up one and not the other maybe? this is done by PCA i guess if you have a data set that has a bunch of plus minus things in each direction — you'll have one direction discretely overtaking another in that case — it's not better to take some 

in high dimensions, can maybe just represent anything you like? why would stuff that is 

so a bunch of stuff is represented. can see from the subspace of variance the support of the readoffs which are changing on these pairs. if we make the sentences similar enough, getting a small subspace, i think we would expect 

suppose more than d things active at once. then there are readoff values which are linear combos of other readoff values with reasonably small coefficients?

like, say there are d+1 active readoffs in dimension d. then we can write any one as a linear combo of the others. what about the coefficients? i guess that there is probably a way to do it also so that the sum of squared coeffs is about 1 here? so in terms of just the readoffs which are active, we can write $r_i = \sum_j c_j r_j$, so the value of readoff $r_i$ is also this linear combo of the values of the readoffs $r_j$. of course these linear combos exist generally — that's just about there being a bunch of vectors packed in a smaller-dimensional space. but something goes wrong when they are also densely activated? hmm, note that the readoff is only given up to error $\sum_j c_j \varepsilon$ though, which worst-case is going to be $\epsilon \sqrt{d}$. with random signs, it could be $\epsilon$ though, which would maybe give a contradiction? so the problem is that the signs do in fact conspire. can we use this to also get the signs to conspire with a smaller set of vectors? well, then we can't get the nice small coeffs, right? can we select a set which always has the signs conspiring though? 

so whether the signs conspire unfortunately doesn't just depend on the vector pair right? it depends also on the particular activation vec. it even depends on the coeffs! hmmm how can we get some signs to not conspire

can we maybe write down a linear combo of these readoff vecs that needs to be zero? that is a sort of interesting constraint on the readoffs right? but yea the readoffs only need to work out to error eps. can we show it's fucked anyway — the signal needs to overwhelm? ok so there exist some nice coeffs, adding up to only like 2

an observation is that the errors need to always conspire to make the linear relation work out. of course, this is also true when you don't get a bunch of stuff on at once. how does that case make stuff any worse really? like sure, you get larger steps then. ok whatever, suppose you get about sqrt{d} things on at once. then you could turn a single thing off or on, and each one of the sqrt{d} ANDs associated with it needs to be turned off. so there's some relation between the vectors before and after turning off here — they need to differ by a bunch along some sqrt{d} directions, and not much along some >d directions. also, there's a bunch of 

can we find a set of size sqrt{d} here

let's try another angle: what's the issue with the usual construction? well, noise along any one direction goes out of control. you'll read rightly from only a small fraction of dimensions, as soon as you get to some kd things present at once. i guess maybe the problem is that making all the other readoffs work out as desired is going to fuck with some readoff too much? so you have to be high along some kd directions at once. does that start to really pin down the value along any one in a bad way? one observation is that for a typical set of d+k directions, there won't be a way to make all of them high at once. the point is that there won't be any vector that is simultaneously in the direction of all of them! maybe this is almost precisely the right question if we make it a high-low distinction instead of 0/1 or something? so now for any set of k sqrt d inputs, there is a corresponding set of k^2 d readoffs such that you need to be high along all of these at once, so minimally you have to make them be in the same half-space. this is a bunch of constraints 

oh wait but high-low is in fact doable! it's done in the input! so i guess maybe the hard bit is getting the OR to give 0 while the AND gives 1. do we need to say that the 






## der vorherige Versuch

status (epistemic and otherwise): putting ideas out there, proposing a framing, heuristic reasoning, lab note, bug report
## Introduction
In this piece, I will (1) present an informal framework for thinking about features in models^[I do not make a claim to novelty re this framework], (2) justify the mean-normalization step of [CCS](https://arxiv.org/pdf/2212.03827.pdf) in terms of this framework, (3) describe a silly little normalization bug that plagued a CCS-extension [codebase](https://github.com/EleutherAI/elk) for months, (4) explain how the feature framework can/must be amended with context-dependent features to make sense of the damage caused by this bug, (5) discuss whether the same data can be made sense of in a discrete picture with different features, and use this framing to (6) suggest possible improvements on probing, as well as (7) possible improvements on representation removal.

## Concepts $\iff$ directions in activation space
I will explain the correspondence between concepts and directions in activation space


## Technical details of the thing

## What must be going on
Suppose the data can be partitioned into two kinds, with different pseudolabel directions $\delta_1,\delta_2\in \mathbb{R}^n$ (let's pick the sign convention that this is the negative-to-positive pseudolabel direction). De-meaning the positive-pseudolabel activations and the negative-pseudolabel activations is then the same (insofar as the difference between the two elements in a contrast pair is concerned, so insofar as e.g. TPC is concerned) as subtracting the mean pseudolabel direction $\frac{\delta_1+\delta_2}{2}$ from each positive-pseudolabel activation vector. This leaves a pseudolabel direction of $\frac{\delta_1-\delta_2}{2}$ on datapoints of the first kind, and a pseudolabel direction of $\frac{\delta_2-\delta_1}{2}$ on datapoints of the second kind. Note that if $\delta_1\neq \delta_2$, then the direction $\delta_1-\delta_2$ can still be used to separate the contrast pairs. I think this is the correct explanation of why it is important to normalize by prompt, but I think we have discussed this already, and this is not the main reason I am writing this now. I think one other take-away from this example is that there is an important difference between removing the ability to linearly predict a certain property, and removing all information about properties of this kind. For instance, in the example above, while we roughly remove the ability to tell the difference between the two pseudolabels with a linear probe, it remains quite possible that after this removal, the TPC result just still completely captures data about pseudolabels. (Namely, it would capture the pseodulabel on each kind of datapoint, but with the orientation flipped depending on the type.)
The main reason is that I have been wondering how to fix this issue: is there a way to get rid of all the pseudolabel-like information from representations? One thing one could do is some clustering of contrast pairs into some small number of types, and then removing the pseudolabel direction for each type.
(by clustering I just mean taking the contrast pair average and clustering those vectors using some standard clustering algorithm which is known to be reasonable for activations)
Here's a story that makes sense of this: diff features

In fact, in a sense, this must be what is happening, because otherwise we'd get the exact same result whichever way we normalize! So the fact that the accuracies are meaningfully different implies that the features are meaningfully different, too.

## Implications for probing
maybe train probes for different contexts? would be good to have an experiment here

Experiment request:
1) Pick a data set for which the way normalization is done (promptwise vs not) matters a lot (i.e. a significant change in the accuracy).
2) Find if it still matters a lot for some pair of 

the pseudolabel direction for each template, find the cosine of the angle between these vectors, as well as the magnitudes of all of these vectors. (The point is to understand something about how much the pseudolabel direction differs ). Could we find a pair of templates such that a probe trained on the two with individual 



A task: I would like to try a version of probing where instead of we first cluster inputs and then apply a probe 
Look into the literature on context 
use embedding similarities to tell context

concrete experiment: see if probes obtained this way generalize better
other concrete experiment: instead of probing with a particular direction, find cluster of new data, within which find two subclusters, so essentially new probe when OOD?



## Implications for concept erasure


## So, are representations nonlinear then?

can think of this as a single feature with direction depending on context, or multiple context-dependent features

but probably not a binary thing right? probably gradually going from one to the other?

the binary interpretation here would be that there are e.g. two different features, with different probabilities of being used for the different prompts (one has high probability of one feature, the other has high probability of the other feature). This seems less likely to me. Perhaps it could be tested emprically.x

`






