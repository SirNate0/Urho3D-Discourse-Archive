mikolan | 2020-07-28 11:59:55 UTC | #1

Hi.

I'm trying to build Urho3D on Raspberry Pi 4 platform.

The RPI build option links against the broadcom GLESv2 and EGL libraries, which aren't supported on Raspberry Pi 4.

Setting RPI=0 gives me some other issues due to assumptions about running on x86 platform at some places.

Has anyone managed to get this to run?

-------------------------

weitjong | 2020-07-28 12:58:24 UTC | #2

Don't hold your breath but RPI 4 64-bit will be supported soon.

-------------------------

weitjong | 2020-07-31 02:22:01 UTC | #3

I am able to cross-compile using 64-bit toolchain successfully now. However, I am not able to verify the build result as I am still not able to get my hand on the RPI4 board locally yet. I would appreciate if someone who has the board now can help me to verify.

In order to get the 64-bit binary, checkout from "upgrade-toolchains" branch and build it like so:
```
$ DBE_TAG=latest URHO3D_LUAJIT=0 URHO3D_ANGELSCRIPT=0 RPI_ABI=RPI4 script/dockerized.sh rpi
```

Yeah, both the scripting subsystems still not working yet for this port.

Edit: I should clarify that LUA actually built cleanly.

Edit2: Now LUAJIT and AngelScript scripting subsystems can be built cleanly too. So, just do this below.

```
$ DBE_TAG=latest RPI_ABI=RPI4 script/dockerized.sh rpi
```

After the latest DBE images are re-tagged as "master", even the "DBE_TAG=latest" option will not be required later.

Edit 3: Some checks on one of the sample 64-bit binary.

```
$ file build/rpi/bin/01_HelloWorld 
build/rpi/bin/01_HelloWorld: ELF 64-bit LSB executable, ARM aarch64, version 1 (GNU/Linux), dynamically linked, interpreter /lib/ld-linux-aarch64.so.1, for GNU/Linux 4.20.8, stripped

$ $RPI_PREFIX-readelf -d build/rpi/bin/01_HelloWorld 

Dynamic section at offset 0x9bbd68 contains 34 entries:
  Tag        Type                         Name/Value
 0x0000000000000001 (NEEDED)             Shared library: [libbcm_host.so.0]
 0x0000000000000001 (NEEDED)             Shared library: [libdl.so.2]
 0x0000000000000001 (NEEDED)             Shared library: [librt.so.1]
 0x0000000000000001 (NEEDED)             Shared library: [libm.so.6]
 0x0000000000000001 (NEEDED)             Shared library: [libGLESv2.so.2]
 0x0000000000000001 (NEEDED)             Shared library: [libstdc++.so.6]
 0x0000000000000001 (NEEDED)             Shared library: [libgcc_s.so.1]
 0x0000000000000001 (NEEDED)             Shared library: [libpthread.so.0]
 0x0000000000000001 (NEEDED)             Shared library: [libc.so.6]
 0x000000000000000f (RPATH)              Library rpath: [/usr/lib/aarch64-linux-gnu:]
 0x000000000000000c (INIT)               0x428ad8
 0x000000000000000d (FINI)               0xbe94d0
 0x0000000000000019 (INIT_ARRAY)         0xdcb658
 0x000000000000001b (INIT_ARRAYSZ)       1520 (bytes)
 0x000000000000001a (FINI_ARRAY)         0xdcbc48
 0x000000000000001c (FINI_ARRAYSZ)       8 (bytes)
 0x0000000000000004 (HASH)               0x400278
 0x000000006ffffef5 (GNU_HASH)           0x404b70
 0x0000000000000005 (STRTAB)             0x418c38
 0x0000000000000006 (SYMTAB)             0x409710
 0x000000000000000a (STRSZ)              51117 (bytes)
 0x000000000000000b (SYMENT)             24 (bytes)
 0x0000000000000015 (DEBUG)              0x0
 0x0000000000000003 (PLTGOT)             0xdcbfe8
 0x0000000000000002 (PLTRELSZ)           8328 (bytes)
 0x0000000000000014 (PLTREL)             RELA
 0x0000000000000017 (JMPREL)             0x426a50
 0x0000000000000007 (RELA)               0x426978
 0x0000000000000008 (RELASZ)             216 (bytes)
 0x0000000000000009 (RELAENT)            24 (bytes)
 0x000000006ffffffe (VERNEED)            0x426858
 0x000000006fffffff (VERNEEDNUM)         6
 0x000000006ffffff0 (VERSYM)             0x4253e6
 0x0000000000000000 (NULL)               0x0

```

-------------------------

tvault | 2020-08-02 21:10:14 UTC | #4

I've been using Urho3D on Raspberry Pi 4 for awhile now using Raspbian Buster, works great, but I've only tried basic example code due to time constraints etc... Most of the samples work great. 

Some things don't work such as shadows and I do get segmentation faults when trying the Ninja Demo but that's not such a big deal at the moment, apart from those minor issues there is no reason why you can't create something.

I can't quite remember everything I did but I didn't change anything, followed the build tutorials using the Native build process.

[EDIT]

I tried again, the build now works, but I had to comment out line 43, 44, 45 of Urho3D/Source/ThirdParty/SDL/src/video/SDL_video.c due to a conflict.

I did not have to use any build scripts, I created a build folder and used cmake within the build folder followed by make and all seems to have built successfully.

-------------------------

tvault | 2020-08-02 11:46:07 UTC | #5

I managed to get an emscripten build working too using emscripten-fastcomp all built natively. 

Urho3D is pretty capable it seems and I think it could possibly be the 'go to' engine for Raspberry Pi.

-------------------------

tvault | 2020-08-02 17:25:36 UTC | #6

There is something I forgot to mention, looking at my simple project, when using CodeBlocks, I link libUrho3D.a with -lGLESv2

-------------------------

weitjong | 2020-08-05 03:54:40 UTC | #7

Just placed an order for RPI4 8GB model B from a local store. I am looking forward to test the 64-bit build myself this weekend when the delivery is on time. I hope I will be able to lift the bone limit that I set for original RPI port many years ago.

EDIT: I have to put this on back burner. My local store just informed me they run out of stock.

-------------------------

urnenfeld | 2020-08-03 10:50:49 UTC | #8

Hello,
For the ones challenging this,
I would recommend taking a look at patches 002, 005 & 006 in:

https://github.com/urnenfeld/meta-urho3D/tree/thud/recipes-urhobox/urho3D/files/rpi

My understanding is that newer RPi ecosystems already have the GPU support integrated in in Linux in a more standard way. Therefore no need to link to specific libraries.

I could not test it though with the RPi4-64...

-------------------------

weitjong | 2020-08-03 11:49:18 UTC | #9

I made it to not depend on X11 intentionally. Urho3D runs on RPI directly without X.

-------------------------

