
https://mathweb.ucsd.edu/~rkoirala/talks/files/fft.pdf

a translation-invariant strict extension of the Lebesgue measure exists, as does an extension to all subsets of R which isn’t translation-invariant assuming some extra axiom considered by logicians: https://math.stackexchange.com/questions/209532/extension-of-the-lebesgue-measurable-sets?noredirect=1&lq=1

there isn’t a maximal extension: https://mathoverflow.net/questions/382299/is-there-a-maximal-translation-invariant-extension-of-lebesgue-measure#comment1164201_382300

i guess zorn’s lemma must fail to apply? we can surely union all sigma-algebras in a chain of extensions, and define a measure for each set just as whatever it is set to in the first sigma-algebra it appears in (it must be set to the same thing in all later ones also by def of our partial order). but i guess one issue is that the sigma-algebra might not be closed under countable unions — consider the case where the unioned sets are from later and later sets along the chain.

it should still be an algebra though? ok extend everything to algebras then. now we can find a maximal algebra containing lebesgue, by zorn. ok but also add the constraint that everything is translation-invariant. now is there somet