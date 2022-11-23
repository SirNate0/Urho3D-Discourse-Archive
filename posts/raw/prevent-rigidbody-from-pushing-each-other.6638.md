CE184 | 2020-12-28 06:45:26 UTC | #1

A common scenario: there are many different characters, we don't want them:
1. walk through each other (so we added rigid body with collision shape);
2. push away each other (this is a tricky one).

I searched a little bit and found (2) is quite a popular question around. I didn't see any straightforward solution but there are some workaround hack. For example, [this one](https://forum.unity.com/threads/how-to-disable-push-force-between-two-rigidbodies.486138/#post-5648188).

The basic idea is to have a parent-child nodes pair, and two rigid body with collision shape one slightly larger than the other. One set to kinematic while the other non-kinematic.

**But we need to disable the collision between those two rigid body.** However, we cannot directly use two different layer since rigidbody1 in character A would collide with rigidbody2 in character B. 
In Unity3D,  we can use ```Physics.IgnoreCollision(rigidbody1, rigidbody2)``` as mentioned in previous [link](https://forum.unity.com/threads/character-pushing-each-other-arg.410324/#post-2676397).

I did not find anything like that in Urho3D PhysicsWorld. I found someone mentioned a similar problem [here](https://discourse.urho3d.io/t/rigidbodies-ignore-collisionshapes-of-child-nodes/3648/2?u=ce184) that adding 'ignore pairs' into PhysicsWorld. But I don't know any easy way to do that without making my own version of Urho3D.

-------------------------

JSandusky | 2020-12-28 23:28:38 UTC | #2

You can add a **btOverlapFilterCallback** to the pair-cache in the broadphase.

The `m_clientObject` in the broadphase-proxy is a btCollisionObject* (most likely a btRigidBody*, but check CollisionObjectTypes enum against `getInternalType()`), so you can get the Urho3D RigidBody* from the `getUserPointer()`.

You can then add an ignore-list to Urho3D::RigidBody ( `bool IgnoreBody(WeakPtr<RigidBody> otherBody) const { return ignoreList_.Contains(otherBody); }`). 

You're probably going to want only do that test on bodies that are flagged as **CF_CHARACTER_OBJECT** which is a built-in flag that Bullet doesn't use (currently).

It's a janky filter (you have to force clear things, here and there) but for this sort of fire-and-forget-never-gonna-touch-it thing it'll be fine.

Edit: so yes, you have to make C++ changes.

-------------------------

CE184 | 2020-12-31 03:44:19 UTC | #3

Eventually, I hacked it this way:
make an outer collider only collide with the same type from other character, and set to be trigger; Then in the event handler function, I manually calculate characters nearby and deviates current velocity direction so that the perpendicular part is zero...

-------------------------

evolgames | 2020-12-31 06:44:53 UTC | #4

Depending on your goals, crowd agents might work better. The CrowdNavigation sample is great. There are avoidance parameters which will keep them apart. You say you dont want them to be pushed away, but I'm not sure exactly what. Like, no contact at all, or just not interfering with how the characters walk.

-------------------------

CE184 | 2020-12-31 06:50:16 UTC | #5

crowd algo can only deals with NPCs, this is mostly for Player-NPCs interaction. e.g. either NPC could push away Player or vice versa.

-------------------------

evolgames | 2020-12-31 06:55:44 UTC | #6

Well the player can be an agent too. And the NPCs will treat them as set. So if the player walks in a crowd the crowd will go around them. Kind of like Assassin's creed, but you'll have to polish it yourself.

-------------------------

CE184 | 2020-12-31 07:32:04 UTC | #7

didn't know the AC crowd moving is using crowd agent, will definitely take a look from this aspect! :smiley:

-------------------------

CE184 | 2021-01-04 19:20:31 UTC | #8

Followup: Crowd Agent is good for NPC-NPC avoidance and NPC-Player avoidance if the player is added as one agent. But for Player to NPC avoidance, it's tricky since I need to manually control the Player's movement, the player's freedom of degree is higher than the NPC, e.g. jump, fall off walls, which is impossible in the framework of NavMesh. So you have to do some customization anyway.

(I'd like NPC to do all the jump, fall off walls actions too, but it's much more complicated when using together with NavMesh. Both physics with RigidBody and NavMesh for navigation are not quite compatible with each other)

-------------------------

evolgames | 2021-01-05 18:32:07 UTC | #9

Oh yeah good point. My use case was simple npcs walking/running on a flat plane only. A more robust navmesh that could work with obstacles would be useful but I guess that'd need to be self-implemented.

-------------------------

