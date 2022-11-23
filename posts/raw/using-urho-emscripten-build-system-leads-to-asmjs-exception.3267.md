hcomere | 2017-06-18 10:05:02 UTC | #1

Hi,

I had successfuly compiled and ran my project with emscripten by linking with Urho from my own build system.

Now i am trying to use Urho's build system following below documentation :
https://urho3d.github.io/documentation/1.6/_using_library.html

Got two issues with that :

== 1) My project must be compiled for windows, asmjs and android, so i am using cmake_vs2015.bat cmake_emscripten.bat and cmake_android.bat to compile respectively in folders build_vs2015/ build_asmjs/ and build_android/

The issue is that i have to define URHO3D_HOME with the correct build_xxx/ according to current platform.
I used to use if(EMSCRIPTEN) condition to detect if i am building for asmjs as it is a variable automaticaly setted by emscripten toolchain.

```
if(EMSCRIPTEN)
    set(URHO3D_HOME "C:/Users/hcomere/Perso/Urho3D-1.6/build_asmjs")
elseif(ANDROID)
    set(URHO3D_HOME "C:/Users/hcomere/Perso/Urho3D-1.6/build_android")
elseif(WIN32)
    set(URHO3D_HOME "C:/Users/hcomere/Perso/Urho3D-1.6/build_vs2015")
endif()
```
 
But this does not work, EMSCRIPTEN variable seems to be undefined using Urho scripts.

I had to add the definitions in cmake_generic.bat 

```
    if "%~1" == "-DWEB" if "%~2" == "1" set "OPTS=-G "MinGW Makefiles" -DCMAKE_TOOLCHAIN_FILE="%TOOLCHAINS%\emscripten.toolchain.cmake" -DEMSCRIPTEN=1"
```

What is the usual way to define URHO3D_HOME according to the platform without customizing cmake_generic.bat ?

== 2) 

The second issue is way more strange, the compilation is OK but i am simply not able to run my project due to a javascript error :

```
Uncaught TypeError: Cannot read property 'viewport' of undefined
```

It worked well with my build system and compiled Urho web samples work well ...
It is like the webgl context has not be created but i do not have any error about that.
Any guess? :confused:


Regards,
Harold

-------------------------

weitjong | 2017-07-02 07:18:23 UTC | #2

First of all, if you are happy with your own build system then use it. There is absolutely no need to reuse Urho3D build system for your own project.

With that gets out of the way. If you just setting up a new project now, you may want to try the latest codebase from the master branch instead as the new release 1.7 is imminent. The Emscripten toolchain file (as well all the others) has been renamed. Things that you have observed may or may not exist anymore with the latest codebase.

-------------------------

hcomere | 2017-06-19 19:38:09 UTC | #3

Hi weitjong,

Sure i can continue to use my build system and complete it with android support, but Urho3D's build system is more complete and elegent so if it can fit my needs it should be perfect :)
I just try to understand differences i have between both, mine need SSE disabled where Urho's one do not, but i have js exception at runtime :confused:

As you suggested i have tried Urho's master but i am not able to compile Urho for emscripten due to the following error :
```
[ 22%] Built target LZ4
[ 24%] Building CXX object CMakeFiles/PackageTool.dir/C_/Users/hcomere/Perso/Urho3D/master/Source/Urho3D/Core/ProcessUtils.cpp.obj
C:\Users\hcomere\Perso\Urho3D\master\Source\Urho3D\Core\ProcessUtils.cpp:587:64: warning: '__stdcall__' attribute only applies to function types [-Wattributes]
 typedef NTSTATUS (WINAPI *RtlGetVersionPtr)(PRTL_OSVERSIONINFOW);
                                                                ^
C:\Users\hcomere\Perso\Urho3D\master\Source\Urho3D\Core\ProcessUtils.cpp:587:64: error: typedef 'Urho3D::RtlGetVersionPtr' is initialized (use decltype instead)
C:\Users\hcomere\Perso\Urho3D\master\Source\Urho3D\Core\ProcessUtils.cpp:587:45: error: 'PRTL_OSVERSIONINFOW' was not declared in this scope
 typedef NTSTATUS (WINAPI *RtlGetVersionPtr)(PRTL_OSVERSIONINFOW);
                                             ^
C:\Users\hcomere\Perso\Urho3D\master\Source\Urho3D\Core\ProcessUtils.cpp:589:19: error: variable or field 'GetOS' declared void
 static void GetOS(RTL_OSVERSIONINFOW *r)
                   ^
C:\Users\hcomere\Perso\Urho3D\master\Source\Urho3D\Core\ProcessUtils.cpp:589:19: error: 'RTL_OSVERSIONINFOW' was not declared in this scope
C:\Users\hcomere\Perso\Urho3D\master\Source\Urho3D\Core\ProcessUtils.cpp:589:39: error: 'r' was not declared in this scope
 static void GetOS(RTL_OSVERSIONINFOW *r)
                                       ^
C:\Users\hcomere\Perso\Urho3D\master\Source\Urho3D\Core\ProcessUtils.cpp:707:1: error: expected '}' at end of input
 }
 ^
make[5]: *** [CMakeFiles/PackageTool.dir/C_/Users/hcomere/Perso/Urho3D/master/Source/Urho3D/Core/ProcessUtils.cpp.obj] Error 1
make[4]: *** [CMakeFiles/PackageTool.dir/all] Error 2
make[3]: *** [all] Error 2
make[2]: *** [Source/Tools/PackageTool-prefix/src/PackageTool-stamp/PackageTool-build] Error 2
make[1]: *** [Source/Tools/CMakeFiles/PackageTool.dir/all] Error 2
make: *** [all] Error 2
``` 

Is it caused by anything on my side ?

Regards,
Harold

-------------------------

