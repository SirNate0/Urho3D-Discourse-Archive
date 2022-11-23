practicing01 | 2017-01-02 01:04:20 UTC | #1

Hello, I'm PhysicsWorld::Raycast()'ing and it works fine untill I cast from inside one of the objects.  I then get the error:
[code]
WARNING: Physics: Overflow in AABB, object removed from simulation
WARNING: Physics: If you can reproduce this, please email bugs@continuousphysics.com
WARNING: Physics: Please include above information, your Platform, version of OS.
WARNING: Physics: Thanks.
[/code]

The node then disappears.

Edit:  I got around it with a distance check: [github.com/practicing01/Urho3DT ... lision.cpp](https://github.com/practicing01/Urho3DTemplate/blob/master/SceneObjectMoveToWithCollision.cpp)

-------------------------

