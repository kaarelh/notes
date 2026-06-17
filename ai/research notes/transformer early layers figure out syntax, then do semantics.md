
Not sure how to think of this for autoregressive models in syntax tree case though where stuff could depend on what comes later in weird ways. Maybe should look at bidirectional models first. The hypothesis is that syntax is figured out first, and then semantics is parsed along the syntax

evidence for this hypothesis:
1) later layers more semantically interpretable, https://www.lesswrong.com/posts/mkbGjzxD8d8XqKHzA/the-singular-value-decompositions-of-transformer-weight (though maybe this is just logit lens getting out of sync and would be fixed by tuned lens? I don't think they study this in the tuned lens appendix): ![[Pasted image 20230411154800.png]]
2) some evidence here: https://www.lesswrong.com/posts/qxvihKpFMuc4tvuf4/recall-and-regurgitation-in-gpt2
3) (also a priori reasons — this is the main paradigm in linguistics I think)

ways to check for this: 
1) see where can deduce syntax (maybe done in https://aletheap.github.io/posts/2020/07/looking-for-grammar/ )
2) try to deduce syntax from attention patterns in a layer in particular, maybe just in first layer, maybe things in a phrase attend to each other more  