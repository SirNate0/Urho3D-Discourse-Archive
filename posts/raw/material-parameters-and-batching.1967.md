Enhex | 2017-01-02 01:11:53 UTC | #1

Can material parameters be used without creating a new material, so it can be batched?

-------------------------

cadaver | 2017-01-02 01:11:54 UTC | #2

Batching requires the same state (including material & geometry), so you would need to put all the needed parameters into a single material, and put some identifying information in the vertex data so that the shader knows what parameters to use.

-------------------------

