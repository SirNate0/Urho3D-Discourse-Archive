umen | 2017-01-02 01:08:50 UTC | #1

Hello all
i tired to build the engine using Linux CentOS 6.7 64 bit 
with all the additional OpenGL libraries installed as it pointed in the documents , 
like this:
[code][root@localhost Urho3D]# ./cmake_eclipse.sh /root/Documents/Dev/3d/Orho3d/git/buildeclispe  -DURHO3D_SAMPLES=1
-- The C compiler identification is GNU 4.4.7
-- The CXX compiler identification is GNU 4.4.7
-- Could not determine Eclipse version, assuming at least 3.6 (Helios). Adjust CMAKE_ECLIPSE_VERSION if this is wrong.
-- Check for working C compiler: /usr/bin/cc
-- Check for working C compiler: /usr/bin/cc -- works
-- Detecting C compiler ABI info
-- Detecting C compiler ABI info - done
-- Check for working CXX compiler: /usr/bin/c++
-- Check for working CXX compiler: /usr/bin/c++ -- works
-- Detecting CXX compiler ABI info
-- Detecting CXX compiler ABI info - done
-- Looking for include file stdint.h
-- Looking for include file stdint.h - found
-- Looking for XOpenDisplay in /usr/lib64/libX11.so;/usr/lib64/libXext.so
-- Looking for XOpenDisplay in /usr/lib64/libX11.so;/usr/lib64/libXext.so - found
-- Looking for gethostbyname
-- Looking for gethostbyname - found
-- Looking for connect
-- Looking for connect - found
-- Looking for remove
-- Looking for remove - found
-- Looking for shmat
-- Looking for shmat - found
-- Found X11: /usr/lib64/libX11.so
-- Found OpenGL: /usr/lib64/libGL.so  
-- Performing Test HAVE_CONST_XEXT_ADDDISPLAY
-- Performing Test HAVE_CONST_XEXT_ADDDISPLAY - Success
-- Performing Test HAVE_CONST_XDATA32
-- Performing Test HAVE_CONST_XDATA32 - Success
-- Found ALSA: /usr/lib64/libasound.so (found version "1.0.22") 
-- Could NOT find PulseAudio development library (missing:  PA_LIBRARIES PA_INCLUDE_DIRS) 
-- Performing Test COMPILER_HAS_HIDDEN_VISIBILITY
-- Performing Test COMPILER_HAS_HIDDEN_VISIBILITY - Success
-- Performing Test COMPILER_HAS_HIDDEN_INLINE_VISIBILITY
-- Performing Test COMPILER_HAS_HIDDEN_INLINE_VISIBILITY - Success
-- Performing Test COMPILER_HAS_DEPRECATED_ATTR
-- Performing Test COMPILER_HAS_DEPRECATED_ATTR - Success
-- Found Urho3D: as CMake target
-- Could NOT find Doxygen (missing:  DOXYGEN_EXECUTABLE) 
-- Configuring done
-- Generating done
-- Build files have been written to: /root/Documents/Dev/3d/Orho3d/git/buildeclispe[/code]

the C make script did successfully run and created the make-file parallel  to the Urho3d source code .
from within eclipse i open it as "Make project with excising code " 
then in the top project which named "buildeclipse"  i did right click -> build project 
and i got :
[code]11:21:51 **** Build of configuration Default for project buildeclispe ****
make all 
Scanning dependencies of target FreeType
[  0%] Building C object Source/ThirdParty/FreeType/CMakeFiles/FreeType.dir/src/autofit/autofit.c.o
In file included from /root/Documents/Dev/3d/Orho3d/git/Urho3D/Source/ThirdParty/FreeType/include/freetype/freetype.h:33,
                 from /root/Documents/Dev/3d/Orho3d/git/Urho3D/Source/ThirdParty/FreeType/src/autofit/afpic.c:20,
                 from /root/Documents/Dev/3d/Orho3d/git/Urho3D/Source/ThirdParty/FreeType/src/autofit/autofit.c:21:
/root/Documents/Dev/3d/Orho3d/git/Urho3D/Source/ThirdParty/FreeType/include/freetype/config/ftconfig.h: In function ?FT_MulFix_x86_64?:
/root/Documents/Dev/3d/Orho3d/git/Urho3D/Source/ThirdParty/FreeType/include/freetype/config/ftconfig.h:484: error: #pragma GCC diagnostic not allowed inside functions
/root/Documents/Dev/3d/Orho3d/git/Urho3D/Source/ThirdParty/FreeType/include/freetype/config/ftconfig.h:485: error: #pragma GCC diagnostic not allowed inside functions
/root/Documents/Dev/3d/Orho3d/git/Urho3D/Source/ThirdParty/FreeType/include/freetype/config/ftconfig.h:524: error: #pragma GCC diagnostic not allowed inside functions
make[2]: *** [Source/ThirdParty/FreeType/CMakeFiles/FreeType.dir/src/autofit/autofit.c.o] Error 1
make[1]: *** [Source/ThirdParty/FreeType/CMakeFiles/FreeType.dir/all] Error 2
make: *** [all] Error 2

