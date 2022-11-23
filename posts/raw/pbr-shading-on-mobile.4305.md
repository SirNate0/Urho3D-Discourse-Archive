Lumak | 2018-06-10 16:27:45 UTC | #1

While investigating PBR Mobile, I came across Unreal's discussion on the topic, https://www.unrealengine.com/en-US/blog/physically-based-shading-on-mobile And investigating further, I found **EnvBRDFApprox()** fn already exist in our shader.

Applying the *roughness* gradient from 0 to 1:
[img]//cdck-file-uploads-global.s3.dualstack.us-west-2.amazonaws.com/standard17/uploads/urho3d/original/2X/9/919b0a5ea55a055d99880a422330d3ebf46037fe.png[/img]
edit: closer image

Applying it to my model using spec map treated as roughness map:
[img]//cdck-file-uploads-global.s3.dualstack.us-west-2.amazonaws.com/standard17/uploads/urho3d/original/2X/d/d281f5c726834edee325fe1e04091b99ff8f85db.png[/img]

**But** I keep finding topics on how texture fetches are expensive on mobile and tried using a constant reflected value instead of a cube lookup:
[img]//cdck-file-uploads-global.s3.dualstack.us-west-2.amazonaws.com/standard17/uploads/urho3d/original/2X/5/5419e4b9b0f9b3660acb50facbd0989d3686b80e.png[/img]
This I can live with it!

The vehicle images are shown with baked bump/normal applied.

-------------------------

WangKai | 2018-06-11 02:04:42 UTC | #2

I think comparing BPR implementations of different game engine, especially for the mobile is very helpful. I guess it would be very helpful for the guys in the community making their own games choose btw Phong and PBR.

-------------------------

dragonCASTjosh | 2018-06-11 14:03:52 UTC | #3

So the main issue i see currently with the PBR implementation is A) the IBL reflection is not affected by roughness. But its awesome you got it compiled and running, i know that was an issue for a long time

-------------------------

Lumak | 2018-06-11 15:00:29 UTC | #4

I had no idea IBL reflection is not affected by roughness (because the EnvBRDFApprox is a function of roughness). I actually didn't test to see how PBR worked on a PC platform but looked through your shader code and tried figuring out how to mix the returned value from EnvBRDFApprox() with env map and specular. Results are not exact as shown in Unreal's roughness spectrum image but I can live with it.

-------------------------

dragonCASTjosh | 2018-06-13 20:36:10 UTC | #5

I recommend testing your changes on PC OpenGL in order to compare the results between the techniques. After they are the same / similar results then try run it on mobile. The issues with the reflections in your version is currently a big issue because its a key part of the visual results.

-------------------------

