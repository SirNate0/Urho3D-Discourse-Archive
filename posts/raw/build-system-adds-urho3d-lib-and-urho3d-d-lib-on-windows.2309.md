godan | 2017-01-02 01:14:38 UTC | #1

I'm using Urho3D as a static lib in a bunch of projects. I use the all the standard CMake stuff, and overall everything works great. However, on Windows Visual Studio builds, I get both Urho3D and Urho3D_d libs in included in the Release configuration.
 
In the Debug configuration, I only get the Urho3D_d. Currently I go through and manually delete the lib reference, but since I build a bunch of projects at one time, this is getting to be a pain.

-------------------------

1vanK | 2017-01-02 01:14:38 UTC | #2

[github.com/urho3d/Urho3D/issues/1523](https://github.com/urho3d/Urho3D/issues/1523)

-------------------------