11:21:51 Build Finished (took 242ms)[/code]

looking at the code the error is in the FreeType
[code]   /* Temporarily disable the warning that C90 doesn't support */
    /* `long long'.                                             */
#pragma GCC diagnostic push
#pragma GCC diagnostic ignored "-Wlong-long"[/code]

im using this compiler :
g++ --version
g++ (GCC) 4.4.7 20120313 (Red Hat 4.4.7-16)

-------------------------

weitjong | 2017-01-02 01:08:50 UTC | #2

First of all, don't use root account.

-------------------------

umen | 2017-01-02 01:08:50 UTC | #3

Is it problem in compilation ? 
i have no problem to use root account this is desktop private PC, no need to create other accounts

-------------------------

weitjong | 2017-01-02 01:08:50 UTC | #4

Most probably not but I couldn't stand to read the thread any further. So, this is probably the last comment you get from me. Call me old timer.  :laughing:

-------------------------

umen | 2017-01-02 01:08:51 UTC | #5

I don't understand what you upset about but its a free world .. 
Comment out the problematic code , and the compilation seams ok
[b]BUT ![/b]
The examples are running very slow , i mean very very slow . 
is there any way to fine tune it or configure it running in the same speed as windows . 
both have 8 giga ram , on board video card

Compiled the irrlicht3d 1.8.3 engine just to get the feel of the speed  Examples and they are running much faster then Urho3D 
how can this explained ? can i run some checks to find what is the problem ?

-------------------------

cadaver | 2017-01-02 01:08:51 UTC | #6

If on Windows you're running in D3D mode then it's just probably that the Windows / D3D GPU drivers are well optimized and the Linux driver is badly written. Or you may even be running the software (Mesa) OpenGL driver. Typically when you're running good drivers the performance drop D3D vs OpenGL should be about 10% maximum.

-------------------------

umen | 2017-01-02 01:08:51 UTC | #7

Thanks for your replay , 
can you tell me please how do i configure Urho3d to compile / Run on the right drivers ?

-------------------------

cadaver | 2017-01-02 01:08:51 UTC | #8

There is no such configuration step. When starting up, Urho (or any Linux OpenGL program) loads the OpenGL library dynamically so whatever is installed to the system gets used.

-------------------------

umen | 2017-01-02 01:08:51 UTC | #9

Is there any way to understand why 
Urho3d examples are very slow , i mean very .
and Irrlicht3d examples are fast ?
i talking about the Irrlicht-1-8.3 02.Quake3Map example and the Demo

-------------------------

cadaver | 2017-01-02 01:08:51 UTC | #10

If I remember right Irrlicht uses fixed function for the most examples, while Urho always runs GLSL shaders and uses per-pixel shading, so it's certainly heavier.

If your requirement is to run on bad drivers or software mode then I believe Urho is not the right engine for you.

-------------------------

umen | 2017-01-02 01:08:51 UTC | #11

well i want to run it on as much of possible operating systems as many flavors of Linux included 
i think that the old Irrlicht used to run on fixed functions but now it is uing GLSL also .

-------------------------

bvanevery | 2017-01-02 01:08:52 UTC | #12

[quote="umen"]well i want to run it on as much of possible operating systems as many flavors of Linux included 
i think that the old Irrlicht used to run on fixed functions but now it is uing GLSL also .[/quote]

Let's make sure we're on the same page with basics.  What standalone video card or integrated circuit are you using?  Do you know about the differences between open source and proprietary driver performance on LInux?  They're huge.  Sorry Linux really doesn't have its act together in this area.  I did LInux for 3 years, only recently quit.  If you want performance on NVIDIA for instance, you use the proprietary driver.  The End [TM].  If you care about licensing politics, you give NVIDIA a stiff upper lip and suffer with the inferior open source stuff.  Phoronix has plenty of benchmarks proving the open source drivers are bad.  Would suggest downloading their test suite, it's an easy way to verify performance.

Some distros make it trivial to install or switch to proprietary driver.  Ubuntu, or anything Ubuntu derived like Mint.  Other distros have religion and you have to figure out driver switching yourself.

