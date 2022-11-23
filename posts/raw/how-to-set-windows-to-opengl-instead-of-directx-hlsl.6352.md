najak3d | 2020-08-28 14:53:58 UTC | #1

Our application runs on Windows, Android, and iOS all using UrhoSharp.

Is there a way to tell UrhoSharp at startup to use OpenGL instead of D3D?   It's a shame to be writing all shaders for both GLSL and HLSL - there's just no point to it, if we can instead get OpenGL to work on Windows.

-------------------------

JTippetts1 | 2020-08-28 16:51:18 UTC | #2

Graphics API selection is done at compile time, not at run time (at least for vanilla Urho3D). If you can't rebuild UrhoSharp with the URHO3D_OPENGL flag, then you're probably out of luck.

-------------------------

najak3d | 2020-08-28 16:51:50 UTC | #3

Ah shoot.  I guess we're stuck writing two versions of every shader.

-------------------------

najak3d | 2020-08-28 17:06:17 UTC | #4

For UWP, I think there are extra challenges to get OpenGL support anyways --- and UWP is one of our platforms -- so I don't think we even have the option of compiling UrhoSharp for OpenGL on UWP.

-------------------------

