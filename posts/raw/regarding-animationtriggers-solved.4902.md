Leith | 2019-02-10 00:24:59 UTC | #1

I'm looking to set up triggers on the footfalls of a biped model, in order to adapt the IK sample to work in combination with a dynamic character controller - ie, my model is moving with some linear velocity, so the existing IK sample is not suitable in its current form to prevent foot-slipping.

I've noticed the Ninja Walk xml file, which sets up two such animation triggers.
Now, I've analyzed my target animation in Blender and determined which two Keys I want to set as triggers. For my target Walk cycle, there are 123 frames, and I need to set triggers on frames 12 and 72.
The xml syntax for animation triggers appears to take Time and NormalizedTime, but it does not appear to allow me to specify precisely which frames I want - am I correct in assuming that I will need to convert my frame indices into time values, and if so, how do I determine the base framerate for a particular animation? Should I be looking to implement my own xml format and programmatic solution in order to specify keyframe indices?

-------------------------

Sinoid | 2019-02-08 01:14:02 UTC | #2

There's no requirement that all tracks be the same length in keys, so whether keys make any-sense to use will depend on exporter/converter. ie. in tweaked facebook fbx -> mdl converter I always emit all keys regardless of track, I have no idea what the blender-exporter / assimp-importer do.

If your keys are good though, you can just add it to the XML load:

```
XMLElement rootElem = file->GetRoot();
for (XMLElement triggerElem = rootElem.GetChild("trigger"); triggerElem; triggerElem = triggerElem.GetNext("trigger"))
{
    if (triggerElem.HasAttribute("normalizedtime"))
        AddTrigger(triggerElem.GetFloat("normalizedtime"), true, triggerElem.GetVariant());
    else if (triggerElem.HasAttribute("time"))
        AddTrigger(triggerElem.GetFloat("time"), false, triggerElem.GetVariant());
    else if (triggerElem.HasAttribute("key") && tracks_.Size() > 0)
    {
        unsigned keyIndex = triggerElem.GetUInt("key");
        if (auto key = GetTrack(0)->GetKeyFrame(keyIndex))
            AddTrigger(key->time_, false, triggerElem.GetVariant());
        else
        {
            const String reportName = GetName();
            URHO3D_LOGERRORF("Unable to find a key for trigger: %u in %s", keyIndex, reportName.CString());
        }
    }
}
```

-------------------------

Leith | 2019-02-08 02:24:09 UTC | #3

Since I do know the framerate of my target animation (30FPS) I computed the two key times as key index / 30 , which yields the two times in seconds (0.4 and 2.4 in my case).

In the same folder as the target "zombie walk.ani" file, I created the following "zombie walk.xml" file.
(braces converted for purpose of posting here)
[quote]
{animation}
    {trigger time="0.4" type="String" value="Right" /}
    {trigger time="2.4" type="String" value="Left" /}
{/animation}
[/quote]

I subscribed to the trigger event as follows:
[quote]
void Character::Start()
{
    // Component has been inserted into its scene node. Subscribe to events now
    SubscribeToEvent( GetNode(), E_NODECOLLISION, URHO3D_HANDLER(Character, HandleNodeCollision));
    SubscribeToEvent( GetNode(), E_SOUNDFINISHED, URHO3D_HANDLER(Character, HandleSoundFinished));
    // Subscribe to receive Animation Trigger events.
    // "Adjustment" node is where my AnimatedModel is attached... it provides Scale to the animated model
    SubscribeToEvent( GetNode()->GetChild("Adjustment",true), E_ANIMATIONTRIGGER, URHO3D_HANDLER(Character, HandleAnimationTrigger));

    // Factory does not initialize these members !!
    AttackAnimationIndex=0;
    okToPlaySound_=true;
}
[/quote]

I added a couple of lines to confirm that the number of trigger keys in the target animation is indeed 2, so I know that my xml is being loaded correctly - yet I am failing to receive the event at runtime. What did I miss?

[EDIT] I also tried using "key" to specify my exact keys , this resulted in NO triggers loaded - looking closer, I see your code for Animation::BeginLoad is slightly different, I have no support for "key" in my engine sourcecode, which was recently built from the latest sourcecode via git - did someone roll that back?

