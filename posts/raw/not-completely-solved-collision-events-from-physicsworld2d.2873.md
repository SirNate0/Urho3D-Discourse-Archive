Eugene | 2017-03-09 17:00:01 UTC | #1

Is there any possibilty to get the same collision events from Box2D as from Bullet?
I am pretty infamiliar with Box2D physics... In fact, I started to work with it today.

**Upd:** Damn, I somehow missed `PhysicsEvents2D` /_-
Solved.

-------------------------

Eugene | 2017-03-09 17:00:40 UTC | #2

Huh. How to parse b2Contact at the script side?
Shall I write some wrappers for it?

-------------------------

1vanK | 2017-03-09 18:07:38 UTC | #3

There is no chance to make real Box2D game on scripts currently. For example to make one side platforms I redefine PhysicsWorld2D class and compare pointers to shapes to detect collision player sensors with ground and walls

-------------------------

Eugene | 2017-03-11 10:39:31 UTC | #4

Is my PR similar to your changes in Urho2D?

-------------------------

1vanK | 2017-03-11 12:24:31 UTC | #5

  http://discourse.urho3d.io/t/one-way-platform/2792

-------------------------

Eugene | 2017-03-11 12:43:35 UTC | #6

I see.
IMO, my way is cleaner.
However, I still feel a bit uncomfortable about that HashSet of contacts and its cleanup...

    class OneSidePlatform : ScriptObject
    {
        void Start()
        {
            SubscribeToEvent(node, "NodeUpdateContact2D", "HandleNodeUpdateContact2D");
        }

        void HandleNodeUpdateContact2D(StringHash eventType, VariantMap& eventData)
        {
            Node@ otherNode = eventData["OtherNode"].GetPtr();
            VectorBuffer points = eventData["ContactPoints"].GetBuffer();
            Vector2 contactPosition = points.ReadVector2();
            Vector2 contactNormal = points.ReadVector2();
            if (contactNormal.y < 0.5)
                eventData["Enabled"] = false;
        }
    }

-------------------------

1vanK | 2017-03-11 13:59:43 UTC | #7

Box2D uses own memory allocator for hundreds created/destroy contacts. So I think copying its to own structures/adding to lists destroys the whole idea. I have no idea how to combine speed and convenience. May be using Box2D memory allocator for own purposes.

EDIT:
https://www.codeproject.com/Articles/17060/A-Fast-Efficient-Allocator-for-Small-Blocks-of-Mem
https://habrahabr.ru/post/274827/

-------------------------

Eugene | 2017-03-11 14:05:04 UTC | #8

I don't copy contacts, I just strore pointers.
Moreover, I store pointers only for contacts that are disabled on client side.

My concern is about HashSet clenup. Box2D may skip EndContact in some artificail cases, and such contact will stay in HashSet forever:
> Note: if you set the number of contact points to zero, you will not get an EndContact callback

I think I shall do something with it before merging PR...

-------------------------

1vanK | 2017-03-11 14:13:07 UTC | #9

[quote="Eugene, post:8, topic:2873"]
I don't copy contacts, I just strore pointers.
[/quote]

This is even worse: http://box2d.org/manual.pdf

> Caution 
> Do not keep a reference to the pointers sent to b2ContactListener. Instead make a 
> deep copy of the contact point data into your own buffer. The example below 
> shows one way of doing this.

-------------------------

Eugene | 2017-03-11 14:36:42 UTC | #10

Huh. That sounds bad.
Unfortunatelly, they don't explain why and what will happen if I do.
They suggest to copy interesting data from contact, but I have no interest in contact content. I need to somehow identify contact in-between. If Box2D has no way to do it, these callbacks are piece of ship.
I shall probably ask on Box2D forum...

-------------------------

1vanK | 2017-03-13 07:04:50 UTC | #11

I think we should just allow Box2D to re enable contacts every frame. It is documented behavior and used everywhere. Islands and forces also cleared every step.
```
	/// Enable/disable this contact. This can be used inside the pre-solve
	/// contact listener. The contact is only disabled for the current
	/// time step (or sub-step in continuous collisions).
	void SetEnabled(bool flag);
```
Anyway you can not just disable contact and forget about him. For one side platform you should check conditions every step and enable/disbale collisions. If you want two bodies to never interact, then you better use collision categories and groups

-------------------------

Eugene | 2017-03-13 10:20:06 UTC | #12

[quote="1vanK, post:11, topic:2873"]
I think we should just allow Box2D to re enable contacts every frame. It is documented behavior and used everywhere. Islands and forces also cleared every step.
[/quote]

