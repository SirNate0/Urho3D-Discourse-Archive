GodMan | 2020-01-19 17:46:15 UTC | #1

I made a new thread for this instead of posting in another one with a different topic.

The issue I am having is when my ai reach there destination and huddle around their destination. The frame-rate starts to bomb depending on how many agents there are. 

About the ai used. They are the same model and all use the same animation. Not a whole bunch of different models and animations to rule out this as a bottle neck.

Here is my code to spawn the ai. It is straight from the crowd navigation sample.

    void CharacterDemo::SpawnZombie(const Vector3& pos, Node* jackGroup)
    {

    	ResourceCache* cache = GetSubsystem<ResourceCache>();
    	SharedPtr<Node>jackNode(jackGroup->CreateChild("Jack"));
    	jackNode->SetScale(Vector3(0.025f, 0.025f, 0.025f));
    	jackNode->SetRotation(Quaternion(-90, Vector3(0, 1, 0)));
    	jackNode->SetPosition(pos);

    	AnimatedModel* modelObject2 = jackNode->CreateComponent<AnimatedModel>();
    	modelObject2->SetModel(cache->GetResource<Model>("Models/masterchief.mdl"));
    	modelObject2->ApplyMaterialList("Materials/zombie.txt");
    	modelObject2->SetCastShadows(false);
    	modelObject2->SetOccludee(true);
    	modelObject2->SetUpdateInvisible(false);

    	
    	handBoneNodeAI = jackNode->GetChild("right_hand_marker", true);

    	AnimatedModel* sword = handBoneNodeAI->CreateComponent<AnimatedModel>();
    	sword->SetModel(cache->GetResource<Model>("Models/plasma_sword.mdl"));
    	sword->ApplyMaterialList("Materials/plasma_sword.txt");

    	jackNode->CreateComponent<AnimationController>();

     // Commented this out. This may be an issue as well. Not sure how else to apply an animation.

        //	AnimationController* swordIdle = jackNode->CreateComponent<AnimationController>();
        //	swordIdle->PlayExclusive("Models/combat_sword_idle.ani", 0, false, 0.5);


        	Material* sentinel = cache->GetResource<Material>("Materials/zombie_armor.xml"); // Was tutorial ground material


        	sentinel->SetTexture(TU_MULTI, multi);
        	sentinel->SetTexture(TU_DETAIL, metalDirty);
        	sentinel->SetTexture(TU_SHIELD, plasmaShield);

        	//Color(0.122f, 0.537f, 0.122f, 1.0f)
        	sentinel->SetShaderParameter("MatDiffColor", Color(0.25f, 0.25f, 0.25f, 1.0f));


        	// Create a CrowdAgent component and set its height and realistic max speed/acceleration. Use default radius
        	CrowdAgent* agent = jackNode->CreateComponent<CrowdAgent>();
        	agent->SetHeight(1.0f);
        	agent->SetMaxSpeed(7.0f);
        	agent->SetMaxAccel(7.0f);
        }

I have not tried weitjong idea yet.

-------------------------

GodMan | 2020-01-20 01:27:33 UTC | #2

