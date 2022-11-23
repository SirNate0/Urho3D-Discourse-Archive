DainTorson | 2017-06-25 20:50:40 UTC | #1

I'm trying to use Urho3D as external library with CMake and VS 2017 as shown here:
https://urho3d.github.io/documentation/1.6/_using_library.html
I managed to build the project, but the font and picture do no load regardless of the place where I put them.
Moreover, when I try to specify any other build folder than default, CMake fails to find Urho3D_d.lib.

Any help will be useful.

-------------------------

weitjong | 2017-06-26 03:00:16 UTC | #2

You have to show us the exact steps you have taken as your problem description is not clear where the mistake happened. The build system could not find the Urho3D library simply means you have made a mistake somewhere.

-------------------------

DainTorson | 2017-06-26 23:41:07 UTC | #3

Thank you for your reply.
Well, I'll try to be as specific as I can.
I've created a folder with the following structure:

urho-test/
 ├ bin/
 │  ├ Data/
 │  └ CoreData/
 ├ CMake/
 │  ├ Modules/
 │  └ Toolchains/
 ├ CMakeLists.txt
 ├ HelloWorld.cpp
 ├ HelloWorld.h
 ├ Sample.h
 └ Sample.inl

where all of the sources were taken from samples of Urho3D.

My CMakeLists.txt is identical to the one from here:
https://urho3d.github.io/documentation/1.6/_using_library.html

I've only specified the location of Urho3D with the folowing command:
`set(URHO3D_HOME "c:/Urho3d/")`

Then I've opened this folder with Visual Studio 2017 (since it now supports CMake) and got the following output from the CMake:

    1> Command line: C:\PROGRAM FILES (X86)\MICROSOFT VISUAL STUDIO\2017\COMMUNITY\COMMON7\IDE\COMMONEXTENSIONS\MICROSOFT\CMAKE\CMake\bin\cmake.exe  -G "Visual Studio 15 2017" -DCMAKE_INSTALL_PREFIX:PATH="C:\Users\Ales\AppData\Local\CMakeBuild\b127fd59-b858-303f-8a0e-0b36e52b0dd1\build\install"  -DCMAKE_CONFIGURATION_TYPES="Debug" "D:\dev\urho-test"
    1> Working directory: C:\Users\Ales\AppData\Local\CMakeBuild\b127fd59-b858-303f-8a0e-0b36e52b0dd1\build\x86-Debug
    1> -- Found Urho3D: C:/Urho3d/lib/Urho3D_d.lib (found version "Unversioned")
    1> -- Looking for C++ include d3dcompiler.h
    1> -- Looking for C++ include d3dcompiler.h - found
    1> -- Looking for C++ include d3d9.h
    1> -- Looking for C++ include d3d9.h - found
    1> -- Looking for C++ include d3d11.h
    1> -- Looking for C++ include d3d11.h - found
    1> -- Looking for C++ include ddraw.h
    1> -- Looking for C++ include ddraw.h - found
    1> -- Looking for C++ include dsound.h
    1> -- Looking for C++ include dsound.h - found
    1> -- Looking for C++ include dinput.h
    1> -- Looking for C++ include dinput.h - found
    1> -- Looking for C++ include dxgi.h
    1> -- Looking for C++ include dxgi.h - found
    1> -- Looking for C++ include xaudio2.h
    1> -- Looking for C++ include xaudio2.h - found
    1> -- Looking for include files windows.h, xinput.h
    1> -- Looking for include files windows.h, xinput.h - found
    1> -- Found DirectX: TRUE  found components:  DInput DSound XAudio2 XInput 
    1> Error copying file (if different) from "D:/dev/urho-test/bin/Autoload" to "C:/Users/Ales/AppData/Local/CMakeBuild/b127fd59-b858-303f-8a0e-0b36e52b0dd1/build/x86-Debug/bin/Autoload".
    1> -- Configuring done
    1> -- Generating done
    1> -- Build files have been written to: C:/Users/Ales/AppData/Local/CMakeBuild/b127fd59-b858-303f-8a0e-0b36e52b0dd1/build/x86-Debug
    1> Starting CMake target info extraction ...
    1> CMake server connection made.

