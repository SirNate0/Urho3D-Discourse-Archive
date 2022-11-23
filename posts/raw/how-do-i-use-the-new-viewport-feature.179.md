GIMB4L | 2017-01-02 00:58:40 UTC | #1

I made this post on the Github page but it'll get more visibility here.

Basically, how exactly do I make a viewport without a camera/scene/octree? I tried doing it with the Viewport constructor that only takes a context, and I still get a null pointer access because the view still tries to flip the camera that isn't there. The culprit is this line:

[code] if (renderTarget_)
    {
        // On OpenGL, flip the projection if rendering to a texture so that the texture can be addressed in the same way
        // as a render texture produced on Direct3D9
        #ifdef USE_OPENGL
        camera_->SetFlipVertical(true);
        #endif
    }[/code]

There are a bunch of checks beforehand, but that line doesn't care if the camera is null or not. Is this a bug or am I using the feature wrong?

-------------------------

cadaver | 2017-01-02 00:58:40 UTC | #2

It is a bug. This was not tested on OpenGL, which flips the rendering.

-------------------------

GIMB4L | 2017-01-02 00:58:40 UTC | #3

Alright, thanks for the fix! But how do I make a sceneless/cameraless viewport? Do I make the viewport with the context constructor and specify a renderpath, or is there something else I have to do?

-------------------------

GIMB4L | 2017-01-02 00:58:41 UTC | #4

I should clarify what I'm doing. Taking the RenderToTexture sample, I have the following code:

[code] RenderSurface* surface = renderTexture->GetRenderSurface();
            SharedPtr<Viewport> rttViewport(new Viewport(context_));
			rttViewport->SetRenderPath(cache->GetResource<XMLFile>("RenderPaths/UIRender.xml"));
            surface->SetViewport(0, rttViewport);[/code]

The renderpath I'm using here takes advantage of my UI-render modification I made to the engine. However, the texture being sampled from is solid black & blank.

-------------------------

cadaver | 2017-01-02 00:58:41 UTC | #5

It is OK to use any of the constructors, just pass null pointers where necessary, for example this one allows to specify the renderpath directly:

Viewport::Viewport(Context* context, Scene* scene, Camera* camera, RenderPath* renderPath) 

The way I'd imagine you would use the sceneless renderpath would be to:
1) setup a normal scene render into the viewport of a Texture2D's rendersurface. Btw. the update mode on the surface needs to be set SURFACE_UPDATEALWAYS, or else the update needs to be manually triggered every frame, as this texture won't be visible in an actual scene
2) setup a sceneless viewport + renderpath into the backbuffer, which just samples the Texture2D from step 1) using a quad command + the Oculus distortion shader

-------------------------

GIMB4L | 2017-01-02 00:58:41 UTC | #6

I'm not using this for the Oculus distortion shader. I got that to work on a per-viewport basis -- this is for rendering the UI (using the edit I made to the subsystem) to a texture, so I can put that on a plane, and put it in front of the camera when in Oculus mode so the HUD still looks right.

-------------------------

GIMB4L | 2017-01-02 00:58:41 UTC | #7

Okay, I've set the texture update to SURFACE_UPDATEALWAYS but I still don't see anything rendering. I can confirm that the UI is attempting to render, and I'll check that it is being rendered to some buffer (GDebugger). Here's the code:

[code]            
        RenderSurface* surface = renderTexture->GetRenderSurface();
	surface->SetUpdateMode(SURFACE_UPDATEALWAYS);
        SharedPtr<Viewport> rttViewport(new Viewport(context_, nullptr, nullptr, nullptr));
	rttViewport->SetRenderPath(cache->GetResource<XMLFile>("RenderPaths/UIRender.xml"));
        surface->SetViewport(0, rttViewport);[/code]

-------------------------

cadaver | 2017-01-02 00:58:41 UTC | #8

It's hard to say what goes wrong. On Direct3D using something like PIX to debug draw calls often helps in cases like this.

-------------------------

GIMB4L | 2017-01-02 00:58:41 UTC | #9

I'm fairly confident it's the sceneless viewport, because I can manipulate where the UI shows up just fine when there is a scene and camera. 

I guess I could make do with an empty scene, without too much computational overhead. However, would blending be an issue in that case? It needs to be transparent so the actual game scene shows up.

-------------------------

cadaver | 2017-01-02 00:58:41 UTC | #10

When the UI is ultimately displayed by an object in front of the camera, only the blend mode of that object's material matters. You probably need to use either additive blending, or alpha blending with a custom shader that computes the alpha value from the RGB values of the UI texture, as the UI itself doesn't render out alpha values.

-------------------------

GIMB4L | 2017-01-02 00:58:41 UTC | #11

Okay, I got the transparency to work. However, the image is flipped backwards and upside-down. Is this an OpenGL- specific occurance?

-------------------------

cadaver | 2017-01-02 00:58:41 UTC | #12

Yes, this is OpenGL-specific. When a viewport is rendered to a texture, it needs to be rendered flipped on OpenGL so that it can be sampled like a normal texture. However the UI constructs its own projection matrix (as it assumes it's rendering to the backbuffer) so it doesn't take this into account. In this case it's probably easiest just flip the UV coords in your shader.

-------------------------

GIMB4L | 2017-01-02 00:58:41 UTC | #13

Yeah I'll just scale it uniformly by -1. Does the same thing.

-------------------------

GIMB4L | 2017-01-02 00:58:42 UTC | #14

Okay, I got the HUD to show up in the texture, and it works great. However, everything looks washed out, and I know it's due to the blending. I want the UI to replace what's in the scene, but to do that it needs alpha values. I could use a custom shader, but the view is rendered after since views are rendered back-to-front, so I wouldn't be able to sample from the diffuse map. How can I make the UI render with alpha values?

-------------------------

GIMB4L | 2017-01-02 00:58:42 UTC | #15

Again I should clarify. Using an add blend mode works fine. However, when I try to do GL_SRC_ALPHA and GL_ONE_MINUS_SRC_ALPHA-style blending, the black UI scene overwrites what's currently in the scene. Is this the order of the rendering or am I blending wrong? Or is an alpha value issue? Since the plane it's being rendered on is part of the scene, I'd imagine it has to be a rendering issue. I could write my own shader for this, but once again how can I be sure the plane is rendered last? Here's the Technique i'm using for the plane:

[code]<technique vs="Unlit" ps="Unlit" psdefines="DIFFMAP">
    <pass name="alpha" depthtest="always" depthwrite="false" blend="alpha" />
</technique>
[/code]

-------------------------

cadaver | 2017-01-02 00:58:42 UTC | #16

You can use the postalpha pass to render after all other alpha geometry. This is used by the editor's gizmo (see CoreData/Techniques/NoTextureOverlay.xml technique)

-------------------------

GIMB4L | 2017-01-02 00:58:42 UTC | #17

I tried doing that but there is no blending at all. I had to write my own shader and check some of the colour values to determine if I should leave the back buffer as is or sample from the UI texture. It works, but it doesn't look the best.

-------------------------

