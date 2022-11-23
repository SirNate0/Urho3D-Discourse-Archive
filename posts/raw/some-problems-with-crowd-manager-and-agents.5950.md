Dave82 | 2020-02-28 21:56:47 UTC | #1

After testing the crowd manager and agents a bit deeper i found some limitations and possible bugs/paradox effects that i really can't track down what would happen if i do certain things. Maybe we should create another tutorial/discussion topic and discuss these issues because sooner or later other people will face the same problems.

1. SetEnabled doesn't seem to work with crowd agents. Your only chance to stop the crowd agents from updating and moving is removing the component from the node. That could be a real pain once you plan adding more complex logic to your enemies instead of moving along a path to a certain destination

2. Due to this behavior, another question arises. Consider the following example (Angelscript code)
[code]
CrowdAgent@ ca = node.GetComponent("CrowdAgent");
ca.Remove();
[/code]
This will indeed remove the agent from the crowd but ca still holds a reference to it. So once ca goes out of scope the CrowdAgent object will be deleted. But what happens if in the meantime the crowdManager is removed or recreated ? Will the agents be notified of this change or still use their invalid crowdManager_ weakPtr (which was deleted previously) ? 

3. We need more helper functions to have more control over the agents. For simple demo purposes where agents follow a simple path until they reach their destionation the current state is ok but adding logic to enemies requires lot more control and access (length of the current path , path points). How can i  activate my agent only if the distance between the player and the agent reaches a certain value without knowing the path distance ?

4. Crowd can only have one target. So if you have two players and you want both of them to be attacked by a crowd of enemies at the same time you can't do that. 

5. I think the ground distance should be irrelevant in crowd navigation. Right now the agents won't move if the ground isn't close enough to their feet (still can't understand how it works but maybe i'm doing something wrong ?) The y position of the agents should be controlled by gravity and the path should be calculated on a ZX plane

So these are the limitations i found in the navigation system. If someone had found some workarounds for these problems feel free to post it here
Thanks

-------------------------

lezak | 2020-02-28 15:05:16 UTC | #2

[quote="Dave82, post:1, topic:5950"]
SetEnabled doesn’t seem to work with crowd agents. Your only chance to stop the crowd agents from updating and moving is removing the component from the node. That could be a real pain once you plan adding more complex logic to your enemies instead of moving along a path to a certain destination
[/quote]

I'm unable to reproduce this. I'v checked it by adding ability to disable agents in sample and agent stops when disabled. There are also other ways to stop agent: SetTargetVelocity to 0 or set target position to current position.

[quote="Dave82, post:1, topic:5950"]
* Crowd can only have one target. So if you have two players and you want both of them to be attacked by a crowd of enemies at the same time you can’t do that.
[/quote]
CrowdManager::SetCrowdTarget has second paramter - Node*. If it's passed it will set target only for agents that are atteched to child nodes. So it's possible to have two groups of enemies attacking different targets, just put those enemies under different nodes.

[quote="Dave82, post:1, topic:5950"]
We need more helper functions to have more control over the agents. For simple demo purposes where agents follow a simple path until they reach their destionation the current state is ok but adding logic to enemies requires lot more control and access (length of the current path , path points). How can i activate my agent only if the distance between the player and the agent reaches a certain value without knowing the path distance ?
[/quote]
I have not checked crowd source code, but when using crowd managment path will adapt itself to the surroundings (obstacles, other agents on move) so propably You will not get one path that is valid from setting target to the moment when agent reaches it. You can check CrowdManager::DrawDebugGeometry to see how to receive points to target.
As for activating agent, it would be probably better to use triggers and not navigation system.

