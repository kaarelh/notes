
seems good source:
http://karpathy.github.io/2015/05/21/rnn-effectiveness/

pretty much just vec pairing operation i guess and embed and unembed, how vec pairing used for inference can depend somewhat on task, but general idea is that there is a hidden state which is passed to next position in sequence, paired with token embedding vec at that position to create new hidden state. pretty straightforward to do next token prediction this way. i guess could also have multiple hiddens per token if one wanted to do more computation instead?

trained with backprop as usual. i guess it becomes a bit messy if it is not clear how many sequential steps one ought to do during inference — what precisely is the model then on which to backprop? but seems pretty simple to solve. i guess one could maybe even define some geometric series and work it out semi-analytically? but easier just unwind some finite num of steps and do regular backprop then. maybe still some issue with vanishing/exploding gradients though? one could also treat all those as separate parameters and update according to average update (maybe rescaled) given to params? idk if this is mathematically the same (under certain randomness assumptions?)

LSTM is a variant of these with a slightly different pairing operation? says andrej? hmm i'd guess maybe not pairing actually? won't investigate now tho