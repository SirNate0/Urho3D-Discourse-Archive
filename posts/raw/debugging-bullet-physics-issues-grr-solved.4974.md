Leith | 2019-03-01 04:16:50 UTC | #1

CollisionShape and RigidBody are just containers for bullet objects - but we don't expose those object in c++, and we don't set the userpointer member on the bullet objects?
At least Erwin had the sense to make (most everything) be POD structs, so we always could access...
Urho3D is limiting my runtime access to its underlying third party objects...

-------------------------

SirNate0 | 2019-02-27 18:25:33 UTC | #2

Aren't `RigidBody::GetBody()` `CollisionShape::GetCollisionShape()` how we expose the underlying bullet structures in c++, or have those been changed/removed?

-------------------------

Leith | 2019-02-28 02:06:50 UTC | #3

I didn't see any CollisionShape::GetCollisionShape anywhere (I'll doublecheck) but my point was really about debugging collision callbacks - where we are handed a bullet CollisionObject that we can cast back to a bullet CollisionShape - but from there, we're screwed, we can't cast back from there to an Urho CollisionShape or RigidBody given a bullet object of those types. Bullet objects have a "userpointer" which is often used for this purpose, but I don't think we're setting it - this means there is no way to, for example, obtain the Name of an object involved in a collision, because we can't get hold of any Urho objects from within a collision callback - therefore we can't get to the parent Node to query its name.

[EDIT]
1. Urho's RigidBody class has no GetCollisionShape method - given an urho rb, we have to query the parent node for the CollisionShape component (which we assume is attached to the same node as the body). But having done so, Urho's CollisionShape class DOES have a GetCollisionShape method to expose the underlying bullet object - so accessing bullet objects from urho objects is definitely possible.

2. Both Urho RigidBody and Urho CollisionShape ARE setting UserPointer on the underlying bullet objects. Therefore, it is also possible to cast back from a bullet object to an Urho object! 

Sometimes it's nice to be wrong :)

[EDIT AGAIN]
It is noteworthy that although Urho's CollisionShape class provides a GetCollisionShape method, the same cannot be said of Urho's RigidBody class - there's no way to access the underlying bullet rb from an urho rb.

-------------------------

guk_alex | 2019-03-01 02:26:59 UTC | #4

> there’s no way to access the underlying bullet rb from an urho rb
 
Urho3D::RigidBody : 

`/// Return Bullet rigid body.`
`btRigidBody* GetBody() const { return body_.Get(); }`

Is that what you asked for?

-------------------------

Leith | 2019-02-28 08:23:08 UTC | #5

Yep! That is what I was looking for :slight_smile:
As I've said, Urho is fairly mature - but lacking in documentation.
Actually, it's not going to help solve my current issues, but nice to know it exists !!
Thank you :)

-------------------------

Leith | 2019-03-01 02:28:38 UTC | #6

After a LOT of debugging, I was able to determine the exact source of my problem.
There is a bug in XML deserialization of Urho3D RigidBody - or rather, a problem with the notion that RigidBodies are instantiated, and attached to the scene, PRIOR to attribute deserialization, so the attributes are never applied to the bullet objects...

When I construct my scene in code, I call RigidBody SetLayerAndMask on every rigidbody that I create. I then save the scene, and note that these values are correctly serialized to xml.
Then I load that same xml file back into my app.
At this point, my rigidbodies are constructed and attached to the new scene with default layer and mask values (-1). But the attributes are never deserialized, or if they are, they are deserialized incorrectly : the default values are being used, and certainly, no attempt is made to call SetLayer, SetMask, or SetLayerAndMask during deserialization. 
If deserialization is correctly reading the values back in, well, the rigidbody was attached with default values, and we probably need to "re-add" rigidbodies just after we deserialize the layer and mask attributes, in order to have our deserialized values applied to the bullet objects.
I'd say this issue is squarely in Urho's court :slight_smile:

-------------------------

Leith | 2019-03-01 04:18:34 UTC | #7

Part of the problem was RigidBody::reAddBody_ flag has a default value of false. When loading scene from XML, the value will also be false by default... this causes a failure in RigidBody::ApplyAttribute().
So I made the following minor change to force attributes to be applied:
[code]
    //if (readdBody_)
        AddBodyToWorld();
[/code]
Now I was able to see for certain that all my rigidbodies had the correct layer and mask values after deserialization. But a problem remained when I performed my raycast!
In my character class, the following line of code is causing me problems:
[code]
        phyWorld->RaycastSingle(result, ray, CollisionFilter::Static);
