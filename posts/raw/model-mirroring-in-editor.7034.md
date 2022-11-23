niansa | 2021-11-02 19:11:27 UTC | #1

Hey, how do I mirror an object in the Urho Editor?
https://media.discordapp.net/attachments/800371248114434069/905172082076295278/IMG_20211102_200218_422.jpg

Thanks
Tuxifan

-------------------------

kannsokusha | 2021-11-03 04:35:04 UTC | #2

Set scale -1 on the axis?

-------------------------

Eugene | 2021-11-03 07:14:03 UTC | #3

I only want to warn you that scale=-1 isn't guaranteed to work consistently everywhere. E.g. it will flip the visuals just fine, but it may break physic collider of the model, or navigation, or something else.
Some things will work just fine, but keep an eye out.

-------------------------

niansa | 2021-11-03 08:05:43 UTC | #4

What would the solution be in this case?

-------------------------

Modanung | 2021-11-03 08:30:34 UTC | #5

Simply use more than one node for the object.

Also, welcome. :confetti_ball: :slightly_smiling_face:

-------------------------

JSandusky | 2021-11-04 10:13:39 UTC | #6

[quote="Eugene, post:3, topic:7034"]
I only want to warn you that scale=-1 isn’t guaranteed to work consistently everywhere. E.g. it will flip the visuals just fine, but it may break physic collider of the model, or navigation, or something else.
[/quote]

Navigation should work, provided that physics works as well since navigation tries to pull box, tri-mesh, and convex-hull physics shape geometry when possible as those SHOULD be faster to voxelize (it was a pretty massive speed up during testing, fewer triangles to process == good, should also be more accurate as to the consequences physics cause for navigation). Edit: not sure if it was @scorvi  or @JTippetts1 that wrote it, it wasn't me. I did test it enough for basic cases.

Physics SHOULD be stuff internal bullet if anything doesn't work ... I think? I don't see anything that looks ignored as far as setLocalScaling goes and so on. I wouldn't be surprised if btAdjustInternalEdgeContacts doesn't work correctly for scaled trimeshes or so on ... I can barely read that function, it's written in problem-domain-expertise.

-------------------------

