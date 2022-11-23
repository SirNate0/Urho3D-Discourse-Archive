Jillinger | 2017-03-07 00:25:44 UTC | #1

HI
I really enjoyed those samples in Urho, and am looking forward excitingly to dame design with this engine. 
The only thing  is, I want to primarily target android, and this is where I am getting problems.
I built as before, using cmake gui.
I just used the android toolchain.

However, when I build the project in Visual Studio, I get 3 errors, that's after I fixed over 300. The errors are basically **error : ld returned 1 exit status**
<img src="//cdck-file-uploads-global.s3.dualstack.us-west-2.amazonaws.com/standard17/uploads/urho3d/original/1X/f4766bbb8b6c10550fa5e05b286af35609e49e81.jpg" width="690" height="135">


1>------ Build started: Project: tolua++, Configuration: Debug Tegra-Android ------
2>------ Skipped Build: Project: doc, Configuration: Debug Tegra-Android ------
2>Project not selected to build for this solution configuration 
3>------ Build started: Project: 21_AngelScriptIntegration, Configuration: Debug Tegra-Android ------
4>------ Build started: Project: 42_PBRMaterials, Configuration: Debug Tegra-Android ------
3>  ../../../libs/armeabi-v7a/libUrho3D.a(as_callfunc_arm.o): In function `CallSystemFunctionNative(asCContext*, asCScriptFunction*, void*, unsigned long*, void*, unsigned long long&, void*)':
3>  C:\Urho3D-1.6\Source\ThirdParty\AngelScript\source\as_callfunc_arm.cpp(219):  undefined reference to `armFuncR0'
3>  C:\Urho3D-1.6\Source\ThirdParty\AngelScript\source\as_callfunc_arm.cpp(223):  undefined reference to `armFunc'
3>  C:\Urho3D-1.6\Source\ThirdParty\AngelScript\source\as_callfunc_arm.cpp(229):  undefined reference to `armFuncR0'
3>  C:\Urho3D-1.6\Source\ThirdParty\AngelScript\source\as_callfunc_arm.cpp(236):  undefined reference to `armFuncR0R1'
3>  C:\Urho3D-1.6\Source\ThirdParty\AngelScript\source\as_callfunc_arm.cpp(243):  undefined reference to `armFuncR0R1'
3>  C:\Urho3D-1.6\Source\ThirdParty\AngelScript\source\as_callfunc_arm.cpp(250):  undefined reference to `armFuncR0'
3>  C:\Urho3D-1.6\Source\ThirdParty\AngelScript\source\as_callfunc_arm.cpp(259):  undefined reference to `armFuncR0R1'
3>  C:\Urho3D-1.6\Source\ThirdParty\AngelScript\source\as_callfunc_arm.cpp(266):  undefined reference to `armFuncObjLast'
3>  C:\Urho3D-1.6\Source\ThirdParty\AngelScript\source\as_callfunc_arm.cpp(269):  undefined reference to `armFuncR0ObjLast'
4>  ../../../libs/armeabi-v7a/libUrho3D.a(as_callfunc_arm.o): In function `CallSystemFunctionNative(asCContext*, asCScriptFunction*, void*, unsigned long*, void*, unsigned long long&, void*)':
4>  C:\Urho3D-1.6\Source\ThirdParty\AngelScript\source\as_callfunc_arm.cpp(219):  undefined reference to `armFuncR0'
4>  C:\Urho3D-1.6\Source\ThirdParty\AngelScript\source\as_callfunc_arm.cpp(223):  undefined reference to `armFunc'
4>  C:\Urho3D-1.6\Source\ThirdParty\AngelScript\source\as_callfunc_arm.cpp(229):  undefined reference to `armFuncR0'
4>  C:\Urho3D-1.6\Source\ThirdParty\AngelScript\source\as_callfunc_arm.cpp(236):  undefined reference to `armFuncR0R1'
4>  C:\Urho3D-1.6\Source\ThirdParty\AngelScript\source\as_callfunc_arm.cpp(243):  undefined reference to `armFuncR0R1'
4>  C:\Urho3D-1.6\Source\ThirdParty\AngelScript\source\as_callfunc_arm.cpp(250):  undefined reference to `armFuncR0'
4>  C:\Urho3D-1.6\Source\ThirdParty\AngelScript\source\as_callfunc_arm.cpp(259):  undefined reference to `armFuncR0R1'
4>  C:\Urho3D-1.6\Source\ThirdParty\AngelScript\source\as_callfunc_arm.cpp(266):  undefined reference to `armFuncObjLast'
4>  C:\Urho3D-1.6\Source\ThirdParty\AngelScript\source\as_callfunc_arm.cpp(269):  undefined reference to `armFuncR0ObjLast'
**4>collect2.exe : error : ld returned 1 exit status**
**3>collect2.exe : error : ld returned 1 exit status**
5>------ Build started: Project: Urho3DPlayer, Configuration: Debug Tegra-Android ------
5>  ../../../libs/armeabi-v7a/libUrho3D.a(as_callfunc_arm.o): In function `CallSystemFunctionNative(asCContext*, asCScriptFunction*, void*, unsigned long*, void*, unsigned long long&, void*)':
5>  C:\Urho3D-1.6\Source\ThirdParty\AngelScript\source\as_callfunc_arm.cpp(219):  undefined reference to `armFuncR0'
5>  C:\Urho3D-1.6\Source\ThirdParty\AngelScript\source\as_callfunc_arm.cpp(223):  undefined reference to `armFunc'
5>  C:\Urho3D-1.6\Source\ThirdParty\AngelScript\source\as_callfunc_arm.cpp(229):  undefined reference to `armFuncR0'
5>  C:\Urho3D-1.6\Source\ThirdParty\AngelScript\source\as_callfunc_arm.cpp(236):  undefined reference to `armFuncR0R1'
5>  C:\Urho3D-1.6\Source\ThirdParty\AngelScript\source\as_callfunc_arm.cpp(243):  undefined reference to `armFuncR0R1'
5>  C:\Urho3D-1.6\Source\ThirdParty\AngelScript\source\as_callfunc_arm.cpp(250):  undefined reference to `armFuncR0'
5>  C:\Urho3D-1.6\Source\ThirdParty\AngelScript\source\as_callfunc_arm.cpp(259):  undefined reference to `armFuncR0R1'
5>  C:\Urho3D-1.6\Source\ThirdParty\AngelScript\source\as_callfunc_arm.cpp(266):  undefined reference to `armFuncObjLast'
5>  C:\Urho3D-1.6\Source\ThirdParty\AngelScript\source\as_callfunc_arm.cpp(269):  undefined reference to `armFuncR0ObjLast'
**5>collect2.exe : error : ld returned 1 exit status**
6>------ Skipped Build: Project: PACKAGE, Configuration: Debug Tegra-Android ------
6>Project not selected to build for this solution configuration 
7>------ Skipped Build: Project: INSTALL, Configuration: Debug Tegra-Android ------
7>Project not selected to build for this solution configuration 
========== Build: 1 succeeded, 3 failed, 65 up-to-date, 3 skipped ==========

