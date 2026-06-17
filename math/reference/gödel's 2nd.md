
a proof using the gödel sentence constructed for gödel's 1st thm

suppose the system could prove that it has no contradiction; i.e., that there is no P such that provable P and provable not-P = Q

consider the gödel sentence P = not-provable-x, which unwinds to say that it itself is not provable (I guess via some nice choice of x as a function of stuff or whatever). now note that one can argue inside (with comments outside in parens) the system as follows: "if P were provable, then, using Q, not-P must not be provable. in other words, provable-x must not be provable, so provable-P must not be provable, so P must not be provable (since 'provable P implies provable provable P' is a thm of the system). but then we have a contradiction, since we have both that P is provable and P is not provable. It follows that P is not provable. Therefore, not-provable-x. Therefore, P."

we can also present this very argument to the system inside quotes to give a proof of provable-P. from this, it can conclude that provable-x, so it can conclude not-P. So the system is inconsistent. ie if you can prove there is no contradiction, then there is a contradiction. that's the thm :)

