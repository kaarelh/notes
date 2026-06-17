
Why is natural data sparse? eg images, eg in the fourier basis, but maybe also otherwise? 

consider also: are quantum wavefunctions sparse in some basis?

There are at least two questions here:
1) why is stuff sparse?
2) wait, why is there linear structure at all??? (i guess this is really part of the first question, but maybe helpful to spell it out. like, a priori, couldn't it be some complete wack shit with like linear structure after passing everything through some weird-ass map first?)



ok, so i take an image, and i apply some transformation or another. is it still sparse now? for a nonlinear transformation, it generally won't be even if it was initially, right? or maybe it will? i'm confused!


from a discussion with dmitry: consider the fourier transform of an interval. i guess it should have mass only on some intermediate range of wavelengths, namely roughly those around the length of the interval. the reason for sparsity is just that any picture only has a few objects, each one has a characteristic length scale, each scale gives some fourier modes

but then the fourier sparsity has to do with object sparsity/uniformity. what are the details of this process?

decomposing activation vectors sparsely <-> decomposing a scene into objects? does it make sense to decompose hierarchically in the activation vector case, too?

## discussion with jake

![[Pasted image 20240305185332.png]]

![[Pasted image 20240305185347.png]]

![[Pasted image 20240305185404.png]]
![[Pasted image 20240305185419.png]]

![[Pasted image 20240305185432.png]]


![[Pasted image 20240305185452.png]]

## the generative view

http://ufldl.stanford.edu/tutorial/unsupervised/SparseCoding/

## bibliography

https://terrytao.wordpress.com/2007/04/13/compressed-sensing-and-single-pixel-cameras/

obsidian://open?vault=notes&file=physics%2Fquestions%2Fcompressed-sensing1.pdf