BTW "whose fault is it", the LInux drivers.  Linus gave middle finger to NVIDIA a few years back, and not without justification.  But nobody figured out whether the future was X11, Wayland, or Mir last I checked.  So who wants to deal with LInux platform confusion and work with such communities?  NVIDIA said we're sticking with desktop X11, screw you guys.  Can't blame them, the confusion is a waste of time and money.

-------------------------

umen | 2017-01-02 01:08:53 UTC | #13

Thanks for your replay , the truth is that im new with desktop Linux as GUI development at home . 
i know linux very well but only from server side stuff never did any graphic related always via ssh . 
but to test things i did compare it with another light engine and the result are different this is what makes me wander . 
the new irrlichet engine also using modern OpenGL . and its way faster then Urho3d . 
so i wander if it is  driver related .
i will compile other engine and will test . 
ogre3d and cube 2 and Horde3d

-------------------------

bvanevery | 2017-01-02 01:08:53 UTC | #14

That's cool but you know you didn't answer my question, right?   :smiley:  Granted I buried it under a lot of further talking.  This time I will refrain.

- what video card or integrated video are you using?
- do you know what driver you're using?

-------------------------

umen | 2017-01-02 01:08:53 UTC | #15

(:
i will check when i will be near it ...

-------------------------

bvanevery | 2017-01-02 01:08:53 UTC | #16

Uh oh meanwhile looks like you might have chosen one of those distros that's hostile to proprietary video drivers.  Still researching, will add further notes when I know for sure.  1st search on "Centos NVIDIA" turns up [url=http://linuxsysconfig.com/2014/09/nvidia-drivers-on-centos-7/]NVIDIA drivers on CentOS 7[/url]:
[quote]Since RPM Fusion doesn?t support RHEL / CentOS 7 and I didn?t feel like dealing with the Nvidia installer, I tried to find alternative package repositories. Fortunately I came across ELRepo which has been providing Nvidia drivers (from the long-lived branch release) in form of precompiled kernel drivers (kmod-nvidia) for a few months.[/quote]

RPM Fusion is a responsible, well curated repo that gets around RedHat / Fedora religious silliness about licenses.  If they're not handling CentOS 7, that's a bad sign.  Be very, very scared when someone offers you video drivers or X11 servers from amateurish 3rd party repos, like ELRepo sounds.  Last time I went down that road, it trashed my OS installation.  The repo [i]claimed [/i]it had tools to reverse the installation, but of course being an amateur hour production, they didn't work.  I can't remember who that offender was; surely someone more interested in having the bleeding edge of X11 everything than whether anything actually worked and was stable.  Lesson learned.  Get your drivers and any other key OS components from responsible sources.

Pending further evaluation of CentOS, and your own specific needs, I will offer the following advice.  For 3d game development, if the distro is getting in the way, [b]dump it[/b].  Not all distros are created equal for various kinds of development.  In particular, Fedora is hostile to proprietary drivers, so deriving from them you need RPM Fusion.    I will suggest Mint because I'm hostile to Ubuntu Unity's default Amazon spyware.  Mint basically replaces the components of Ubuntu that are objectionable.  Any Ubuntu-derived distro has a trivial control panel thingy for enabling a proprietary driver if you want it.  Which you do, if you don't have an Intel GPU.  Intel did a lot of open source stuff with their recent HW, not sure how that ends up in anyone's final code as I was running a NVIDIA machine those 3 years.

With Mint you lose a little bit of the release professionalism compared to straight Ubuntu.  I've had times when Mint systems worked fine, and times when they just wouldn't work on my old HW, so I had to do something else.  I did a lot of Lubuntu with the LXDE desktop.  For awhile there it was the best performing on old HW because it did the least while still being sane.  Looks like they're still releasing in sync with Ubuntu version numbers, so the project is not dead yet.  I had my doubts at one point due to all the Wayland / Mir hoopla, but hey if it works now then fine.  Lubuntu was definitely my best experience out of many distros on old HW.

I'm getting tired of looking for recent CentOS 7 NVIDIA installation tips.  Older articles from 2014 seem to indicate [url=https://www.linkedin.com/pulse/20140808222919-219659043-rhel-centos-7-and-nvidia-drivers]you've chosen "teh suk"[/url]:
[quote]
The most recent release, version 7, has a large number of the latest updates across the entire Linux community. This has both huge benefits and huge drawbacks. One simultaneous benefit/drawback is that 7 supports the open source NVidia driver, Nouveau, by default. For someone who just wants a 3D accelerated desktop experience this is wonderful news. For someone who needs to run applications that severely tax the video card, this is another obstacle to avoid before getting to work. Unfortunately, while the Nouveau driver provides acceptable performance, it does not use the full capabilities of the video card because, as of the writing of this article, the Nouveau drivers cannot dynamically change the clock speed. Since NVidia cards typically boot at their most power saving mode, this does not bode well for Linux power users.

All that to say that the Nouveau drivers need to be disabled prior to installing the NVidia drivers, which is a difficult task this time around. I just spent the worst 6 hours of my professional life trying to figure this one out, so let me save you the grief.
[/quote]
Wow if he only spent 6 hours on crap like that, he must have a dainty professional life!  Or a short one.  I wish I could figure out how to cut 'n' paste an image.  He has a great one of [red hat logo] + [nvidia logo] = [poison angry face].  He also did an [url=https://www.linkedin.com/pulse/rhel7centos-nvidia-drviers-updated-christopher-meacham]August 2015 followup[/url] that doesn't sound much better.  Please, save your soul and dump this CentOS thing.

-------------------------

umen | 2017-01-02 01:08:57 UTC | #17

here is my hardware info 
following this link:
[askubuntu.com/questions/28033/ho ... eo-drivers](http://askubuntu.com/questions/28033/how-to-check-the-information-of-current-installed-video-drivers)

[code]lspci -vnn | grep VGA -A 12
01:00.0 VGA compatible controller [0300]: NVIDIA Corporation GF119 [GeForce GT 610] [10de:104a] (rev a1) (prog-if 00 [VGA controller])
	Subsystem: NVIDIA Corporation GF119 [GeForce GT 610] [10de:104a]
	Flags: bus master, fast devsel, latency 0, IRQ 30
	Memory at f6000000 (32-bit, non-prefetchable) [size=16M]
	Memory at e8000000 (64-bit, prefetchable) [size=128M]
	Memory at f0000000 (64-bit, prefetchable) [size=32M]
	I/O ports at e000 [size=128]
	Expansion ROM at f7000000 [disabled] [size=512K]
	Capabilities: [60] Power Management version 3
	Capabilities: [68] MSI: Enable+ Count=1/1 Maskable- 64bit+
	Capabilities: [78] Express Endpoint, MSI 00
	Capabilities: [b4] Vendor Specific Information: Len=14 <?>
	Capabilities: [100] Virtual Channel
[/code]

[code]find /dev -group video
/dev/fb0
/dev/dri/card0
/dev/dri/renderD128
/dev/dri/controlD64
[/code]


[code]glxinfo | grep -i vendor
libGL error: unable to load driver: nouveau_dri.so
libGL error: driver pointer missing
libGL error: failed to load driver: nouveau
server glx vendor string: SGI
client glx vendor string: Mesa Project and SGI
OpenGL vendor string: Mesa Project
[/code]

it shows i have some drivers that can't be loaded i have no idea if this is related

-------------------------

bvanevery | 2017-01-02 01:08:57 UTC | #18

Yikes you've got a lousy open source NVIDIA driver.  Dump CentOS.

-------------------------

umen | 2017-01-02 01:08:57 UTC | #19

The Desire is to be as wide as possible .. not to dump the OS 
any way i see that other engines are also faster ... so the problem is not in the OS

-------------------------

boberfly | 2017-01-02 01:08:57 UTC | #20

CentOS is a perfectly valid OS to use, it is the go-to for the VFX industry so the Nvidia proprietary driver certainly works on it. I'm not sure about if there's easy installable RPMs anywhere, you could just install the official one from Nvidia (and make sure you re-install on every kernel update, or get DKMS to work).

bvanevery is correct, you probably don't want to use nouveau (the open source driver) if performance is concerned, and from the mesa result it looks like it can't find the dri driver so it might be using GL software mode.

Urho3D is very performance-oriented I wouldn't put the blame on the engine itself. To get to parity with Windows you will need to get the proprietary driver working. The Geforce 610 GPU is quite slow so you'd probably can't push it too far, most likely it is best to keep it in forward-rendering mode.

-------------------------

bvanevery | 2017-01-02 01:08:58 UTC | #21

[quote="boberfly"]CentOS is a perfectly valid OS to use, it is the go-to for the VFX industry so the Nvidia proprietary driver certainly works on it. I'm not sure about if there's easy installable RPMs anywhere, you could just install the official one from Nvidia (and make sure you re-install on every kernel update, or get DKMS to work).[/quote]

Ok the OP can enjoy the painful learning curve of how to install NVIDIA drivers manually.  I won't be helping with that problem; been there, done that!  Doesn't even sound like the OP's driver installation is healthy anyways.  But on distros that make this stuff complicated, life is too short for me to figure it out.  I did this sort of shuffle for 3 years....

-------------------------

TikariSakari | 2017-01-02 01:08:58 UTC | #22

I tried using Urho with linux mint and my experience of using Linux + urho was pretty good. I had a lot of problems with Mesa drivers on opengl3, but they worked decently with -gl2. Although after installing proprierity amd drivers on my old gpu (5870 hd), these issues went away + the performance increased quite a lot. Also in general I think if you don't need opengl3 features, things seem to work faster with opengl2 on urho3d, but then again I could be completely wrong about this.

On the other hand I had some very weird problem with the desktop environment Cinnamon. Apparently it is supposed to be new and all that good, but for some reason when I had 10+ windows open, the graphics started glitching on windows that were in like index of 10+, which seemed to be Urho a lot of times, because when I kept testing the code, eventually I had a situation where the window manager opened Urho in one of those buggy window slots, but this is about 1 year ago, and the source code has changed tremendously since then. Basically I had to use different DE than Cinnamon, those older ones seemed to work a lot better (MATE was something I really liked), and they even seemed to give slight boost in terms of fps, but then again I think my knowledge about 3D is quite weak and was even worse 1 year ago so I wouldn't really count that kind of performance test what I did back then really a good measure of what works faster and what doesn't.

My impression of Urho is, that the engine is actually performs really well on Android phones, or at least that's the conclusion I've come to. My guess is that Urho utilizes worker threads really to use CPU, and mobile phones seem to usually have really good CPUs but not so good GPUs, where as I think that most engines seem to go to the way of doing more and more stuff with GPU and completely clogging it up, while CPU itself isn't doing much.

The good side I noticed on Urho with Linux was that the compile times seemed a lot faster, and I think that is because despite I have upgared my CPU and GPU, I am still using HDD instead of SSD. Overall the HD seemed to perform far better in linux than it does on my windows partition, although I havent really booted into linux for quite some time.

-------------------------

umen | 2017-01-02 01:08:59 UTC | #23

Thanks for all for the answers 
I Appreciate it

-------------------------

bvanevery | 2017-01-02 01:08:59 UTC | #24

[quote="TikariSakari"]I had a lot of problems with Mesa drivers on opengl3, but they worked decently with -gl2.[/quote]

Well that's really the rub, and something you're going to learn if you dig through the Linux benchmarking ecology long enough.  Lots of those benchmarks on Phoronix, are only testing OGL 2.0 technology.  Which at this late a date, is dumb, and gives a totally false sense of confidence in 3d capabilities.  But, the benches are driven by the realities of volunteer open source game development on Linux.  They weren't doing a lot of 3.3+ or DX10+ stuff, they were pretty much in a Quake-derived ghetto.  Irrlicht, no different back then, they were 2.0.  Very few benches if any will test OGL 3.3+ technology.  Really the only one I found was the cross-platform Unity benchmarks, like Unigine Valley.  That's what I mostly used to figure out what was really going on with my OSes and drivers.

The hope was that by now, we'd all be rolling in SteamOS, Steam Machines, and drivers that Valve had beaten into shape.  Well, um, for having finally just released their HW in November, the press sure is quiet about what's going on.  I think that's a really bad sign.  I'm not going to be shocked if in a few months, someone finally pronounces the death of the Steam Machines.  It would be nice to be pleasantly surprised, but various people have been saying they were DOA even at conception.  Back when they started that ambition, I realize the new Windows 8 Store looked like a big scary threat to them.  So they came up with what they thought was a response.  Unfortunately that kind of response takes a lot of execution to pull off, and I think we're seeing that they're only Valve.  Meanwhile Windows 8 flopped, and the Windows Store hardly proved to be the threat to Steam that Valve thought.

Now, maybe they could worry all over again with Windows 10, because 10 is actually pretty good.  UI-wise certainly it is good, pretty much like 7 but with facepaint of 8.  Stability, well, I wanted to accuse my 2 Windows 10 laptops of blowing up the other day, but they may have been HW problems.  Hard to say.  MS shipped a huge update in November and both my machines had their troubles right after that.  Maybe MS quietly and sneakily has shipped their fixes for their bloopers, who knows.  My ancient 2007..2008 era laptops have worked fine with 10, which really surprised me, but the advice of waiting until the last minute before the Windows 10 free upgrade period closes, still sounds like good advice.

-------------------------

practicing01 | 2017-01-02 01:08:59 UTC | #25

Urho works well for me on mint linux and android.  I'm planning on buying a Steam Machine when they bundle one with Half-Life 3 and Source 2 :slight_smile:

-------------------------

