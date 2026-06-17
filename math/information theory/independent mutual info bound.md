

"independent things inform jointly at least [as much as they inform individually, aggregated]"


Thm. Let $X_1,\ldots,X_n$ be independent random variables, and $W$ a random variable. Then 
$$I((X_1,\ldots,X_n);W)\geq \sum_i I(X_i;W).$$

Pf.
$$I((X_1,\ldots,X_n);W)=H(X_1,\ldots,X_n)-H((X_1,\ldots,X_n)|W)= \sum_i H(X_i) -\sum_i H(X_i|W,X_1,\ldots,X_{i-1})\geq \sum_i H(X_i)-H(X_i|W)=\sum_i I(X_i;W).$$


the case with $n=2$ says that $I(X_1;X_2;W)=I(X_1; W)-I(X_1; W |X_2)$... nvm