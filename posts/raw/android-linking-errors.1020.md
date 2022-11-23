gulaghad | 2017-01-02 01:04:52 UTC | #1

I can build Urho3D and my project (topdown) on linux without problems. I have followed
[url]http://urho3d.github.io/documentation/HEAD/_using_library.html[/url] and
[url]http://urho3d.github.io/documentation/HEAD/_building.html#Building_Android[/url].

Urho3DPlayer builds fine for android. But when I try to build my project (topdown) I get errors:
[url]http://pastebin.com/hi1cVtrJ[/url]

-------------------------

weitjong | 2017-01-02 01:04:52 UTC | #2

It looks like you have not passed the "-DANDROID=1" when configuring/generating your own Android project file.

-------------------------

gulaghad | 2017-01-02 01:04:52 UTC | #3

[code]./cmake_android.sh android-build[/code]
[pastebin]GjSDgmS8[/pastebin]
I have also tried using cmake_generic.sh with "-DANDROID=1". Result is same.

I am doing something wrong, but I can't seem to find what it is. Maybe setting URHO3D_HOME or I don't know. I am building Urho3D for linux in source. So
[code]
export URHO3D_HOME="/home/can/work/projects/Urho3D"
./cmake_generic.sh .
[/code]
Urho3D for android to android-build. And, while building my project
[code]
export URHO3D_HOME="/home/can/work/projects/Urho3D/android-build"
./cmake_android.sh android-build
[/code]
And getting that paste. What is the proper way of having multiple builds (linux and android)?

-------------------------

weitjong | 2017-01-02 01:04:52 UTC | #4

I think this CMake warning about Policy CMP0054 is harmless. You can try to explicitly set the policy to NEW or OLD to see which one work best for you. If I understand this specific policy correctly from CMake documentation then it should be set to NEW. We do not directly maintain the CMake/Toolchains/android.toolchain.cmake file. It is mainly a copy from [github.com/taka-no-me/android-c ... hain.cmake](https://github.com/taka-no-me/android-cmake/blob/master/android.toolchain.cmake) with some of Urho3D-specific patches. We try to keep the patches as minimal and as localized as possible, so we could merge the changes from upstream easily. All the other CMake files that are fully maintained by us should not trigger this policy warning because we use "quote" sparingly and only when it is absolutely necessary. In short, setting the policy CMP0054 in the main CMakeLists.txt is the right approach for user using CMake 3.1 or higher in order to suppress this warning.

I am still using CMake 3.0.2 on my Linux box (Fedora 21). Although I have latest CMake version installed on my Window and Mac OS X boxes, I only do cross-compile to target Android platform on my Linux box. So, I have never encountered this warning yet. If you can confirm setting the policy explicitly works then let us know and we will make the change in the master branch. Or you can send us a PR instead.

Regarding your last question. You can generate multiple build-trees anywhere you like from a same Urho3D project source tree. As long as you do not mix up the build-tree for each platform then you should be good. Same goes for your own project.

-------------------------

