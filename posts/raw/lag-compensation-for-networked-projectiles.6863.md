lebrewer | 2021-05-26 18:21:38 UTC | #1

I've been reading and working on top of the NinjaSnowWar sample project in order to come up with a basic networked game. One of challenges I've been facing is lag compensation and projectiles. I've read a little bit on how the Source engine does it:

https://developer.valvesoftware.com/wiki/Source_Multiplayer_Networking#Lag_compensation

But I'm still not sure how that applies in Urho. Do I have to, on every frame, get all reported positions for the project + the player, and do a Slerp based on server time, and see if the hit was probable or not?

-------------------------

JSandusky | 2021-05-27 05:56:03 UTC | #2

Is your game competitive? If it's cooperative than you can just rely on the client like the Monster Hunter series has done for more than a decade in order to operate on poor latency devices (PS2, PSP, 3DS).

-------------------------

lebrewer | 2021-05-27 19:54:36 UTC | #3

Yes, competitive. Although I'm not really worried about cheating, since this not likely have enough traction, and even if it does, it is supposed to be played among friends and not really building a community around it.

-------------------------

George1 | 2021-05-28 04:56:49 UTC | #4

There is a network prediction demo floating around in this new forum.

-------------------------

vmost | 2021-05-29 00:34:10 UTC | #5

[quote="George1, post:4, topic:6863"]
in this new forum.
[/quote]

Where?
20characters...

-------------------------

George1 | 2021-05-31 00:50:39 UTC | #6



Search for "network prediction"

-------------------------

vmost | 2021-05-29 17:07:55 UTC | #7

You said 'in this new forum'. This discourse forum has been around over a year... I was seeking clarification not condescension.

-------------------------

George1 | 2021-05-31 01:31:43 UTC | #8

I understand. We just need to search for the correct keyword.  The older forum has many other stuffs which might not being brought over to this one. It has been many years.   By the way, I like the new front page from Wei Tjong. Nice modern looking.
Cheers.

Just a side note.  There is an Urho3d archived, which contains some nice demo from previous guys.

https://github.com/urho3d-archive
There is a SceneReplication network demo that allows to change gear from Lumak.  The demo in the current version needs to be updated with this feature.

-------------------------

Enhex | 2021-06-01 18:54:31 UTC | #9

old & probably outdated of client side prediction, maybe one of the forks updated it:
https://github.com/Enhex/Urho3D-CSP

Note that i don't maintain it anymore, so you're better off forking instead of making PRs.

-------------------------

