xalinou | 2017-01-02 01:12:51 UTC | #1

What's the best way to blend between single animation keyframes with custom animation curves in Urho? I'm trying to implement the following technique: 

[gdcvault.com/play/1020583/An ... e-Approach](http://www.gdcvault.com/play/1020583/Animation-Bootcamp-An-Indie-Approach)
[blog.wolfire.com/2008/11/procedu ... ion-redux/](http://blog.wolfire.com/2008/11/procedural-animation-redux/)

I've tried using single keyframes as separate states, but i wasn't able to find a way to blend between them inside AnimationController using curves.

-------------------------

Enhex | 2017-01-02 01:12:51 UTC | #2

You could try to extend AnimationController to allow using spline interpolation for the time/fading.
Also possible to make your own class for managing animations.

Relevant: [urho3d.github.io/documentation/H ... ation.html](http://urho3d.github.io/documentation/HEAD/_attribute_animation.html)

-------------------------

xalinou | 2017-01-02 01:12:51 UTC | #3

I'm not sure if i follow. The attribute animation only allows me to apply Linear/Spline interpolated animation routines to objects which accept SetObjectAnimation. Does a bone accept that? Would it be a matter of SetObjectAnimation on each bone, following the position/rotation of the next pose?

-------------------------

Enhex | 2017-01-02 01:12:52 UTC | #4

[quote="xalinou"]I'm not sure if i follow. The attribute animation only allows me to apply Linear/Spline interpolated animation routines to objects which accept SetObjectAnimation. Does a bone accept that? Would it be a matter of SetObjectAnimation on each bone, following the position/rotation of the next pose?[/quote]

Attribute animation can be used for attributes of anything that derives from [url=http://urho3d.github.io/documentation/HEAD/class_urho3_d_1_1_animatable.html]Animatable[/url].

Attributes list: [urho3d.github.io/documentation/H ... _list.html](http://urho3d.github.io/documentation/HEAD/_attribute_list.html)

It doesn't seem AnimationController uses the time as an attribute. That means it will require either extending it or making custom animation controller.

Alternative approach would be to use [url=http://urho3d.github.io/documentation/HEAD/class_urho3_d_1_1_spline.html]Urho3D::Spline[/url] instead of attributes.

-------------------------

namic | 2017-01-02 01:12:54 UTC | #5

Bone data is not an attribute, so, that approach would not be possible. You will have to extend the animation controller and, for each bone, apply your custom interpolation routine between frames. How are your animations structured? Full rigid frames or different animations for each pose?

IMHO, different animations for each pose would be easier to blend. So you have one animation called "walking_pose1" and "walking_pose2" and you can interpolate, and call that "walking".

-------------------------

Enhex | 2018-02-15 16:38:36 UTC | #6

You don't need to do it per bone, you just need to control the weight of each animation.

-------------------------

burt | 2018-02-14 14:53:18 UTC | #7

Is there any documentation or example on how to switch blending modes between animation frames?

-------------------------

Eugene | 2018-02-14 15:47:40 UTC | #8

[quote="burt, post:7, topic:2077"]
how to switch blending modes between animation frames?
[/quote]

Could you elaborate what blend modes do you mean?

-------------------------

Modanung | 2018-02-15 17:16:06 UTC | #9

Could this be what you're looking for?

`bool` **`AnimationController::SetBlendMode`**`(const String& name, AnimationBlendMode mode)`

Also, welcome the forums @burt! :confetti_ball:

-------------------------

burt | 2018-02-16 23:25:12 UTC | #10

Thank you! I'm not sure. AnimationBlendMode seems to only allow either Additive or Lerp. How can i customize how the frames are blended by using a ease-in/ease-out function and the time it should interpolate?

Imagine that I have just two frames, with very different poses:  Legs together, legs apart. I want to customize how those two are blended to create a real time animation based on how fast the character is going, etc.

-------------------------

Sinoid | 2019-02-22 01:17:00 UTC | #11

Necromancy!

**MotionWheel**, does the surveyer's wheel tracking. It's fairly robust but be aware that it's really only designed for 1 direction recording (it can do forward/back along the given axis, but it's not well suited for that), so recording the 4 ground-plane directions requires 4 components.

Basically, component tracks the accumulated motion along a vector (dotted for accuracy) and provides a *wheel* with arbitrary *ticks* to facilitate intelligible fractions out of it and visual interpretation. Or just use it to record how long as something has been falling, do watch out for being sure to use `Reset`/`Resize` for teleport or changes in gait.

Working on a different controller that does the **DOOM** method with pie-slices and void-blend zones on the surface-plane.

https://gist.github.com/JSandusky/d0e077b5527a07400bf11cfaad67a30e

---

Utilities for yanking keyframes out of animations. Pretty poorly tested (and edited immediately before being gist uploaded to strip out *phases* and morph tracks that don't exist in master). 

You can use a 3 key run animation Overgrowth style but then use a curve to select frame times to extract out a 30 key animation that has been sigmoid squashed or w/e (sample sigmoid/logit adjusted, but output linear).

More useful as a base.

https://gist.github.com/JSandusky/2c590178c23c4ce958fd9a1d0c1c7ccc

-------------------------

