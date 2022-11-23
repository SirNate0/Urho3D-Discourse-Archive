ghidra | 2017-01-02 01:01:43 UTC | #1

Is it possible to use 2D physics in a 3D scene?

I've been playing around with making a shmup. I'm certain bullet can handle a large amount of objects, but I was also curious if I could just use Box2d instead?
At the moment i dont have a too many things going on. All the collision happen at y 0 anyway. Hopefully at some point, i could have many hundreds of bullets flying around... maybe a thousand or so.

-------------------------

weitjong | 2017-01-02 01:01:43 UTC | #2

Yes, I agree. In theory it should work. The 2D variants of the rigidbody and collisionshape are just normal component class that could be attached to any node. You just have to remember to also replace the physicworld3D to 2D at the root scene node.

-------------------------

