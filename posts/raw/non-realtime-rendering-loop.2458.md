George | 2017-01-02 01:15:32 UTC | #1

Hi I have a question about rendering loop in Urho.

How do I control the rendering loop. So that it update the rendering of the scene when ever I want it to be.

For example: I want to render after all my object has been updated its position after 5 iterations?

I want to skip using non realtime time based on my event object.
 
I don't want my scene to be rendered at all, while I want object in the scene to still update it's position and orientation.

Thanks

-------------------------

cadaver | 2017-01-02 01:15:32 UTC | #2

You can call the parts of the Urho Engine class update & render process on their own. Note that update call is always required before render, since the visible viewports are culled & processed during update.

See the Tundra-Urho3D project, where the Framework class invokes one frame during Framework::ProcessOneFrame(). Some of the calls are to Tundra-Urho3D's own subsystems and can be ignored, but the basic Urho order is BeginFrame -> Update -> Render -> ApplyFrameLimit -> EndFrame

[github.com/realXtend/tundra-urh ... k.cpp#L337](https://github.com/realXtend/tundra-urho3d/blob/master/src/TundraCore/Framework/Framework.cpp#L337)

You can also look at more detail at what events should be sent for scene update vs. render update, but I will not guarantee that the result is what you're looking for. In extreme cases you can go for engine modifications.

[urho3d.github.io/documentation/ ... _loop.html](https://urho3d.github.io/documentation/HEAD/_main_loop.html)

-------------------------

George | 2017-01-02 01:15:32 UTC | #3

Thanks cadaver,

I think like you said ProcessOneFrame() is the one that I should be looked at.

Do we already have this function in Urho3d?  So that I don't recreate the wheel.

Thanks

-------------------------

cadaver | 2017-01-02 01:15:33 UTC | #4

Urho already has a "ProcessOneFrame" of its own, which does everything, and that's Engine::RunFrame(). The more involved work comes in when you want to be in more control, and for example run multiple scene updates vs. only one render, or manipulate the timestep. That's a quite specialized case and it feels OK to me that this would be controlled by manual code.

-------------------------

George | 2017-01-02 01:15:34 UTC | #5

Thanks mate,
I think my knowledge is not advanced enough to mess around with the graphic rendering.

My interest is in in simulation.

Best regards

-------------------------

