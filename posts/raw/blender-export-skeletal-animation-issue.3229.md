hcomere | 2017-06-08 20:44:11 UTC | #1

Hello,

I am trying to export a blender model with skeletal animations using https://github.com/reattiva/Urho3D-Blender/ addon.

It is all ok excepted for skeletal animations, i have the following warning :
```
Object xxxObject should have the same origin as its armature xxxArmature
```

I have checked 10 times the object's origin and the armature's origin in Object Mode, they are both to 0. 0. 0. :frowning:

Is there a nuance that i didnt see ?

Regards,
Harold

-------------------------

jmiller | 2017-06-09 07:09:05 UTC | #2

Hello,

If you have not yet, perhaps try 'apply location'?

And it seems that warning should not appear if 'global origin' option is selected.
[code]    if not tOptions.globalOrigin and meshObj.location != armatureObj.location:[/code]

-------------------------

Mike | 2017-06-09 05:48:54 UTC | #3

It is a scaling issue, you certainly have resized your armature and not your meshes.
Use apply scale before exporting.

-------------------------

johnnycable | 2017-06-09 07:00:37 UTC | #4

That normally means your rest pose is not in sync with vertices...

-------------------------

hcomere | 2017-06-09 07:08:21 UTC | #5

Hello,

Applying Location fixed the problem, thanks all :)

Regards,
Harold

-------------------------

