
* interpret activations first, then weights
* key question with SVD and NMF approaches (actually, does it apply to NMF?) is whether features should be orthogonal (even the compositional ones), which is quite poorly understood. Of course, orthogonal features should be easier to individually read off, but that's definitely not the only pressure to which the features are subject to during training! There are also, for instance, pressures to pack lots of features into a small space
  e.g. https://arxiv.org/abs/2303.02536
  This also applies to cases which are not exactly about decomposing activations, but e.g. https://www.lesswrong.com/posts/mkbGjzxD8d8XqKHzA/the-singular-value-decompositions-of-transformer-weight
* we suffer from a bad terminological situation with 'polysemanticity' and 'superposition'
  "If you stare at it for a while, you begin to get a sense of how MLPs differ systematically from the OV circuits. MLPs, while each representing a single coherent concept in each singular vector, generally appear much more polysemantic than the OV circuit heads" https://www.lesswrong.com/posts/mkbGjzxD8d8XqKHzA/the-singular-value-decompositions-of-transformer-weight#_MLP_in_interpretability
  
* 