weitjong | 2017-06-20 00:28:17 UTC | #4

Most probably. I haven't seen any errors like that in my build environment for Web platform. For what it's worth, since you have been retrying, you should probably ensure you retry on new build tree location each time so that past failure does not interfere. Good luck.

-------------------------

hcomere | 2017-06-20 16:00:47 UTC | #5

Hi,

After many tries, i still have the same error but by removing lines causing the problem in ProcessUtils.cpp i am able to compile.
Good news, using master, i have not anymore the js exception described in original post.

Regarding the compile error, i have commented following lines : 
```
#if defined(_WIN32)
/*typedef NTSTATUS (WINAPI *RtlGetVersionPtr)(PRTL_OSVERSIONINFOW);

static void GetOS(RTL_OSVERSIONINFOW *r)
{
    HMODULE m = GetModuleHandle("ntdll.dll");
    if (m)
    {
        RtlGetVersionPtr fPtr = (RtlGetVersionPtr) GetProcAddress(m, "RtlGetVersion");
        if (r && fPtr && fPtr(r) == 0)
            r->dwOSVersionInfoSize = sizeof *r; 
    }
}*/
#endif 
```
and
```
String GetOSVersion() 
{
#if defined(__linux__) && !defined(__ANDROID__)
    struct utsname u;
    if (uname(&u) == 0)
        return String(u.sysname) + " " + u.release; 
#elif defined(_WIN32)
    /*RTL_OSVERSIONINFOW r;
    GetOS(&r); 
    // https://msdn.microsoft.com/en-us/library/windows/desktop/ms724832(v=vs.85).aspx
    if (r.dwMajorVersion == 5 && r.dwMinorVersion == 0) 
        return "Windows 2000"; 
    else if (r.dwMajorVersion == 5 && r.dwMinorVersion == 1) 
        return "Windows XP"; 
    else if (r.dwMajorVersion == 5 && r.dwMinorVersion == 2) 
        return "Windows XP 64-Bit Edition/Windows Server 2003/Windows Server 2003 R2"; 
    else if (r.dwMajorVersion == 6 && r.dwMinorVersion == 0) 
        return "Windows Vista/Windows Server 2008"; 
    else if (r.dwMajorVersion == 6 && r.dwMinorVersion == 1) 
        return "Windows 7/Windows Server 2008 R2"; 
    else if (r.dwMajorVersion == 6 && r.dwMinorVersion == 2) 
        return "Windows 8/Windows Server 2012";
    else if (r.dwMajorVersion == 6 && r.dwMinorVersion == 3) 
        return "Windows 8.1/Windows Server 2012 R2"; 
    else if (r.dwMajorVersion == 10 && r.dwMinorVersion == 0) 
        return "Windows 10/Windows Server 2016"; 
    else*/ 
        return "Windows Unidentified";
#elif defined(__APPLE__)
[...]
```

The strange thing is that ProcessUtils.cpp does not compile only when building PackageTool.exe, not when building Urho lib itself.
PRTL_OSVERSIONINFOW and RTL_OSVERSIONINFOW are unknown at this stage.

It looks like an issue with my MinGW windows headers which are not found.
Btw i am not using MinGW-W64 as suggested in :
https://urho3d.github.io/documentation/1.6/_building.html
I dont know it can be the cause.

Regards,
Harold

-------------------------

weitjong | 2017-06-21 00:37:26 UTC | #6

Glad to hear that you gave figured it out. Regarding the commented lines, I recall those are quite recently added code by a contributor. You may want to report this as an issue or even take it as a chance to send in a PR to fix this simple issue.

-------------------------

weitjong | 2017-06-26 03:38:54 UTC | #7

I have raised this as an issue. https://github.com/urho3d/Urho3D/issues/1998

-------------------------

slapin | 2017-06-26 05:47:11 UTC | #8

I wonder if there's some preprocessor macro which can be used there...

-------------------------

weitjong | 2017-06-26 05:59:26 UTC | #9

I also believe this is a simple issue to fix. You are too welcome to try to fix it, if you have extra time.

-------------------------

cadaver | 2017-06-26 20:16:27 UTC | #10

At least the MINI_URHO flag can be used to exclude the OS version functionality in the case of building PackageTool as part of Web build. However this doesn't solve the case where a native build would fail due to the same error. Possibly, old or incompatible MinGW. A kind of nuclear option for this case would be to disable it altogether on MinGW and derivatives.

-------------------------

slapin | 2017-06-26 20:54:30 UTC | #11

I think MinGW version check is less radical solution.

-------------------------

slapin | 2017-06-26 20:55:45 UTC | #12

But now I think it is best to just disable this function for web build (or provide faked version).

-------------------------

weitjong | 2017-06-27 01:35:27 UTC | #13

Alternatively, we could detect if the "built in" function is actually exists and route the code path conditionally.

-------------------------

cadaver | 2017-06-27 08:09:55 UTC | #14

That sounds like the best option. I could still do the MINI_URHO check as a first measure, since that doesn't arguably hurt.

-------------------------

weitjong | 2017-06-27 10:44:07 UTC | #15

Yes, I agree... I agree... (20 chars)

-------------------------

weitjong | 2017-07-02 07:18:23 UTC | #16

@hcomere, it would be great if you can test out the latest master branch to see whether it solves your remaining build issue.

-------------------------

hcomere | 2017-07-02 07:18:13 UTC | #17

Yes, with latest master, starting from scratch, emscripten build is OK now, thanks :)

-------------------------

JimSEOW | 2017-07-07 10:02:52 UTC | #18

[quote="hcomere, post:5, topic:3267"]
GetOSVersion
[/quote]

Regarding String GetOSVersion() 

Will there be issue to include Windows 10, for x64 and ARM? 

Still learning from others to figure out what are challenges

-------------------------

