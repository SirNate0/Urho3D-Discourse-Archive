huminzheng | 2022-03-30 13:20:19 UTC | #1

Hi, can anybody tell me how to use -s MAX_WEBGL_VERSION=2 to build urho3d with emcc?
I do as follows ,but  the building process cannot go on.
D:\Aphro3DWeb>Script\cmake_emscripten.bat d:\Aphro3DWeb\build -D URHO3D_TESTING=0 -D EMSCRIPTEN_SHARE_DATA=1 -D URHO3D_PLAYER =0  -s MAX_WEBGL_VERSION =2

-------------------------

SirNate0 | 2022-03-30 13:55:10 UTC | #2

You need to set the -s MAX_WEBGL_VERSION=2 as part of one of the cmake flags. I believe either the C/CXX COMPILER FLAGS or as the LINKER FLAGS, maybe both.

-------------------------

huminzheng | 2022-03-30 14:09:14 UTC | #3

 CXX_FLAGS =  -s MAX_WEBGL_VERSION=2 -std=c++11 -Wno-invalid-offsetof -mno-sse -Wno-warn-absolute-paths -Wno-unknown-warning-option --bind -Qunused-arguments -include "D:/Aphro3DWeb/build/Source/Urho3D/Precompiled.h" -Winvalid-pch -Oz -DNDEBUG -fvisibility=hidden -fvisibility-inlines-hidden
At this place? Thanks a lot!

-------------------------

