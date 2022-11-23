Leith | 2019-04-20 05:59:12 UTC | #1


I've recently been fighting an issue with respect to rootmotion (something I'd like to incorporate) : Mixamo animations don't have a root bone, they apply translation directly to the skeleton root bone (ie the hips).

I've come up with a 14-point workflow (for Blender) for adding root bones to affected animations (ie those that contain root motion). It involves creating a new root bone for the hips, between the feet, which coincides with where we expect the model origin to be:) I appreciate that it would be astute to use the same root bone name on every affected animation. The workflow involves creating a new bone at (typically 0,0,0), adding translation keyframe channels to the new bone, copying the translation of the "previous" root bone (generally "Hips") to the new bone, deleting the translation keyframes from previous root bone (except for the first key), and parenting the hips to the new root bone, while preserving offset. It's exhausting!

My question is in two parts - since I am changing the skeleton hierarchy, will I also need to re-export the Model? And secondly, will I need to perform these changes to all animations - even though some don't need it - or will exported animations target the most appropriate root bone, even if some bones fail to be mentioned?

-------------------------

Lumak | 2019-04-20 15:49:04 UTC | #2

Have you looked at rku's work:
https://discourse.urho3d.io/t/root-motion-patch/4464

-------------------------

rku | 2019-04-20 16:51:25 UTC | #3

Why don't you use hip bone as root bone?

-------------------------

Leith | 2019-04-21 02:20:23 UTC | #4

I tried using hip as root bone, the problem with that is that the offset from the character root node to the hips is not constant (even a simple walk contains desirable translation keys on the hips) - and when (desired) root motions translate the hips, that translation is not transferred to the character root node. If I want to avoid adding a root bone that coincides with the character root node, I have to wait until after animation occurs, and then teleport the character root and physics capsule to synch them to the animated hips. Seems a lot simpler to fix the bad assets than try to deal with it in code. 

And yeah, I saw the proposed root motion patch - but like the other guys, I need the final deltas, not the deltas per animationstate but the blended deltas. I tried measuring and applying hip deltas but the values are often tiny, and numerical precision errors quickly mount up.

Just adding (to animations, and to our rig) a root bone at the origin (0,0,0) and retargeting hip translation to the new root bone should make all my troubles go away, since I now have two nodes whose world positions should be equality-constrained - the character root node (direcly under the physics capsule) and the skeleton root bone can then easily be constrained to the same world position.

-------------------------

Leith | 2019-04-26 08:49:51 UTC | #5

I've experimented with using DrawableUpdateFinished (?) to measure delta-transforms on the Hips and apply (some of) those deltas to my character's root node and physics hull, but the results are "unpleasant". This was a bit of a fail for me.
The problem really is that my character has a RootBone, but my animations don't get applied to it. For animations, the root bone is "Hips", the Skeleton has a "RootBone" that never receives animation, and the real boss node, owner of my character controller, is not the node that applies default rotation and scale! I need to transfer animation from one track to another. AnimationController offers no way to do it. Doing it in code should have been trivial, but isn't working. Sigh.

-------------------------

