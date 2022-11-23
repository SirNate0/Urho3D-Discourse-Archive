JTippetts | 2017-01-02 01:08:13 UTC | #1

I'm working on a toy for my son. Trying to use a point light with a material using the NoTextureVCol technique (D3D11 build), with vertex colors painted on in Blender, but it isn't functioning as I would expect:

[img]http://i.imgur.com/eo3iaxv.png[/img]

The object is currently painted with white vertex colors. The point light is colored slightly yellowish. It seems as if the area lit by the point light somehow replaces the vertex colors sent to the pixel shader with a range of colors oriented along the local axes.

For additional context:

In the actual toy, I am using a tri-planar shader that uses the vertex color in the pixel shader to blend from among 3 different texture sets. When a point light is used with this material, the blended terrain within the range of the light changes depending on the orientation and position of the light, so it becomes apparent that the light is actually modifying the vertex color that gets sent to the pixel shader.

[img]http://i.imgur.com/HavNYZD.jpg[/img]

 This behavior exhibits both in my tri-planar shader and in the basic LitSolid shader with NoTexture and VCol options.

Any recommendations on how I can fix this?

EDIT: Using forward rendering.

-------------------------

cadaver | 2017-01-02 01:08:14 UTC | #2

This looks like wrong interpolators being used, which is a D3D11-only "feature"; the shader compiler messes up even though we should have explicitly assigned interpolator semantics. We should be able to fix the input/output order in the shader source file so that this is avoided.

Can you check if D3D9 or OpenGL work OK?

(OK, I just read this: [gamedev.stackexchange.com/questi ... sl-d3d11-c](http://gamedev.stackexchange.com/questions/40348/partial-shader-signatures-hlsl-d3d11-c) , which confirms that when shaders are compiled separately, user-defined semantics have no meaning and don't help with the order at all. So one can treat the in/out parameters as a struct whose memory layout needs to match exactly.)

-------------------------

JTippetts | 2017-01-02 01:08:14 UTC | #3

Looks like it does work correctly with D3D9.

-------------------------

cadaver | 2017-01-02 01:08:14 UTC | #4

Should be fixed for D3D11 in the master branch.

-------------------------

JTippetts | 2017-01-02 01:08:16 UTC | #5

Looks like it works. Thank you.

-------------------------

