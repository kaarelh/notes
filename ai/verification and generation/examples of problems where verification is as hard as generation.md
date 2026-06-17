
for some problems where one specifies the desired answer in terms of a protocol for computing it, there isn't any faster way to verify the answer than just following along that protocol as well:
* eg: what is the parity of [the number of numbers-with-weird-unstructured-property below $10^{100}$]?
	* it seems plausible that one can't provide a shorter proof that the answer is sth here than one which just goes through all the numbers, checking whether they have the weird property, and keeps track of the sum mod 2? idk maybe one can exploit some structure for some properties, but probably not for some?
	* and so one probably can't verify an answer significantly faster than one can generate it?
* eg: finding whether a turing machine halts in some number of steps (for some turing machines, presumably you can't provide a significantly shorter proof than one which just follows the execution for that number of steps)
* more generally:
	* finding the output of a turing machine (for some turing machines, presumably you can't provide a significantly shorter proof than one which just follows the execution until it outputs something)