cin | 2017-01-02 01:01:55 UTC | #1

I want try to understand how to build step by step Urho3D and my app for android platform on Windows. I download Android NDK, ant and all paths is writed to system.

-------------------------

alexrass | 2017-01-02 01:01:56 UTC | #2

0) download sdk, ndk, ant and install jdk
1) enviroment
set JAVA_HOME="c:\Program Files\Java\jdk1.7.0_51" <- or your version
set ANDROID_NDK=<PATH TO>\android-ndk\
set ANDROID_SDK=<PATH TO>\android-sdk-windows\
set PATH=%PATH%;<PATH TO>\android-sdk-windows\tools
set PATH=%PATH%;<PATH TO>\android-sdk-windows\platform-tools
set PATH=%PATH%;<PATH TO>\android-sdk-windows\build-tools
set PATH=%PATH%;<PATH TO>\android-ndk\prebuilt\windows\bin
set PATH=%PATH%;<PATH TO>\apache-ant-1.9.3\bin <- or your version
2)
in Urho3D folder run cmake_android.bat -DURHO3D_MKLINK=1 -DCMAKE_BUILD_TYPE=Release
3)
go to folder "android-Build"
3.5)
android update project -p . -t 1 (only needed on the first time, replace '-t 1' with desired target-id ("android list targets" for list targets))
4)
make (or make -j4)
5)
ant release
6)
install Urho3D.apk

-------------------------

hdunderscore | 2017-01-02 01:01:56 UTC | #3

