![[Pasted image 20250919084848.png]]

# thinking about the problem
* hmm it's a number theory problem
* $f\colon \mathbb{N}\to\mathbb{N}$, denoting positive integers
* some kind of functional equation. $f(a)$ divides $b^a - f(b)^{f(a)}$ for all a,b
* vaguely reminds me of the term "lifting the exponent" but i don't remember what the lemma actually is lol. maybe i could figure it out if needed? hmm actually maybe more like fermat's little thm. that says that a^{p-1}=1 mod p for a not dividing p. 
* the problem: to determine the smallest const such that $f(n)\leq cn$ is forced for any such function
* hmm so what can we construct here. let's just try functions of the form f(n) = cn. seems like a good way to get familiarity with the problem. of course c must be a natural number in such a function. hmm then $f(b)^{f(a)}=(cb)^{ca}$. so clearly c=1 is an example. in general, we get $b^a-(cb)^{ca}=b^a(1-c^{ca}b^{(c-1)a})$, which ca is not going to divide for c>1 because c is not going to divide the thing in parens and also not b^a for some b. so the only function of this form is f(a)=a
* what sort of constraint is it? could we start tiling making sure the constraint is satisfied? well intuitively there being a constraint for each pair makes it kinda hard... 
* are there other constructions? i guess f(n)=1 works.
* maybe fix a and study the thing for all b. then we have some number f(a), and a bunch of multiples of it. always
	* eg a=1 has f(1) dividing b-f(b)^{f(1)}. is this possible for f(1) not 1? eg say 2 dividing b - b^2. i guess that always happens lol. but 3 dividing b-b^3? that always happens as well lol. oh oops right fermat's little theorem makes this work at least at all primes. 
	* ok what about a=2. here have f(2) dividing b^2 - f(b)^{f(2)}. can this work out? if f(2)=1, then clearly yes, it always works. but what if let's say f(2)=2? then get 2 div b^2 - f(b)^2. this would just say f(b) must have the same parity as b always. what about f(2)=3? then get b^2 - f(b)^3 needs to always be div by 3. this means that if b is 0 mod 3 then f(b) is also 0, and if b is 1 or 2, then f(b) must be 1. 
	* are we going to get strong restrictions at some a? maybe using that f(a) has to divide a^a and f(b) has to divide b^b 
* could also fix b and study it for all a. then f(b) is some const, and we have f(a) always dividing $b^a - f(b)^{f(a)}$ 
* could also take a = b. here get f(a) divs a^a - f(a)^{f(a)}. equivalently, f(a) divs a^a. a=1 gives f(1) divving 1, so f(1)=1
	* ok so also f(a) divs $(a^a-b^a) - (f(a)^{f(a)}-f(b)^{f(a)})$ 
	* set b=1 now. oh oops that's just $1-1$, so not interesting
* oh ok so maybe f(a) dividing a^a is actually really useful because of the following: it implies that f(p^k)=p^m, with the m depending on p and k potentially.
	* so eg for two primes p and q we get that f(p)=p^k divides q^p - q^{m p^k}, so divides 1-q^{m p^k - p}, so $(q-1)$ times a sum. sound like lifting the exponent. let me just look the damn thing up lol.
	* ok maybe we want a=$p^\ell$ actually. and then still say f(a)=p^k, and we get $p^k$ dividing $b^{p^\ell}-f(b)^{p^k}=q^{p^\ell}-q^{mp^k}$, so dividing $
	* trying p = 2 seems pretty nice? in that case the exponent is even, so the 2-valuation is 
* try $f(2^\ell)$. suppose we know $f(2)=2$ somehow. i guess we know it is 1, 2 or 4 from divving. can it be 4? then 4 divides $b^2-f(b)^4$ for all b. this alone seems easily satisfied lol — it's satisfied iff the parity f(b) is that of b. but also need all f(a) to divide 2^a - 4^f(a). hmm wait can we make stuff work with just like 1 4 1 2 1 2 1 2 ...? a = 1 surely works, and a = 2 as well. other a = odd works trivially. and other a = even just need b^a - f(b)^{f(a)} always even. which will be true because the two terms have the same parity! so this indeed works. so c can't be below 2. 
* this motivates: maybe we can sneak in more big stuff? like, could we make 3 be 3^2 or 3^3. need 4 to still divide 3^2 - f(b)^{4}. works for f(3)=9. also works for 27. in fact works for any f(b). ok so just need the divs at a=3 work out. here have eg 9 dividing b^3 - f(b)^{9}. mod 3 we have preservation when cubing so this is going to be just b - f(b). but these might not match mod 3. so this doesn't work
* hmm what about sneaking in more big stuff at powers of 2 then? intuitively it can't work because b^{2^\ell} will be some large thing but f(b)^{f(a)} will be some small thing? well ok idk about that but we can make the large thing have a large power of 2 inside — just pick even b. but then f(b)^{f(a)} will also have a large power of 2 inside right? because f(b) is even as well. so maybe this case is fine. what about b odd though. then f(b) is 1, and the second term is just 1. is the first term necessarily 1 more than a power of 2? see lifting exponent, the first case: get num powers of 2 being num in b-1 plus num in b+1 plus num in a minus 1. the first two terms are going to be in the worst case eg b = 3 mod 8 respectively 1 and 2, and then the last term is \ell when a = 2^\ell. so get \ell + 2 . so potentially we could sneak in a 4x, but no more with this idea?
* so we could try eg the function 1 2 1 16 1 2 1 2 ...
	* if a odd, then trivially works. 
	* if a usual even, then have 2 dividing even, works
	* if a = 4, then need 16 to div b^4 - f(b)^{16}. for usual even, this is b^4 - 2^4, so works. for b=4, clearly works. for odd, this is b^4 - 1. here we could check the mod 16 manually maybe to be super sure? 1 works, 81 works, 5 becomes 9 so works, 7 becomes 1 so works, others work by reflection. so yea c must be at least 4.
*  can we prove that we get issues if we send any 2^\ell to more than 2^{\ell+2}? hmm then certainly have 2^{\ell+3} divide b^{2^\ell}-f(b)^{2^{\ell+3+x}}. let me get a notebook, this is getting annoying
![[Pasted image 20250919094117.png]]

# some thoughts on what was going on

* well, establishing a bunch of facts about what the function must be like
