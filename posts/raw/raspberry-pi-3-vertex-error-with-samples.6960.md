PerfectSlayer | 2021-08-09 19:50:48 UTC | #1

Hello,

I am quite new to the project and I try to compile and run the sample on my raspberry pi 3.

I successfully compiled the engine and the sample using the dockerized build environment (DBE) using `RPI_ABI=RPI3 script/dockerized.sh rpi rake build install` then scp the build to my pi.

But when I try to run a sample, I always get a shader related error. Here is the error I get from running 01_HelloWorld:
```
ERROR: Failed to link vertex shader Basic(DIFFMAP VERTEXCOLOR) and pixel shader Basic(DIFFMAP VERTEXCOLOR):
error: too many vertex shader inputs (max 8)
ERROR: Failed to link vertex shader Basic(DIFFMAP VERTEXCOLOR) and pixel shader Basic(ALPHAMAP VERTEXCOLOR):
error: too many vertex shader inputs (max 8)
```

I wonder:
- If the raspberry pi is able to run the samples. It should be able to run them as I saw posts of people that make them work,
- If there is something wrong with my build or my pi OS. 

I am using the Raspberry PI OS 64 bits beta ([source here](https://www.raspberrypi.org/forums/viewtopic.php?t=275370)) that has some issues with graphics libraries (check the first port for all details). I choose to use this beta because the build from DBE was using armv8 architecture (64 bits) where the default raspbian os is using armv7 (32 bits).

If you have any recommended OS for the Raspberry PI 3 to make the engine work or if you know how to build the project for the PI 3 using armv7, please let me know.

Thanks for your help
Regards

-------------------------

weitjong | 2021-08-10 17:07:40 UTC | #2

I guess it is my fault. There is a missing information in the DBE Quick Start online documentation. It is unfortunate that I was forced to leave the project (at least for a short while) before documenting all critical information why they were still fresh in my mind at the time. Anyway, your issue has brought a fragment of  my memory back :slight_smile: and I will amend the documentation soon.

With the exception of Web DBE image, all the other DBE images actually support both 32-bit and 64-bit (default) compiler toolchains. You would have to set the `ARCH=32` environment variable when running DBE in order to switch to the alternate compiler toolchain. Thus, for the RPI platform the command should actually read:

```
ARCH=32 script/dockerized.sh rpi rake build install
```

About the OGL error, I am not sure it was caused by the 64-bit Raspbian OS, which is still in beta, or caused by the new Mesa driver. I hope it was the former. The old posts you saw in the forum were most probably taken on RPI3 or older running on the "legacy" but proprietary VideoCore driver.

Personally, I have not tested the RPI build on the actual 64-bit Raspian OS nor on the 32-bit Raspbian with new Mesa driver yet. I am looking forward for your experiment result though.

-------------------------

PerfectSlayer | 2021-08-10 19:44:48 UTC | #3

Thanks for the heads up and the documentation udpate!

I found it few hours later when I start reading the source code of the DBE... I saw [the following lines](https://github.com/weitjong/dockerized/blob/9d0a513690bb20170e525ee176e663f4083d0f0e/urho3d/rpi/sysroot/rpi_entrypoint.sh#L25) and try it. The build binaries are well for armv7. Thanks!

---

*Quick question:* does it mean DBE only supports RPI 3 and 4 only? (no more 1 or 2, but I guess I can still build them myself using CMake)

---

So I tested the build using DBE and ARCH=32 parameter but it does not seem to start neither... I always got the following message:
```
Bus error
```
Then the sample stops with error code 135.


<s>I checked at the source code and it seems to be related to `Tracy`, the engine profiler: [related source](https://github.com/urho3d/Urho3D/blob/9f968f3d24a97ee0619e1310522ebb6e89507363/Source/ThirdParty/Tracy/client/TracyProfiler.cpp#L848).</s> It look like the sample is receiving a [SIG_BUS](https://en.wikipedia.org/wiki/Bus_error).

As I just reflash a new raspbian, I increase the video memory to 128mo and even 256mo but I still get the issue. I also tried the three GL Driver options (1. `Legacy-Original non-GL desktop driver`, 2. `GL (Fake KMS)-OpenGL desktop driver with fake KMS` and 3. `GL (Full KMS)-Open GL desktop driver with full KMS`) from `raspi-config` but the samples keep crashing with the same error.

My next step will be to find a way to disable profiling at all and check if sample works. I saw `URHO3D_PROFILING ` from the documentation and `TRACY_ENABLE` from source code. I just need to find a way to use them!

If you have any better idea for the `Bus error`, I am all ears opened! Thanks again

*EDIT:* I checked at the build log and Tracy is not enabled so the error might come from the binary itself. 
I can see from `cat /proc/cpu/alignment` the `User` count increases for each call to the sample... So there should be [a memory alignment issue](https://www.kernel.org/doc/Documentation/arm/mem_alignment).

-------------------------

weitjong | 2021-08-11 15:06:30 UTC | #4

[quote="PerfectSlayer, post:3, topic:6960"]
I found it few hours later when I start reading the source code of the DBE… I saw [the following lines](https://github.com/weitjong/dockerized/blob/9d0a513690bb20170e525ee176e663f4083d0f0e/urho3d/rpi/sysroot/rpi_entrypoint.sh#L25) and try it. The build binaries are well for armv7. Thanks!

*Quick question:* does it mean DBE only supports RPI 3 and 4 only? (no more 1 or 2, but I guess I can still build them myself using CMake)
[/quote]

Last night when I looked at those lines and I also realized that those lines are a mistake. The lines should have left the `RPI_ABI` build option alone. I am in the process of upgrading the DBE images as a whole. I can promise you that the next RPI DBE image will fix that issue. I think my original intention is to set it as the default when it is not yet set.

It has been awhile since I last tried and played on the actual RPI device. I may give it a try later after I have all the DBE images upgraded or when the new RPI DBE image is ready.

If you have looked at my Dockerfile for RPI DBE image then you should see that I actually have to build the cross-compiler toolchain myself. If I recall correctly, I did that because the other prebuilt RPI cross-compiler were too old for me. I use crosstool-ng and the steps are pretty much tried and tested. I had to make a few configuration tweaked though, so there might be a tiny possibility that the SIG_BUS error was caused by bad cross-compiler. Perhaps you can try to build a simple hello world program with it and see if it runs fine or not. I must admit that I didn't done that myself. I had wanted to test it with RPI4 at the time but it was out of stock and my order was delayed. By the time it arrived, I had already moved on to do other thing. :slight_smile:

-------------------------

