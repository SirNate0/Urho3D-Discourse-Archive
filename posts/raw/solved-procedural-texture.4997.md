Lunarovich | 2019-03-23 11:23:08 UTC | #1

Hello! I'm trying to create a texture by means of simple post-processing effect on the auxiliary viewport. Here's the code

    SharedPtr<Texture2D> Game::CreateTexture(int width, int height)
    {
        //Get the Resource Cache subsystem
        ResourceCache* cache = GetSubsystem<ResourceCache>();
        
        SharedPtr<Texture2D> renderTexture(new Texture2D(context_));
        renderTexture->SetSize(width, height, Graphics::GetRGBFormat(), TEXTURE_RENDERTARGET);
        renderTexture->SetFilterMode(FILTER_BILINEAR);

        // Create the scene which will be rendered to a texture
        rttScene_ = new Scene(context_);
        
        // Create a camera for the render-to-texture scene.
        rttCameraNode_ = rttScene_->CreateChild("Camera");
        auto* rttCamera = rttCameraNode_->CreateComponent<Camera>();

        RenderSurface* surface = renderTexture->GetRenderSurface();
        SharedPtr<Viewport> rttViewport(new Viewport(context_, rttScene_, rttCameraNode_->GetComponent<Camera>()));
        surface->SetViewport(0, rttViewport);

        SharedPtr<RenderPath> effectRenderPath = rttViewport->GetRenderPath()->Clone();
        effectRenderPath->Append(cache->GetResource<XMLFile>("PostProcess/BasicPP.xml"));
        rttViewport->SetRenderPath(effectRenderPath);

        surface->QueueUpdate();

        return renderTexture;
    }

I've created BasicPP.xml and the corresponding BasicPP.glsl which creates a simple gradient by using gl_FragColor. The effect is working as expected on the main viewport. Also, when I attach a .png texture to my sprite, it gets shown on the screen.

So what am I missing?

-------------------------

Modanung | 2019-03-04 08:22:45 UTC | #2

What results do you get and how do they not match up with your expectations?

-------------------------

Lunarovich | 2019-03-04 13:53:11 UTC | #3

For a 128x128 texture I get a black rectangle. I render the effect on the renderer's viewport to be sure that it's working, so I'm expecting to see a mini-version of the background where the black 128x128 rectangle is.

