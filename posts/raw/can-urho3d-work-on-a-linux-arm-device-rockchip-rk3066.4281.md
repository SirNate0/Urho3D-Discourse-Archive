molul | 2018-06-04 08:18:56 UTC | #1

Hi! I've been asked to make the UI for a project that will run on a Rockchip RK3066 (ARM processor) with Linux (instead of the default Android).

At first I chose Unity, but it doesn't seem to support Linux+ARM. It does support Android ARM and Linux x86-x64, but not Linux ARM.

I was wondering if Urho3D is compatible with Linux+ARM, in which case I'd be willing to remake the UI with it. The UI is really simple, only 2D sprites and texts and some background music, and I'd need the ability to launch a second app through command line.

Thanks a lot in advance :)

-------------------------

weitjong | 2018-06-04 12:39:06 UTC | #2

Urho supports generic Linux/ARM platform. Whether it supports your particular ARM processor is the question you have to test and answer yourself. In theory our build system can integrate with any GCC/Clang cross-compiler toolchain with little or no changes. You can pass additional compiler flags without making any changes to the build system. Check our ARM CI build setup to get some inspiration from it. The C/C++ source code is already written in a cross-platform way, so that should be the least you need to worry about. Good luck.

-------------------------

