
# mess

so have prior on params. with any reasonable prior, almost all probability is on param settings with complexity basically 

actually let's assume we have a uniform prior on param settings for now. then most param settings have almost full complexity (namely, at least roughly log num param settings). look at those param settings, look at which function f produced. can specify param setting by specifying that function with K(f) bits, then saying "find all param settings which give that function", then specifying pointer into this set of size p(f) times num param settings, so have to waste log num param settings - log 1/p(f) bits here. so this needs to be at least log num param settings, so have K(f) > log(1/p(f)) mostly, so also 







if you include some degeneracy assumption of the form , then you can conclude that there are some simple functions getting much higher probability than any complicated function. However, afaict there is nothing in this story forcing low-complexity functions to get high prior, 


Now, if you add the further condition that certain functions $f$ have much higher probability than others, then the proposition 
