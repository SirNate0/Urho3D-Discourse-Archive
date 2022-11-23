slapin | 2017-01-02 01:15:24 UTC | #1

Hi, all!

I currently work on tool which should allow me to create ragdolls
(as it is currently very hard and frustrating task).
The idea is to be able to select bone with mouse click and be able to
create RigidBody, CollisionShape  and Constraint allowing settings, rotation, etc.
And write the result as xml (or whatever format)for later use.

The planned feature is to start simple, i.e. something similar to Unity ragdoll wizard,
but done in different way. So we select subset of bones we want for ragdoll
and set them to a category, also setting masses and constraint axes (could not find
how to do this automagically).

Of course doing
this I've met a lot of first-type problems of showstopper kind and would appreciate all
help with these.
My current completion status is here: [youtu.be/rsq9gtbxb4E](https://youtu.be/rsq9gtbxb4E) so
to visually show the idea.

What I come up with is 3D model displayed in view and allowing to select bones
and do various things:

- I need to implement a way for user to see which local bone axes point in which direction,
so I need to draw such geometry. As I understand I just need to add StaticModel to bone node
which shows axes and the bone transform for bone node will do the rest. Is it correct?

- I need to indicate the selection, i.e. I need to show which bone is selected on 3D model.
The best would be to show what bone is current among axes. The direction axes are pointing is important
for constraints use and placement, while dependency is not really well grasped yet.
Also I need to know the length of bone. Basically I need to know 2 points - base and tip,
so I could draw some geometry on top.

- In addition I need to visualize collision shapes - I wanted to go cheap way and use debug geometry for that,
but somehow this doesn't work as debug geometry is somehow overdrawn by actual model geometry (can be seen
on video). But if debug geometry can be made working that would be much better.

If these 3 problems get solved the rest seems to be trivial to do. I just wonder why nobody did this yet?
(or is there some works in the area?)

Thanks!

-------------------------

Mike | 2017-01-02 01:15:24 UTC | #2

I think first and only step is to procedurally generate the ragdoll. This has already been discussed in a couple of threads.
That way you don't have to rely on xml definitions or oyher complicated setups.

From what I remember Unity expects bones to be oriented in a standard way, so if you don't use the correct orientation or use a reversed hip setup you may get into trouble. This certainly also applies here.

-------------------------

slapin | 2017-01-02 01:15:25 UTC | #3

Well, the "procedural ragdoll" thing applies only to bone bounding boxes, as I see,
but as for constraints it is really not known how to match constraints, and that is really a problem for me too.
I think that it should be possible using reference skeleton (ragdoll template) to know what needs to be
rotated (axis rotation) to make things work, to make things work. But I still can't get there...

-------------------------

