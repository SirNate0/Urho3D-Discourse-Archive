talos | 2021-02-11 23:25:27 UTC | #1

Hello everyone,

Building Urho3D on Debian works, but on my Arch machine I get the following error "*multiple definition of `WAYLAND_wl_proxy_get_user_data'*" during the stage of  "*Linking CXX executable ../../../bin/Urho3DPlayer*". 

More logs:

    make[2]: *** [Source/Tools/Urho3DPlayer/CMakeFiles/Urho3DPlayer.dir/build.make:104: bin/Urho3DPlayer] Error 1
    make[1]: *** [CMakeFiles/Makefile2:2746: Source/Tools/Urho3DPlayer/CMakeFiles/Urho3DPlayer.dir/all] Error 2
    make: *** [Makefile:171: all] Error 2

Does anyone have an idea of what's the issue?

Many thanks in advance.

-------------------------

S.L.C | 2021-02-11 21:26:13 UTC | #2

Possibly related: https://medium.com/@clentfort/using-esy-sdl2-with-gcc-10-91b4fa0c5aa9
And also: https://github.com/onivim/oni2/issues/1778

Basically, you either add `-fcommon` to your compiler flags or if you need `-fno-common` then `-Wl,--allow-multiple-definition` to your linker. See [link](https://stackoverflow.com/questions/37525922/how-to-handle-gcc-link-optionslike-whole-archive-allow-multiple-definition).

-------------------------

talos | 2021-02-11 23:22:40 UTC | #3

In case anyone else runs across the same problem, issue was solved by adding `add_definitions("-fcommon")` to `CMakeLists.txt`.

-------------------------

Modanung | 2021-02-11 23:22:55 UTC | #4

You may also run into:

https://gitlab.com/luckeyproductions/dry/-/issues/2

-------------------------

Teknologicus | 2021-02-12 05:14:45 UTC | #5

I'm on Manjaro Linux (which is based on Arch Linux) and I disable wayland with cmake to solve this issue for my builds:
`cmake -DVIDEO_WAYLAND=OFF`

-------------------------

Modanung | 2021-02-12 10:15:36 UTC | #6

Issues relating to the topic:
https://gitlab.com/luckeyproductions/dry/-/issues/3
https://github.com/urho3d/Urho3D/issues/2758

-------------------------

