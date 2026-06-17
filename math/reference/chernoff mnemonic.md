
n random variables, assume expectation and standard deviation const

then sum standard deviation $\sigma$ scales with sqrt(n), and roughly standard dev squared is expectation

so $\mu \delta$ away is the same as $n\delta$ away is the same as $\sqrt{n}\delta\sigma$ away; this has prob at most $e^{-\mu \delta^2/2}$ 

in terms of $\rho=\sqrt{n}\delta$ (capturing how many standard devs away we are instead), we have $\delta=\rho/\sqrt{n}$, so this is $e^{-\rho^2c}$. so scales just with square of deviation in the exponent. this is also just at least pretty much usual gaussian behavior i guess because tail decays fast enough i guess so that tail integral goes down like pdf or something (need to maybe think more carefully here)

note this true for 0/1 rvs only right, idk if true in much more generality, see other note