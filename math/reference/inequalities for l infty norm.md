
from a tweet by clement canonne; forwarded by adam shai:

For x in R^d,

L_infty (x) <= L_{log_2 d}(x) <= 2 L_infty 

ie, up to a const 2, L_infty and L_{log_2 d} are the same

pf of the first inequality: note that L_infty is the lim of L_p as p->infty — this is clear enough. it then suffices to show that for p>=q, we have L_p(x)<=L_q(x). this is saying that sum_i x_i^p <= (sum_i x_i^q)^{p/q}. this is true iff sum_i (x_i^q)^{p/q} <= (sum_i x_i^q)^{p/q} which is true just because (x+y)^alpha<=x^alpha+y^alpha for alpha>=1, which is true just because (x/(x+y))^alpha+(y/(x+y))^alpha<= x/(x+y)+y/(x+y)=1, where the ineq holds because for t<=1 and alpha>=1 we have t^alpha<=t because t^(alpha-1)<=1 because log t <= 0

pf of the second inequality: well, it's just the inequality between p-means (or whatever that's called). pf of that: wts (sum_i x_i^p / d)^{1/p} <= (sum_i x_i^q / d)^{1/q}. equivalently wts  sum_i (x_i^q)^{p/q} / d <= (sum_i x_i^q / d)^{p/q}. this is jensen for x^alpha. apply with p = log_2 d and each q, take lim as q->infty 