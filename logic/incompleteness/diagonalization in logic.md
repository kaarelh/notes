
let's eg try to construct a sentence that says 'this sentence has no proof'. maybe consider phi('x') = 'x' is a sentence with one free variable and 'x('x')' has no proof. and then phi('phi') says that 'phi' is a sentence with one free variable and 'phi('phi')' has no proof. so the sentence phi('phi') indeed says that it itself has no proof. i guess we're done?

let's try again with rosser: now the sentence is supposed to say 'for any proof of this sentence, there is a shorter disproof'. now we let phi('x') = 'x' is a sentence with one free variable such that if p is a proof of x(x) then there is a q such that q is shorter than p and q is a proof of not-x(x). and then phi('phi') says that the sentence itself has a shorter disproof for any proof.

the general pattern here is that for any predicate phi with one free variable which talks about sentences with one free variable and plugs the input into itself, we can construct a phi(phi). maybe let's pin down what's happening a bit more though.:
* let phi(x) have the form: 'x('x')' has some property (examples above) (well, i guess crucially, the property is a property of the string, so think of it as a syntactic property. eg famously can't do truth, says tarski's thm)
* the observation is then that phi(phi) says that phi(phi) itself has that property

so this is a fully general way to construct a particular sentence that says it itself has a certain syntactic property