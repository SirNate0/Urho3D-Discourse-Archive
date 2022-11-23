JTippetts | 2017-01-02 01:12:14 UTC | #1

Hey guys.

Recently, my Windows install got bricked. Been trying to use Urho3D on Linux.

I've gotten Urho to build just fine, but when I run anything I get the error: "Could not create window, root cause: 'No OpenGL support in video driver'

I'm using Linux Mint, with the proprietary Radeon drivers from AMD. glxinfo reports:

OpenGL vendor string: Advanced Micro Devices, Inc.
OpenGL renderer string: AMD Radeon HD 6530D
OpenGL core profile version string: 4.3.13416 Core Profile Context 15.302
OpenGL core profile shading language version string: 4.40

Any suggestions?

-------------------------

JTippetts | 2017-01-02 01:12:14 UTC | #2

Sorry, guys, I figured it out.

According to a random forum thread I saw somewhere, SDL looks for gl.h, glx.h and glu.h to determine OpenGL support, but I hadn't installed libglu1-mesa-dev yet. (Brand new Linux install and all.) Installed the package, and it all works now.

-------------------------

weitjong | 2017-01-02 01:12:14 UTC | #3

I think you need to make sure your binary is indeed using the proprietary Radeon driver from AMD. Run this command to check "ldd binary-name". I am using proprietary nVidia driver, so my binary has output like this:
[code][weitjong@igloo Urho3D]$ ldd ../native-Build/bin/01_HelloWorld
	linux-vdso.so.1 (0x00007f9e02f2f000)
	libUrho3D.so.0 => /home/weitjong/ClionProjects/urho3d/native-Build/lib/libUrho3D.so.0 (0x00007f9e014de000)
	libdl.so.2 => /lib64/libdl.so.2 (0x00007f9e012a5000)
	librt.so.1 => /lib64/librt.so.1 (0x00007f9e0109d000)
	libm.so.6 => /lib64/libm.so.6 (0x00007f9e00d9b000)
	libGL.so.1 => /usr/lib64/nvidia/libGL.so.1 (0x00007f9e00a66000)
	libstdc++.so.6 => /lib64/libstdc++.so.6 (0x00007f9e006e4000)
	libgcc_s.so.1 => /lib64/libgcc_s.so.1 (0x00007f9e004cd000)
	libpthread.so.0 => /lib64/libpthread.so.0 (0x00007f9e002af000)
	libc.so.6 => /lib64/libc.so.6 (0x00007f9dffeee000)
	/lib64/ld-linux-x86-64.so.2 (0x000055912414c000)
	libnvidia-tls.so.358.16 => /usr/lib64/nvidia/tls/libnvidia-tls.so.358.16 (0x00007f9dffcea000)
	libnvidia-glcore.so.358.16 => /usr/lib64/nvidia/libnvidia-glcore.so.358.16 (0x00007f9dfe088000)
	libX11.so.6 => /lib64/libX11.so.6 (0x00007f9dfdd48000)
	libXext.so.6 => /lib64/libXext.so.6 (0x00007f9dfdb36000)
	libxcb.so.1 => /lib64/libxcb.so.1 (0x00007f9dfd913000)
	libXau.so.6 => /lib64/libXau.so.6 (0x00007f9dfd70f000)[/code]
Notice that the libGL.so shared library that the binary uses is pointing to nVidia implementation. Usually you don't want to use Mesa implementation, especially when you have the vendor-specific proprietary graphic driver installed.

-------------------------

JTippetts | 2017-01-02 01:12:14 UTC | #4

ldd did indicate at the time I was using the correct driver. At the time, I had not yet installed anything of Mesa, and I had uninstalled the open source AMD driver in favor of the proprietary. But I did not yet have any of the Mesa dev headers. After installing the Mesa dev headers and re-building Urho3D, then it worked correctly. I am unsure which GL headers were present at the time of my first build (ie, unsure which headers were present from the opensource driver), but it was only after I installed libgl1-mesa-dev and libglu1-mesa-dev that it worked correctly. It would build before that successfully, but executing anything would give me the OpenGL-not-supported error.

-------------------------

weitjong | 2017-01-02 01:12:14 UTC | #5

When you install a library's dev package, the package manager usually installs both the library package in question (if it is not installed yet) and then the dev package. Actually, it automatically installs all the dependency packages of the package you attempt to install. So, if I were you I would double check the apt-get's log to make sure it didn't inadvertently install Mesa on top of your Radeon. Your earlier.runtime error indicates there was something wrong with your Radeon driver installation. To fix it by installing some unrelated mesa dev package sounds weird to me.

-------------------------

JTippetts | 2017-01-02 01:12:14 UTC | #6

/usr/lib/libGL.so.1 does, indeed, still point to /usr/lib/fglrx/fglrx-libGL.so.1.2, the fglrx folder being where the Radeon driver is installed. That was the first thing I checked after installing the mesa headers, ready to fix the symlink if I had to.

I'm tempted to do another wipe and re-install, just to nail down the exact sequence of things I did, since I was also doing a whole bunch of other stuff at the same time to get other stuff set up.

-------------------------

