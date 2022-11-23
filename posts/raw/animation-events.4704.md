smellymumbler | 2018-12-01 09:37:35 UTC | #1

Is it possible to create some sort of "event" that triggers from a specific point in an animation playback? I'm trying to tie a "footstep" sound to the moment that the foot touches the ground.

-------------------------

Sinoid | 2018-11-30 20:36:01 UTC | #2

See `AnimationTriggerPoint` and `Animation::AddTrigger` (Animation.h).

-------------------------

weitjong | 2018-12-01 00:34:57 UTC | #3

NinjaSnowWar shows how to do that.

https://github.com/urho3d/Urho3D/blob/master/bin/Data/Scripts/NinjaSnowWar/FootSteps.as

-------------------------

smellymumbler | 2018-12-01 01:21:54 UTC | #4

Thank you so much, guys! I swear I couldn't find this in the docs.

-------------------------

