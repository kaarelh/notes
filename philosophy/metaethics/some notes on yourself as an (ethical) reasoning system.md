
# a syntax that can sorta talk about meaning in that syntax itself?

humans kinda seem to do this, right; what does this look like? is such meaning-talk dependent on having a notion of self? hmm. what's a first-order syntax that can do this?

# what kinds of self-knowledge or self-understanding are possible?

an attempt at a more concrete question: we can see the first-order theory of ZFC as talking about provability in itself — but do we get some contradiction if we 'have the system itself recognize that it's talking about provability in itself'. For instance, we could maybe add some more axioms? Which axioms would we add?

a more concrete case: imagine 'making a human into a turing machine that knows itself': tell a human that you'll put them to sleep, take a scan of their brain, then make their only input-output-channels communicating with a big tape (like a TM, maybe make it infinite if it matters); on this tape at initialization, you put the source code of this human (which you obtained by scanning the brain); perhaps you also add a second tape on which you record the history of queries after that. You could also dynamically give new brain states I guess — i.e., have a thing you can query for the state of the brain at any given past time step (assuming it's presented as a nice computational structure in which this makes sense)? This should make them into a Turing machine that fully knows itself, right? Of course, you can't read everything and remember it or sth, but you can certainly analyze yourself a lot. Can we think through some Gödelian stuff here?

one issue here is that we'd want the human to also be sort of like a first-order language proof-search type thing for gödelian stuff to very directly work out, but how would we do this? even if the human were this, to get this from the brain state, would the human need to solve interp? this seems tricky