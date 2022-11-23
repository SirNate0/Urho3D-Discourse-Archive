ToolmakerSteve | 2021-11-30 07:33:48 UTC | #1

Looking at Basic Techniques sample scene, I don't see any that actually displace the surface of a model.

Nor do I see any mention in the Techniques folder.

I'm making a Stone Wall. Normal map works - but would love to have actual depth to its surface - the fakeness of the wall is obvious, especially on the top.

I've got a "displacement" image - just need a way to make use of it.

Recommendations?

OR are there modeling tools out there that can take the "displacement" image, and make a 3D model from it, that would make the wall more realistic? I would need a way to specify how many polygons are okay.

And there probably will be issues where the side meets the top - but one step at a time!

-------------------------

Modanung | 2021-11-30 08:24:45 UTC | #2

https://discourse.urho3d.io/t/parallax-mapping-opengl-only-for-now/1158

-------------------------

ToolmakerSteve | 2021-12-01 18:34:04 UTC | #3

Thanks! Sounds like what I was hoping for. Trying it out now. (I'm using OpenGL)

-------------------------

ToolmakerSteve | 2021-12-03 01:16:30 UTC | #4

I replaced CoreData/Shaders/GLSL/LitSolid.glsl with this one.

When ran, got this exception:

"Failed to compile vertex shader LitSolid(DIRLIGHT INSTANCED NORMALMAP PARALLAX PERPIXEL SHADOW):\nERROR: 0:1086: '=' :  cannot convert from '4-component vector of highp float' to '3-component vector of highp float'\nERROR: 0:1102: 'GetShadowPos' : no matching overloaded function found (using implicit conversion) \nERROR: 0:1102: 'GetShadowPos' : function is not known \nERROR: 0:1101: 'assign' :  cannot convert from 'const highp float' to '4-component vector of highp float'

NOTE: I'm running via urho.Net.

-------------------------

elix22 | 2021-12-03 09:16:43 UTC | #5

This is an old Sample using an old **LitSolid.glsl** shader 
You are mixing old shaders with new ones (Urho.Net is using the new ones)
The signature for GetShadowPos() did change (in Lighting.glsl)
`vec4 GetShadowPos(int index, vec3 normal, vec4 projWorldPos)`

I would advice you to use the matching native part of Urho.Net. for  your development. 
For windows compilation use the scripts in the scripts folder 
https://github.com/elix22/Urho3D/blob/dotnet/script/build_vs2019_dotnet_dll.bat

https://github.com/elix22/Urho3D/tree/dotnet


Also look at a more recent and working implementation 
https://github.com/Lumak/Urho3D-ParallaxOcclusionMap

-------------------------

ToolmakerSteve | 2021-12-03 21:31:08 UTC | #6

Thank you elix. I'm seeing visual artifacts using these parallax shaders.

Occlusion: thin "contour lines" visible - is this expected? fixable?

![occlusion parallax - thin contour lines visible|526x500](upload://mCDXedHcCh8GaQQZIH8H7KRTjf7.jpeg)

Offset: no depth at all, instead, textures distort:

![offset parallax - distorted texture|645x499](upload://nzqZsuZ1xFNM2Ld6jV6C0xD8LNX.jpeg)

This is on standard Box model. Same behavior if apply to my wall. It also happens using the various offset/occlusion materials and textures provided in that repo.

Windows 10, OpenGL, Urho.Net.

In case it was something else in that scene, I've also tested in a simple scene, with nothing but a ground plane and some Boxes, a simple directional light, no shadows.

If approach any of 6 faces of box straight on, the texture looks perfect. As increase camera angle relative to plane of the surface, those distortions appear/increase.

-------------------------

elix22 | 2021-12-04 00:17:06 UTC | #7

Hmm ...
I quickly added this sample to the feature-samples (literally took less the 5 minutes)
Well it's Parallax mapping , just gives an illusion of depth (check the sample below in the link ) .
 https://github.com/Urho-Net/Samples/tree/main/FeatureSamples/Source/Parallax

I guess you want a real displacement mapping , with real depth ?
This sample contains another scene `TerrainScene.xml` created by the same author , some combination of height map + Parallax map

-------------------------

George1 | 2021-12-05 01:20:34 UTC | #8

I think parallax offset has some artifacts at high viewing angle.  Maybe leave a message to Lumak on his Git.

-------------------------