![01|644x500](upload://n2luwn0sE2q4XskX923wv3yyuII.png) 

If I don't set size with sprite->SetSize(IntVector2(128, 128)); I don't get anything... Just a background with a post processing gradient. So, obviously, the post-processing effect is not rendered on the created texture.

-------------------------

SirNate0 | 2019-03-11 21:15:56 UTC | #4

I think you may need to add an octree to the scene, possibly also a zone.

-------------------------

Modanung | 2019-03-15 00:00:20 UTC | #5

The `Renderer` has a default `Zone` (which can be accessed and modified through `GetSubsystem<Renderer>()->GetDefaultZone()`) so that should not be the problem.
Indeed the `Scene` does not seems to have an `Octree` component added. @Lunarovich Your program should output an error about this to the console/terminal/IDE (if it contains `Drawable`s).
> `ERROR: No Octree component in scene, drawable will not render`

-------------------------

Lunarovich | 2019-03-14 19:35:32 UTC | #6

Thanx. I'll try the solution and inform about the results.

-------------------------

Modanung | 2019-03-15 10:09:45 UTC | #7

[quote="Lunarovich, post:1, topic:4997"]
rttCameraNode_-&gt;GetComponent&lt;Camera&gt;()
[/quote]

Your intent seems to be to use - the currently unused - `auto* rttCamera` here, btw. This should not be causing any trouble, though.

-------------------------

Bananaft | 2019-03-18 09:38:31 UTC | #8

Is single shader all you want to draw into this texture? Or you also want to draw some 3d geometry there? If first, you don't really need a scene, viewport, camera and all that stuff. You can draw a quad right into render target.

here is the code for that:

    Graphics* graphics = context_->GetSubsystem<Graphics>();
	graphics->SetClipPlane(false);
	graphics->SetScissorTest(false);
	graphics->SetStencilTest(false);
	graphics->SetDepthWrite(false);
	graphics->SetDepthTest(CMP_ALWAYS);
	graphics->SetCullMode(CULL_NONE);
	graphics->SetFillMode(FILL_SOLID);
	graphics->SetBlendMode(BLEND_REPLACE);
	graphics->ResetRenderTargets();
	graphics->ClearTransformSources();
	
	WeakPtr<Texture2D> renderTarget(renderTexture);
	
	graphics->SetRenderTarget(0, renderTarget);
	graphics->SetViewport(IntRect(0, 0, TEX_X, TEX_Y));
	graphics->Clear(CLEAR_COLOR, Color(9e99, 0.0f, 0.0f, 0.0f));
	ShaderVariation* vs = graphics->GetShader(VS, "SdfCalculator" );
	ShaderVariation* ps = graphics->GetShader(PS, "SdfCalculator", this->GetDefines());
	graphics->SetShaders(vs, ps);

	Matrix3x4 modelMatrix = Matrix3x4::IDENTITY;
	modelMatrix.m23_ = 0.0f;
	graphics->SetShaderParameter(VSP_MODEL, modelMatrix);
	graphics->SetShaderParameter(VSP_VIEWPROJ, Matrix4::IDENTITY);
	
	graphics->SetTexture(TU_DIFFUSE, upldTexture);
	Renderer* renderer = context_->GetSubsystem<Renderer>();
	Geometry* geometry = renderer->GetQuadGeometry();
	geometry->Draw(graphics);

-------------------------

Lunarovich | 2019-03-23 11:22:16 UTC | #9

@SirNate0 and @Modanung, indeed, the octree was missing. Here is the working code for the future reference:

    #include <Urho3D/Graphics/Graphics.h>
    #include <Urho3D/Graphics/Texture2D.h>
    #include <Urho3D/Graphics/RenderPath.h>
    #include <Urho3D/Resource/XMLElement.h>
    
    SharedPtr<Texture2D> Game::CreateTexture(int width, int height)
    {
      //Get the Resource Cache subsystem
      ResourceCache* cache = GetSubsystem<ResourceCache>();
    
      // Create a renderable texture (1024x768, RGB format), enable bilinear filtering on it
      SharedPtr<Texture2D> renderTexture(new Texture2D(context_));
      renderTexture->SetSize(width, height, Graphics::GetRGBFormat(), TEXTURE_RENDERTARGET);
      renderTexture->SetFilterMode(FILTER_BILINEAR);
    
      // Create the scene which will be rendered to a texture
      rttScene_ = new Scene(context_);
      rttScene->CreateComponent<Octree>();
    
      // Create a camera for the render-to-texture scene.
      rttCameraNode_ = rttScene_->CreateChild("Camera");
      auto* rttCamera = rttCameraNode_->CreateComponent<Camera>();
    
      // Get the texture's RenderSurface object
      //(exists when the texture has been created in rendertarget mode)
      // and define the viewport for rendering the second scene,
      // similarly as how backbuffer viewports are defined
      // to the Renderer subsystem. By default the texture viewport
      // will be updated when the texture is visible in the main view
      RenderSurface* surface = renderTexture->GetRenderSurface();
      SharedPtr<Viewport> rttViewport(new Viewport(context_, rttScene_, rttCameraNode_->GetComponent<Camera>()));
      surface->SetViewport(0, rttViewport);
    
      SharedPtr<RenderPath> effectRenderPath = rttViewport->GetRenderPath()->Clone();
      effectRenderPath->Append(cache->GetResource<XMLFile>("PostProcess/BasicPP.xml"));
      rttViewport->SetRenderPath(effectRenderPath);
    
      surface->QueueUpdate();
      return renderTexture;
    }

@Bananaft thank you for  your answer. I'll try it and inform about the results here.

-------------------------

