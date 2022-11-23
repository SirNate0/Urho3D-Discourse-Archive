najak3d | 2022-01-26 23:50:29 UTC | #1

We have a non-rigged mesh with multiple geometries, one of which is a propeller, that we'd like to spin manually.  Is there a way to do this without rigging it to a bone?   I'm not finding an API for rotating a sub-mesh, unless it were attached rigidly to a bone.

-------------------------

JTippetts1 | 2022-01-27 00:56:27 UTC | #2

Transforms belong to Node, and bones are held internally as Nodes, so if you want to transform a thing you need to attach it to a Node somehow, either as a bone or as a separate child Node. So if you don't want to use a bone you'll probably need to have the propeller as a separate object attached to a Node that is a child of the plane.

-------------------------

dertom | 2022-01-27 02:16:31 UTC | #3

As @JTippetts said and since you are using urho.net you can perfectly use Actions. Actually in the SamplyDemo there is excatly that:

https://github.com/Urho-Net/Samples/blob/2935180e5a280350455211ed7f344422add7fa05/SamplyGame/Source/Aircrafts/Player.cs#L39

-------------------------

najak3d | 2022-01-27 05:31:02 UTC | #4

Thanks!   OK - looks like I'd need an AnimatedModel to make it work with a bone.

We are displaying up to 1000 windmills in the scene, each with rotating propeller (although we may only animate the ones close to camera).   And we are using the "StaticModelGroup" -- so looks like if we want to Animate these while keeping them instances, we're going to need to split the mesh into two parts, each part of a separate StaticModelGroup, and we'll animated by rotating the Node.

Does Urho support Instancing (similar to StaticModelGroup) for AnimatedModel's?    We'd have all models animated in unison so all Skeletal states would be shared (same state).   

(To keep it from looking too creepy with all in unison, we'd employ 5 groups total and intersperse them, and spin at different rates.)

We'd prefer to do this with instanced AnimatedModels.   If we can't, then we may resort to splitting this into 2 Static Models (2nd model will be the turbine blades).

-------------------------

