Bart | 2019-06-30 20:42:54 UTC | #1

Hi All!

I would like to know if you get any idea on optimisation of rendering process when rendering a lot of views. My objective is to create a fisheye camera with 180? FOV (or more). I succeeded doing so using process descibed here:  [url]http://strlen.com/gfxengine/fisheyequake/[/url]. In short, you create 5 cameras instead of one, each 90? FOV and pointing in directions front, left, right, top, bottom (and optionally rear). The cameras originate in single point. Output of these cameras is rendered on sides of TextureCube. Then I sample it from the texture cube in a simple shader and display to output Texture2D. I share the code if anyone finds it useful:

Sample(camera mounted on grill of brown car, 180? FOV):
[img]http://urho.czweb.org/CubeCamera.png[/img]

[details=CubeCamera.h]
```
#pragma once

#include <Urho3D/Container/Str.h>
#include <Urho3D/Core/Context.h>
#include <Urho3D/Graphics/Camera.h>
#include <Urho3D/Graphics/Graphics.h>
#include <Urho3D/Graphics/RenderPath.h>
#include <Urho3D/Graphics/RenderSurface.h>
#include <Urho3D/Graphics/Texture2D.h>
#include <Urho3D/Graphics/TextureCube.h>
#include <Urho3D/Resource/ResourceCache.h>
#include <Urho3D/Resource/XMLFile.h>
#include <Urho3D/Scene/Scene.h>

using namespace Urho3D;

class CubeCamera
{

public:
    /// Construct.
	CubeCamera(Context * context, Scene * scene, Node * parent_node, String name);

	Texture2D * GetOutputTexture();

protected:

private:
	Context * context_;
	String name_;
	Scene * scene_;
	SharedPtr<TextureCube> cubeRenderTex_;
	SharedPtr<Texture2D> cubeResultRenderTex_;
	SharedPtr<Viewport> cubeViewport_;
	SharedPtr<Node> parentNode_;
	SharedPtr<Node> frontCubeCameraNode_;
	SharedPtr<Node> leftCubeCameraNode_;
	SharedPtr<Node> rightCubeCameraNode_;
	SharedPtr<Node> topCubeCameraNode_;
	SharedPtr<Node> bottomCubeCameraNode_;

};
```
[/details]

