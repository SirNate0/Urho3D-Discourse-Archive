x6herbius | 2018-05-31 21:08:45 UTC | #1

Hi,

I found this engine this evening and it looks like it'd be very useful for a personal project of mine (a 3D level editor), but I have a few of questions regarding some of the technical aspects:

* I see that the co-ordinate system is X-right Y-up Z-forward. The co-ordinate system I'm required to use for compatibility with the Source engine is X-right Y-forward Z-up. Would it be feasible to somehow use/coerce this within the Urho3d engine? I have before in other code used a final transform just before projection to flip the latter two axes, but I suspect this wouldn't play nicely with Euler angles since pitch and yaw would end up being swapped too.
* Does the engine have high DPI support? I've tried the samples on my MacBook and the UI is rather small in many of them. Alternatively, would there be support to just run the engine in a lower resolution and scale the resulting frames up at a window manager level?
* This one's not so critical, but is there any support (or would support be planned) for multi-window functionality? It'd be nice to be able to spawn off sub-windows belonging to the engine so that I can take advantage of multiple monitors.

Thanks.

-------------------------

johnnycable | 2018-06-01 19:17:37 UTC | #2

[quote="x6herbius, post:1, topic:4276"]
Does the engine have high DPI support? I’ve tried the samples on my MacBook and the UI is rather small in many of them. Alternatively, would there be support to just run the engine in a lower resolution and scale the resulting frames up at a window manager level?
[/quote]

You can run the sample at a lower resolution by setting window width and size to your liking. If you plan to use full resolution, then you need upscaled compatible assets... like you were doing 2x 3x assets for iphone. Those are not included in the standard urho package.
Last but not least; mind the editor doesn't work on Os X. There's a running bug preventing you to click and point correctly, so probably that angelscript app needs some fixing. As of now I hadn't any problem in c++.
As for you other questions, I don't know. HTH

-------------------------

hdunderscore | 2018-06-02 01:01:18 UTC | #3

For HighDPI, I don't think there are enough contributors to test HighDPI contributions, however there is a pending pull-request that touches on it, perhaps you could take a look at and leave comments: https://github.com/urho3d/Urho3D/pull/2272 

For co-ordinate system, Urho3D supports matrices as well, so your solution could work. Alternatively, simply exporting the model into the urho-preferred coordinate system might also work.

-------------------------

x6herbius | 2018-06-02 10:28:24 UTC | #4

The biggest thing for me at the moment is how to solve the co-ordinate system problem. I don't want the user to even have to know that there are two co-ordinate systems (it's confusing enough for me converting between the two), so I'd need to allow them to work only in the Z-up system.

Ignoring the Y-up convention, working as if Z were up and then applying a pre-projection transformation to flip back to OpenGL's system would work as far as the scene is concerned, because I've done it before. However, it does mean that Euler angles would still be applied as if Y were up, resulting in pitch and yaw affecting the opposite axes to the ones that they should in a Z-up system. I did take a look at the engine code to see whether anything could be done about this, but due to the fact that vectors are used interchangeably for Euler angles, and that there's no encapsulation on the X/Y/Z components, it doesn't look like it'd be easy to change the behaviour of Euler angles.

In addition, objects in the engine that assume internally that the co-ordinate system is Y-up (the most significant example being cameras) would continue to do so, even though the scene itself would not correspond to that co-ordinate system.

DPI-wise, I'll have a look at that pull request and see if it's something I can test on my Mac.

-------------------------

SirNate0 | 2018-06-02 13:36:31 UTC | #5

If the users won't be touching the code (i.e. they will never create our use a Vector3 directly but only see them in UI and logs and how you label axes) you can probably just convert to Urho's system on import and back on export and then in all of your UI's print vectors as "X: {v.x_} Y: {v.z_} Z: {v.y_}" and then do a similar trick to negate the Euler angles if needed (positive angles are probably opposite of what the users are used to).

-------------------------

x6herbius | 2018-06-03 20:17:06 UTC | #7

Not quite sure why the last post was withdrawn, I read the e-mail notification for it and it was quite informative. I guess the most sensible way will probably end up being to use the Y-up system for everything editor-wise and then convert to/from Z-up on export/import. The question then becomes how best to insulate the user from the potential awkwardness that entails, but I guess that's part of my application design.

-------------------------

