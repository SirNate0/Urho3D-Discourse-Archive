NinjaPangolin | 2019-02-04 12:26:15 UTC | #1

I used MinGW from [Stephan Lavavej's site](https://nuwen.net/mingw.html) to compile Urho3D on Windows 7 and it worked just fine. Now I've updated to Windows 10 and successfully compiled the lib. Used default options (OpenGL renderer) with `cmake_mingw.bat build -DMINGW_SYSROOT=C:\MinGW`. 2D samples works fine, but 3D ones do not. Here's how 13_CharacterDemo.exe looks like:

![Urho3D|645x499](upload://ipkWXZM4qdZnDfV2eN5JGVqyep2.png) 

It's upside-down, model is squashed and moving the mouse causes it to be stretched into infinity. What is going on here?

-------------------------

Leith | 2019-02-04 12:29:26 UTC | #2

Interestingly, the 2D UI stuff is not being affected - did you download the latest code from the master on github, or the older 1.7 stuff from the website? I'm running windows 10 in dual boot, and would be happy to verify and check out what happened.

-------------------------

Eugene | 2019-02-04 12:32:07 UTC | #3

I have seen similar issues when there was compiler bug in VS 2017.
Try DX9/11 just in case, and other compiler too.

-------------------------

Leith | 2019-02-04 12:32:44 UTC | #4

A compiler bug somehow flips matrices? hmmm

-------------------------

NinjaPangolin | 2019-02-04 12:32:54 UTC | #5

I use 1.7 version from the website because I have problems with compiling `ThirdParty/SLikeNet` with MinGW (no safe functions such as `strcpy_s` and `strcat_s` were available).

-------------------------

Leith | 2019-02-04 12:34:19 UTC | #6

I have to suspect SDL is at fault, without having looked closer

-------------------------

Miegamicis | 2019-02-04 12:35:32 UTC | #7

[quote="NinjaPangolin, post:5, topic:4894, full:true"]
I use 1.7 version from the website because I have problems with compiling `ThirdParty/SLikeNet` with MinGW (no safe functions such as `strcpy_s` and `strcat_s` were available).
[/quote]

Could you create issue about this on Github with the Windows version, MinGW version etc. so I can take a look at this?

-------------------------

Eugene | 2019-02-04 12:35:32 UTC | #8

@Leith There was a bug that 16th argument of the function was just ignored. So the matrix got slightly mis-constructed that resulted in weird projection artifacts.

@NinjaPangolin I thought SLikeNet issues were fixed. I highly recommend to use `master` version whenever possible.

-------------------------

Leith | 2019-02-04 12:36:30 UTC | #9

thanks for the heads up, I am not used to seeing 'half' of the render get inverted

-------------------------

S.L.C | 2019-02-04 12:36:33 UTC | #10

Isn't this the good ol GCC 8.x matrix issue? https://github.com/urho3d/Urho3D/issues/2326

-------------------------

Leith | 2019-02-04 12:53:09 UTC | #11

Looks like it, argument limits are annoying and wrong

-------------------------

NinjaPangolin | 2019-02-04 13:15:51 UTC | #12

@Miegamicis, I've created the issue: https://github.com/urho3d/Urho3D/issues/2416

 Tried to build with DirectX (`cmake_mingw.bat build_direct -DMINGW_SYSROOT=C:\MinGW -DURHO3D_D3D11=1`), also with Lavavej's MinGW 16.1, got different error:

> CMake Error at C:/Program Files/CMake/share/cmake-3.13/Modules/FindPackageHandleStandardArgs.cmake:137 (message):
>   Could NOT find DirectX using MinGW default search paths (missing: D3D11)
> Call Stack (most recent call first):
>   C:/Program Files/CMake/share/cmake-3.13/Modules/FindPackageHandleStandardArgs.cmake:378 (_FPHSA_FAILURE_MESSAGE)
>   CMake/Modules/FindDirectX.cmake:239 (find_package_handle_standard_args)
>   CMake/Modules/UrhoCommon.cmake:470 (find_package)
>   CMakeLists.txt:45 (include)
> 
> 
> -- Configuring incomplete, errors occurred!
> See also "C:/GameProject/Urho3D/build_direct/CMakeFiles/CMakeOutput.log".
> See also "C:/GameProject/Urho3D/build_direct/CMakeFiles/CMakeError.log".

Looks like it's related to [this](https://github.com/urho3d/Urho3D/issues/1247).

Currently trying to compile Urho 1.7 with MinGW 16.0 version (GCC 8.1.0 instead of GCC 8.2.0), though if it's really GCC 8.X.X then I guess it won't help. I'll try 7.3 next time.

-------------------------

Leith | 2019-02-04 13:23:07 UTC | #13

Thank you for raising this issue. I tend to fix issues or complain, you took the time. I commend you.

-------------------------

Miegamicis | 2019-02-04 13:27:34 UTC | #14

Thanks, will take a look at this!

-------------------------

NinjaPangolin | 2019-02-04 18:15:50 UTC | #15

Removing `-ffast-math` from ` Urho3D/CMake/Modules/UrhoCommon.cmake` helped.

-------------------------

