thatonejonguy | 2017-01-02 01:07:35 UTC | #1

How can I set the destination for a Render to Texture into one of a Render Target's texture units? The samples use the rtt into one of a material's texture units and I have been unsuccessful so far adapting this for a Render Target. Any help would be appreciated. Thanks.

-Jon

-------------------------

friesencr | 2017-01-02 01:07:35 UTC | #2

There is a sample that does exactly that.  Refer to example 10 for more details.

[code]
            Node* boxNode = scene_->CreateChild("ScreenBox");
            boxNode->SetPosition(Vector3(0.0f, 10.0f, 0.0f));
            boxNode->SetScale(Vector3(21.0f, 16.0f, 0.5f));
            StaticModel* boxObject = boxNode->CreateComponent<StaticModel>();
            boxObject->SetModel(cache->GetResource<Model>("Models/Box.mdl"));
            boxObject->SetMaterial(cache->GetResource<Material>("Materials/Stone.xml"));

            Node* screenNode = scene_->CreateChild("Screen");
            screenNode->SetPosition(Vector3(0.0f, 10.0f, -0.27f));
            screenNode->SetRotation(Quaternion(-90.0f, 0.0f, 0.0f));
            screenNode->SetScale(Vector3(20.0f, 0.0f, 15.0f));
            StaticModel* screenObject = screenNode->CreateComponent<StaticModel>();
            screenObject->SetModel(cache->GetResource<Model>("Models/Plane.mdl"));

            // Create a renderable texture (1024x768, RGB format), enable bilinear filtering on it
            SharedPtr<Texture2D> renderTexture(new Texture2D(context_));
            renderTexture->SetSize(1024, 768, Graphics::GetRGBFormat(), TEXTURE_RENDERTARGET);
            renderTexture->SetFilterMode(FILTER_BILINEAR);

            // Create a new material from scratch, use the diffuse unlit technique, assign the render texture
            // as its diffuse texture, then assign the material to the screen plane object
            SharedPtr<Material> renderMaterial(new Material(context_));
            renderMaterial->SetTechnique(0, cache->GetResource<Technique>("Techniques/DiffUnlit.xml"));
            renderMaterial->SetTexture(TU_DIFFUSE, renderTexture);
            screenObject->SetMaterial(renderMaterial);

            // Get the texture's RenderSurface object (exists when the texture has been created in rendertarget mode)
            // and define the viewport for rendering the second scene, similarly as how backbuffer viewports are defined
            // to the Renderer subsystem. By default the texture viewport will be updated when the texture is visible
            // in the main view
            RenderSurface* surface = renderTexture->GetRenderSurface();
            SharedPtr<Viewport> rttViewport(new Viewport(context_, rttScene_, rttCameraNode_->GetComponent<Camera>()));
            surface->SetViewport(0, rttViewport);
[/code]

-------------------------

thatonejonguy | 2017-01-02 01:07:35 UTC | #3

Hey, thanks for the reply. I was looking at that example, but instead of using it for a material, I was trying to use the render surface directly in the render path. Anyway, I got it figured out. I just needed to name the texture, manually add it to the resource cache, then set the render surface to SURFACE_UPDATEALWAYS (that's where I was getting hung up ;p).

-Jon

-------------------------

