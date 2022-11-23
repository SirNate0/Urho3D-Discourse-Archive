spwork | 2020-11-01 04:21:51 UTC | #1

[ 77%] Linking CXX executable ../../../bin/Urho3DPlayer
/usr/bin/ld: ../../../lib/libUrho3D.a(SDL_surface.c.o):(.bss+0x0): multiple definition of `WAYLAND_wl_proxy_get_user_data'; ../../../lib/libUrho3D.a(SDL_video.c.o):(.bss+0x0): first defined here
/usr/bin/ld: ../../../lib/libUrho3D.a(SDL_surface.c.o):(.bss+0x8): multiple definition of `WAYLAND_wl_proxy_set_user_data'; ../../../lib/libUrho3D.a(SDL_video.c.o):(.bss+0x8): first defined here
/usr/bin/ld: ../../../lib/libUrho3D.a(SDL_surface.c.o):(.bss+0x10): multiple definition of `WAYLAND_wl_proxy_add_listener'; ../../../lib/libUrho3D.a(SDL_video.c.o):(.bss+0x10): first defined here
how should i fix it?

-------------------------

SirNate0 | 2020-11-01 05:41:13 UTC | #2

Like like it could be the same as this issue (for a different project) using gcc 10 with SDL. They said they got it working by adding -fcommon to the flags passed to gcc. If you're also using gcc version 10 you might try that.

https://github.com/onivim/oni2/issues/1778

-------------------------

spwork | 2020-11-01 05:11:50 UTC | #3

how can do adding -fcommon to gcc whith cmake :joy:

-------------------------

spwork | 2020-11-01 05:41:03 UTC | #4

built succeed.add CmakeLists.txt
SET(GCC_FCOMMON_COMPILE_FLAGS "-fcommon")

add_definitions(${GCC_FCOMMON_COMPILE_FLAGS})

-------------------------

weitjong | 2020-11-01 16:07:10 UTC | #5

I just upgraded my Fedora to version 33 which comes with GCC 10.2.1. If I can reproduce the issue locally and able to fix it, I may push my fix to the main branch. And, if I can get my NVIDIA proprietary driver to play ball with Wayland this time then I will make Urho3D engine to support Wayland correctly too with the help from SDL. Don't hold your breath as always.

EDIT: well, just one "rake" command on the master branch. Everything went through uneventfully without any change nor sweat. Test run a few samples and they were OK. Still on X11 though.

-------------------------

weitjong | 2021-07-24 08:45:14 UTC | #6

Time flies. Just got my new rig to multi-boot into F34 with beta version of NVIDIA driver that finally works on XWayland. So, it means both X11 apps running on XWayland as well as Wayland-native apps could run with hardware acceleration. Personally I think the time is right to switch to Wayland now, even for those using NVIDIA graphics card like me.

EDIT: forgot to mention that finally I am able to reproduce the issue locally now :)

-------------------------

weitjong | 2021-08-05 16:00:07 UTC | #7

I could not find anything in upstream SDL for the fix yet. So, I have added a quick fix to add the `-fcommon` compiler flag when compiling SDL library. In my test both GCC and Clang compilers need this patch, i.e. it seems both of them default to `-fno-common`.

https://github.com/urho3d/Urho3D/commit/884c09447dd5068e79f86f81e09a06b2f47aa946

-------------------------

