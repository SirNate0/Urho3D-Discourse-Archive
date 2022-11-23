sabotage3d | 2017-01-02 01:08:15 UTC | #1

Hi guys I am struggling with a few physics problems in my game and I hope that someone might be able to help me.
My character controller is based on lerping position between the current position and the target position similar to the crowds implementation. My questions are.
Should I keep everything [b]SetKinematic(true)[/b] ? I am getting different results if I set the the player to [b]SetKinematic(false)[/b] but keep the level to [b]SetKinematic(true)[/b] vs [b]SetMass(0.0f)[/b]
As I have animated platforms and cars should I update the node positions in the fixedUpdate  this is the update for the platforms [b]direction += Vector3(speed * timeStep, 0.0f, 0.0f)[/b]
Should I update the players node position in fixedUpdate? 
Should I set the rigidBody position vs the node position (is there any difference)? 
I have subscribed all my prefabs to [b]E_NODECOLLISION[/b] to keep track of collisions is that good for performance?
While my player is on the ground I keep getting collision events from the ground even when he is in rest is there a way to get a single collision event until he collides with something else (stop the collision events from reseting) ?
Should I use the [b]P_TRIGGER[/b] instead of[b] P_OTHERBODY[/b] and[b] P_OTHERNODE[/b]?
How should I tackle moving platforms should I just add the local position of the platform to the player or I should let the physics handle it?

-------------------------

heytao | 2021-09-22 11:01:42 UTC | #2

Have the same questions. :thinking:

-------------------------

PsychoCircuitry | 2021-09-22 22:58:51 UTC | #3

Hi, lots of questions in the ops topic lol. But for generalized game mechanics there's often no one size fits all solution. It's more about what works as intended for the results you are expecting and how you want to implement it.

Some advice on these questions tho, kinematic vs zero mass ie static body. If you want your controllable characters to be defined solely by your own movement logic, ie in the physics world but not physics controlled, I believe either will work, but kinematic body, a physics object that sends forces to other objects but doesn't receive any, generally seems favored in most implementations. The downside here is that you then have to handle any desired receiving physics logic on your own, gravity, movement restrictions, etc. Not that a full rigid body object is any easier, just different problems to overcome, with its own advantages. EDIT: also looking thru the source code I see that any type of static object collision to static object collision is removed from the collision events. So keep that in mind. Collision detection will need to be done with at least one of the bodies being dynamic, kinematic or otherwise.

Any type of node teleportation movement, ie you are manually moving the node position vs apply a force to move, probably needs some type of raycast, or other query to prevent teleporting into penetrating other objects. I don't think you will have the physics smoothing in this case, where the substeps are interpolated, so handling this in update or fixed update will be a tradeoff of per rendered frame smoothness vs physics instability. I'm not sure if raycasts or other queries are performed based off the last fixed update position or the interpolated position of the current substep. Also in this case, I think teleporting the node or just the body itself makes no difference, so using the node is probably easier for management.

For single frame collision events: in addition to the nodecollision event, there are also nodecollisionstart and nodecollisionend which are handled per object. If you need to do something just at the start or end of a particular collision you can use these events instead of trying to manage logic for the entire duration of the collision. I don't think that subscribing every node or prefab to a collision callback function is necessarily a limiting factor. The engine is already generating these events whether you use them or not in your logic. Lots of physics calculations will slow down anyway regardless of your own methods, but if you do use heavy logic in these callbacks, perhaps optimizing repetitive tasks into a data oriented design scheme would help. But urho is pretty much designed to be using these event callbacks specifically this way.

Characters on platforms, it really depends on how the platforms are designed and how it is intended to be interacted with, parenting to the platform, or soft parenting, just apply the position and/or rotation, is probably going to work more consistently than trying to let the physics engine handle it alone,, thru friction or gravity overrides or whatever else, not that it can't be done in this fashion, it just usually has some kind of slipping or other type artifacts that require additional finesse solutions.

I'm no expert, just urho3d hobbyist, but giving my ideas on the questions in the original post.

Hope any of this is helpful
-PsychoCircuitry

Edit: one other thing that I thought I might mention regarding the collision questions in the original post. I'm not sure what is meant by using P_TRIGGER instead of P_OTHERBODY P_OTHERNODE. Maybe I'm not understanding the premise, but P_TRIGGER in the event data is just a boolean that reflects if one of the colliding bodies is set to a trigger (responds to collisions but has no other physics influence). I'm not sure how this would negate the use of the other pointers, if you need the other pointers in your collision logic. But basically, urho3d does no prefiltering of collision types for you, it merely supplies all presumably needed data for you to do anything you wish. If you need different responses for different scenarios, it'd be up to you to implement the branching however you'd like. Your collision handler will run for every collision. If you have multiple collisions per frame it will run multiple times per frame. You can branch this out to other inline methods or defined methods as necessary. If you do branch it out to another defined method, I think it is wise to parse any additional variables out of the event data you will need and send those as their own variables into the function method. I've tried just passing the event data variant map into subsequent functions, and it does not work reliably.

-------------------------

