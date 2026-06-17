


topic modeling
1) can we frame our problem so that we can apply methods from topic modeling?
2) just mention that it's related but different from even the model-agnostic case — it's about token predictions, not about words in that way

trying to construct an analogy: maybe the activation vec is generated from some latent model?


arora talk on skills

come up with a model of using skills which has the property that the skills used can be read off the similarity scores? preferably in a really robust way?


todo: consider task decomposition but for middle-layer activations? does this make sense? like the q is which middle-layer activations are seen the same way




In this post, we first motivate why thinking about task decomposition and task
similarity might be important. Second, and more importantly, we give brief starting points for
several different metrics of task similarity (most of which correspond to
task decomposition methods) that one could use for LLMs. An example of work
using such a metric is [here](https://www.lesswrong.com/posts/qCecZwptWuAEZN3Td/transfer-learning-and-generalization-qua-capability-in). If you don't want the motivation, feel
very free to skip straight to the 'Methods for gauging task structure in ML' heading below.

Epistemic status: have thought about this stuff for a while, but mostly
in messy notes or conversations. This post was written very quickly and
may be disjointed.

# Motivation
-   It would be a real boon for alignment — interpretability in
    particular — if each ML model (or transformer language models
    specifically) could be understood as a large 'task dictionary'
    together with simple algorithms (circuits) for each task (think: [an algorithm that captures (some of) how GPT-2 determines indirect objects in certain cases](https://arxiv.org/pdf/2211.00593.pdf)[^1]). In this
    case, we could hope to understand a model by decomposing its domain
    into specific tasks, then reverse-engineering what circuit is
    implemented in the model for each task individually, and also
    reverse-engineering how the model computes this task decomposition.
    Perhaps things are like this! We happen to doubt they are very much like this,
    especially for those models or those parts of models that are
    important for understanding general intelligence and for aligning
    generally intelligent systems. Nevertheless, we hope the similarity
    metrics outlined in the post can (a) help figure out the extent to
    which this task-dictionary hypothesis about language models is
    right; and (b) conditional on that hypothesis being right to some
    significant degree, lead to methods for (automatically) determining
    the way a model sees its domain as being decomposed into tasks.

-   Separately, having a way to quantify the distance between tasks
    could lead to a way to measure the ability of a model to
    generalize.[^2] Other than being of object-level interest, this is
    helpful for evaluating and predicting capabilities. Indeed, the
    ability to generalize (which is intuitively related to the ability
    to learn quickly) is often cited as a key limitation of present ML
    models compared to humans. We think it'd be interesting to use
    \[task distances \[models are able to generalize across\]\] to
    measure generalization ability in models and humans, e.g., for
    forecasting when model generalization performance will beat human
    generalization performance (i.e., maybe, when we'll have AGI). One
    can also perhaps use such metrics to track model generalization in
    more fine-grained ways, e.g. comparing the input clusterings of
    different Pythia checkpoints to see when certain inputs first come
    to be seen as similar by the model, or comparing the subtask
    clusters of GPT-3 to those of GPT-4, potentially seeing certain clusters
    merge or split.

-   Finally, we find it scientifically interesting how
    a domain might be decomposed into tasks: it would be nice to better
    understand what makes two things similar in general. Automated ways to determine the
    similarity-structure of a domain would be helpful, and LLMs give us an easy starting
    point for this broader scientific aim.

# Important distinctions we don't track in this post

-   'Task decomposition simpliciter' vs 'a particular subject's task
    decomposition': We will sometimes talk about the task decomposition
    (of, e.g., natural language) without referring to a particular
    reference observer/agent; and sometimes about how some particular
    model or another (or a human) (implicitly) decomposes natural
    language into tasks. Here are some ways in which these are
    related: (1) each can provide a helpful guess for the other; (2)
    alternatively, one could argue that the former really only makes
    sense as a case of the latter with the observer left implicit
    (though we think there's more to the former than that); (3)
    uniformity across observers of the latter (is worth investigating and) could help establish that the former is a sensible thing to consider. But we won't track this distinction.

-   Task similarity vs input(-output-pair) similarity vs decomposition:
    A way to measure the distance (from a model's point of view) between
    two inputs (or input-output pairs) can generally give rise to a way
    to partition inputs (or input-output pairs) into tasks: apply a
    clustering algorithm on the complete graph whose edges are labeled
    by these distances. However, some of the methods below make sense
    mostly just for measuring task-to-task similarity, not for measuring
    the similarity between two inputs. In this case, providing an
    associated decomposition algorithm appears nontrivial. While we
    believe this can be done in particular cases, we ignore it in this
    post. Also, given a way to measure the similarity between two
    inputs, one can measure the similarity between two tasks with the
    expectation of the similarity between a random input from the first
    and a random input from the second.

-   Absolute vs relative metrics vs clusterings: Most of the metrics
    provided below are not intended to output individually
    meaningful/interesting numbers; however, the numbers can become
    meaningful when compared to other outputs. For example, it's hardly
    meaningful to say that a pair of inputs have a certain kind of similarity $0.08$, but it could begin to be meaningful in a context where other similarities are
    $-0.3,-0.002,0.001,0.003,0.15,0.9$. And even if these similarities
    are also somehow wrongly normalized — the ordering of these
    similarities is sometimes not that of the 'true similarities' —
    clusterings could still be meaningful.

-   Mathematical precision: We won't be mathematically careful (that
    said, we will try not to get anything 'wrong'). For example, we will
    not discuss which clustering algorithm is most appropriate in a
    particular context. To be clear: we consider it obviously valuable
    to be mathematically careful — it's just outside the scope for
    now.


# Methods for gauging task structure in ML

In this section, we specify a number of ways one can try to measure task similarity.[^3]

## Inspecting activations

-   Activation distance: Let $S_A$ and $S_B$ be sets of activation
    vectors (perhaps from a middle layer[^4]) obtained by taking
    instantiations of task $A$ and $B$ respectively and passing them
    through the model. A similarity metric for the two tasks $A$ and $B$
    is, for instance,
    $$d(A,B)=\left\lVert \frac{\sum_{v \in S_A}v}{|S_A|}-\frac{\sum_{v \in S_B}v}{|S_B|}\right\rVert.$$

    (Instead of using the $L^2$ norm here, we could also use cosine
    similarity, or maybe run the data points through a SAE and
    compute the correlation between SAE coefficients, or use some other
    more principled norm (maybe [this](https://arxiv.org/pdf/2311.03658.pdf)?).)

To compare activations on particular inputs, replace the averages by the activation vectors on those particular inputs. Instead of comparing activations that live in a particular activation space, we could of course also compare the activations that e.g. a particular OV part outputs.

-   activation steering transfer: Take some pair of tasks $A$ and $B$. First, obtain some steering vector representing a meaningful disposition towards task $A$ (e.g. a disposition to play 'cooperate' in a prisoner's dilemma). Then, steer the model on task $B$ with the steering vector. Compare the resultant behavior on $B$ to baseline performance on $B$. So, the metric is, say, $$d(A,B)=D_{KL} \left( A \middle\| (A|B_s) \right).$$

-   Probe transfer: Take two tasks $A$ and $B$ in the context of both of which some intuitive concept makes sense. For example, task $A$ might be a set of English sentences labeled 'true' and 'false', and task $B$ might be a set of Spanish sentences similarly labeled. Then, train a logistic regression to predict from middle layer activations whether an English sentence is true or false. Then test how well that probe transfers to the Spanish sentences. Formally, $$d(A,B)=\text{probe-acc}(A)-\text{probe-acc}(B).$$ This is supposed to give a way to access whether a model sees the two tasks in terms of the same concepts. One could also do something similar with concept ablations — i.e., checking if they transfer (either in terms of changing behavior in a reasonable way, or in terms of making the same concept inaccessible (see [this](https://arxiv.org/pdf/2306.03819.pdf)) in the other context as well).

## Inspecting learning

-   Fine-tuning transfer: Take some pair of tasks $A$ and $B$. First
    fine-tune on task $A$, then briefly fine-tune on task $B$, and
    compare performance on task $B$ to the case where we fine-tune (for
    equally many steps) on $B$ throughout.[^5] So let's say
    $$d(A,B)=1-\frac{L(B|\emptyset)-L(B|A,B_s)}{L(B|\emptyset)-L(B|B,B_s)},$$
    where the conditional notation is meant to specify what the model
    has been fine-tuned on, with $B_s$ representing a small fine-tuning
    set of task $B$.

-   Few-shot prompting transfer: repeat the above point but with
    in-context learning. That is, few-shot prompt with examples of $B$
    vs examples of $A$ (maybe with a smaller number of $B$ at the end
    again), then ask it to do $B$. So, let's say,
    $$d(A,B)=1-\frac{\text{acc}(B|A)-\text{acc}(B|\emptyset)}{\text{acc}(B|B)-\text{acc}(B|\emptyset)}.$$[^6]

-   Pre-training transfer: repeat the above point but with more thorough
    training, perhaps seeing how much cutting $A$ from pretraining hurts
    performance on $B$, or how much cutting $A$ and $B$ hurts
    performance on $B$ more than just cutting $B$. So, let's say,
    $$d(A,B)=1-\frac{L(B|\neg B)-L(B|\neg \emptyset)}{L(B|\neg A,\neg B)-L(B|\neg \emptyset)}.$$
    Or, analogously to the fine-tuning transfer metric above, we could
    compare accuracy on $B$ \[when one trains solely on $A$ and
    fine-tunes on $B$\] to when one just trains on $B$ for equally many
    steps.

## Inspecting weights

Note that the first three metrics in this section would have fit equally
well under the above subsection on learning.

-   clustering gradients (from [here](https://arxiv.org/pdf/2303.13506.pdf)): take two tasks (or single
    input-output pairs) $A$ and $B$. Compute the gradients
    $\nabla L (A),\nabla L (B)$ on the two tasks. We could then let
    $$d(A,B)= 1-\frac{\angle \left(\nabla L (A),\nabla L(B)\right)}{\pi}.$$

    Alternatively, we could see how much a gradient update on one input
    affects the computation on another, perhaps measured in terms of the
    $L^2$ distance between activation vectors (or just the KL-divergence
    of the output distribution) on the other output before and after the
    update.

-   optimal grafting overlap (from [here](https://arxiv.org/pdf/2302.06600.pdf)): Fine-tune a model on some
    task $A$. Then go back to the original model, and carefully pick a
    tiny set of parameters to replace with parameters of the fine-tuned
    model, making the performance on the task as good as possible. One
    can then measure the distance between two tasks by how different
    their sets of grafting parameters are. Formally, letting the
    grafting index sets be $S_A,S_B$, we could let
    $d(A,B)=\frac{|S_A\setminus S_B|}{S_A}$.

-   weight ablation transfer/similarity: Take two tasks $A$ and $B$. For
    each model component (or weight in a more fine-grained sense, e.g.,
    the edge between two neurons), (zero/random) ablate it and measure the change in
    performance in $A$, as well as the change in performance on $B$.
    Storing these KL divergences (or, alternatively, absolute values of
    the changes in the loss) in two vectors $v_A,v_B$, the metric could
    then be, say,
    $$d(A,B)=1-\frac{v_A\cdot v_B}{\lVert v_A\rVert \lVert v_B\rVert }.$$

-   mixture of experts overlap: Take two inputs $A$ and $B$, and pass
    them through the model, and see if they go through the same expert.
    This is perhaps particularly interesting in switch transformers,
    where we can get a more fine-grained view of expert similarity
    (whether or not the two inputs go through the same expert isn't just
    a binary — one can examine whether the choices made in the many
    switch layers line up). Formally, in the switch transformer case, we
    can let the distance $d(A,B)$ be the fraction of switch layer
    choices that do not match.

# Analogues in humans

-   Many of the above metrics transfer — somewhat gracefully — to
    humans. For example, it is easy to imagine metaphorically
    fine-tuning a mathematician to be good at, say, physics. There would
    likely be a reasonably large transfer there, and the same would
    likely hold in an LLM trained on maths and fine-tuned on physics. It
    is intellectually interesting whether our intuitive, human task
    clusterings transfer into LLM ontologies.

-   There being a somewhat universal task similarity metric
    would be good news for an avenue of research that aims to compare
    the generalization ability of ML models to that of humans. Given
    such a metric, one could then perhaps compare \[the task similarity
    distance that humans can generalize across\] to \[the task
    similarity distance that GPT-k can generalize across\]. In fact,
    perhaps one could produce a scaling law in generalization distance,
    and use it to estimate the time to AGI along the default path.

# Acknowledgements

Thanks to Andis Draguns, Lawrence Atkins, and Jake Mendel for helpful
discussions, including contributing a couple methods; to Clem von
Stengel, Nina Rimsky, Rudolf Laine, and Arjun Panickssery for discussions and comments; to Robert Avery for discussions, comments, and edits; and potentially to people we've forgotten (feel free to message us).

[^1]: A possible objection here: wouldn't the ideal indirect object identification circuit be more like a full description of what a model does to do IOI; i.e., isn't the task dictionary/classifier part of this decomposition unnecessary? So, couldn't it be more like: there's a bunch of circuits for various tasks that are always running, except perhaps not having some nodes activate because of looking for something that does not exist in the input, or something, and then the final answer is some aggregation of the outputs of the circuits that do activate? Well, maybe it could be like that (or, at least, we won't get into an extended analysis whether it could be like that here), but as far as we can tell, the IOI paper is not significant evidence of that — the method used would not detect computations with outputs shared by everything on the dataset on which its mean ablations are computed; in particular, its method would not find a hypothetical task classifier (which could well be more complex than the circuit found) which always decides that the task is indeed IOI on the reference data set (this is also true for resampling ablations from the same data set). In any case, even if the correct hypothesis to entertain were that models are more like ensembles of unconditional circuits that always 'try to run', the present bullet point would still make sense, mutatis mutandis.

[^2]: It seems reasonable to operationalize generalization as applying
    understanding of a task (say, writing English poetry) to other
    subtasks (e.g. writing French poetry) of a certain natural
    "metatask" (writing poetry).

[^3]: We note that each method below could well turn out not to measure any reasonable kind of similarity. We also note that the methods would likely end up measuring distinct flavors of task similarity, but we do not provide an analysis of these flavors in this piece.

[^4]: We might similarly want to upweight contributions from middle layers in many scores below.

[^5]: We add the small amount of fine-tuning on $B$ at the end because
    we want the model to be able to make some amount of connections
    between what it has learned from $A$ and the new domain $B$.

[^6]: Note that this metric also works as a measure of decomposition —
    not just similarity.





## done todos

todo: discuss how universality is interesting (in caveat on subjectivity)

todo: add footnote on IOI confusion to motivation

todo: discuss how different methods give subtly different things, interestingly and understandably so (in caveats, perhaps new caveat)

# Methods for gauging task structure in ML

In this post, we first motivate why thinking about task decomposition and task
similarity might be important. Second, and more importantly, we give brief starting points for
several different metrics of task similarity (most of which correspond to
task decomposition methods) that one could use for LLMs. An example of work
using such a metric is [here](https://www.lesswrong.com/posts/qCecZwptWuAEZN3Td/transfer-learning-and-generalization-qua-capability-in). If you don't want the motivation, feel
very free to skip straight to the 'Methods for gauging task structure in ML' heading below.

Epistemic status: have thought about this stuff for a while, but mostly
in messy notes or conversations. This post was written very quickly and
may be disjointed.

## Motivation
-   It would be a real boon for alignment — interpretability in
    particular — if ML models (or transformer language models more
    specifically) could be understood as large 'task dictionaries'
    together with simple algorithms (circuits) for each task (think: [a circuit for indirect object identification](https://arxiv.org/pdf/2211.00593.pdf)). In this
    case, we could hope to understand a model by decomposing its domain
    into specific tasks, then reverse-engineering what circuit is
    implemented in the model for each task individually, and also
    reverse-engineering how the model computes this task decomposition.
    Perhaps things are like this! We happen to doubt they are very much like this,
    especially for those models or those parts of models that are
    important for understanding general intelligence and for aligning
    generally intelligent systems. Nevertheless, we hope the similarity
    metrics outlined in the post can (a) help figure out the extent to
    which this task-dictionary hypothesis about language models is
    right; and (b) conditional on that hypothesis being right to some
    significant degree, lead to methods for (automatically) determining
    the way a model sees its domain as being decomposed into tasks.

-   Separately, having a way to quantify the distance between tasks
    could lead to a way to measure the ability of a model to
    generalize.[^1] Other than being of object-level interest, this is
    helpful for evaluating and predicting capabilities. Indeed, the
    ability to generalize (which is intuitively related to the ability
    to learn quickly) is often cited as a key limitation of present ML
    models compared to humans. We think it'd be interesting to use
    \[task distances \[models are able to generalize across\]\] to
    measure generalization ability in models and humans, e.g., for
    forecasting when model generalization performance will beat human
    generalization performance (i.e., maybe, when we'll have AGI). One
    can also perhaps use such metrics to track model generalization in
    more fine-grained ways, e.g. comparing the input clusterings of
    different Pythia checkpoints to see when certain inputs first come
    to be seen as similar by the model, or comparing the subtask
    clusters of GPT-3 to those of GPT-4, potentially seeing certain clusters
    merge or split.

-   Finally, we find it scientifically interesting how
    a domain might be decomposed into tasks: it would be nice to better
    understand what makes two things similar in general. Automated ways to determine the
    similarity-structure of a domain would be helpful, and LLMs give us an easy starting
    point for this broader scientific aim.

## Important distinctions we don't track in this post

-   'Task decomposition simpliciter' vs 'a particular subject's task
    decomposition': We will sometimes talk about the task decomposition
    (of, e.g., natural language) without referring to a particular
    reference observer/agent; and sometimes about how some particular
    model or another (or a human) (implicitly) decomposes natural
    language into tasks. Here are some ways in which these are
    related: (1) each can provide a helpful guess for the other; (2)
    alternatively, one could argue that the former really only makes
    sense as a case of the latter with the observer left implicit
    (though we think there's more to the former than that); (3)
    uniformity across observers of the latter could help establish that
    the former is a sensible thing to consider. But we won't track this
    distinction.

-   Task similarity vs input(-output-pair) similarity vs decomposition:
    A way to measure the distance (from a model's point of view) between
    two inputs (or input-output pairs) can generally give rise to a way
    to partition inputs (or input-output pairs) into tasks: apply a
    clustering algorithm on the complete graph whose edges are labeled
    by these distances. However, some of the methods below make sense
    mostly just for measuring task-to-task similarity, not for measuring
    the similarity between two inputs. In this case, providing an
    associated decomposition algorithm appears nontrivial. While we
    believe this can be done in particular cases, we ignore it in this
    post. Also, given a way to measure the similarity between two
    inputs, one can measure the similarity between two tasks with the
    expectation of the similarity between a random input from the first
    and a random input from the second.

-   Absolute vs relative metrics vs clusterings: Most of the metrics
    provided below are not intended to output individually
    meaningful/interesting numbers; however, the numbers can become
    meaningful when compared to other outputs. For example, it's hardly
    meaningful to say that a pair of token prediction instances have
    cosine similarity $0.08$, but it could begin to be meaningful in a
    context where other cosine similarities are
    $-0.3,-0.002,0.001,0.003,0.15,0.9$. And even if cosine similarities
    are also somehow wrongly normalized — the ordering of cosine
    similarities is sometimes not that of the 'true similarities' —
    clusterings could still be meaningful.

-   Mathematical precision: We won't be mathematically careful (that
    said, we will try not to get anything 'wrong'). For example, we will
    not discuss which clustering algorithm is most appropriate in a
    particular context. To be clear: we consider it obviously valuable
    to be mathematically careful — it's just outside the scope for
    now.

## Methods for gauging task structure in ML

In this section, we provide a list of ways to measure task similarity.

### Inspecting activations

-   Activation distance: Let $S_A$ and $S_B$ be sets of activation
    vectors (perhaps from a middle layer) obtained by taking
    instantiations of task $A$ and $B$ respectively and passing them
    through the model. A similarity metric for the two tasks $A$ and $B$
    is, for instance,
    $$d(A,B)=\left\lVert \frac{\sum_{v \in S_A}v}{|S_A|}-\frac{\sum_{v \in S_B}v}{|S_B|}\right\rVert.$$

    (Instead of using the $L^2$ norm here, we could also use cosine
    similarity, or maybe run the data points through a SAE and
    compute the correlation between SAE coefficients, or use some other
    more principled norm (maybe [this](https://arxiv.org/pdf/2311.03658.pdf)?).)

To compare activations on particular inputs, replace the averages by the activation vectors on those particular inputs. Instead of comparing activations that live in a particular activation space, we could of course also compare the activations that e.g. a particular OV part outputs.

-   activation steering transfer: Take some pair of tasks $A$ and $B$. First, obtain some steering vector representing a meaningful disposition towards task $A$ (e.g. a disposition to play 'cooperate' in a prisoner's dilemma). Then, steer the model on task $B$ with the steering vector. Compare the resultant behavior on $B$ to baseline performance on $B$. So, the metric is, say, $$d(A,B)=D_{KL} \left( A \middle\| (A|B_s) \right).$$

-   Probe transfer: Take two tasks $A$ and $B$ in the context of both of which some intuitive concept makes sense. For example, task $A$ might be a set of English sentences labeled 'true' and 'false', and task $B$ might be a set of Spanish sentences similarly labeled. Then, train a logistic regression to predict from middle layer activations whether an English sentence is true or false. Then test how well that probe transfers to the Spanish sentences. Formally, $$d(A,B)=\text{probe-acc}(A)-\text{probe-acc}(B).$$ This is supposed to give a way to access whether a model sees the two tasks in terms of the same concepts. One could also do something similar with concept ablations — i.e., checking if they transfer (either in terms of changing behavior in a reasonable way, or in terms of making the same concept inaccessible (see [this](https://arxiv.org/pdf/2306.03819.pdf)) in the other context as well).

### Inspecting learning

-   Fine-tuning transfer: Take some pair of tasks $A$ and $B$. First
    fine-tune on task $A$, then briefly fine-tune on task $B$, and
    compare performance on task $B$ to the case where we fine-tune (for
    equally many steps) on $B$ throughout.[^2] So let's say
    $$d(A,B)=1-\frac{L(B|\emptyset)-L(B|A,B_s)}{L(B|\emptyset)-L(B|B,B_s)},$$
    where the conditional notation is meant to specify what the model
    has been fine-tuned on, with $B_s$ representing a small fine-tuning
    set of task $B$.

-   Few-shot prompting transfer: repeat the above point but with
    in-context learning. That is, few-shot prompt with examples of $B$
    vs examples of $A$ (maybe with a smaller number of $B$ at the end
    again), then ask it to do $B$. So, let's say,
    $$d(A,B)=1-\frac{\text{acc}(B|A)-\text{acc}(B|\emptyset)}{\text{acc}(B|B)-\text{acc}(B|\emptyset)}.$$[^3]

-   Pre-training transfer: repeat the above point but with more thorough
    training, perhaps seeing how much cutting $A$ from pretraining hurts
    performance on $B$, or how much cutting $A$ and $B$ hurts
    performance on $B$ more than just cutting $B$. So, let's say,
    $$d(A,B)=1-\frac{L(B|\neg B)-L(B|\neg \emptyset)}{L(B|\neg A,\neg B)-L(B|\neg \emptyset)}.$$
    Or, analogously to the fine-tuning transfer metric above, we could
    compare accuracy on $B$ \[when one trains solely on $A$ and
    fine-tunes on $B$\] to when one just trains on $B$ for equally many
    steps.

## Inspecting weights

Note that the first three metrics in this section would have fit equally
well under the above subsection on learning.

-   clustering gradients (from [here](https://arxiv.org/pdf/2303.13506.pdf)): take two tasks (or single
    input-output pairs) $A$ and $B$. Compute the gradients
    $\nabla L (A),\nabla L (B)$ on the two tasks. We could then let
    $$d(A,B)= 1-\frac{\angle \left(\nabla L (A),\nabla L(B)\right)}{\pi}.$$

    Alternatively, we could see how much a gradient update on one input
    affects the computation on another, perhaps measured in terms of the
    $L^2$ distance between activation vectors (or just the KL-divergence
    of the output distribution) on the other output before and after the
    update.

-   optimal grafting overlap (from [here](https://arxiv.org/pdf/2302.06600.pdf)): Fine-tune a model on some
    task $A$. Then go back to the original model, and carefully pick a
    tiny set of parameters to replace with parameters of the fine-tuned
    model, making the performance on the task as good as possible. One
    can then measure the distance between two tasks by how different
    their sets of grafting parameters are. Formally, letting the
    grafting index sets be $S_A,S_B$, we could let
    $d(A,B)=\frac{|S_A\setminus S_B|}{S_A}$.

-   weight ablation transfer/similarity: Take two tasks $A$ and $B$. For
    each model component (or weight in a more fine-grained sense, e.g.,
    the edge between two neurons), ablate it and measure the change in
    performance in $A$, as well as the change in performance on $B$.
    Storing these KL divergences (or, alternatively, absolute values of
    the changes in the loss) in two vectors $v_A,v_B$, the metric could
    then be, say,
    $$d(A,B)=1-\frac{v_A\cdot v_B}{\lVert v_A\rVert \lVert v_B\rVert }.$$

-   mixture of experts overlap: Take two inputs $A$ and $B$, and pass
    them through the model, and see if they go through the same expert.
    This is perhaps particularly interesting in switch transformers,
    where we can get a more fine-grained view of expert similarity
    (whether or not the two inputs go through the same expert isn't just
    a binary — one can examine whether the choices made in the many
    switch layers line up). Formally, in the switch transformer case, we
    can let the distance $d(A,B)$ be the fraction of switch layer
    choices that do not match.

## Analogues in humans

-   Many of the above metrics transfer — somewhat gracefully — to
    humans. For example, it is easy to imagine metaphorically
    fine-tuning a mathematician to be good at, say, physics. There would
    likely be a reasonably large transfer there, and the same would
    likely hold in an LLM trained on maths and fine-tuned on physics. It
    is intellectually interesting whether our intuitive, human task
    clusterings transfer into LLM ontologies.

-   There being a somewhat universal task similarity metric
    would be good news for an avenue of research that aims to compare
    the generalization ability of ML models to that of humans. Given
    such a metric, one could then perhaps compare \[the task similarity
    distance that humans can generalize across\] to \[the task
    similarity distance that GPT-k can generalize across\]. In fact,
    perhaps one could produce a scaling law in generalization distance,
    and use it to estimate the time to AGI along the default path.

## Acknowledgements

Thanks to Andis Draguns, Lawrence Atkins, and Jake Mendel for helpful
discussions, including contributing a couple methods; to Clem von
Stengel and Nina Rimsky for discussions and comments; to Robert Avery for discussions, comments, and edits; and potentially to people we've forgotten (feel free to message us).

[^1]: It seems reasonable to operationalize generalization as applying
    understanding of a task (say, writing English poetry) to other
    subtasks (e.g. writing French poetry) of a certain natural
    "metatask" (writing poetry).

[^2]: We add the small amount of fine-tuning on $B$ at the end because
    we want the model to be able to make some amount of connections
    between what it has learned from $A$ and the new domain $B$.

[^3]: Note that this metric also works as a measure of decomposition —
    not just similarity.
