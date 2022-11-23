WangKai | 2021-04-06 14:41:31 UTC | #1

Hi guys,

I just found that if `RigidBody` with zero mass stops moving for a while, it will become **"deactivated"** and stops all collisions.
https://github.com/urho3d/Urho3D/blob/6802a83fcd259430098426480d6c045114c0786c/Source/ThirdParty/Bullet/src/BulletDynamics/Dynamics/btRigidBody.h#L499

It seems we need to set active to `DISABLE_DEACTIVATION` and add as an interface to `RigidBody`.

https://github.com/urho3d/Urho3D/blob/6802a83fcd259430098426480d6c045114c0786c/Source/ThirdParty/Bullet/src/BulletDynamics/Dynamics/btRigidBody.h#L518

Please correct me if this is not accurate.

-------------------------

