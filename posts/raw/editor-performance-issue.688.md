abcjjy | 2017-01-02 01:02:08 UTC | #1

Once the editor starts, at least one of the cores of the cpu runs at 100% and make my laptop very hot. Is it a known issue? What makes it so cpu consuming?

Thanks

-------------------------

hdunderscore | 2017-01-02 01:02:08 UTC | #2

Yeah it's a bit of a bizarre choice, but even locking fps only locks to 200fps which is well above necessary. One thing you can do is enter this into the F1 console:
[code]engine.maxFps = 30[/code]

You can also change the source so it's always like that.

Best thing would be to make the change change in master branch.

-------------------------

abcjjy | 2017-01-02 01:02:08 UTC | #3

Great, it works fine. For an editor without animation, I think fps 15 is adequate.

-------------------------

cadaver | 2017-01-02 01:02:08 UTC | #4

You can also run with -v command line option to enable vsync. A typical editor app with native GUI would only refresh when something in the 3D view changes, but Urho also renders the UI with GPU as part of the frame update processing and therefore going much below 60fps will likely impact the UI responsiveness. It's not that bad since the mouse cursor will always refresh as fast as you move it.

-------------------------

abcjjy | 2017-01-02 01:02:09 UTC | #5

Is it possible to update only when user input coming in?

-------------------------

cadaver | 2017-01-02 01:02:09 UTC | #6

Not in a sensible manner, or without severe modifications. Urho3D is meant as a realtime game engine and the editor is in a sense a "misuse" of that.

-------------------------

abcjjy | 2017-01-02 01:02:09 UTC | #7

Is that to say the editor is more of a sample than a practical tool? Is it recommended to use the editor in real world project?

-------------------------

hdunderscore | 2017-01-02 01:03:37 UTC | #8

The editor works quite well and is easily extended. You'll need to determine whether it suits your need independently. 

However I bump this post for this: [github.com/hdunderscore/Urho3D/tree/lazy-render](https://github.com/hdunderscore/Urho3D/tree/lazy-render)

If you build the editor with URHO3D_LAZY_RENDER in cmake options on that fork, the editor will only update the graphics when it needs to. Let me know if it works out for you.

-------------------------

