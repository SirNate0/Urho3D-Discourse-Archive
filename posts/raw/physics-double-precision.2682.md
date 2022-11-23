apat | 2017-01-06 23:29:00 UTC | #1

If I want to use bulletphysics in double precision mode, I guess I have to recompile the bullet library with the

#define BT_USE_DOUBLE_PRECISION

Will the urho3d bulletphysics integration part still work?

-------------------------

cadaver | 2017-01-07 14:46:26 UTC | #2

If Bullet API changes to doubles, I'm fairly sure it won't work. The Urho scene model still operates on floats, and the physics integration code even does some nasty reinterpret-casts to write to Bullet's vectors, assuming its and Urho's Vector3 memory layout matches. You're welcome to work on that and contribute a PR.

-------------------------

apat | 2017-01-07 19:40:54 UTC | #3

Ok, I'll see if I figure something out. I'll try to not change so much in the scene model, just convert bullets double data to float for Urho3D. Thanks for your answer!

-------------------------

