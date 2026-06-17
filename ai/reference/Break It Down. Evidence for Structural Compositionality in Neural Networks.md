
https://arxiv.org/pdf/2301.10884.pdf

The task they pick is to determine whether one shape is both inside another and touching it. They then train masks to optimally do this task just on data where the inside property varies (always touching), and where just the touching property varies (always inside) (? not sure if they also do this). The thought is that if there are separate networks for each, then their masking would kill performance in the other case (and also in the general case, I guess). This is actually not that obvious to me (it might be that e.g. input processing gets hit for the other kind), hmm?

