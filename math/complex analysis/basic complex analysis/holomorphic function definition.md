
is it sufficient for the limit along any direction of the derivative to exist at any point? i'm pretty sure the answer is no! can probably just construct something with bumps that are ever taller and ever closer and ever smaller in a spiral extending some finite angle, asymptoting to a line? except maybe one can't actually create a complex bump thing? well, one can't create a holomorphic one because of the maximum modulus principle or something, but maybe one can create just a complex along lines differentiable one?

certainly one can make a complex function differentiable along lines in this way for just one point — the bump thing above should just work — but idk, this might cause you to be fucked at other points


OOPS: ans is that this does suffice for complex functions somehow!! even just being continuous and having partials which satisfy CR is sufficient, don't even need differentiability in any direction https://en.wikipedia.org/wiki/Looman%E2%80%93Menchoff_theorem


from [wiki](https://en.wikipedia.org/wiki/Holomorphic_function#:~:text=A%20function%20is%20holomorphic%20on,at%20every%20point%20of%20A.) :
The relationship between real differentiability and complex differentiability is the following: If a complex function _f_(_x_ + _i y_) = _u_(_x_, _y_) + _i v_(_x_, _y_) is holomorphic, then u and v have first partial derivatives with respect to x and y, and satisfy the [Cauchy–Riemann equations](https://en.wikipedia.org/wiki/Cauchy%E2%80%93Riemann_equations "Cauchy–Riemann equations"):[[6]](https://en.wikipedia.org/wiki/Holomorphic_function#cite_note-Mark-6)

∂�∂�=∂�∂�and∂�∂�=−∂�∂�![{\displaystyle {\frac {\partial u}{\partial x}}={\frac {\partial v}{\partial y}}\qquad {\mbox{and}}\qquad {\frac {\partial u}{\partial y}}=-{\frac {\partial v}{\partial x}}\,}](https://wikimedia.org/api/rest_v1/media/math/render/svg/b2b7e5ead4b2cdcc7ccd78602fc988fc371d56ef)

or, equivalently, the [Wirtinger derivative](https://en.wikipedia.org/wiki/Wirtinger_derivative "Wirtinger derivative") of f with respect to �¯,![{\displaystyle {\bar {z}},}](https://wikimedia.org/api/rest_v1/media/math/render/svg/77c492a9c6194f497ee3e55ca21af397fe6a320e) the [complex conjugate](https://en.wikipedia.org/wiki/Complex_conjugate "Complex conjugate") of �,![{\displaystyle z,}](https://wikimedia.org/api/rest_v1/media/math/render/svg/47989a9b66a4ea8a0ec19e8159749fce8a9a8ca8) is zero:[[7]](https://en.wikipedia.org/wiki/Holomorphic_function#cite_note-Gunning-7)

∂�∂�¯=0,![{\displaystyle {\frac {\partial f}{\partial {\overline {z}}}}=0,}](https://wikimedia.org/api/rest_v1/media/math/render/svg/793c48c1205a39f2d2e7c00cf2388a57528689da)

which is to say that, roughly, f is functionally independent from �¯,![{\displaystyle {\bar {z}},}](https://wikimedia.org/api/rest_v1/media/math/render/svg/77c492a9c6194f497ee3e55ca21af397fe6a320e) the complex conjugate of z.

If continuity is not given, the converse is not necessarily true. A simple converse is that if u and v have _continuous_ first partial derivatives and satisfy the Cauchy–Riemann equations, then f is holomorphic. A more satisfying converse, which is much harder to prove, is the [Looman–Menchoff theorem](https://en.wikipedia.org/wiki/Looman%E2%80%93Menchoff_theorem "Looman–Menchoff theorem"): if f is continuous, u and v have first partial derivatives (but not necessarily continuous), and they satisfy the Cauchy–Riemann equations, then f is holomorphic.[[8]](https://en.wikipedia.org/wiki/Holomorphic_function#cite_note-8)

so, thm: continuous partials and CR implies holo

but 