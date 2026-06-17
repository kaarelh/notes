

We could be interested in relating the circuit complexity of a function to the number of wrong predictions a circuit induction algorithm makes when learning it.

# messages to dmitry proving the expected number of mistakes gives an upper bound on the circuit complexity
ok i \approx convinced myself that for circuit induction, expected regret m when learning the function f implies there is a circuit of size O(m log m * inputdim) implementing f

the idea is to upper bound contributions to log loss, splitting into cases according to whether a mistake probability is low or high. contributions of the low mistake probabilities are easy to bound by the expected number of mistakes. contributions of the high mistake probabilities can be bounded by noticing that mistakes can't be overwhelmingly likely because you can always just add opposite memorizations to all surviving circuits

i wrote down this more detailed argument, then realized it has an issue; i think the issue is not serious, just mildly annoying, but i probably won't write a corrected version now (i'm getting sleepy):

Suppose that the expected number of mistakes when learning the boolean function $f$ is $m$. Let the mistake probabilities on each step be $P_1, P_2,\ldots$ (we think of these as random variables that depend on the reveal order of inputs $x_1,x_2,\ldots$). The log loss one would incur by the end is $-\sum_i \log(1- P_i)$. To show there is a circuit of size at most $poly(m)$ implementing $f$, it suffices to show the log loss is at most $poly(m)$.

We have $\mathbb{E}[\sum P_i]=m$ by definition of $m$. We're interested in upper-bounding $\mathbb{E}[-\sum_i \log (1-P_i)]$ or equivalently just $-\sum_i \log (1-P_i)$ over any sequence (because it's just the negative log prior probability of $f$, so actually independent of the sequence). Let's consider separately the contribution from the error probabilities $P_i$ that happen to be $<1/2$ and the contribution from the $P_i$ that are $>1/2$. That is, let's split $\mathbb{E}[-\sum_i \log (1-P_i)]=\mathbb{E}[-\sum_i \log (1-P_i)I_{P_i\leq 1/2}]+\mathbb{E}[-\sum_i \log (1-P_i)I_{P_i>1/2}]$. We can do the same indicator split for the sum defining $m$. That is, $\mathbb{E}[\sum P_i]=\mathbb{E}[\sum P_i I_{P_i\leq 1/2}]+\mathbb{E}[\sum_i P_i I_{P_i>1/2}]$.

Let us first bound the small error probability contribution $\mathbb{E}[-\sum_i \log (1-P_i)I_{P_i\leq 1/2}]$. For $P_i\leq 1/2$,, we have $-\log (1-P_i)<10 P_i$, so $\mathbb{E}[-\sum_i \log (1-P_i)I_{P_i\leq 1/2}]\leq 10\mathbb{E}[\sum P_i I_{P_i\leq 1/2}]\leq 10 m$.

