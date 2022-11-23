CrazySnail-LLLL | 2021-08-09 13:01:03 UTC | #1

I can compile normally on my Mac OS X. but Fedora34 cannot be compiled.

[ 51%] Building C object Source/ThirdParty/toluapp/src/bin/CMakeFiles/tolua++.dir/tolua.c.o
[ 51%] Building C object Source/ThirdParty/toluapp/src/bin/CMakeFiles/tolua++.dir/generated/toluabind.c.o
[ 51%] Linking C executable ../../../../../bin/tool/tolua++
/usr/bin/ld: ../../../Lua/libLua.a(loslib.c.o): in function `os_tmpname':
loslib.c:(.text+0x22c): 警告：the use of `tmpnam' is dangerous, better use `mkstemp'
[ 51%] Built target tolua++
[ 51%] Generating tolua++ API binding on the fly for Audio
[ 51%] Generating tolua++ API binding on the fly for Core
[ 51%] Generating tolua++ API binding on the fly for Engine
[ 51%] Generating tolua++ API binding on the fly for Graphics
[ 51%] Generating tolua++ API binding on the fly for IK
[ 52%] Generating tolua++ API binding on the fly for IO
[ 52%] Generating tolua++ API binding on the fly for Input
[ 52%] Generating tolua++ API binding on the fly for LuaScript
[ 52%] Generating tolua++ API binding on the fly for Math
[ 52%] Generating tolua++ API binding on the fly for Navigation
[ 52%] Generating tolua++ API binding on the fly for Network
[ 52%] Generating tolua++ API binding on the fly for Physics
[ 52%] Generating tolua++ API binding on the fly for Resource
[ 52%] Generating tolua++ API binding on the fly for Scene
[ 52%] Generating tolua++ API binding on the fly for UI
[ 52%] Generating tolua++ API binding on the fly for Urho2D
make[2]: *** 没有规则可制作目标“/home/liu/Urho3D-1.7.1/Source/Urho3D/Container/Str.h”，由“Source/Urho3D/Precompiled.h.Release.pch.trigger” 需求。 停止。
make[1]: *** [CMakeFiles/Makefile2:2212：Source/Urho3D/CMakeFiles/Urho3D.dir/all] 错误 2
make: *** [Makefile:156：all] 错误 2

-------------------------

CrazySnail-LLLL | 2021-08-09 13:13:45 UTC | #2

At this time my cmake version： cmake version 3.20.5  gcc (GCC) 11.2.1 20210728 (Red Hat 11.2.1-1)  ++ (GCC) 11.2.1 20210728 (Red Hat 11.2.1-1)

-------------------------

weitjong | 2021-08-09 13:28:23 UTC | #3

If you insist on using the old release version then perhaps you should also match it with the GCC and CMake version that were available at the time it was being released. However, just for a long shot, you could try to disable the Precompiled Header for the Urho3D library building by disabling the "URHO3D_PCH" build option.

祝你好运

-------------------------

CrazySnail-LLLL | 2021-08-10 04:53:55 UTC | #4

Thanks!After turning off the URHO3D_PCH option, it can be compiled, but it cannot be linked. I want to know the version requirements of gcc g++ cmake.I use the source code of 1.7.1.

-------------------------

weitjong | 2021-08-10 05:25:03 UTC | #5

You didn’t say what was the linker error. But in any case, you should always remember to nuke the build tree and recreate a new one to test, especially when you have changed the critical build options and/or attempted to install prerequisites dependency development packages as you go the first time round. The CMake cache is a double-edged sword.

-------------------------

CrazySnail-LLLL | 2021-08-10 11:53:03 UTC | #6

This is my error log.

