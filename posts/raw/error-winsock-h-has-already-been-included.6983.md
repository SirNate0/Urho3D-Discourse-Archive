nickwebha | 2021-09-05 23:44:35 UTC | #1

I am trying to compile my Urho3D application with Boost ASIO/Beast. MinGW complains:
`#error WinSock.h has already been included`

The Internet suggests the solution is to include the Boost libraries before including `windows.h` but, of course, I am not including `windows.h`, Urho3D is. I have tried including the Boost headers before `Urho3DAll.h` but that does not help.

The Linux build compiles and runs fine.

Any ideas?

-------------------------

nickwebha | 2021-09-08 11:11:35 UTC | #2

I figured it out.

Passing `-D WIN32_LEAN_AND_MEAN` to `g++` bypasses the problem. The second problem that will pop up after you fix the first one is resolved by passing `-Wa,-mbig-obj`.

Re: Second issue. File size of object files too large.

-O0 seems to pass too much information. -O3 (of course for a release build) makes smaller files which also helps alleviate this issue.

-------------------------

weitjong | 2021-09-06 05:04:47 UTC | #3

The build scripts configure the optimization level based on the chosen build config.

-------------------------

nickwebha | 2021-09-07 15:20:10 UTC | #4

`-D WIN32_LEAN_AND_MEAN` was the important part when compiling the application (not Urho3D itself).

I compile my Linux (`g++`) debug build with `-O0` and `-g3` and the Windows (`MinGW`) release with `-O3`. Seems to be working fine now.

I should note I am only using Urho3D's build system (`cmake`) to build Urho3D itself, not my application.

-------------------------

weitjong | 2021-09-07 17:06:14 UTC | #5

Urho3D build system is designed to be reusable by downstream app too. It is of course not mandatory to use it, but if you do then you will get many benefits out of the box. Getting the compiler flags properly configured based on the chosen build config/combo is only one of them. But yeah, I was wrong to assume you are reusing the build system too.

-------------------------

nickwebha | 2021-09-08 11:09:08 UTC | #6

[quote="weitjong, post:5, topic:6983"]
assume you are reusing the build system
[/quote]
I know I should be. I just did not realize it when I first started and now `g++` is working out so well for me.

-------------------------

weitjong | 2021-09-08 12:54:36 UTC | #7

You will appreciate it more when targeting multiple platforms.

-------------------------

