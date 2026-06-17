
maybe should call this: kleene's self-reference theorem

thm. suppose there is Q(x,y). then also there is a program p such that p(y)=Q(p,y) (for all y — ie these are equal functions)

informally: it's fine to write programs that know their own source code. there always is a program that does the same thing without magic

pf. see mess below


# mess

want to say we just set p(y)=Q(Q,y) but of course that's different than Q(p,y) then because p will be Q with itself plugged into the first coord. 
we could try to say p(y) = Q(Q with itself plugged into the first coord, y) but that isn't right either because then p will not be Q with itself plugged into the first coord
in general the issue is that 

maybe we define an auxiliary A(a,y) that runs a(a,y) (if that makes syntactic sense)? now A(A,y) runs A(A,y)

maybe we define an auxiliary A(a,y) that runs a(a(a,blank),y) (if that makes syntactic sense)? now A(A,y) runs A(A(A,blank),y)


ok maybe let's get rid of the y for now. can we just have a program that does something with its source code, without a second input? like we have Q(x) and want to show there is some program p such that p outputs what Q(p) outputs. 

again, we can't just do Q(Q).

we can define an auxiliary that takes in a program with one free variable and runs it with itself plugged in: A(s) = s(s).

can we do Q(A(Q))? this is Q(Q(Q))

ok so need Q(p) to somehow compile into p, for some special p. p needs to have some longer form... the outer part needs to be Q() i guess but inside you could have something funny? 

maybe define aux program A(s) that does Q(s(s))? and then consider A(A) = Q(A(A)). yay now we have a program A(A)=p which satisfies p = Q(p)!

ok so now let us go back to the two variable case. we similarly define an auxiliary A(s,y) = Q(s(s,blank),y) and now we note A(A,y) = Q(A(A,blank),y). now let p(y)=A(A,y) and note that p(y)=A(A,y)=Q(A(A,blank),y)=Q(p,y). nice!