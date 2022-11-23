slapin | 2019-05-23 13:20:00 UTC | #1

Hi, all!
While I tried to be as tactful and tasteful as I possibly could I think this post might
be considered offensive by some people, so I really sincerely apologize to them
and ask to remain constructive. I don't intend to offend anybody and I really like
helpful and friendly community.
As I will probably would write another long post which would break people's brains,
I thought I could ask my question in more picture/comic form, so people who won't read could really
get interest and actually try to understand what I want to ask.

![ai_architecture|597x500](upload://hfgHxJ6zbFAczVfgFbFgkVKRKaJ.png)

What I want is simple - make group behaviors. Not only this one but as many as needed in systemic form.
The current AI architecture I use is based on individual agents. Similar to NinjaSnowWar,
but technologically improved (behavior tree, some complex mechanics, different specialized character controllers for vehicle, on-foot, etc.). But lets start from NinjaSnowWar or similar concept - how would you change the AI architecture of NinjaSnowWar to allow group behaviors?
![ai_architecture2|250x500](upload://fvxEUJYhjXpg3oO62Dicd4ls8FW.png)

Many games implement such systems, but I never seen any tutorials, any explanations
on AI architectures implementing this, I seen only very brief commentaries on GDC videos and some game AI papers. I really would like to see the code, architecture guides, blueprints, references, suggestions et al. about implementation of such architecture, to boost individual agent AI to group awareness AI.

Additional thanks would be to a person who would teach me on this (I would pay for proper knowledge; most AI books contain too much words and too little information, the area looks heavily commercial, with very hard way to get to truth so proper pointers on practical references and tutorials would be very welcome, even if these are paid stuff).

Here I really hope that I just look in wrong direction and the answer is on surface, but really it looks like it is not a topic which is easily accessible.

-------------------------

SirNate0 | 2017-07-26 16:47:17 UTC | #2

What I would do (having never done it, and not doing it at present) is have a group AI manager class that would have 'slots' to be filled, and assign these roles. If the GroupManager has control of the agent, it does nothing by itself (i.e. it doesn't send the control signals) and just waits for the GroupManager to release it. I'm not certain what conditions I would use for entering the Group Behavior -- naturally there is a base requirement of the number of agents available (in your example, 4 + 1 enemy). Given that scenario, I would probably have the enemy AI trigger it -- have the red one store a list of aggressors/targets (when the NPCs attack, they are added to it, and then removed after a timeout and/or if they are defeated), and then if you have the required 4 aggressors randomly instantiate the GroupManager (say a 1/10 chance or something, or much lower if you are going to check every frame). The GroupManager is passed the list of aggressors, and assigns them to their roles, and it sends the commands that would otherwise be done by the individual agent (I am assuming you already have controls set up for the individual agents such as hold, attack, and play victim). The GroupManager will then execute until some condition is met -- say while (Red is not defeated && all Blues are alive && timer <= 20 seconds) and then release the individual agents, notifying them of their role/last action (if they don't record it) -- this way they can (but don't have to) do something different based on whether they were the victims or the attackers in the group managed scenario).

If you already have in place methods of querying nearby AIs, then you don't even need to have the Red agent trigger it -- you can have some zone-based system (what I would do -- give bounding regions for the possible scenarios, and have the manager check if conditions are right within the region -- say in an alley for your given scenario) or a global one and it can create the GroupManager if the conditions are right (say a 4v1 fight in the given area). This also makes it easier should you want, e.g. a 2v2 group scenario, as it means you don't have to figure out how the 2 red AIs coordinate to know that they both exist, and both (or individually) have the 2 blue enemies.

-------------------------

slapin | 2017-07-26 17:41:04 UTC | #3

Thanks for your answer, you added some things to think about.

How would you implement zones - trigger rigid bodies? I actually never seen these implemented using
physics, but nobody shared the details...

Also these zones probably should be dynamic and spawned around camera... sort of simulation bubble -
any ideas on how to implement it?

-------------------------

SirNate0 | 2017-07-26 18:24:01 UTC | #4

Last question first, since the code is fairly long: depending on the scale of your game (you are going for a *very* large scale, right?) you may want to just not bother with dynamic spawning. If you are reasonably sure that it would be an issue, it depends on how you set up your map. I set up my maps with a bunch of 'chunks' that are each a node with all of the stuff in that chunk parented to it (the static stuff -- player is just parented to scene). In that case, since my chunks are disabled and enabled, I would just have the chunk handle spawning the triggers, or, if you have a fairly static scene layout, you could just have them loaded already and enable/disable the trigger node (this is what I do, but I think you are going for a larger scale than I am and that could require different solutions). If your map is not divided this way, you may be able to use the Octree to accomplish the zoning, provided you aren't going for a particularly map-aware zoning (i.e. if the zones don't have to correspond to, say, a room or an alley). If you do want the map-aware zoning, but having the collision stuff spawned and just disabled is a problem, you can instead just mark your map with some empty nodes that have either the Trigger component loaded and let it spawn the collision stuff as needed later, storing the parameters needed in the node's user variables (or the trigger's attributes). If this to is too burdensome, you will probably have to create a subsystem for it that stores all of the triggers in some structure efficient for querying based off of proximity to a location (i.e. the camera's), and then you instantiate the first 50 or so of them every second or so, and perhaps give them all a timer so they remove themselves after 15 seconds or whatever if they are not re-instantiated (to be clear, I have very little idea of what you would need for this, so I would test the other solutions first, as I have no real idea if this is a good answer).

And here's how I set up triggers for battles in my game. You would probably also need to subscribe to E_NODECOLLISIONEND, and then remove the agents that leave the region and possibly also those that end up assigned to a group action (if the group action takes it out of the region that is fine, as the GroupManager would still store them)
```cpp
#pragma once

#include <Urho3D.h>
#include <Scene/Component.h>
#include <Core/Object.h>
#include <Core/Context.h>
#include "../CollisionMasks.hpp"
#include "../Character.hpp"
#include <Physics/PhysicsEvents.h>

using namespace Urho3D;

#include "BattleEvents.hpp"
#include "BattleQueue.hpp"
#include <IO/Log.h>

class BattleTrigger: public Component
{
	OBJECT(BattleTrigger, Component);

	SharedPtr<BattleQueue> battle_;

	BattleTrigger(Context* context): Component(context), battle_(
			new BattleQueue(context, nullptr, 2/*number of participants*/))
	{

	}

	static void RegisterBattleTrigger(Context* context)
	{
		context->RegisterFactory<BattleTrigger>();
	}

	/// Handle scene node being assigned at creation.
	virtual void OnNodeSet(Node* node)
	{
		if (node == 0)
			return;
		//todo: change to GetComponents?
		RigidBody* body = node->GetComponent<RigidBody>();
		if (body)
		{
			body->SetCollisionLayerAndMask(COLLISION_BATTLE, COLLISION_PERSON);
			body->SetTrigger(true);
			SubscribeToEvent(node, E_NODECOLLISIONSTART, 
					HANDLER(BattleTrigger, HandleCollision));
		}
	}
	void HandleCollision(StringHash eventType, VariantMap& eventData)
	{
		if (!enabled_)
			return;
		using namespace NodeCollisionStart;
		Node*other = (Node*)eventData[P_OTHERNODE].GetPtr();
		if (other == nullptr)
			return;
		using namespace BattleTriggered;
		eventData[BattleTriggered::P_BATTLE_QUEUE] = battle_;
		eventData[P_TARGET] = other;
//The pretrigger is so that the character can 'capture' the trigger and display a dialogue.
// Skipping to the E_BATTLE_TRIGGERED is more like what you want.
// Or just storing the agents that enter and removing them when they leave,
// using this class as the 'manager' that decides when a GroupManager should be instantiated
		node_->SendEvent(E_BATTLE_PRE_TRIGGERED, eventData);
		if (eventData[BattlePreTriggered::P_CAPTURE].GetBool())
			LOGDEBUG("Battle Trigger Captured.");
		else
			node_->SendEvent(E_BATTLE_TRIGGERED, eventData);
//In my game, the Player object receives this event and then has the queue start the battle
	}
};
```

-------------------------

slapin | 2019-05-23 13:20:00 UTC | #5

Thank you so much for the code!

I see you use custom events, right?

I wonder about this part:
```c++
node_->SendEvent(E_BATTLE_PRE_TRIGGERED, eventData);
if (eventData[BattlePreTriggered::P_CAPTURE].GetBool())
	LOGDEBUG("Battle Trigger Captured.");
else
	node_->SendEvent(E_BATTLE_TRIGGERED, eventData);
```

Your comment above is qute clear, but I wonder how do you fill the eventData part - is it happens directly in handler? is such reuse of eventData safe?

Anyway, I currently think of strategy to use having behavior trees handling group behaviors.

![ai_behavior_tree_problem|250x500](upload://99k5AYGtnuRQdYczECWq01hykj1.png)

I'd like to inject group behavior somehow so they do not increase complexity of BTs
and still do not be a heavy hack.
I need to think of this now, as I currently re-implement the AI architecture to get rid of many shortcomings, as I was going from one shortcoming to next blindly, because I never did such thing and there is too little hints around here... Actually I think I need to write a tutorial of sorts after I finally get enlightened
so to have some records left :)

-------------------------

slapin | 2017-07-27 08:59:50 UTC | #6

So if i have large number of zones with large number of group behaviors, together with zone-based behaviors, I need something systemic to handle behavior injection, and i still could not find ejjective way to do that...

-------------------------

SirNate0 | 2017-07-27 15:42:13 UTC | #7

I am pretty sure that what I did was safe. P_CAPTURE, if it is not actually filled in the handler, should just be constructed as a new Variant, which returns false since the type is not VAR_BOOL. Let's say, at least, that what I did has not been a problem for me. I think it should be completely safe (since I've defined the two events to use the same parameters, so a new variant map doesn't need to be filled, and as eventData is passed by reference to the handlers it has worked). I suppose engine changes could break it, but that isn't something I need to be too worried about, as I can always just not move to the next release.

Let us know how it goes! A tutorial sounds great :slight_smile:

What I might think about doing is having the behavior trees all just query 'the engine' about behaviors attached to their location every so often, and then cache those to be considered for a while. I've no real experience in behavior trees, though, so perhaps someone else can help you, otherwise good luck!

Also, if you've not seen it, I think this presentation *might* have gone in to how they implemented location-based behaviors (though I watched it quite a while ago, so no promises): [Building a Better Centaur AI at Massive Scale](https://www.youtube.com/watch?v=OiFdlYY-GFA)

-------------------------

slapin | 2017-07-27 20:21:12 UTC | #8

Thanks for your answers!

I watched this one too, and remember they do a bit of teaser but do not go into much detail
of implementation.
About BTs - I implemented them in very rough way using article on https://www.youtube.com/watch?v=n4aREFb3SsU

http://aigamedev.com/insider/tutorial/second-generation-bt/

using AngelScript first, but almost finished rewrite to C++. I also wrote graphical editor for them. I wonder if it is feasible to add them to engine though,
as Urho rarely have high-level engine constructs... probably should ask such question to @cadaver

-------------------------

slapin | 2017-07-28 05:44:48 UTC | #9

I found a great approach to implement various systems with Urho. It just occured to me that I could communicate events through components of the same node, which makes scripted behavior tree nodes not necessary which allows to remove huge chunk of ugly code. So I can replace all BT action nodes with events and implement everything in much simpler way. This also can be used to inject zone-based behaviors easily.
Also this can decouple tree from character controller, which is also great!
Looks I have some refactoring work now, and the result will be much better than before!

-------------------------

