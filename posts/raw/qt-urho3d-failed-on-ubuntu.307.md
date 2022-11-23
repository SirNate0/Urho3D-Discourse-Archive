aster2013 | 2017-01-02 00:59:31 UTC | #1

Hi, all

I have created an editor for with Qt + Urho3D. When I run it on Windows, it work well. but when I run it on Ubuntu (with Virtual Box), it failed and report:

[code][Tue Jun 17 22:36:45 2014] INFO: Opened log file Urho3DEditor.log
deterministic_cache: unknown level/typenumber combo (2/1), cannot
deterministic_cache: recognize cache type
[Tue Jun 17 22:36:45 2014] INFO: Created 1 worker thread
[Tue Jun 17 22:36:45 2014] INFO: Added resource path /home/aster/Documents/Urho3D/Bin/CoreData/
[Tue Jun 17 22:36:45 2014] INFO: Added resource path /home/aster/Documents/Urho3D/Bin/Data/
libGL error: failed to authenticate magic 3
libGL error: failed to load driver: vboxvideo
[Tue Jun 17 22:36:45 2014] ERROR: Could not create OpenGL context
[/code]

How to fix it?

-------------------------

jorbuedo | 2017-01-02 00:59:31 UTC | #2

Looks like a problem with virtualbox graphics adapter. Try to modify virtualbox settings and install the guest additions.

-------------------------

alexrass | 2017-01-02 00:59:32 UTC | #3

File Source\Engine\Graphics\OpenGL\OGLGraphics.cpp
line 464:
change
        [code]if (!GLEW_EXT_framebuffer_object || !GLEW_EXT_packed_depth_stencil)[/code]
to
        [code]if (!GLEW_EXT_framebuffer_object /*|| !GLEW_EXT_packed_depth_stencil*/)[/code]

works ok.

-------------------------

