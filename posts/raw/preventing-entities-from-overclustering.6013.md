throwawayerino | 2020-03-25 05:18:37 UTC | #1

I've got a player with a group of AIs after it. Problem is when the player moves they all follow the same path and clip into each other. Would physics collision help fix this?

-------------------------

Dave82 | 2020-03-24 13:51:00 UTC | #2

Are you using the CrowdManager and CrowdAgents ? Don't use physics, it will mess things up even more. Can you show some code ?

-------------------------

throwawayerino | 2020-03-24 13:54:58 UTC | #3

I experimented with physics and so far nothing exploded. I am using `FindPath()` for each character. Are CrowdManagers more efficient/better for moving targets?

-------------------------

Modanung | 2020-03-24 14:50:02 UTC | #4

`CrowdManager`s are meant to be used for groups of entities. Sample 39 demonstrates their use.

Alternatively you could apply the basic rules of [swarm behaviour](https://en.wikipedia.org/wiki/Swarm_behaviour#Mathematical_models) to your AI:
> + Move in the same direction as their neighbours
> + Remain close to their neighbours
> + Avoid collisions with their neighbours

_Casting_ spheres could help with determining which neighbours each AI should "pay attention to".

-------------------------

GodMan | 2020-03-24 21:10:50 UTC | #5

I used a simple capsule for my NPC's. They use a crowd-manger just fine. You do have to be careful with the physics though. It causes strange behavior. 

Also I believe their is a limitation to using a crowd manger, for example the agents can only go to one position or track only one position ieg: track the players position.

-------------------------

