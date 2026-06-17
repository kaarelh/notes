
This framing might be from Yudkowsky, or from the 'twitter dog profile pic guy', or it might be independent, I'm not sure. The story is that pretrained LLMs are solving sudoku puzzles initially, are finding tokens that match a number of constraints specified in the context. (How are they doing this? Has anything interesting been said here?)

* maybe this can help make some sense of activation steering? https://arxiv.org/pdf/2308.10248 e.g. adding wedding embeddings adds a constraint that each next token should have something to do with embeddings

RLHF-ing or otherwise training it with a longer horizon where it gets to use its own generations in future generations later also makes it solve the puzzle of finding tokens that create constraints for the future which pin down the right answers in the future.