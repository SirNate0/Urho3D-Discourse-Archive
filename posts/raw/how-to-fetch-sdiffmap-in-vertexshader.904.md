codingmonkey | 2017-01-02 01:03:58 UTC | #1

Hi folks!
Today i'm trying write some vertex shader and it must fetch the diffmap for vertex displacement
i'm copy the libSolid.hlsl and doing some fixes into it.
the first of all i try to find how dx9 doing fetch from textures in vertex shader and find this tut
[http.developer.nvidia.com/GPUGem ... ter18.html](http://http.developer.nvidia.com/GPUGems2/gpugems2_chapter18.html) 
i find this  
[code]float4 main(float4 position : POSITION,
  uniform sampler2D tex0,
[/code]
so i decide just add sampler2D sDiffMap : COLOR for VS in parameters
[code]void VS(float4 iPos : POSITION,
    float3 iNormal : NORMAL,
    float2 iTexCoord : TEXCOORD0,
    sampler2D sDiffMap : COLOR,
    #if defined(LIGHTMAP) || defined(AO)
        float2 iTexCoord2 : TEXCOORD1,
    #endif
    #ifdef NORMALMAP
        float4 iTangent : TANGENT,
    #endif
    #ifdef SKINNED
        float4 iBlendWeights : BLENDWEIGHT,
        int4 iBlendIndices : BLENDINDICES,
    #endif[/code]

vertex displace
[code]
    float4x3 modelMatrix = iModelMatrix;
    float3 dcolor = tex2Dlod (sDiffMap, float4(iTexCoord.xy, 0,0));
    float displace = (dcolor.r * cChannelFactor.r + dcolor.g * cChannelFactor.g + dcolor.b * cChannelFactor.b );
    float3 dispPos = iPos.xyz + iNormal.xyz * displace * cDisplacement;   
     
    float3 worldPos = mul(dispPos, modelMatrix);
    oPos = GetClipPos(worldPos);
    oNormal = GetWorldNormal(modelMatrix);  
    oWorldPos = float4(worldPos, GetDepth(oPos));
[/code]

also i'm add some uniforms for vs and ps in uniforms.hlsl

[code]uniform float4 cChannelFactor;
uniform float cDisplacement;
uniform float2 cRange;[/code]

but i'm got an editor's crush then trying to open my scene, with object that have this custom draw tech.

i guess there not so simple way to doing fetch in dx9 ?

-------------------------

cadaver | 2017-01-02 01:03:59 UTC | #2

I can confirm that I see odd things happening when I attempt to do vertex texture fetch with D3D9. This will require further investigation, but for now (without debugging/fixing the problem deeper yourself) you can assume you can't really do working VTF.

I tried the following modified TerrainBlend shader, which is supposed to sample the weight map in VS and bring that color over for the PS to use, but the result was that only a single quad of the terrain would get rendered, and it would move incorrectly along with the camera position.

[code]
#include "Uniforms.hlsl"
#include "Samplers.hlsl"
#include "Transform.hlsl"
#include "ScreenPos.hlsl"
#include "Lighting.hlsl"
#include "Fog.hlsl"

sampler2D sWeightMap0 : register(S0);
sampler2D sDetailMap1 : register(S1);
sampler2D sDetailMap2 : register(S2);
sampler2D sDetailMap3 : register(S3);

uniform float2 cDetailTiling;

void VS(float4 iPos : POSITION,
    float3 iNormal : NORMAL,
    float2 iTexCoord : TEXCOORD0,
    out float4 oColor: TEXCOORD0,
    out float4 oPos : POSITION)
{
    float4x3 modelMatrix = iModelMatrix;
    float3 worldPos = GetWorldPos(modelMatrix);
    float2 texCoord = GetTexCoord(iTexCoord);

    oColor = tex2Dlod(sWeightMap0, float4(texCoord, 0.0, 0.0));
    oPos = GetClipPos(worldPos);
}

void PS(float4 iColor : TEXCOORD0,
    out float4 oColor : COLOR0)
{
    oColor = iColor;
}
[/code]

-------------------------

codingmonkey | 2017-01-02 01:03:59 UTC | #3

thanks, now i even see something without editor's crash )
after adding: sampler2D sDispMap : register(S0); to shader head
but also see strange these bugs if i move camera

-------------------------

cadaver | 2017-01-02 01:03:59 UTC | #4

One possibility is that using vertex fetch somehow throws off the shader analysis that Urho does with MojoShader, in which case Urho no longer knows how to stuff the correct shader constants into registers. In this case a potential fix would be to update MojoShader.

-------------------------

codingmonkey | 2017-01-02 01:03:59 UTC | #5

well i'm update the mojoShader from this repo [github.com/flibitijibibo/MojoShader](https://github.com/flibitijibibo/MojoShader)
but it still have a some problem with strange deforms when the camera moves

lately i found this note
[robertwrose.com/2005/05/vert ... notes.html](http://www.robertwrose.com/2005/05/vertex-texture-sampling-notes.html)
and i guess that need other format of texture with f32 for each channel for vector
or this issue real metter only for if you doing write from vertex shader to texture?

i found something 
float4 dispPos = iPos.xyzw;
befor i use float3

also i'm check that simple displace by normal works well
    float4 dispPos = float4(iPos.xyz + iNormal.xyz * cDisplacement, iPos.w);
    float3 worldPos = mul(dispPos, modelMatrix);

[url=http://savepic.su/5307617.htm][img]http://savepic.su/5307617m.png[/img][/url]

-------------------------

codingmonkey | 2017-01-02 01:03:59 UTC | #6

i found what in this topic [gamedev.net/topic/631832-ver ... etch-sm30/](http://www.gamedev.net/topic/631832-vertex-texture-fetch-sm30/)
Tispe solve his problem with one thing, changed code:
pGraphicsDevice->GetDevice()->SetTexture(1, pAnimationTexture);
Changed to:
pGraphicsDevice->GetDevice()->SetTexture(D3DVERTEXTEXTURESAMPLER0, pAnimationTexture);

-------------------------

cadaver | 2017-01-02 01:03:59 UTC | #7

Ok, I believe this needs some thinking to support properly, because so far the texture units have been assumed to be pixel shader only, or shared between the stages (OpenGL works that way.)

-------------------------

codingmonkey | 2017-01-02 01:03:59 UTC | #8

i'm made some addings and fixes to 
D3DTexture.h
[code]
class URHO3D_API Texture : public Resource, public GPUObject
{
public:
    /// Construct.
    Texture(Context* context);
    /// Destruct.
    virtual ~Texture();
    
    unsigned VTF_SAMPLER;
    
    /// Set number of requested mip levels. Needs to be called before setting size.
    void SetNumLevels(unsigned levels);
[/code]

and to D3DGraphics.cpp in proc SetTexture()
[code]
    if (texture != textures_[index])
    {
        if (texture)
			if (texture->VTF_SAMPLER == 0)
				impl_->device_->SetTexture(index, (IDirect3DBaseTexture9*)texture->GetGPUObject());
			else
				impl_->device_->SetTexture(texture->VTF_SAMPLER, (IDirect3DBaseTexture9*)texture->GetGPUObject());
        else
            impl_->device_->SetTexture(index, 0);
      
		textures_[index] = texture;
	}
[/code]

then build engine with this changes

in my test project i'm manualy get texture from material and set texture->VTF_SAMPLER to D3DVERTEXTEXTURESAMPLERn

[code]
		StaticModel* model = node->GetComponent<StaticModel>();
		Material* mat = model->GetMaterial(0);
		Texture* tex = mat->GetTexture(TU_NORMAL);

#define D3DDMAPSAMPLER 256
#define D3DVERTEXTEXTURESAMPLER0 (D3DDMAPSAMPLER+1)
#define D3DVERTEXTEXTURESAMPLER1 (D3DDMAPSAMPLER+2)
#define D3DVERTEXTEXTURESAMPLER2 (D3DDMAPSAMPLER+3)
#define D3DVERTEXTEXTURESAMPLER3 (D3DDMAPSAMPLER+4)

		tex->VTF_SAMPLER = D3DVERTEXTEXTURESAMPLER1;
		mat->SetTexture(TU_NORMAL, tex);
[/code]

shader code
sampler2D sDispMap : register(S1); // normal sampler store dispalacemap

float4x3 modelMatrix = iModelMatrix;
float3 dcolor = tex2Dlod(sDispMap, float4(iTexCoord.xy, 0,0));
    
float displace = (dcolor.r * cChannelFactor.r + dcolor.g * cChannelFactor.g + dcolor.b * cChannelFactor.b );
float4 dispPos = float4(iPos.xyz + iNormal.xyz * displace * cDisplacement, iPos.w);
//float4 dispPos = float4(iPos.xyz + iNormal.xyz * cDisplacement, iPos.w); // this displace works fine
    
float3 worldPos = mul(dispPos, modelMatrix);

but it still have same problems. i guess that this not enough. 
maybe also need to check texture format somehow, that supported VTF

in the mirror the displaced sphere looks more realistic sometimes
[video]http://youtu.be/0foxxAmJkfE[/video]

add:
found this topic 
[msdn.microsoft.com/en-us/librar ... 48(v=vs.85](https://msdn.microsoft.com/en-us/library/windows/desktop/bb219748(v=vs.85)).aspx
with this tip: 
[quote]?Not all formats can be used as displacement maps but only those that support the D3DUSAGE_DMAP. The application can query that with the CheckDeviceFormat CheckDeviceFormat.
[/quote] 
i think that need somehow enforce the texture to use this flag when it create

-------------------------

codingmonkey | 2017-01-02 01:04:02 UTC | #9

Today i'm add this query proc. it must return an vector<unsigned> of supported formats that works with VTF on my gpu.
[code]
		SharedPtr<Texture2D> t = SharedPtr<Texture2D>(new Texture2D(context_));
		File textureFile(context_, GetSubsystem<FileSystem>()->GetProgramDir() + "Data/Textures/rgb-compose.png",FILE_READ);
		t->vtf = D3DVERTEXTEXTURESAMPLER0;
		t->Load(textureFile);		
		Vector<unsigned> vv;
		t->FindSupportedVertexTextureFormat(vv);
[/code]

result's are

    D3DFMT_A8R8G8B8             = 21,
    D3DFMT_R16F                 = 111,
    D3DFMT_G16R16F              = 112,
    D3DFMT_A16B16G16R16F        = 113,
    D3DFMT_R32F                 = 114,
    D3DFMT_G32R32F              = 115,
    D3DFMT_A32B32G32R32F        = 116,


the proc that do query for test i'm placed just in the texture2D class :slight_smile:
[code]
unsigned Texture2D :: FindSupportedVertexTextureFormat(Vector<unsigned>& formats) 
{
	IDirect3DDevice9* device = graphics_->GetImpl()->GetDevice();
	usage_ = D3DUSAGE_QUERY_VERTEXTEXTURE;
	
	for (unsigned fc = D3DFMT_R8G8B8; fc < 120; fc++) {
		if (graphics_->GetImpl()->CheckFormatSupport((D3DFORMAT)fc, usage_, D3DRTYPE_TEXTURE)) 
		{
			formats.Push(fc);
		}
	}

	return 0;
}
[/code]

and now i'm trying to find the way to store my texture(1024*1024 png with 24 bit's) in one of format that support Vertex Fetch.

add:
find some old topic there folks had an same problems: [monogame.codeplex.com/discussions/428213](https://monogame.codeplex.com/discussions/428213) 
as you say before the main problem can be in MojoShader.
what he do in the engine, that functionality ?
can be engine live without it ?
or maybe may do so that under Win Platform shaders compiled with diretly with directx D3DCompile() ?

-------------------------

codingmonkey | 2017-01-02 01:04:15 UTC | #10

well, today i'm trying do this vertex texture fetch on gl-renderer and it's work's on gl.

[video]http://www.youtube.com/watch?v=N_qvbcb0mVs[/video]

change model from sphere to icosphere (with subdiv apply) also set smooth normal for geometry
new 
[url=http://savepic.su/5424860.htm][img]http://savepic.su/5424860m.png[/img][/url]

-------------------------

najak3d | 2021-03-02 02:06:39 UTC | #11

I'm not sure how this got concluded, for the rest of us.

As of now, does Urho3D support Sample2D (or texture2D) from the Vertex Shader?  It SURE WOULD BE NICE.

For a terrain heightmap, it's far more efficient to just encode a HeightMap into a Texture2D/image, and then inside the Vertex Shader, use this heightmap to offset the Y value.   Then you can employ a static Grid-mesh and apply a dynamic XZ offset to correctly position it horizontally. 

The alternative requires us to duplicate the Vertex Buffer, which is 20 bytes per vertex, instead of only 4-bytes per vertex for the HeightMap Image approach.   (20% of the byte size in GPU - plus it's easier on the CPU building the heightmap).

-------------------------

JSandusky | 2021-03-02 02:23:40 UTC | #12

Should work out of the box. You need to add the texture and sampler to the VS code. The default shaders are setup so that if `COMPILEPS` isn't defined (compiling a pixel shader) then there are no textures/samplers being defined, so you have to define them yourself (or fiddle the master shaders) and use the appropriate register/name for the texture you wish to see (See `Samplers.glsl/hlsl`).

D3D11 goes out of its way to always set them to be available. I can't recall what D3D9 does there.

In OpenGL the driver manages it based on what the compiled program does.

-------------------------

JTippetts1 | 2021-03-02 02:56:16 UTC | #13

A couple years ago I did a [little experiment](https://github.com/JTippetts/Urho3DGrassTest) with a grass/vegetation shader that used a texture fetch in the VS. It pretty much does work out of the box as @JSandusky said. One potential gotcha in my case was culling, since the vertex shader displacement would push the vertices beyond the 'natural' bounding box so the meshes were getting culled. Had to work around that a little bit. Also, remember that you have to specify the mip level in the texture fetch call, since the vertex shader doesn't have any of the info needed to make that determination. For example, in GLSL you use textureLod(tex,uv,miplevel). HLSL is probably similar.

-------------------------

najak3d | 2021-03-02 03:02:40 UTC | #14

I created a new/fresh topic, since this one is old and I can't really mark "solution".

Here is the new thread.  For me, it's not working out-of-box.   If you can go to the new thread and tell me where I went wrong, that would be great. 

[https://discourse.urho3d.io/t/how-to-sample-texture2d-from-vertexshader/6740](https://discourse.urho3d.io/t/how-to-sample-texture2d-from-vertexshader/6740)

-------------------------

JSandusky | 2021-03-02 03:06:39 UTC | #15

Yeah, has to be either Load, SampleLevel, or SampleGrad. 

There's a few more available in a few cases for Gather/SampleCmpLevelZero/etc but Urho defaults to `vs_4_0` so you can't use those.

MSDN D3D11 docs give you a table at the bottom for all of the Texture/Buffer objects that mark which stages which function is available in. Only a few of them omit it (SampleCmpLevelZero).

-------------------------

