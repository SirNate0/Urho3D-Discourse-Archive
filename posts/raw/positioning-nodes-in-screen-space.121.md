Kingsley | 2017-01-02 00:58:10 UTC | #1

I'm trying to position objects in the world based on screen position. Camera's ScreenToWorldPoint seemed like it'd do the trick, but it appears to be misbehaving.
It claims to "Convert normalized screen coordinates (0.0 - 1.0) and depth to a world space point.", but when I run the following code:
[code]
    // This line should set the cube in the very top-left corner of the screen. Or not?
    Vector3 playerPos = camera->ScreenToWorldPoint(Vector3(0, 0, 20));
    cubeNode_->SetPosition(playerPos);
[/code]

When screen height is 800 and width is 600:
[img]http://i.imgur.com/m2chHaA.png[/img]

When screen height is 800 and width is 200:
[img]http://i.imgur.com/PMv2ns3.png[/img]

Camera is orthographic, of course. Am I doin' it right? :V 

Here's the [url=https://dl.dropboxusercontent.com/s/vb1mtvrkh20cmbe/ScreenSpacePositioning.zip]code[/url] I used, for your perusal.

-------------------------

JTippetts | 2017-01-02 00:58:10 UTC | #2

It's most likely related to the fact that you never call Camera::SetOrthoSize() or camera:SetAspectRatio() after creating it, so the internal aspectRatio_ member is still 1.0. The aspect ratio is necessary to indicate the ratio between width and height, and if it is 1 then the reverse projection code thinks that the screen is square shaped.

-------------------------

cadaver | 2017-01-02 00:58:10 UTC | #3

Yeah, like JTippetts said, it's the aspect ratio. By default cameras have the autoAspectRatio -mode set, which means they will adjust aspect ratio automatically according to the viewport they're rendering.

However, that adjustment doesn't happen before the camera renders the viewport for the first time! So when you set the node position once on startup, the camera will still have the default square aspect ratio. You can correct this by either setting the aspect ratio manually, or waiting until the viewport has been rendered at least once. In typical cases the mouse would be used to continuously steer an object, in which case it would not be an issue.

-------------------------

Kingsley | 2017-01-02 00:58:11 UTC | #4

Thanks, delaying the initialization until the second frame solves that. However, I want to place objects relative to the screen size when the game starts, and the one-frame delay causes either pop-in or 'teleporting' objects, depending on which initialization frame I create the object's model. 

Assuming there's no way to force it to detect the aspect ratio before the first frame is rendered, can I at least blank out the first frame so nothing is drawn? I tried graphics->Clear(CLEAR_COLOR), but it doesn't seem to have any effect.
I could just overlay a black plane in front of the camera, but we're getting into pretty hacky territory there :I

Also, why is the scripting API with Start/DelayedStart not carried over to the C++ API? Considering it's necessary to writing any sort of reusable components, leaving it to the user feels like unnecessary makework.

-------------------------

cadaver | 2017-01-02 00:58:11 UTC | #5

It's easiest that you set the aspect ratio manually to the camera. Get the screen width & height from Graphics subsystem, convert to floats, divide width with height.

In C++ there are performance considerations. The majority of existing components don't need to subscribe to the scene update or physics update events, so doing that in the base class would be a potential large waste of CPU time. Unlike script, a base class cannot easily detect whether the derived class implements functions like Update() or FixedUpdate(). However, we could add a "game logic component" base class that would subscribe those events and call your virtual Start(), Update() etc. methods.

-------------------------

cadaver | 2017-01-02 00:58:12 UTC | #6

In the head revision (it didn't make it to V1.31) there is now a component called LogicComponent which can be used as a base for updating C++ components. It has Start() / DelayedStart() / Stop() / Update() / PostUpdate() / FixedUpdate() / FixedPostUpdate() virtual functions. By default all update events are subscribed to (perhaps unnecessarily) but there's a function, SetUpdateEventMask(), which can be used to optimize the subscription.

-------------------------

Kingsley | 2019-07-02 19:43:28 UTC | #7

...I could have sworn I tried that. :D

Thanks for LogicComponent! One thing I'm noticing though, is it requires SceneUpdate to be subscribed to for DelayedStart to work. That seems like it could be confusing if someone made a component that requires only, say, DelayedStart and FixedUpdate. 

Maybe a delayed initialization subsystem would be a good workaround, something like this? (LogicComponent simplified for clarity).
https://gist.github.com/Kingsquee/9401301
An approach like this would also save each component instance from needlessly doing delayedStartCalled_ checks each frame, since only the subsystem does that. Not really a performance issue, but unnecessary work feels unpleasant.

-------------------------

cadaver | 2017-01-02 00:58:12 UTC | #8

The physics pre-step (before FixedUpdate call) will also call DelayedStart if necessary. I think that for now a note of this is enough.

EDIT: There were other logic issues in case you would reduce the event mask in the middle of the component's existence, now those should be fixed and DelayedStart() should be called also with a zero event mask.

-------------------------

Kingsley | 2017-01-02 00:58:12 UTC | #9

Yeah..missed that comment somehow. 

I'm going back to bed.

-------------------------

