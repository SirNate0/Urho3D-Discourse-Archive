najak3d | 2020-12-24 08:02:48 UTC | #1

I need to send a 16-bit value to my GLSL pixel shader, and am expecting it to show up as a Normalized value between 0...1.    But then I should be able to multiply it by 65535 to convert it back to the integer format that I desire.

I'm having bad luck with this.  I'm not sure what the Pixel Buffer format should be for this Texture.

I'm setting Pixel Format to 6406 (Alpha), and 6410 (LuminanceAlpha), 6409 Luminance to try and get something to work.

But nothing seems to be working or even making sense.

For HLSL, I use format R16G16, and it works as expected.  The texture "r" value is actually a 16-bit float, and the 'g' value is also a 16-bit float.   I write my values to it as "ushort" (16-bit int's), and then in the shader am able to convert them back to the 'int' value by multiplying by 65535.  It works like a charm.

But for OpenGL - I can seem to get these other formats to make any sense.  If I can't get this working, I'll have to resort to using RGBA format, and combining two-channels together like this:

int value = (color.r * 65280.0) + (color.g * 255.0);

===
For one shader we only need ONE 16-bit value, and would prefer to have the texture be 16bpp, not 32bpp, to save on RAM.

OpenGL - seems to be our problem-child.

-------------------------

najak3d | 2020-12-24 08:18:06 UTC | #2

I think I may have figured out PART of my own problem here.   I think "LuminanceAlpha" is a 16-bpp texture, where it thinks there are 2 components -- (rgb) and (a).    Where Rgb channels are all derived from the Luminance.   But in this case there are no 16-bit channels.  All Channels are 8-bit.

Is there any better way to send a 16-bit value to a GLSL shader via a texture, aside from awkwardly combining them with a function like:   

int value = (color.r * 65280.0) + (color.a * 255.0)


????

-------------------------

Eugene | 2020-12-24 18:49:38 UTC | #3

[quote="najak3d, post:1, topic:6630"]
I need to send a 16-bit value to my GLSL pixel shader
[/quote]
I don't think GL ES 2 supports it.
![image|578x221](upload://1FnXoDiDt1PvveHzYPBcJX9AEcv.png)

-------------------------

najak3d | 2020-12-24 18:49:33 UTC | #4

OK - so the best I can do, probably, is to select "LuminanceAlpha" as the pixel format, which means it uses a texture that is 16 bpp, with 2 channels, "rgb" and "a".  (where rgb are always the same value).

And I'll have to use the contorted math to combine these two values to create the 16-bit int that I need.

OpenGL appears handicapped compared to DirectX.  It's a shame.  (i.e. OpenGL also doesn't support bitwise operations, which also sucks, because these make it easier to pack information into various bits)    A shame really.

-------------------------

Eugene | 2020-12-24 19:14:50 UTC | #5

Well, GL ES standard is created to be compatible with the broadest scope of hardware.
So it is made as simple as possible. You may look for vendor extensions, but those are seldom used in Urho, only for most necessary things (e.g. depth texture support).

-------------------------

SirNate0 | 2020-12-24 21:46:04 UTC | #6

I'm not certain, but I think regular (desktop) Open GL should support a GL_R16 format, or a GL_R16UI format if you want the integers themselves https://www.khronos.org/opengl/wiki/Image_Format

It looks like GLSL also supports bitwise operations, it just requires integers for them. https://community.khronos.org/t/bitwise-operators-in-glsl/70532

-------------------------

najak3d | 2020-12-24 23:00:11 UTC | #7

SirNate0 - thanks!  I may give bit-wise ops another try in the future.   My first attempt failed miserably, despite me using Integers inside the shader.   I believe it gave me compiler errors.

We only use OpenGL for Android/iOS, never Desktop.  On the desktop, we're using HLSL.   HOWEVER, if we could make UrhoSharp use OpenGL in UWP (Universal Windows Platform), then we'd prefer this, so that we don't have to keep writing two-versions of each shader.

-------------------------

najak3d | 2021-04-05 06:24:39 UTC | #8

@Eugene , we're getting further into our App, and again ran into this obstacle.  This time, we're trying to pack in 2 16-bit channels into a single texture -- first value for "elevation" and 2nd for "Normal Info".

Again, we're trying to avoid the awkward math of:
     int value = (color.r * 65280.0) + (color.a * 255.0)

And would prefer to read this in as a single normalized float value, then multiply by 65535.0.

I see that Open GL ES2 only supports 8-bits per channel MAX.   However, all of the devices we're aiming to support, have Open GL ES 3.0.   We're targeting non-old devices.

Is there a way to enable "OpenGL ES 3.0" mode for Urho3D?  And in so doing, we could then use the Open GL ES 3.0 texture formats? (which permits us to use 16-bits of precision in a channel, similar to HLSL's "R16G16_Normalized" format).   It sure would be nice.

-------------------------

Eugene | 2021-04-05 12:26:49 UTC | #9

[quote="najak3d, post:8, topic:6630"]
Is there a way to enable “OpenGL ES 3.0” mode for Urho3D?
[/quote]
I just looked into the code and I don't see any kind of switch

-------------------------

SirNate0 | 2021-04-05 13:36:48 UTC | #11

There is a pull request that adds GLES3 support:

https://github.com/urho3d/Urho3D/pull/2536

-------------------------