Between steps 4 and 5, you might need:
[quote]android update project -p . -t 1 (only needed on the first time, replace '-t 1' with desired target-id)[/quote]
([urho3d.github.io/documentation/1 ... lding.html](http://urho3d.github.io/documentation/1.32/_building.html))

You can see which targets you have with:
[quote]android list targets[/quote]

-------------------------

cin | 2017-01-02 01:01:56 UTC | #4

I'm manually copy all files to android-Build folder and run cmake_android.bat

[b]Output:[/b]
[spoiler]F:\Urho3D>cmake_android.bat -DURHO3D_MKLINK=0 -DCMAKE_BUILD_TYPE=Release

F:\Urho3D>cmake -E chdir Source\Android cmake  -G "Unix Makefiles" -DANDROID=1 -DCMAKE_TOOLCHAIN_FILE=..\CMake\Toolchains\android.toolchain.cmake -DLIBRARY_OUTPUT_PATH_ROOT=.  -DURHO3D_MKLINK=0 -DCMAK
E_BUILD_TYPE=Release ..
CMake Warning (dev) at CMake/Toolchains/android.toolchain.cmake:601 (elseif):
  Policy CMP0054 is not set: Only interpret if() arguments as variables or
  keywords when unquoted.  Run "cmake --help-policy CMP0054" for policy
  details.  Use the cmake_policy command to set the policy and suppress this
  warning.

  Quoted variables like "ANDROID" will no longer be dereferenced when the
  policy is set to NEW.  Since the policy is not set the OLD behavior will be
  used.
Call Stack (most recent call first):
  f:/CMake/share/cmake-3.1/Modules/CMakeDetermineSystem.cmake:95 (include)
  CMakeLists.txt:24 (project)
This warning is for project developers.  Use -Wno-dev to suppress it.

CMake Error at CMake/Toolchains/android.toolchain.cmake:839 (list):
  list index: 17 out of range (-17, 16)
Call Stack (most recent call first):
  f:/CMake/share/cmake-3.1/Modules/CMakeDetermineSystem.cmake:95 (include)
  CMakeLists.txt:24 (project)


CMake Warning (dev) at CMake/Toolchains/android.toolchain.cmake:1682 (if):
  Policy CMP0054 is not set: Only interpret if() arguments as variables or
  keywords when unquoted.  Run "cmake --help-policy CMP0054" for policy
  details.  Use the cmake_policy command to set the policy and suppress this
  warning.

  Quoted variables like "LIBRARY_OUTPUT_PATH_ROOT" will no longer be
  dereferenced when the policy is set to NEW.  Since the policy is not set
  the OLD behavior will be used.
Call Stack (most recent call first):
  f:/CMake/share/cmake-3.1/Modules/CMakeDetermineSystem.cmake:95 (include)
  CMakeLists.txt:24 (project)
This warning is for project developers.  Use -Wno-dev to suppress it.

-- Looking for include file stdint.h
CMake Error at F:/Urho3D/Source/CMake/Toolchains/android.toolchain.cmake:723 (list):
  list sub-command REMOVE_DUPLICATES requires list to be present.
Call Stack (most recent call first):
  F:/Urho3D/Source/Android/CMakeFiles/3.1.0-rc3/CMakeSystem.cmake:6 (include)
  CMakeLists.txt:3 (project)

-- Configuring incomplete, errors occurred!
See also "F:/Urho3D/Source/Android/CMakeFiles/CMakeOutput.log".

CMake Error at F:/Urho3D/Source/CMake/Toolchains/android.toolchain.cmake:724 (list):
  list sub-command SORT requires list to be present.
Call Stack (most recent call first):
  F:/Urho3D/Source/Android/CMakeFiles/3.1.0-rc3/CMakeSystem.cmake:6 (include)
  CMakeLists.txt:3 (project)


CMake Error at F:/Urho3D/Source/CMake/Toolchains/android.toolchain.cmake:730 (message):
  No one of known Android ABIs is supported by this cmake toolchain.
Call Stack (most recent call first):
  F:/Urho3D/Source/Android/CMakeFiles/3.1.0-rc3/CMakeSystem.cmake:6 (include)
  CMakeLists.txt:3 (project)


CMake Error: CMAKE_C_COMPILER not set, after EnableLanguage
CMake Error: Internal CMake error, TryCompile configure of cmake failed[/spoiler]

[b]f:\Urho3D\Source\Android\CMakeFiles\CMakeOutput.log[/b]

The target system is: Linux - 1 - armv7-a
The host system is: Windows - 6.1 - AMD64


[b]Output for android list targets[/b]

[spoiler]F:\Urho3D>android list targets
Available Android targets:
----------
id: 1 or "android-16"
     Name: Android 4.1.2
     Type: Platform
     API level: 16
     Revision: 5
     Skins: HVGA, QVGA, WQVGA400, WQVGA432, WSVGA, WVGA800 (default), WVGA854, WXGA720, WXGA800, WXGA800-7in
 Tag/ABIs : default/armeabi-v7a
----------
id: 2 or "android-21"
     Name: Android 5.0.1
     Type: Platform
     API level: 21
     Revision: 2
     Skins: HVGA, QVGA, WQVGA400, WQVGA432, WSVGA, WVGA800 (default), WVGA854, WXGA720, WXGA800, WXGA800-7in
 Tag/ABIs : no ABIs.
----------
id: 3 or "Google Inc.:Google APIs:21"
     Name: Google APIs
     Type: Add-On
     Vendor: Google Inc.
     Revision: 1
     Description: Android + Google APIs
     Based on Android 5.0.1 (API level 21)
     Libraries:
      * com.google.android.media.effects (effects.jar)
          Collection of video effects
      * com.android.future.usb.accessory (usb.jar)
          API for USB Accessories
      * com.google.android.maps (maps.jar)
          API for Google Maps
     Skins: HVGA, QVGA, WQVGA400, WQVGA432, WSVGA, WVGA800 (default), WVGA854, WXGA720, WXGA800, WXGA800-7in
 Tag/ABIs : google_apis/x86[/spoiler]

my path is:

...
f:\CMake\bin;
f:\android-ndk-r10d\;
e:\Android\sdk\;
e:\Android\sdk\tools;
e:\Android\sdk\platform-tools;
e:\Android\sdk\build-tools;
f:\android-ndk-r10d\prebuilt\windows\bin\;
f:\apache-ant-1.9.4\bin\;

-------------------------

alexrass | 2017-01-02 01:01:56 UTC | #5

[quote="hd_"]Between steps 4 and 5, you might need:
[quote]android update project -p . -t 1 (only needed on the first time, replace '-t 1' with desired target-id)[/quote]
([urho3d.github.io/documentation/1 ... lding.html](http://urho3d.github.io/documentation/1.32/_building.html))

You can see which targets you have with:
[quote]android list targets[/quote][/quote]

Thanks, missed.
[b]sin[/b]
There may be several compiler in path and cmake does not know what to choose

-------------------------

cin | 2017-01-02 01:01:56 UTC | #6

For first step I user CMake GUI:

[url=http://i.imgur.com/a3lV0AB.png][img]http://i.imgur.com/a3lV0ABs.jpg[/img][/url]  

[b]F:\Urho3D\android-Build>make -j4[/b]
[code]
[  6%] "Built target Box2D"
[  7%] "Built target Civetweb"
[ 13%] "Built target FreeType"
[ 13%] "Built target JO"
[ 13%] "Built target LZ4"
[ 13%] "Built target PugiXml"
[ 13%] Building C object ThirdParty/SDL/CMakeFiles/SDL.dir/src/audio/directsound/SDL_directsound.c.obj
In file included from F:/Urho3D/Source/ThirdParty/SDL/src/audio/directsound/SDL_directsound.h:26:0,
                 from F:/Urho3D/Source/ThirdParty/SDL/src/audio/directsound/SDL_directsound.c:31:
F:/Urho3D/Source/ThirdParty/SDL/src/audio/directsound/directx.h:96:19: fatal error: ddraw.h: No such file or directory
 #include <ddraw.h>
                   ^
compilation terminated.
make[2]: *** [ThirdParty/SDL/CMakeFiles/SDL.dir/src/audio/directsound/SDL_directsound.c.obj] Error 1
make[1]: *** [ThirdParty/SDL/CMakeFiles/SDL.dir/all] Error 2
make: *** [all] Error 2
[/code]

-------------------------

weitjong | 2017-01-02 01:01:56 UTC | #7

I suggest you to retry again from scratch or at the very least perform a cmake_clean.bat first. Your last screenshot of cmake-gui already indicates to me that something is not quite right. How did the MinGW toolchain got into the picture? :slight_smile:

-------------------------

cin | 2017-01-02 01:01:56 UTC | #8

Yes. I select MinGW make files as compiler type.

I'm add check to see if ANDROID checkbox checked:
[url=http://i.imgur.com/Zbqtuic.png][img]http://i.imgur.com/Zbqtuics.jpg[/img][/url] 

Corrected Generator type selected - MinGW

[url=http://i.imgur.com/T5tqduX.png][img]http://i.imgur.com/T5tqduXs.jpg[/img][/url]  

But it always use Win32 (also after I check ANDROID checkbox and press Configure again)

-------------------------

weitjong | 2017-01-02 01:01:57 UTC | #9

No, you got it all wrong. Our CMake Android build does not work that way. To my understanding, CMake configures the compiler toolchain only once in the initial configuration step. No matter how many times you click on the Configure button in the GUI (or by running the CMake again in CLI to do reconfiguration), it will never be successful in changing the chosen compiler again that will be used for the project. For Android build, you will for sure required to use the Android toolchain provided by the NDK. The CMake generator can be "Unix Makefiles" or "Eclipse CDT 4 - Unix Makefiles" or even others, but the compiler must be set to use the one provided by Android NDK and never be MinGW compiler. To use the Android toolchain correctly, you must call cmake_android.bat on a clean build tree (just delete the old build tree if you are unsure). If you must use cmake-gui then make sure at the initial configuration step, you remember to choose the option "Specify toolchain file for cross-compiling" and select the android.toolchain.cmake in the next dialog window. Good luck.

-------------------------

cin | 2017-01-02 01:01:57 UTC | #10

Thanks, I select F:/Urho3D/Source/CMake/Toolchains/android.toolchain.cmake. But error.
[url=http://i.imgur.com/Ny4noJM.png][img]http://i.imgur.com/Ny4noJMs.jpg[/img][/url]     [url=http://i.imgur.com/ZwCWY7i.png][img]http://i.imgur.com/ZwCWY7is.jpg[/img][/url]

-------------------------

weitjong | 2017-01-02 01:01:57 UTC | #11

Getting closer. I see from the error that you are already using Android NDK r10d. You must use a matching android.toolchain.cmake file to use that bleeding edge version. We have just upgraded our toolchain file a few days ago in the master branch (commit 8b496896f2762d8313fcaab184c67daa7ac004ca). So, you must either git pull your master branch and use that master branch to do Android build OR copy that single file into whatever version you are currently using OR downgrade to NDK r10c. Note that Urho3D 1.32 release only supports up to Android NDK r10c.

-------------------------

