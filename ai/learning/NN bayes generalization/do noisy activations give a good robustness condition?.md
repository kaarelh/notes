
* say we have finite bit precision activations
* say we round probabilistically into the closest buckets
* now we subsample. this adds some noise to the real-numbered underlying activations
* but it shifts by much less than a bucket width (we could set things up st this is true)
* 