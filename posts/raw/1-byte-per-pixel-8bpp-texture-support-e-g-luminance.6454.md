najak3d | 2020-10-22 01:38:38 UTC | #1

We're wanting to add a single, 8-bit channel per pixel, such as a "Luminance" map, and so we only need 1 byte per pixel to indicate the "Brightness" of that pixel.

I'm not sure how to do this in Urho3D.  Is it possible?   We're trying to avoid setting a full UInt32 for each pixel (4 bytes instead of 1).

The Texture formats seem to be limited to these values:

public enum CompressedFormat
	{
		None = 0,
		Rgba = 1,
		Dxt1 = 2,
		Dxt3 = 3,
		Dxt5 = 4,
		Etc1 = 5,
		PvrtcRgbN2Bpp = 6,
		PvrtcRgbaN2Bpp = 7,
		PvrtcRgbN4Bpp = 8,
		PvrtcRgbaN4Bpp = 9
	}

Our images are programmatic, such as a geographic Height Map.  We read in the elevations of the area, and then write values to a bitmap.   We'd like to simply write a value of 0..255 for the height, rather than a 32-bit float, or UInt32.     1 byte is enough for us.

Here's an image of our Map app here.   The color coding here is based off Height and Slope.  Currently we're encoding the "slope" component into the RBGA format "Alpha" channel, but we really need to reserve this channel for "alpha" so that we can have transparency.

![image|690x381](upload://1uHmv6kWbMEHRPpvwC96TmPTwSZ.jpeg)

-------------------------

Modanung | 2020-10-22 07:55:12 UTC | #2

If you're running out of channels, maybe you could *pair* two equally sized images?

-------------------------

najak3d | 2020-10-22 15:41:41 UTC | #3

Ideally, we'd like to have just 2 channels per pixels: 
1. 1 Byte - indicates Palette Color (0..255 options) - this indicates "Height/Elevation" at that pixel.
2. 1 Byte - indicates Brightness / Alpha (where  0 = Invisible, 1..255 are fully opaque)

And then send our Pixel shader a 2nd texture of "Palette colors".

In short, we're trying to save on RAM and processing-time (less data makes it faster).

As far as I can tell, there is no way to format a texture to be 1-byte-per-pixel?  Although I suppose we could do something more creative such as "tiling" and have tile #1 use the first two channels, then tile #2 use the 2nd two channels...   So the same texture would be used for 2 tiles.

Maybe that's the answer.  (Texture sharing, and mapping different channels to different tiles.)

-------------------------

SirNate0 | 2020-10-22 18:46:29 UTC | #4

Doesn't Graphics provide several options for this - GetAlphaFormat() and GetLuminanceFormat() for 1Bpp, and then GetLuminanceAlphaFormat() and GetRG16() for 2Bpp? In any case, I would guess (I have no evidence for it) that it would be more efficient to use a 2Bpp texture over 2 separate 1Bpp textures unless you are only going to be modifying one or they are different sizes.

-------------------------

najak3d | 2020-10-22 19:31:13 UTC | #5

[quote="SirNate0, post:4, topic:6454"]
GetLuminanceFormat
[/quote]

Ah shoot, this could be another UrhoSharp limitation on the API.   UrhoSharp only provides "Graphics.GetFormat(CompressedFormatEnum)"... and those enumeration options are shown in my initial post, and doesn't contain a Luminance option.

We may opt for a 4-channel RBGA format, and split it across 2 Renderable Tiles.   Tile #1 will use Channels RG, and Tile #2 will use Channels BA.

-------------------------

Eugene | 2020-10-23 16:07:00 UTC | #7

[quote="najak3d, post:5, topic:6454"]
“Graphics.GetFormat(CompressedFormatEnum)”
[/quote]
1bpp luminance texture is _not_ compressed format.
It should be accessible directly via e.g. `Image::SetSize` (it should take number of components as input)

-------------------------

najak3d | 2020-10-23 16:10:44 UTC | #8

Eugene, I think may be my solution right there, thanks!   UrhoSharp still allows us to set the Texture Format as a "uint", and so we'll just have to do our own logic to determine the "Luminance Format", which appears to be:

D3D9:  50 (L8)
D3D11:  61 (R8_UNORM)
OpenGL: 33321 (R8)

Or if I wanted, looks like I should be able to easily select/create a 2-channel texture (16bpp), and use that as well.

I'll give this a try and let you know how it works out.  THANKS!

-------------------------

Eugene | 2020-10-23 16:14:09 UTC | #9

[quote="najak3d, post:8, topic:6454"]
Or if I wanted, looks like I should be able to easily select/create a 2-channel texture (16bpp), and use that as well.
[/quote]
I _think_ that 1-channel textures are supported as well. You may need to use R component instead of A in shader tho.

-------------------------

najak3d | 2020-10-27 05:32:10 UTC | #10

Eugene, I tried to convert the DiffMap to 2-channel format  (R8G8_UINT), and every channel (RGBA) in the shader from the Sampler turns up as "0".    Is the DiffMap *allowed* to be 2-channel in these shaders?    I didn't see a mapping for "Luminance" in the "samplers.hlsl", but saw options for Specular and Emissive -- both of which seemed to be RGB format for all the shaders that use these.

I see no examples that make use of any 1 or 2 channel textures.  Can you point me to some example code that does this?   (all the examples I see use RGB or RGBA formatted textures)

-------------------------

Eugene | 2020-10-27 07:43:56 UTC | #11

Shaders don’t care about number of channels. Although I want to see how you create 2-channel texture on code side.

-------------------------

najak3d | 2020-10-27 18:10:21 UTC | #12

This is how I create the texture:
_textureFormat = 50;   // equiv to:  DXGI_FORMAT_R8G8_UINT
_texture.SetSize(size.Width, size.Height, _textureFormat, TextureUsage.Static);
_texture.SetData(0, 0, 0, size.Width, size.Height, (void*)bitmap.pBits);

This code works fine for 4-channel RGBA format, but not for 2-channel.   _texture is a Texture2D.

For 2-channel, the shader just shows blank.

The Pixel Shader looks like this:
void PS(
    float2 oTexCoord : TEXCOORD0,
    float4 iColor : COLOR0,
    out float4 oColor : OUTCOLOR0)
{
    float4 diffColor = iColor * Sample2D(DiffMap, oTexCoord).rgba;
    diffColor.a = 1.0;
   oColor = diffColor;
}

Channels R & G should have non-zero data... but all I see is "opaque BLACK" (Color 0,0,0,1)

====
My concern is that Urho3D isn't just "normal shader logic" since we use some built in include files, like "sampling.hlsl" which defines "DiffMap".    I wasn't sure if Urho3D somehow demands that DiffMap always be a 4-channel texture.

-------------------------

najak3d | 2020-10-27 18:14:21 UTC | #13

NOTE -- it's working if I change the format from 50 to 49, which is R8G8_UNORM.

So we're all set now, it seems.

-------------------------