[/code]
The value of the mask for the raytest (CollisionFilter::Static) is 2. But when I debugged this call to PhysicsWorld::RaycastSingle? 
[code]
void PhysicsWorld::RaycastSingle(PhysicsRaycastResult& result, const Ray& ray, float maxDistance, unsigned collisionMask)
{
    URHO3D_PROFILE(PhysicsRaycastSingle);

    if (maxDistance >= M_INFINITY)
        URHO3D_LOGWARNING("Infinite maxDistance in physics raycast is not supported");

    if(collisionMask==(unsigned)-1){
        URHO3D_LOGWARNING("ERROR! RaycastSingle called with Mask=Everything!!!");
        // Generate an interrupt
        std::raise(SIGABRT);
        }
[/code]
This trap is triggered - what the hell? I passed in a constant integer value of 2, yet somehow that argument's value has become -1!!! 
My callstack in this call is showing different values to what I expressly passed in!
It is noteworthy that I perform some other raycasts in a different method of the same class, passing in the very same mask value, and they don't trigger this trap.

Could this be a compiler bug? Or even a bug in GDB debugger?
Here's what I get when I debug the call:
[quote]
Calling RaycastSingle with mask=2
[Fri Mar  1 15:07:14 2019] WARNING: ERROR! RaycastSingle called with Mask=4294967295
[/quote]

-------------------------

Leith | 2019-03-01 04:16:20 UTC | #8

Finally figured it out!

Some of my raycast calls were missing a maxDistance argument!
This meant that maxDistance was set to my input mask value, and the mask value used in the call was the default M_MAX_UNSIGNED value.
I've just managed to crash codeblocks ide again, but I am feeling certain that I've solved this mystery :)

-------------------------

Modanung | 2019-03-01 08:20:50 UTC | #9

Are you counting how often you're wrongfully claiming there's a bug in not-your-code?

https://discourse.urho3d.io/t/possible-bug-in-handling-of-e-physicscollisionend/4940/11

Sometimes things are simply not working as _expected_.

-------------------------

Leith | 2019-03-01 09:30:49 UTC | #10

I don't mind being wrong - but I did find an honest bug in this one. The issue is RigidBody::ApplyAttributes after reload - a flag is not being observed because its default value is false, and I didn't change it in my code. The issue is that attributes dont get applied after a reload.

-------------------------

Leith | 2019-03-01 09:52:58 UTC | #11

Good documentation goes a long way also.
And also, pretty sure, there are no examples of foot-slipping mixed with foot-ik. Happy to share back!
Notice how the snow ninjas slide around like they are skating on ice?
Finally, after three days of whining and complaining, nobody pointed out my error, despite my posts. I had to work out for myself why my callstack was corrupted. And I did so. With no help ;)
If you don't like how often I am posting, either ban me, or help me. I am at least offering feedback with positive results, despite my complaints.
I'm embarrassed when I am totally wrong, but this time, I caught a deserialization bug you can reproduce.

-------------------------

Modanung | 2019-03-01 10:53:19 UTC | #12

[quote="Leith, post:11, topic:4974"]
If you don’t like how often I am posting, either ban me, or help me. I am at least offering feedback with positive results, despite my complaints.
[/quote]

I'm not asking you to post less. I'm just saying the more often you *wrongfully assume with seeming certainty* a bug to be outside your own code, the more your credibility (when it comes to identifying bugs) may be reduced.
I think it saves [FUD](https://en.wikipedia.org/wiki/Fear%2C_uncertainty_and_doubt) when simply speaking of "unexpected behavior" for instance, until you have more certainty about the root cause.

-------------------------

Leith | 2019-03-01 10:58:26 UTC | #13

im not worried about my street cred mate, this is not my first engine
If i come off looking like a fool, at least at the end I post the answer, while nobody else did

-------------------------

lezak | 2019-03-01 11:44:01 UTC | #14

I guess this thread is nice example of what @Modanung is saying. Your statement:

[quote="Leith, post:10, topic:4974"]
The issue is RigidBody::ApplyAttributes after reload - a flag is not being observed because its default value is false, and I didn’t change it in my code. The issue is that attributes dont get applied after a reload.
[/quote]
doesn't seem right. It's enought to have a quick look at the rigidBody source to see that when attributes (collision mask and layer also) are loaded, 'MarkBodyDirty' is called and this method sets 'readdBody_' to true and therefore when attributes are applied AddBodyToWorld is called, so Your minor change (commenting out readdBody check) should make absolutely no difference. 
Right now I don't have much time to check this closer, but i made quick efford to reproduce Your problem by simply loading ninja object (it's serialized with rigid body) and it seems that everything is working as expected, readd flag is changed when loading, AddBodyToWorld is called on ApplyAttributes.

-------------------------

Leith | 2019-03-01 12:17:07 UTC | #15

after reload, the relevant flag is still false, and so ApplyAttributes does nothing - check your facts, I do
that modification to the engine allowed me to proceed to find the true cause, but it was part of the problem, and it was not my code doing it (or rather, not doing it). For your satisfaction sir, I shall issue a tiny PR tomorrow to cover this issue, which was just a sub-issue for me.

-------------------------

lezak | 2019-03-01 12:33:59 UTC | #16

When rigid body is created, before loading attributes:
![before|690x169](upload://cg4vXDjnBEupf2kWLvyDYzrc6g3.png) 
After loading attributes, when ApplyAttributes is called:
![after|690x168](upload://oCsUOgotFEZe39dBGlF38qU4hA.png) 
It's this way because of this:

> URHO3D_ATTRIBUTE_EX("Collision Layer", int, collisionLayer_, **MarkBodyDirty**, DEFAULT_COLLISION_LAYER, AM_DEFAULT);

And MarkBodyDirty is:
>void MarkBodyDirty() { readdBody_ = true; }

-------------------------

Leith | 2019-03-02 01:09:32 UTC | #17

After loading, I do one more unusual thing... I disable the gamescene node hierarchy...  later, when I enable it again, readdBody is false... looks like the "enabled" flag does not get along well with the "readdBody" flag.

-------------------------

