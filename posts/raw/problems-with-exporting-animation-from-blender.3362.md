DainTorson | 2017-07-16 18:16:59 UTC | #1

So, I'm trying to export animation from Blender with this plugin:
https://github.com/reattiva/Urho3D-Blender

However, during exporting process I have the "Object has no animation to export error" and .ani file is not being generated.

The settings I'm using:
<img src='//cdck-file-uploads-global.s3.dualstack.us-west-2.amazonaws.com/standard17/uploads/urho3d/original/1X/2b02504127f8d5d56c3369df3091381054354fad.png'>

The model I'm trying to export:
https://drive.google.com/open?id=0B1_Bnxyx1nNfd1lmUU1FelBuSW8

Any help will be useful.

-------------------------

1vanK | 2017-07-17 21:59:48 UTC | #2

Select "All actions" in list under "Animations"

-------------------------

rasteron | 2017-07-16 19:37:28 UTC | #3

For models with animations, another fast option is to export it to FBX and just convert using AssetImporter.

-------------------------

Modanung | 2017-07-17 16:39:12 UTC | #4

Or **unmute** the NLA track named _[Action Stash]_ and **Push Down** the other animations.

Since you wouldn't want to export pose libraries.

-------------------------

JTippetts | 2017-07-16 23:19:12 UTC | #5

I feel like a guide on doing animations in Blender might be useful. I'm able to get it done, but I'm certain I'm not really doing it 'right'. The Blender animation system has gotten pretty complex lately.

-------------------------

rasteron | 2017-07-16 23:25:51 UTC | #6

[quote="JTippetts, post:5, topic:3362"]
The Blender animation system has gotten pretty complex lately.
[/quote]

I agree, that's why this 2 step works for me

**Blender (FBX) -> AssetImporter (MDL + ANI)**

Of course the FBX exports settings needs to setup properly, depending on your animations or preference.

-------------------------

Modanung | 2017-07-17 14:19:08 UTC | #7

[quote="JTippetts, post:5, topic:3362"]
The Blender animation system has gotten pretty complex lately.
[/quote]

I think it's quite sensible. Once you understand that many 3D viewport [commands](http://www.luckeyproductions.nl/blenderhotkeys.html) apply in the Graph Editor too, as well as the _[Fake user](https://docs.blender.org/manual/en/dev/animation/actions.html#working-with-actions)_ concept for saving unused Datablocks... in my experience it works really well.

For looping animations it's best to set the start frame to be 1 (in the NLA Editor after pushing down) and have an identical key set on the 0th and last frames, btw. This to avoid double frames while keeping the animation continuous. The _Start at frame zero_ option should be disabled on the exporter in this case.
It's also worth looking into [F-Modifiers](https://docs.blender.org/manual/en/dev/editors/graph_editor/fcurves/fmodifiers.html).

A [proper rig](https://www.blenderguru.com/tutorials/introduction-to-rigging) can save a ton of work _and_ improve your animations once you get the hang of constraints.

-------------------------

Mike | 2017-07-17 12:25:52 UTC | #8

Slightly off topic, I've recently investigated the longstanding issue reported by Vivienne [here](https://discourse.urho3d.io/t/solved-exporting-animation-please-remove/898), which plagues MakeHuman users (and everyone of us to a lesser degree).

From the tests I've ran, the boost at export can range from seconds to minutes for average users, depending on number of bones and animation length. For MakeHuman users it can save hours or days.

You can find details [here](https://github.com/reattiva/Urho3D-Blender/issues/60) .Testers are welcome :rabbit:

-------------------------

DainTorson | 2017-07-17 22:02:25 UTC | #9

Lots of thanks, it did the trick. However, I've faced with two more problems:

1. Exported model has some bones, which stick out from the model. Is this an export bug or have I done something wrong?
2. The model is rotated clockwise on 90 degrees. Can I somehow reset this rotation during the export process?

-------------------------

DainTorson | 2017-07-17 22:00:49 UTC | #10

I will definitely try it, thanks. :)

-------------------------

1vanK | 2017-07-17 22:21:18 UTC | #11

you can select forward direction in export settings

-------------------------

rasteron | 2017-07-18 01:07:07 UTC | #12

Sure thing. Here's the Wolf file loaded and exported using Blender FBX to AssetImporter in less than a minute with your animations.

<img src="//cdck-file-uploads-global.s3.dualstack.us-west-2.amazonaws.com/standard17/uploads/urho3d/original/1X/ed7134934a42267d2b4a6d347202265ff176641b.jpg" width="268" height="469">

-------------------------

Mike | 2017-07-18 15:48:29 UTC | #13

Takes 4 seconds when checking 'Read actions by Fcurves' option.

-------------------------

DainTorson | 2017-07-18 18:58:35 UTC | #14

Can you please post the exact arguments you supplied to AssetImporter? I've failed to export animation properly and furthermore the model is rotated on 180 degrees.

-------------------------

rasteron | 2017-07-19 00:22:43 UTC | #15

Try this..

`Assetimporter model Wolf.fbx Wolf.mdl`

Usually the animations are separate and I have noticed in this file, the animations are also exported with just the `model` option. You can also configure the FBX export orientation with Forward and Up option.

<img src="//cdck-file-uploads-global.s3.dualstack.us-west-2.amazonaws.com/standard17/uploads/urho3d/original/1X/0b3b54d36d7f61b3acdcee03f54d314c335b4890.png" width="222" height="175">

-------------------------