I also tried @weitjong idea. Hopefully this is what he meant.


    const unsigned NUM_ZOMBIES = 2;
    	for (unsigned i = 0; i < NUM_ZOMBIES; ++i)
    	{
    		Node* zombie = scene_->CreateChild("Zombie");
    		zombie->SetScale(Vector3(0.025f, 0.025f, 0.025f));
    		zombie->SetRotation(Quaternion(-90, Vector3(0, 1, 0)));
    		zombie->SetPosition(Vector3(205.84f, 1.0f, -293.97f));

    		AnimatedModel* modelObject2 = zombie->CreateComponent<AnimatedModel>();
    		modelObject2->SetModel(cache->GetResource<Model>("Models/masterchief.mdl"));
    		modelObject2->ApplyMaterialList("Materials/zombie.txt");
    		modelObject2->SetCastShadows(false);
    		modelObject2->SetOccludee(true);
    		modelObject2->SetUpdateInvisible(false);


    		handBoneNodeAI = zombie->GetChild("right_hand_marker", true);

    		AnimatedModel* sword = handBoneNodeAI->CreateComponent<AnimatedModel>();
    		sword->SetModel(cache->GetResource<Model>("Models/plasma_sword.mdl"));
    		sword->ApplyMaterialList("Materials/plasma_sword.txt");

    		zombie->CreateComponent<AnimationController>();

    		AnimationController* swordIdle = zombie->CreateComponent<AnimationController>();
    		swordIdle->PlayExclusive("Models/combat_sword_idle.ani", 0, false, 0.5);


    		Material* zombie_armor = cache->GetResource<Material>("Materials/zombie_armor.xml"); // Was tutorial ground material


    		zombie_armor->SetTexture(TU_MULTI, multi);
    		zombie_armor->SetTexture(TU_DETAIL, metalDirty);
    		zombie_armor->SetTexture(TU_SHIELD, plasmaShield);

    		//Color(0.122f, 0.537f, 0.122f, 1.0f)
    		zombie_armor->SetShaderParameter("MatDiffColor", Color(0.25f, 0.5f, 0.25f, 1.0f));


    		// Create a CrowdAgent component and set its height and realistic max speed/acceleration. Use default radius
    		CrowdAgent* agent = zombie->CreateComponent<CrowdAgent>();
    		agent->SetHeight(1.0f);
    		agent->SetMaxSpeed(7.0f);
    		agent->SetMaxAccel(7.0f);

    	} 


I did see some improvement, but not a huge difference. The above code tries to split the agents instead of making them all one big group. Assuming I did it correctly.

Here is a screenshot. Only 10 AI's if they huddle at their destination the update stats climbs as high as 15 and 16. Frame-rate drops to the 40s.