[details=CubeCamera.cpp]
```
#include <Urho3D/Urho3D.h>

#include "CubeCamera.h"

#define CAM_W 1280
#define CAM_H 1280
#define CAM_FAR_CLIP 100.0f
#define CUBE_SIZE 1280

CubeCamera::CubeCamera(Context * context, Scene * scene, Node * parent_node, String name) :
context_(context),
scene_(scene),
parentNode_(parent_node),
name_(name)
{
	ResourceCache* cache = context->GetSubsystem<ResourceCache>();

	// Create perpendicular cameras with FOV of 90deg
	frontCubeCameraNode_ = parent_node->CreateChild(name + "FrontCubeSide");
	frontCubeCameraNode_->Rotate(Quaternion(0.0f, Vector3::RIGHT), TS_PARENT);
	Camera* frontCubeCamera = frontCubeCameraNode_->CreateComponent<Camera>();
	frontCubeCamera->SetFarClip(CAM_FAR_CLIP);
	frontCubeCamera->SetFov(90.0f);
	leftCubeCameraNode_ = parent_node->CreateChild(name + "LeftCubeSide");
	leftCubeCameraNode_->Rotate(Quaternion(-90.0f, Vector3::UP), TS_PARENT);
	Camera* leftCubeCamera = leftCubeCameraNode_->CreateComponent<Camera>();
	leftCubeCamera->SetFarClip(CAM_FAR_CLIP);
	leftCubeCamera->SetFov(90.0f);
	rightCubeCameraNode_ = parent_node->CreateChild(name + "RightCubeSide");
	rightCubeCameraNode_->Rotate(Quaternion(90.0f, Vector3::UP), TS_PARENT);
	Camera* rightCubeCamera = rightCubeCameraNode_->CreateComponent<Camera>();
	rightCubeCamera->SetFarClip(CAM_FAR_CLIP);
	rightCubeCamera->SetFov(90.0f);
	topCubeCameraNode_ = parent_node->CreateChild(name + "TopCubeSide");
	topCubeCameraNode_->Rotate(Quaternion(-90.0f, Vector3::RIGHT), TS_PARENT);
	topCubeCameraNode_->Rotate(Quaternion(-90.0f, Vector3::FORWARD), TS_LOCAL);
	Camera* topCubeCamera = topCubeCameraNode_->CreateComponent<Camera>();
	topCubeCamera->SetFarClip(CAM_FAR_CLIP);
	topCubeCamera->SetFov(90.0f);
	bottomCubeCameraNode_ = parent_node->CreateChild(name + "BottomCubeSide");
	bottomCubeCameraNode_->Rotate(Quaternion(90.0f, Vector3::RIGHT), TS_PARENT);
	bottomCubeCameraNode_->Rotate(Quaternion(90.0f, Vector3::FORWARD), TS_LOCAL);
	Camera* bottomCubeCamera = bottomCubeCameraNode_->CreateComponent<Camera>();
	bottomCubeCamera->SetFarClip(CAM_FAR_CLIP);
	bottomCubeCamera->SetFov(90.0f);

	// Create cube texture (intermediate render target)
	cubeRenderTex_ = new TextureCube(context);
	cubeRenderTex_->SetSize(CUBE_SIZE, Graphics::GetRGBAFormat(), TEXTURE_RENDERTARGET);
	cubeRenderTex_->SetName(name + "CubeTex");
	cache->AddManualResource(cubeRenderTex_);

	// Create render surfaces on individual sides of the cube texture
	RenderSurface* surface = cubeRenderTex_->GetRenderSurface(CubeMapFace::FACE_POSITIVE_X);
	SharedPtr<Viewport> cubeFrontViewport(new Viewport(context, scene, frontCubeCamera));
	surface->SetViewport(0, cubeFrontViewport);
	surface->SetUpdateMode(SURFACE_UPDATEALWAYS);
	surface = cubeRenderTex_->GetRenderSurface(CubeMapFace::FACE_POSITIVE_Z);
	SharedPtr<Viewport> cubeLeftViewport(new Viewport(context, scene, leftCubeCamera));
	surface->SetViewport(0, cubeLeftViewport);
	surface->SetUpdateMode(SURFACE_UPDATEALWAYS);
	surface = cubeRenderTex_->GetRenderSurface(CubeMapFace::FACE_NEGATIVE_Z);
	SharedPtr<Viewport> cubeRightViewport(new Viewport(context, scene, rightCubeCamera));
	surface->SetViewport(0, cubeRightViewport);
	surface->SetUpdateMode(SURFACE_UPDATEALWAYS);
	surface = cubeRenderTex_->GetRenderSurface(CubeMapFace::FACE_POSITIVE_Y);
	SharedPtr<Viewport> cubeTopViewport(new Viewport(context, scene, topCubeCamera));
	surface->SetViewport(0, cubeTopViewport);
	surface->SetUpdateMode(SURFACE_UPDATEALWAYS);
	surface = cubeRenderTex_->GetRenderSurface(CubeMapFace::FACE_NEGATIVE_Y);
	SharedPtr<Viewport> cubeBottomViewport(new Viewport(context, scene, bottomCubeCamera));
	surface->SetViewport(0, cubeBottomViewport);
	surface->SetUpdateMode(SURFACE_UPDATEALWAYS);

	SharedPtr<RenderPath> cubeRenderPath = cubeFrontViewport->GetRenderPath()->Clone();
	cubeRenderPath->Append(cache->GetResource<XMLFile>("PostProcess/FXAA3.xml"));
	cubeRenderPath->SetEnabled("FXAA3", true);
	
	// Use RenderPath with FXAA3 enabled
	cubeFrontViewport->SetRenderPath(cubeRenderPath);
	cubeLeftViewport->SetRenderPath(cubeRenderPath);
	cubeRightViewport->SetRenderPath(cubeRenderPath);
	cubeTopViewport->SetRenderPath(cubeRenderPath);
	cubeBottomViewport->SetRenderPath(cubeRenderPath);

	// Render result image to single Texture2D
	RenderPathCommand rrpc;
	rrpc.type_ = CMD_QUAD;
	rrpc.tag_ = "FisheyeCube";
	rrpc.vertexShaderName_ = "FisheyeCube";
	rrpc.pixelShaderName_ = "FisheyeCube";
	rrpc.SetOutput(0, "viewport");
	rrpc.SetTextureName(TU_DIFFUSE, name + "CubeTex");

	RenderPath * rrp = new RenderPath();
	rrp->AddCommand(rrpc);

	cubeViewport_ = new Viewport(context_, scene_, frontCubeCameraNode_->GetComponent<Camera>(), rrp);

	cubeResultRenderTex_ = new Texture2D(context_);
	cubeResultRenderTex_->SetSize(CAM_W, CAM_H, Graphics::GetRGBAFormat(), TEXTURE_RENDERTARGET);
	surface = cubeResultRenderTex_->GetRenderSurface();
	surface->SetViewport(0, cubeViewport_);
	surface->SetUpdateMode(SURFACE_UPDATEALWAYS);


}

Texture2D * CubeCamera::GetOutputTexture()
{
	return cubeResultRenderTex_;
}
[/details]

[details=FisheyeCube.hlsl]
```
#include "Uniforms.hlsl"
#include "Samplers.hlsl"
#include "Transform.hlsl"
#include "ScreenPos.hlsl"
#include "Lighting.hlsl"

