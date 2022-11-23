najak3d | 2022-02-02 09:31:19 UTC | #1

I think this is a no brainer but wanted to make sure I wasn't missing something before we make this our plan.    If we call "staticModelGroup.Material.SetShaderParameter(...)" will this apply that parameter for all instances of the group reliably?

If it's that easy, that's awesome, because then for our 1000 windmill example, we can just employ a custom shader that uses a ShaderParameter called "cRotation", that applies this rotation (in model space) on each vertex prior to converting to world space in the vertex shader -- and effectively we'll be able to cheaply animate our WindMill Propellers simply by incrementing the value of the "cRotate" value each frame, for each StaticModelGroup.

So the blades aren't all in full-unison, we'll split it up into a dozen such groups, interleafed spatially, so that we don't have any two adjacent windmills spinning in unison.  It may not be perfect, but cheaply avoids the "creepy spinning in perfect unison nuance" that would otherwise result.

Are we missing anything here?  Our plan is just to create a custom Vertex shader that applies a "Roll rotation" to Propeller vertices prior to converting into World space.

-------------------------

JTippetts1 | 2022-02-02 13:34:53 UTC | #2

Yes, they will share a material so all uniforms will be shared. If you want randomized per-windmill rotations, you can use the translation part of the model view matrix in the vertex shader as a sort of unique identifier. Hash it to generate a rotation value for just that windmill that will be different from its neighbors.

-------------------------

najak3d | 2022-02-02 17:06:24 UTC | #3

That is brilliant!   Thank you for the great idea.   That's exactly what we'll do!

-------------------------

