Leith | 2019-03-11 03:57:15 UTC | #1

I have attached some bodyparts (kinematic rigidbodies) to the bone nodes of an animated character.
Soon I realized that I can't really use Bullet to test for collisions on these bodies - kinematic bodies can't actually hit each other in Bullet physics... what I really want to do, is to drive dynamic bodies via animation... but I don't want to mess with motors and desired velocities, and the default order of events in urho updates could be a problem.

I examined the order of updates in the Urho engine, and I note the following:
E_UPDATE triggers the updating of each scene (presumably by order of scene id).
Within each Scene update, E_PHYSICSPRESTEP may nor may not fire, because physics runs at a fixed rate that differs to the framerate. E_SCENEPOSTUPDATE triggers the update of animation controllers, and it happens LAST in a scene update.

After all scenes are updated, we get E_POSTUPDATE - would this be the right place to overwrite the transforms of rigidbodies to match with animated bones? This seems rather late, for partial ragdolls, I now have to deal with transforming constraints themselves? I'd like to maintain angular and linear momentum... Erwin suggests zeroing them out, but that's not acceptable for my use-case.

-------------------------

Bananaft | 2019-03-14 07:25:59 UTC | #2

I'm not sure I fully understand what you are making. But you can try storing previous transform for each body, and then use it to calculate and apply linear and angular velocity.

-------------------------

Leith | 2019-03-15 06:09:21 UTC | #3

I'm trying to constrain a dynamic ragdoll to an animated skeleton.
If I just make the bodies be kinematic, everything is perfect - except that kinematic bodies don't get any penetration correction or other restitution forces due to contact with dynamic or even other kinematic bodies.
I want to constrain a set of dynamic rigidbodies, and preferably also their existing joint constraints, to match an animated set of bones.

-------------------------

Modanung | 2019-03-15 09:36:09 UTC | #4

[quote="Leith, post:3, topic:5013"]
I want to constrain a set of dynamic rigidbodies, and preferably also their existing joint constraints, to match an animated set of bones.
[/quote]

That's a tough one. As long as you don't work with (something akin to) motors, interactions will likely remain wonky since - for instance - a leg will not be slowed down by any dynamic objects it kicks around as it should be. As a result it will push the object harder than it should, requiring some form of tweaking that will probably start to look like motors again.

-------------------------

Leith | 2019-03-15 09:37:38 UTC | #5

yeah, I know... my logic is not working with the usual ik forwards concept in mind.

-------------------------

Leith | 2019-03-19 08:21:14 UTC | #6

Attempt #1: neither before, inside, or after physics update, can we hard-set the position and rotation of dynamic objects. None of these three work, I current have them all enabled. I guess I need to talk to the motionstate object directly.

-------------------------

TrevorCash | 2019-03-19 21:03:33 UTC | #7

This was really annoying for me as well. In my newton wrapper If the transform of a node has been changed to anything other than the last transform that newton had updated it to - the rigid body is teleported automatically.  So then calls like node->SetWorldTransform() work like you expect and the rigidbody is teleported.  Its also really nice and makes sense for Kinematic Bodies

-------------------------

Leith | 2019-03-20 05:58:48 UTC | #8

My current thought is that "Bullet wants to move dynamic objects, so let it" - I think I need to wait until after the physics update before I teleport them into their bone-animated states.

I can accept that bone animation is generally taken from the previous frame, since animationcontrollers update very late in the frame, and certainly after physics update.
But so far, I'm not having much luck in manually setting the transforms on dynamic bodies.

Part of my confusion, is that these dynamic rigidbodies are parented to scene nodes, so I assume that Bullet will be writing to those transforms via motionState.. and at the same time, those scene nodes are Bones, and will typically be written to (later in the frame) by the animationcontroller.
This means that the values I can expect to see, by calling node methods such as GetWorldPosition, will vary depending on when in the frame I ask the question. Confusing on my brain.

-------------------------

Leith | 2019-03-22 04:29:41 UTC | #9

I finally have a solution (three days, man) - posted elsewhere, essentialy we wait for the physics post-step event, then transform the parent nodes of rigid bodies, in a top-down order preferably. I am using Node::SetTransform on the parent nodes of rigidbodies.

-------------------------

