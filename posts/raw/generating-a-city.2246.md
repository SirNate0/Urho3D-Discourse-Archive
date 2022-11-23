slapin | 2017-05-11 22:41:47 UTC | #1

Hi all!

I experiment with generating of city from scratch:
https://youtu.be/A9AxA8P7dw0

I came upon idea as generating of all little building details using algorithms might be troublesome task
I want to make some parts (like window frames, etc.) in Blender and then combine them into building.

The problem is if I just instance them like nodes, I have some CPU load problems and have too much geometry due to
culling issues. I want for the whole building to have just one bounding box, so I want merged geometry.

I use AngelScript to produce geometry which is quick enough for the job.

I produce road network and buildings procedurally then make models out of that geometry.
The building consists of 4 facades as separate nodes. This produce some splitting artifacts when I rotate camera,
and as windows are separate nodes too, they also separate from remaining geometry.
I want to join whole building into single geometry, including separate model parts.
I tried straightforward approach - [b]model.GetGeometry()/model.SetGeometry()[/b]
and combine all into one Model. But for some reason, while there is no produced errors,
the resulting model is not rendered. Is there some example of simple model combining?
I need separate geometry anyway for parts which use different materials (but I want to merge geometries
for all parts using the same material). Any ideas, suggestions?

-------------------------

slapin | 2017-05-11 22:42:08 UTC | #2

My older Godot Engine demo is [youtube.com/watch?v=j99vFXPXHHA](https://www.youtube.com/watch?v=j99vFXPXHHA)
and I want to implement somthing like thos PoC (Godot engine) [youtube.com/watch?v=c8Cu_VzcL2Y](https://www.youtube.com/watch?v=c8Cu_VzcL2Y) in Urho.

-------------------------

horvatha4 | 2017-01-02 01:14:13 UTC | #3

Hi!
Maybe, an interesting thread for you: [discourse.urho3d.io/t/iogram-wip/2072/13](http://discourse.urho3d.io/t/iogram-wip/2072/13)

-------------------------

slapin | 2017-01-02 01:14:14 UTC | #4

Well, my goal is much more specialized.

Regarding this I have a question - what is the process of creating Model with several Geometries?

-------------------------

Modanung | 2017-05-12 19:22:20 UTC | #5

3 posts were split to a new topic: [Comparing engines](/t/comparing-engines/3117)

-------------------------

