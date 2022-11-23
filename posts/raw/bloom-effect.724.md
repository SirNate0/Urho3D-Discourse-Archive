vivienneanthony | 2017-01-02 01:02:26 UTC | #1

Hey

Did anyone get the bloom and ansiotropic(I think it's how it spelled) effect working?

Vivienne

PS. Sorry  about so many messages. It's a lot of things going on at one time.

-------------------------

rasteron | 2017-01-02 01:02:26 UTC | #2

Hey Vivienne,

Yes, AFAIK Bloom/HDR has been tested since way back on [url=https://groups.google.com/forum/#!searchin/urho3d/HDR/urho3d/fQWJEHNL1wk/WjVAwxQ0OTIJ]Google groups[/url] days.  :wink: 

I think you can test it now with this as or c++ [url=https://github.com/urho3d/Urho3D/blob/f120aa4be00d95f98bddab26ea25c84052f68217/Bin/Data/Scripts/09_MultipleViewports.as#L120]demo[/url].

I'm not sure about Anistropic filtering, I don't see it on the shader files.

-------------------------

vivienneanthony | 2017-01-02 01:02:26 UTC | #3

[quote="rasteron"]Hey Vivienne,

Yes, AFAIK Bloom/HDR has been tested since way back on [url=https://groups.google.com/forum/#!searchin/urho3d/HDR/urho3d/fQWJEHNL1wk/WjVAwxQ0OTIJ]Google groups[/url] days.  :wink: 

I think you can test it now with this as or c++ [url=https://github.com/urho3d/Urho3D/blob/f120aa4be00d95f98bddab26ea25c84052f68217/Bin/Data/Scripts/09_MultipleViewports.as#L120]demo[/url].

I'm not sure about Anistrophic filtering, I don't see it on the shader files.[/quote]

Ah. Ok

-------------------------

vivienneanthony | 2017-01-02 01:02:26 UTC | #4

[quote="rasteron"]Hey Vivienne,

Yes, AFAIK Bloom/HDR has been tested since way back on [url=https://groups.google.com/forum/#!searchin/urho3d/HDR/urho3d/fQWJEHNL1wk/WjVAwxQ0OTIJ]Google groups[/url] days.  :wink: 

I think you can test it now with this as or c++ [url=https://github.com/urho3d/Urho3D/blob/f120aa4be00d95f98bddab26ea25c84052f68217/Bin/Data/Scripts/09_MultipleViewports.as#L120]demo[/url].

I'm not sure about Anistropic filtering, I don't see it on the shader files.[/quote]


I tried this and I seen no difference. Hmm. Maybe Chris would notice what's wrong.

[code]/// Set up a viewport to the Renderer subsystem so that the 3D scene can be seen. We need to define the scene and the camera
    /// at minimum. Additionally we could configure the viewport screen size and the rendering path (eg. forward / deferred) to
    /// use, but now we just use full screen and default render path configured	SetOrthographic ( in the engine command line options
    SharedPtr<Viewport> viewport(new Viewport(context_, scene_, cameraNode_->GetComponent<Camera>()));
    renderer->SetViewport(0, viewport);

    SharedPtr<RenderPath> effectRenderPath = viewport->GetRenderPath()->Clone();
    effectRenderPath->Append(cache->GetResource<XMLFile>("PostProcess/Bloom.xml"));

    /// Make the bloom mixing parameter more pronounced
    effectRenderPath->SetShaderParameter("BloomMix", Vector2(0.9f, 0.6f));
    effectRenderPath->SetEnabled("Bloom", false);
    viewport->SetRenderPath(effectRenderPath);[/code]

In the code that toggles.

[code]  /// parameters for debug related command
    if(argument[1]=="bloom")
    {
        RenderPath* effectRenderPath = GetSubsystem<Renderer>()->GetViewport(0)->GetRenderPath();

        effectRenderPath->ToggleEnabled("Bloom");
}
[/code]

Header file

[code] /// The UI's root UIElement.
    SharedPtr<UIElement> uiRoot_;
    SharedPtr<Viewport> viewport;
    SharedPtr<RenderPath> effectRenderPath;

[/code]

-------------------------

franck22000 | 2017-01-02 01:02:26 UTC | #5

Well maybe if you were setting: 

[code]effectRenderPath->SetEnabled("Bloom", false);[/code]

To 

[code]effectRenderPath->SetEnabled("Bloom", true);[/code]

It would work better :slight_smile:

-------------------------

vivienneanthony | 2017-01-02 01:02:26 UTC | #6

[quote="franck22000"]Well maybe if you were setting: 

[code]effectRenderPath->SetEnabled("Bloom", false);[/code]

To 

[code]effectRenderPath->SetEnabled("Bloom", true);[/code]

It would work better :slight_smile:[/quote]
I thought that was basically the toggle. Even if the change it did not work.

-------------------------

reattiva | 2017-01-02 01:02:26 UTC | #7

The example 09_MultipleViewports.as has the bloom effect.

-------------------------

vivienneanthony | 2017-01-02 01:02:26 UTC | #8

[quote="reattiva"]The example 09_MultipleViewports.as has the bloom effect.[/quote]

I'll look at it again. That's what I based my code from.

-------------------------

vivienneanthony | 2017-01-02 01:02:27 UTC | #9

[quote="reattiva"]The example 09_MultipleViewports.as has the bloom effect.[/quote]

I got the bloom effect working. I'll play with the FXAA ones once I change the source to be Urho 1.32 friendly.

-------------------------

