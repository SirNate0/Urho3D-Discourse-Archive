Faizol | 2017-01-02 00:59:05 UTC | #1

Hi all,

  I have successfully run a skeleton program to test my development environment. Is there anywhere I should read on how to setup the needed cmake to compile my test application on Android platform? I've already tried searching it in the forum to no avail. Also it's a bit hard as the word 'android' is listed as an ordinary word and won't be used in the search parameter.

 Thanks in advance.

  cheers,

-------------------------

weitjong | 2017-01-02 00:59:05 UTC | #2

Urho3D project does not have just a cross-platform engine library, it has a cross-platform build script as well using just the same set of CMakeLists.txt files. In other words, there is no specific setup in CMakeLists.txt just for Android platform. Follow the instruction in [url]http://urho3d.github.io/documentation/a00004.html[/url] and in [url]http://urho3d.github.io/documentation/a00001.html[/url]. Then invoke CMake with one of the provided shell script or batch file that targets your desired platform, in this case: cmake_gcc.sh or cmake_android.bat. For the former, it relies on ANDROID_NDK environment variable to detect that you intend to target Android platform. The latter also needs the ANDROID_NDK environment variable to work properly.

-------------------------

Faizol | 2017-01-02 00:59:06 UTC | #3

[quote="weitjong"]Urho3D project does not have just a cross-platform engine library, it has a cross-platform build script as well using just the same set of CMakeLists.txt files. In other words, there is no specific setup in CMakeLists.txt just for Android platform. Follow the instruction in [url]http://urho3d.github.io/documentation/a00004.html[/url] and in [url]http://urho3d.github.io/documentation/a00001.html[/url]. Then invoke CMake with one of the provided shell script or batch file that targets your desired platform, in this case: cmake_gcc.sh or cmake_android.bat. For the former, it relies on ANDROID_NDK environment variable to detect that you intend to target Android platform. The latter also needs the ANDROID_NDK environment variable to work properly.[/quote]

Hi weitjong,

Thanks for the info. I don't have any problem with compiling and installing Urho3D samples on Android as the instruction in the documentation is very clear. Also I don't have any problem in building my test application (skeleton application as I mentioned previously) using the just compiled library. I have also read a few of your replies helping newbies about the two development structures (from inside Urho3D folder, and from out of Urho3D folder), which really helped me in getting my test application compiled.

What I'm trying to achieve now is to get my test program to use cmake automation in compiling for the android platform, much like how cmake_gcc.sh did for the samples on Android platform. While the documentation explains very clearly on how to compile application using cmake on the existing platform, there's no clue on how to do the same for the mobile platform.

Is there any pointer on how to achieve the necessary steps to compile for the Android platfom from outside of Urho3D folder?

Thank you in advance.

cheers,

-------------------------

cadaver | 2017-01-02 00:59:06 UTC | #4

On Android you need a few extra steps: 
- you need to create a Source/Android directory
- you need to copy the CMake toolchains from Source/CMake/ToolChains directory of the Urho3D source tree into your project's Source/CMake/ToolChains (I wonder if this could use the URHO3D_HOME enviroment var if set and use the toolchains from there instead)

After that it should be possible to invoke CMake for the Android toolchain and build the shared library of your application. That's only half of the battle though, then you need to build the apk for deployment; you can use the source & project files from Urho3D's Source/Android directory as a basis.

-------------------------

Faizol | 2017-01-02 00:59:06 UTC | #5

Hi cadaver,

Thank you for the tips. I've been modifying cmake_gcc.sh with limited success as I didn't know which folders are required to ensure a proper compilation of a program for android platform.

Again thank you for the help. Really appreciate it.

cheers,

-------------------------

cadaver | 2017-01-02 00:59:06 UTC | #6

Note that what I wrote is possibly relevant only on Windows; I haven't personally compiled for Android (and especially not a project external to Urho) outside Windows for a while.

-------------------------

scorvi | 2017-01-02 00:59:06 UTC | #7

hey 

i am using the lib also as an external library [url]http://urho3d.github.io/documentation/a00004.html[/url] and as long as i dont use  android.toolchain.cmake i can build my projects.

but if i use the cmake_android.bat script file i get the error: 
[code]
CMake Error at C:/Users/vitali/Hobby/Coding/Engine/Urho3D/Source/CMake/Modules/FindUrho3D.cmake:166 (message):
  Could not find Urho3D library in default SDK installation location or
  Urho3D project root tree.  For searching in a non-default Urho3D SDK
  installation, use 'URHO3D_INSTALL_PREFIX' environment variable to specify
  the prefix path of the installation location.  For searching in a build
  tree of Urho3D project, use 'URHO3D_HOME' environment variable to specify
  the Urho3D project root directory.  The Urho3D library itself must already
  be built successfully.
