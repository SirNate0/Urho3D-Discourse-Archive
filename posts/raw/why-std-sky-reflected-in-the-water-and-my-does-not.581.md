codingmonkey | 2017-06-29 07:59:56 UTC | #1

i record video demo of this problem.

http://www.youtube.com/watch?v=YFDy6Bf-VWc&feature=youtu.be

standart sky doom reflected in water but my sky sphere does not.
why?

-------------------------

hdunderscore | 2017-01-02 01:01:31 UTC | #2

Interesting that it works in the editor.
[ul][li]When you open the console in your game (f1), or look at the log, are there errors loading resources?[/li]
[li]Do you have a diffuse texture on the water material ?[/li][/ul]

-------------------------

codingmonkey | 2017-01-02 01:01:31 UTC | #3

>Interesting that it works in the editor

in editor water always reflect random texture, just in that time it reflect right texture )

>?Do you have a diffuse texture on the water material ?
yes, i'm created diff texure manualy in c++ code

[code]
void GameMain::WaterSetup(Urho3D::String waterNodeName) 
{
	ResourceCache* cache = GetSubsystem<ResourceCache>();
	Graphics* graphics = GetSubsystem<Graphics>();

	// ??????? ????? ???? ?? ???????????? ?????? ? ???????? ?? ???-?????
	Node* waterNode_ = scene_->GetChild("waterNode",true);
	StaticModel* waterMesh = waterNode_->GetComponent<StaticModel>();
	// ???????? ???? ???-????? ????? ???????? ?? ?? ?????? ??????? ????? ???????? 
	waterMesh->SetViewMask(0x80000000);

	// ????????? ? ????. ?????????
	//???????? ????????? ???? ??? ??????????
	waterPlane_ = Plane(waterNode_->GetWorldRotation() * Vector3(0.0f, 1.0f, 0.0f), waterNode_->GetWorldPosition()); 
	// ? ???? ????????????
	waterClipPlane_ = Plane(waterNode_->GetWorldRotation() * Vector3(0.0f, 1.0f, 0.0f), waterNode_->GetWorldPosition() - Vector3(0.0f, 0.1f, 0.0f));

	// ???????? ?????? ??? ?????????
	// ??? ????? ????? ???? ????? ????????? ????????? ? ???????, ??? ? ??????? ?????? ????.
	reflectionCameraNode_ = cameraNode_->CreateChild();
	Camera* reflectionCamera = reflectionCameraNode_->CreateComponent<Camera>();

	reflectionCamera->SetFarClip(1000.0);
	reflectionCamera->SetFov(75.0f);
	reflectionCamera->SetViewMask(0x7fffffff); // Hide objects with only bit 31 in the viewmask (the water plane)
	reflectionCamera->SetAutoAspectRatio(false);
	reflectionCamera->SetUseReflection(true);
	reflectionCamera->SetReflectionPlane(waterPlane_);
	reflectionCamera->SetUseClipping(true); // Enable clipping of geometry behind water plane
	reflectionCamera->SetClipPlane(waterClipPlane_);
	// The water reflection texture is rectangular. Set reflection camera aspect ratio to match
	reflectionCamera->SetAspectRatio((float)graphics->GetWidth() / (float)graphics->GetHeight());


	// C??????? ???????? ? ???????? ?? ??? ??? ?????????, ?????????? ???????? ??? ????? ????? ? ????????? ???? 
	int texSize = 2048;
	SharedPtr<Texture2D> renderTexture(new Texture2D(context_));
	renderTexture->SetSize(texSize, texSize, Graphics::GetRGBFormat(), TEXTURE_RENDERTARGET);
	renderTexture->SetFilterMode(FILTER_BILINEAR);
	RenderSurface* surface = renderTexture->GetRenderSurface();
	SharedPtr<Viewport> rttViewport(new Viewport(context_, scene_, reflectionCamera));
	surface->SetViewport(0, rttViewport);
	Material* waterMat = cache->GetResource<Material>("Materials/Water.xml");
	waterMat->SetTexture(TU_DIFFUSE, renderTexture);
}
[/code]

I believe this is due to
because i'm using the usual great texture and not use cubemap for my sky sphere, besides i'm manualy fix( hack) constant bias = 1 in material for my sky. 

But how can I use on cubemap my sphere sky mesh ?)  

Moreover I do not need doom-like sky. 
i needed the lower part of the sphere too 
because my land in air and sky on the bottom of the world, should be seen too.

May simply try to use cube mesh ?)
and to hell with it, I bake for him sky cubemap texture in a blender )

-------------------------

codingmonkey | 2017-06-29 07:59:46 UTC | #4

I came up with an easier way, I copied the standard technique skybox and renamed it to skysphere and in file i'm changed the name of the shader to skysphere.
then i found the skybox.hlsl and copied it, then renamed to skysphere.hlsl and corrected for my sphere
like this:

skysphere.hlsl
[code]#include "Uniforms.hlsl"
#include "Samplers.hlsl"
#include "Transform.hlsl"

void VS(float4 iPos : POSITION, float2 iTexCoord: TEXCOORD0,
    out float4 oPos : POSITION,
    out float2 oTexCoord : TEXCOORD0)
{
    float4x3 modelMatrix = iModelMatrix;
    float3 worldPos = GetWorldPos(modelMatrix);
    oPos = GetClipPos(worldPos);
    
    oPos.z = oPos.w;
    oTexCoord = iTexCoord;
}

void PS(float3 iTexCoord : TEXCOORD0,
    out float4 oColor : COLOR0)
{
    oColor = cMatDiffColor * tex2D(sDiffMap, iTexCoord);
}[/code]

now it working like as it should be

-------------------------

