
various proxies somewhat aligned: money with value-generated-for-others, h-index or lesswrong karma or tenure with value-of-research, supervisor's opinion with becoming good

(i guess at the end of the day, it's all just goodness-to-others, but i guess it's fine to think of there being examples where that routes to some intermediate proxy)

how do you avoid goodharting? of course, one option is to just try to track the underlying, not the heuristic

but what if you're adversarial instead? when is it still fine? can we prove that it's fine iff u are dumber than the heuristic-computer? is it true? is there a verifier's advantage somehow?

formal setup. principal is computing worlds -> heuristic, trying to make heuristic \approx value. you (in the adversarial case) are trying to find worlds with high heuristic. can we come up with a setup where we just give you two different amounts of compute and prove something? does the supervisor have a verifier's advantage at all here?

also, you might want to track the underlying, but just recognize that you're really confused about the underlying — maybe you trust the supervisor to track it better than you do. then is it reasonable to optimize for the supervisor's opinion? it seems like there are still obviously bad ways to do that (imagine giving your supervisor a drug that makes them think u are great) — you should certainly still keep in mind that you are trying to get at the underlying via the supervisor, not trying to make the supervisor happy. i guess this is just the usual CIRL idea? there's a secret value that the supervisor has access to, but can ofc be wrong in non-i.i.d. ways. want to extract the underlying pattern, and not get the noise. paper by stuart armstrong on decomposing as values + rationality is roughly this? anyway, it seems reasonable to use the supervisor as a query machine if you try to make them be iid? is there a way to make sense of this if you don't already contain a 'kernel of the underlying' yourself? surely there is just good practical advice for how to use someone for info about an underlying without goodharting? maybe this can be formalized?