This sounds reasonable.
However, I don't know how to walk around this malicious re-enabling if I make one-side platform.
I can correctly check normal of contact only on the very first step. After that I have no relevant information about the contact.

Then please help me to rewrite this to something logically equivalent:

    void HandleNodeUpdateContact2D(StringHash eventType, VariantMap& eventData)
    {
        Node@ otherNode = eventData["OtherNode"].GetPtr();
        VectorBuffer points = eventData["ContactPoints"].GetBuffer();
        Vector2 contactPosition = points.ReadVector2();
        Vector2 contactNormal = points.ReadVector2();
        if (contactNormal.y < 0.5)
            eventData["Enabled"] = false;
    }

Note that I don't know anything about object shapes here.

-------------------------

1vanK | 2017-03-13 11:34:49 UTC | #13

I do not understand why this works. In my tests normal can be directed in opposite directions randomly.

> Then please help me to rewrite this to something logically equivalent:

Why not official method? https://github.com/erincatto/Box2D/blob/master/Box2D/Testbed/Tests/OneSidedPlatform.h

-------------------------

Eugene | 2017-03-13 11:47:42 UTC | #14

[quote="1vanK, post:13, topic:2873"]
I do not understand why this works. In my tests normal can be directed in opposite directions randomly.
[/quote]
Wow. Why? Or maybe I just was lucky... But I always had good normals.

This doesn't matter, actually. I may check position and it would be really meaningful only on the first iteration.

[quote="1vanK, post:13, topic:2873"]
Why not official method?
[/quote]
Because 

`position.y < m_top + m_radius - 3.0f * b2_linearSlop`

what's this piece of shit and how does it work for e.g. rotating box actor?

-------------------------

1vanK | 2017-03-13 11:48:13 UTC | #15

I was not interested in the case for a rotated box (my character always vertical), but I think there's no problem in finding out the bottom coordinate of the transformed box.

-------------------------

Eugene | 2017-03-13 11:52:24 UTC | #16

I want one-way obstacle to work with any simulated object with unknown shape.
So... I can't imagine how to make this code generic enough.

And anyway... This is so dirty. Real check is trivial - if begin point of the contact is on passable side, ignore this contact forever. I want to make the same (so simple!) logic in Box2D.

-------------------------

1vanK | 2017-03-13 12:09:44 UTC | #17

> I want one-way obstacle to work with any simulated object with unknown shape.

if contact exists, you can use AABB to get bottom coord

-------------------------

Eugene | 2017-03-13 12:16:27 UTC | #18

1. Rigid body don't have AABB in its API.
1. What about diagonal platforms?

Box2D author may get medal of the most awkward architecture.
Small bugfeature that breaks ton of possibilities. Great.

-------------------------

1vanK | 2017-03-13 12:23:07 UTC | #19

> Rigid body don't have AABB in its API.

b2Shape::ComputeAABB()

> What about diagonal platforms?

I will repeat, I was not interested in this question on practice, and I can not quickly answer this question, how to effectively deal with the situation, if both shapes are transformed

-------------------------

Eugene | 2017-03-13 12:27:02 UTC | #20

I understood. I am just trying to find nice solution.

Do you know how to match BeginContact and EndContact if Box2D recommend not to store pointers on contacts?

-------------------------

1vanK | 2017-03-13 12:36:10 UTC | #21

fixtures can contain user data SetUserData (currently it is pointer to Urho3D::CollisionShape2D)
but currently has no way to identify urho's components, so I compare pointers

```
void PlayerLogic::HandleNodeBeginContact2D(StringHash eventType, VariantMap& eventData)
{
    using namespace NodeBeginContact2D;
    CollisionShape2D* shape = (CollisionShape2D*)eventData[P_SHAPE].GetPtr();
    CollisionShape2D* otherShape = (CollisionShape2D*)eventData[P_OTHERSHAPE].GetPtr();

    if (shape == bottomSensor_)
        bottomSensorContacts_.Push(otherShape);
}

void PlayerLogic::HandleNodeEndContact2D(StringHash eventType, VariantMap& eventData)
{
    using namespace NodeBeginContact2D;
    CollisionShape2D* shape = (CollisionShape2D*)eventData[P_SHAPE].GetPtr();
    CollisionShape2D* otherShape = (CollisionShape2D*)eventData[P_OTHERSHAPE].GetPtr();

    if (shape == bottomSensor_)
        bottomSensorContacts_.Remove(otherShape);
}
```

-------------------------

