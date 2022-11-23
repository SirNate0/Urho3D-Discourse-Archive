GoogleBot42 | 2017-01-02 01:04:35 UTC | #1

When I generate a project using rake can try to compile I get this error:

[code]GoogleBot42@Comp ~/Desktop/Rake-Test/Build-Linux64 % make
Scanning dependencies of target Main
[100%] Building CXX object CMakeFiles/Main.dir/Urho3DPlayer.cpp.o
In file included from /usr/local/include/Urho3D/Graphics/GraphicsImpl.h:26:0,
                 from /home/GoogleBot42/Desktop/Urho3D/Urho3D.h:83,
                 from /home/GoogleBot42/Desktop/Rake-Test/Urho3DPlayer.cpp:23:
/usr/local/include/Urho3D/Graphics/OpenGL/OGLGraphicsImpl.h:36:23: fatal error: GLEW/glew.h: No such file or directory
 #include <GLEW/glew.h>
                       ^
compilation terminated.
CMakeFiles/Main.dir/build.make:54: recipe for target 'CMakeFiles/Main.dir/Urho3DPlayer.cpp.o' failed
make[2]: *** [CMakeFiles/Main.dir/Urho3DPlayer.cpp.o] Error 1
CMakeFiles/Makefile2:60: recipe for target 'CMakeFiles/Main.dir/all' failed
make[1]: *** [CMakeFiles/Main.dir/all] Error 2
Makefile:75: recipe for target 'all' failed
make: *** [all] Error 2
2 GoogleBot42@Comp ~/Desktop/Rake-Test/Build-Linux64 %   [/code]

This error is strange because when I set up the project myself it works just fine.  I am using the lastest git version of Urho3D...

-------------------------

weitjong | 2017-01-02 01:04:36 UTC | #2

How did you install your SDK? I am not able to reproduce your problem using my Linux host system. This is what I have tried in a nutshell.
[code]
$ cd /path/to/my/Urho3D/project/root
$ rake cmake
$ rake make
$ sudo rake make install
$ rake scaffolding dir=/tmp/test
$ cd /tmp/test
$ rake cmake
$ rake make
[/code]

-------------------------

