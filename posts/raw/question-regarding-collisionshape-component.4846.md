Leith | 2019-01-22 04:28:35 UTC | #1

Bullet is quite ok to share CollisionShapes among many RigidBodies.

Does our CollisionShape Component create a unique bullet collisionshape object per instance, or is it somehow able to recognize familiar collision shape objects as shared resources?

What I am getting at, is that if we have a thousand boxes all the same size, or a thousand mushrooms, we do not need a thousand copies of the same shape information.

-------------------------

QBkGames | 2019-01-28 01:11:30 UTC | #2

I might not be the best person to answer this as my inner knowledge of the engine is quite limited, but from having had a (brief) look at the physics code, I noticed the following:
- the complex shapes (mesh and hull based) share the geometry
- the primitive shapes are not shared but each node has individual copies
- internally all collision shape assigned to a Urho node are composite shapes

I guess this design trades the efficiency of sharing shapes with the flexibility of allowing you to easily add/remove any number of collision shapes to any node and automatically letting you have a transform for each shape (primitive shapes assume your model is centered which is really rarely the case).

-------------------------

