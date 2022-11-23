throwawayerino | 2020-04-12 18:34:25 UTC | #1

```error X3004: undeclared identifier 'iModelMatrix'```
Isn't it supposed to be a global variable?

-------------------------

SirNate0 | 2020-04-12 20:03:01 UTC | #2

Did you include the necessary headers and set the necessary defines? (Not sure if both of those are a possible problem for your specific issue, but it seems likely to be that one of them is there cause)

-------------------------

SamFGD | 2020-04-12 21:40:56 UTC | #3

iModelMatrix is defined in Transform.hlsl/glsl and it can only be accessed in the vertex shader because of COMPILEVS.

-------------------------

throwawayerino | 2020-04-13 11:38:08 UTC | #4

Turns out putting the actual code at the top of the file and removing the comments solved it? Pretty weird but at least it's working now

-------------------------

throwawayerino | 2020-04-13 12:00:48 UTC | #5

Now it's complaining about iNormal.

-------------------------

Eugene | 2020-04-13 12:10:09 UTC | #6

Without actual shader code there's nothing we can do.

-------------------------

throwawayerino | 2020-04-13 12:32:19 UTC | #7

Problem is in VS(), the GetWorldNormal
``` #include "Uniforms.hlsl"
#include "Transform.hlsl"

#ifdef COMPILEVS
uniform float cOutlineWidth = 0.01;
#endif

#ifdef COMPILEPS
uniform float4 cOutlineColor = float4(1.0, 1.0, 1.0, 1.0);
#endif

void VS(float4 iPos : POSITION,
	out float2 oTexCoord : TEXCOORD0,
	out float2 oScreenPos : TEXCOORD1,
	out float4 oPos : OUTPOSITION)
{
	float4x3 modelMatrix = iModelMatrix;
	float3 worldPos = GetWorldPos(modelMatrix);
	float3 vNormal = GetWorldNormal(modelMatrix);
// Scale along normal
	worldPos += vNormal * cOutlineWidth;
	//gl_Position = GetClipPos(worldPos);
    oPos = GetClipPos(worldPos);

}

void PS(float2 iTexCoord : TEXCOORD0,
	float2 iScreenPos : TEXCOORD1,
	out float4 oColor : SV_Target)
{
	oColor = cOutlineColor.rgba;
}
```

-------------------------

Eugene | 2020-04-13 12:51:48 UTC | #8

Well. You don't pass the normal into shader. So the compiler cannot find it.
You can see how standard shaders pass normal and do the same.

https://github.com/urho3d/Urho3D/blob/master/bin/CoreData/Shaders/HLSL/LitSolid.hlsl#L8-L68

Although I admit that design of shader API in Urho is meh.

-------------------------

throwawayerino | 2020-04-13 12:52:53 UTC | #9

Thanks a lot for the info! I admit the solution was very simple, but it would've been helpful if it was mentioned in the docs.

-------------------------

