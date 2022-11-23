Bluemoon | 2019-02-27 19:03:25 UTC | #1

I'm trying to build Urho3D for android using the dockerize-android through docker's kitematic. Everything goes well and the build runs for a while, then it fails with:

>  /home/urho3d/Source/Urho3D/AngelScript/../AngelScript/Addons.h:35:10: fatal error: 'AngelScript/angelscript.h' file not found

I am confused as to why this should even happen. Below is the full output of the container log

>Task :android:urho3d-lib:externalNativeBuildDebug FAILED
>A<==-----------> 23% EXECUTING [51s]DB> IDLEDBA
>FAILURE: Build failed with an exception.
>* What went wrong:
>Execution failed for task ':android:urho3d-lib:externalNativeBuildDebug'.
>Build command failed.
>  Error while executing process /android-sdk/cmake/3.6.4111459/bin/cmake with arguments {--build /home/urho3d/android/urho3d-lib/.externalNativeBuild/cmake/debug/x86_64 --target Urho3D}
>  [1/280] Building CXX object Source/Urho3D/CMakeFiles/Urho3D.dir/AngelScript/GraphicsAPI.cpp.o
>  [2/280] Building CXX object Source/Urho3D/CMakeFiles/Urho3D.dir/AngelScript/AudioAPI.cpp.o
>  FAILED: /usr/bin/ccache /android-sdk/ndk-bundle/toolchains/llvm/prebuilt/linux-x86_64/bin/clang++  --target=x86_64-none-linux-android21 --gcc-toolchain=/android-sdk/ndk-bundle/toolchains/x86_64-4.9/prebuilt/linux-x86_64 --sysroot=/android-sdk/ndk-bundle/sysroot  -DHAVE_SINCOSF -DTOLUA_RELEASE -DURHO3D_ANGELSCRIPT -DURHO3D_FILEWATCHER -DURHO3D_IK -DURHO3D_IS_BUILDING -DURHO3D_LOGGING -DURHO3D_LUA -DURHO3D_LUA_RAW_SCRIPT_LOADER -DURHO3D_NAVIGATION -DURHO3D_NETWORK -DURHO3D_PHYSICS -DURHO3D_PROFILING -DURHO3D_STATIC_DEFINE -DURHO3D_THREADING -DURHO3D_URHO2D -DURHO3D_WEBP -ISource/Urho3D -I../../../../../../Source/Urho3D -I../../../../build/tree/Debug/x86_64/include/Urho3D/ThirdParty -I../../../../build/tree/Debug/x86_64/include/Urho3D/ThirdParty/Bullet -I../../../../build/tree/Debug/x86_64/include/Urho3D/ThirdParty/Detour -I../../../../build/tree/Debug/x86_64/include/Urho3D/ThirdParty/Lua -isystem /android-sdk/ndk-bundle/sources/cxx-stl/llvm-libc++/include -isystem /android-sdk/ndk-bundle/sources/cxx-stl/llvm-libc++abi/include -isystem /android-sdk/ndk-bundle/sysroot/usr/include/x86_64-linux-android -g -DANDROID -ffunction-sections -funwind-tables -fstack-protector-strong -no-canonical-prefixes -Wa,--noexecstack -Wformat -Werror=format-security -std=c++11  -std=c++11 -Wno-invalid-offsetof -Qunused-arguments -fcolor-diagnostics -O0 -fno-limit-debug-info  -fPIC -MD -MT Source/Urho3D/CMakeFiles/Urho3D.dir/AngelScript/AudioAPI.cpp.o -MF Source/Urho3D/CMakeFiles/Urho3D.dir/AngelScript/AudioAPI.cpp.o.d -o Source/Urho3D/CMakeFiles/Urho3D.dir/AngelScript/AudioAPI.cpp.o -c /home/urho3d/Source/Urho3D/AngelScript/AudioAPI.cpp
>  In file included from /home/urho3d/Source/Urho3D/AngelScript/AudioAPI.cpp:25:
>  In file included from /home/urho3d/Source/Urho3D/AngelScript/../AngelScript/APITemplates.h:25:
>  /home/urho3d/Source/Urho3D/AngelScript/../AngelScript/Addons.h:35:10: fatal error: 'AngelScript/angelscript.h' file not found
>  #include <AngelScript/angelscript.h>
>           ^~~~~~~~~~~~~~~~~~~~~~~~~~~
>  1 error generated.
>  FAILED: /usr/bin/ccache /android-sdk/ndk-bundle/toolchains/llvm/prebuilt/linux-x86_64/bin/clang++  --target=x86_64-none-linux-android21 --gcc-toolchain=/android-sdk/ndk-bundle/toolchains/x86_64-4.9/prebuilt/linux-x86_64 --sysroot=/android-sdk/ndk-bundle/sysroot  -DHAVE_SINCOSF -DTOLUA_RELEASE -DURHO3D_ANGELSCRIPT -DURHO3D_FILEWATCHER -DURHO3D_IK -DURHO3D_IS_BUILDING -DURHO3D_LOGGING -DURHO3D_LUA -DURHO3D_LUA_RAW_SCRIPT_LOADER -DURHO3D_NAVIGATION -DURHO3D_NETWORK -DURHO3D_PHYSICS -DURHO3D_PROFILING -DURHO3D_STATIC_DEFINE -DURHO3D_THREADING -DURHO3D_URHO2D -DURHO3D_WEBP -ISource/Urho3D -I../../../../../../Source/Urho3D -I../../../../build/tree/Debug/x86_64/include/Urho3D/ThirdParty -I../../../../build/tree/Debug/x86_64/include/Urho3D/ThirdParty/Bullet -I../../../../build/tree/Debug/x86_64/include/Urho3D/ThirdParty/Detour -I../../../../build/tree/Debug/x86_64/include/Urho3D/ThirdParty/Lua -isystem /android-sdk/ndk-bundle/sources/cxx-stl/llvm-libc++/include -isystem /android-sdk/ndk-bundle/sources/cxx-stl/llvm-libc++abi/include -isystem /android-sdk/ndk-bundle/sysroot/usr/include/x86_64-linux-android -g -DANDROID -ffunction-sections -funwind-tables -fstack-protector-strong -no-canonical-prefixes -Wa,--noexecstack -Wformat -Werror=format-security -std=c++11  -std=c++11 -Wno-invalid-offsetof -Qunused-arguments -fcolor-diagnostics -O0 -fno-limit-debug-info  -fPIC -MD -MT Source/Urho3D/CMakeFiles/Urho3D.dir/AngelScript/GraphicsAPI.cpp.o -MF Source/Urho3D/CMakeFiles/Urho3D.dir/AngelScript/GraphicsAPI.cpp.o.d -o Source/Urho3D/CMakeFiles/Urho3D.dir/AngelScript/GraphicsAPI.cpp.o -c /home/urho3d/Source/Urho3D/AngelScript/GraphicsAPI.cpp
>  In file included from /home/urho3d/Source/Urho3D/AngelScript/GraphicsAPI.cpp:25:
>  In file included from /home/urho3d/Source/Urho3D/AngelScript/../AngelScript/APITemplates.h:25:
>  /home/urho3d/Source/Urho3D/AngelScript/../AngelScript/Addons.h:35:10: fatal error: 'AngelScript/angelscript.h' file not found
>  #include <AngelScript/angelscript.h>
>           ^~~~~~~~~~~~~~~~~~~~~~~~~~~
>  1 error generated.
>  ninja: build stopped: subcommand failed.

