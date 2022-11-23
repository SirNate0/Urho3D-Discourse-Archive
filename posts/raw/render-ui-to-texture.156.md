GIMB4L | 2017-01-02 00:58:29 UTC | #1

Is it possible to render the UI to a texture? I don't see anything in the demos.

-------------------------

cadaver | 2017-01-02 00:58:29 UTC | #2

No. For now the UI subsystem always renders into the backbuffer.

-------------------------

GIMB4L | 2017-01-02 00:58:29 UTC | #3

Does this happen after or before the postprocessing?

-------------------------

cadaver | 2017-01-02 00:58:29 UTC | #4

After. If you need postprocessing for the UI, at this point I recommend just digging into the UI rendering code and modifying it for your needs. 

In the future, the ideal situation would be to have the UI root as just another component in the scene, so there could be multiple of them, used to texture in-world objects etc.

-------------------------

GIMB4L | 2017-01-02 00:58:30 UTC | #5

Okay, so I figured out why simply calling graphics->SetRenderTexture(...) doesn't work. Since the UI is rendered after, the texture it rendered to was already sampled earlier. 

The fix would be to render the UI first to a texture, and then use materials/shaders to combine it with wherever it should go. How do I make a texture that everything can reference?

-------------------------

GIMB4L | 2017-01-02 00:58:31 UTC | #6

Okay, I thought about it some more, and maybe it would be best to include the UI pass as an actual pass in the renderpaths. I attempted to do this, but I'm not sure how rendertargets work, and how the engine renders the scene to them. I noticed that before the UI renders, it resets all the rendertargets so the UI is displayed on the backbuffer. I removed this and tried rendering to one of the viewports, but nothing showed up. How exactly are views rendered?

-------------------------

cadaver | 2017-01-02 00:58:31 UTC | #7

Let's assume that you have a Texture2D that's been created as a rendertarget (again, refer to the RenderToTexture sample). You would name it and make it accessible by name in renderpaths as follows:

[code]
    myTexture->SetName("UITexture");
    GetSubsystem<ResourceCache>()->AddManualResource(myTexture);
[/code]

To redirect UI rendering to it, put the following in UI::Render() right after the call to ResetRenderTargets:

[code]
    graphics_->SetRenderTarget(0, myTexture->GetRenderSurface());
    graphics_->SetViewport(IntRect(0, 0, myTexture->GetWidth(), myTexture->GetHeight()));
[/code]

-------------------------

GIMB4L | 2017-01-02 00:58:31 UTC | #8

So I did something cool! I managed to make the UI render as part of a renderpath, in any viewport following that render path! This allowed me to render the UI to multiple  viewports AND apply shaders to it! If this is a desired feature I can make a pull request.

-------------------------

cadaver | 2017-01-02 00:58:31 UTC | #9

That's cool that you got it working.

However right now the UI heavily assumes that it's sized like the whole screen, and there can only exist one UI hierarchy, so I believe that feature would not be generally usable yet.

-------------------------

sduensin | 2017-01-02 01:00:05 UTC | #10

This would be a great feature to have.  I'd love to be able to create in-world UIs.  (I realize that requires quite a bit more than just rendering to a texture, but hey, one can wish!)

-------------------------

stark7 | 2017-08-22 21:31:36 UTC | #11

Hello cadaver, has this feature been revisited or discussed lately? Particularly making the UIElement a Node or Node Component and have it part of the scene itself

EDIT: I just saw https://github.com/urho3d/Urho3D/pull/2074 so never mind :). Also.. don't go? I'll tell you the ending to GoT.

-------------------------

