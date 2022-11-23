GodMan | 2020-12-04 20:15:53 UTC | #1

Is it possible to have agents that don't track just one point on a navigation mesh or crowd agent? 

For example lets say I have 10 agents apart of a crowd navigation. Is it possible to have them track different positions instead of all of them moving to one location?

Thanks

-------------------------

Eugene | 2020-12-04 22:13:02 UTC | #2

Target positions can be set for each agent individually.
https://github.com/urho3d/Urho3D/blob/master/Source/Urho3D/Navigation/CrowdAgent.h#L100

-------------------------

GodMan | 2020-12-05 07:15:00 UTC | #3

I will look this over..
Thanks  @Eugene

-------------------------

evolgames | 2020-12-08 02:01:53 UTC | #4

I've done this in a WIP game and can verify it works how you want it to.
The crowd can be told to go somewhere together, which is fine, but not what you want. They avoid each other great, though. So what I do is I set each individual agent's target position using the function Eugene referenced. I think the Sample has the first agent go to the exact group destination and each other npc is a random point somewhere near (in a radius around it), however you can override that and just set all those targets to anywhere on your navmesh. I use script objects to track where they are and when they arrive at their destinations (for example with waypoints) and then set the next one.

-------------------------

