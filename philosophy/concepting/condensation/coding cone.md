
so setup. each variable needs to be recovered from some given subsets of channels. the variables are independent let's say. then conjecture: can code iff can code variables separately and concatenate.
simple case to try to prove this in: just 2 variables, each needing to be seen from some given subsets


for each old latent: the new latents have to know enough about it, above each singleton

so can track how much the new latents in fact know about it. i guess this has to be wrt some fixed ordering for the upset above each singleton. these could come from a global ordering. the old latent also then knows at least this much about these new latents

can we then just say that the rate of each new latent has to be at least the sum over old latents of how much it knows about each old latent? then we'd be done i think? something like this is true bcs the old latents are independent but i'm worried the precise thing we need might not follow like this because we aren't conditioning on the right stuff to make it work



for each old latent and singleton below it, that singleton has to know that latent — ie the new latents above that singleton have to know that latent. so the old latent has to know a bunch about these new latents

can ask: how much does the old latent have to know about each new latent. but maybe not that much because maybe it only knows about them jointly? i guess then could fix some ordering and still say sth?

could say: all old latents above a singleton together have to know a bunch about all new latents above a singleton together

so all new latents above a singleton together have to be 


suffices to show that can code at rates => could code the latents separately and just concatenate

# looking at an inequality

so each ij needs to tell us at least 1 bit about i,j given all the other stuff. but also 

123 is a function of any two. if you condition on two, it doesn't matter if you also condition on that. given any two, the third gives no info about the top, and we know it has to give more than 1 bit about the two singletons below it

it feels like the third has to spend some info knowing about the top though. but idk how to make that precise 

is it possible to have 4 random variables (or maybe codes) A, B, X, Y such that:
* X and Y together tell you A and B. A and B are independent
* H(X)<2
* X tells you >=1 bit about A alone
* given Y, X tells you >=1 bit about B

we know that X can't tell you >=1 bit about B alone, but maybe it can do so given Y?

ok let's say A and B are indep coinflips. say X tells you A in full. then how tf can X have a whole other bit about B given Y?? it needs to get us from knowing nothing about B to knowing everything about B, given Y. i guess Y could be the XOR of the two coins? hmm i guess here indeed we could even make H(X)=1. but this depends on Y knowing something about (A,B) which isn't just knowing 

ok so can we understand the difference between I(X;B) and I(X;B|Y)? this is H(B)-H(B|X) vs H(B|Y)-H(B|X,Y)

how much do X,Y tell you about A,B together? 

I(X,Y;A,B)=

maybe another sharp example would be good?

 1.5,  1. ,  1. ,  1. ,  1. ,  1. ,  1. , -0. 

1
0 0 0
1 1 1

goes to

   0
3/2 3/2 3/2
  0    0    0

can one be sharper than that? like in terms of total entropy, we might hope to get 4/3 each? what would go wrong then? so now we have a supposed coding with

   0
4/3 4/3 4/3
  0    0    0

each pair has some function on it giving the top bitstring. after that there are typically 2^{5n/3} choices left for what the pair is right?  on these choices there is a further partition giving the bottom bitstring they have to determine together. then there are still 2^{2n/3} choices left typically for what the pair is. so 

wait surely we just have a redundancy argument here. like there can't be any multiple-informing about the top latent. but also the top latent has to be seen from any pair. wtf. each pair has 1 bit about the top. this leaves each pair 5/3 bits to have about anything else 

can we just show that the new latents have to know stuff about each other maybe? like how could they have 0 mutual info. any pair knows the top. if the third knew sth about the top alone, the pair would know something about the third i think? yea i guess I(pair, third)>=I(top, third) so I(top, third) must be 0... so each thing must know 0 about the top lol. so given any one thing, any other thing must know 1 bit about the top. so given any thing, any other thing knows only 1/3 about what's below. so each thing must know 1 bit about both things below it!!!!!!!



maybe we could make this still work in the sharper case by conditioning it all on 1 also or something? the issue is currently that you get that given any thing any other thing knows at most 1 bit about what's below, which isn't enough to get sth interesting

1 0 0 0 1 1 1 -> 0 1.49 1.49 1.49 0 0 0

at most 0.47 mutual info. ij and ik know 123 but also know i. so jk can't know too much about 123,i — else we would have too much redundancy. more precisely, we get I(123,i;jk)<0.47 (and permutations). adding ij in, we fully determine j and also fully determine 123 

wait do we know that ij and ik tell us stuff about j and k also? anyway, to the extent that they do, that's another thing that jk can't know much about 