What exactly am I doing wrong? I don't know if anyone has encountered this too. 

System Specs: Windows 10 x84_64

-------------------------

weitjong | 2019-02-28 00:44:55 UTC | #2

It is not enough just give output without telling us the actual steps you took. I assume you use the Docker images for the DBE, which requires specific way to run it in a container. The DBE only provides a convenient shell script to do this and there is no batch file yet. However, you can have a look at that  “dockerized.sh” script and try to do the Windows-equivalent way to run the container on Windows. The most important part is to mount the project you want build correctly. For sure this has not been tested on Windows host AFAIK, but the DBE is designed to work everywhere.

-------------------------

Leith | 2019-02-28 01:57:35 UTC | #3

This is a path-completion issue.
Apparently, the path to Source/Urho3D/ThirdParty folder is missing from the search paths in your build settings. It should be easy enough to manually add that search path, so your compiler can then find Source/Urho3D/ThirdParty/AngelScript/angelscript.h

-------------------------

Bluemoon | 2019-02-28 09:10:15 UTC | #4

Ok.

So I'm running docker on windows through Docker Toolkit and it comes with a "Docker Quick Start" Terminal and Kitematic (more like the GUI interface).

Docker Quick Start Terminal prepares the docker environment in a terminal for you to be able to run script/dockerized.sh. But when I run the dockerised script I get
> C:\Program Files\Docker Toolbox\docker.exe: open /dev/fd/63: The system cannot find the path specified.
See 'C:\Program Files\Docker Toolbox\docker.exe run --help'.

I noticed this came from the --env-file line so I made a modification to bypass it but then I get stuck with

> C:\Program Files\Docker Toolbox\docker.exe: Error response from daemon: invalid mount config for type "bind": bind source path does not exist: /C/Uhro3D_Build/Urho3D_Git.
See 'C:\Program Files\Docker Toolbox\docker.exe run --help'.

The funny thing is that the said bind path that it complains does not exists is actually where I'm running the command from.

