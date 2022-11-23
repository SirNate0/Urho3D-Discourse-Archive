TEDERIs | 2017-01-02 01:12:55 UTC | #1

I'm working on forest rendering system. And faced with the need to show on the screen chunks with lots of objects inside. But standard octree check the visibility of each individual object which significantly reduces the speed. Is it possible to disable the octree and manually determine which objects to draw and which are not?

-------------------------

Modanung | 2017-01-02 01:12:55 UTC | #2

Enhex's answer seems to hit the metaphorical nail on the head.

-------------------------

Enhex | 2017-01-02 01:12:56 UTC | #3

Try StaticModelGroup, the description says it does culling as a single unit:
[urho3d.github.io/documentation/H ... group.html](http://urho3d.github.io/documentation/HEAD/class_urho3_d_1_1_static_model_group.html)

-------------------------

