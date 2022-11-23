Virgo | 2018-02-22 09:30:33 UTC | #1

Im thinking about making a shooter game with Urho3D (as a hobbyist), by so far I have encountered several problems, like:

1. how to do scopes zooming effect
2. how to do voice chat with this engine (i want voice to be played as 3D sounds)
3. how to simulate the bullets, including the dropping and piercing stuffs

weeks gone by and i still have no idea about them, help me!
thanks in advanced.

-------------------------

johnnycable | 2018-02-22 09:49:45 UTC | #2

> how to do scopes zooming effect
- what do you mean?

> how to do voice chat with this engine (i want voice to be played as 3D sounds)

- I don't know

> how to simulate the bullets, including the dropping and piercing stuffs

- using this:

https://discourse.urho3d.io/t/spark-particle-engine-renderer/3670

-------------------------

Virgo | 2018-02-22 09:57:11 UTC | #3

by 1. i meant the display of scaled scene, dont know how to call it, so, "zooming" <3

and 3. hows a particle engine gonna do with bullet simulation...

-------------------------

Eugene | 2018-02-28 03:39:14 UTC | #4

[quote="Virgo, post:1, topic:4036"]
how to do scopes zooming effect
[/quote]

Just camera zoom. If you want part-screen scopes like Escape from Tarkov, it'd requre more complicated solutions.

[quote="Virgo, post:1, topic:4036"]
how to simulate the bullets, including the dropping and piercing stuffs
[/quote]
Custom bullet tracing isn't so hard.
https://github.com/eugeneko/Urho3D-Sandbox-Dirty/tree/networking-prototype/Source/FlexEngine/Physics

[quote="Virgo, post:1, topic:4036"]
how to do voice chat with this engine (i want voice to be played as 3D sounds)
[/quote]
IDK. I'm not an expert in sound networking. Urho support custom network messages.

-------------------------

Virgo | 2018-02-22 10:11:21 UTC | #5

okay, im so stupid and careless, didnt even find the zooming attribute in Camera class.
im checking out your bullet system later, thx <3

-------------------------

Enhex | 2018-02-22 10:12:51 UTC | #6

1. You can manipulate Field of View (FOV) to achieve zooming effect.
EDIT: camera zoom is should be better.

2. You'll need to capture and stream the player's mic input to others, and play it as a 3D sound source.
AFAIK Opus is the highest quality codec available and it's FOSS:
http://opus-codec.org/
I know Discord uses it.

Maybe you can find open source library for voice chat. RakNet lists voice communication in its features, tho it uses an outdated codec.

3. You'll need implement it yourself.
Using the physics engine would probably be expensive and won't solve penetration.
You can come up with penetration calculations using raycasts, so you might as well implement the bullets as raycast steps, which it quite simple (just velocity, gravity, and maybe air resistance).

-------------------------

Virgo | 2018-02-22 14:58:10 UTC | #7

okay, seems i got tons of stuffs to study here
i wonder if there is any example of recording with opus from mic input, i cant find one

-------------------------

Lumak | 2018-02-22 17:03:43 UTC | #8

If you've never created a shooter game before, this might be a good reference - https://discourse.urho3d.io/t/codename-outbreak-remake-sources/876
I learned a lot from that resource.

-------------------------

smellymumbler | 2018-02-22 20:45:47 UTC | #9

Why would you want to reinvent VOIP when you have open-source and battle-tested like https://github.com/mumble-voip/mumble ?

-------------------------

Virgo | 2018-02-23 17:31:53 UTC | #10

I want to play them as 3d sounds :slight_smile:

-------------------------

smellymumbler | 2018-02-23 20:51:32 UTC | #11

You mean positional audio? You can do that with Mumble: https://wiki.mumble.info/wiki/Link

-------------------------

Virgo | 2018-02-24 01:37:32 UTC | #12

okay okay, honestly i just dont want mumble, as i remember, mumble runs as a background program, this sucks.

-------------------------

Sinoid | 2018-02-24 09:54:22 UTC | #13

[quote="Virgo, post:1, topic:4036"]
3. how to simulate the bullets, including the dropping and piercing stuffs
[/quote]

Triangle mesh colliders are hollow, so for those you can just advance the origin of the ray to the backside of the hit point and repeat the trace (+epsilon). The 2nd hit will be a backface where you can check if you want to continue through (ie. surface too deep) or not - a 3rd ray cast is the exiting ray.

Other rigid bodies lack that (unless an AABB is good enough) and bullet doesn't expose the underlying shapes well enough - though you could use MathGeoLib to mirror the shape and use its' ExtremePoint functions to find the opposite side of an object (or just port them over), doing the same thing in 2 ray casts instead of 3.

There's the [GNU Ballistics](https://github.com/grimwm/libballistics) library ... which is probably far beyond what you're after.

-------------------------

Virgo | 2018-02-24 14:26:26 UTC | #14

okay, checked out the example, but just cant understand :( too much math, i cant do that

-------------------------

smellymumbler | 2018-02-25 03:34:06 UTC | #15

3D game development is pure math. I know, it's hard, but you definitely want to read something like this:

https://www.amazon.com/Foundations-Game-Engine-Development-Mathematics/dp/0985811749/ref=pd_cp_14_2

If you want to achieve something. Otherwise you'll just be banging rocks together.

-------------------------

johnnycable | 2018-02-25 11:29:27 UTC | #16

You may be better suited with something like [this](https://www.amazon.com/Artificial-Intelligence-Games-Ian-Millington/dp/0123747317):

![15|402x499](upload://1Pdd3NLu4Eb5qaqBmsXnFfJEx0C.png)

this has the logic in pseudo code form and the base math without getting too much complicated. Relevant to your question:

![00|576x240](upload://kice07qzhRKLntLsPpQlhtWInuq.png)

The everything-base math:

![39|690x288](upload://28TCEswgeNR3Q28GoRh1oYou584.png)

that's for, you know, jumping, so it's really the base...

-------------------------

Virgo | 2018-02-28 03:38:48 UTC | #17

Thank you guys, i think i got the ideas (except the VoIP one though), gotta go study the basics.

-------------------------

