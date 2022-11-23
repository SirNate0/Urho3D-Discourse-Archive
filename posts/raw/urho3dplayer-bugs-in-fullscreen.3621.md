zakk | 2017-09-30 14:38:17 UTC | #1

Hello,

I encountered this bug with 3 differents machines running ArchLinux, with Urho3D packaged for it or not («or not» => i've used the pre-compilated 64 binaries).

Since my first try with Urho3D ,some years ago, i see this bug.

How to see the bug ? Simple, just run an example (Lua or AngelScript) in fullscreen mode.
`~/sources/Urho3D-1.7-Linux-64bit-SHARED/usr/local/bin/Urho3DPlayer 01_HelloWorld.lua`

Results: the screen goes black (just see the mouse pointer, nothing else). Obviously, the sample covers the whole screen, as a high priority window. I cannot see other windows previously opened, and cannot open new windows on top of the UrhoPlayer one.

I have to switch to a virtual term for killing the player (`pkill -9 Urho3DPlayer`).

Results in the term, after Urho3DPlayer process has been killed:

> [Sat Sep 30 16:30:59 2017] INFO: Opened log file /home/zakk/.local/share/urho3d/logs/01_HelloWorld.lua.log                                                                                                                       
> [Sat Sep 30 16:30:59 2017] INFO: Created 1 worker thread                                                                                                                                                                         
> [Sat Sep 30 16:30:59 2017] INFO: Added resource path /home/zakk/sources/Urho3D-1.7-Linux-64bit-SHARED/usr/local/bin/../share/Urho3D/Resources/Data/                                                                              
> [Sat Sep 30 16:30:59 2017] INFO: Added resource path /home/jzakk/sources/Urho3D-1.7-Linux-64bit-SHARED/usr/local/bin/../share/Urho3D/Resources/CoreData/                                                                          
> [Sat Sep 30 16:30:59 2017] INFO: Added resource path /home/zakk/sources/Urho3D-1.7-Linux-64bit-SHARED/usr/local/bin/../share/Urho3D/Resources/Autoload/LargeData/                                                                
> [Sat Sep 30 16:30:59 2017] INFO: Set screen mode 1920x1080 fullscreen monitor 0                                                                                                                                                  
> Killed

By the way, the resolution of my screen is 1920x1080, so it should be ok.

>  ~$ xrandr
> Screen 0: minimum 320 x 200, current 1920 x 1080, maximum 8192 x 8192
> eDP-1 connected primary 1920x1080+0+0 (normal left inverted right x axis y axis) 309mm x 173mm
>    1920x1080     60.05*+
>    1400x1050     59.98  
> (etc…)


In windowed mode, there is no problems.
` ~/sources/Urho3D-1.7-Linux-64bit-SHARED/usr/local/bin/Urho3DPlayer 01_HelloWorld.lua -w`

Results: the sample runs fine, and i've got this in the term:

> [Sat Sep 30 16:26:56 2017] INFO: Opened log file /home/zakk/.local/share/urho3d/logs/01_HelloWorld.lua.log                                                                                                                       
> [Sat Sep 30 16:26:56 2017] INFO: Created 1 worker thread                                                                                                                                                                         
> [Sat Sep 30 16:26:56 2017] INFO: Added resource path /home/zakk/sources/Urho3D-1.7-Linux-64bit-SHARED/usr/local/bin/../share/Urho3D/Resources/Data/                                                                              
> [Sat Sep 30 16:26:56 2017] INFO: Added resource path /home/zakk/sources/Urho3D-1.7-Linux-64bit-SHARED/usr/local/bin/../share/Urho3D/Resources/CoreData/                                                                          
> [Sat Sep 30 16:26:56 2017] INFO: Added resource path /home/zakk/sources/Urho3D-1.7-Linux-64bit-SHARED/usr/local/bin/../share/Urho3D/Resources/Autoload/LargeData/                                                                
> [Sat Sep 30 16:26:56 2017] INFO: Set screen mode 1024x768 windowed monitor 0                                                                                                                                                     
> [Sat Sep 30 16:26:56 2017] INFO: Initialized input                                                                                                                                                                               
> [Sat Sep 30 16:26:56 2017] INFO: Initialized user interface                                                                                                                                                                      
> [Sat Sep 30 16:26:56 2017] INFO: Initialized renderer                                                                                                                                                                            
> [Sat Sep 30 16:26:56 2017] ERROR: Could not initialize audio output                                                                                                                                                              
> [Sat Sep 30 16:26:56 2017] INFO: Initialized engine                                                                                                                                                                              
> [Sat Sep 30 16:26:56 2017] INFO: Loaded Lua script 01_HelloWorld.lua                                                                                                                                                             
> [Sat Sep 30 16:26:56 2017] INFO: Loaded Lua script LuaScripts/Utilities/Sample.lua                                                                                                                                               
> [Sat Sep 30 16:26:56 2017] INFO: Executed Lua script 01_HelloWorld.lua 

Thank you for reading,
Zakk.

-------------------------

weitjong | 2017-09-30 16:46:57 UTC | #2

I can reproduce this problem on my Fedora 64-bit system using the downloaded package from SF.net. My screen has even higher native resolution (1920x1200). However, I do not think this is a bug with Urho3DPlayer specifically or with Urho game engine in general. Because, when I build everything from source using proper (proprietary) graphical driver then running in fullscreen is a non issue. I would suspect the problem is with how the package is being built. All the packages are built using Ubuntu VM with Mesa graphic driver. I have tested the same package on one of my Ubuntu VM with Mesa graphical driver and sure enough I could run "fullscreen" there without any problem (the VM itself is just a window in my host, but as far as Urho3DPlayer is concerned, it was running fullscreen in the VM).

-------------------------

zakk | 2017-09-30 18:21:39 UTC | #3

I understand.

I have tested on three machines: two of them use the intel GPU , so it's the intel driver of Xorg with mesa.
The other one is using nvidia proprietary driver, so it's using its own opengl API.

If i understand well, i shouldn't have any problems with the machines using the intel GPU for display, should i ?

I've looked in Xorg.log. It's using this driver:

`[   593.991] (II) Loading /usr/lib/xorg/modules/drivers/intel_drv.so`

I think it's using mesa, because of these lines:

    [   594.023] (II) AIGLX: enabled GLX_MESA_copy_sub_buffer
    [   594.023] (II) AIGLX: enabled GLX_SGI_swap_control and GLX_MESA_swap_control

I think that a workaround could be to detect the native resolution, and then using a windowed mode with no borders (no window decoration), at the same resolution. I don't know if it's working on a MS-Windows platform (may be there's no problem with fullscreen on MS-Windows).
Of course, best thing would be to correct the problem :) Tell me if i can help.

Thank you for reading,
Zakk.

-------------------------

weitjong | 2017-10-01 00:27:43 UTC | #4

Actually you misunderstood what I said a little bit. Ideally we should not care how the package is being built and the software should just work on our system, provided we have a proper graphics driver that supports our screen native resolution. In my case, if I have a working nvidia graphics driver then I should not have the problem in fullscreen regardless. However, in reality it does not work that way. When I ran the `ldd` command on the binaries and compared them, I could clearly see the difference between the one I built myself and the one from the package, indicating the software in the prebuilt package is not as universal as we want it to be.

On the other hand, if your system only has low end integrated graphics card and/or only has Mesa installed then it is a totally separate problem. In this case, even when I were to send you my good copy of binaries instead of prebuilt package, you would probably still face the fullscreen issue and other rendering artifacts caused by the low end card or Mesa itself on your end. Mesa still have quite a few miles to go to support 3D in high screen resolution, IMHO.

p.s. Running "fullscreen" in my VM worked is not because I have a matching graphics driver, but I believe it is simply because the "fullscreen" in guest OS has lower screen resolution that Mesa can still stomach.

-------------------------

zakk | 2017-10-01 09:25:28 UTC | #5

Hello Weitjong,

Yes i'm not sure to understand all, so let's make some more experiments :slight_smile: 

I don't think it's a mesa problem or a resolution too-high for a tired chipset ;) . And as you said, it should work with nvidia (same problems with my nvidia card).