#define M_PI 3.141592654

void VS(float4 iPos : POSITION,
	out float2 oScreenPos : TEXCOORD0,
	out float4 oPos : OUTPOSITION)
{
	float4x3 modelMatrix = iModelMatrix;
	float3 worldPos = GetWorldPos(modelMatrix);
	oPos = GetClipPos(worldPos);
	oScreenPos = GetScreenPosPreDiv(oPos);
}

void PS(float2 iScreenPos : TEXCOORD0,
    out float4 oColor : OUTCOLOR0)
{
	float Z = -2.0*iScreenPos.x + 1.0;
	float Y = -2.0*iScreenPos.y + 1.0;
	float X = 0.85 * sqrt(1.0 - Y*Y - Z*Z);  //Manipulate coeffitient to get different "zoom"
	X = X*X;                                            //Manipulate power to get different "zoom progression"
	float3 vec = { X, Y, Z };

	float3 color;

	if (sqrt(Z*Z + Y*Y)<=1.0)
	{
		oColor = float4(SampleCube(DiffCubeMap, vec).rgb, 1.0);
	}
	else
	{
		oColor = float4(0.0, 0.0, 0.0, 0.0);
	}
}
[/details]

Everything works, so far so good. Only issue I have with this is that it is quite demanding on the processing power, as there are many independent viewports that must be rendered. I would like to know wheter there are some ways to optimize the process. I get a huge rise in steps like ExecuteRenderPaths, RenderScenePass, an I would like to know wheter some of these steps could be combined to save time. Especially when the 5 views are sampled from the same point and are only rotated. I tried something to set multiple outputs in RenderCommands but without success. I'd like to know if there is principally anything I could do to improve efficiency.

Thanks for ideas!

-------------------------

cadaver | 2017-01-02 01:07:40 UTC | #2

It should be possible to modify the View class to allow a "replay" of another View with a different camera matrix. This would only have the cost of actually rendering, skipping the redundant CPU-side work of culling, occlusion, light processing, batch queue building etc. However I don't know the cleanest way how this should be exposed in the engine, considering that there's a separation into the view preparation, and rendering at the end of frame.

It would be rather easy if there would be imperative "Cull()" and "Render()" functions each taking a camera, and the "Render()" function taking the destination texture. However now there's rather the mechanism of the engine detecting the necessary views during the frame, then rendering them in the end taking care of the dependencies.

Btw. I like small cars so your example picture was very pleasing :slight_smile:

-------------------------

Bart | 2017-01-02 01:07:40 UTC | #3

Thanks for the info. So that means I would have to create my own fork of the engine, which is something I'd rather avoid. Unless you come up with a clean way how to implement this, I would enjoy to implement it then and share with others. Will take look in the engine code tomorrow, if I am able to comprehend it in the first place  :slight_smile: 

