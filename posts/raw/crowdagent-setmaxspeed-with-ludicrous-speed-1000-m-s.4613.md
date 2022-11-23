mvendra | 2018-10-22 21:02:02 UTC | #1

As per title - what would be the best way to assign an enormous amount of speed to a CrowdAgent?

I'm working on an application that's mostly based off of the CrowdNavigation demo (39) - all parameters are mostly the same. Agents are part of a crowd (CrowdManager).

My problem is - the higher the max speed, **the more the agent wobbles around the final target**, going back and forth until it stops. This can be mitigated by also raising the agent's max accel. (SetMaxAccel) - but it only goes so far.

I've found that max speed 30 and max accel ~800 will result in instant stoppage at the final target. But I need something like 1500 for the max speed, and there's no high enough accel. that makes it work well.

A sufficiently high max speed (regardless of the max accel) and the agent wobbles indefinitely around the target, and it does so with insane enthusiasm.

I'm also willing to accept hack-ish workarounds as well. Thanks!

-------------------------

slapin | 2018-10-22 21:17:28 UTC | #2

Well, the reason it wobbles is because crowd navigation works in discrete steps and overshooting fixup will lead to problems.

General solution to this would be additional checks which will correct max speed according to distance to target so that movement per step will not overshoot. Also you might check other settings of DetourCrowd that would lead to the same result and you also can increase number of steps per frame.
Also you can ask questions like this to recast google group.

-------------------------

mvendra | 2018-10-22 21:46:24 UTC | #3

Any way I could "teleport" the agents and/or force-stop them? Using Node::SetPosition manually seems to be messing up my CrowdAgents.

-------------------------

slapin | 2018-10-22 22:07:04 UTC | #4

You can and I do this a lot but I do not move at so high speeds. You can try removing agent from crowd and add again. It is done automatically if errors are detected, but ymmv, I'd try that anyway. Elaborate on what you call "messed up".

-------------------------

slapin | 2018-10-22 22:12:13 UTC | #5

Understand that DetourCrowd works using current state and converting that to new state according to rules, so you can modify agent state the way you like to your advantage. Understand that if you change position much you need to update othet state vars otherwise you will have problems. Just read code and understand internal mechanics, it is simple enough.

-------------------------

mvendra | 2018-10-22 22:14:28 UTC | #6


"messed up" = I was meddling with the agent's corresponding Urho3D::Node's position, while the CrowdManager was also taking ownership of it - no surprise I ran into conflicts. I'll just manually remove and teleport them whenever I need extreme speeds.

@slapin thank you!

-------------------------

slapin | 2018-10-23 02:53:32 UTC | #7

In general you can move and correct your nodes (i.e. physics-based motion) but it looks like for very high speeds something influences velocities. If you frequently need high speeds I suggest you investigate that as there is cost to add/remove agent from/to crowd.

-------------------------

mvendra | 2018-10-23 17:29:51 UTC | #8

I had another idea: I could also use a much smaller scale. What I needed was 1500x more speed than my normal speed (base speed around 1.5 m/s, and I wanted a factor of 1500x faster. This was for implementing a "fast forward simulation" feature, so agents and internal time would both advance much faster - something like the Sim City games).

So I could instead use a base speed of 0.01 m/s, and use 15 m/s for ultra speed (1500x faster) - and scale down my world models to match it visually.

@slapin would you anticipate any problems with this approach? Thanks.

-------------------------

slapin | 2018-10-24 02:08:14 UTC | #9

The problem I think is loss of local collision avoidance. You need to keep step values sane.
I'd play with deltas.and steps per frame to make sure your motion deltas are not too large. Otherwise it it will pass through.walls and other unpassable objects and agent collisions will not be detected.

-------------------------

Sinoid | 2018-10-26 06:33:44 UTC | #10

Is the scene time-scale not working with crowds?

Although DetourCrowd uses a variant of RVO so it should at least sort of work out of the box, the agent-corridors might be too small out of the box though - I couldn't imagine anything beyond 32x not being full of issues.

-------------------------

mvendra | 2018-10-26 12:26:39 UTC | #11

Thanks for the suggestion. Pretty much everything I tried resulted in all sorts of problems (at 1500 m/s for agents). I circumvented the problem by pre-calculating the final position and then teleporting at the right time.

-------------------------

slapin | 2018-10-27 17:16:23 UTC | #12

I'd suggest using the following algorithm: 1. Set speed as high as possible not having any problems. 2. Increase speed 3. Change agent parameters until no problem occur. Go to 2. X. Understand dependency and have formula to configure. If you don't need rvo at high speeds then you could do tricks but I'm pretty sure you can make DetourCrowd work fine at 1500. Sorry I never ran DetourCrowd at high speed and agent parameters there are poorly documented if at all, but you can see code.and experiment to understand influence.

-------------------------

mvendra | 2018-10-28 17:57:14 UTC | #13

I tried that algorithm, more or less. Basically, the parameters that make it work are a combination of agent's speed and agent's acceleration. There is an erratic ratio between the two that results in a sweet spot where they work well, but above a certain amount, the agents just "go insane", at around 90 m/s and above (and a matching 5x factor for the max accel)

Thanks, the teleport solution will do fine for now.

-------------------------

NinjaPangolin | 2019-03-24 20:56:53 UTC | #14

Had the same problem: altering `MaxSpeed` and `MaxAccel` caused model to come back and forth at the end of the path. For future reference, here's a hack I've found that stops model immediately after reaching final position. When I handle `E_CROWD_AGENT_REPOSITION` event I disable agent if it has arrived:
```
void CrowdAgentEventHandler::HandleCrowdAgentReposition(Urho3D::StringHash eventType, Urho3D::VariantMap& eventData) {
    using namespace Urho3D::CrowdAgentReposition;

    auto* agent = static_cast<Urho3D::CrowdAgent*>(eventData[P_CROWD_AGENT].GetPtr());

    // ...

    agent->SetEnabled(true);
    if(agent->HasArrived()) {
        agent->SetEnabled(false);
    }
}
```
Not sure why exactly, but it seems to do the trick :smiley:

Strangely, if I comment out `agent->SetEnabled(true);` only the first click have this effect, further are bouncy again.

-------------------------

Leith | 2019-03-25 12:25:35 UTC | #15

A wild guess? You didn't call agent->SetEnabled(true) anywhere else, so an agent which reaches its destination becomes disabled, and stays that way.

A similar approach can be found in the Character Sample, where the Update(?) method sets the onGround_ boolean to false at the end of the method, ready for the next frame, where it sets the value for that bool near the start of the method. Outside of the Update(?) method, that flag is always false, which can lead to confusion, should we query that flag from a bunch of other event handlers.
Personally I find this approach distasteful, and lacking in respect for the concept of state logic. Frame updates are not trivial, but they are linear - we should respect the last known state value, not trash it before we leave.

-------------------------

mvendra | 2019-03-28 22:16:59 UTC | #16

Thanks I'll give it a try!

-------------------------

