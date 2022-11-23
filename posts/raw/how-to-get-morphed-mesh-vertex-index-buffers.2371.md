godan | 2017-01-02 01:15:01 UTC | #1

I've been working on integrating the animation system in to Iogram: [twitter.com/Mesh_Geometry/statu ... 0849591296](https://twitter.com/Mesh_Geometry/status/792051690849591296)

However, how do I get the morphed mesh out of the AnimatedModel class? Is it the Animation State? Or one of the morph targets?

-------------------------

1vanK | 2017-01-02 01:15:01 UTC | #2

ApplyMorph() modify morphVertexBuffers_ in AnimatedModel::UpdateMorphs(), so I think you need AnimatedModel::GetMorphVertexBuffers()

-------------------------

