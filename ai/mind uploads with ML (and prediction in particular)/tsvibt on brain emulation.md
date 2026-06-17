
tsvibt in https://www.lesswrong.com/posts/jTiSWHKAtnyA723LE/overview-of-strong-human-intelligence-amplification-methods :

"
# Brain emulation

## The approach

> Method: figure out how neurons work, scan human brains, make a simulation of a scanned brain, and then use software improvements to make the brain think better.

The idea is to have a human brain, but with the advantages of being in a computer: faster processing, more scalable hardware, more introspectable (e.g. read access to all internals, even if they are obscured; computation traces), reproducible computations, A/B testing components or other tweaks, low-level optimizable, process forking. This is a "figure it out ourselves" method——we'd have to figure out what makes the emulated brain smarter.

## Problems

- While we have some handle on the fast (<1 second) processes that happen in a neuron, no one knows much about the slow (>5 second) processes. The slow processes are necessary for what we care about in thinking. People working on brain emulation mostly aren't working on this problem because they have enough problems as it is.
    
- Experiments here, the sort that would give 0-to-1 end-to-end feedback about whether the whole thing is working, would be extremely expensive; and unit tests are much harder to calibrate (what reference to use?).
    
- Partial success could constitute a major AGI advance, which would be extremely dangerous. Unlike most of the other approaches listed here, brain emulations wouldn't be hardware-bound (skull-size bound).
    
- The potential for value drift——making a human-like mind with altered / distorted / alien values——is much higher here than with the other approaches. This might be especially selected for: subcortical brain structures, which are especially value-laden, are more physiologically heterogeneous than cortical structures, and therefore would require substantially more scientific work to model accurately. Further: because the emulation approach is based on copying as much as possible and then filling in details by seeing what works, many details will be filled in by non-humane processes (such as the shaping processes in normal human childhood).
    

Fundamentally, brain emulations are a 0-to-1 move, whereas the other approaches take a normal human brain as the basic engine and then modify it in some way. The 0-to-1 approach is more difficult, more speculative, and riskier.

"