-------------------------

Leith | 2019-02-08 04:32:01 UTC | #4


Here's a short version of my setup for non player characters:
[quote]
Node="Zombie"
==RigidBody
==CollisionShape
==Character
==SoundSource3D
==Node="Adjustment" Scale=".01"
====AnimatedModel
====AnimationController
====Node="RootNode"
======... Rest of Skeleton nodes
[/quote]

There are only two nodes of any real importance, my code resides in Character component, I have tried both the root "Zombie" node (parent of Character), and also the child "Adjustment" node (parent of animated model and controller) - neither resulted in me receiving the event.

[EDIT] 
According to the sourcecode, I should be using the node that is parent to the Model, which is "Adjustment" in my case - regardless, I tried both Nodes, and neither worked.
This is very frustrating, because I can receive the E_ANIMATIONFINISHED event, which is generated by the same engine code as E_ANIMATIONTRIGGER , in the very same method.
I've checked that my animation has triggers, and checked their time values agree with my xml, everything appears to be correct.

[EDIT]
I discovered that I can receive the event if I subscribe from within the frame update method!
This means that somehow my subscription is being "lost" during my application initialization.
The only thing I do that is strange? I create my scene programatically (Character is instantiated, Character::Start is called), dump it to xml, and then reload it. This destroys the existing Scene, but when the scene is re-loaded, and the Character object reconstructed, and Character::Start again called, the event subscription is being ignored. Yet a short while later, Character::Update is able to subscribe with success! Something is very strange, and it's very likely related to my teardown and recreation of the scene at runtime. Still, the call to subscribe is definitely being made after loading, and being silently ignored for no apparent reason. I can certainly write a workaround that lets me subscribe to the event on demand during update, but the code would "smell bad". Wonder what I'm doing, or not doing, that is causing this issue?

[EDIT] Well, now I have discovered that SOME event subscriptions in the Character::Start method work fine - so far its only the Trigger event that is failing to register correctly. Further, if I move that problem event subscription to DelayedStart, it works perfectly. I consider this a workable solution, but still don't truly understand the issue.

-------------------------

Sinoid | 2019-02-08 23:38:00 UTC | #5

At the time `Start` is called you probably have no children to query for since serialization won't have created them yet. If you attempt subscribe to an event on a null sender it'll do nothing, not fall back on a global-handler.

That'd be why delayed start works, when that's called your subtree exists.

> I also tried using “key” to specify my exact keys , this resulted in NO triggers loaded - looking closer, I see your code for Animation::BeginLoad is slightly different, I have no support for “key” in my engine sourcecode, which was recently built from the latest sourcecode via git - did someone roll that back?

It's an edit I made to add it, I guess "*you can just add it to the XML load*" wasn't quite that clear that it was referring to the load-code.

-------------------------

Leith | 2019-02-09 03:17:53 UTC | #6

Thank you, that clears everything up!

-------------------------

GodMan | 2019-02-11 18:19:49 UTC | #7

I've run into the same problem. I tried using Footsteps as a reference, and looked at the C++ version of NSW. I tried using it in the character demo as well.

What did you do to fix the issue?

-------------------------

Leith | 2019-02-12 02:35:03 UTC | #8

