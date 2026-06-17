
i wonder what happens in this circuit learning example when we drop the in-distribution assumption

for this learning algorithm to suck when learning a function f for some input-output pair reveal order, there'd need to be a long sequence of inputs x_1, x_2, ..., x_n (let's say "long" means n is superpolynomial in the circuit complexity of f) such that there is a sequence of circuits C_1, C_2, ..., C_n satisfying the following conditions:
* the size of C_1 <= the size of C_2 <= the size of C_3 <= ... ("size" = specification length = circuit complexity of the function)
* C_i agrees with f on x_1, x_2, ..., x_{i-1}, but then disagrees with f on x_i

i'd like to be able to construct an example or prove this can't happen

(caveat: i think the above is necessary for the learning algorithm to suck, but maybe not sufficient. so i think the above is maybe technically not equivalent to whether the learning algorithm sucks on some input sequence. but it feels like the/a right question to ask anyway)

# oops the ans is "this is possible" but also this isn't the right question

so you just construct each C_i to be the same base thing (eg just the const -1 function or whatever) together with a small exception. you make the exception circuits of increasing complexity. then you get this sequence i guess... but it's not an example showing circuit induction sucks because these previous exceptions aren't actually the lowest complexity things so far right! like, instead, you just get the const -1 function as your guess until you get to the correct exception input eventually and you're wrong there but maybe right after! like, these intermediate C_i are not the circuits you'd really learn

# why it's weird to get this ood generalization failure

somehow you need the simplest circuit to not generalize correctly but most circuits to survive... seems weird

