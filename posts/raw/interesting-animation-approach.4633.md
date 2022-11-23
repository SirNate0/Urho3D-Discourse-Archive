smellymumbler | 2018-11-03 02:17:45 UTC | #1

Simple and easy: https://twitter.com/citizen_no7/status/1058368225136775168

-------------------------

JTippetts1 | 2018-11-03 05:29:18 UTC | #2

TLDR for people who don't want to click through to twitter?

-------------------------

slapin | 2018-11-03 11:00:40 UTC | #3

It is about ue4 blendspaces. Godot has thrse too. Urho lacks high level animation constructs (and I think most of developers are against them as these add code.and not needed for tetris and.asteroids clones). If somebody needs these I think entire high level animation tree can be copied from Godot and implemented on top of AnimationController and AnimationState.

-------------------------

slapin | 2018-11-03 16:29:52 UTC | #5

You mess-up blendspaces with blurprint.

-------------------------

Sinoid | 2018-11-03 17:31:40 UTC | #7

@JTippetts1 it's the overgrowth few keyframes thing just done in UE4's blendspaces.

> If somebody needs these I think entire high level animation tree can be copied from Godot and implemented on top of AnimationController and AnimationState.

That's bonkers overkill, 1D and 2D blend spaces are trivial. 3D blend states aren't particularly *hard* either.

Implementing on-top-of instead of as-part-of animation wouldn't be a great idea IMO, because of networking and ice-skating client-side.

-------------------------

slapin | 2018-11-03 18:21:32 UTC | #8

No, it is implemented in C++ and it uses data-driven approach

They are accessible from blueprint for scripting purposes but not have to.

See [https://docs.unrealengine.com/en-us/Engine/Animation/Blendspaces](https://docs.unrealengine.com/en-us/Engine/Animation/Blendspaces)

See [https://docs.unrealengine.com/en-US/engine/animation/blendspaces/overview](https://docs.unrealengine.com/en-US/engine/animation/blendspaces/overview)

Basically, 2D blendspace is 2D plane where you can set points, and each point is assigned animation.

Then you can set blendspace to some value, like Vector2(0.5, 0.1)  and it will result in blending animations

according to that point. Please use the above links for better explanation. The idea is to use single vector
value for blending 200 animations together. Very good technique, I use it in Godot.
[https://godotengine.org/article/godot-gets-new-animation-tree-state-machine](https://godotengine.org/article/godot-gets-new-animation-tree-state-machine)

-------------------------

Modanung | 2018-11-04 15:27:01 UTC | #10

@turbo9 This shouldn't cost too much resources. EDIT: Meant "should **not**" :/

Urho currently _does_ allow you to set weights for each animation. Doesn't this allow the creation of "blendspaces" with a few lines of code?

-------------------------

slapin | 2018-11-04 13:48:53 UTC | #11

This will not cost much at all.
It is just to calculate weight parameters.
I think if some data-driven way existed in Urho to configure AnimationController and states, it would br trivial to implement this tecnique in Urho editor which would skyrocket usability.

-------------------------

slapin | 2018-11-04 13:50:28 UTC | #12

Basically no runtime cost at all for constant case and only tiny time to recalculate weights for runtime modification.

-------------------------

JTippetts1 | 2018-11-04 14:50:04 UTC | #13

Yeah, I honestly don't see how this is any different from just setting animation weights.

-------------------------

smellymumbler | 2018-11-04 22:40:28 UTC | #14

You can't set a curve for the blending between weight values in Urho. I think that's the only difference.

-------------------------

Sinoid | 2018-11-05 01:49:24 UTC | #15

> You can’t set a curve for the blending between weight values in Urho. I think that’s the only difference.

Is the Spline class broken?

---

I suppose there's no reason the AnimationController couldn't forward weights and the like to dynamic attributes (not unlike scripts). That exposes value-animation and whatever other madness anyone cooks up that plays with attributes (I have *linking / binding* in my fork).

-------------------------

Sinoid | 2018-11-05 01:56:15 UTC | #16

There's also a ton of "*well ... that's not so crazy*" simple stuff in the recent talk about Doom-2016's animation.

https://www.youtube.com/watch?v=3lO1q8mQrrg

Nothing really new there (except the *duh* with trajectories), but it's explained with pretty outstanding clarity for such a brief talk. Itching to try out the footstep stuff.

-------------------------

smellymumbler | 2018-11-05 04:22:04 UTC | #17

Just in case anyone needs more info on how it works: https://www.youtube.com/watch?v=7b9WM8TVdpA

https://www.youtube.com/watch?v=vA11a8xEngc

-------------------------

