restless | 2019-12-25 19:59:19 UTC | #1

So I create a render to texture with linked depth target like this:

    impRenderTexture_ = new Texture2D(context_);
    impRenderTexture_->SetSize(segment_res,
                               segment_res,
                               Graphics::GetRGBAFormat(),
                               Urho3D::TEXTURE_RENDERTARGET,
                               0);

    impRenderTextureDepth_ = new Texture2D(context_);
    impRenderTextureDepth_->SetSize(segment_res,
                                    segment_res,
                                    Graphics::GetDepthStencilFormat(),
                                    Urho3D::TEXTURE_DEPTHSTENCIL,
                                    0);

    impRenderPath_ = new RenderPath();
    impRenderPath_->Load(
        GetSubsystem<ResourceCache>()
        ->GetResource<XMLFile>("RenderPaths/ImpostorForwardDepth.xml"));
     RenderSurface* renderSurface = impRenderTexture_->GetRenderSurface();
    impViewport_ = new Viewport(context_,
                                impScene_,
                                impCameraNode_->GetComponent<Camera>());
    impViewport_->SetRenderPath(impRenderPath_);
    renderSurface->SetUpdateMode(Urho3D::SURFACE_MANUALUPDATE);
    renderSurface->SetLinkedDepthStencil(
         impRenderTextureDepth_->GetRenderSurface());
    renderSurface->SetViewport(0, impViewport_);

Then I start rendering it:

    impRenderTexture_->GetRenderSurface()->QueueUpdate();
    SubscribeToEvent (E_ENDVIEWRENDER,
                      URHO3D_HANDLER(Impostor, HandleRenderDone));


And when I recieve event I read texture data:

    impRenderTexture_->GetData(0, my_buffer);

And it works good: my_buffer now contains whole the rendered frame data.

But when I try to read depth data like this:

    auto surface = impRenderTexture_->GetRenderSurface()->GetLinkedDepthStencil();
    Texture2D* tx2d = reinterpret_cast<Texture2D*>(tex->GetParentTexture());
    // tx2d now actually points to the impRenderTextureDepth_ that we created
    // and linked..
    tx2d->GetData(0, my_depth_buffer);

But GetData() fails like this  (in OGLTexture2D.cpp:303):

    bool Texture2D::GetData(unsigned level, void* dest) const
    {
        if (!object_.name_ || !graphics_)
        {
            //<----------- FAILS HERE :( ------------>
            URHO3D_LOGERROR("No texture created, can not get data");    
            return false;
        }
        ...

Am I missing something on how it's done?

Things I tried to no result so far:

* Let the engine create depth buffer automatically -- don't seem to have any way to access it then

SOLUTION is elaborated a bit in post #3

-------------------------

Bananaft | 2019-12-25 19:55:29 UTC | #2

Have you tried other formats? Like LinearDepth or ReadableDepth ? If nothing works, you can even use color format RGBA16F.

Also, can you show your renderpath?

-------------------------

restless | 2019-12-25 19:58:10 UTC | #3

Render path (stock ForwardDepth.xml):

    <renderpath>
        <rendertarget name="depth" sizedivisor="1 1" format="lineardepth" />
        <command type="clear" color="1 1 1 1" depth="1.0" stencil="0" output="depth" />
        <command type="scenepass" pass="depth" output="depth" />
        <command type="clear" color="fog" depth="1.0" stencil="0" />
        <command type="scenepass" pass="base" vertexlights="true" metadata="base" />
        <command type="forwardlights" pass="light" />
        <command type="scenepass" pass="postopaque" />
        <command type="scenepass" pass="refract">
            <texture unit="environment" name="viewport" />
        </command>
        <command type="scenepass" pass="alpha" vertexlights="true" sort="backtofront" metadata="alpha">
            <texture unit="depth" name="depth" />
        </command>
        <command type="scenepass" pass="postalpha" sort="backtofront" />
    </renderpath>

Do you mean different formats in SetSize? Like this:
```
impRenderTextureDepth_->SetSize(segment_res,
                                segment_res,
                                Graphics::GetDepthStencilFormat(),  // this one?
                                Urho3D::TEXTURE_DEPTHSTENCIL,
                                0);
```

Good idea! Replaced it with Graphics::GetReadableDepthFormat() and now it seems to be working! Need to work on the client code to confirm everything works now.

Thanks a lot!

UPD: Solution was to use Graphics::GetReadableDepthFormat() when creating a texture for depth rendering. ![2889602834704_37impostor_depthstencil|500x500](upload://b9hLkdsUa2TjZd9uwxjr3wtGPTy.png)

-------------------------

restless | 2019-12-25 20:01:15 UTC | #4

By the way, I seem to be getting the data in 1-byte format. Is it legal for the texture to return 0 from .GetComponents()? Should I file a bug on this?

-------------------------

