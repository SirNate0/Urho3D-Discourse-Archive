Leith | 2019-02-18 08:56:56 UTC | #1

I've set up a character with an outer physics hull, and deeper in the same hierarchy, some ragdoll bodyparts are attached to various bones. When the app begins, I get E_PHYSICSCOLLISIONSTART twice, which is specifically about the Foot Bodies touching the ground.
But I never get E_PHYSICSCOLLISIONEND during walk cycles - it seems the fact that a parent body that remains in contact with the ground, prevents the E_PHYSICSCOLLISIONEND event from being issued in child bodies. I'll be able to confirm this very soon, by disabling the outer physics hull, but I wanted to know if this is a known issue before I go digging around to find out why this is happening.

I'm subscribing anonymously to these events, as they are not sent to any node.
I also plan to move to node events, but I suspect the same issue will apply.

I should have added - I set up the collision layers and masks carefully.
This is for a Non Player Character:

Outer Hull has CollisionFilter::NonPlayerCharacter, CollisionFilter::Static
Bodyparts have CollisionFilter::NonPlayerCharacter, CollisionFilter::Static || CollisionFilter::PlayerCharacter

Finally, here's my physics filters:
[code]
enum CollisionFilter
{
        Default = 1,
        Static = 2,
        Kinematic = 4,
        Debris = 8,
        Trigger = 16,
        PlayerCharacter = 32,
        NonPlayerCharacter = 64,
        Everything = -1 //all bits sets: DefaultFilter | StaticFilter | KinematicFilter | DebrisFilter | SensorTrigger
};
[/code]

-------------------------

Modanung | 2019-02-18 09:05:05 UTC | #2

Could it be the parent and child nodes are colliding non stop? To be sure you _could_ name the nodes and output the names of colliding node pairs.

-------------------------

Leith | 2019-02-18 09:05:28 UTC | #3

parent and child are masked to never collide

-------------------------

Leith | 2019-02-18 09:05:54 UTC | #4

they are in the same group, but their mask indicates they can never hit each other

-------------------------

Leith | 2019-02-18 09:06:28 UTC | #5

my understanding of bullet physics groups and masks is: I am in this group, I can hit those groups

-------------------------

Modanung | 2019-02-18 09:08:19 UTC | #6

If I'm correct, the collision _mask_ defines the _layers_ a body can collide with.

-------------------------

Leith | 2019-02-18 09:08:57 UTC | #7

layers is an urho term for groups in bullet, but its the same idea, binary flags, bitmasking

-------------------------

Leith | 2019-02-18 09:09:45 UTC | #8

AND masking is used in bullet to determine collisions

-------------------------

Leith | 2019-02-18 09:10:42 UTC | #9

I specifically omitted the group "non player" from being able to ever be hit by another "non player", for the purposes of this test

-------------------------

Leith | 2019-02-18 09:17:06 UTC | #10

I'm willing to hook up the continual collision event and debug spew it to be sure its not my fault, but I feel like I'm going to be wading around in urho guts again very soon sigh
I have a horrible feeling from memory that Bullet only uses 16-bit masks, but even so, I'm only using 7 bits

-------------------------

Modanung | 2019-02-18 09:21:30 UTC | #11

[quote="Leith, post:10, topic:4940"]
I’m willing to hook up the continual collision event and debug spew it to be sure its not my fault...
[/quote]
If I had a dime for every time I wrongly blamed Urho in the beginning... ;)

-------------------------

Leith | 2019-02-18 09:24:33 UTC | #12

I know, still, I did due diligence with the masking stuff, so it's got me baffled - more debug, then wade around in the source as a last resort, given there are no easy answers for complex questions, willing to dig for answers, and post them

-------------------------

Leith | 2019-02-18 09:25:15 UTC | #13

my concern is that urho might treat shape trees as compounds by default

-------------------------

Leith | 2019-02-18 09:27:08 UTC | #14

bullet has compound shapes, I suspect urho puts all the child shapes into a compound, I hope not, I doubt this is generally useful, and i bet theres no way to opt out

-------------------------

Leith | 2019-02-18 09:53:21 UTC | #16

I further suspect, that urho does not look for end of contact events in children of its compounds
I am here to help, all I can find on my travels, will be revealed, some of it will be PR'd and hopefully well received - Unity made me a worse coder in one year, but I got paid, I got paid to develop games, and also to sell unity solutions, outside of their framework, without the possibility of seeing my fixes make it into the engine.
Here, I can give my fixes, sure I won't be paid, but I can share what I learn, and fix what's broken.
I'm a qualified toolmaker - a trade that no longer exists. I can basically repair anything electromechanical or not, and if it's too far gone, I can reproduce it from a bar of shit, I am among the last of a dying trade

-------------------------

Leith | 2019-02-19 07:16:30 UTC | #17

OK! I found that the foot bodies were never colliding with the floor (the two collisions I was seeing were the outer hull of player and non player, with the floor),
I feel silly - look at the symbol I used for "or" - I have a logical or (||), I wanted a binary or (|).

[quote="Leith, post:1, topic:4940"]
Bodyparts have CollisionFilter::NonPlayerCharacter, CollisionFilter::Static || CollisionFilter::PlayerCharacter
[/quote]

I expanded one foot body to a ridiculous size to ensure it collided with the floor, and I am receiving that event - so I'm fairly confident that I'll now be able to also receive the end of collision event as well.

[EDIT]
Yep, we have "lift-off" :smiley:
At this point I'll switch from using anonymous collision handling events, to node-specific events (since each bodypart is owned by a unique and well-named node), and start experimenting with using foot collisions as a guide to detecting footfalls, as opposed to using animation triggers. This should allow me to apply my foot-planting solution "early" when walking up a slope, and "late" when walking down a slope. I'll probably still need to use IK to find a proper position for the pelvis based on the animated pose, looking forward to backporting the results into the existing IK Sample, and will offer resulting code back to the community via PR.
Oh, I've also realized that I can probably omit the foot bodies, if I extend the length of the lower leg bodypart down past the ankle, to the heel, ie, until it touches the zero plane.

-------------------------

Leith | 2019-02-20 07:04:20 UTC | #18

I switched to node collision events, because global handlers are prohibitively expensive to service in a complex environment.
I'm still having issues, but it's a different issue - I am getting the "collision ended" event just a few frames after "collision started" - when you walk forward, and plant a foot on the ground, it's meant to stay planted for a fair while, what the hell? My zombie foot is a kinematic animated body, since the animation says the foot is down, it should stay down, I should not be told that collision has ceased.

-------------------------

Modanung | 2019-02-20 09:25:45 UTC | #19

Maybe this has to do with the order of events since the animation will lift the foot (and end collision) before any correction are made?

-------------------------

Leith | 2019-02-20 10:35:53 UTC | #20

its happening way too soon

-------------------------

Leith | 2019-02-20 11:42:51 UTC | #21

https://www.youtube.com/watch?v=Nwsyr5gAEuM

-------------------------

