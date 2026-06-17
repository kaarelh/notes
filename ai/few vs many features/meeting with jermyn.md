
A common claim: after the embedding, there are 50000 tokens in superposition in the 768-dimensional residual stream; in fact, the sparse representation only ever has one feature being active. However, isn't it simultaneously also the case that the embedding space probably has some useful linear structure, just like any other word embedding? For instance, is stuff like king-man+woman=queen not true in token space? How do you think about 


\item Train a model with $n$ neurons at layer $l$. Then retrain the network, holding all weights fixed except $W_{l-1,l}$ and $W_{l,l+1}$ which are re-initialised. Do small $k$ techniques like SVD find the same features both times (as measured by cosine similarity of features sorted by the canonical ordering of each singular vector set)? What about large $k$ techniques like sparse autoencoding?

\item Repeat the first experiment, but use $D>d$ neurons at layer $l$ when retraining.
Now we want the decomposition in the narrower layer to be the same as the decomposition into the top $k$ features in the wide layer (in generalm we expect that the number of features learned in the wide model is likely to be larger than in the narrow model). Does this work better when our decomposition is with a small $k$ technique or a large $k$ technique?

 \item Repeat the first experiment, but in retraining, reinitialise the weights between more layers. Now we don't expect features to be represented in the same directions as before, but insofar as the \textit{Universality Hypothesis} (\cite{li2016convergent, olah2020zoom}) is true, the same features are likely to be represented in some way or other. Using the technique that worked best in the first experiment, can we identify features we find in the two models with each other?

\item Train pairs of (model with ReLU at layer $l$, model with ReLU and a filter which sets to zero all but the top $m$ activations at layer $l$) for a range of values of $d$. If the top-$m$ filter forces features to be aligned to the neuron basis, then the models should only have similar performance when the number of features $k \leq d$. 

\item We'd like to improve our confidence that sparse autoencoders have found the real features. If we train the sparse autoencoder twice, do we get the same decomposition of activation vectors? If we fix some weights on the sparse autencoder to hardcode some random features into the model, but we learn their biases, does the model choose to ignore them from its feature set by setting their bias really low so the neurons never activate? 

\item Is there something correct in both the large-$k$ and small-$k$ pictures? For instance, instead of doing SVD and also instead of using a sparse autoencoder for feature decomposition, train an autoencoder in which some number $\delta<d$ of neurons have no $L^1$ penalty, and the rest do. The thought is that these $\delta$ features might pick out the top $\delta$ compositional directions, and the rest will be used for capturing the features in superposition. Will we find that the features are more interpretable this way than in either the dense or sparse extreme?


sparse autoencoder, dictionary learning more generally probably right; things which are in superposition might be in same direction, this can cause issues, things uncorrelated in superposition, gradient of L^1 penalties that goes from L^1; how do you know when the right answer is found 

criterion which says that you have found the right answer 

look at wes gurnee paper appendix

see if basic super 
