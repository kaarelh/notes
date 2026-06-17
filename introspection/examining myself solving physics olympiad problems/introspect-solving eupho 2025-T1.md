
from https://eupho.ee/wp-content/uploads/2025/06/EuPhO_2025_Theory_ENG.pdf :
![[Pasted image 20250902173259.png]]

# thinking about the problem

* ok i'm going to start reading the problem
* seeing the picture, i have a vague sense that it's going to be asking me to look at the picture and figure out some stuff 
* ok i understand there's a cylinder which is perfectly reflecting, with light falling on it from some sides. i guess maybe we can see which sides from the picture? like, it looks like light is coming from the left mostly? from the bright spot next to the leg, and the shadow inside that spot?
* hmm illuminance surplus... i guess it's the delta of illuminance compared to the ambient illuminance? i wonder if we should take ambient illuminance as const? anyway it should be the extra coming from the leg reflection surely
* i wonder if the leg is like a mirror or if it reflects diffusely... if it were diffuse then wouldn't we expect to not see these radial-ish lines inside the illuminance pattern
* ok so it's asking for illuminance surplus inside the circle as a function of radius and angle. i wonder how much we're supposed to measure stuff from the picture vs calculate it fairly theoretically? i guess it's hard to measure 
* wait what's illuminance again... oh it says in the text that it is amount of incoming light per area... wait is it light incoming onto the floor or into your eye from the floor? i guess it probably doesn't matter? assuming the floor radiates diffusely or something? anyway i think we should go with light hitting the floor. wait what is "amount of light"? oh i guess here it doesn't matter because we don't have some weird different behavior of different wavelengths. like we can just count photons or count power or whatever — it'll all be the same
	* hmm i guess the picture does have the directions toward the camera looking a bit brighter. so maybe there is a real diff between light falling onto the floor vs hitting your eye... i think we should go with the light hitting the floor — the light hitting your eye will be much more cursed so they're probably not asking for that
