tianlv777 | 2022-03-21 09:44:22 UTC | #1

Crowdmanager navigation makes an inexplicable turn after reaching the position

-------------------------

tianlv777 | 2022-03-21 09:44:40 UTC | #2

![6JJN~T~{VZR763A`%YWMFFW|690x484](upload://fdazDpE87XHxZsTqXKsGoNoKA0A.jpeg)

-------------------------

tianlv777 | 2022-03-21 09:45:00 UTC | #3

![J_P~%WWNUM%1I`1GVQ2_B|690x432](upload://l94b2ZYhxAfAtjcOLaXPVbw0r1E.jpeg)

-------------------------

Nerrik | 2022-03-22 15:34:59 UTC | #4

"Arrived" with crowdmanager can be a little unreliable and works other than expected. 
For example depending on the speed the agent can overshoot the target and then make a turn back. So i check the agent distance to the target for my self and reset the target shortly before the agent arrives manually.

-------------------------

Nerrik | 2022-03-22 16:14:38 UTC | #5

at the HandleCrowdAgentReposition event function
```
float arrived = 4.5f;
if ((Vector3(agent->GetPosition().x_, agent->GetPosition().y_, agent->GetPosition().z_) - Vector3(agent->GetTargetPosition().x_, agent->GetTargetPosition().y_, agent->GetTargetPosition().z_)).Length() < arrived)
{
   scenen->GetComponent<CrowdManager>()->ResetCrowdTarget(agentnode);
}
```

In my project i replaced the agent->GetPosition().y_ and agent->GetTargetPosition().y_ with 0.0f to check only the xz distance for more force at gradients, but i dont have overlapping navmeshes.

-------------------------

JSandusky | 2022-03-23 05:50:17 UTC | #6

IIRC as an agent arrives things can get a bit bonkers. Is the vector it ends up facing perhaps a "*natural*" vector like +X or so on? So many things can go wrong there at the end.

While a number of people have contributed to making the detour stuff happen (@scorvi @JTippetts @cadaver and myself [I think @Eugene and @weitjong as well plus some others here and there]) it's best to consider the the navigation and crowd handling to be a baseline you can start with rather than an out of the box solution so things that one could call a hack (like @Nerrik's solution, which should really be a modification inside of detour as a threshold) are to be expected necessities to some degree. 

Expect to code, navigation ultimately gets project specific on a long enough timeline and some features like off-mesh connections are only handled to the bare minimum by what's there (there are no assumptions we could make ... is the offmesh connection a teleporter? a ladder? a wall climb? leap over a gap?). So that sort of work is ultimately on the end-user.

-------------------------

tianlv777 | 2022-03-23 06:14:39 UTC | #7

Em I'm very skeptical about the performance of crowdagent. In fact, I want to make a tower defense game, like war3 TD（Tower defense） map. But if there are 1000 units running in the map, will it get stuck in the sky?

-------------------------

tianlv777 | 2022-03-23 06:18:33 UTC | #8

Yes, if I insist to create a  tower defense game, I think I should write the navigation logic myself, so that thousands of units can run to the destination on the map.not use crowdmanager.

-------------------------

JSandusky | 2022-03-23 06:32:14 UTC | #9

Safely, the CrowdManager as it is written caps out at about 200 units (it can do more depending on hardware, but this is the safe range). DetourCrowd can handle thousands, but how it's wrapped in Urho raises tons of events for every CrowdAgent so if you want to break that 200 agent safe limit you need to switch to a DOD approach and raise events for agents in bulk rather than per agent. 

Crowds quickly saturate event signaling overhead as well as script overhead if using Angelscript/Lua responding to those events.

DOD'ing crowds should get you over the 1000 mark safely though but it's not a bad decision to do something else if you know your constraints.

-------------------------

