rogerdv | 2017-01-02 01:01:09 UTC | #1

I installed Visual Studio Express 2012 and recompiled Urho3d and my project without problems, but when I try to run the project I get an error: missing D3DCOMPILER_46.dll. This project was working well when I tested it using VC++ 2010. How can I solve this?

-------------------------

weitjong | 2017-01-02 01:01:10 UTC | #2

You need to copy the D3DCOMPILER_46.dll to Bin directory. This has been documented in [urho3d.github.io/documentation/H ... ng_Shaders](http://urho3d.github.io/documentation/HEAD/_building.html#Building_Shaders).

-------------------------

glebedev | 2020-06-27 14:20:13 UTC | #3

According to https://docs.microsoft.com/en-us/windows/win32/directx-sdk--august-2009-

> The D3DCOMPILER_46.DLL or D3DCOMPILER_47.DLL from the Windows SDK is not a system component and should not be copied to the Windows system directory. You can redistribute this DLL to other computers with your application as a side-by-side DLL.

So it should be part of a pre-build urho although it is clearly missing from "3D9" bulild in https://sourceforge.net/projects/urho3d/files/Urho3D/1.7.1/

-------------------------

George1 | 2020-06-27 17:36:38 UTC | #4

Why are you still using 1.7.1?

-------------------------

glebedev | 2020-06-27 18:14:44 UTC | #5

Yes. Is it fixed in 1.8?

-------------------------

George1 | 2020-06-28 01:03:01 UTC | #6

I think Git version does not have any missing thing.
Why not using cmake and build static lib.

-------------------------

weitjong | 2020-06-28 05:05:52 UTC | #7

I do not recall our build script ever attempts to copy this DLL on developer behalf. Although I agree it could be made automatic on Windows build environment. PR is welcome.

-------------------------

George1 | 2020-06-28 11:49:06 UTC | #8

On post build in visual studio you can execute batch command.  So it is possible to copy automatically after build.

-------------------------

