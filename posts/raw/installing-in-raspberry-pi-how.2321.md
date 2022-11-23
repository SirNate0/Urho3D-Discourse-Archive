OMID-313 | 2017-01-02 01:14:43 UTC | #1

Hi guys.

I'm trying to install Urho3D on RPi 3 (GPU=768 MB).

First, I tried the general linux method described here: [github.com/urho3d/Urho3D/wiki/G ... d-in-Linux](https://github.com/urho3d/Urho3D/wiki/Getting-started-in-Linux)
But it gave error during the final make process:
[code]
[ 56%] Building CXX object Source/Urho3D/CMakeFiles/Urho3D.dir/Graphics/Skybox.cpp.o
[ 57%] Building CXX object Source/Urho3D/CMakeFiles/Urho3D.dir/Graphics/Graphics.cpp.o
In file included from /root/Urho3D/Source/Urho3D/Graphics/../Graphics/GraphicsImpl.h:29:0,
                 from /root/Urho3D/Source/Urho3D/Graphics/Graphics.cpp:34:
/root/Urho3D/Source/Urho3D/Graphics/../Graphics/OpenGL/OGLGraphicsImpl.h:36:23: fatal error: GLES2/gl2.h: No such file or directory
 #include <GLES2/gl2.h>
                       ^
compilation terminated.
Source/Urho3D/CMakeFiles/Urho3D.dir/build.make:1916: recipe for target 'Source/Urho3D/CMakeFiles/Urho3D.dir/Graphics/Graphics.cpp.o' failed
make[2]: *** [Source/Urho3D/CMakeFiles/Urho3D.dir/Graphics/Graphics.cpp.o] Error 1
CMakeFiles/Makefile2:1198: recipe for target 'Source/Urho3D/CMakeFiles/Urho3D.dir/all' failed
make[1]: *** [Source/Urho3D/CMakeFiles/Urho3D.dir/all] Error 2
Makefile:137: recipe for target 'all' failed
make: *** [all] Error 2[/code]

Someone suggested to run cmake_rpi.sh instead of cmake . in the cmake process.

But when I run . cmake_rpi.sh it gives the following:

[code]Usage: cmake_genereic.sh /path/to/build-tree [build-options][/code]

So, what shall I do !?
How can I install Urho3D in RPi !!?

-------------------------

OMID-313 | 2017-01-02 01:14:44 UTC | #2

Ok. I did it.
I had to define a path!
I used the following command:
[code]. cmake_rpi.sh /home/pi/Urho3D/[/code]
I hope the ongoing make process doesn't give any more errors.

-------------------------

