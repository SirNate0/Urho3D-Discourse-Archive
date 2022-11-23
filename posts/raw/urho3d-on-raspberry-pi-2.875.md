boberfly | 2017-01-02 01:03:42 UTC | #1

Hi all,

I'd just like to say thanks weitjong for the excellent build system, I only got my Raspberry Pi 2 last night and got Urho3D to cross-compile on my laptop within the hour with Arch Linux! No X11 needed!

What I did was get the cross-compiler that Arch uses for armv7 (not armv6) and for the system root I literally just mounted the Pi2's sysroot using sshfs which I found much easier than replicating one on the host machine.

So far I just needed to bump the GPU memory to 256MB and 1920x1200 res works but I brought it down to 720x480 for extra FPS which I needed to do in /boot/config.txt as the -x -y flags didn't do anything. I set multi sample to -m 4 and I didn't notice a huge performance hit at all!

I'm guessing the character demo issue is a known problem where some of the skinning is glitched, presumably because there's only half the uniforms passed down to the shader on the Pi and the skinned character has more than 32 bones. I also noticed shadows didn't render but I didn't investigate this hugely, but render2texture stuff worked fine (it crashed though before I set it to use 256MB).

I thought I'd share my experience if anyone else wants to try it out or need verification that it does indeed work on the Pi2 using armv7, and on a distro that's not raspian or pidora... :slight_smile:

-------------------------

weitjong | 2017-01-02 01:03:42 UTC | #2

[quote="boberfly"]I'm guessing the character demo issue is a known problem where some of the skinning is glitched, presumably because there's only half the uniforms passed down to the shader on the Pi and the skinned character has more than 32 bones.[/quote]
Yes, this is a known issue. As you suspected, the Broadcom OpenGL ES 2.0 driver implementation has limited number of uniforms. If we don't half the number of uniforms that Urho3D normally passes to the shader then the shader program won't compile. 

It is good to know that our build system works on RPI2 too. I don't have RPI2 to play with yet. I believe we can tweak some of the build configuration to better use of the available hardware, using armv-7a instead of armv6 and using the NEON FPU support, etc. I think we should also check whether RPI2 has the same caps as older RPI model, so perhaps we can increase the number of uniforms passed and/or the number of physical/logical CPU cores that can be utilised (it is hardcoded to 1 at the moment for RPI).

-------------------------

boberfly | 2017-01-02 01:03:42 UTC | #3

Hi weitjong

I can do some tests and patches for these. AFAIK the GPU is identical to the Pi1 so I presume the uniform limit is still there but I can quickly check when I get home. I'm building with an 'armv7l hard' toolchain from here: [archlinuxarm.org/developers/dist ... -compiling](http://archlinuxarm.org/developers/distcc-cross-compiling) and the latest Arch armv7 for Pi2 for the sysroot so I'd say that this would be enough to not use armv6 unless there's some hard-coded defines in Urho?

As for the CPU thread limit where abouts is the code for this I'd like to disable it and do some more tests... :slight_smile: The port looks like it really struggles with physics so supporting NEON and threading would help here, but from memory I think bullet is always single-threaded on all platforms right now?

Cheers

-------------------------

weitjong | 2017-01-02 01:03:43 UTC | #4

Sorry for my bad English. I meant to say we could create another build option to specify the target arch for the RPI build, say RPI_ARCH, so we can support both old and new models. The new build option is defaulted to 'armv6' so it works for both Raspberry Pi 1 and 2. But by setting RPI_ARCH=armv7-a then we could tweak the build configuration specifically to target Raspberry Pi 2 better. The CPU core counts function can be found in the Core/ProcessUtils class.

Currently for Raspberry Pi 1 we use these flags: -mcpu=arm1176jzf-s -mfpu=vfp -mfloat-abi=hard.
For Raspberry Pi 2 I think these flags are more appropriate: -mcpu=cortex-a7 -mfpu=neon-vfpv4 -mfloat-abi=hard

-------------------------

cadaver | 2017-01-02 01:03:43 UTC | #5

To get worker threads you need to implement GetNumPhysicalCPUs() in ProcessUtils.cpp for RPI. The physical CPU core count is used for the amount of worker threads. However, as you suspected this will only help render pre-processing and octree tests such as raycasts, not physics.

