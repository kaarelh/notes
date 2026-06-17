
https://scottaaronson.blog/?p=710

consistent guessing problem:
is there a TM which says if input TM accepts or rejects on given input if it halts and always outputs something when it doesn't halt

(ie i've not given a problem here strictly speaking — there's a variety of allowed behaviors)

the ans is that there is no TM which does this. the proof is usual diagonalization, constructing a machine that runs a machine on its own source code and gives the opposite output or whatever when it doesn't halt, then running that on itself

now suppose there is a consistent complete syntax. then i can use it to build a guessing TM by just searching for proofs of accept vs no accept, outputting accept/reject accordingly. when the machine actually accepts, i must say that it does, because otherwise there'd be a purely syntactic contradiction — just do the TM steps vs the no-accept proof. similarly, when the machine actually rejects, i must say it doesn't accept, otherwise i'd be inconsistent. so this would solve consistent guessing, which is impossible! therefore there's no consistent complete syntax