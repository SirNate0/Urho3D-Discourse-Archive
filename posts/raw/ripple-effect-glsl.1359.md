rasteron | 2017-01-02 01:07:10 UTC | #1

[video]https://www.youtube.com/watch?v=dTiXcZlTJ8U[/video]

[gist]https://gist.github.com/d4c1caef18f501138e11[/gist]
[gist]https://gist.github.com/d313b2c05fe9bd165e37[/gist]
It would be nice to add this to the water shader with interaction to objects or something similar.

enjoy! :slight_smile:

-------------------------

Lumak | 2017-01-02 01:07:10 UTC | #2

This is cool!

-------------------------

rasteron | 2017-01-02 01:07:11 UTC | #3

[quote="Lumak"]This is cool![/quote]

Thanks Lumak :slight_smile: I've seen better versions but this will do for now..

-------------------------

1vanK | 2017-01-02 01:07:42 UTC | #4

I'm trying to use two shader simultaneously

[code]
    Renderer* renderer = GetSubsystem<Renderer>();
    SharedPtr<Viewport> viewport(new Viewport(context_, scene_, cameraNode_->GetComponent<Camera>()));
    renderer->SetViewport(0, viewport);

    ResourceCache* cache = GetSubsystem<ResourceCache>();
    SharedPtr<RenderPath> effectRenderPath = viewport->GetRenderPath()->Clone();
    effectRenderPath->Append(cache->GetResource<XMLFile>("PostProcess/Ripple.xml"));
    effectRenderPath->Append(cache->GetResource<XMLFile>("PostProcess/Vignette.xml"));
    viewport->SetRenderPath(effectRenderPath);
[/code]

and the program is crashed. Although individually shaders work normally. Also another combination work normally.

[code]
    Renderer* renderer = GetSubsystem<Renderer>();
    SharedPtr<Viewport> viewport(new Viewport(context_, scene_, cameraNode_->GetComponent<Camera>()));
    renderer->SetViewport(0, viewport);

    ResourceCache* cache = GetSubsystem<ResourceCache>();
    SharedPtr<RenderPath> effectRenderPath = viewport->GetRenderPath()->Clone();
    effectRenderPath->Append(cache->GetResource<XMLFile>("PostProcess/Blur.xml"));
    effectRenderPath->Append(cache->GetResource<XMLFile>("PostProcess/GreyScale.xml"));
    viewport->SetRenderPath(effectRenderPath);
[/code]

Any ideas?

-------------------------

rasteron | 2017-01-02 01:07:42 UTC | #5

Hey IvanK,

I'm not sure what could be the problem with activating both in any particular order but I think it might have something to do with the dynamic aspect of the ripple shader. Another option is you could just modify and combine/chain both sources if necessary. See my Old TV effect, it has a simple Fish Eye, Noise and GreyScale shader combined.

One thing I noticed though, the Vignette effect just overrides the ripple (in any order) and it does not crash on my set up.

-------------------------