What I decided to do next is to use the Kitematic approach. I opened the app, browsed for urho3d dockerized images, saw that of android (dokerized-android) and pulled it down to my system. With this done i went to the volume tab and set /home/urho3d to point to a local and acccessible Urho3D project folder. At the General Tab under "Environment Variable" section I added PROJECT_DIR key and set its value to /home/urho3d.

Every single thing went well. On starting the image the build process began, downloaded gradle and other kotlin libs and accessories, it infact began to successfully compile some of the third-party libs. Every thing was moving smooth till it hit the error I posted earlier above as summarized below
> /home/urho3d/Source/Urho3D/AngelScript/…/AngelScript/Addons.h:35:10: fatal error: ‘AngelScript/angelscript.h’ file not found
#include &lt;AngelScript/angelscript.h&gt;
^~~~~~~~~~~~~~~~~~~~~~~~~~~
1 error generated.
ninja: build stopped: subcommand failed

So that's my current dilemma.

---
I've just been looking for how I can get an android build for Urho3D but my trials keep failing :disappointed:

-------------------------

Bluemoon | 2019-02-28 09:11:03 UTC | #5

Seems so but the build setting is all in the docker image

-------------------------

weitjong | 2019-02-28 10:23:59 UTC | #6

I have not used the tools you mentioned, so I am afraid I cannot help you much. But the point to take back is, the docker images that we published in the DockerHub only contain the dockerized “build environment” (hence we named it DBE) and it does not tie to Urho3D project specifically. The DBE simply invokes the same and well-tested CMake build system to generate the build tree and this is no exception for Android build (just that now it is Gradle invoking the CMake on our behalf). And so far we have never required our user to manually tweak the generated build tree to fix any build. It just works out of the box, at least on all those host/platform combinations that our CI build covers.

-------------------------

Leith | 2019-02-28 09:56:21 UTC | #7

I'm no expert in c#, but usually there is a manifold file that describes the input files - actually, this guy, weitjong, tends to deal with build issues, I defer to him on this issue
But if a customer is complaining, I am willing to try to help too. Try to be specific about your build settings, it can help us to help you.

-------------------------

weitjong | 2019-02-28 15:57:37 UTC | #8

Just wonder whether you have tried to temporarily disable AngelScript with `URHO3D_ANGELSCRIPT=0` and see how far the build would go.

-------------------------

Bluemoon | 2019-02-28 16:17:51 UTC | #9

I disabled AngelScript and the now the build is faulting the IK lib :sweat_smile:
> Source/Urho3D/CMakeFiles/Urho3D.dir/IK/IKEffector.cpp.o -MF Source/Urho3D/CMakeFiles/Urho3D.dir/IK/IKEffector.cpp.o.d -o Source/Urho3D/CMakeFiles/Urho3D.dir/IK/IKEffector.cpp.o -c /home/urho3d/Source/Urho3D/IK/IKEffector.cpp
  In file included from /home/urho3d/Source/Urho3D/IK/IKEffector.cpp:25:
  /home/urho3d/Source/Urho3D/IK/../IK/IKConverters.h:28:10: fatal error: 'ik/quat.h' file not found
  #include &lt;ik/quat.h&gt;
           ^~~~~~~~~~~
1 error generated.
ninja: build stopped: subcommand failed.

What I observed though is that the Third Party libraries build without issue but the problem arises when the build process approached Urho3D lib proper. 

I'm kind of sure it's a third party lib include issue. I'm still investigating

-------------------------

weitjong | 2019-03-01 02:09:34 UTC | #10

You know you can “exec -it” into a running container to execute the “bash” command and poke around, right? Actually you can also run the initial container with “bash” command directly too, instead of the default command “./gradlew build”. Just supply the command as  the last arg. This is all docker feature, not specific to our DBE images. Once inside the bash, invoke Gradle or what have you then check the build tree’s “include/Urho3D” subdir. Somewhere there should have all the symbolic links to 3rd-party headers. Our build script has always configured the header search path with this subdir. So when the symlinks were not created correctly due to whatever reason in your case then that would probably explains your current situation. Good luck.

-------------------------

Leith | 2019-03-01 02:41:52 UTC | #11

You're still missing some include paths.
In this case, you want to include the ThirdParty folder.
It's path will be something like "Urho3D/Source/ThirdParty" in your master source folder.

-------------------------

Bluemoon | 2019-03-01 13:39:11 UTC | #12

As an update, I manually created the symlinks and was able to build pass x86_64 architecture for android but it fails at x86.

Still looking for how to get it done

-------------------------

weitjong | 2019-03-01 13:55:32 UTC | #13

At least you are onto something and on the right track now. The symlink creation macro is available in our own `UrhoCommon.cmake`. CMake does not have this command built-in because of Windows host does not support this concept. Our macro implementation detects what is the host system and branch accordingly. So, it is possible that with Windows host running dockerized build environment (which is actually based on Ubuntu), now our detection logic goes haywire. This is just a guess of course.

-------------------------

