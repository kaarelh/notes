
* Viktoria Krakovna's list of examples of specification gaming: https://docs.google.com/spreadsheets/d/e/2PACX-1vRPiprOaC3HsCf5Tuum8bRfzYUiKLRqJmbOoC-32JorNdfyTiRRsR7Ea5eWtvsWzuxo8bjOxCG84dAg/pubhtml
	* the reward model which is supposed to train a hand to grab a ball being fooled by a hand hovering in front of the ball is a cool example (wait was it just the reward model getting confused, or also the humans providing data for training the reward model? i think probably just the model?)
* reasoning models totally try to bullshit you all the time, eg giving fake mathematical proofs. i haven't read this post but it probably makes this point: https://www.lesswrong.com/posts/KgPkoopnmmaaGt3ka/o3-is-a-lying-liar

 
 i feel intuitively like there should be more examples of humans getting hacked (ie of really pathological behavior being found by training with reward/"verification" from a human)? if there indeed aren't many examples, here are some potential reasons why:
 * the training process and/or models might still be too dumb (compared to humans)
	 * for example, maybe sample complexity is bad enough that you can't really even train against direct labels/reward from a single human
* examples which are incorrectly accepted by humans might be hard for us to grok as pathological — they are pretty much precisely such by definition!
* hacking a human might just be quite hard, when the human is trying to keep up? maybe verification just is a lot easier than generation or something?