-------------------------

boberfly | 2017-01-02 01:03:43 UTC | #6

Cheers guys, I've just added a quick & dirty -DRPI2=1 option to CMAKE for the arch/vpu flags which also sets the define for the pre-processor and just makes it 'return 4' so I get 3 worker threads.

Yeah I looked up Bullet's multithreaded capabilities and it's a bit of a mess/mishmash of 'PhysicsEffects' for mobile which has a bunch of neon assembly/intrinsics, some GPU/OpenCL dispatcher which lives in Bullet3 and a retired BulletMultiThreaded from Bullet2, not very fun and straightforward. I'd assume you'd somewhat need to wrap it to Urho3D's worker threads into tasks somehow as well.

I didn't notice a huge impact with NEON/cortex-a7 support but this is just an unscientific observation, however the main thread isn't being taxed as much, there's more of an even spread amongst threads (Arch's top command has a nice graphic for it).

Oh I was able to bump up the skinning uniforms to 38 but it can't get past this. I'm thinking perhaps scale doesn't need to be passed to the RPI to increase bone count which only need translate+quaternions...

-------------------------

weitjong | 2017-01-02 01:03:43 UTC | #7

[quote="boberfly"]Oh I was able to bump up the skinning uniforms to 38 but it can't get past this. I'm thinking perhaps scale doesn't need to be passed to the RPI to increase bone count which only need translate+quaternions...[/quote]
If my memory serves me right, I (we) intentionally did not use up all the uniforms for the skinning because: 1) it is anyway not enough to fix the rendering artifact in character (Jack) demo, 2) 32 is a nice number, and 3) to leave some buffers just in case more uniforms are being declared later for other purposes. It's a pity that the GPU does not get the necessary upgrade in the new model.

-------------------------

weitjong | 2017-01-02 01:03:47 UTC | #8

I took a shot in the dark as I don't have Raspberry Pi 2 to verify my changes. The CPU count should be determined correctly for both RPI 1 and RPI 2 now. It basically uses the same function as the one used by Android platform. Please let me know if it does not or send a PR to fix it directly. :wink:

-------------------------

esak | 2017-01-02 01:04:40 UTC | #9

I'm trying to compile directly on Pi 2 with g++, but discovered that it didn't work at all with g++ 4.6.
So I'm thinking of updating my g++ installation, but the question is what version should/can I pick?

-------------------------

weitjong | 2017-01-02 01:04:40 UTC | #10

I would say, goes for the latest version you can find for your Pi OS.

-------------------------

esak | 2017-01-02 01:04:41 UTC | #11

I updated g++ to version 4.8. Now it works like a charm!  :slight_smile:

-------------------------

zerokol | 2017-01-02 01:06:28 UTC | #12

I was getting trouble to compile inside RaspberryPI too!

For me, worket to upgrade g++ and gcc from 4.6 to 4.8 version:

First of all:

[code]sudo apt-get update
sudo apt-get upgrade[/code]

Install new version:

[code]sudo apt-get install gcc-4.8 g++-4.8[/code]

Remove alterantives:

[code]sudo update-alternatives --remove-all gcc
sudo update-alternatives --remove-all g++[/code]

Install new alternatives

[code]sudo update-alternatives --install /usr/bin/gcc gcc /usr/bin/gcc-4.6 20
sudo update-alternatives --install /usr/bin/gcc gcc /usr/bin/gcc-4.8 50
sudo update-alternatives --install /usr/bin/g++ g++ /usr/bin/g++-4.6 20
sudo update-alternatives --install /usr/bin/g++ g++ /usr/bin/g++-4.8 50[/code]

To test:

[code]sudo gcc --version[/code]

And, if you want to back:

[code]sudo update-alternatives --config gcc
sudo update-alternatives --config g++ [/code]

-------------------------

HeadClot | 2017-01-02 01:07:03 UTC | #13

What distros of the  Raspberry Pi does this work on?

Just curious :slight_smile:

-------------------------

weitjong | 2017-01-02 01:07:04 UTC | #14

The RPI port was developed using Pidora (no pun intended for our Russian readers  :smiley: ) and our RPI CI build is using Raspbian.

-------------------------

