rogerdv | 2017-01-02 01:03:41 UTC | #1

I came back from vacatins, pulled and tried to compile, but Im getting this:

[code]/home/roger/projects/Urho3D/Source/Urho3D/generated/NetworkLuaAPI.cpp:40:30: fatal error: Network/Controls.h: No such file or directory
 #include "Network/Controls.h"
                              ^
compilation terminated.
make[2]: *** [Source/Urho3D/CMakeFiles/Urho3D.dir/generated/NetworkLuaAPI.cpp.o] Error 1
make[1]: *** [Source/Urho3D/CMakeFiles/Urho3D.dir/all] Error 2
make: *** [all] Error 2
[/code]

I have cleaned and ran cmake again, but the problem persists. How can I solve this?

-------------------------

GoogleBot42 | 2017-01-02 01:03:41 UTC | #2

#include "" cannot be used anymore in the head repo.  

You need to use #include <>

See this: [url]http://discourse.urho3d.io/t/new-build-system/715/1[/url]

-------------------------

cadaver | 2017-01-02 01:03:41 UTC | #3

Also, Controls.h is now part of the Input subdirectory, to allow using it when networking is not compiled in.

-------------------------

rogerdv | 2017-01-02 01:03:41 UTC | #4

Solved it by manually removing generated directory.

-------------------------

