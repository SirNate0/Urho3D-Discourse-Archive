grumbly | 2017-01-02 01:05:08 UTC | #1

Hi,

I see Urho doesn't (yet?) have a concave 2D polygon collision type. How best can I approximate this?

My first thought is to create a master node for my concave shape, within which are many nodes, each one with its own convex polygon. I'll take this route unless someone else has a better idea.

-------------------------

Mike | 2017-01-02 01:05:08 UTC | #2

This is a limitation of Box2D. You should try compound convex shapes in your node (1 node, 1body and 2+ convex shapes).

-------------------------

grumbly | 2017-01-02 01:05:12 UTC | #3

Thanks Mike, that works perfectly. I didn't know we could have multiple components of the same type on the same node (was thinking PhysicsWorld2D for example...).

-------------------------