[quote="Dave82, post:1, topic:5950"]
I think the ground distance should be irrelevant in crowd navigation. Right now the agents won’t move if the ground isn’t close enough to their feet (still can’t understand how it works but maybe i’m doing something wrong ?) The y position of the agents should be controlled by gravity and the path should be calculated on a ZX plane
[/quote]
Urho uses third party library for navigation (recast/detour), so it works like it's designed in this library, also what You think that "should be" is kind of project specific - for example if Y position should be controlled by gravity, what to do when project is not using physics? If the path should be calculated only on flat plane how to handle building with multiple floors? That being said, there are some ways to implement custom behavior - there's a <a href="https://urho3d.github.io/documentation/1.5/class_urho3_d_1_1_crowd_agent.html#a5975f317bdc1d689a945408e3e049083">CrowdAgent::SetUpdateNodePosition</a>. You can disable it and implement custom node reposition logic that uses physics. Another way would be to use custom class instead of CrowdAgent - NavigationMesh and CrowdManager provide several methods to find paths (and do other stuff) without using crowd agents.

-------------------------

GodMan | 2020-02-28 16:52:55 UTC | #3

So basically you posted some of the issues I had. Many users said that we must be doing something wrong. I also noticed that agents can on track one position only. Which works fine for me. I never tried to track two different positions. Nice find.

-------------------------

Dave82 | 2020-02-28 17:06:53 UTC | #4

[quote="lezak, post:2, topic:5950"]
I’m unable to reproduce this. I’v checked it by adding ability to disable agents in sample and agent stops when disabled. There are also other ways to stop agent: SetTargetVelocity to 0 or set target position to current position.
[/quote]

Yes it stops but once i start to move and reset my target pos , the agent is re-added to the crowd again (debugging crowd agents shows this behavior. Try moving your target while the agent is disabled i use 1.7 btw)

[quote="lezak, post:2, topic:5950"]
You will not get one path that is valid from setting target to the moment when agent reaches it
[/quote]
That's not what i was suggesting. My suggestion was to get the current generated path (path this frame) so i can check i'ts length. If the enemy is far away stop movement and e.g play idle animation. If the path length is below some value , activate the agent and start moving towards target.

[quote="lezak, post:2, topic:5950"]
for example if Y position should be controlled by gravity, what to do when project is not using physics?
[/quote]

I didn't explained this well. By gravity i didn't really mean physics gravity, but to have y as an idependent value (e.g follow slopes by raycast). As i mentioned if the agent is slightly above or under the navigation mesh "floor" then the agent isn't moving (probably the path is invalid).

-------------------------

dertom | 2020-02-28 18:51:23 UTC | #5

[quote="Dave82, post:4, topic:5950"]
As i mentioned if the agent is slightly above or under the navigation mesh “floor” then the agent isn’t moving (probably the path is invalid).
[/quote]

You might want to use navMesh's FindNearestPoint(..) to get a valid point on the navmesh.

-------------------------

SirNate0 | 2020-02-28 21:54:32 UTC | #6

[quote="Dave82, post:4, topic:5950"]
That’s not what i was suggesting. My suggestion was to get the current generated path (path this frame) so i can check i’ts length. If the enemy is far away stop movement and e.g play idle animation. If the path length is below some value , activate the agent and start moving towards target.
[/quote]

You may have some scenario that requires this, but this seems like a really expensive test to find the distance to a target. A simple Vector3 Length check seems much more suitable than calculating the path to the target, or perhaps a raycast. If it's an indoors issue where the path may take lots of turns I would suggest zones - enemies in this and the neighbor zones can attack or are on guard, others are idle. Maybe as a final case confirm that the actual path that would be taken is short enough, to handle the cases of barriers and such.

That said, I do agree that some sort of CalculatePathLength or GetCurrentPathLength method would be appropriate.

-------------------------

George1 | 2020-02-29 00:56:22 UTC | #7

I think Lezak have answered most of the questions.
There is also a FindPath in the NavMesh.  The first argument provide the list of points to destination from current position.  I think just call that using one of the agent node in the crowd should give you what you need. You then just convert that to distance. Or just use simple radius or ray cast distance.

Lezak also mentioned about split crowd for multi targets.  Re-child to different parent node.

-------------------------

