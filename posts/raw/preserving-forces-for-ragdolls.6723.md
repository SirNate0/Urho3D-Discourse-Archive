evolgames | 2021-02-19 19:55:08 UTC | #1

I have an issue with ragdoll forces.
In my game, NPCs are animated and have simple collision capsules around them. Upon a collision (with a force threshold) they will become ragdolls. This works similar to the Ragdolls sample.
So, if you smash a car into them they instantly go limp. It's realistic enough, but there's an issue.
The force from hitting the NPC (at 50mph, for example) should send them flying with the hit limbs moving more, but because the capsule merely detects the collision that impact is lost. The ragdoll is created without any forces on it. So I need a way to get any forces that would impact the ragdoll on specific parts before it's created. Not sure if that makes sense. 
Any ideas? Should I have it created at all times or something?
I was also considering physics prestep collision events or translating the ragdoll a bit back on a collision (though high speeds might not work for that)

-------------------------

SirNate0 | 2021-02-20 07:42:43 UTC | #2

You should be able to get the forces on the capsule from the collision. You could then apply them to the ragdoll so it goes flying, figuring out the direction and position of the force. If that still doesn't look good in terms of the limbs I would suggest either applying a small random force to each limb or have a few presets (like forces that would make the NPC curl into a ball or spread its limbs out like a cartwheel) and see if that looks satisfying.

-------------------------

Modanung | 2021-02-20 10:07:39 UTC | #3

You could also copy the velocity of the replaced rigid body, or is it a trigger?

-------------------------

evolgames | 2021-02-21 17:26:49 UTC | #4

These are some good ideas, thanks. I'll give them a try and see if that suffices. It's not a simulation so it doesn't need to be accurate, just look 'real enough.'

-------------------------

evolgames | 2021-02-21 17:30:34 UTC | #5

So I did tried this and it helps, though not a full solution. Bumping a capsule and hitting specifically legs or arms at certain angles produce fairly different results. But it does help because there is a huge expectation that the npcs will be pushed back first.
I think I might need to do a combination of things, maybe some random forces like Nate said.

-------------------------

