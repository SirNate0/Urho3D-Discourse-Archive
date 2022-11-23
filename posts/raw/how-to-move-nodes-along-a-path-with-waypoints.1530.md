tommy3 | 2017-01-02 01:08:19 UTC | #1

is there an easy way to move nodes along a path with waypoints?

i've already tried 'SplinePath' but it needs other nodes as control points. what i'm searching is a way to use a collection of e.g. Urho3D::Vector3 as waypoints for the path.

imagine a 2d point and click adventure with a walkable area where you can send characters around. it would be a useful feature in combination with NavigationMesh::FindPath(...).

-------------------------

tommy3 | 2017-01-02 01:08:19 UTC | #2

thanks for your reply. i knew this example already. i guess it should be possible to implement a component or so to manage a path and the movement for a node to be able to attach this behaviour/ability to a node. i will try to build such a thing...

-------------------------

1vanK | 2017-01-02 01:08:19 UTC | #3

I wrote a similar component for the project [github.com/1vanK/Urho3D-Color-L ... r/Path.cpp](https://github.com/1vanK/Urho3D-Color-Lines/blob/master/Path.cpp) but it is a highly specialized. It is not difficult to realize the component to fit your needs.

-------------------------

tommy3 | 2017-01-02 01:08:19 UTC | #4

very cool. thank you for the link.

-------------------------

1vanK | 2017-01-02 01:08:19 UTC | #5

It should be remembered that is the old source. In some places you need rename defines (eg OBJECT -> URHO3D_OBJECT) and update Urho3dAl.h ([github.com/1vanK/Urho3DAll.h](https://github.com/1vanK/Urho3DAll.h))

-------------------------

