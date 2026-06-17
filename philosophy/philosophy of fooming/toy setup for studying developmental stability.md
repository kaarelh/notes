it would be interesting to understand if stability is in conflict with being able to develop a lot or with being able to get a great deal done
related: can we specify some precise statement that says you can't have both development/freedom and be cancer-free? is there such a true theorem?

we can say there is a self-modifying program. ok even simpler: we could say it is a program that runs for some time and then outputs a next program to run. we could say that there is some property which we want to have preserved. i guess it could be a property of the program? we could think of this as analogous to keeping some promise, eg to be nice to humans. we could then enforce that it be preserved by just requiring the next program to provably have this property each time. the question then is: is this extremely restrictive on which programs you can output? like: does this completely mess up development?

maybe we should pick some hard thing for the program to be doing while preserving the property as well, asking how much it has to lose on the hard thing to provably preserve the property? how about finding large primes? maybe you at each point care about the discounted sum of future outputs, with discounts decaying rapidly enough that it converges. actually maybe just do the next two outputs? or maybe: instead of primes, writing code of a TM that runs a really long time and then haltsfor a long time. equivalently, just specifying a large number

maybe it's very simplest to just say we want to generate a string which is high on some score and has some property, and then we want to know how much the property restricts the score. of course this will depend a lot on what score and property we pick! idk if something interesting can be said in general

we should have some sort of developmental objective that requires a lot of reconfiguring... can we write down some mathematical thing that is that hard? like where you need to keep putting in genuinely more effort to get more of the objective. and then what sort of property should we have? like it should be hard, but not unfairly hard?

what is wrong with solutions that have some sort of meta system ensuring the property is preserved, like just adding a thing on top that rolls things back each time it looks like the property wasn't preserved? one issue is that it can be really cursed to check if the property was preserved. one issue is that in practice it needs to be done by the system itself thoughtfully, for the properties we really care about, maybe? one weird thing is that in practice it seems like you can have the meta thing be subverted by stuff inside, but i guess we can make a program such that this cannot happen pretty easily. but maybe one could just do this in practice as well? like, couldn't one upload the entire world onto a computer which does some basic resource acquisition and self-repair? and then install whatever control loop on top of the world that one likes

components of a developing system:
* a mind doing stuff, made of technological components which are added and changed over time
* another mind, maybe the first or a version of it, judging the changes
can we set these up st things are stable?

is there some fundamental scale threshold after which a mind can proceed stably? if yes, this could be an interesting “fundamental metaphysical constant”

maybe we should define some sorts of degrees into which histories/processes can be classified:
* you can have stability if you don’t have to develop at all. eg launching dumb probes which use sunlight to turn certain kinds of matter on certain kinds of planets into diamond
* you might be able to get pretty good stability if you develop but only by filling in content into a certain kind of fixed rigid system? you might be able to do some more stuff this way. eg now you can do probes with some more advanced decision-making maybe