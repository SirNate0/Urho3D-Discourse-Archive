yushli | 2017-01-02 01:09:23 UTC | #1

suppose the following code:
HashMap test;
for (auto one : test) {
}
It compiles successfully in VS2015, and Linux with android ndk, but when building in windows with android ndk(r10d), the following errors occur:

error: 'begin' was not declared in this scope
for (auto one : test) {
note: suggested alternative:
In file included from E:/android-ndk-r10d/sources/cxx-stl/gnu-libstdc++/4.9/include/string:51:0,
from E:/android-ndk-r10d/sources/cxx-stl/gnu-libstdc++/4.9/include/random:40,
from E:/android-ndk-r10d/sources/cxx-stl/gnu-libstdc++/4.9/include/bits/stl_algo.h:66,
from E:/android-ndk-r10d/sources/cxx-stl/gnu-libstdc++/4.9/include/algorithm:62,
from D:/software/Urho3D_dev/Source/Urho3D/GameMei/../Container/ForEach.h:30,

I see begin is defined in HashMap.h, and also this file is included. What's possibly wrong here?

-------------------------

