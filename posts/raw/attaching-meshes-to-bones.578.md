rogerdv | 2017-01-02 01:01:29 UTC | #1

Is there any way to attach a mesh to an skeleton bone? I was looking at Skeleton class and I dont see anything I can use for that. Perhaps there is another approach to this?

-------------------------

weitjong | 2017-01-02 01:01:29 UTC | #2

Each skeleton's bone has a scene node. Have you tried to attach a static model component to this node?

-------------------------

rogerdv | 2017-01-02 01:01:29 UTC | #3

I was thinking the Ogre way (and I think Unigine does the same, with attach points). In Ogre, I used specific bones to attach helmets, weapons, etc.
Im looking right now at the docs and see that I can get the node from a bone.

-------------------------

codingmonkey | 2017-01-02 01:01:30 UTC | #4

first of all your needs skeleton with one or few animations (animated rig).
you export model from 3d editor and import it to urho
then you import the animated model you will get a hierarchy of nodes, in same place with AninationModel component.
in these nodes you can put other nodes or yours models (staitc, animated, dyn...).
and when you play the animation to the skeleton(or some of his childs bones), those objects that you previously linked to some node of skeleton - will move too.

-------------------------

