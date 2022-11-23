Sinoid | 2018-09-11 03:48:40 UTC | #1

Here's an MIT'd dump of premake scripts for building significant portions of Urho3D:

https://github.com/JSandusky/Urho3DPremake

Significant changes are made in some regards such as all of Detour, Recast, and DetourCrowd becoming one. The scripts as uploaded are meant to be dropped into the Git root of Urho3D.

Files and folders are likely missing from them as they include in-house things or platform bits that I can't enforce, prune them out and you'll be fine. I'd rather dump it as is than fuss for months about dumping it.

The provided scripts are really just windows scripts, but if  you're familiar with premake you'll know how trite it is to change this.

To deal with Urho3D's CMake-centric header copy stage you have to build symbolic links to those directories.

This isn't for amateurs or hobbyists, these scripts are for hitting the ball to get rolling on consoles ... hell, not fighting with Android-Studio's garbage gradle implementation is relief enough.

-------------------------

green-zone | 2018-09-11 07:49:59 UTC | #2

<img src='//cdck-file-uploads-global.s3.dualstack.us-west-2.amazonaws.com/standard17/uploads/urho3d/original/2X/7/7e57b42da7514dd9857a1c3d49bf87e2719c1579.jpeg' alt="time to let dx9 die in peace"><br>
Ok, but compare it with Linux and others OS (without Windows)

Steam (August 2018):
Windows XP - 32 bit 0.18%
Ubuntu 18.04.1 LTS 64 bit - 0.16%

Statcounter (Jan 2018):
Windows XP - 3.36%
Other (no win) - 0.08%

NetMarketShare (Jan 2018):
Windows XP - 4.05%
Linux - 1.31%

I do not use DirectX (also for Windows), but this step need discussion (imho)

-------------------------

rku | 2018-09-12 09:27:12 UTC | #3

Not a fan of premake but simplicity of these scripts is simply lovely! How does premake deal with crosscompiling? Is it possible to build a part of codebase with native compiler and rest of it with crosscompiler? How about targetting multiple archs/build configs (debug/release) with single build?

-------------------------

Sinoid | 2018-09-14 02:33:31 UTC | #4

@rku, I don't know the answers to those. All my work occurs out of Citrix-VMs that are spun-up on demand so even though premake is life here the reasons I can think of to do such a thing aren't really applicable (outsourcing management firm, VMs for client segregation and for VMs from clients).

Single build depends on the premake target though, VS for instance still can't queue multiple builds without plugins/macros to conceal the GUI interaction. If you meant a mixed solution with x86, x64, and Android as available targets, yes.

Although the scripts are quite clean, I can't really attest to their viability in a multi-user / version-controlled environment as they've really just been my after-hours project (cleared). Git-ignore has been enough so far for just me versioning my own stuff locally, but it might not hold up.

-------------------------

Sinoid | 2018-09-14 02:44:47 UTC | #5

@green-zone, DX9 is just a random opinion on why I neglected it from the build-scripts, tinted with western glasses. I wouldn't be surprised if DX9 is actually a large appeal to Urho3D in locales where XP is still strong.

-------------------------

CaptainCN | 2018-09-17 06:05:47 UTC | #6

How about Xmake(https://github.com/tboox/xmake).

xmake is a cross-platform build utility based on lua.

-------------------------

Sinoid | 2018-09-20 04:22:17 UTC | #7

@CaptainCN, though I've never heard of Xmake before - there's really no comment at all about the Urho3D build system here. It's just a "*here's this thing, you might dig it, you might not, you might just like it's existence as some kind of reference, but it's another way to build*".

Xmake does look a little interesting, but it'd have to trump Premake in how easy it is to add toolchains, platforms, etc for me to really consider such a thing. Premake is pretty *meh* outside of how trivial it is to expand on the generators/toolchains.

-------------------------

