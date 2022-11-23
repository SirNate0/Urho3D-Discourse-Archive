najak3d | 2021-03-21 20:21:52 UTC | #1

For our Map Grid shader, in the vertex shader we are sampling the Height/Normal from the DiffMap, as follows:
===
[code]
Texture2D tDiffMap : register(t0);
SamplerState sDiffMap : register(s0);

void VS(....)
{
    ....
    float2 diffVal = Sample2DLod0(DiffMap, iTexCoord).rg;
    // 'r' component is our "elevation value"
    // 'g' component encodes our normal - used for crude shadowing
}
[/code]
===
And it is working on Windows (haven't tested Android/iOS mobile).   In order to avoid 'interpolation' between adjacent pixel values, we offset our iTexCoord value with "half Pixel size" to guarantee we're sampling in the exact center of each pixel - -and so there is no interpolation.  This is a bit awkward, but works.

I have seen talk of a alternate method called "texelFetch" which may be more suited for the Vertex Shader, and grabbing pixel data without interpolation.

We need this to work on Windows, UWP, iOS, and Android alike.   It's OK if it only runs on newer mobile devices (2015 or newer).

My Questions are:
1. Does our current method 'Sample2DLod0' work for our targeted platforms? (e.g. non-old mobile)
2. Is the 'texelFetch' method a better choice?  And if so, what are the benefits?  (e.g. runs faster?)

I was seeing talk from 2013 about some mobile devices not supporting texture sampling from the Vertex Shader.  I assume this is no longer an issue, yes?

-------------------------

JSandusky | 2021-03-22 08:21:36 UTC | #2

`texelFetch` will not filter. It's the best choice when appropriate. On GL (and on DX in Urho because of how samplers are implemented) it's also your only option if you need to extract unfiltered data from a filtered texture, such as when packing data into channels or using the sign-bit as an extra bool where filtering will mung those values.

WebGL2 and GLES3 capable hardware have vertex texture support. It isn't required for GLES2 but will likely be there on anything reasonable. For Apple it's devices that shipped with iOS 7 and above IIRC, Samsung is S6 and above. Save some goats to sacrifice if you need to target hardware east of Greece where there's more device diversity per year than the entire lifetime of smartphones in the west.

-------------------------

najak3d | 2021-03-22 08:27:14 UTC | #3

[quote="najak3d, post:1, topic:6765"]
`float2 diffVal = Sample2DLod0(DiffMap, iTexCoord).rg;`
[/quote]

BTW, I am using this now inside my Vertex Shader, and it's accurate, no interpolation/filtering.  I seem to be getting the raw texture data.   This was accomplished by ensuring my texCoord values sample the "exact center" of each pixel. (using half-pixel-size offsets for each -- e.g. to get pixel 0,0 on a texture size 256, I sample texCoord (1/512, 1/512), rather than 0,0,  and for 1,1 I sample (3/512, 3/512) and so on, up to 255, 255 sampling at (511/512, 511/512) to get the last pixel's center.

No matter, I think I'll be switching it to "texelFetch", because it's more appropriate for this task. (and I'm guessing it probably runs faster, since it has no logic to "sample 4 pixels and interpolate/blend").

-------------------------