Call Stack (most recent call first):
  CMakeLists.txt:21 (find_package)
[/code]

and if i manualy add the lib with cmake-gui  i can generate the makefile project but if i compile it i get the error :
[code]
C:\......\Engine\Urho3D\scorvi\VerseClient\android-Builf>make
Scanning dependencies of target VerseClient
[ 33%] Building CXX object CMakeFiles/VerseClient.dir/VerseClient.cpp.o
In file included from C:/....../Engine/Urho3D/Source/Engine/C
ontainer/Ptr.h:25:0,
                 from C:/....../Engine/Urho3D/Source/Engine/Core/Attribute.h:25,
                 from C:/......//Engine/Urho3D/Source/Engine/Core/Context.h:25,
                 from C:/......//Engine/Urho3D/Source/Engine/Engine/Application.h:25,
                 from C:/......//Engine/Urho3D/scorvi/VerseClient/Source/CallForDungeons.cpp:22:
C:/....../Engine/Urho3D/Source/Engine/Container/RefCounted.h:
25:20: fatal error: Urho3D.h: No such file or directory
 #include "Urho3D.h"
                    ^
compilation terminated.
make[2]: *** [CMakeFiles/VerseClient.dir/VerseClient.cpp.o] Error 1
make[1]: *** [CMakeFiles/VerseClient.dir/all] Error 2
make: *** [all] Error 2
[/code]

with the toolchain cmake does not find the urho3d libs/includes ... dont know why :-/

-------------------------

cadaver | 2017-01-02 00:59:06 UTC | #8

Do you have URHO3D_HOME environment variable set? Urho3D for Android built successfully in that location? And the toolchain copied to your own source directory? You may need to do CMake cleanup to (cmake_clean.bat) to remove traces of previous failed configuration attempts. Other than that I don't know of more steps that would be needed.

-------------------------

scorvi | 2017-01-02 00:59:06 UTC | #9

yes i set URHO3D_HOME and i did build Urho3d for android and for visual studio. so if i build the whole Uhro3d project it works fine. 
 
i created a project in the uhro3d root folder and a project besides the uhro3d root folder. i tested builds with toolchain copied and without but every build with the toolchain results in the same error ... i also used a new uhro3d version to test ... so the toolchain does something funny to the FindUrho3D.cmake modul if it is not in the Urho3d build  :-/

-------------------------

weitjong | 2017-01-02 00:59:06 UTC | #10

We tested the external project linking to Urho3D as external library everyday for all the supported platforms in our Travis CI setup. We have gone an extra mile to ensure that external project can find the Urho3D library, provided the external project is being setup correctly as per documentation. You can study the Rakefile script closely how it uses cmake_gcc.sh single-handedly to configure the projects for Linux, Windows, Android, and Raspberry Pi. You can see that it can achieve all this with the same set of CMakeLists.txt. You can also see that how the same cmake_gcc.sh script is being used to configure both the Urho3D project and external project to use the CMake's android toolchain.

There are two steps for Android build (this is how I understand it, please correct me if I am wrong):
[ol]
[li] Compiling and linking C/C++ native-code with the help of Android NDK and CMake's android toolchain.[/li]
[li] Creating APK with the help of Android SDK which targets a range of API levels.[/li][/ol]

Only in step 2, you need the "Source/Android" directory structure as mentioned by Lasse. Your Android project would need both steps, of course. Our CI build does both steps for Urho3D project but only step 1 for external project (because we only want to test it whether it can link with Urho3D library without creating another apk).

Project configuration for cross-compiling builds, using MinGW, Android, or Raspberry PI toolchain, are still not fully tested via CMake GUI (graphical user interface). But I am not saying it is not possible. Currently our build scripts know which build options are specific to those platforms and will attempt to make the options available for user to configure interactively in the GUI. However, it stops short to configure the toolchain part. So, I would say, unless you know what you are doing, you are better off with configuring for cross-compiling builds using the CMake CLI (command line interface) via the provided cmake_* shell scripts or batch files.

Going back to your CMake error. You should not get it if you have followed the setup correctly as per documentation. You need to set the URHO3D_HOME correctly or install the Urho3D library/SDK correctly. Can you tell us which approach do you use? If it is the former, make sure CMAKE_MODULE_PATH is set properly and the Urho3D library itself has been built. I am sorry to point out the obvious as I could not think of anything else for the failure.

-------------------------

