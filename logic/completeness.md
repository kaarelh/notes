godel's completeness thm. phi provable <=> phi true in all models

provable => true in all models is easy, because inference rules are such that they only let you get true things out from true things

now true in all models => provable

equivalent to not provable => false in some model
phi not provable <=> adjoining neg phi still gives a consistent set, so it's equivalent to show that:
consistent <=> has model

has model => consistent is easy again, because inference rules only take trues to true in that model, so can't get a falsehood

consistent => has model is the hard part

trusting chatgpt a little, the trick seems to be:
1) make a new const symbol for each existential statement