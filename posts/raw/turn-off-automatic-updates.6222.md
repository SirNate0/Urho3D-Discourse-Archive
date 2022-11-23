btschumy | 2020-06-26 10:43:43 UTC | #1

My app is updating at around 60 FPS even when nothing is going on.  Is there a way to turn off the automatic updates and request updates only when needed?  I am concerned about battery drain when the app is just siting there with no user interaction.

I've looked in the Scene and Application classes since that would be a likely place for this feature, but don't see anything.

-------------------------

jmiller | 2020-06-24 14:15:47 UTC | #2

There are `Engine::SetMaxInactiveFps()`, `SetMaxFps()` etc.
  https://urho3d.github.io/documentation/HEAD/class_urho3_d_1_1_engine.html

And there are a few analogues in the engine parameters:
  https://urho3d.github.io/documentation/HEAD/_main_loop.html

-------------------------

btschumy | 2020-06-24 14:59:19 UTC | #3

Thanks for the suggestions.  I hadn't looked at Engine.

This app is currently running on iOS using UrhoSharp.

`Engine.MaxInactiveFps = 5;`

Doesn't seem to do what I need.  The app still spins at 60 FPS while it is just sitting there.

I suppose what I can do is use a timer and set MaxFps to something low when there has been no user interaction for the past 5 seconds or so.  Then when there is interaction I can bump it up to 60 and reset the timer.

This is what I had to resort to when using SceneKit on iOS.  I was hoping there was a built-in way to do this in UrhoSharp.

-------------------------

Virgo | 2020-06-24 15:52:59 UTC | #4

i suppose inactive means when app loses focus, not "when nothing is going on"

irrc, someone asked this question on the forum before, and the answer is there is no easy solutions?

-------------------------

SirNate0 | 2020-06-25 04:29:42 UTC | #5

I'd recommend 10 or 20 fps personally. Waiting up to .2 seconds for the app the respond to you if it enters that state sounds unpleasant.

-------------------------

btschumy | 2020-06-24 17:50:53 UTC | #6

That's exactly what I had to do in SceneKit.  I set the idle FPS to around 10 FPS.  If I set it lower there would be a noticeable lag when first tapping to drag the view.

-------------------------

