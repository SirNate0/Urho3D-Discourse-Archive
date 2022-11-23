OMID-313 | 2017-01-02 01:14:41 UTC | #1

Hi everyone.

I'm trying to install Urho3D on RPi 3. (GPU = 768 MB)

I installed all the essential dependencies. All the steps went fine.
Until this error which occurred during the final [b][i]make [/i][/b]step:

[code][ 56%] Building CXX object Source/Urho3D/CMakeFiles/Urho3D.dir/Graphics/Skybox.cpp.o
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

Any suggestions?
What should I do !?

-------------------------

weitjong | 2017-01-02 01:14:42 UTC | #2

Although it is not related, do not use "root" account for anything else than administering your system!

-------------------------

OMID-313 | 2017-01-02 01:14:42 UTC | #3

[quote="weitjong"]Although it is not related, do not use "root" account for anything else than administering your system![/quote]

Thanks @weitjong for your point.

One question:
Do I have to run [b]"cmake_rpi.sh"[/b] instead of [b]"cmake ."[/b] ?
(I followed the general linux tutorial.)

-------------------------