![Screenshot_Sun_Jan_19_19_05_04_2020|690x291](upload://8OgIoAV1l2PAkgY3KFlLJUmw7OZ.jpeg)

UPDATE: I just tested the urho3d crowd sample and spawn 10 of the default character. It has the same problem. Once the agents reach their destination and huddle there. The frame-rate plummets. I was getting 40 fps. This is all in debug mode though. I'm not sure if it goes away in release mode.

-------------------------

JTippetts | 2020-01-20 14:05:41 UTC | #3

Pathfinding in general is an 'expensive' operation, so you should probably be using states to manage when it happens it a little better. If an agent doesn't need to be actively seeking a path, it shouldn't be seeking a path. When an agent is at or near its destination, disable it's agent component so it doesn't keep recalculating and moving or attempting to move. Last year, I did an ARPG for a game jam and was able to handle a couple hundred enemy mobs in a crowd, through mob state handling, disabling mobs that were too far away to need to act, disabling agent components of mobs that were near their approach target, etc...

-------------------------

GodMan | 2020-01-20 18:09:21 UTC | #4

@JTippetts Great answer. I looked through the docs to see how to disable the agents once they get to their destination. I did not see anything on this. I had looked at this option in the past.

-------------------------

weitjong | 2020-01-20 21:48:42 UTC | #5

For the crowd navigation demo you can press the 'space' key to toggle the debug geometry. If you do that you will know what I meant by agent not able to "settle down" as it cannot possibly reach its designated target position because it is overcrowded. Pay attention to the color of the debug geometry of the agent. Start with one agent and move it around and slowly increase the number to two, then three, and four. When you click to choose a target area, notice each agent got one spot assigned from the target area. But if the target area is too small then there bound to be overlapped and that's when agent get stuck and not able to settle down.

-------------------------

JTippetts | 2020-01-20 21:50:41 UTC | #6

Well, you can use the SetEnabled method at the Component level to enable/disable the crowd agent, however that has the effect of actually removing the agent from the crowd, which is fine for faraway agents, but probably not what you want to do for agents that are nearby. In the case of nearby agents, you can use CrowdAgent::ResetTarget() to reset the agent's target, meaning it shouldn't look for a path again until you call CrowdAgent::SetTargetPosition with a new position to path to. So if an agent is "close enough" to where it should be, call ResetTarget and it shouldn't try to path until it needs to move again.

-------------------------

GodMan | 2020-01-20 23:09:56 UTC | #7

@weitjong I will take a look again. I did view it in debug mode. That may be one of the issues. I did notice they try to occupy one quad that is in the ground. I tried adjust some of the agent params, but nothing really changed. 

@JTippetts I added this to the HandleCrowdAgentReposition event:
```
if (arrived)
{
    agent->ResetTarget(); 
    return;
} 
```
This works, but I noticed the ai will start to randomly walk out to the edges of the navmesh. Looks kinda neat actually LOL. I I call agent->Remove(); It works great. Only downside is I can't tell them to move to another location later because I removed the agent.

-------------------------

JTippetts | 2020-01-20 22:45:56 UTC | #8

If you use agent->SetEnabled(false) instead of Remove, then when you re-enable the agent component with SetEnabled(true) it gets re-added to the crowd. Otherwise, you remove the component entirely with Remove, and have to add/create another agent component to get it going again.

AI randomly walking after you reset target sounds buggy. You might try calling agent->SetTargetVelocity with Vector3(0,0,0) to see if maybe it has some residual velocity that it shouldn't have. To be extra safe, call SetTargetPosition() with the object's current position, to ensure it doesn't have a target position elsewhere, before you call ResetTarget(). This shouldn't be necessary, but you just never know right?

-------------------------

GodMan | 2020-01-21 02:50:34 UTC | #9

Okay so I tried some of the ideas posted. The setEnabled() does not seem to improve anything. I tried the rest target with velocity of zero. They do stay in place now. However not real performance increase. If I remove the agent my Update stats stay at their default ranges and no frame-rate bombs. 

If I choose to remove the agent what is the best way to add it back for them to move again?

-------------------------

Sinoid | 2020-01-21 06:46:58 UTC | #10

What hardware are you running on for this case?

> The setEnabled() does not seem to improve anything. 

It won't, not for anything but the most extreme differences.

> If I choose to remove the agent what is the best way to add it back for them to move again?

The agent position is on-nav-mesh, you can use that so long as it's a real on mesh position. The multispace stuff is mostly bullshit.

-------------------------

SirNate0 | 2020-01-21 14:26:35 UTC | #11

[quote="Sinoid, post:10, topic:5825"]
> The setEnabled() does not seem to improve anything.

It won’t, not for anything but the most extreme differences.
[/quote]
Having never used the navigation stuff before, why would SetEnabled(false) result in different performance than removing the component? It seems to me they should be effectively the same except for memory usage.

-------------------------

JTippetts | 2020-01-21 15:22:47 UTC | #12

SetEnabled removes the agent from the crowd, the same as removing the component altogether. So in that respect, they're essentially identical.

Performance benefits from either are probably going to be fairly marginal. An agent with no target that is not walking amounts to a `continue;` inside the various loops in dtCrowd::update, so removing the agent altogether really only amounts to removing the small bit of overhead each agent adds to iterating the collection of agents, plus the overhead of steering calculations for moving agents that need to steer around them. However, for nearby agents, you want the agent to remain in the crowd, because that steering behavior is the whole point.

-------------------------

GodMan | 2020-01-21 20:26:56 UTC | #13

@Sinoid I'm not sure what you mean?

I did see some benefits with the setenabled option. It was not as much as removing the agent.

I don't mind removing the agent. I just don't know the most efficient way to re-enable it again.

-------------------------

GodMan | 2020-01-21 21:46:49 UTC | #14

[quote="JTippetts, post:12, topic:5825"]
SetEnabled removes the agent from the crowd, the same as removing the component altogether. So in that respect, they’re essentially identical.
[/quote]


I don't think that is true. I compared disabling it versus removing it, and removing the agent shows a noticeable difference. The Update stats in debug view return to normal range before the agents were used. However if I disable the agent once they reach their destination the stats seem to higher. Then if I later send the agents to a new destination once they arrive and the agent is disabled again the stats will start to climb up even more. Closer to the original problem.

-------------------------

JTippetts | 2020-01-21 23:08:04 UTC | #15

You might be right about that, I'm operating a lot on what *should* be the case, but since working on that ARPG project I haven't really dug into it. CrowdAgent::OnSetEnabled() indicates that it adds/removes the agent from the crowd, so theoretically it should be about the same as removing the agent altogether, but I should know better than to operate on theoretically since I don't actually know all the details that well.

-------------------------

GodMan | 2020-01-22 00:21:12 UTC | #16

I appreciate the help.

I just don't know how to re-enable the agent after removal. Should I just recreate it again? I just feel like my methods are not very efficient.

-------------------------

JTippetts | 2020-01-22 03:56:32 UTC | #17

Well, if you remove the CrowdAgent component then the only way is to re-create another agent component in its place. Remove() physically removes it from the node.

-------------------------

GodMan | 2020-01-22 04:59:07 UTC | #18

Yes I know. My thoughts are what is the most efficient way to recreate the agent again.

-------------------------

Sinoid | 2020-01-30 07:50:10 UTC | #19

@GodMan some of what you describe could be an agent leak. Do you have any obvious artifical holes in your crowds like there's some sort of empty void they refuse to enter?

Crowds are never expected to perform well past 100 agents, that's the generic engine trade-off for the amount of events Urho raises (which is far too many). If you need to do something like Dynasty-Warriors/KUF then you need to roll it yourself.

-------------------------

GodMan | 2020-01-30 18:03:57 UTC | #20

@Sinoid I am not using a large number of agents. I think maybe 15 at most. 
When you say void. Do you mean does the mesh that is used to generate the navmesh have holes? Meaning holes that were designed into the mesh?

-------------------------

GodMan | 2020-01-31 00:11:24 UTC | #21

@Sinoid I thought about this. Would that assumption be wrong though? It has the same problem in the demo that ships with Urho. If you have lets say 12 - 15 agents. The frame-rate bombs just like the issue I am having. If I remove the agent once they reach their destination everything is fine. 

I believe the demo mesh is just a simple plane.

-------------------------

lezak | 2020-02-01 12:03:08 UTC | #22

I don't think that removing or disabling agents is a good solution - let's take for an example situation where You don't need to move whole crowd, but only some selected agents and since You've removed others, they won't be used in path calculation, so You'll loose collision avoidance with them.
Another thing is that adding/removing components (agents) on every move/stop will trigger lot of 'component added' 'component removed' events which will also affect performance with bigger number of agents. If don't care much about avoidance, You can try setting navigation pushiness of agents to none - this should help with a problem with agents not being able to reach their destination, yet still - only to some point - they will avoid eachother when moving.
Finally, 12-15 agents seems extremely low, so I must ask the obvious - are You having this problem in release build? Because there is a big difference in crowd performance between debug and release.

-------------------------

GodMan | 2020-02-01 17:13:31 UTC | #23

@lezak I stated in an earlier post that I have not tested this issue in release mode. I have been testing the add and remove component and it's been working great. What I do is set this on a delay so Urho does not add or remove the component each loop.

-------------------------

JTippetts1 | 2020-02-02 00:26:32 UTC | #24

You really need to do your performance testing in release mode.

-------------------------

GodMan | 2020-02-01 17:36:35 UTC | #25

I plan on testing it soon.

-------------------------

JTippetts1 | 2020-02-01 17:51:04 UTC | #26

I suggest doing it before you do anything else to try to fix your problem. It's hard to overstate how important it is, because there can be a LOT of perf-stealing bullshit added to a debug build.

-------------------------

GodMan | 2020-02-01 18:38:35 UTC | #27

Okay. I will post here with results.

-------------------------

GodMan | 2020-02-02 00:26:32 UTC | #28

Okay so I compiled in release mode and tested the crowd navigation sample. Everything seems rock solid. The update stats got to only 2.0 and then goes back down. Frame-rate never budged. Guess all my issues were debug info. I spawned 15 of them no issues. Did not even drop one frame. :smile: :smile: :smile:

-------------------------

Sinoid | 2020-02-06 01:37:35 UTC | #29

Yeah, debug build will do that. Debug builds are super slow, this explains why your issues felt so weird.

I strongly recommend that you use `RelWithDebInfo` builds for everything except deployment.

That tends to be good enough for 75% of debugging.

Sometimes you'll get garbage info from the debugger you can then wrap the functions that are problems with `#pragma optimize("", off)` and `#pragma optimize("", on)` to see them in full debug-build detail.

Or just wrap the whole .cpp file staring from inside the namespace.

Here's an example of what I mean from my render-library (see how the function is wrapped in #pragma):
```
#pragma optimize("", off)
void DX11StateCache::SetBlendState(ID3D11BlendState* s)
{
	if (s == blendState_)
		return;

	blendState_ = s;
	float blendFactor[4] = { 1.0f, 1.0f, 1.0f, 1.0f };
	device_->GetD3DContext()->OMSetBlendState(s, blendFactor, 0xFFFFFFFF);
}
#pragma optimize("", on)
```

-------------------------

