ghidra | 2017-01-02 01:13:00 UTC | #1

I have been chasing down a crash that I can't seem to cure. 
This is what the terminal tells me:

[code]
WARNING: Physics: Overflow in AABB, object removed from simulation
[/code]

doing a gdb bactrace, i get this:

[code]
#0  0x00007ffff71399cd in Urho3D::InitialQuickSort<Urho3D::InstanceData, bool (*)(Urho3D::InstanceData const&, Urho3D::InstanceData const&)> () from Urho_DYN/lib/libUrho3D.so.0
#1  0x00007ffff713e6f0 in Urho3D::BatchQueue::SortFrontToBack() () from Urho_DYN/lib/libUrho3D.so.0
#2  0x00007ffff70efe1b in Urho3D::WorkQueue::ProcessItems(unsigned int) () from Urho_DYN/lib/libUrho3D.so.0
#3  0x00007ffff70e7a2a in Urho3D::ThreadFunctionStatic(void*) () from Urho_DYN/lib/libUrho3D.so.0
#4  0x0000003fbfe079d1 in start_thread () from /lib64/libpthread.so.0
#5  0x000000354d6e88fd in clone () from /lib64/libc.so.6
[/code]

Which doesnt tell me a lot.. or at least doesnt tell me where in my code it might be happeneing.
What I am doing. I have a "level" of the game spawning a lot of physics objects, and removing them. Bullets, enemies, shell casings, pick ups, etc. They get removed after a certain amount of time (casing, bullets), or if they get far enough away from the player (bullets,enemies), and other bits of logic.
I am using FixedUpdate for the most part. But i recently added FixedPostUpdate, since the docs seem to say it happens after the physics update. So, I flag any node removals during the FixedUpdate, then if they are flagged, I remove the node_ in FixedPostUpdate.
Is that a good idea? is there a better idea?

My initial "fix" seems to have made the crashing occur a lot less frequently, but it still occurs sometimes.

Any push in the right direction would be very much appreciated.

-------------------------

Lumak | 2017-01-02 01:13:00 UTC | #2

The physics warning comes from void	btCollisionWorld::updateSingleAabb(btCollisionObject* colObj), in btCollisionWorld.cpp
[code]
	if ( colObj->isStaticObject() || ((maxAabb-minAabb).length2() < btScalar(1e12)))
	{
		bp->setAabb(colObj->getBroadphaseHandle(),minAabb,maxAabb, m_dispatcher1);
	} else
	{
		//something went wrong, investigate
		//this assert is unwanted in 3D modelers (danger of loosing work)
		colObj->setActivationState(DISABLE_SIMULATION);

		static bool reportMe = true;
		if (reportMe && m_debugDrawer)
		{
			reportMe = false;
			m_debugDrawer->reportErrorWarning("Overflow in AABB, object removed from simulation");
			m_debugDrawer->reportErrorWarning("If you can reproduce this, please email bugs@continuousphysics.com\n");
			m_debugDrawer->reportErrorWarning("Please include above information, your Platform, version of OS.\n");
			m_debugDrawer->reportErrorWarning("Thanks.\n");
		}
	}

[/code]

It's possible that you might have erroneous collision mesh that results in size > 1e12.

-------------------------

ghidra | 2017-01-02 01:13:01 UTC | #3

[quote]It's possible that you might have erroneous collision mesh that results in size > 1e12[/quote]

Assuming that occurs when I am removing node..

What would be best practice when removing a node_ that has rigidbody and collision shape on it safely.
Like i mentioned, I am flagging the node to be removed during the FixedPostUpdate step, with a simple node_->Remove();

I guess I could also check for outrageous collisionshape sizes to prevent this crash.

Assuming its not related to node removal, how else can I be sure that my physics data is acceptable?

-------------------------

Lumak | 2017-01-02 01:13:01 UTC | #4

Ah, I see.  If the error is occurring during the removal of the physics object then bullet is seeing corrupt data.  The events: USE_FIXEDUPDATE and  USE_FIXEDPOSTUPDATE are directly associated with bullet's E_PHYSICSPRESTEP and E_PHYSICSPOSTSTEP, respectively, and that's when bullet is processing all physics objects -- probably a bad idea to remove them during those stages.

It might be safer to pend the removal until E_ENDFRAME or even E_BEGINFRAME.

-------------------------

cadaver | 2017-01-02 01:13:01 UTC | #5

Update and PostUpdate should be safe. NinjaSnowWar removes colliding or timer-expiring objects during FixedUpdate and hasn't crashed, so that too should usually be safe. However I'm not sure what exact case is occurring here, if perhaps Bullet is in an unsafe state removing-wise. In theory each substep should be self-contained, and removal of rigidbodies inbetween them should remove them also from Bullet's internal structures (collision islands and so..)

-------------------------

ghidra | 2017-01-02 01:13:01 UTC | #6

Thank you for your replies. I've tried a few things, and managed to decrease the crashes... but still get them. 
So I am likely doing something entirely incorrect. Obviously.
I followed the model of ninja warrior and removed them in the FixedUpdate. I'll probably return to that method, while I track down what it is I am doing so wrong.
I'll call this semi-solved.

-------------------------

ghidra | 2017-01-02 01:13:11 UTC | #7

I might have traced the source of a lot my my physics related crashes to my custom geometry creation.
I am making procedural trianlge meshes with trianglemesh physics shape.
If I turn that "feature" off (the generation of the physics triangle mesh), that crashing goes away.
It is being created during the E_POSTUPDATE event handler.

Perhaps there is a better time to create custom physics geomtry?

-------------------------

cadaver | 2017-01-02 01:13:12 UTC | #8

The time position in a frame when geometry is created should not have an adverse effect. Hard to tell what's going on without minimally functional example code, that both creates the custom geometry and causes the issue.

-------------------------

Dave82 | 2017-01-02 01:13:13 UTC | #9

[quote]WARNING: Physics: Overflow in AABB, object removed from simulation[/quote]

I had the same issue , but it was triggered by adding more than one rigid body and shape component to a Node.(It was a bug i fixed it in the meantime now it works fine).So maybe you miss removing the RigidBody or Shape component somwhere and you try to add another one ? (Just an idea)

-------------------------

ghidra | 2017-01-02 01:13:14 UTC | #10

[quote]Hard to tell what's going on without minimally functional example code, that both creates the custom geometry and causes the issue[/quote]

Of course. I appreciate that its largely impossible to troubleshoot and help with this issue with no concrete example. My code base and trying to find the problem makes it a little difficult to show some example code at the moment. I should probably strip it down and generate something like that.. might help me find the problem a lot easier too.

I guess I was currently just looking for shots in the dark as to what can cause it.

like:

[quote]I had the same issue , but it was triggered by adding more than one rigid body and shape component to a Nod[/quote]

I'll have to examine this. Its possible. Thanks for the suggestion.
Still digging.

-------------------------

