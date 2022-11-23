Jens | 2021-06-08 12:42:49 UTC | #1

I have a character model, which needs to be movable. Unfortunately, parenting between mesh and bones causes strange problems when exporting via fbx - either the material is not drawn where it should be (is somehow deformed), else it is omitted altogether.

At first I'd thought the mesh is messed up; however, looking at the fbx model in a viewer shows the mesh  intact, whilst the material either isn't present, or in the wrong position. For example with just a single bone, the hands are not visible, and part of the head is incorrect.

I do have software experience inc. c++ games (long time ago); however, here I'm using Urhosharp for an android application and am trying to learn as I go. I would imagine that Urho3d would also have problems with this model, since it nearly must be a problem with AssetImporter. Having said that, there are a lot of Blender (v2.92) options I'm not 100% sure of, so it could also be a problem with me. For example, maybe the mesh (approx. 9000 triangles) is too complex, and should be simplified. Having said that, the model renders perfectly when no bones attached. ANY help would be much appreciated, thanks.

-------------------------

SirNate0 | 2021-06-03 14:07:16 UTC | #2

[quote="Jens, post:1, topic:6871"]
At first I’d thought the mesh is messed up; however, looking at the fbx model in a viewer shows the mesh intact, whilst the material either isn’t present, or in the wrong position. For example with just a single bone, the hands are not visible, and part of the head is incorrect.
[/quote]

Wouldn't this indicate that it is a problem with Blenders fbx exporter, as opposed to something to do with the AssetImporter? If so, you might want to try the blender add-ons that directly export to Urho's model format.

Also, welcome to the forum!

-------------------------

Jens | 2021-06-03 14:26:19 UTC | #3

[quote="SirNate0, post:2, topic:6871"]
Wouldn’t this indicate that it is a problem with Blenders fbx exporter, as opposed to something to do with the AssetImporter? If so, you might want to try the blender add-ons that directly export to Urho’s model format.

Also, welcome to the forum!
[/quote]

Thanks very much!

I should maybe of mentioned this, but importing the fbx file back into Blender works fine (at least as far as material rendering goes).

Unfortunately, the blender add-on does not work with the newest versions of Blender. Though, if there seems to be no solution to this, my only option might be to try an older version + add on.

-------------------------

SirNate0 | 2021-06-03 16:55:34 UTC | #4

According to another user there is a branch of the add-on that does work with Blender 2.92

https://discourse.urho3d.io/t/what-are-the-options-for-dealing-with-animations/6840/4

-------------------------

Jens | 2021-06-06 19:10:21 UTC | #5

[quote="SirNate0, post:4, topic:6871"]
According to another user there is a branch of the add-on that does work with Blender 2.92
[/quote]

Ok, that's good to know, thanks. Having tried the add-on, the problem persisted, so I tried to download another model to see what happens. Again, once an armature is applied to the mesh, render problems occur. Bit more dramatic this time in that the right arm and part of the chest are simply not rendered. The mesh is taken into Urho3d (via c# wrapper) as an AnimatedModel, with the .SetModel method's boolean argument (create bones) set to true. Strangely, if this is set to false there is no apparent change - the skeleton still has a bone, and the rendered model still misses an arm. A material is then applied from a solid colour.

The only clue I can find, is that both models had a warning in the add-on export details:
'Incompatible vertex elements in object....'

Nonetheless, I'm completely baffled as to what is happening, especially since the model renders perfectly when the armature is deleted. I've uploaded some screen shots of the differing model in the android emulator, plus the blender workspace. I was hoping to upload the actual blender file, in the hope that someone more knowledgeable might figure out what is wrong, but this is not allowed.

![NoBoneAndroid|350x500, 50%](upload://uTYFnLqO72vtKHqsjDS5eQKifAL.png)

-------------------------

Jens | 2021-06-06 19:11:00 UTC | #6

It turns out that new users can only upload one item:
![SingleBoneAndroid|360x500, 50%](upload://vsZUVJg1s1nazIafN4LWX8sPeYI.png)

-------------------------

Jens | 2021-06-06 19:12:18 UTC | #7

![SingleBoneBlender|467x500, 50%](upload://6e79xrTjUomAozMrAJsOhJBw7Al.jpeg)

-------------------------

SirNate0 | 2021-06-07 00:33:28 UTC | #8

The error in the exporter looks like it's due to missing blend indices or something like that. Try making sure all the vertices have at least one bone with nonzero weight.

-------------------------

Jens | 2021-06-08 12:47:22 UTC | #9

You are correct - on my full skeleton rig, changing parenting from auto to envelope weights fixed this. I thought that'd already been tried, but apparently not. Single bone tests were not useful, as it seems a single bone will not correctly set weights on all vertex groups.

-------------------------