In order to receive animation triggers after a scene reload, I needed to wait until the scene was fully reconstructed before registering to receive animation trigger events. The reason is that my AnimatedModel is not connected to the same (root) node as my Character component, there is a child node that applies scale *below* the character/physics/controller - an adjustment node is the true parent of my animated model, and I need it to exist before I can register my event handler. I used "DelayedStart", which is called only when all the components and nodes have been constructed.
The reason I needed a scaling node is because I started out playing with ragdolls, and noticed that physics objects are subject to node scaling - I did not wish scale to be applied to my physics objects, but I still wanted to scale my model down 100 times (wouldn't it be cool if the AssetExporter could apply a fixed scale to vertices and animation translations during export?)

In order to prevent foot-slipping on animated models using dynamic physics, I implemented a cheap form of "foot-planting", which I briefly described here: https://discourse.urho3d.io/t/wip-screenshot-everyone-loves-zombies/4892/10?u=leith

If you have more specific questions, or would like to see sourcecode, I'd be happy to talk about my solution (which still needs work, as it is causing the character to walk through solid objects, but I'll keep tinkering until I get it perfect... I'm effectively ignoring the state of the physics hull while walking, which is not exactly ideal...)

-------------------------

GodMan | 2019-02-12 03:55:14 UTC | #9



    #include <Urho3D/Core/Context.h>
    #include <Urho3D/Graphics/AnimationController.h>
    #include <Urho3D/IO/MemoryBuffer.h>
    #include <Urho3D/Physics/PhysicsEvents.h>
    #include <Urho3D/Physics/PhysicsWorld.h>
    #include <Urho3D/Physics/RigidBody.h>
    #include <Urho3D/Scene/Scene.h>
    #include <Urho3D/Scene/SceneEvents.h>
    #include <Urho3D/Input/Input.h>
    #include <Urho3D/Graphics/DrawableEvents.h>
    #include <Urho3D/Graphics/AnimatedModel.h>
    #include <Urho3D/Audio/SoundSource3D.h>
    #include <Urho3D/Audio/Sound.h>
    #include <Urho3D/Audio/AudioEvents.h>
    #include <Urho3D/Resource/ResourceCache.h>
    #include <Urho3D/Graphics/ParticleEffect.h>
    #include <Urho3D/Graphics/ParticleEmitter.h>

    #include "Character.h"
    #include "GameObject.h"



    Character::Character(Context* context) :
        LogicComponent(context),
        onGround_(false),
        okToJump_(true),
        inAirTimer_(0.0f)
    {
        // Only the physics update event is needed: un-subscribe from the rest for optimization
        SetUpdateEventMask(USE_FIXEDUPDATE);
    }

    void Character::RegisterObject(Context* context)
    {

        context->RegisterFactory<Character>();

        // These macros register the class attributes to the Context for automatic load / save handling.
        // We specify the Default attribute mode which means it will be used both for saving into file, and network replication
        URHO3D_ATTRIBUTE("Controls Yaw", float, controls_.yaw_, 0.0f, AM_DEFAULT);
        URHO3D_ATTRIBUTE("Controls Pitch", float, controls_.pitch_, 0.0f, AM_DEFAULT);
        URHO3D_ATTRIBUTE("On Ground", bool, onGround_, false, AM_DEFAULT);
        URHO3D_ATTRIBUTE("OK To Jump", bool, okToJump_, true, AM_DEFAULT);
        URHO3D_ATTRIBUTE("In Air Timer", float, inAirTimer_, 0.0f, AM_DEFAULT);
    }

    void Character::Start()
    {
        // Component has been inserted into its scene node. Subscribe to events now
        SubscribeToEvent(GetNode(), E_NODECOLLISION, URHO3D_HANDLER(Character, HandleNodeCollision));
    	SubscribeToEvent(GetNode()->GetChild("Jack",true), E_ANIMATIONTRIGGER, URHO3D_HANDLER(Character, HandleAnimationTrigger));
    }

    void Character::FixedUpdate(float timeStep)
    {
        /// \todo Could cache the components for faster access instead of finding them each frame
        RigidBody* body = GetComponent<RigidBody>();
        AnimationController* animCtrl = node_->GetComponent<AnimationController>(true);
    	Input* input = GetSubsystem<Input>();

        // Update the in air timer. Reset if grounded
        if (!onGround_)
            inAirTimer_ += timeStep;
        else
            inAirTimer_ = 0.0f;
        // When character has been in air less than 1/10 second, it's still interpreted as being on ground
        bool softGrounded = inAirTimer_ < INAIR_THRESHOLD_TIME;

        // Update movement & animation
        const Quaternion& rot = node_->GetRotation();
        Vector3 moveDir = Vector3::ZERO;
        const Vector3& velocity = body->GetLinearVelocity();
        // Velocity on the XZ plane
        Vector3 planeVelocity(velocity.x_ * 0.5f, 0.0f, velocity.z_ * 0.5f);

        if (controls_.IsDown(CTRL_FORWARD))
            moveDir += Vector3::FORWARD;
        if (controls_.IsDown(CTRL_BACK))
            moveDir += Vector3::BACK;
        if (controls_.IsDown(CTRL_LEFT))
            moveDir += Vector3::LEFT;
        if (controls_.IsDown(CTRL_RIGHT))
            moveDir += Vector3::RIGHT;


        // Normalize move vector so that diagonal strafing is not faster
        if (moveDir.LengthSquared() > 0.0f)
            moveDir.Normalize();

        // If in air, allow control, but slower than when on ground
        body->ApplyImpulse(rot * moveDir * (softGrounded ? MOVE_FORCE : INAIR_MOVE_FORCE));

        if (softGrounded)
        {
            // When on ground, apply a braking force to limit maximum ground velocity
            Vector3 brakeForce = -planeVelocity * BRAKE_FORCE;
            body->ApplyImpulse(brakeForce);

            // Jump. Must release jump control between jumps
            if (controls_.IsDown(CTRL_JUMP))
            {
                if (okToJump_)
                {
                    body->ApplyImpulse(Vector3::UP * JUMP_FORCE);
                    okToJump_ = false;
    				animCtrl->PlayExclusive("Models/stand_sword_airborne.ani", 0, false, 0.2f);
                }
            }
            else
                okToJump_ = true;
        }

    	// On air
    	if (!onGround_) {

    		// Falling a lot
    		if (inAirTimer_ > 2.75f)	{
    			animCtrl->PlayExclusive("Models/Falling.ani", 0, true, 0.2f);

    			// Falling a bit		
    		}
    		else {
    			animCtrl->PlayExclusive("Models/stand_support_high_airborne.ani", 0, true, 0.2f);
    		}

    		// On ground
    	}
    	else {

    		// On ground with movement
    		if (softGrounded && !moveDir.Equals(Vector3::ZERO)) {

    			// Moving forward
    			if (softGrounded && moveDir.Equals(Vector3::FORWARD)) {
    				animCtrl->PlayExclusive("Models/bogeyman_movefront.ani", 0, true, 0.2f);
    				animCtrl->SetSpeed("Models/bogeyman_movefront.ani", planeVelocity.Length() * 0.3f);
    			}

    			// Moving back
    			if (softGrounded && moveDir.Equals(Vector3::BACK)) {
    				animCtrl->PlayExclusive("Models/walk_back.ani", 0, true, 0.2f);
    				animCtrl->SetSpeed("Models/walk_back.ani", planeVelocity.Length() * 0.3f);
    			}

    			// Moving left
    			if (softGrounded && moveDir.Equals(Vector3::LEFT)) {
    				animCtrl->PlayExclusive("Models/walk_left.ani", 0, true, 0.2f);
    				animCtrl->SetSpeed("Models/walk_left.ani", planeVelocity.Length() * 0.3f);
    			}

    			// Moving right
    			if (softGrounded && moveDir.Equals(Vector3::RIGHT))	{
    				animCtrl->PlayExclusive("Models/walk_right.ani", 0, true, 0.2f);
    				animCtrl->SetSpeed("Models/walk_right.ani", planeVelocity.Length() * 0.3f);
    			}

    			// On ground idle
    		}
    		else {
    			animCtrl->PlayExclusive("Models/bogeyman_idle.ani", 0, true, 0.2f);
    		}

    	}

    	if (controls_.IsDown(CTRL_MELEE)) {
    		animCtrl->PlayExclusive("Models/hammer_slam.ani", 0, false, 1.0f); // Try tweaking the last value.
    		animCtrl->SetSpeed("Models/hammer_slam.ani", 1.0f); // Try tweaking the last value.
    	}
    	if (controls_.IsDown(CTRL_CROUCH) && softGrounded) {
    		animCtrl->PlayExclusive("Models/crouch_sword_idle.ani", 0, false, 0.25f); // Try tweaking the last value.
    		animCtrl->SetSpeed("Models/crouch_sword_idle.ani", 0.5f); // Try tweaking the last value.
    	}

        // Reset grounded flag for next frame
        onGround_ = false;

    }

    void Character::HandleNodeCollision(StringHash eventType, VariantMap& eventData)
    {
        // Check collision contacts and see if character is standing on ground (look for a contact that has near vertical normal)
        using namespace NodeCollision;

        MemoryBuffer contacts(eventData[P_CONTACTS].GetBuffer());

        while (!contacts.IsEof())
        {
            Vector3 contactPosition = contacts.ReadVector3();
            Vector3 contactNormal = contacts.ReadVector3();
            /*float contactDistance = */contacts.ReadFloat();
            /*float contactImpulse = */contacts.ReadFloat();

            // If contact is below node center and pointing up, assume it's a ground contact
            if (contactPosition.y_ < (node_->GetPosition().y_ + 1.0f))
            {
                float level = contactNormal.y_;
                if (level > 0.75)
                    onGround_ = true;
            }
        }
    }

    void Character::HandleAnimationTrigger(StringHash eventType, VariantMap& eventData)
    {
    	DelayedStart();
    	using namespace AnimationTrigger;
    	AnimatedModel* model = node_->GetComponent<AnimatedModel>();
    	if (model)
    	{
    		exit(0);
    		AnimationState* state = model->GetAnimationState(eventData[P_NAME].GetString());

    		if (state == NULL)
    			return;


    			Node* bone = node_->GetChild(eventData[P_DATA].GetString(), true);

    			if (bone != NULL)
    			GameObject::SpawnParticleEffect(bone, node_->GetWorldPosition(), "Particle/Smoke.xml", 1, LOCAL);
    			GameObject::SpawnSound(bone, node_->GetWorldPosition(), "Sounds/BigExplosion.wav", 3);

    	}

    }


Here is my Character.cpp. I have tried quite a few things. The XML file is fine. I can't get the animation trigger to work. I believe is may be what @Sinoid said. I'm not sure how to fix it though.

-------------------------

Leith | 2019-02-12 03:58:32 UTC | #10

I will reply you my character class in one day, please stand by, it is a little different but mostly the same
Your main problem is likely the same as I had - when you register for an event, sometimes you need to hand in the parent node associated with the thing that is generating that event - for example, animation events need you to hand in the node that was parent to the animatedmodel

-------------------------

Sinoid | 2019-02-12 04:46:58 UTC | #11

Don't do this:
```
void Character::Start()
{
    // Component has been inserted into its scene node. Subscribe to events now
    SubscribeToEvent(GetNode(), E_NODECOLLISION, URHO3D_HANDLER(Character, HandleNodeCollision));
	SubscribeToEvent(GetNode()->GetChild("Jack",true), E_ANIMATIONTRIGGER, URHO3D_HANDLER(Character, HandleAnimationTrigger));
}
```
the problem is the `GetChild`. When `Start` is called your subtree to find the child does not exist.

Override `DelayedStart` not `Start`.

---

Here's two phrases to burn it into your memory:

- **Start** is self
- **DelayedStart** is global

---

The E_NODECOLLISION event is valid where it is though if you want to keep it there.

-------------------------

Leith | 2019-02-12 09:54:50 UTC | #12

yeah - the problem is trying to subscribe, with child nodes that dont exist yet - well that was the issue I experienced - no warning is generated, its a silent error.

-------------------------

I3DB | 2019-02-12 18:26:24 UTC | #13

[quote="Leith, post:12, topic:4902"]
the problem is trying to subscribe, with child nodes that dont exist yet
[/quote]

Can't you just do that event subscription inside 'OnAttachedToNode' rather than in 'Start'? Doesn't that solve the problem?

-------------------------

GodMan | 2019-02-12 21:05:50 UTC | #14

@I3DB I don't see that in the docs??

I solved my problem. Thanks for the help guys.

-------------------------

Leith | 2019-02-13 05:29:06 UTC | #15

Unfortunately, no that does not solve the problem... the OnNodeSet method is called as soon as a component (or node) is attached to another node, it's no guarantee that "lower" nodes or components have been created yet. The scene loader creates and attaches objects in top-down hierarchical order - objects are attached pretty much as soon as they are instantiated, so it's way too early to do anything that requires access to objects that are lower down in the scenegraph. 

On the bright side, the component that was causing me grief happens to derive from LogicComponent, which gives me access to "DelayedStart", a method guaranteed not to fire until the scene has been fully loaded and all the nodes and components attached.

-------------------------

