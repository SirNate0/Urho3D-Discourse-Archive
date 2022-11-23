ChunFengTsin | 2022-06-06 14:43:39 UTC | #1

I want to give notes to you all, 

When you compile the source of urho3d with CLion and LLVM-MINGW under Windows.

You should set the Generator to "MinGW Makefiles", in CMake panel.

NOT DEFAULT Ninja!

-------------------------

ChunFengTsin | 2022-06-06 14:46:13 UTC | #2

and comments out like this:
-fno-keep-inline-dllexport
```
elseif (MINGW)
            # MinGW-specific setup
            set (CMAKE_C_FLAGS "${CMAKE_C_FLAGS} -static -static-libgcc")# -fno-keep-inline-dllexport")
            set (CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -static -static-libgcc")# -static-libstdc++ -fno-keep-inline-dllexport")
type or paste code here
```
# [llvm-mingw 20220323 with LLVM 14.0.0](https://github.com/mstorsjo/llvm-mingw/releases/tag/20220323)

If you use default ninja, will have link error!

-------------------------

Victor | 2022-06-17 13:40:34 UTC | #3

Thanks for the info! I also was having this same issue with CLion and the main Urho3D branch.

-------------------------

