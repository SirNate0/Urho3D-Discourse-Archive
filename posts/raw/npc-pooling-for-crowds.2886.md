slapin | 2017-03-12 18:04:50 UTC | #1

Hi, all!

I want to implement large amount of NPCs in world, i.e. keeping track of their state/action.
So I want to store position and general state for each NPC.
As soon as player comes closer to NPC he should see NPC doing something logical which is done according to schedule and impulses. So it should not be spawned out of sudden. Also, NPCs should be dynamic
so as time passes they change their occupation and location, and this location should be logical, i.e.
like leave work at 18:00, get in car and go home, and anywhere on path NPC could be intercepted.

What I think is that when player is distant, NPCs at locations are randomly spawn, as they are far from NPC,
the low-poly version is spawn, which does distant-behavior (simplified, just motion or idling or some
occupation animations like phone talking), no IK or physics or navmesh applied. All actions are according to place or spawn point. As player comes closer, the motion becomes physics-based, navmesh is used for reference, IK is applied for some animations like walking, interaction is possible between player and NPCs and between NPCs, behavior becomes complex and models are replaced by high-poly versions.

if player follows NPC, he can get for all his scedule. Other NPCs use standard spawning/removing.
I don't understand yet how to handle this, but I think this should be possible, probably keeping track of a set of closest NPCs and never remove them. So there should be some distance where NPCs are collected and spawned and inside this zone no collection and spawn should happen.

Any suggestions on how I could implement this? Which Urho features can be used?

-------------------------

