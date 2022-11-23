najak3d | 2021-07-19 07:32:47 UTC | #1

Today, we were experiencing some crazy behavior in Shader, seeing the uniform variables being overwritten by some outside force.     It would work for a while, but then would start messing up reliably after about 30 seconds of panning around our map.

After trying everything else, we finally figured out that changing "register(b6)" to "register(b5)" worked, miraculously (and we see no other side-effects yet from this).

#ifdef COMPILEPS
cbuffer CustomPS : register(b5)  <== changing this from (b6) to (b5) FIXES the issue.
{
    bool cShowRelief;   <== this parameter alone GOES HAYWIRE, sporadically. (gets overwritten?)
    float cAlpha;
    float cOwnshipAltitudeFt;
    float cAltThreshWarn;
    float cAltThreshDanger;
}
#endif

Questions:
1. Is there any reason why we can't/shouldn't use register b5?
2. Does anyone have any clues as to why register b6 could have some sort of cross-talk/overwriting occurring?

-------------------------

najak3d | 2021-07-19 07:32:11 UTC | #2

Update, the following change ALSO fixes our issue, combining the final two uniforms into a float2, as follows:

#ifdef COMPILEPS
cbuffer CustomPS : register(b6)
{
    bool cShowRelief;
    float cAlpha;
    float cOwnshipAltitudeFt;
    float2 cThreshHolds;     <=== combined cAltThreshWarn/Danger into a float2, also fixes this.
}
#endif

This is making no sense to us.   Anyone got any clues?

Luckily this final workaround does work, so we're going to "go with it".

-------------------------

Eugene | 2021-07-19 09:10:59 UTC | #3

If we ignore a possibility of driver bug messing up with packing bool into uniform buffer... I don't know. Perhaps Urho messes up parsing such layout, I dunno.
It's hard to tell without actual GPU debugging (I prefer Visual Studio debugger, which is still quite trash)

Personally I would have just avoided using bool uniforms alltogether. You have floats and integers.

-------------------------

najak3d | 2022-03-09 07:18:28 UTC | #4

FYI -- I encountered this same behavior again tonight -- only impacting HLSL.   One Shader's parameters overwriting another's.   This time, I'm not making any sense of it.     One way to fix it is to have a single fake float constant defined (that I don't even use) -- and for some reason this clears up the issue.

It works fine in GLSL.   After hours of playing around with this -- still no real progress, other than figuring out a kludge that seem "seems to magically work" for this one instance.

Here's the shader that is failing:
```
#ifdef COMPILEPS
cbuffer CustomPS : register(b6)
{
    uniform float4 cColor;
    //uniform float cBOGUSPARAMETER; // Adding this, fixes the issue, otherwise "cColor" is overridden by crosstalk from another shader.
}
#endif

void PS(
    float2 oTexCoord : TEXCOORD0,
    out float4 oColor : OUTCOLOR0)
{
    float4 diffColor = cColor * Sample2D(DiffMap, oTexCoord).bgra;
    oColor = diffColor;
}
```

Does anyone have any clues as to what might be causing this?   It seems like an Urho bug to me, at this point.

-------------------------

najak3d | 2022-03-09 19:35:51 UTC | #5

I spent another 4 hours trying to find the pattern to this -- and turns out it's worse than I thought.   I could make this error happen in a great many situations -- all HLSL.   The fix to issues were all nonsense stuff (like above) -- but at least these kludges work.   And so we can move on.

This bug exists in UrhoSharp, not Urho3D.NET -- because Urho3D.NET uses OpenGL on Windows, and so avoids usage of HLSL entirely.   And so I'm going to just live with the silly workaround, and we're glad that this workaround actually works.

-------------------------

