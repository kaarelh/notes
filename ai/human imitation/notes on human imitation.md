
https://intelligence.org/files/AlignmentMachineLearning.pdf

sort of this, or one version of this https://ai-alignment.com/mimicry-maximization-and-meeting-halfway-c149dd23fc17

here's a problem/framing/approach in alignment that seems interesting to me:  
Plausibly, alignment is solved if we can upload Eliezer (or 100 researchers, or whatever) and run the upload(s) at 1000x speed. Now, maybe this "uploading" could look like training a model that behaves like Eliezer. This is an old idea (imitation learning, behavioral cloning, etc.) discussed e.g. in the second half of https://www.lesswrong.com/posts/S7csET9CgBtpi7sCh/challenges-to-christiano-s-capability-amplification-proposal, but let's slightly reframe this as model stealing/cloning (https://twitter.com/ESYudkowsky/status/1635577836525469697?s=20 ) Eliezer instead. Given this framing, it becomes quite natural to ask to what degree training on input-output pairs of a model creates a new model which is really a clone (in terms of its internals) of the previous one, as opposed to a model that predicts the outputs of the first model in a very different way (sth like thinking about the model from the outside and trying to predict it), and in particular as opposed to one that predicts the outputs during training through some possibly deceptive outer loop playing the training game. Either way, I guess what matters is that the trained model generalizes correctly on test data + out-of-distribution (or at least in a reasonable way — it's not really necessary it generalizes in the same way, e.g. comes up with the exact same research breakthrough). I like this direction because (1) it has some reasonable chance of reducing alignment to a relatively standard/technical ML problem of out-of-distribution generalization, (2) in fact, it seems like we can study many (most?) crucial aspects of this empirically now, and (3) if we can get a clone of Eliezer, we just need to oversee sth at ~[our level] of capabilities (this can include sth like fine-tuning / consulting Eliezer again at critical junctures)

here's a related nearly concrete math problem (might be well-known from like classical learning theory, or obvious? seems like the obvious OOD generalization problem to write down? not sure, haven't put much thought into this yet and in particular haven't done any literature review (beyond having taken some complexity theory classes)):
Take a random boolean circuit $C$; it implements some function $f\colon \{0,1\}^n\to \{0,1\}$. (We will probably need to pick the circuit to have some reasonably small size, like at most the size at which one starts to get all boolean functions.) Split the input space into train and test data (maybe even drawn from a different distribution to model the out-of-distribution case). Is it the case that with high probability (i.e. for most $C$), any circuit $C'$ with associated function $f'$ which agrees with $f$ on the train data will either also agree with $f$ on test data or be much larger? (Ideally, putting some complexity prior on circuits, almost all the probability mass conditional on seeing the input-output behavior on train data would be on $C$.)

(Of course, this is analogous to the above with the boolean circuit being the model being stolen, i.e. Eliezer.)


https://ftp.cs.ucla.edu/pub/stat_ser/pearl-1978-connection.pdf



(side remark: compressed sensing stuff, in particular https://arxiv.org/pdf/math/0410542.pdf , is a sort of very strong version of this for a particular (silly) model class, ie where input is a vector, and the model is just multiplication by another secret vector but known to be sparse. their thm exactly says that the secret vector can be recovered as the simplest one with the given input-output behavior with just a small num of data pts

i wonder if this can be made a special case of some more general thm for a much larger func class.)


