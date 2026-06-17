
for symmetric matrices, A dot B = trace(AB) creates a PSD inner product (does this also work for matrices in general if one transposes one of them? probably does?). in fact it's just the usual inner product when these are taken as vectors because that's just what the trace of a product does

see here for a cool application: https://www.sciencedirect.com/science/article/pii/0021869373901233?ref=pdf_download&fr=RR-2&rr=802dfe7c0c994213

briefly, an idea is that projection matrices live in this inner product vec space because they are symmetric. and $Tr(u u^T v v^T)=Tr((u\cdot v) uv^T)=Tr((u\cdot v)^2)=(u\cdot v)^2$. I guess this is useful there because the previous condition is on the dot prods to be $\pm \alpha$, and now we get a condition on the squared dot prods to just be $\alpha^2$, much nicer. Now we can construct the gram matrix of a bunch of these projections taken as vectors and argue about its rank as usual to get a bound on the number of projections. 