
https://www.lesswrong.com/posts/mkbGjzxD8d8XqKHzA/the-singular-value-decompositions-of-transformer-weight

When one does SVD to a lot of weight matrices in transformers, the singular vectors that correspond to writing to the residual stream, and probably also those that correspond to reading from the residual stream (in practice this is equivalent to just dimensions matching, since there aren't conspiracies making other dims match), often appear to capture human-understandable semantic properties under the logit lens. I.e. just unembed and take the logits. (One potential issue though: maybe it is just a property of the embedding matrix that a lot of directions are quite interpretable, so it is quite unsurprising for singular vectors to look interpretable (though still, it would be helpful for getting a sense of what each head is doing)? The embedding matrix is learned, after all. See https://www.lesswrong.com/posts/BMghmAxYxeSdAteDc/an-exploration-of-gpt-2-s-embedding-weights for more on the embedding. edit: Ok this comparison seems to be made in Appendix E of https://arxiv.org/pdf/2303.08112.pdf, though I think it's plausible that they are not doing it sensibly.)
![[Pasted image 20230411154457.png]]

Also, tuned lens appendix E claims that directions from this post are not much better than random, but I think they are unfortunately quite confused


