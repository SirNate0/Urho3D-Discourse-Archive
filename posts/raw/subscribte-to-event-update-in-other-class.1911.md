Kanfor | 2017-01-02 01:11:25 UTC | #1

Hi, urhofans.

I have a own class when I would like to subscribe an event update.
Can I do it? Must I create a class like LogicComponent, for example?

Thank you very much!  :smiley:

-------------------------

hdunderscore | 2017-01-02 01:11:28 UTC | #2

You can definitely do it, and that's one of the main concepts :smiley:

Example using LogicComponent: [github.com/urho3d/Urho3D/blob/m ... ehicle.cpp](https://github.com/urho3d/Urho3D/blob/master/Source/Samples/19_VehicleDemo/Vehicle.cpp)  You could also use a regular Component.

Here's another option, inherit from a relatively lighter weight Object class if your class fits more of the subsystem concept: [github.com/urho3d/Urho3D/blob/m ... eCache.cpp](https://github.com/urho3d/Urho3D/blob/master/Source/Urho3D/Resource/ResourceCache.cpp)

All depends on your class.

-------------------------

Kanfor | 2017-01-02 01:11:35 UTC | #3

Thanks you!
It was very useful  :stuck_out_tongue:

-------------------------