Another idea: would it be possible to implement this in a shader code? First rendering 180deg view to have correct culling, shadows, etc, then having a vertex shader chop it up into 5 different rendertargets (cube faces) and then joining it the way I already do? But that would require manipulating camera matrix in the VS, and I dont know if that is possible or is already too late?

-------------------------

cadaver | 2017-01-02 01:07:40 UTC | #4

Got interested in this and already implemented it in the master branch. There was some trickiness involved, and I don't guarantee it's 100% bugfree yet.

Documentation will be added later, but the basic idea is that you can call Viewport::SetCullCamera() to set a separate camera for culling. When multiple viewports set the same cull camera, the view will only be prepared once. Obviously they will also need the same renderpath or the sharing will be disabled.

Note that simply using the same camera (without SetCullCamera) on two viewports will not automatically trigger this optimization, as the viewports could be using the same camera with different auto aspect ratios and therefore different culling.

-------------------------

boberfly | 2017-01-02 01:07:41 UTC | #5

Thanks for implementing this cadaver! When I was doing some porting to Oculus Rift DK2 I was thinking along the lines of a 'cull camera' for an optimisation, where you'd have a camera matrix which is the size of the two eyes, then render with left/right eye matrices onto the same framebuffers using glViewport (to prevent so many framebuffer changes and 2x culling).

I'll open up that branch again and play with this change as well.

-------------------------

Bart | 2017-01-02 01:07:41 UTC | #6

Hi, thanks for such quick implementation, you're the best :slight_smile:

However, I made a test and it is actually little slower than before. Although we can see drop in count of GetDrawables, ProcessLights, GetLightBatches and GetBaseBatches, the overall fps is lower. For comparison:

4 fisheyes, SetCullCamera, No shadows (=27fps)
[spoiler][img]http://urho.czweb.org/4cam_noshadow_cullcamera.png[/img][/spoiler]
4 fisheyes, No shadows (=30fps)
[spoiler][img]http://urho.czweb.org/4cam_noshadow_nocullcamera.png[/img][/spoiler]
4 fisheyes, SetCullCamera, Shadows (=13fps)
[spoiler][img]http://urho.czweb.org/4cam_shadow_cullcamera.png[/img][/spoiler]
4 fisheyes, Shadows (=15fps)
[spoiler][img]http://urho.czweb.org/4cam_shadow_nocullcamera.png[/img][/spoiler]

These result numbers are quite stable, so I would trust it. Is there anything I could do to optimize the calculations in Render section, or is this strictly bound to each view? I am also curious about the Present step, what does it do, and why is it so much longer when shadows are enabled (45ms with shadows, 16ms without shadows)?

Do you think my shader solution of the fisheye problem mentioned in my previous post would be viable or is it impossible for some reason? Could it be like this?:
[ul][li]Create 180deg view - all verices get into gpu stream[/li]
[li]In render path, run vertex shader 5 times, each time processing vertices from region of interest and transform them in such way that we get 5x 90deg camera view into 5 different render targets (cube sides). This is the trickiest part - is this even possible? [/li]
[li]Unite these 5 rendertargets into one in pixel shader (i do this already). Output into viewport[/li][/ul]


Thank you

-------------------------

cadaver | 2017-01-02 01:07:41 UTC | #7

Urho doesn't implement geometry shaders, so you can't render into several rendertargets at the same time sensibly, only MRT output for e.g. deferred rendering.

Actually I'm not surprised by this result, because now it means that the whole view's objects are rendered for each fisheye face, which can result in a lot more triangles and draw calls (check your stats in the top-left corner!) In cubemap rendering the culling per face can help a lot to eliminate unnecessary objects, and furthermore the View is quite intelligent to e.g. disable shadows if there are no shadow casters / receivers visible. In this case the view preparation sharing would only help if you're CPU bound and your GPU is so powerful that it can take the extra object rendering without much slowdown.

The view preparation saving would be most significant in stereoscopic applications because in that case the views are nearly identical and there are no (or very little) wasted objects being drawn.

If you can take a bit wrong output the fastest would be to just render a forward view, perhaps with extra-wide FOV, and use a pixel shader to incorrectly warp it into a fisheye.

-------------------------

Bart | 2017-01-02 01:07:41 UTC | #8

Ok, thank you very much for the claricifaction, thats what I needed to hear.

Have a nice weekend!

-------------------------

