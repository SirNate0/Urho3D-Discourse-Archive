fnadalt | 2018-11-14 18:10:35 UTC | #1

Hi! I need some help to implement scene objects "grabbing" by my character. Some scene props tagged as "items" should be held by hand. Items have RigidBody. Items are grabbed by pressing CTRL when colliding against them.
The first apprach I used was reparenting the item to the "hand" node and disabling its RigidBody. I has this issue when "dropping" it: https://discourse.urho3d.io/t/physics-issue-when-reparenting-node/4559/2.
The second approach was to disable physics at grabbing and re-enabling it when "dropping". Grabbed object transform is updated according to the hand node at FixedUpdate.
Neither of them performs well over network, being the item REPLICATED.
Any ideas?

https://github.com/fnadalt/World/blob/master/bin/Data/Scripts/Person.as.

-------------------------

Modanung | 2018-11-14 18:11:03 UTC | #2

Have you tried using `RigidBody::SetKinematic(true)` instead of disabling the rigid body?

-------------------------

Sinoid | 2018-11-14 20:32:18 UTC | #3

[quote="fnadalt, post:1, topic:4675"]
Neither of them performs well over network, being the item REPLICATED.
[/quote]

Can you explain how so? Things run slow or latency chokes it or what?

---

Create a kinematic body (flagged to be nonreactive to most everything in the scene) on the hand and point-constraint linking the hand and the object. When dropping, remove the constraint. Switch flags on your object as necessary.

Only suitable for short-term carry (constraints don't make sense for long-term carry, heavy), and if network latency is the problem then that's not going to be any better.

-------------------------

