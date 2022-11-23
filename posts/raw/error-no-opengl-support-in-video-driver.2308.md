OMID-313 | 2017-01-02 01:14:37 UTC | #1

Hi all,

I installed Urho3D on Ubuntu 14 (on VMware on Windows) following the instructions here ([github.com/urho3d/Urho3D/wiki/G ... d-in-Linux](https://github.com/urho3d/Urho3D/wiki/Getting-started-in-Linux)).

After that, I rebooted the system.

Then I tried to run the Ninja example by:
cd /Urho3D/bin
. NinjaSnowWar.sh

But it gives the following error:

[Sat Oct  8 18:31:40 2016] INFO: Opened log file /root/.local/share/urho3d/logs/NinjaSnowWar.as.log
[Sat Oct  8 18:31:40 2016] INFO: Added resource path /home/omid/Urho3D/bin/Data/
[Sat Oct  8 18:31:40 2016] INFO: Added resource path /home/omid/Urho3D/bin/CoreData/
[Sat Oct  8 18:31:40 2016] INFO: Added resource path /home/omid/Urho3D/bin/Autoload/LargeData/
[Sat Oct  8 18:31:40 2016] ERROR: Could not create window, root cause: 'No OpenGL support in video driver'

How can I solve this problem ?

-------------------------

Lumak | 2017-01-02 01:14:38 UTC | #2

As the wiki page mentions, there's more extensive info at [url]https://urho3d.github.io/documentation/1.6/_building.html[/url].

Here's the apt-get list when I was installing on Bash on Ubuntu on Windows.

[code]
apt-get update
apt-get install build-essential
apt-get install freeglut3 freeglut3-dev
apt-get install unixodbc-dev
apt-get install libegl1-mesa-dev
apt-get install libx11-dev libxcursor-dev
apt-get install libxext-dev libxi-dev
apt-get install libxinerama-dev libxrandr-dev
apt-get install libxrender-dev libxss-dev libxxf86vm-dev
apt-get install libasound2-dev
apt-get install libaudio-dev
apt-get install libesd0-dev
apt-get install libpulse-dev
apt-get install libroar-dev
apt-get install libreadline6-dev
apt-get install cmake
[/code]

-------------------------

Lumak | 2017-01-02 01:14:38 UTC | #3

I just read on your other post about you having Nvidia GeForce 9400 GT. If you go into the software manager or device manager (can't remember which I looked into), you can find an Nvidia driver to install.

The apt-get install list that I provided was also used to install on my VMWare and VirtualBox and that worked for me.

-------------------------

OMID-313 | 2017-01-02 01:14:38 UTC | #4

[quote="Lumak"]I just read on your other post about you having Nvidia GeForce 9400 GT. If you go into the software manager or device manager (can't remember which I looked into), you can find an Nvidia driver to install.

The apt-get install list that I provided was also used to install on my VMWare and VirtualBox and that worked for me.[/quote]

Thanks @Lumak for your reply.

I installed all the items in your apt-get list above, but again it didn't work. The same error.

I also checked the additional drivers section for Nvidia drivers, but it doesn't show anything.
I searched a little on google, people say it's not possible to install nvidia driver on vmware.

So, what do I have to do !!?

-------------------------

OMID-313 | 2017-01-02 01:14:38 UTC | #5

Still I'm getting the same error:

[b]ERROR: Could not create window, root cause: 'No OpenGL support in video driver'[/b]

What should I do to solve this ?

I've installed Urho3D on Ubuntu 14.04 on VMware on Win 7 .
My graphics card is Nvidia GeForce 9400 GT, but it seems that VMware doesn't use it.

Any suggestions !!!!?

-------------------------

OMID-313 | 2017-01-02 01:14:38 UTC | #6

Here's some info:

[code]root@ubuntu:/home/omid/Urho3D/bin# ldd 01_HelloWorld

linux-gate.so.1 =>  (0xb77de000)
libdl.so.2 => /lib/i386-linux-gnu/libdl.so.2 (0xb77c0000)
librt.so.1 => /lib/i386-linux-gnu/librt.so.1 (0xb77b7000)
libGL.so.1 => /usr/lib/i386-linux-gnu/mesa/libGL.so.1 (0xb7724000)
libstdc++.so.6 => /usr/lib/i386-linux-gnu/libstdc++.so.6 (0xb763c000)
libm.so.6 => /lib/i386-linux-gnu/libm.so.6 (0xb75f6000)
libgcc_s.so.1 => /lib/i386-linux-gnu/libgcc_s.so.1 (0xb75d9000)
libpthread.so.0 => /lib/i386-linux-gnu/libpthread.so.0 (0xb75bd000)
libc.so.6 => /lib/i386-linux-gnu/libc.so.6 (0xb740d000)
/lib/ld-linux.so.2 (0xb77e1000)
libexpat.so.1 => /lib/i386-linux-gnu/libexpat.so.1 (0xb73e4000)
libglapi.so.0 => /usr/lib/i386-linux-gnu/libglapi.so.0 (0xb73cb000)
libXext.so.6 => /usr/lib/i386-linux-gnu/libXext.so.6 (0xb73b8000)
libXdamage.so.1 => /usr/lib/i386-linux-gnu/libXdamage.so.1 (0xb73b4000)
libXfixes.so.3 => /usr/lib/i386-linux-gnu/libXfixes.so.3 (0xb73ad000)
libX11-xcb.so.1 => /usr/lib/i386-linux-gnu/libX11-xcb.so.1 (0xb73aa000)
libX11.so.6 => /usr/lib/i386-linux-gnu/libX11.so.6 (0xb7276000)
libxcb-glx.so.0 => /usr/lib/i386-linux-gnu/libxcb-glx.so.0 (0xb725e000)
libxcb-dri2.so.0 => /usr/lib/i386-linux-gnu/libxcb-dri2.so.0 (0xb7258000)
libxcb-dri3.so.0 => /usr/lib/i386-linux-gnu/libxcb-dri3.so.0 (0xb7253000)
libxcb-present.so.0 => /usr/lib/i386-linux-gnu/libxcb-present.so.0 (0xb724f000)
libxcb-sync.so.1 => /usr/lib/i386-linux-gnu/libxcb-sync.so.1 (0xb7248000)
libxcb.so.1 => /usr/lib/i386-linux-gnu/libxcb.so.1 (0xb7226000)
libxshmfence.so.1 => /usr/lib/i386-linux-gnu/libxshmfence.so.1 (0xb7223000)
libXxf86vm.so.1 => /usr/lib/i386-linux-gnu/libXxf86vm.so.1 (0xb721c000)
libdrm.so.2 => /usr/lib/i386-linux-gnu/libdrm.so.2 (0xb720c000)
libXau.so.6 => /usr/lib/i386-linux-gnu/libXau.so.6 (0xb7208000)
libXdmcp.so.6 => /usr/lib/i386-linux-gnu/libXdmcp.so.6 (0xb7201000)[/code]

And some more info:

[code]root@ubuntu:/home/omid/Urho3D/bin# lspci -vnn | grep VGA

00:0f.0 VGA compatible controller [0300]: VMware SVGA II Adapter 15ad:0405
Subsystem: VMware SVGA II Adapter [15ad:0405][/code]

Any suggestion what to do !!??!?!??

-------------------------

OMID-313 | 2017-01-02 01:14:38 UTC | #7

Some info on OpenGL :

[code]root@ubuntu:/home/omid/Urho3D/bin# glxinfo | grep OpenGL

OpenGL vendor string: VMware, Inc.
OpenGL renderer string: Gallium 0.4 on SVGA3D; build: RELEASE;  
OpenGL version string: 2.1 Mesa 10.3.2
OpenGL shading language version string: 1.20
OpenGL extensions:[/code]

-------------------------

weitjong | 2017-01-02 01:14:39 UTC | #8

Either clear the CMake cache then regenerate and rebuild; or just nuke the build tree and regenerate. The cache is a double edged sword. Once a wrong value is cached due to incomplete deps, it will linger even you fulfill the deps later.

-------------------------

OMID-313 | 2017-01-02 01:14:39 UTC | #9

[quote="weitjong"]Either clear the CMake cache then regenerate and rebuild; or just nuke the build tree and regenerate. The cache is a double edged sword. Once a wrong value is cached due to incomplete deps, it will linger even you fulfill the deps later.[/quote]

Thanks @weitjong for your reply.

Would you please help me how to do these ?
What commands do I have to run in terminal !?
(sorry, I'm new to linux)

-------------------------

OMID-313 | 2017-01-02 01:14:39 UTC | #10

[quote="weitjong"]Either clear the CMake cache then regenerate and rebuild; or just nuke the build tree and regenerate. The cache is a double edged sword. Once a wrong value is cached due to incomplete deps, it will linger even you fulfill the deps later.[/quote]

One more question @weitjong:

If I clear the cmake cache, and do the build process from the beginning, will it solve the graphics card problem of VMware !!?
How can I make sure I fullfill the deps [b][i]before [/i][/b]rebuilding the whole process !?

-------------------------

OMID-313 | 2017-01-02 01:14:39 UTC | #11

Ok.
I did it.

First I deleted the whole Urho3D folder.
Then Installed it from the beginning.
This time it didn't give any errors.
And also, the Ninja game works when I run it. (although with problems! just blue screen!!)

Thanks everyone for your support and help.

-------------------------

weitjong | 2017-01-02 01:14:42 UTC | #12

[quote="OMID-313"][quote="weitjong"]One more question @weitjong:

If I clear the cmake cache, and do the build process from the beginning, will it solve the graphics card problem of VMware !!?
How can I make sure I fullfill the deps [b][i]before [/i][/b]rebuilding the whole process !?[/quote][/quote]
Ideally the CMake build script should intervene and instruct the CMake to stop the build tree generation process when a mandatory software component is missing, instead of generating a build tree that could not be built successfully later on. As you can see there are still room for improvement in our build system.

It is one thing to build Urho3D library using a guest OS in a VM and it is quite another thing to actually running it in one. While the former is usually problem free (once all the prerequisite development software packages have been installed), the latter is almost always not the case (even when you have setup everything correctly, one would expect some kind of artifacts or worse performance, if the app could run at all). YMMV, but I found the VirtualBox with Guest Additions does provide an acceptable compromise to allow me to quickly test run the app in a VM.

EDIT: I should have also pointed out earlier that you should never use "root" account for compiling software. Should I have spotted this earlier, you won't get any of support from me.  :wink:

-------------------------

