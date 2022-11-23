smellymumbler | 2017-05-24 18:27:21 UTC | #1

Does Urho have anything similar to the standard Character Controller in Unity 5?

https://docs.unity3d.com/Manual/class-CharacterController.html

-------------------------

S.L.C | 2017-05-24 19:35:13 UTC | #2

Check the character example. That should give you an idea of what's available.

-------------------------

slapin | 2017-05-24 19:55:42 UTC | #3

No, but you can ad-hoc yourself your own one. See examples.

-------------------------

smellymumbler | 2017-05-24 20:46:39 UTC | #4

Yes, but the character example is missing a few things like isGrounded, minMoveDistance, radius, slopeLimit, stepOffset, etc... it's just a very basic controller. I was looking for a more core component.

-------------------------

slapin | 2017-05-24 21:01:17 UTC | #5

I think you can make one like in Unity in about a day. The problem is you often want more...
But I think if Urho had some builtin character controller for starter, that would not hurt either.
You can manage without it, but you don't have to. Probably somebody could just add character
from Bullet - that one is not very nice, but it do not require too much work to implement and it can be useful for some people.

-------------------------

jmiller | 2017-05-25 02:27:19 UTC | #6

[b]hdunderscore[/b] posted his character controller in that most extensive topic:
https://discourse.urho3d.io/t/character-controller/1468/28

For blending animations, there's JSandusky's animation motion controller script.
https://gist.github.com/JSandusky/340b09e9d104bae4c16b

-------------------------