To be sure, i tried this :

`~/sources/Urho3D-1.7-Linux-64bit-SHARED/usr/local/bin/Urho3DPlayer 01_HelloWorld.lua -x 1920 -y 1080 -borderless -v -t -w`

The `-v` and `-t` was to be as close as possible to the fullscreen mode (i didn't knew if it forces vsync and triple buffering, so , just in case i put the options).
The sample is covering the whole screen at native resolution, without borders of windows. So it's an acceptable workaround.

With this options, the samples are working perfectly at the same resolution that the fullscreen mode couldn't achieve. So i guess the problem is elsewhere, at the initialisation. But the good news is Urho3D pre-packaged binaries are correct.

The output in my term with those options:

> [Sun Oct  1 11:16:02 2017] INFO: Opened log file /home/zakk/.local/share/urho3d/logs/01_HelloWorld.lua.log                                                                                                                       
> [Sun Oct  1 11:16:02 2017] INFO: Created 1 worker thread                                                                                                                                                                         
> [Sun Oct  1 11:16:02 2017] INFO: Added resource path /home/zakk/sources/Urho3D-1.7-Linux-64bit-SHARED/usr/local/bin/../share/Urho3D/Resources/Data/                                                                              
> [Sun Oct  1 11:16:02 2017] INFO: Added resource path /home/zakk/sources/Urho3D-1.7-Linux-64bit-SHARED/usr/local/bin/../share/Urho3D/Resources/CoreData/                                                                          
> [Sun Oct  1 11:16:02 2017] INFO: Added resource path /home/zakk/sources/Urho3D-1.7-Linux-64bit-SHARED/usr/local/bin/../share/Urho3D/Resources/Autoload/LargeData/                                                                
> [Sun Oct  1 11:16:02 2017] INFO: Set screen mode 1920x1080 windowed monitor 0 borderless                                                                                                                                         
> [Sun Oct  1 11:16:02 2017] INFO: Initialized input                                                                                                                                                                               
> [Sun Oct  1 11:16:02 2017] INFO: Initialized user interface                                                                                                                                                                      
> [Sun Oct  1 11:16:02 2017] INFO: Initialized renderer                                                                                                                                                                            
> [Sun Oct  1 11:16:02 2017] ERROR: Could not initialize audio output                                                                                                                                                              
> [Sun Oct  1 11:16:02 2017] INFO: Initialized engine                                                                                                                                                                              
> [Sun Oct  1 11:16:02 2017] INFO: Loaded Lua script 01_HelloWorld.lua                                                                                                                                                             
> [Sun Oct  1 11:16:02 2017] INFO: Loaded Lua script LuaScripts/Utilities/Sample.lua                                                                                                                                               
> [Sun Oct  1 11:16:02 2017] INFO: Executed Lua script 01_HelloWorld.lua


Thank for reading,
Zakk.

-------------------------

weitjong | 2017-10-01 09:51:32 UTC | #6

Technically speaking you are still only using windowed mode. To me, the correct binary should just work in fullscreen without any workaround on host system with proper graphics driver installed, which is not the case right now with our prebuilt package. And therefore, we always advice to rebuild the library and samples from source.

-------------------------

zakk | 2017-10-01 10:04:41 UTC | #7

Ok, i will compile a binary for my system.

I will have a look to the part of code which do the fullscreen,too. Seems «fishy» (normal for Urho? :)).

