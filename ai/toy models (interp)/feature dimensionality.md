
https://transformer-circuits.pub/2022/toy_model/index.html



We'll define the dimensionality of the �ith feature, ��Di​, as:

�� = ∣∣��∣∣2∑�(��^⋅��)2Di​ = ∑j​(Wi​^​⋅Wj​)2∣∣Wi​∣∣2​

where ��Wi​ is the weight vector column associated with the �ith feature, and ��^Wi​^​ is the unit version of that vector.

Intuitively, the numerator represents the extent to which a given feature is represented, while the denominator is "how many features share the dimension it is embedded in" by projecting each feature onto its dimension. In the antipodal case, each feature participating in an antipodal pair will have a dimensionality of �=1/(1+1)=1/2D=1/(1+1)=1/2 while features which are not learned will have a dimensionality of 00. Empirically, it seems that the dimensionality of all features add up to the number of embedding dimensions when the features are "packed efficiently" in some sense.