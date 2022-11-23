slapin | 2017-03-14 23:41:03 UTC | #1

Hi, all!

I want to implement picking-up items, and not just formally picking, but really putting an item in hand.

Imagine item like ragdoll or other physics object. It is currently laying on floor.
I want my player character and NPCs to be able to pick it up so that it displays in hands.

Lets look at simplest case: There is a ball which can be picked, carried and thrown into
basket for some score. But also the actual picking can be interrupted by others (others are player and/or npcs,
they can snatch a boll while picking). Also the actual picking animation should depend on weight of item.

What can be done to improve player experience here? Obvious plan like remove object,
put non-physical object into hand then spawn physical one on throwing is obvious, but there are some complications.
Some objects are to be simulated while carrying, like ragdoll, bucket of water, chain/rope. Of course there can be done some shortcuts and I will use some of them but now I'm interested in eye candy (will think about common sense later),
so I want to carry knocked-out NPC to safe place, or want to get rid of knocked-down enemy by throwing
him into river (these are just some random thoughts as example). Also carrying rope around with ability to drop and pick-up usigng any part of it (interesting combat tactics running around with chain to catch enemies, for example).
I understand how to move solid/rigid objects, but I wonder how to make simulated objects possible to carry...

-------------------------

TheComet | 2017-03-15 19:21:19 UTC | #2

These are just thoughts, but typically the biggest problem is the transition from animated bones to physically simulated bones.

Why? Animated bones are not bound by the physics world. They can move in ways that would be physically impossible, or otherwise require ridiculous forces to be possible. Attaching a physically simulated object to the hand of an animated bone can cause spastic results.

I can think of two solutions to this problem.

1) Keep track of the animated node's global position and calculate the required velocities or forces to position a physical object at that position. It is incredibly important to clamp these calculated forces to plausible values. The drawback with this approach is that when your animation does introduce impossible forces, the physics object will have to play catchup for a few frames before it stabilises again.

2) The better solution in my opinion is to use a combination of solution 1) and inverse kinematics to move the hand to the proper location of the physically simulated object.

I'm working on getting IK integrated into Urho3D (http://discourse.urho3d.io/t/inverse-kinematics/1819/26). Hopefully I will be able to complete this soon.

-------------------------