But how can we do for distributing binaries, then ? Without the need to recompile everything ?
Because it can be hard to ask this to someone who just wanted to play :slight_smile:

But if i've well understood , fullscreen is ok with Ubuntu, so maybe it's more a problem of DLL hell ? (a problem of versions of libs which are not the same outside of Ubuntu world ?)

Thank you for reading,
Zakk.

-------------------------

weitjong | 2017-10-01 14:03:23 UTC | #8

That's not what I meant obviously. I just suspect that our prebuilt packages from Travis-CI VM may not up to normal expectation. It is a free service, so we cannot complain much. If we have the money to setup a proper build farm, I suppose we would not have this issue. We could also use flatpak or something like that to create a true universal packages. Just in case you are not aware, our current build artifacts are just an afterthought. We use Travis mainly for our CI need.

-------------------------

zakk | 2017-10-01 10:49:53 UTC | #9

I tried to create the AUR package for Urho3D on a machine which works fast.
The binaries are working on the machine itself, but i get a segfault with `illegal instruction` when i run on another. Usually, i can prepare Arch packages on this machine without problems.

I've removed all my special flags (for core i5 optimization and so), and compile in pure blend mode, but still i get the `illegal instruction`. Something just after the stub of the executable. It's hard to debug as i'm not even sure to have the proper instruction (may be with objdump ?).

It's a different issue, not related to this thread, but it shows that distributing binaries of Urho3d is not a piece of cake. (as i've removed all my own compilations flags, i should now look in the cmake generated makefile).

So in fact, your farm of compilation is doing an excellent job :slight_smile:
At least, binaries can be launched.

Thank you for reading,
Zakk.

-------------------------

weitjong | 2017-10-01 14:10:19 UTC | #10

May be you just forgot to set deployment target build option. By default our build system will use the "native" and expect the package maintainers to adjust the deployment target according to their own target audience.

-------------------------

zakk | 2017-10-01 14:12:47 UTC | #11

Yes, that's it!

I've used `generic` as deployement target, and now it works on my other machine without segfaulting.

For the Archlinux PKGBUILD , it is:

> cmake "$srcdir/Urho3D-$pkgver/" -DCMAKE_INSTALL_PREFIX="/usr" -DURHO3D_USE_LIB_DEB=1 -DURHO3D_DEPLOYMENT_TARGET="generic"

And i can run Urho3DPlayer in fullscreen without problems, too.

Thank you :slight_smile:

-------------------------

