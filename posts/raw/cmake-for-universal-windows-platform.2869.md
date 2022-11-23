NiteLordz | 2017-03-08 14:25:56 UTC | #1

I have recently been playing with the UWP, and i got a version working within UWP.  However, i am not using SDL (it's a modified Urho3D port).  I was wondering, if we could get a CMAKE toolchain to build a solution in VS 2015, or 17 for UWP, and what would it take. 

I am not skilled in CMAKE at all, but would be more than willing to help.

-------------------------

rku | 2017-03-08 14:45:55 UTC | #2

    CMake -G "Visual Studio 14 2015" -DCMAKE_SYSTEM_NAME=WindowsStore -DCMAKE_SYSTEM_VERSION=10.0 

That came from [first google result](http://stackoverflow.com/questions/31857315/how-can-i-use-cmake-to-generate-windows-10-universal-project).

-------------------------

