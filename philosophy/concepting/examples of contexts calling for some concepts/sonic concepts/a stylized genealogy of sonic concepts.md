
i realized after getting halfway through this that maybe we should rewrite this starting from generic pressure recordings instead — ie, the recording are not necessarily musical pieces, but what one gets by just going around with a microphone recording stuff. a reason this might be better: one is then better-positioned to see the concepts which are useful/"present" only because of human activity, vs the concepts which would also be useful even just when looking at sound in the non-human world

# which kind of genealogy are we giving?
the following are all interesting questions one could be trying to answer:
* given a bunch of audio recordings obtained by having a guy walk around with a microphone, how/why might a mind listening to these recordings gain the various human sonic (including musical) concepts?
	* if we are to keep the data set of recordings reasonably-sized, we might want the guy to be spending a lot more time in concert halls or browsing music online than one might naively expect
	* one could ask for one or a few plausible stories of how the listener might gain each of our familiar sonic concepts, or one could ambitiously ask for some sort of total account of all the ways in which these sonic concepts could be gained
* how did humans end up with the sonic concepts we have?
	* answering this question would be pretty different than answering the first question. one difference: one would need to be paying more careful attention to actual history. an even more important difference: many of our sonic concepts are there in significant part because we created various sonic things — phonemes, spoken words, chords, verses, oratorios, violins, orchestras — and so we'd need to give an account of why these things were invented (which is potentially very different from seeing these things in recordings once they are already there)
* wait, what even is it to have a sonic concept?
* wait, how did we even end up with a capacity to have concepts?

# examples of sounds

