lebrewer | 2020-10-22 00:50:55 UTC | #1

So, I'm considering separating a few animation tracks in my character to solve a few sync issues I've been having. For example, recording an animation with the finger pulling the trigger, or the fingers typing, or the hand grabbing something. My intent is to combine those "small" and "modular" animations into whatever other animation is playing, but those are also combined: legs moving (walk, run) and arms (idle, preparing, defending, attacking, holding something, etc). 

Is it possible to do something like in Urho, as is? Or do I have to come up with a custom blending solution?

-------------------------

Modanung | 2020-10-22 07:03:53 UTC | #2

Run, run while you still can...

[![](https://gitlab.com/luckeyproductions/hantik/-/raw/master/pirmit/structure.svg)](https://gitlab.com/luckeyproductions/hantik/-/tree/master/pirmit)

-------------------------

1vanK | 2020-10-22 07:57:38 UTC | #3

AnimationBlendMode::ABM_ADDITIVE?

 https://urho3d.github.io/documentation/HEAD/_skeletal_animation.html

-------------------------

Modanung | 2020-10-22 07:59:17 UTC | #4

...and `SetStartBone`

-------------------------

lebrewer | 2020-10-26 14:49:04 UTC | #5

I'm sorry, but I don't get it. Run, why?

-------------------------

Modanung | 2020-10-26 17:30:01 UTC | #6

Long story. :slight_smile:

...that sort of started here:
https://discourse.urho3d.io/t/need-a-hand/6390

Only enter the PiRMIT if you think you can handle the curse of the pharaoh. :wink:

-------------------------

Modanung | 2020-10-26 17:50:01 UTC | #7

The upshot of the animation part is to basically make all animations conveniently procedural by grouping bones as tendons, each coupled to a single letter. By defining the min and max rotation of each bone and their respective tendons outside the animations, normalized keyframes should make animations transferable between models, recombinable and easily modifiable on the fly.

So far this is mainly conceptual, and the "Red PiRMIT" [sent me down a lane](https://gitlab.com/luckeyproductions/witch) that has little to do with animation and more with geometry... and so far, *nothing* with Urho. :slightly_smiling_face: 

[![](https://files.gitter.im/572c3ba0c43b8c6019716cff/aPhy/image.png)](https://gitlab.com/luckeyproductions/raddish) |
---|
[![](https://gitlab.com/luckeyproductions/hantik/-/raw/master/Antiq/images/snail_green.svg)](https://gitlab.com/luckeyproductions/hantik/-/tree/master/Antiq) |

-------------------------