* do we know the shape is really a circle? i guess the problem says that? but is it like basically precise or very rough? im guessing it's basically precise... that'd be physically sensible i guess. this seems fairly sensible looking at the next picture?
* ok so do we say the sun is infinitely far away? do we say it is a point? seems sensible? 
* ok so ambient illuminance is definitely not const if we look at eg the shadow and the patch of light around it and the rest of the floor. i'm pretty sure we should do a fairly theoretical thing, not look much at the picture.
* prolly the illuminance at B is eps compared to the illuminance at A. i think light does that sorta thing — things looking lighter are like this are really much lighter. this also makes sense in a reflection model... i think ill just go with that tentatively
* there's defo no modeling the cursed hair inside... maybe we just learn from it that the leg is really reflecting not diffuse. can also learn that from the central shadow i guess!
* ok so let's just make a theoretical model with a point source radiating at a cylinder like this. do we need to know the angle? i guess the angle should be not so bad to find... we can look at the central circle maybe? along the horizontal, on the left we have circle start determined by lowest bounce, on the right we see that same thing passing by the chair leg... hmm but isn't it always a 2x diff in distance? for a thin leg at least... so maybe shouldn't look at that. 
* can we tell what the angle of incidence is from the angle between the two chair parts which should be at 90 degrees in 3d? do we know they are at 90 degrees? ehh maybe it's close enough? especially fine given the prob text...
* hmmm also we can look at the length of the shadow vs the length of the reflection! oh wait no these should always be approx equal lol. nvm
* ok back to the angle between the chair parts. it's annoying that we don't know the angle of the chair. or we can see it from the pic but it's annoying to understand... 
* hmm ok so if we had the cylinder alone then could we tell at all? maybe not? we could maybe tell from the delta in length between the leg and the circle? but we can't see the whole leg... hmm can we see what part of the leg is illuminated?? maybe? but it seems weirdly incompatible with where the bright spot starts? like it feels like the bright spot should start lower... we can see a line of lower illumination on the leg... i guess the window is tilted there and this causes a faster drop... cursed! we could try to take that into account given that we see the angle from the bright spot but it seems involved... there should be sth simpler. wait do we even need the damn thing? 
* ok maybe it is independent of the angle...
* ok well we can count widths of the chair leg... for different angles, would have different multiples of the width 
* ok no it shouldn't matter i guess... for each angle of light there is some height of shadow start which gives one that picture...
* just say all the leg is illuminated. apply correction for center ring later. just say const angle const illumination from the left along the entire leg. how bright it is can be detected from the right direct hit surface. ok so is it true that small vertical cylinder segment becomes small vertical circle segment? hmm have const angle light incident... yea parallels escape in parallel in new direction! what is the new spread? if segment is at theta and width is d theta, then note that reflection flips comp 
* i guess maybe the key point with this business about not needing to know the angle is that a reflection against a vertical plane isn't going to change the horizontal intensity 
* ok so theta angle means for theta > 90, incidence is at 180-theta (from normal vec), so goes out at 180-theta to other side of the vec at theta, so final angle should be theta - (180-theta) = 2 theta - 180. oh we are using the fact that can split into vertical component and component in horizontal plane. this is what happens to the horizontal plane component. vertical component of velocity just stays const. yea the point is that the two components along plane stay const, whereas the comp into the plane gets flipped. if we observe projected to horizontal plane, then adding vertical velocity makes no difference. so even in the angled case we get this strip at theta becoming a strip at 2 theta - 180
* btw this means illuminance inside a strip goes down as 1/r. how does it total light into strip depend on theta again? well the total light falling into chair strip will be 0 except for theta between 90 and 270. for those theta, the strip total area in the right direction is prop to sin theta-90. so goes from 0 to 0. checks out. so the function is C sin(theta-90)/r. oh wait this is what goes into the strip at 2theta-180 = phi. so here actually have C sin(phi/2)/r
* but what is C? well, the total photon count has to be the total count hitting the floor. letting that be Q, we get int C sin (phi/2)/r dr r dphi = Q, so get CR int sin beta 2 d beta = CR 4, so C = Q/(4R). so illuminance is Q/4R sin(phi/2)/r
* question: wait is the ratio of intensities between bright and rest indep of angle? let alpha be angle from vertical. then the total falling onto chair leg scales with sin alpha. the radius of the circle also scales with sin alpha. so Q/4R is indep of alpha. illuminance of each spot will be the same C sin (phi/2)/r regardless. we can measure at what frac along the way B is. so then illuminance at B is like C sin(phi/2)/0.7 R let's say. the illuminance of the spot is going to be prop to cos alpha. like I_0 cos alpha, whereas Q = 
* ok maybe the thing about the light on the right and the reflection on the left starting at the same place isn't quite right, because the leg has thickness. like, we have reflection happen to the left of the center by a, but then it keeps falling from there to the other side, traveling horizontally by an extra a. ill want to draw this... (general note: it might be better to do this exercise on an ipad. want to allow drawing. haven't been drawing so far!)
* ok i was confused since getting this alpha seems really horrible and looked at the official soln a bit. it seems like it is not necessary. so let's try to think this through one more time. 
* so the light is from angle alpha. if you had an actual mirror then brightness of reflected would be the same as brightness of direct, hmm...
* hmm so radius R scales with tan alpha actually i think. and Q scales with sin alpha. so Q/4R sin(phi/2)/r has Q/4R scaling as sin/tan = cos alpha. oops it is indeed the same lol! ok put I in there. get Q = I 2a sin alpha L and R = tan alpha L, so cancels to 2 I a cos alpha/4 = I a cos alpha/2. floor gets cos alpha I. so letting that be I_0 now, we get that Q/4R = a I_0/2, so we get illuminance a I_0/2 sin(theta/2)/r. ok yay this is the correct ans! fucking small error!! could have maybe avoided it with careful thinking. was right earlier that angle doesn't matter!