1 0 0 0 1 1 1 -> 0 3/2 3/2 3/2 0 0 0 is maybe a slightly nicer sharp case for this inequality. a proof that you can't code with the 3/2 replaced by 3/2-eps here:
* say the input latents 1,2,3,123 are independent coinflips. suppose you can code with all H(ij) < 3/2
* since H(12)+H(13)+H(23)<9/2 and they have to determine 1,2,3,123 with H(1,2,3,123)=4, we have I( ij,ik ; jk) < 1/2 (the new latents can't know too much about each other)
* since ij,jk determine 123, it follows that I(123;jk) <= I( ij,ik ; jk) < 1/2 (no latent can know much about 123)
* since jk,ik determine 123, we then have I( 123 ; ik | jk ) > 1/2 (each latent has to know a lot about 123 given any other latent)
* since H(ik) < 3/2, we have I( i,j,k ; ik | jk , 123) < 1 (no latent can know much about singletons given another latent and 123)
* so  I( i,j,k ; jk | 123) + I( i,j,k ; ij | ik, jk, 123) > 2

1 > I( i,j,k ; ik | jk , 123) = H(i,j,k|jk,123)-H(i,j,k|ik,jk)=H(i,j,k|jk,123)-H(i,j|ik,jk)

I( i,j,k ; ij | ik, jk, 123) = H(i,j|ik,jk)>1


H(i,j,k|ik,jk)>1

ij and ik have <1 bit to say about j and k
but each alone has >1 bit about i,j and i,k respectively?
and together know i? so then don't they know more than 1 bit about j and k maybe?

I( i,j,k ; ij,ik ) = I(i,j,k;ij)+I(i,j,k;ik|ij)
1+I(j,k;ij,ik)<2

maybe look at I( i,j,k,ijk ; ij,ik )? well this is 4 minus how much jk informs after, which is how much it informs about j,k, which we have already established to be at least 1 bit

maybe there's some contradiction in ij needing to say 1/2 about 123 when added second, but also maybe we can show it has to know >= 1 bit about stuff below still? like say adding ij after ik. how much does it need to say about stuff below? well it needs to finish determining i and it also probably says something about j



so the third one always knows 1 bit about singletons given two. but so what! it needn't know anything about the top one right? hmm
what about the second one? i guess it needs to know 1/2 about 123, and so <1 about singletons


any two 


did we already know jk knows a bunch about i,j,k? hmm. so what goes wrong if it knows >1 bit about them when alone? i guess we know then that each thing knows >1 about stuff below
do we maybe get 2 eps down somehow?




ij and ik know i together. so one must know at least 1/2 about i


the third one needs to inform by > 1 bit about stuff after the first two, for any third one

but can it even have that much entropy left after the other latents are revealed? given that any pair also determines sth with 1 bit together?



like on the one hand every latent needs to have 1 bit of entropy given the other two

on the second hand any two need to determine a function which takes 1 bit

on the third hand each has <3/2 bits of entropy itself

intuitively, you need to lose 1/2 bit to the function at least, and then you can't have a full bit once the function is known?
like, surely at least one of them has to lose 1/2 bit to the function?

ahh yea maybe this works! like given 12, we have that the function 123 knows a bunch about 13. but then also 12 and 23 together know a bunch about 13. but then 13 can't know that much more? but it needs to know more!

let's try to make this precise

1 0 0 0 1 1 1 -> 0 3/2 3/2 3/2 0 0 0 is maybe a slightly nicer sharp case for this inequality. a proof that you cannot code with the 3/2 replaced by 3/2-eps here:
* say the input latents 1,2,3,123 are independent coinflips. suppose you can code with all H(ij) < 3/2
* since H(12)+H(13)+H(23)<9/2 and they have to determine 1,2,3,123 with H(1,2,3,123)=4, we have I( ij,ik ; jk) < 1/2 (the new latents can't know too much about each other)
* since ij,jk determine 123, it follows that I(123;jk) <= I( ij,ik ; jk) < 1/2 (no latent can know much about 123)
* since jk,ik determine 123, we then have I( 123 ; ik | jk ) > 1/2 (each latent has to know a lot about 123 given any other latent)
* from 1/2 < I( 123 ; ik | jk ) = H(ik|jk)-H(ik|123,jk) and H(ik|jk) <= H(ik) < 3/2, we conclude H(ik|123,jk)<1 (a latent doesn't have that much entropy given 123 and another latent)
* since 123 is a function of ij and jk, we have 1 > H(ik|123,jk) >= H(ik|123,jk,ij) >= H(ik|ij,jk) (a latent doesn't have that much entropy given the other two latents)
* but then the total entropy of the latents is strictly less than 3/2+3/2+1=4, a contradiction

I'm pretty sure this proof will give the 

1 0 0 0 1 1 1 -> 0 3/2 3/2 3/2 0 0 0 is maybe a slightly nicer sharp case for this inequality. a proof that you cannot code with the 3/2 replaced by 3/2-eps here:
* say the input latents 1,2,3,123 are independent coinflips. suppose you can code with all H(ij) < 3/2
* 12 and 13 together have to tell you 123, so either [12 tells you at least 1/2 bits about 123] or [13 tells you at least 1/2 bits about 123 given 12] :
	* [if 12 tells you at least 1/2 bits about 123] : then of course 123 tells you at least 1/2 bits about 12. but recall that 13 and 23 tell you 123, so then they must also tell you at least 1/2 bits about 12. but then H(13,23,12) < 3/2+3/2+3/2-1/2 = 4, contradicting with the latents coding something of 1+1+1+1=4 bits total
	* [if 13 tells you at least 1/2 bits about 123 given 12] : then (similarly to the above point) 12 and 23 together tell you at least 1/2 bits about 13, again leading to the same contradiction



* since H(12)+H(13)+H(23)<9/2 and they have to determine 1,2,3,123 with H(1,2,3,123)=4, we have I( ij,ik ; jk) < 1/2 (the new latents can't know too much about each other)
* since ij,jk determine 123, it follows that I(123;jk) <= I( ij,ik ; jk) < 1/2 (no latent can know much about 123)
* since jk,ik determine 123, we then have I( 123 ; ik | jk ) > 1/2 (each latent has to know a lot about 123 given any other latent)
* from 1/2 < I( 123 ; ik | jk ) = H(ik|jk)-H(ik|123,jk) and H(ik|jk) <= H(ik) < 3/2, we conclude H(ik|123,jk)<1 (a latent doesn't have that much entropy given 123 and another latent)
* since 123 is a function of ij and jk, we have 1 > H(ik|123,jk) >= H(ik|123,jk,ij) >= H(ik|ij,jk) (a latent doesn't have that much entropy given the other two latents)
* but then the total entropy of the latents is strictly less than 3/2+3/2+1=4, a contradiction

### a combinatorial attempt

ok so we have these 4 things — a common string and 3 private ones — and we are interested in 3/2-eps factor longer strings generating the uniform distros on these guys in some structured way

namely, for any two strings, we have a map from the product space to the joint string. and then also another map from the product space to a private string. each one cuts the 2^(3-2eps)n size space into 2^n pieces. 
can we somehow think of a pair as storing the common thing and some other stuff always?

the difficult thing is that they all need to be independent but the common string needs to always be the same. maybe think of common string as chosen first. now each product space has (2-2eps)n choices of a point left, tho ofc these 3 choices need to be made compatibly — making the choice in 12,13 restricts the choice in the other two prods to be given by just picking an elt of 23.

# a different inequality


3.,  2. ,  2. ,  2. ,  1. ,  2. ,  2. , -0. 

when is this interesting? it's almost the same as the one above, except that one place has sth smaller. if that place were negative, it would be implied by the other one, so that place needs to be positive for this to be interesting. what if we still just did pos neg pos? then one thing one the constraint would be eg:

2
-2 -2 -2
2 1 1

ie 
2
0 0 0
2 1 1 

going to

0
2 2 2
0 0 0

wait but wtf, this is already ruled out by the previous thing right? 

ok lets think it over. we have this linear combo being >= 0. we already had before another linear combo with + sth >= 0. if that sth is positive, then the present constraint is just strictly stronger. so this constraint 


either i'm confused or this cone is wrong:
* the slepian-wolf idea lets us do 2 0 0 0 1 1 1 -> 0 2 2 2 0 0 0 (just split the top latent into 1 1 1 and lift each bottom latent to 1/2 1/2)
* so -2 2 2 2 -1 -1 -1 should be a valid move

ohhhh i see. i was getting the sign wrong. yes, the change needs to have sth positive at that coord. so it shouldn't be the same sign as before. maybe we could go back to the sign pattern being pos neg pos then? i guess then we are just strictly bigger than the first inequaelity we could prove, so this wouldn't be interesting. maybe have a split in the bottom layer so that one is pos and others are neg? and let's say middle layer pos and top neg? so like:

x
0 0 0
0 y y 

goes to

0
z z w
q 0 0