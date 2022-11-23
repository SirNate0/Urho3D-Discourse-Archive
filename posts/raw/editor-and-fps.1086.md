globus | 2017-01-02 01:05:19 UTC | #1

[b]Urho3D[/b] editor show in FRAPS [b]~250 fps[/b] stable

[b]Blender3D[/b] editor show [b]~0-5 fps[/b] if i do nothing
and when i quick rotate scene or move 3d object
fps is up to [b]60 fps[/b] (may be limit in blender)

In Godot engine editor FPS also how in Blender.
Only limit ~20 fps.

Question:
When i work in Urho3D editor my hardware do big work (always)  
It may be necessary to revise the method of updating in editor?

-------------------------

cadaver | 2017-01-02 01:05:19 UTC | #2

There is a branch for lazy render by hd_:

[github.com/hdunderscore/Urho3D/tree/lazy-render](https://github.com/hdunderscore/Urho3D/tree/lazy-render)

However the UI code becomes a bit dirty, as it's checking for any changes and forcing a render in that case.

-------------------------

globus | 2017-01-02 01:05:19 UTC | #3

Okey.
I think, this is target of branch:
"Initial lazy rendering for GUI applications -- attempt to only render? 
? when the UI is updated, or when otherwise told by a call to Renderer::SetRenderFrame."

-------------------------

thebluefish | 2017-01-02 01:05:21 UTC | #4

It is also possible to do this by using Render-To-Texture. [url=https://github.com/scorvi/Urho3DSamples/tree/master/06_InGameEditor]Scorvi's C++ Editor[/url] does this, and by extension [url=https://github.com/thebluefish/Editor-Demo]my branch[/url] also does this (though not by default, the option is there). It should be possible to implement in Angelscript as well.

-------------------------

Bananaft | 2017-01-02 01:05:23 UTC | #5

I've just added "engine.maxFps = 60;" into editor.as , sure, not as efficent as blender's 0-5, but at least my GPU fan won't buzz like it is about to takeoff.

-------------------------

globus | 2017-01-02 01:05:43 UTC | #6

I got the same effect as a [b]FPS in Blender[/b].
When I tested the one game engine,
if the application window is not in focus - all the contents of the window 
is updated only when cursor is moved over. 
When the cursor does not move anything not updated (including animation, particle effects, etc.)
[b]FPS[/b] - from [b]0[/b] to the [b]limit[/b].

-------------------------

