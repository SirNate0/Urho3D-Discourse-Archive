lebrewer | 2020-11-06 22:26:05 UTC | #1

I've been trying to implement a small feature on my third-person character. When his arms touch any surface, I was trying to rotate the pelvic bone so you never have arms inside geometry, for example. I'm doing a raycast, but when it hits, how can I get the pelvic bone from the raycast callback?

-------------------------

evolgames | 2020-11-07 00:35:55 UTC | #2

I did something that is not as elegant as it probably could be. I have ragdoll-like collision shapes ready to go at character creation, rather than just a large capsule. I needed to do ragdolls *anyway* so raycast hits on those collision shapes are easy to track. Then you can just grab the corresponding bone and manipulate it.

-------------------------

lebrewer | 2020-11-09 13:15:27 UTC | #3

Oh, that's really smart. Thanks, i'll try that approach!

-------------------------