part b:
* ooh we have some shadows that are lines in a plane but that don't turn into circles hmmm
* we are looking at the inside of the ring created by the middle finger. hmm
* the inside comes from the ray that passes to the left of that finger
* unfortunately the finger looks significantly tilted 
* ok i peeked at the solution and it seems to assume that's not the case. nice i guess. sad if you're at the competition?
* what kind of strip of the leg should we say is covered... well the shadow of a horizontal cylinder... what are the extremal rays like... well they fall along a plane! what does it look like if you have this plane cut into the cylinder... well it looks like a slice lol, at some angle obviously. so imagine a slice thru. what do these points reflect to? well we saw earlier that angle theta becomes angle 2 theta - 180. what's the radius there? ok so if the plane has angle alpha then the height of reflection is like h_0 - ... ok want paper
* finished soln in notebook. idk just understand geometry then calculate. some tricks involved in doing the calculation nicely. need to understand what's small ykno


# thoughts on what was happening when i was solving this

some themes:
* asking a question to make better sense of the situation, and answering it
	* it's like i'm improving a model of the situation by figuring out some stuff. eg:
		* is the rod reflecting like a mirror or like an uneven surface?
			* one can look at some stuff and the problem text and conclude it's more like a mirror
		* what does "illuminance surplus" mean? what's the precise comparison? in what model does that concept make sense?
			* ok we think of there being light coming from the rod and other light. the light coming from the rod is what we're quantifying
		* wait what does "illuminance" even mean again? is it like power, or like a photon count thing?
			* a lot of these choices are equivalent for our purposes, so basically it doesn't matter
		* which direction is the light incident from?
			* well we know it's on the left, because we can see the shadow of the rod
			* the angle from horizontal turns out not to matter for the answer. i suspected this but then i messed up a calculation and spent a while thinking that it does matter, and trying to figure out a way to find it
		* is the finger horizontal?
* i guess we could see a lot of what happened as asserting propositions. some questions in this frame:
	* what did i do to establish a proposition? like, how did i go from holding a proposition as a hypothesis to asserting it? i guess that a lot of the time i didn't have the proposition as a hypothesis before having a justification for it — i just reached it from some reasoning. eg the meaning of the illuminance surplus not mattering. but sometimes i did hold it as a hypothesis/question, eg the incidence angle not mattering. maybe i almost universally got propositions as answers to some questions which i did have before, though? like, the question needn't be a binary, it could be eg "why am i seeing these lines?" or "what's the difference between the distance of the reflection on the left and the distance of the bright spot on the right?"
	* where did the questions themselves come from? hmm let's see... i guess a lot of the time it just feels like i'm asking to understand better? but what criterion am i following there? what is this "understanding better"? how do i identify places where i'm confused?
	* maybe i'm like trying to have a clear sense of things and tracking where i don't... like which aspects that seem important i'm still unsure about... with criteria on this model ultimately somehow determined by what i'm trying to do... is this just a restatement?  
	* hypothesis: when we are asking a friend to clarify some background variable of a story they are telling us, and when we are asking a research question in mathematics, we are guided by a sense of what good questions are in a very similar manner
		* maybe it's good to study what makes a mathematical question good to make progress here. a reason this would be good is that math is fairly legible
* when calculating some quantities, i guess i'm tracking which quantities are already given and which are not given (maybe in terms of some variable), and then constantly trying to expand the set of variables which are known in a good direction?

# mess

C sin(90-theta)/r = Q, where we int from 90 to 270, ie sin(phi/2)/r int from 180 to 0 in sin, integrating that first gives - cos phi from 180 to 0 which gives 2. so get int 2/r. oh wait this was density and we have an area term of d theta r dr. so the r/r cancels actually and just get int 2 from 0 to R, so just 2R is the ans. so C 2 R = Q, so C = Q/2R
* 