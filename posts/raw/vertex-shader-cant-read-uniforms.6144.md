najak3d | 2020-05-06 22:23:20 UTC | #1

We have a simple custom shader for drawing lines on a flat map.  Each line layer has a different fixed Y value, so that it'll appear "on top" of other layers (this is how we z-order).  So we want to set the "Y" position value inside of a Uniform value.

The Uniform Value can be read just fine from the Pixel Shader, but from the Vertex Shader, it's treated the value as "always default/zero".

Here is our HLSL:

#include "Uniforms.hlsl"
#include "Transform.hlsl"

uniform float cYPos;

void VS(float4 iPos : POSITION,
    out float4 oPos : OUTPOSITION)
{
    iPos.y = cYPos; // <<<<<<<<<<<<<< THIS IS ALWAYS ZERO!!!!

    float4x3 modelMatrix = iModelMatrix;
    float3 worldPos = GetWorldPos(modelMatrix);
    oPos = GetClipPos(worldPos);
}

void PS(
    out float4 oColor : OUTCOLOR0)
{
    float color = 0.05 * cYPos; // <<<<<<<<<<<<< Here it reads YPos just fine
    oColor = float4(color, color, color, 1.0);
}

==
We are using UrhoSharp, to set the Shader parameter as follows:

			float yPos = 1f;
			foreach (var layer in _lineLayers.Values)
			{
				layer.Material.SetShaderParameter("YPos", yPos);
				yPos += 1f;
			}

I have tried reading the YPos, and it is always Zero within the VertexShader, while works fine for the PixelShader.

The Urho Samples do not have any examples where a Vertex Shader accesses the Uniforms (that I can find), to prove that this works.

Help would be greatly appreciated here.  Has anyone else gotten Vertex Shaders to access the Uniform values?

-------------------------

Eugene | 2020-05-06 21:50:41 UTC | #2

I recommend using constant (aka uniform) buffers for DX11 API.
Orphan parameters were never really tested and, looking at the code, I don't see how they can work (so they probably cannot).

-------------------------

najak3d | 2020-05-06 22:30:22 UTC | #3

So we have 10 line layers, each uses the same shader, but with a different Uniform setting for YPos, so that each layer will draw to a different Y-positioned flat/horizontal plane (they are stacked).   So I add these as 10 instances of dynamic Geometry. 

If I use a Constant DX buffer to store an array of YPos[], then how does each layer know it's "layer index"?   I need a way to tell ALL VERTICES for a single layer "You are Index 1" or "Your YPosition is 1.0".    I'm trying to avoid passing in "YPos = 1.0" to all N vertices.

-------------------------

najak3d | 2020-05-06 22:46:15 UTC | #4

In order to take advantage of this efficiency, it looks like I'll have yet another hurdle to clear, in that "POSITION" always comes in as "float4", but I'm wanting to ONLY pass in the XZ coordinates (per vertex), and skip the "Y" component.

Will Urho permit me to define Position as a "Vector2" in the Vertex Buffer? (saving 4 bytes per vertex).

I'm also wanting to pack in ONLY the "U" coordinate (of a UV TEXCOORD), and omit the "V" coordinate, so that each vertex will instead only be 12 bytes total:    X, Z, and U.

(we don't need "Y" or "V", assuming I can read the fixed-Y value from the Uniform values)

Before this optimization, we've got 20-bytes per vertex;  we're trying to reduce this to 12 bytes.   It technically could be 8 bytes + 1 bit (65 bits).   The "U" coordinate is EITHER 0 or 1, nothing in between.  

We could encode the "U" coordinate into a single bit of the X or Z coordinates and make this be 8 bytes per vertex.

For our next step, we'd be happy just to reduce 20 bytes to 12 bytes.

-------------------------

najak3d | 2020-05-07 12:27:18 UTC | #5

BTW, although the issue remains that Vertex Shaders can't see Uniforms (a big bug, IMO), I am going to resolve our specific problem simply by changing the Node Position Y value for each layer, which works just fine.  And to keep it simple (yet kludgy), we're going to pack the "U" value into the Vertex "Y" value, so that we'll achieve our 12 bytes per vertex goal.

-------------------------