Let us now bound the large error probability contribution $\mathbb{E}[-\sum_i \log (1-P_i)I_{P_i>1/2}]$. Note that the expected number of indices $i$ at which $I_{P_i>1/2}=1$ is at most $2m$, because each one contributes at least $1/2$ to the expected number of mistakes. Similar reasoning gives that with probability at least $99\%$, the number of times this indicator fires is at most $200m$. Each time it does fire, how big can $-\log(1-P_i)$ be? Note that you can take each circuit compatible with the data so far and surgically add to it a memorized exception $x_i\mapsto f(x_i)$, which adds at most $poly(inputdim)$ to its description length (i later realized this but i don't want to rewrite atm: oops i think actually this should also have a $+O(\log m)$ term because of details of connecting up the memorization circuit), so creates another circuit which has prior at least $2^{-poly(inputdim)}$ its prior and does not make an error on $x_i$. This implies that $P_i/(1-P_i)\leq 2^{poly(inputdim)}$, which implies that $-\log(1-P_i)\leq poly(inputdim)$. So, restricting the distribution on input sequences only to the $>99\%$ cases where the indicator fires at most $200m$ times, the big error probability term contributes at most $200m \cdot poly(inputdim)$. 


Now we change what we're doing a bit to make everything hang together. Restrict the distribution of input orderings to these $99\%$ of cases, changing the meaning of $\mathbb{E}$. Note that it still suffices to show $\mathbb{E}[-\sum_i \log (1-P_i)I_{P_i\leq 1/2}]+\mathbb{E}[-\sum_i \log (1-P_i)I_{P_i>1/2}]\leq poly(m)$, because it actually suffices to show this for any input ordering. Note that the former term is still at most $10m/0.99\leq 11m$. And we've argued that the latter term is at most $200 m \cdot poly(inputdim)$. QED. 

edit later: taking the earlier edit into account, i guess we should get $m\log m$

hmm actually i now think the statement that [the expected number of mistakes when learning f is m] => [f has a circuit of size poly(m)] is true for NN bayes as well

# the circuit complexity also bounds the expected number of mistakes

i convinced myself that the other direction works as well btw, ie that expected regret < poly(circuit complexity). i give an argument below. probably you knew this already.

We have a function $f$ of complexity $C(f)$. There are at most $exp(poly(C(f)))$ functions with smaller complexity. Let's upper bound the probability that occam learning makes an error on step $n+1$. The expected number of errors can then be upper bounded by the sum of these bounds over $n$ (by linearity of expectation).

We split the event that occam learning makes a mistake on step $n+1$ into two cases according to whether the error probability of the simplest remaining circuit after the first $n$ data points is big or small:
* The smallest remaining circuit's error probability is very unlikely to be greater than $2d\cdot poly(C(f))/n$ (with the same poly as before, and with $d$ being the input dimension), so this case doesn't contribute that much.
	* Concretely, if the error probability is more than $d\cdot poly(C(f))/n$, then some circuit with at least this error probability must have survived. But there are at most $exp(poly(C(f)))$ circuits with such an error probability to begin with, and for each one of these, the probability it survives the first $n$ steps is $(1-2d\cdot poly(C(f))/n)^n\approx e^{(-2d\cdot poly(C(f))/n) n}=e^{-2d\cdot poly(C(f))}$. By a union bound, the probability that any circuit with at least this error probability has survived is thus at most $exp(-d\cdot poly(C(f)))$. So the probability that after $n$ steps occam learning has a high error probability smallest remaining circuit and it makes a mistake is also at most $exp(-d\cdot poly(C(f)))$.
* And the probability that after $n$ steps the smallest remaining circuit has error probability less than $2d \cdot poly(C(f))/n$ and then it makes an error on step $n+1$ is at most $2d\cdot poly(C(f))/n$. 

Combining these two bounds and summing a harmonic series, we get that the expected number of errors on the first $N=2d \cdot poly(C(f)) \cdot exp(d)$ data points is at most $poly(C(f),d)$. 

After the first $N$ data points, the expected number of further mistakes is at most the expected number of surviving wrong circuits (since each mistake occam learning makes can be associated with a circuit that is then ruled out); we will finish the proof by arguing this is small. Note that each wrong circuit has error probability at least $1-2^{-d}$ — there are only $2^d$ different inputs, and if the circuit does not implement $f$, it has to be wrong on at least one of them. (Here I'm assuming we have a uniform distribution on inputs. The argument still works if you have a different distribution, as long as you have a lower bound of the form $exp(-poly(d,C(f)))$ on each nonzero probability. Without any assumption on the distribution, proving this sort of regret bound becomes equivalent to the out-of-distribution case, which idk how to rigorously prove (also idk if the statement is even true). However, a PAC bound is still easy in the in-distribution case for any distribution.) Thus, the expected number of remaining wrong circuits is at most $exp(poly(C(f)))(1-2^{-d})^N\approx exp(poly(C(f)))e^{-2^{-d}\cdot 2d\cdot  poly(C(f))\cdot e^d}<1$.

Combining the error count from the first $N$ data points with the error count from the remainder, we conclude that the expected number of errors is at most $poly(C(f),d)$. 




# mess
For each specific circuit of the $exp(C(f))$ relevant ones, the probability that it survives for the first n steps and then makes a mistake on step $n+1$ is at most $1/(n+1)$ (this follows from symmetry under permuting the input sequence — recall that we are in the iid case). Since occam learning making an error on step $n+1$ implies this event for at least one circuit, we can bound the occam learning error probability by the union bound of $exp(C(f))\frac{1}{n+1}$.

Summing these, we conclude that after seeing $n$ data points, the expected number of errors is at most $

After this, ie with $n>2d \cdot poly(C(f)) \cdot exp(d)$, the latter case becomes impossible because the error probability of any circuit has to be at least $2^{-d}$ 