So it sucessfully generates solution somewhere inside of AppData, and when I build and execute it, black window without any text appears, despite of the fact that GetResource function returns some valid pointer.

Also when I try to change working directory for CMake in CMakeSettigns.json, I  get the following error:

     CMake Error at CMake/Modules/FindUrho3D.cmake:352 (message):
    1>   Could NOT find compatible Urho3D library in Urho3D SDK installation or
    1>   build tree.  Use URHO3D_HOME environment variable or build option to
    1>   specify the location of the non-default SDK installation or build tree.
    1>   Ensure the specified location contains the Urho3D library of the requested
    1>   library type.

-------------------------

weitjong | 2017-06-27 00:42:30 UTC | #4

I haven't tried VS2017 yet, so I don't know how well it supports CMake directly. But assuming all it does is internally invoke "cmake" CLI then we can probably rule out that the source of your problem. Still, if I were you, I would try to isolate the problem first by manually invoking "cmake" to generate the build tree (solution file), then try to build the solution with VS. 

In your post you have linked to version 1.6 of the documentation. Also another common pitfall, note that our online doc are versioned. If you are using "master" branch in Git for the code then you have to use "HEAD" version of the online doc. Most notably the content of main CMakeList.txt is not entirely identical from version to version in general.

-------------------------

Lumak | 2017-06-27 00:56:40 UTC | #5

[quote="DainTorson, post:3, topic:3281"]
**Error copying file** (if different) from "D:/dev/urho-test/bin/Autoload" to "C:/Users/Ales/AppData/Local/CMakeBuild/b127fd59-b858-303f-8a0e-0b36e52b0dd1/build/x86-Debug/bin/Autoload".
[/quote]

Doesn't look like it was a success. It looks more like you have no admin rights and it blocked copy.

-------------------------

weitjong | 2017-06-27 01:28:05 UTC | #6

No. I strongly against using Admin account for doing development. Moreover the error line looks like because his project source tree doesn't have Autoload directory.

-------------------------

Lumak | 2017-06-27 01:47:15 UTC | #7

You don't have to be logged into Admin account, just change your Command Prompt and give it admin rights.

-------------------------

weitjong | 2017-06-27 02:36:19 UTC | #8

It's analogy to executing any mundane dev process using sudo. Also a big NO in my book. But this is out of topic discussion.

-------------------------

Lumak | 2017-06-27 04:08:35 UTC | #9

I think most Windows users are aware that certain apps require changing Admin rights and command prompt is one of them. sudo in Windows? huh.

-------------------------

weitjong | 2017-06-27 10:35:43 UTC | #10

Of course I meant it's equivalent to sudo on Linux (the host I am using). :slightly_smiling_face:

-------------------------

DainTorson | 2017-06-27 21:16:26 UTC | #11

Thank you for the quick reply!

So, I've generated the solution with the help of CMake GUI, but still have the same issue. I can build the project, but all I get is a black window instead of text, despite of the fact that GetResource function returns valid pointer. Is there any way to find why the text wasn't created?

-------------------------

weitjong | 2017-07-08 16:16:19 UTC | #12

Aha! Then what you are facing is probably not a build system related issue. If you build your project as a console app (see URHO3D_WIN32_CONSOLE build option) then you should be able to get some log entries from the console output/error streams. Or just use the debugger to step through your code.

-------------------------

DainTorson | 2017-06-28 20:33:08 UTC | #13

I've finally managed to build the HelloWorld project, when I've enabled console. The problem was in the resourses that I didn't copy from Data folder (I've only copied  fonts assuming it's enough :flushed:). 

Anyway, many thanks for your help. It's truly amazing to see such caring and active community.

-------------------------

JimSEOW | 2017-07-07 09:46:25 UTC | #14

Can u make your hello as a github so others do not have to repeat the challenges u face. Thanks

-------------------------

DainTorson | 2017-07-08 16:21:03 UTC | #15

No problem. I link the minimal example here:

https://github.com/DainTorson/urho-helloworld-vs2017/

-------------------------

