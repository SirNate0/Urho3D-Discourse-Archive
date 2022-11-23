Alex-Doc | 2017-07-22 09:15:48 UTC | #1

Hello,
let's suppose we have a 3D model, which has an animated part(bone) and we want it to push the other RigidBodies.

As (by design?) this will not work as I expect it:
[code]
< Main Node >
    < rigidbody />
    < collisionShape />
    < AnimatedModel />
    < Child Bone Node >
        < other collisionShape />
    < /Child Bone Node >
< /Main Node >
[/code]

Adding a second [b]non-trigger[/b] RigidBody to the child node it's _probably not a good idea_,
how would you normally overcome this?

So far, the only solution I have in mind, is to add a RigidBody to the Child Bone Node as a [b]Trigger[/b] and manually check/apply the collisions.

Any ideas?

-------------------------

Lumak | 2017-07-22 12:42:56 UTC | #2

Isn't having char capsule sufficient enough to know that you've collided with a "push-able" object and transition to push-anim state?

-------------------------

Alex-Doc | 2017-07-22 12:59:29 UTC | #3

Not in this case, I better explain: 
Imagine the model as an AT-ST from Star Wars (the biped robot thing), we want the player to be able to pass between the legs but also the legs to collide while it "walks".

The model in question (biped) is not the player.
The player just has a capsule as usual.

-------------------------

Lumak | 2017-07-22 13:13:07 UTC | #4

I see. I know you discussed using static collision objects on another thread, that didn't work?  If not, apply kinematic to it.

-------------------------

Alex-Doc | 2017-07-22 13:34:40 UTC | #5

That was referred to collisions between triggers, no forces involved.(I've used that for melee weapons)
 
I know I could just set the children bodies as Triggers and use the contacts to apply the forces, but I'd like to know if there's some other way.

Basically I'm looking for a way to tell physicsWorld to ignore collisions between two bodies, I know I could do this with masks, but I want it to be limited to the node's children.

Setting the children Rigidbody to kinematic makes the simulation go crazy, as the "main" body is set to use physics.

-------------------------

Lumak | 2017-07-22 13:53:12 UTC | #6

Try this:
[code]
ColLayer_Static     = (1<<0),
ColLayer_ATST       = (1<<6), // just as example
ColLayer_ATST_Parts = (1<<7),

ColMask_ATST         = ~(ColLayer_ATST_Parts),
ColMask_ATST_Parts   = ~(ColLayer_Static | ColLayer_ATST | ColLayer_ATST_Parts),

[/code]

also ATST parts:
kinematic,  apply gravity = false, linear factor = 0, angular factor = 0, and mass > 0

edit: added collayer_static and atstparts to not collide with it

-------------------------

Alex-Doc | 2017-07-22 14:08:36 UTC | #7

Thanks, I've already thought about setting the collision masks but I'd have preferred if the "ATST part" VS other node "ATST part" case, would have collided.

I have also wondered about adding the ignore list functionality to PhysicsWorld but I don't see it so good performance-wise: 
Something like having each body to preserve a Vector of Rigidbody pointers and check if it should collide or not.

-------------------------

Lumak | 2017-07-22 14:49:10 UTC | #8

I'm trying to understand why you'd desire to have atstpart vs atstpart collision. So say you have upperleg, leg, and foot - you're wanting the leg and foot to collide as it walks? I know you are aware that collision resolver will try to separate them.

edit:  i thought you were referring to the ignore list as the rigidbody settings, sry.

-------------------------

Alex-Doc | 2017-07-22 17:07:23 UTC | #9

I mean to have two separate instances of ATST collide:
ATST0 foot, able to collide with ATST1 body.

That would exclude the Mask and Layer settings as I want them to only ignore the [b]children[/b] Rigidbody recursively.

This introduces the ignore list feature, pretty much consists of:

RigidBody has a 
[code]Vector<RigidBody*> ignoreList_;[/code]
Which can be used as:
[code ]
RigidBody* body = node_->GetComponent<RigidBody>();
RigidBody* other = GetOtherBodyExample();
body->AddToIgnoreList(other);
other->AddToIgnoreList (body);
[/code]

And finally, where PhysicsWorld processes the collisions, it does a check of Rigidbody's ignoreList content and decides whether to apply forces and report the collisions or not.

-------------------------

Lumak | 2017-07-23 02:48:36 UTC | #10

You know, I didn't know what ATST looked like and had to look it up when you first mentioned it, but for one ATST to have its foot on another's body either the 1st is doing some high kicks or the 2nd is dead?  If the 2nd is dead and in a ragdoll state then it's easier problem to solve.

And I agree, your ignore list check would eat performance.

-------------------------

Alex-Doc | 2017-07-23 06:19:00 UTC | #11

[quote="Lumak, post:10, topic:3375"]
ATST to have its foot on another’s body either the 1st is doing some high kicks or the 2nd is dead?  If the 2nd is dead and in a ragdoll state
[/quote]

The AT-ST reference is more about having an exaggerated example of body+legs collisions, the actual in-game models are more generic and various.

At this point I think the best way would be to work-around it where possible and use triggers or masks on the "foot" where unavoidable.

The last doubt I have is about the animated and kinematic RigidBody with the Mask/Layer configuration: 
Would it push non-kinematic RigidBody in a strange way? 
I will test it later today and report here.

-------------------------

Alex-Doc | 2017-07-23 10:36:26 UTC | #12

I might have found the solution:
I could make the RigidBody to have the ignore list in its members and then,
I can probably add a custom NearCallback in PhysicsWorld.

see [here](https://github.com/urho3d/Urho3D/blob/master/Source/Urho3D/Physics/PhysicsWorld.cpp) and [here](http://bulletphysics.org/mediawiki-1.5.8/index.php/Collision_Filtering)

Surely it can impact performances, but I don't think it would be that worse than a Trigger calling collision events to apply forces on each physics tick.

-------------------------

Lumak | 2017-07-23 13:53:06 UTC | #13

Best solution is to use Constraints and not have connected bodies collide with each other, see 13_Ragdoll/CreateRagdoll.cpp, line 164.

-------------------------

