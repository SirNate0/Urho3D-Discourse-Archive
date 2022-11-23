Bluemoon | 2019-09-26 10:01:00 UTC | #1

So I returned back to try building an android version on Urho3D, this time using the dockerized build environment on a proper docker installation (not docker toolkit as was my earlier attempt). 

However I'm unfortunately still no making much headway. I downloaded the image using

> docker pull urho3d/dockerized-android

Next I ran the below to build urho3d for android
> docker run -it --rm --mount type=bind,source=C:\urho3d\urho3d-source,target=/urho3d   -e PROJECT_DIR=/urho3d   -e HOST_UID=1234 -e HOST_GID=1234   urho3d/dockerized-android ./gradlew -P ANDROID_ABI=armeabi-v7a build

But then after much initializations and configurations it fails with the below output

> Downloading https://services.gradle.org/distributions/gradle-5.4.1-all.zip
> ..............................................................................................................................
>         
> Welcome to Gradle 5.4.1!
>         
> Here are the highlights of this release:
>  - Run builds with JDK12
>  - New API for Incremental Tasks
>  - Updates to native projects, including Swift 5 support
>         
> For more details see https://docs.gradle.org/5.4.1/release-notes.html
>         
> Starting a Gradle Daemon (subsequent builds will be faster)
> Compatible side by side NDK version was not found.
> Compatible side by side NDK version was not found.
>         
> FAILURE: Build failed with an exception.
>         
> * What went wrong:
> Could not determine the dependencies of task ':android:urho3d-lib:mergeReleaseNativeLibs'.
> \> The SDK directory '/urho3d/C:\Users\blue\AppData\Local\Android\Sdk' does not exist.
>         
> * Try:  
> Run with --stacktrace option to get the stack trace. Run with --info or --debug option to get more log output. Run with --scan to get full insights.
>         
> * Get more help at https://help.gradle.org
>         
> BUILD FAILED in 4m 52s
> PS C:\urho3d\urho3d-source>

From the little I can take out from the above output it seems there is a problem locating my android sdk installation. But I thought all those were all supposed to be bundled up in the DBE.

-------------------------

weitjong | 2019-09-26 10:52:52 UTC | #2

You probably will have a better luck with WSL2. The DBE has not been intended for Windows system as it is now.

-------------------------

weitjong | 2019-09-26 16:24:05 UTC | #3

[quote="Bluemoon, post:1, topic:5629"]
* > The SDK directory ‘/urho3d/C:\Users\blue\AppData\Local\Android\Sdk’ does not exist.
[/quote]

Sorry for double post. But I have an extra information which may be valuable to you. Based on the above line, I believe you might have tried Gradle build with Android SDK locally installed in your Windows host system too. If so, then your previous attempt may have generated a file called "local.properties" at the project root. You need to delete this file so that it does not interfere and let the Gradle Android plugin (in the DBE) regenerates it with the correct bundled SDK installation path. So, this should at least fix that problem.

There is still other problems with your attempt though, for example the value 1234 for the HOST_UID and HOST_GID in my README are really just a placeholder that needs to be substituted with the actual UID and GID of your account at the host system (a notion that does not exist on Windows). They are needed so that all the build artifacts generated during DBE run can be set to be owned by this UID:GID, making them accessible by host user after the container has ended the run, i.e. making them virtually indistinguishable from conventional build artifact. Having said that, since Windows system does not have this UID:GID notion, it may work accidentally too as Windows may just let whoever the host user to access the generated build artifacts. IDK.

-------------------------

Bluemoon | 2019-09-26 23:54:58 UTC | #4

:sweat_smile:
You are absolutely right. I actually tried an android build directly on my host system and it didn't work, that was before I resorted DBE. After deleting the generated "local.properties" file the project build. You were also right about the HOST_UID and HOST_GID, I still left them as is since my build system is windows.

However after the urho3d lib has been build and now the samples were been built the process encountered series of errors complaining about the redefinition some urho3d objects. Below is a section of the output

>In file included from /urho3d/Source/Samples/02_HelloGUI/HelloGUI.cpp:27:
>In file included from /urho3d/android/urho3d-lib/build/tree/Debug/armeabi-v7a/include/Urho3D/Input/Input.h:33:
>In file included from /urho3d/android/urho3d-lib/build/tree/Debug/armeabi-v7a/include/Urho3D/Input/../UI/Cursor.h:27:
>In file included from /urho3d/android/urho3d-lib/build/tree/Debug/armeabi-v7a/include/Urho3D/Input/../UI/../Graphics/Texture.h:25:
>/urho3d/android/urho3d-lib/build/tree/Debug/armeabi-v7a/include/Urho3D/Input/../UI/../Graphics/../Graphics/GPUObject.h:33:7: error: redefinition of 'GPUObjectHandle'
>union GPUObjectHandle
>      ^
>/urho3d/android/urho3d-lib/build/tree/Debug/armeabi-v7a/include/Urho3D/Graphics/../Graphics/GPUObject.h:33:7: note: previous definition is here
>union GPUObjectHandle
>      ^
>In file included from /urho3d/Source/Samples/02_HelloGUI/HelloGUI.cpp:27:
>In file included from /urho3d/android/urho3d-lib/build/tree/Debug/armeabi-v7a/include/Urho3D/Input/Input.h:33:
>In file included from /urho3d/android/urho3d-lib/build/tree/Debug/armeabi-v7a/include/Urho3D/Input/../UI/Cursor.h:27:
>In file included from /urho3d/android/urho3d-lib/build/tree/Debug/armeabi-v7a/include/Urho3D/Input/../UI/../Graphics/Texture.h:25:
>/urho3d/android/urho3d-lib/build/tree/Debug/armeabi-v7a/include/Urho3D/Input/../UI/../Graphics/../Graphics/GPUObject.h:42:18: error: redefinition of 'GPUObject'
>class URHO3D_API GPUObject
>                 ^
>/urho3d/android/urho3d-lib/build/tree/Debug/armeabi-v7a/include/Urho3D/Graphics/../Graphics/GPUObject.h:42:18: note: previous definition is here
>class URHO3D_API GPUObject

-------------------------

weitjong | 2019-09-27 15:57:57 UTC | #5

I am sorry to hear that. I have not encountered anything like this before on Linux, so I am not sure what could possibly be causing this. Are you using STATIC or SHARED lib type? Perhaps it worth your time to try to flip the type add see how far you could go.

-------------------------