* wind, rain, leaves rustling
* birdsong^[music from birdsong: https://youtu.be/cUD4ED5hezQ]
* frog sounds
* human speech
* human singing
* human tapping
* human instrumental music
* beatbox
* sounds made by human-made machinery (traffic, home appliances)
# examples of concepts

we could have a data set of recordings of musical pieces^[just like with some standard method described here: https://en.wikipedia.org/wiki/Digital_audio . i guess we could eg be using a membrane to measure pressure and recording those (quantized) measurements?]. what kinds of concepts are sorta there in those recordings? it would be neat to automatically get all of the following more "external" things:
* a partition of the pieces into genres. maybe even getting a sense that the pieces came about at different times, and getting a sense of their ordering? also, a partition by culture/country? maybe even getting a sense that there's a globe, with cultures corresponding to regions on it?
* a partition of the pieces by composer; also, a partition by performer. or given that two people can sometimes be playing together and sometimes not, maybe we want a property for each performer saying whether that performer was involved. we could also have a "had the same performer" relation, or maybe a fuzzy relation ( https://www.sciencedirect.com/topics/earth-and-planetary-sciences/fuzzy-relation ) (ie weighted (di)graph with weights in $[0,1]$) to account for performers sometimes being partly shared and partly different
* a partition by instrument, or a (fuzzy) property for each instrument capturing its involvement
* we would want to see the development of each performer — in particular, we'd want to see an ordering of their pieces
* different scales, different keys


# wait what are these concepts we are after

taking a break from listing "latents", i want to mention one thing that feels off here:
* it's not like you're really supposed to get these precise objects — you know, like it's pretty crazy to ask for a property for each musician being in each piece, or a linear ordering of all the pieces by release date. we can be more relaxed and ask for some probabilistic things instead — like, for a probability distribution over linear orderings, or a probabilistic relation for which of two pieces came first, or for a probability that each musician is in each piece — but that sorta still feels like asking for way too much, at least compared to the things which humans have. maybe it's more like: we could hope that a system develops a sense that there is a question to be asked about which of two pieces came first, or about whether two pieces involve the same instrument or different instruments, even if it doesn't have any answer? like, there should somehow be these questions, without there being any kind of answers? but the immediate paradigm wants to talk in terms of answers, not questions?
* but how do we make sense of these questions? we can probably make sense of questions in the presence of some larger context — like, if we already understand that the pieces are played by people on instruments (and so on), then we can perhaps make sense of the question "which instrument is playing this tune?". but i feel like we'd want to get the question also without having this broader context. how might that work?

to work through an example, let's try to think about what kind of thing our notion of pitch is
* we hear some sounds as pitched; this shows up in eg us being able to compare sounds in pitch (higher vs lower), in being able to then hum the same tone, etc..
* what kind of thing should we think of pitch as being? there are some corresponding things, eg the set of all possible sound-segments which we would think of as having that pitch, or like a partial function from sound segments to pitches, but it'd probably be a confusion to say that this is what pitch is? we could say this is a presentation of the concept of pitch in terms of its extension

one way to go about figuring out "the type signature of pitch":
* maybe one can guess "the structure of a data structure" from what kinds of queries it supports. this motivates the questions:
	* what kinds of questions would someone who has a notion of pitch (or tempo, or scales, or beats, or letters) be able to answer?
		* maybe: more specifically, what kinds of questions about pitch would they be able to answer?
	* more generally, what would such a person be able to do?
* one can be asking this in our broad human context, where eg having a notion of pitch might help one tell what the volume of the chamber of an ocarina is. or one can ask this in a more limited context, eg where one fundamentally only has a bunch of pressure time series data? maybe we would ask significantly less of a notion in the latter case? (otoh, the former might be easier to imagine by default)

here are some things a human would plausibly be able to do if they had a concept of pitch:
* recognize some sounds as pitched, and some sounds as not-really-pitched. sing a note with the same pitch back
* be able to tell if two pitches are the same (roughly)
* be able to tell which of two (pitched) sounds is higher-pithced and which is lower-pitched
* (roughly) split a monophonic piece of music (say, a playable audio file or a pressure time sequence) into intervals in which different pitches are played
* go from singing a note to singing a higher-pitched note
* classify intervals, sing intervals
* recognize some melodies; repeat melodies
	* repeat melodies from different starting pitches
* recognize chords; sing chords (arpeggion)
* maybe: write code that detects pitch ( https://en.wikipedia.org/wiki/Pitch_detection_algorithm )

# some more later remarks about what kinds of things these concepts might be

* re pitch: we think of a pressure time series as being a harmonic sequence — we try to find a harmonic sequence that sorta matches the given function, or more generally find a couple harmonic sequences which sum to the given function
* this seems quite general — maybe more generally, we often think of a situation as involving some things?
# examples of concepts (resumed)

a list of internal things as well:
* the notion of pitch/frequency? (like, taking the fourier transform of each small chunk, like https://en.wikipedia.org/wiki/Short-time_Fourier_transform , and doing sth with it?)
* notes (like, splitting a musical piece into const-frequency pieces of certain durations?)
* the tempo (like, recognizing that there's something special about some unit of time)
* bars (like, recognizing that there's something special about another unit of time)
* decomposing into instruments/voices (if many instruments/voices are involved). seeing two hands of piano player separately?
* seeing key changes inside pieces
* chords
* chord sequences

# examples of sonic concepts which are (mostly) not musical

* phonemes, words, phrases (?), sentences (?)


# thoughts on how these concepts could be gained

actually, we made concepts and made music with these concepts in mind, and that's a major reason why music has the structure(s) it does — it's not like we made all our music first and then looked at our music and discovered/invented our musical concepts. but we can still ask how one might gain these concepts if just given our music!

# toy case — just pitch and duration

suppose have songs consisting of pure notes with random pure pitches (ie with the fourier transform being a delta function) and durations. or maybe each song is just a pure note with some duration!

then how do we see it in terms of frequency and duration? like, what makes these the right variables? we could say that these are individually useful in other contexts — say, that a human uses duration for some stuff and pitch for some other stuff — but do we want to say that? maybe there are many reasons why this is a good decomposition?

# sonic concepts preceding pitch?

which sonic concepts might come before pitch? evolutionarily, surely there was some kind of hearing before having a sense of pitch
* from An Overview of the Evolutionary Biology of Hearing by Carl Gans (but imo supported by not-great argumentation): "... it seems most likely that the initial role ofhearing was prey detection. An example might be the kind of auditory detection seen in sharks which can be attracted by the sounds of struggle or similar irregular sequences."

more precisely, some sort of loudness measure might precede pitch, maybe? do humans have something nice here across different pitches? i guess i mean: does the human sense of loudness correspond to sth physically principled?. i think it looks pretty cursed:

![[Pasted image 20250503213112.png]]

maybe loudness could have been a sorta time-averaged sign-ignoring version of the pressure time sequence, but it doesn't seem to be that. i guess it maybe could be that if one looks at the displacement of something in the cochlea
* loudness probably could not have had any nice scale though (like we could have had nice ordinal loudness maaaybe, but probably not nice cardinal loudness like we sorta have cardinal pitch), because there's nothing making there be natural intervals i guess (for pitch, overtones create natural intervals)

which sounds can humans even hear?:

![[Pasted image 20250503213216.png]]

# how come/do humans think of sounds in terms of pitches?

## what low-level thing (in air pressure, i guess) even corresponds to our sensed pitch?

is the pitch a human hears more like the frequency (1/period) of the pressure sequence or more like the frequencies of the fourier components inside? (these can come apart, eg if you add sines at 800 hz and 1000 hz, then from the period, one should hear 200 hz; i tried with pure waves and i think i didn't hear 200 hz, ie just heard 800 hz and 1000 hz.) o3 claims it is a mess: https://chatgpt.com/share/6806a3aa-d7d0-800f-b121-4bb9cc794603

important to note: because of math stuff ( https://en.wikipedia.org/wiki/Fourier_series ), the fourier frequencies have to be multiples of 1/period. so a pressure sequence not being harmonic (ie having really irrational ratios of frequencies, i guess) is just the same as it not being periodic

the question here could then be: if periodic, when do you hear the 1/period pitch, vs when do its overtones make up one or multiple separate pitches one hears

deep research o3 attempting a literature review on fairly clean models of human pitch perception: https://chatgpt.com/share/6810684f-7618-800f-8b2f-90afff7fbb8b
* says there are both period-finding-based models (these use sth called autocorrelation; i guess this is just looking for the shortest period across which the values have high correlation or sth like that) and fourier-based models (these look at the fourier peaks and try to make sense of them as coming from some harmonic overtone series)

## how does a vibrating string turn into nicely vibrating air pressure at each point?

when a string vibrates, how come this causes a pressure wave that is nice? why doesn't the pressure wave end up being sorta messy, given that you have many sources doing different things?
* a model: at each point, you have many sine waves adding up, with different phases, but with the same frequency. oh yep just think geometrically about $A_1e^{i(\omega t+\varphi_1)}+A_2e^{i(\omega t+\varphi_2)}$. You have two rotating sticks being added to each other, at const angle to each other. of course this creates just another circular motion! So these different sine waves from different points on the string would indeed just add up to a sine wave! (Probably this relates to how light from a weird shape turns into a coherent front?)
* next question: is the amplitude also even, or are there places where you get cancellation and places where you get constructive interference? hmm i guess that the amplitude just isn't so even when you're close to the string (what would that even mean?), but when you are far from the string, all the waves look pretty much in sync — the string starts to look like a "point source". the precise calculation here might depend on the speed of sound and the frequency? like, if your note is 400 hz and sound goes at 330 m/s, then the wavelength is order 1 m. and then when you are much more than 1m away from the vibrating string, the distance from you to each point on the string is roughly compared to 1m (like, the diff will be much less than 1m), so you pretty much just get constructive interference, at least as long as the string itself is vibrating up and down coherently. if the string is doing sth else, then i guess it is less clear? well you should still at least have roughly the same wave at each point when you're far away still i guess. and maybe you just can have some destructive interference? 
* and i guess this story can mostly be told for each frequency separately. and then the vibrational modes of the string will just be the components you hear as well!
* and i guess maybe one can go further and say that even the shape of the vibrating string corresponds to the shape of the air pressure graph?
	* one could maybe say this is because: imagine the string over time making a 2d height plot. in this plot, x-slices and y-slices look the same!? (the wave equation is almost symmetric in x and t, https://en.wikipedia.org/wiki/Wave_equation . i guess maybe it becomes precisely symmetric if change coordinates to say $t=iu$? idk how to think well about this) and what one hears is sorta-kinda a slice in the time direction?
	* one could also just speak of the string being a sum of standing waves with some vibrational frequencies which are i'm pretty sure reciprocally related to their wavelengths along the string, but the wavelengths in air will also be such! so we are adding waves with the same wavelengths (up to rescaling) in each case! so that makes a whole bunch of sense of the shapes being similar i think

a bowed violin string in slow motion: https://www.youtube.com/watch?v=6JeyiM0YNo4
plucked(?) guitar strings, probably with some sorta-camera-artifacts in play, but still maybe interesting: https://www.youtube.com/watch?v=8YGQmV3NxMI
plucked(?) guitar string in slow motion: https://www.youtube.com/watch?v=4kWHBBVAVTY
hit string in slow motion: https://www.youtube.com/watch?v=9O3VEXzuOKI
## some air pressure graphs

from https://musicandcomputersbook.com/chapter1/01_01.php , a tiny segment from human speech:
![[Pasted image 20250421161044.png]]

3 utterings of the word "ramen" (two by the same person) from https://physics.stackexchange.com/a/240133 (wait is the number of waves in the word really that low? wow):
![[Pasted image 20250421163511.png]]

some wind instruments: https://demos.smu.ca/demos/waves/20-sound-waves

## how does a brain/ear do a fourier transform?

i'm not confident here but i think it's probably basically as follows:
* there is like a linear thing which has parts in sequence with increasing resonance frequencies. like, imagine a bunch of springs on a line, with spring constants increasing, so natural oscillation frequencies increasing. then if you have sound, it pushes all of these, but the ones that start vibrating with a high amplitude are those whose frequencies are present in the sound (this is some fact about driving having high energy transfer only when done close to the natural frequency of the oscillator). 
* ok so now you have certain springs vibrating — namely those whose natural frequencies are present in the sound. and each spring has like a nerve next to it, with the nerves which are next to high-amplitude springs getting activated. now you've sorta done sth like a fourier transform i guess!
## why do we hear pitch? why is it natural to hear pitch?

* some objects make sounds at particular pitches: strings, pipes/flutes, bottles/ocarinas; (well-tuned) bells and (well-tuned^[https://wtt.pauken.org/]) kettledrums^[https://www.youtube.com/watch?v=PRTxPJfCKhY], also, but those are harder to get to make nice sounds; sorta but not really: hanging any solid object up and hitting it (these have a discrete spectrum by sth like https://en.wikipedia.org/wiki/Dirichlet_eigenvalue i think — it's just that the overtones are usually "not harmonic"). in brief: it is natural to make pitched sounds
* maybe: it is fairly easy to make a device that measures pitch? or maybe a device that performs a fourier transform of a pressure time series? (such a device can look like what's described in the previous subsection. it would be interesting to see if the same design has been invented independently more times by evolution or humanity.)
* there is an obvious regularity in the pressure time sequence: it sorta looks like sth repeating a bunch of times. roughly, the sorta-period of this is the pitch. maybe we should see pitch as coming from this regularity, maybe from some associated sort of "prediction task".^[is there something that should be said in general about regularities typically having quantities attached? i guess this is false in general — eg an object staying together doesn't that naturally have a quantity attached?]
* pressure time series are sparse in the fourier basis i think! i haven't thought this through carefully but i think this has to do with https://en.wikipedia.org/wiki/Dirichlet_eigenvalue and https://en.wikipedia.org/wiki/Spectral_theorem#The_spectral_theorem_for_compact_self-adjoint_operators . and this should be the only basis in which the time series is sparse, right!?
	* wait no, not that sparse. or like, there are other countable bases which have some amplitude sequence, right, like polynomials (you can also make these orthonormal if you like) ( https://en.wikipedia.org/wiki/Orthonormal_basis ), so this doesn't make the fourier basis so special! i guess there could be some further nice fact about the amplitudes dropping off really quickly in the fourier basis, maybe, but is it really the best basis on that metric? (it might be!) anyway, i think we can see that it is more special because of translation invariance or sth. like coeffs sorta unchanged if you translate? this has to do with fourier basis elts being characters of [$\mathbb{R}$ with addition]
		* wait in fact the fourier basis decompositions we want to say are somehow natural are not even into a countable basis — or maybe we are changing the basis from signal to signal — if we want to say there is one basis element for each real-number-frequency
	* there could still be sth to sparsity alone? why do we use fourier for not just audio, but also for image and video compression lol (ok i think actually it is fourier with a silly boundary issue fixed: https://en.wikipedia.org/wiki/Discrete_cosine_transform for image and video. ok actually there is a major thing here: the image/video is blocked, with fourier being applied only to the blocks (which are like maybe 32 x 32 or even just 8 x 8 i think). for audio, there is blocking as well (but here o3 claims it is like 20 ms for speech and 200 ms for music which seem less crazily small to me), with some further trick to avoid some kind of popping at block boundaries where i think you do sth like applying a specific partition of unity and fouriering those parts: https://en.wikipedia.org/wiki/Modified_discrete_cosine_transform (why isn't popping also a problem for images? o3 claims it has to do with ears natively doing fourier and then all the oscillators getting bonked when there is a sharp pressure edge but the eye being more fine with small sharp edges or sth). anyway all this is a lot like using wavelets with small support roughly speaking)? among all the orthogonal bases which are easy to 
	* if the pressure time series data were gaussian with a covariance matrix that depends on distance alone (ie toeplitz covariance matrix), which is a sorta interesting model, then one should get fouriers as the eigenbasis of the covariance matrix (wait is this true?), so also as the PCA basis of generated data, making it in some sense the best basis to capture data variance (if you have to truncate). o3 says: "Stationary first-order Markov model → covariance is Toeplitz → eigenvectors ≈ cosines → DCT is near-optimal (Ahmed & Rao, 1975)"
* sth like: the fourier basis is the right basis for pressure time series prediction? is there an analogy with how hamiltonian eigenfunctions are the right basis for time evolution in QM? yea i think each component will have its own nice amplitude decay law! time evolution will look really nice, "non-interacting", in this basis. it might be the unique basis with this property (+ maybe sth else)? would be good to think this through carefully
* what fraction of what we want to explain is just "the human ear does not hear phase" (https://en.wikipedia.org/wiki/Ohm%27s_acoustic_law)? how good an explanation of this is that phase differences between components are not that stable? concretely, phase differences should change when you hear the same object being hit in a different medium, and even more importantly when you hear the same object from a different distance, i think because different frequencies travel through media with slightly different speeds usually. i think this is probably also true already at a vibrating object over time — like, for the vibrations in the object already. these things mean that phase information is basically fine to forget for recognizing/classifying objects via sound


## more notes on pitch

* according to chatgpt, there's an organ-thing called "the cochlea" that like has different parts vibrating more intensely depending on the frequency of the pitch, letting you activate different neurons depending on the pitch or whatever https://chatgpt.com/c/67eca692-147c-800f-82ed-2c5682b4b107
* this leaves open: why did we evolve the ability to think in terms of pitches? i guess maybe there's something to be said here about how it is easy to make sounds of specific pitches — like, just hit a thing (well, at least some particular things with particularly nice shapes or something, i guess? if we isolated a door and hit it really hard, would it make a note?), just vibrate a string, just blow air across the top of a bottle, etc. and then you want to be able to distinguish sounds with different sources, and pitch is a great feature to be able to track for that?
* the pitch we think in terms of isn't really the lowest played frequency? eg maybe if you pick a frequency $f$ and play $nf$ for all $n\geq 2$ but not $f$ itself, then one hears that pretty much as $f$? idk i sorta tried and didn't feel like that worked but maybe i messed up the amplitudes or whatever
	* yea wiki says this happens: The pitch of complex tones can be ambiguous, meaning that two or more different pitches can be perceived, depending upon the observer.[[4]](https://en.wikipedia.org/wiki/Pitch_\(music\)#cite_note-hartmann-4) When the actual [fundamental frequency](https://en.wikipedia.org/wiki/Fundamental_frequency "Fundamental frequency") can be precisely determined through physical measurement, it may differ from the perceived pitch because of [overtones](https://en.wikipedia.org/wiki/Overtones "Overtones"), also known as upper partials, [harmonic](https://en.wikipedia.org/wiki/Harmonic "Harmonic") or otherwise. A complex tone composed of two sine waves of 1000 and 1200 Hz may sometimes be heard as up to three pitches: two spectral pitches at 1000 and 1200 Hz, derived from the physical frequencies of the pure tones, and the [combination tone](https://en.wikipedia.org/wiki/Combination_tone "Combination tone") at 200 Hz, corresponding to the repetition rate of the waveform. In a situation like this, the percept at 200 Hz is commonly referred to as the [missing fundamental](https://en.wikipedia.org/wiki/Missing_fundamental "Missing fundamental"), which is often the [greatest common divisor](https://en.wikipedia.org/wiki/Greatest_common_divisor "Greatest common divisor") of the frequencies present.[[10]](https://en.wikipedia.org/wiki/Pitch_\(music\)#cite_note-10)
* ahh the point is that we hear the period right? when you do sine waves at $nf$ for all $n\geq 2$, then the period is still $1/f$ right? like, there is some crap shape which roughly has some period, and we hear the period? any sine wave stuff might be a further thing that's not needed for pitch at all!
	* yea https://en.wikipedia.org/wiki/Pitch_(music) : "In most cases, the pitch of complex sounds such as [speech](https://en.wikipedia.org/wiki/Speech_communication "Speech communication") and [musical notes](https://en.wikipedia.org/wiki/Musical_note "Musical note") corresponds very nearly to the repetition rate of periodic or nearly-periodic sounds, or to the [reciprocal](https://en.wikipedia.org/wiki/Multiplicative_inverse "Multiplicative inverse") of the time interval between repeating similar events in the sound waveform.[[7]](https://en.wikipedia.org/wiki/Pitch_\(music\)#cite_note-goldstein-7)[[8]](https://en.wikipedia.org/wiki/Pitch_\(music\)#cite_note-lyon-8)"
	* idk how happy we should be about this "in most cases". we should maybe still be open to there being a different way to describe it that is about as nice as this but generalizes even better (ie works in even more cases)
* ok and then i'd guess that if you hit an irregular object, it doesn't ring at any pitch because you just don't have anything meaningfully periodic? i guess that probably happens if the "vibrational modes" are not that discrete
# getting from some sort of primitive ability to tell pitch to a more refined thing

* why do we quotient by octave? this is probably very common (like, across cultures and even across species). i guess the overtone series overlap explains this? like, the higher notes has precisely half the overtones of the lower one. this is a max overlap situation right
* it makes sense that we get a notion of an octave-interval from this (note this is a bit separate from thinking of pitches which are an octave apart as the same). now we can think of all these technically different steps as the same type of step!
* why do we think of perfect fifths as being the same? since they are at 3/2 freq ratio, their overtone series have the next most overlap i think, in any reasonable metric for that (after octaves and multiples octaves, anyway). namely every second of the top one is in the bottom one, and every third of the bottom one is in the top one. it maybe makes sense then that we hear a fifth as clean, tho a little less clean than an octave!
	* wait no actually probably an octave plus a fifth (ie going 3x) should be cleaner? now we are sharing a third and all of the overtones respectively. i listened to it here https://www.onlinepianist.com/virtual-piano (it doesn't have just intonation ofc but that should only be a small diff) and it indeed plausibly sound cleaner? i'd like to listen to 5x also to compare 3/2 to 5x in clarity. but yknow 3/2 is up there in clarity in any case
	* anyway octave+fifth becomes a fifth if one is doing the quotienting of octaves already
	* a fifth is also the diff between the second and third harmonic i guess? is that somehow more the real reason we have fifths?
	* btw, birds seem to also "think of different perfect fifths as the same", because they sing the same melody from various different starting notes: https://www.hollistaylor.com/ewExternalFiles/Decoding%20the%20song%20of%20the%20pied%20butcherbird.pdf
* fourths are similar and a little less clean again
* these fifths and fourths could maybe also be somewhat downstream of timbre? like the clarity is maybe adjacent to timbre intuitively? and one could think of a fifth as just an overtone sequence of the tonic of the octave below with some fairly bizarre weights (in particular, with a missing fundamental pitch)
* conditioning on frequency, fifths and fourths are "much more nicely periodic" than some shitter ratios — like, they are periodic with much smaller periods. maybe there's some prediction machinery in the brain doing period-based prediction that gets low prediction error when you have fifths and forths, and that somehow underlies the sound being "clear"?
	* maybe we could say more precisely: the sound is most "clear" when a periodicity-detector's identified frequency is closest to some fourier-detector's identified "frequency"?
* one could also start seeing two pitch-jumps as being by the same interval from having two strings of the same length next to each other and pressing them down at the same point (just imagine a string instrument here)
* one sorta gets the western 12 notes ( https://en.wikipedia.org/wiki/12_equal_temperament ) by going up in fifths 12 times? $(3/2)^{12}\approx 129.7\approx 128=2^7$ is the point — you're sorta back to where you started (assuming we quotient octaves) after 12 steps up by a fifth
* ok but why are there only 7 notes in a scale lol? i guess you go in fifths for some time, quotienting by octave, and stop somewhere. you want to stop where the intervals are sorta nice — maybe there are two kinds only. this happens at 5 and 7, and also above but here maybe it becomes too dissonant with 2 semitones in a row somewhere. https://robertinventor.com/software/tunesmithy/help/hypermos.htm
	* btw it's kinda cool that there cannot be more than 3 gap sizes: https://en.wikipedia.org/wiki/Three-gap_theorem

# some sonic concepts "more advanced than" pitch


* scales: each song 


# general remarks
* good concepts tend to be good for many reasons, i think. like, there could be many genuinely different ways to discover the same good concept. eg, different pitches are "easy to hear", but also "easy to make" (though we could say these two things are both downstream of things liking to resonate at some particular frequencies when hit i guess?). probably related: https://www.lesswrong.com/posts/E9EevrzBcDMap6dbs/the-thingness-of-things
* it makes sense to just ask how humans came to have each notion, and to be very guided by that
* i think we shouldn't be afraid to say: this particular representation makes some things evident — like, you just pretty much see the damn periods in your pressure recording — and it is fine to then be interested in those things, even if a different representation might make other things evident, or if there might be other algorithmically simple-to-predict bits in there as well. like, without any starting representation at all, if we drop the time axis and just have a set of intensity readings with no structure, there just isn't much structure one could find! to see structure at all, one must start from some representation. this representation is unlikely to be the best representation, and will probably be reworked a bunch. but it's fine to start from it anyway, i think! there's a wish to do stuff without assuming anything at all, free of all preconceptions and privileged representations, but maybe this is just silly. anyway, the real thing is well-described as starting sense-making from some representation
* from First Language Acquisition: How do children form conceptual categories in the first place? They start out, it seems, with the ability to group things by how similar they are. These early groupings are also influenced by perceptual Gestalts that highlight “figures” against “grounds.” Anything that moves stands out against its back-ground and so is the figure. And when objects move, they move as a whole, so whole objects are more salient than any one part. Once children have represented an object-type, they can go on to attend to the actions and relations that link it to other things around it. These kinds of conceptual organization provide a starting point for what might also be represented in language.
	* a maybe good idea: objecthood from stuff moving together
	* i guess this maybe sorta requires seeing stuff moving in the first place? like you can get the notion of a car after you get the notion of a wheel and the notion of a window, only then being able to see the wheel and the window moving together?
	* but then how does the wheel come about? from its pieces? maybe from continuity and sharp boundaries?
	* it also seems important that there are many wheels! like you could recognize it as a thing even just seeing one wheel maybe, but 
* the human hearing system is a crazy mess. but i guess it is doing some nice thing? maybe this is a generally nice example to keep in mind, of evolution building a crazy thing that ultimately does something nice?
	* well, it's probably false that it ultimately entirely tracks something nice. it probably importantly does a bunch of things
	* okay so human hearing is plausibly doing a crazy messload of things, or at least we probably have little clue what it's up to and couldn't eg replace it with some nice designed thing at this point, but maybe some entire contrived system is doing something nice anyway here: maybe we could come close to replacing the human ear up to like the point where electrical signals are caused by the small vibrating hairs with just a fourier transform device? like, scrapping the ear and connecting that with those nerves? could we work with that just fine? maybe some stuff will be wrong, but we could cope — we could still hear just fine after an adjustment/fixing/learning period?

# miscellaneous

* why are high notes called "high"?
	* they aren't in some cultures (idk if they are flipped anywhere tho? that'd be cool)
	* maybe sth to do with high notes causing vibration in one's head and low notes causing vibration in one's chest??
	* https://www.reddit.com/r/musictheory/comments/y0dn3h/why_do_we_call_high_notes_high_and_low_notes_low/
* try listening to the different wave shapes here: https://www.szynalski.com/tone-generator/ . if you turn on the non-sine shapes, i think it feels like you start to hear sth like the sine wave after a few seconds of playing the sound — like, in addition to what you hear initially, with the thing you hear initially also not going away. i guess sth in your ear needs a little time to start sine-resonating, maybe? i don't really understand resonance that well atm
* how does an ocarina work even. ans maybe: https://linuxsquirrel.livejournal.com/45528.html . claims this is relevant: https://en.wikipedia.org/wiki/Helmholtz_resonance
* animations of air oscillating in a closed pipe: https://en.wikipedia.org/wiki/Acoustic_resonance#Closed_at_both_ends
* playing a string instrument with a bow, one has stick-slip motion. like the string keeps sticking on the bow then slipping. this keeps adding energy to the string. https://www.youtube.com/watch?v=KPpBvHXYWz4
	* apparently this is also what causes the squeak of a basketball shoe on the floor, https://en.wikipedia.org/wiki/Stick%E2%80%93slip_phenomenon
* (some) birds probably also kinda quotient octaves: https://www.reddit.com/r/askscience/comments/u5nd7n/comment/i544jjr/?utm_source=share&utm_medium=web3x&utm_name=web3xcss&utm_term=1&utm_content=share_button
* it'd be cool to just literally try to make sense of bird recordings — to try to discover the "concepts" that birds think of their songs in terms of.
	* this is supposed to be analogous to what we are mainly envisaging doing to human music recordings here. well, it is ofc unclear to what extent birds can think (in terms of concepts), but i think we can meaningfully ask sth like this anyway?
	* https://pmc.ncbi.nlm.nih.gov/articles/PMC5884127/
* one thing maybe making sonic concepts interesting/good to look at: all the things will be living in a world with 0 space dimensions and 1 time dimension? thinking of time as being laid out, a pressure time sequence is a 1-dimensional picture
	* fun: we decompose the signal into various components — eg imagine being able to hear the individual instruments in an orchestra. ignoring for simplicity that we have more than one ear, this would be impossible for even two "instruments" if their contributions could be generic pressure time sequences. but instead they are nice in the fourier basis, and we can do this decomposition. now note that in pitch, each instrument can be doing an arbitrary thing. but this seems to say that we got two arbitrary functions $f_1,f_2\colon \mathbb{R}\to\mathbb{R}$ from just one function after all — kinda cool. naive ways to say this is exciting might fail, but i'm guessing there is something good to say here. i'm also guessing it is important that we lost the ability to change pitch super quickly here (we lost this ability because changing pitch significantly in a single period would destroy hearing the parts as pitched at all i think). it's kind of like going from one arbitrary sequence in  $\approx$continuous time to two arbitrary sequences in $\approx$discrete time 
* so: [what might a 1d painting look like? it could look like a musical piece!]
* only rhythm (and maybe some sort of resonant frequency distribution determining data, and then eventually just a buzz or no sound at all maybe?) left when playing and recording the same sound over and over again: https://www.youtube.com/watch?v=fAxHlLK3Oyk




# potential references

Gestalt psychology: https://en.wikipedia.org/wiki/Gestalt_psychology

Auditory scene analysis: https://en.wikipedia.org/wiki/Auditory_scene_analysis

META-HODOS: https://monoskop.org/images/1/13/Tenney_James_Meta-Hodos_and_Meta_Meta-Hodos.pdf