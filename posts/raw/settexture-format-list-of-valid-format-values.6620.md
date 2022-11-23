najak3d | 2020-12-20 21:39:48 UTC | #1

I looked through what I thought was the complete Urho3D source code, but couldn't find the values 6408 nor 6410 for the OpenGL formats for RGBA(6408) and AlphaLuminance(6410).

I'm wondering where if these exist in the code anywhere, or are they pulled from some other dependency?   I was trying to look up viable Formats for Textures.

I was trying to find an equivalent for DX RG16_UNormalized (value 35) for OpenGL.   I think the only option might be AlphaLuminance.   

So my question is more regarding "how do you see the full list of OpenGL format options?"   Or maybe there's a link on the internet that shows this.   The links I found showed values that are rejected by UrhoSharp (gives "failed to create texture" errors).   So I'm sorta lost on how to figure out this list.

The "CompressedFormats" enum, for example doesn't seem to include AlphaLuminance.  I just lucked onto finding this in another OpenGL link, and tried it, and it accepts this value without error.

-------------------------

Lys0gen | 2020-12-21 00:15:03 UTC | #2

There's various GL defines (as hexadecimal values, e.g. your 6408 is 0x1908) in these files:

[Source/ThirdParty/SDL/include/SDL_opengles2_gl2.h](https://github.com/urho3d/Urho3D/blob/44220053a992aa574fa0aa6de3f47ef06b339346/Source/ThirdParty/SDL/include/SDL_opengles2_gl2.h)
[Source/ThirdParty/SDL/src/video/khronos/GLES2/gl2.h](https://github.com/urho3d/Urho3D/blob/44220053a992aa574fa0aa6de3f47ef06b339346/Source/ThirdParty/SDL/src/video/khronos/GLES2/gl2.h)
[Source/ThirdParty/SDL/include/SDL_opengl.h](https://github.com/urho3d/Urho3D/blob/44220053a992aa574fa0aa6de3f47ef06b339346/Source/ThirdParty/SDL/include/SDL_opengl.h)

Whether they contain what you're looking for, I don't really know.

-------------------------

najak3d | 2020-12-21 00:14:56 UTC | #3

Brilliant, thank you!

-------------------------

