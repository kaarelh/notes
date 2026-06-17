
can tell which data points are memorized by looking at whether the gradient updates on these improve loss on other data points (if these have memorizing circuits, they shouldn't, whereas updates on data points which are done using a generalizing circuit should)?

and probably looking at how much gradient updates on other data points improve loss on these should also work, eg would maybe expect that if a data point is still largely memorized, more of its output comes from its memorizing circuit, so pumping more mass into the generalizing circuit should help less on this data point?