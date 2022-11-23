Lumak | 2017-04-12 20:03:52 UTC | #1

Just another one of those projects that got me curious and had to code it to see if it'd work.
Using the water shader from the last project - it looks pretty good :grin:

repo: https://github.com/Lumak/Urho3D-Buoyancy

https://youtu.be/GnQhrGUrPq0

-------------------------

sabotage3d | 2017-04-11 23:26:49 UTC | #2

Nice! Did you attach a constraint at the bottom of each object?

-------------------------

Lumak | 2017-04-11 23:58:48 UTC | #3

No, no constraint of any kind.  Just applied Archimedes' Principle and his buoyant force eqn.

-------------------------

johnnycable | 2017-04-12 12:36:43 UTC | #4

Great! I had this thing on the back of my mind for so long! Never found the occasion to build it. Glad to see it can be done in urho!

-------------------------

Lumak | 2017-04-12 20:05:38 UTC | #5

created a repo, link on top of the page.

-------------------------

suncaller | 2017-04-13 16:37:04 UTC | #6

Cool stuff as usual, although I must say the water looks more like jello here :laugh:

-------------------------

Lumak | 2017-04-13 23:00:26 UTC | #7

Especially when it looks this delicious from the side.

[url=https://ibb.co/fyHQbQ][img]//cdck-file-uploads-global.s3.dualstack.us-west-2.amazonaws.com/standard17/uploads/urho3d/original/1X/3e05132ccace85af053f69a5b2ad3d866e53bcea.jpg[/img][/url]

-------------------------

Lumak | 2017-04-14 18:52:32 UTC | #8

updated repo: changed under water reflection and added smooth cam.
I think that's the last of the updates, although, I found Rasterson's underwater shader while googling under water distortion and that maybe a cool thing to add in the future.

-------------------------

coldev | 2017-04-15 16:35:47 UTC | #9

nice share codes .. God Bless You

-------------------------

slapin | 2017-04-15 18:16:49 UTC | #10

Please add underwater stuff, that will help me understand how to do underwater location transition
(i.e. getting and exiting water and diving and moving under).

-------------------------

Lumak | 2017-04-15 19:00:28 UTC | #11

Only check required is:

    if (waterBbox_.IsInside(cameraNode_->GetPosition()))

which checks to see if the cam is inside the water's bbox.

-------------------------

Bluemoon | 2017-04-17 13:48:21 UTC | #12

:astonished: 
This is awesome, playing around with it is cool as well. Great Work

-------------------------

Lumak | 2017-04-17 20:58:54 UTC | #13

Glad you're enjoying it :slight_smile:

-------------------------

Miegamicis | 2017-04-18 14:35:44 UTC | #14

This is awesome! Great work!

-------------------------

LanceJZ | 2017-08-19 19:26:40 UTC | #15

Wow, thank you so much for sharing this! This is so awesome! I can learn so much from this!

-------------------------

