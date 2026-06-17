**editorial remark: moved to overleaf**
commands
$\newcommand{\R}{\mathbb{R}}$

end commands

>Let $U\subseteq \mathbb{R}$ be open. Then $U$ is a disjoint countable union of open intervals. (Note that we are not requiring intervals to be finite here, and indeed the statement would be false in that case.)
>Proof. For each $x\in U$, let $I_x$ be the union of all intervals that are subsets of $U$ and contain $x$. Note that $I_x$ is an interval. Letting $\mathcal{I}$ denote the set of all such intervals for points in $U$ (i.e. if different points have the same interval, it only appears once in this set), note that two non-equal intervals have to be disjoint (otherwise their union would be another interval in $U$, implying that neither would be in $\mathcal{I}$), and that $U$ is the union of the elements of $\mathcal{I}$. Since each element of $\mathcal{I}$ is an interval, it in particular contains a rational number; pick one such rational number $q_I$ for each $I\in \mathcal{I}$. Note that since all $q_I$ are distinct, $\mathcal{I}$ is countable.



>If $E\subseteq \R$ has positive measure, for any $0\leq \rho<1$, there is an interval $I$ such that $\mu(E\cap I)\geq \rho \mu(I)$ 

>If $E\subseteq \R$ has positive measure, then $E-E$ contains an interval.

Let's show that an open interval around $0$ is contained in $E-E$. If not, then arbitrarily small gaps are missing from $E$.  

>There is a measurable set $A\subseteq \R$ such that for every nonempty open interval $I$, $0<m(A\cap I)<m(I)$, where $m$ denotes the Lebesgue measure. 