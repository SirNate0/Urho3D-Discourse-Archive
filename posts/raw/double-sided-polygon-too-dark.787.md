practicing01 | 2017-01-02 01:02:53 UTC | #1

Hello, I've created a model in blender and set it to be double sided.  Everything looks fine in blender, within the Urho3D editor however, one side is darker than the other.  I've set the model to use the DiffAlphaMask technique and no culling.  Any help would be greatly appreciated, thanks for your time.

-------------------------

JTippetts | 2017-01-02 01:02:53 UTC | #2

What's your lighting setup like? DiffAlphaMask is a lit shader, so it will respond to lighting.

-------------------------

practicing01 | 2017-01-02 01:02:54 UTC | #3

I've got a directional light for each direction, the entire model is lit well.  As a temp fix I just duplicated the faces and flipped the normals in blender.

-------------------------

codingmonkey | 2017-01-02 01:02:54 UTC | #4

>As a temp fix I just duplicated the faces and flipped the normals in blender.
and you maybe got z-fighting if the cull mode is = none.

-------------------------

OvermindDL1 | 2017-01-02 01:03:15 UTC | #5

Likely the back side was just not being lit because the normals were pointing the wrong way for it and the shader does not flip it for polys that wind the other way?

-------------------------

