x6herbius | 2018-06-16 16:08:25 UTC | #1

I've created a custom UI element which will resize 4 viewports depending on how a middle quad-divider is dragged. However, I'm finding that when I resize the viewports, the FPS rate will reduce as time goes on.

https://www.youtube.com/watch?v=YTe20POg-ME

(Forgive the mouse not being 100% on the divider, I'm currently only paying attention to the position delta in the event data just to make it work.)

I'm still getting drag events through and logged as fast as I drag in the UI, but the viewports don't update for sometimes almost a second afterwards.

Could this be an issue to do with the OpenGL buffer allocation/deallocation internal to the View3D? Is there anything I can do to mitigate it?

-------------------------

TheComet | 2018-06-18 10:15:32 UTC | #2

This is actually hilarious.

-------------------------

Eugene | 2018-06-18 10:34:01 UTC | #3

Could you try other graphic backends?

-------------------------

x6herbius | 2018-06-18 13:01:01 UTC | #4

I could give it a try, but I'm currently working mostly on Mac/Linux, so I'd have to dig a Windows machine out.

-------------------------

Eugene | 2018-06-18 13:17:03 UTC | #5

Could you make small sample then? On top of standard Urho samples, if possible.
Viewport resizing isn't good operation as it leads to constant resource recreation.
Maybe driver gets crazy because of it. Maybe some defect in Urho.
I'll think about workaround.

-------------------------

x6herbius | 2018-06-18 20:30:25 UTC | #6

The repo I was using is https://github.com/x6herbius/calliper-urho3d, which is still very small. I have a build script to build the engine from a sub-repo, but pointing the CMake tree at an existing SDK installation should work.

If that's not suitable, I'll look into creating something from scratch over the next few days when I have time.

-------------------------