[ 78%] Linking CXX static library ../../lib/libUrho3D.a
Merging all archives into a single static library using ar
[ 78%] Built target Urho3D
[ 78%] Building CXX object Source/Tools/Urho3DPlayer/CMakeFiles/Urho3DPlayer.dir/Urho3DPlayer.cpp.o
[ 78%] Linking CXX executable ../../../bin/Urho3DPlayer
/usr/bin/ld: ../../../lib/libUrho3D.a(SDL_waylandopengles.c.o):(.bss+0x0): multiple definition of `WAYLAND_wl_proxy_get_user_data'; ../../../lib/libUrho3D.a(SDL_waylandvideo.c.o):(.bss+0x0): first defined here
/usr/bin/ld: ../../../lib/libUrho3D.a(SDL_waylandopengles.c.o):(.bss+0x8): multiple definition of `WAYLAND_wl_proxy_set_user_data'; ../../../lib/libUrho3D.a(SDL_waylandvideo.c.o):(.bss+0x8): first defined here
/usr/bin/ld: ../../../lib/libUrho3D.a(SDL_waylandopengles.c.o):(.bss+0x10): multiple definition of `WAYLAND_wl_proxy_add_listener'; ../../../lib/libUrho3D.a(SDL_waylandvideo.c.o):(.bss+0x10): first defined here
/usr/bin/ld: ../../../lib/libUrho3D.a(SDL_waylandopengles.c.o):(.bss+0x18): multiple definition of `WAYLAND_wl_proxy_destroy'; ../../../lib/libUrho3D.a(SDL_waylandvideo.c.o):(.bss+0x18): first defined here
/usr/bin/ld: ../../../lib/libUrho3D.a(SDL_waylandopengles.c.o):(.bss+0x20): multiple definition of `WAYLAND_wl_proxy_marshal_constructor_versioned'; ../../../lib/libUrho3D.a(SDL_waylandvideo.c.o):(.bss+0x20): first defined here
/usr/bin/ld: ../../../lib/libUrho3D.a(SDL_waylandopengles.c.o):(.bss+0x28): multiple definition of `WAYLAND_wl_proxy_marshal_constructor'; ../../../lib/libUrho3D.a(SDL_waylandvideo.c.o):(.bss+0x28): first defined here
/usr/bin/ld: ../../../lib/libUrho3D.a(SDL_waylandopengles.c.o):(.bss+0x30): multiple definition of `WAYLAND_wl_proxy_create'; ../../../lib/libUrho3D.a(SDL_waylandvideo.c.o):(.bss+0x30): first defined here
/usr/bin/ld: ../../../lib/libUrho3D.a(SDL_waylandopengles.c.o):(.bss+0x38): multiple definition of `WAYLAND_wl_proxy_marshal'; ../../../lib/libUrho3D.a(SDL_waylandvideo.c.o):(.bss+0x38): first defined here
/usr/bin/ld: ../../../lib/libUrho3D.a(SDL_waylandmouse.c.o):(.bss+0x38): multiple definition of `WAYLAND_wl_proxy_marshal'; ../../../lib/libUrho3D.a(SDL_waylandvideo.c.o):(.bss+0x38): first defined here
/usr/bin/ld: ../../../lib/libUrho3D.a(SDL_waylandmouse.c.o):(.bss+0x18): multiple definition of `WAYLAND_wl_proxy_destroy'; ../../../lib/libUrho3D.a(SDL_waylandvideo.c.o):(.bss+0x18): first defined here
/usr/bin/ld: ../../../lib/libUrho3D.a(SDL_waylandmouse.c.o):(.bss+0x28): multiple definition of `WAYLAND_wl_proxy_marshal_constructor'; ../../../lib/libUrho3D.a(SDL_waylandvideo.c.o):(.bss+0x28): first defined here
/usr/bin/ld: ../../../lib/libUrho3D.a(SDL_waylandmouse.c.o):(.bss+0x8): multiple definition of `WAYLAND_wl_proxy_set_user_data'; ../../../lib/libUrho3D.a(SDL_waylandvideo.c.o):(.bss+0x8): first defined here
/usr/bin/ld: ../../../lib/libUrho3D.a(SDL_waylandmouse.c.o):(.bss+0x10): multiple definition of `WAYLAND_wl_proxy_add_listener'; ../../../lib/libUrho3D.a(SDL_waylandvideo.c.o):(.bss+0x10): first defined here
/usr/bin/ld: ../../../lib/libUrho3D.a(SDL_waylandmouse.c.o):(.bss+0x0): multiple definition of `WAYLAND_wl_proxy_get_user_data'; ../../../lib/libUrho3D.a(SDL_waylandvideo.c.o):(.bss+0x0): first defined here
/usr/bin/ld: ../../../lib/libUrho3D.a(SDL_waylandmouse.c.o):(.bss+0x20): multiple definition of `WAYLAND_wl_proxy_marshal_constructor_versioned'; ../../../lib/libUrho3D.a(SDL_waylandvideo.c.o):(.bss+0x20): first defined here
/usr/bin/ld: ../../../lib/libUrho3D.a(SDL_waylandmouse.c.o):(.bss+0x30): multiple definition of `WAYLAND_wl_proxy_create'; ../../../lib/libUrho3D.a(SDL_waylandvideo.c.o):(.bss+0x30): first defined here
/usr/bin/ld: ../../../lib/libUrho3D.a(SDL_waylandevents.c.o):(.bss+0x18): multiple definition of `WAYLAND_wl_proxy_destroy'; ../../../lib/libUrho3D.a(SDL_waylandvideo.c.o):(.bss+0x18): first defined here
/usr/bin/ld: ../../../lib/libUrho3D.a(SDL_waylandevents.c.o):(.bss+0x28): multiple definition of `WAYLAND_wl_proxy_marshal_constructor'; ../../../lib/libUrho3D.a(SDL_waylandvideo.c.o):(.bss+0x28): first defined here
/usr/bin/ld: ../../../lib/libUrho3D.a(SDL_waylandevents.c.o):(.bss+0x8): multiple definition of `WAYLAND_wl_proxy_set_user_data'; ../../../lib/libUrho3D.a(SDL_waylandvideo.c.o):(.bss+0x8): first defined here
/usr/bin/ld: ../../../lib/libUrho3D.a(SDL_waylandevents.c.o):(.bss+0x10): multiple definition of `WAYLAND_wl_proxy_add_listener'; ../../../lib/libUrho3D.a(SDL_waylandvideo.c.o):(.bss+0x10): first defined here
/usr/bin/ld: ../../../lib/libUrho3D.a(SDL_waylandevents.c.o):(.bss+0x0): multiple definition of `WAYLAND_wl_proxy_get_user_data'; ../../../lib/libUrho3D.a(SDL_waylandvideo.c.o):(.bss+0x0): first defined here
/usr/bin/ld: ../../../lib/libUrho3D.a(SDL_waylandevents.c.o):(.bss+0x38): multiple definition of `WAYLAND_wl_proxy_marshal'; ../../../lib/libUrho3D.a(SDL_waylandvideo.c.o):(.bss+0x38): first defined here
/usr/bin/ld: ../../../lib/libUrho3D.a(SDL_waylandevents.c.o):(.bss+0x20): multiple definition of `WAYLAND_wl_proxy_marshal_constructor_versioned'; ../../../lib/libUrho3D.a(SDL_waylandvideo.c.o):(.bss+0x20): first defined here
/usr/bin/ld: ../../../lib/libUrho3D.a(SDL_waylandevents.c.o):(.bss+0x30): multiple definition of `WAYLAND_wl_proxy_create'; ../../../lib/libUrho3D.a(SDL_waylandvideo.c.o):(.bss+0x30): first defined here
/usr/bin/ld: ../../../lib/libUrho3D.a(SDL_waylanddyn.c.o):(.bss+0x208): multiple definition of `WAYLAND_wl_proxy_marshal'; ../../../lib/libUrho3D.a(SDL_waylandvideo.c.o):(.bss+0x38): first defined here
/usr/bin/ld: ../../../lib/libUrho3D.a(SDL_waylanddyn.c.o):(.bss+0x200): multiple definition of `WAYLAND_wl_proxy_create'; ../../../lib/libUrho3D.a(SDL_waylandvideo.c.o):(.bss+0x30): first defined here
/usr/bin/ld: ../../../lib/libUrho3D.a(SDL_waylanddyn.c.o):(.bss+0x1e8): multiple definition of `WAYLAND_wl_proxy_destroy'; ../../../lib/libUrho3D.a(SDL_waylandvideo.c.o):(.bss+0x18): first defined here
/usr/bin/ld: ../../../lib/libUrho3D.a(SDL_waylanddyn.c.o):(.bss+0x1e0): multiple definition of `WAYLAND_wl_proxy_add_listener'; ../../../lib/libUrho3D.a(SDL_waylandvideo.c.o):(.bss+0x10): first defined here
/usr/bin/ld: ../../../lib/libUrho3D.a(SDL_waylanddyn.c.o):(.bss+0x1d8): multiple definition of `WAYLAND_wl_proxy_set_user_data'; ../../../lib/libUrho3D.a(SDL_waylandvideo.c.o):(.bss+0x8): first defined here
/usr/bin/ld: ../../../lib/libUrho3D.a(SDL_waylanddyn.c.o):(.bss+0x1d0): multiple definition of `WAYLAND_wl_proxy_get_user_data'; ../../../lib/libUrho3D.a(SDL_waylandvideo.c.o):(.bss+0x0): first defined here
/usr/bin/ld: ../../../lib/libUrho3D.a(SDL_waylanddyn.c.o):(.bss+0x1f8): multiple definition of `WAYLAND_wl_proxy_marshal_constructor'; ../../../lib/libUrho3D.a(SDL_waylandvideo.c.o):(.bss+0x28): first defined here
/usr/bin/ld: ../../../lib/libUrho3D.a(SDL_waylanddyn.c.o):(.bss+0x1f0): multiple definition of `WAYLAND_wl_proxy_marshal_constructor_versioned'; ../../../lib/libUrho3D.a(SDL_waylandvideo.c.o):(.bss+0x20): first defined here
/usr/bin/ld: ../../../lib/libUrho3D.a(SDL_waylandwindow.c.o):(.bss+0x38): multiple definition of `WAYLAND_wl_proxy_marshal'; ../../../lib/libUrho3D.a(SDL_waylandvideo.c.o):(.bss+0x38): first defined here
/usr/bin/ld: ../../../lib/libUrho3D.a(SDL_waylandwindow.c.o):(.bss+0x28): multiple definition of `WAYLAND_wl_proxy_marshal_constructor'; ../../../lib/libUrho3D.a(SDL_waylandvideo.c.o):(.bss+0x28): first defined here
/usr/bin/ld: ../../../lib/libUrho3D.a(SDL_waylandwindow.c.o):(.bss+0x18): multiple definition of `WAYLAND_wl_proxy_destroy'; ../../../lib/libUrho3D.a(SDL_waylandvideo.c.o):(.bss+0x18): first defined here
/usr/bin/ld: ../../../lib/libUrho3D.a(SDL_waylandwindow.c.o):(.bss+0x8): multiple definition of `WAYLAND_wl_proxy_set_user_data'; ../../../lib/libUrho3D.a(SDL_waylandvideo.c.o):(.bss+0x8): first defined here
/usr/bin/ld: ../../../lib/libUrho3D.a(SDL_waylandwindow.c.o):(.bss+0x10): multiple definition of `WAYLAND_wl_proxy_add_listener'; ../../../lib/libUrho3D.a(SDL_waylandvideo.c.o):(.bss+0x10): first defined here
/usr/bin/ld: ../../../lib/libUrho3D.a(SDL_waylandwindow.c.o):(.bss+0x0): multiple definition of `WAYLAND_wl_proxy_get_user_data'; ../../../lib/libUrho3D.a(SDL_waylandvideo.c.o):(.bss+0x0): first defined here
/usr/bin/ld: ../../../lib/libUrho3D.a(SDL_waylandwindow.c.o):(.bss+0x20): multiple definition of `WAYLAND_wl_proxy_marshal_constructor_versioned'; ../../../lib/libUrho3D.a(SDL_waylandvideo.c.o):(.bss+0x20): first defined here
/usr/bin/ld: ../../../lib/libUrho3D.a(SDL_waylandwindow.c.o):(.bss+0x30): multiple definition of `WAYLAND_wl_proxy_create'; ../../../lib/libUrho3D.a(SDL_waylandvideo.c.o):(.bss+0x30): first defined here
/usr/bin/ld: ../../../lib/libUrho3D.a(loslib.c.o): in function `os_tmpname':
loslib.c:(.text+0x22c): 警告：the use of `tmpnam' is dangerous, better use `mkstemp'
collect2: 错误：ld 返回 1
gmake[2]: *** [Source/Tools/Urho3DPlayer/CMakeFiles/Urho3DPlayer.dir/build.make:98：bin/Urho3DPlayer] 错误 1
gmake[1]: *** [CMakeFiles/Makefile2:2266：Source/Tools/Urho3DPlayer/CMakeFiles/Urho3DPlayer.dir/all] 错误 2
gmake: *** [Makefile:156：all] 错误 2

