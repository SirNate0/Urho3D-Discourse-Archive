Lumak | 2017-07-01 07:31:40 UTC | #1

Not sure what to call it really, but it helps characters walk over objects.

You'll get what I mean in the video - [b]need a better name![/b]

https://youtu.be/YQZGtH5VJzQ

-------------------------

johnnycable | 2017-07-01 10:52:36 UTC | #2

What about portable steps?:wink:

-------------------------

S.L.C | 2017-07-01 15:40:27 UTC | #3

Foot Bridge
Field Traversal
Byway Solver

-------------------------

Lumak | 2017-07-01 16:59:09 UTC | #4

Pedo-Porter?

I like portable steps so far.

-------------------------

Modanung | 2017-07-01 17:14:59 UTC | #5

Step flaps?

>:business_suit_levitating: 
>:hole:

-------------------------

Lumak | 2017-07-01 17:51:00 UTC | #6

If you're considering naming it, do it fast because I'm done with the implementation and testing.  Whatever the name I choose will become the github repo name.

-------------------------

johnnycable | 2017-07-01 22:16:06 UTC | #7

Voxel Paddles? (---lots of characters here---)

-------------------------

Cpl.Bator | 2017-07-01 22:23:30 UTC | #8

DuckStep ?  (---lots of characters here---)

-------------------------

slapin | 2017-07-01 23:34:28 UTC | #9

NightWalk? (the silly fliller for 20 character limit, hehehe)

-------------------------

rasteron | 2017-07-02 02:07:20 UTC | #10

I'd simply name it **UrhoStep**, so it sounds something like **Euro step**, that basketball move..

https://en.wikipedia.org/wiki/Euro_step

-------------------------

weitjong | 2017-07-02 02:36:50 UTC | #11

EnvironmentAwareCharacterController (no filler needed, pun intended)

-------------------------

Lumak | 2017-07-02 22:47:18 UTC | #12

Thank you all for your suggestions, but I decided on this:

https://github.com/Lumak/Urho3D-Height-Stepper/

edit: changed the default stepUpDuration value in the repo.
edit2: updated repo once again- added surface step normal and max height checks.

-------------------------

Lumak | 2017-07-03 16:50:42 UTC | #13

I don't like how this works and just may try something else. There are two limiting factors that I dislike, both related to animation and should do away with relying on animation all together.

-------------------------

Lumak | 2017-07-03 21:05:44 UTC | #14

Revamped:
* stepper no longer relies on the foot or animation
* removed dbg textures
* charImpulse is no longer defaulted to true 

If anyone was testing this, I'd appreciate any feedback on the new implementation.

-------------------------

Lumak | 2017-07-04 04:55:09 UTC | #15

Ok, I'm wrapping this up. repo updated - steppernode is no longer enabled/disabled in the stepperenable() function to save btrigidbody from being destroyed and re-added to the world.

One should consider calling stepperenable from the Character class when jumping/falling to prevent the stepper from catching on to a side of a wall or whatever.

-------------------------

slapin | 2017-07-05 17:41:34 UTC | #16

Hi,
have you tried to benchmark how many characters it can run at the same time?

-------------------------

Lumak | 2017-07-05 19:12:52 UTC | #17

I haven't specifically benchmarked the height stepper, but I have benchmarked kinematic, trigger bodies that constantly move in the world - see

[quote="Lumak, post:19, topic:3182"]
Stress test
[/quote]

-------------------------

