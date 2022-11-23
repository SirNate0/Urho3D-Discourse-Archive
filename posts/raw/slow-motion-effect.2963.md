TheComet | 2017-03-28 11:07:34 UTC | #1

What would be the best way to temporarily slow down the time step in Urho3D to create a slow motion effect? I thought about having my own separate "time step" value, but then I'd have to make sure to multiply it everywhere with Urho3D's timeStep and that seems extravagant.

It would have to work with everything, including physics objects, particles, animation updates, the Update() and FixedUpdate() calls, etc.

-------------------------

Florastamine | 2017-03-28 11:51:33 UTC | #2

Have you looked into [Scene::SetTimeScale()](https://urho3d.github.io/documentation/1.6/class_urho3_d_1_1_scene.html#ac8b0f11b63f431f1e605dd7379f39ede)?

-------------------------

TheComet | 2017-03-28 15:59:31 UTC | #3

Wow! When was that introduced? Works perfectly, thanks!

-------------------------

Modanung | 2017-03-28 17:03:09 UTC | #4

[quote="TheComet, post:3, topic:2963"]
When was that introduced?
[/quote]
At least two years ago.
[quote="TheComet, post:3, topic:2963"]
Works perfectly, thanks!
[/quote]
Splinin' it? ;P

-------------------------

Enhex | 2017-03-28 18:04:58 UTC | #5

Something to keep in mind - Scene::SetTimeScale() doesn't affect sounds.
I don't see any "master frequency" either.

-------------------------

TheComet | 2017-03-28 19:09:55 UTC | #6

It would be super cool if you could somehow apply a lowpass filter on all of the sounds. I haven't done much with Urho3D and sound so hard to say how feasible it is. Maybe someone else knows how you could do this.

-------------------------

