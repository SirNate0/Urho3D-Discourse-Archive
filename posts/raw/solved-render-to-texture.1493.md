Sasha7b9o | 2017-01-02 01:08:07 UTC | #1

Hi.
Create texture and surface thus:
[code]    Node* nodeCameraTarget = gScene->CreateChild("CameraTarget");
    Camera* cameraTarget = nodeCameraTarget->CreateComponent<Camera>();
    cameraTarget->SetNearClip(1.0f);
    cameraTarget->SetFarClip(radiusDetect);

    SharedPtr<Texture2D> renderTexture = new Texture2D(gContext);
    renderTexture->SetSize(SIZE_WINDOW_TARGET, SIZE_WINDOW_TARGET, D3DFMT_X8R8G8B8, Urho3D::TEXTURE_RENDERTARGET);
    renderTexture->SetFilterMode(Urho3D::FILTER_DEFAULT);

    SharedPtr<RenderSurface> renderSurface = renderTexture->GetRenderSurface();
    SharedPtr<Viewport> viewport(new Viewport(gContext, gScene, cameraTarget));
    renderSurface->SetViewport(0, viewport);
    renderSurface->SetUpdateMode(Urho3D::SURFACE_UPDATEALWAYS);[/code]

In event E_POSTRENDERUPDATE call 
[code]   renderTexture->GetData(0, buffer)[/code]
contents buffer is 0xcd, 0xcd, 0xcd ....

renderTexture It is stored separately, the image from it is planned to bring to UI.

-------------------------

Sasha7b9o | 2017-01-02 01:08:08 UTC | #2

[quote="Sinoid"]Can you post the code for this "buffer" you're passing in?
[code]renderTexture->GetData(0, buffer)[/code][/quote]
[code]    uint *buffer = new uint[SIZE_WINDOW_TARGET * SIZE_WINDOW_TARGET];[/code]

[quote="Sinoid"]Any error messages being written to the log?[/quote]
Many thanks! Parameter D3DFMT_X8R8G8B8 was wrong (And how I could forget to look at the log?)
Returned to an initial state Graphics::GetRGBFormat() and everything earned.
Thanks very big!

-------------------------

Sasha7b9o | 2017-01-02 01:08:08 UTC | #3

Very useful remarks.
Thanks.

-------------------------