I did a google search, and found it a very common error, but this answer seems to be the one that's clearer, and I can better understand.
[https://forum.qt.io/topic/35492/collect2-exe-1-error-error-ld-returned-1-exit-status-solved/2](https://forum.qt.io/topic/35492/collect2-exe-1-error-error-ld-returned-1-exit-status-solved/2)

So I changed the directory to not have any spaces, using the 8.3 names.
C:\PROGRA~2\MICROS~1.0\VC\bin;$(AdditionalGdbDirectories)
However, all that did was produce over 100 warnings, but the 3 errors remain.

Does someone have any ideas how I can fix these errors.
I'm eager to get past this and start a project.
Thanks.

-------------------------

weitjong | 2017-03-07 01:28:18 UTC | #2

At the moment our build system only support cross-compiling using certain compiler toolchains. Cross-compiling using VS is not yet supported though.

-------------------------

Jillinger | 2017-03-07 00:42:56 UTC | #3

Thanks.
So the error is due to the fact I used VS?
Which compiler can I use, and what IDE works well with android?

-------------------------

weitjong | 2017-03-07 01:40:06 UTC | #4

Yes. It is not because VS doesn't support cross-compiling but more because our build system currently can't with VS (msbuild to be more precise). Contribution is welcome if anyone can make it works.

As for your question. Any IDE that can open/load a Makefile-based project build tree will do the work just fine. The compiler for Android platform is anyway provided by Android NDK regardless of which IDE you choose.

-------------------------

Jillinger | 2017-03-07 02:51:38 UTC | #5

I understand, for the most part, I guess.
I'm not ready to give up yet though. Three errors which really boils down to one, isn't so bad, right? :wink:
I found this article - https://msdn.microsoft.com/en-us/library/txcwa2xx.aspx
Maybe it can help me. Then I 'll give myself a day to see if I can beat that error.

Can't hurt to try.
Thanks.

-------------------------

Jillinger | 2017-05-28 11:39:00 UTC | #6

Looks like I may have found a better solution - A guide using my my other favorite IDE.
https://discourse.urho3d.io/t/deploying-urho3d-to-android-studio-in-windows/1107
Now I can go sleep easy. :smiley::sleeping:

-------------------------

