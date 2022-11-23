mcmordie | 2020-10-08 03:34:17 UTC | #1

Does Urho3D support rendering the same scene to multiple OS-level windows via different cameras / shaders?  I have done some digging and it doesn't look like it, but I see SDL seems to support this, so I am reasoning that it should be possible:

https://discourse.libsdl.org/t/does-sdl2-actually-support-multiple-windows/25933

I am extending an application which renders via multiple cameras to multiple RenderSurfaces, but all of these are displayed within the same SDL window (as textures within the scene).  I see that multi-window support is not a critical use case for Urho3D users, but in my case there is not alternative-- I have multiple output displays which need to be driven simultaneously with the same scene.

If it is not already supported, can somebody outline for me what I need to think through and implement to get it done?  To me it looks like the graphics class really wasn't intended to do this, and I am hoping to do minimal damage to make it work and maybe even generate a PR to share this work.  I would also appreciate a guestimate of how hard this is likely to be.


Thanks!

Dave

-------------------------

Eugene | 2020-10-08 21:32:34 UTC | #2

[quote="mcmordie, post:1, topic:6420"]
If it is not already supported, can somebody outline for me what I need to think through and implement to get it done?
[/quote]
Something like that was done for Dear ImGUI integration in the fork:
 https://github.com/rokups/rbfx/blob/master/Source/Urho3D/SystemUI/SystemUI.cpp
I don't know all the details, but the general idea was to let ImGUI handle multiple windows and use render to texture for rendering into windows provided by ImGUI.
`Graphics` was left untouched and I don't see any realistic way to add multi-window support there.

Last time I checked it worked ok-ish with rare layout bugs on ImGUI side.
So, that's the easiest way: let ImGUI handle this stuff and glue it to `Graphics` with a couple of hacks.

-------------------------

mcmordie | 2020-10-08 20:23:38 UTC | #3

Thank you for your guidance on this.  I am sure you are right, but I am also stubborn.  What I see is that Graphics is 1:1 with the SDL Window.  If I create a second Window by creating other Graphics object sharing the same context (setExternalContext), I get another window, with rendering to the first one still working.  What I don't understand is how set up a second renderer and viewport so that they work with this second window.  What is driving my stubbornness is that I think I know how to make this work in OpenGL, but of course we are multi-platform and I am roughing this in on D3D9 / Win10.   Is this a totally lost cause, or is there potential feasibility to make this work through SDL?

-------------------------

Eugene | 2020-10-08 21:32:33 UTC | #4

[quote="mcmordie, post:3, topic:6420"]
If I create a second Window by creating other Graphics object
[/quote]
`Graphics` is singleton, you cannot create another instance of it.
Well, you can do that technically, but it's not expected (and was never designed) to work in defined way. First (but not last) obstacle is abundance of mutable static variables in `Graphics/*`.

I predict one of the following outcomes:
1) It will crash or assert;
2) Only first `Graphics` will work properly, others will be disabled or broken;
3) Multiple instances of `Graphics` will interfere with each other in unpredicatble ways;
4) Any combination of items 1-3.

I neither know nor care enough to try estimating the scope of such task (which is equivalent to overall `Graphics/*` refactoring).

-------------------------

mcmordie | 2020-10-08 21:11:53 UTC | #5

Wow that is super helpful, especially as I overlooked the static vars and since the constructor is public I assumed it was not a singleton.  So if I wanted to take a stab at this it would have to start with building a multi-instance/multi-window version of Graphics and then probably spiral out of control into crazyland breaking every other class in a codebase I have zero experience with.  Sounds like a party.

One last question while I have your ear: if I went down this rabbit hole, would *anyone* else benefit from this?  The reason I ask is that I notice that Unity3D supports this, so there must be some demand for it.

I guess the only sane option in Urho3D  is the first one you outlined.  Thanks for staying with me to make the case.

-------------------------

Eugene | 2020-10-08 22:42:23 UTC | #6

[quote="mcmordie, post:5, topic:6420"]
I went down this rabbit hole, would *anyone* else benefit from this?
[/quote]
In my opinion, risks outweight the benefits.

You don't exactly need multiple native windows for _games_, I don't remember I have ever played 3D game with more than one window.

And if you need it for tools, then ImGUI+Render-to-texture is much simpler and less invasive solution than trying to refactor whole `Graphics` stuff.

-------------------------

mcmordie | 2020-10-08 22:48:47 UTC | #7

Got it.  Thanks again for your help!

-------------------------

