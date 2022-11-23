practicing01 | 2017-01-02 01:07:45 UTC | #1

Hello, I've rented a vps and uploaded my game for testing.  I ran it with -Headless and got the error: "Error while loading shared libraries: libGL.so.1 cannot open shared object file: No such file or directory."  Any ideas on how to fix this (the vps is running ubuntu)?  Thanks for any help.

-------------------------

boberfly | 2017-01-02 01:07:45 UTC | #2

Hi,

You can apt-get libgl1-mesa-glx
[packages.ubuntu.com/search?keywo ... 1-mesa-glx](http://packages.ubuntu.com/search?keywords=libgl1-mesa-glx)

Which has libGL, but it's a bit shit that it brings in X11 for a VPS.

Perhaps headless needs some SDL flag to make it build in some kind of dummy mode, maybe wayland mode?
[hg.libsdl.org/SDL/file/tip/docs/README-linux.md](https://hg.libsdl.org/SDL/file/tip/docs/README-linux.md)

Or if Urho3D could work without any SDL for the purposes of headless...

-------------------------

practicing01 | 2017-01-02 01:07:46 UTC | #3

I installed urho's dependencies on the vps and the app loaded but now I'm getting an error from the server "Illegal Instruction".  Gdb backtrace says that it's at kNet::Network::Init()

-------------------------

weitjong | 2017-01-02 01:07:46 UTC | #4

Are you using the latest master branch? If yes then you must ensure you have configured your build to target the CPU on the VPS host correctly. Alternatively, build Urho natively there.

-------------------------

practicing01 | 2017-01-02 01:07:46 UTC | #5

The suggestion to compile on the vps worked, thanks for all the help! Is there any way around this?  It is a great hassle to do so via the command-line.

Pic: master server on the top putty terminal, server on the bottom, client on the right:
[img]http://img.ctrlv.in/img/15/10/24/562bc4187d9c4.png[/img]

-------------------------

weitjong | 2017-01-02 01:07:46 UTC | #6

What do you mean by that? I find the CLI to be convenient to use even though my host/build system is not headless :slight_smile:

Use the 'cat /proc/cpuinfo' on the target system to get the CPU information. Use that information to pass the right -march compiler flag when configuring a build tree in your local host/build system with URHO3D_DEPLOYMENT_TARGET build option.

-------------------------