-------------------------

weitjong | 2021-08-10 12:13:16 UTC | #7

That’s the GCC 10 (and above) problem. It didn’t exist in the past. Since version 10 GCC has defaulted to “-fno-common”. In its release notes, it states it is the right thing to do even though knowingly the change will break some legacy code. To cut the story short, you need this patch from the main branch. 

https://github.com/urho3d/Urho3D/commit/884c09447dd5068e79f86f81e09a06b2f47aa946

-------------------------

CrazySnail-LLLL | 2021-08-10 15:15:53 UTC | #8

I used the patch, but the link still failed. This is the error log.

[ 54%] Built target tolua++
[ 54%] Linking CXX static library ../../lib/libUrho3D.a
Merging all archives into a single static library using ar
下载Syntax error in archive script, line 1
下载/usr/bin/ar: /home/liu/: file format not recognized
gmake[2]: *** [Source/Urho3D/CMakeFiles/Urho3D.dir/build.make:5118：lib/libUrho3D.a] 错误 1
gmake[1]: *** [CMakeFiles/Makefile2:2382：Source/Urho3D/CMakeFiles/Urho3D.dir/all] 错误 2
gmake: *** [Makefile:156：all] 错误 2

-------------------------

weitjong | 2021-08-10 15:42:42 UTC | #9

Now this one is totally not expected. I have not encountered this before. Some how your build tree has generated a broken "script.ar" file. Search for that file and inspect its content. Try to invoke "ar" command with it. Do you have a space in your path or something? Or a path with Chinese character?

-------------------------

CrazySnail-LLLL | 2021-08-10 16:18:30 UTC | #10

Cool! I run it successfully.



The problem is that my path has Chinese characters in it.



Thanks for you. I can use it to make my first game. :grinning_face_with_smiling_eyes:

-------------------------

weitjong | 2021-08-10 16:22:23 UTC | #11

Glad to hear that. You should really use the main branch if you just start to make your game. There is no point to stick to the old release.

-------------------------

nickwebha | 2021-08-11 15:14:47 UTC | #12

Saw this page, reminded me of this thread.

[New version](https://www.gamingonlinux.com/2021/08/sdl-version-2016-is-out-now-with-much-improved-wayland-support) of SDL2 released with "much improved Wayland support".

-------------------------

weitjong | 2021-08-11 15:27:13 UTC | #13

Yes, that's the main reason why I am upgrading the Linux DBE with libdecor and Pipewire deps installed.

-------------------------

