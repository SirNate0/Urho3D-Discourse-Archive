JimSEOW | 2017-05-20 16:50:32 UTC | #1

Microsoft will release Windows 10 on Arm. Is there a roadmap to support Urho3D to run native in 64bit Windows 10 on Arm?

It seems the limitations are [AngleScript](https://discourse.urho3d.io/t/angelscript-and-windows-phone/2203/4)

-------------------------

Enhex | 2017-05-20 19:05:33 UTC | #2

AngelScript can be disabled via CMake options I think (or was it only Lua?).
doing so solves the problem?

-------------------------

weitjong | 2017-05-21 00:52:56 UTC | #3

AngelScript can be opt out in the similar way as Lua or LuaJIT. As for the OP's question. Currently we don't have such plan, we don't even have a roadmap. :slight_smile: But if your question is, will we accept the contribution that will enable the support for ARM on Windows, then the answer is yes. I do see it won't be easy though because so far our build scrips has assumed MSVC does not support cross-compiling and this compiler does not behave anything like GCC or Clang.

-------------------------

S.L.C | 2017-05-21 01:11:27 UTC | #4

Since Urho3D 1.7 might include c++11 support. It shouldn't be too hard to create some wrappers and use the generic function calling. If that's what you mean.

-------------------------

JimSEOW | 2017-05-21 04:11:31 UTC | #5

We are UrhoSharp developers interested to bring Urho3D to Windows 10 mobile running on e.g. Snapdragon 820 ARM. Snapdragon 835 will appear in increasingly more mixed reality wearables. E.g. ODG glass. It would be of interest to Urho3D communities to support Snapdragon ARM. With Urho.dll for this ARM, Xamarin could starts to bring Urho3D .Net binding to more mobile devices and wearables.

FYI: Windows 10 on ARM have been tested and demo to run on Snapdragon 820 and 835. 

Windows 10 Mobile like 950XL run on 820.

It will be great that Urho3D 1.7 starts supporting urho.dll for Snapdragon ARM.

-------------------------

weitjong | 2017-05-21 05:19:06 UTC | #6

Our build system has been tested to target generic ARM, but it is for Linux platform. To me, it would be really easy to switch to a GCC/Clang compiler toolchain that could target Snapdragon and build Urho3D with it. It is the "Windows" part that I have some doubts, perhaps it is because I am not familiar with it. But like I said before, if someone else can contribute first and show us how to do it then I am very sure the contribution will be accepted (provided it does not break the other platforms of course).

-------------------------

JimSEOW | 2017-05-21 09:22:49 UTC | #7

Visual Studio support Cross Compilation
e..g Compile VC++ library for Window Phone/Window Store (ARM)
[
Migration issues](https://msdn.microsoft.com/en-us/library/jj635841.aspx)

CMake support this configuration
https://cmake.org/cmake/help/v3.8/generator/Visual%20Studio%2014%202015.html

How to[ compile](https://github.com/urho3d/Urho3D/wiki/Setting%20up%20Urho3D%20on%20Windows%20with%20Visual%20Studio) Urho3D with Visual C++

=> Ideally, one disable AngelScript in CMake (which as discussed last year, is the bottleneck for failure to compile Urho3D for ARM using VC++

=> additionally use CMake to configure for Visual Studio ARM platform

=> Currently, I think the feedback is that it is not trivial (without sufficient knowledge in Urho3D to uncouple AngelScript from Urho3D) <===============

-------------------------

SirNate0 | 2017-05-21 20:06:32 UTC | #8

Disabling AngelScript is just seeing a CMake flag to 0 when building the library. I don't know what the problems with AngelScript are with Windows+Arm, so getting AngelScript working may or may not be trivial, but just removing it from the build is simple.

-------------------------

weitjong | 2017-05-22 02:04:58 UTC | #9

AS bindings are either implemented using native calling convention or generic calling convention whenever AS library hasn't natively supported the platform yet, e.g Arm64. Generic call is naturally slower than native one. In the past Urho3D only knew how to use native calling convention but that changes a few months ago (or was it last year already) when we had a contribution that makes the generic calling convention possible. Thus, whatever points made in the old discussions superseded by the above development may not be valid anymore now.

-------------------------

JimSEOW | 2017-06-01 23:18:26 UTC | #10

[More OEM](https://www.theverge.com/2017/5/31/15711334/microsoft-windows-10-arm-qualcomm-pcs-asus-hp-lenovo) will support Windows 10 on ARM on schedule Q4 2017

@weitjong Not exactly understand your arguments and feedback. 

It will be great if some how Urho3D will eventually work NATIVE for Win10 ARM AND Xamarin will start binding it for W10M..

-------------------------

weitjong | 2017-06-02 00:54:50 UTC | #11

Sorry if I didn't make myself clear. English is my third language. Basically I just want to say, anyone who want to contribute to make this happens is welcome but be warned that it is not easy due to the existing (wrong) assumptions made in the build scripts about Windows/VS.

-------------------------

JimSEOW | 2017-07-07 07:44:17 UTC | #12

The big picture, MS mixed reality vision and Apple ARkit means big demand for 3D frame work like Urho3D.

Big demand is expected soon to be able to build using VS2017 for Win64 and Win Arm

Please list the wrong assumptions. What can be done now. A few weeks later, a few months later, until once and for all, we remove these wrong assumptions

-------------------------

weitjong | 2017-07-07 05:51:46 UTC | #13

Well, if you think you could request for something for free with the way you wrote it now, good luck with that. Personally I am not interested in this anymore and will not respond in this thread further.

-------------------------

JimSEOW | 2017-07-07 07:49:31 UTC | #14

[This may be of interest to the discussion](https://channel9.msdn.com/coding4fun/kinect/UrhoSharp-HoloLens)

-------------------------

