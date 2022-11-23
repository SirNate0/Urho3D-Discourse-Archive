Marcin | 2017-10-19 05:38:11 UTC | #1

Hi!
I have a similar case as in "20_HugeObjectCount." I have many boxes, but I need to be able to move them, and delete just like in Minecraft, and be able to dynamically change the color or texture of some boxes. With a large number of boxes (eg. 10000) and 3 viewports, greatly decreases my performance. How to optimize it? Boxes for now have no texture, just the color (diffuse). Grouping them as "20_HugeObjectCount" causes that depending on the camera position, boxes instantly change color to pale. I'm not sure what is the reason. How to best optimize it with such a large number of objects to be able to move, delete, and change the color or texture?
Thanks in advance.

-------------------------

cadaver | 2017-10-19 05:38:05 UTC | #2

Don't attempt to do MineCraft with individual block objects. Instead have custom code which builds a mesh from the visible edges of your world. No generic-use 3D engine is going to do MineCraft with acceptable performance when each block is an individual scene node / renderable object.

-------------------------

Marcin | 2017-03-02 13:04:49 UTC | #3

Hi,
Could occluding be suitable/helpful in this case? In order to not draw boxes which are at the back. Is somewhere info how to use the occluding, maybe some example?

-------------------------

Eugene | 2017-03-02 13:56:40 UTC | #4

Occluding may be helpful. However, it won't help to render 100k boxes with acceptable performance.

-------------------------

Marcin | 2017-03-03 06:27:41 UTC | #5

In front will be about 3-5k visible boxes, rest of them will be behind and should be invisible. Is somewhere info how to use the occluding? maybe some example?
Thanks in advance.

-------------------------

Eugene | 2017-03-03 08:46:54 UTC | #6

[quote="Marcin, post:5, topic:2410"]
Is somewhere info how to use the occluding?
[/quote]
Built-in occlusion is just some flag in settings, so it'd be easy to enable/disable it.

However, you shall understand that neither occlusion nor anything else will help you draw scene with 100k cubes with acceptable performance.

-------------------------

