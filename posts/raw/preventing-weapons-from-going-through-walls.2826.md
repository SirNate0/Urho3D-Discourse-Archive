smellymumbler | 2017-02-28 18:49:03 UTC | #1

I'm building a small FPS example in Urho and i'm facing the following bug that i also experienced in Unity: https://www.youtube.com/watch?v=9kekrsZzLG8

However, i don't know how to fix it in Urho. Any tips?

-------------------------

1vanK | 2017-02-28 19:28:15 UTC | #2

Camera::SetViewMask()
(but it is not cool method - shadows from another objets do not drop on weapon)

-------------------------

jmiller | 2017-02-28 19:46:43 UTC | #3

Similar question is asked with solutions here:
http://discourse.urho3d.io/t/how-to-control-render-order/1240

-------------------------

smellymumbler | 2017-02-28 20:05:53 UTC | #4

First of all, thanks for the quick replies! :grin:

I've checked that thread before, but that solution comes with a bug: when inside a wall, the weapon is shadowed. During gameplay, this is very noticeable. Is there another way of doing this with Urho?

-------------------------

1vanK | 2017-02-28 20:09:24 UTC | #5

At the moment, I believe, the best method is move gun backward (or to side) when gun collides to objects. This is done in many modern games

-------------------------

smellymumbler | 2017-02-28 20:14:25 UTC | #6

Pushing back without IK would look terrible, as if the player was going into aim down the sights. Or am i not understanding correctly?

-------------------------

1vanK | 2017-02-28 20:18:32 UTC | #7

I do not understand why you need IK here, just move model with hands backward

-------------------------

smellymumbler | 2017-02-28 20:23:34 UTC | #8

Because if i just move the weapon model and the arms model along the Z axis, it's going to look as if it was zooming in and out, not actually moving the arms to avoid collision. The only proper way of doing that is to rotate the elbow bone and also the hand bone, OR some sort of IK to avoid collision. That's why i chose the camera fix in Unity, easier.

-------------------------

jmiller | 2017-03-01 06:00:08 UTC | #9

I thought the above thread actually addressses the shadow issue (but perhaps with some caveats) :)

-------------------------

HplusDiese | 2017-03-03 19:17:06 UTC | #10

What about projection matrix hack for this? Useful thing.

-------------------------

1vanK | 2017-03-03 19:51:00 UTC | #11

> What about projection matrix hack for this? Useful thing.

 http://discourse.urho3d.io/t/depthhack-for-weapon-rendering/2202
no one know how to do it )

-------------------------

HplusDiese | 2017-03-04 03:05:22 UTC | #12

You can use custom Render Path command for drawing fps related stuff.
Maybe i implement it later.

-------------------------

