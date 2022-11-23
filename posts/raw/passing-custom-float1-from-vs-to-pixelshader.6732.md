najak3d | 2021-02-26 20:24:47 UTC | #1

I'm trying to pass a Float1 (singe float value) from Vertex Shader to Pixel Shader.   Looks like in HLSL I have to define a valid "semantic" for this to work.

So I chose SV_CLIPDISTANCE, but apparently this semantic is hard-wired to discard all pixels where this goes negative.  So I can't use it to pass a negative value to the Pixel Shader.

What semantic should I use for a "user custom" value?  I can't find a location in the Urho3D code which defines the available Custom/User semantics (ones not used for other purposes already).

Here is my HLSL Code:

void VS(float4 iPos : POSITION,
    float2 iTexCoord : TEXCOORD0, 
    out float2 oTexCoord : TEXCOORD0,
    out float oCustomValue : SV_CLIPDISTANCE0,
    out float4 oPos : OUTPOSITION)
....

and

void PS(
    float2 oTexCoord : TEXCOORD0,
    float iCustomValue : SV_CLIPDISTANCE0,
    out float4 oColor : OUTCOLOR0)
....



Whenever my "oCustomValue" goes negative, the pixel disappears (guessing because SV_CLIPDISTANCE0 is hardwired to behave this way).

-------------------------

Eugene | 2021-02-26 21:15:39 UTC | #2

[quote="najak3d, post:1, topic:6732"]
So I chose SV_CLIPDISTANCE
[/quote]
SV literally means "System Value", i.e. "value used by GPU itself".
Just used TEXCOORD1, or whatever index is free

-------------------------

najak3d | 2021-02-26 21:16:41 UTC | #3

Thanks!  I didn't realize I could use TEXCOORD1 as a Float1.  I figured it was only allowed to be used for Float2.   Using TEXCOORD1 fixed the issue entirely.

-------------------------

