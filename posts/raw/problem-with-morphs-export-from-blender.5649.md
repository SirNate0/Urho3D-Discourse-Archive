Elendil | 2019-10-06 18:15:44 UTC | #1

I creted two morphs in blender. I animated them and allways I export the model, logger give me warrning "Empty shape 1" and "Empty shape 2".

How to correct export morphs from Blender? I use https://github.com/reattiva/Urho3D-Blender

![MORPHS1|690x277](upload://aMW9OgY5G3ZORKlWM6fT5SUXJVL.jpeg) ![MORPHS2|219x500](upload://kBk3OwOqRUaKFniUmlBpZqVqz97.jpeg)

-------------------------

Modanung | 2019-10-07 09:36:21 UTC | #2

Could you share the Blend?

-------------------------

Elendil | 2019-10-07 09:46:48 UTC | #3

I found solution

1. Morphs doesn't need animations in Blender.
1. Shape Keys must be relative.
2. In settings ApplyModifiers must be checked (under some time I can't unchecked it if i have morphs checked, it is strange)
3. Normals
A) If model have flat shading Normals must be unchecked from Morphs export. But in Urho3D morphs will have not correct morphs = object can have holes on model edges.
B) If model is Smoothed then Normals must be checked from Morphs export. Then it is correct.

[quote="Modanung, post:2, topic:5649, full:true"]
Could you share the Blend?
[/quote]
Yes. I upload it on [dropbox](https://www.dropbox.com/s/bsp3r3byhvpx8lb/morphShapesTest.zip?dl=1) because forum can handle zip or blend files.

-------------------------

Modanung | 2019-10-07 09:41:54 UTC | #4

[quote="Elendil, post:3, topic:5649"]
It take some time.
[/quote]

But since you solved the problem, I guess there is no need.

-------------------------

Elendil | 2019-10-07 09:45:21 UTC | #5

It happens :) but for others when wants to check how to export morphs.
https://www.dropbox.com/s/bsp3r3byhvpx8lb/morphShapesTest.zip?dl=1

-------------------------

