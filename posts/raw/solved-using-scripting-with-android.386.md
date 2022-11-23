zakk | 2017-01-02 01:00:02 UTC | #1

Hello,

I'm wondering how to use [b]Urho3DPlayer[/b] with [b]Android,[/b].

On X86_64 platform, you get an Urho3DPlayer executable, which can launch samples written in Lua or AngelScript.
Fine, just what i'd like to have on Android platform.

I've built Android libs (both shared and static), and also the Urho3DPlayer.
After the build, i got [i]libUrho3DPlayer.so[/i]  (in Urho3D/android-Buildlibs/armeabi-v7a/ ), but no executable.

Does it means that for Android, I must write C++ code for launching Urho3DPlayer, and calling my ?main.lua? script ?

As all the Android samples are compiled as a shared lib, i guess there's a trick somewhere. May be they have to be called from the ?base? Java class, which launch everything else ?

If someone can explain, or give me a link to the documentation? i've made a search in this forum with ?Urho3DPlayer? but found nothing related.

Thank you.

-------------------------

weitjong | 2017-01-02 01:00:02 UTC | #2

It seems that this is one of the FAQ for Android. The instruction is in [urho3d.github.io/documentation/_ ... ng_Android](http://urho3d.github.io/documentation/_building.html#Building_Android). After the build (make step), all you get is shared libraries. After the ant step, only then you get the *.apk which can be deployed.

-------------------------

zakk | 2017-01-02 01:00:02 UTC | #3

Yes, i've read the link about apk generation.

But i'm talking about steps which are at the very beginning.

Let's take an example, it will be easier for me to explain my problem.

Let's say i want to adapt [i]01_HelloWorld.lua[/i], which can be found in [i]$URHO_ROOT/Bin/Data/LuaScripts/[/i]

I'm doing it step by step, like this, it will be easier to follow and correct my errors.

First, i need to define an environment for my project:

[code]

~/sources$ mkdir hello_droid #my project

~/sources$ cd Urho3D/ #go to root of Urho3D sources.

~/sources/Urho3D$ rake scaffolding dir=~/sources/hello_droid/

~/sources/Urho3D$ export URHO3D_HOME=$PWD

~/sources/Urho3D$ cd ../hello_droid

~/sources/hello_droid$ ls
[Bin]  cmake_clean.sh  cmake_codeblocks.sh  cmake_eclipse.sh  cmake_gcc.sh  cmake_ios.sh  cmake_macosx.sh  [Source]

~/sources/hello_droid$ ./cmake_gcc.sh -DURHO3D_64BIT=1 -DURHO3D_LUA=1

Android build
================================================================================
-- Found Urho3D: /home/zakk/sources/Urho3D/android-Build/libs/armeabi-v7a/libUrho3D.a
-- Configuring done
-- Generating done
-- Build files have been written to: /home/zakk/sources/hello_droid/android-Build

Native build
================================================================================
-- The C compiler identification is GNU 4.9.0
-- The CXX compiler identification is GNU 4.9.0
-- Check for working C compiler: /usr/lib/colorgcc/bin/cc
-- Check for working C compiler: /usr/lib/colorgcc/bin/cc -- works
-- Detecting C compiler ABI info
-- Detecting C compiler ABI info - done
-- Check for working CXX compiler: /usr/lib/colorgcc/bin/c++
-- Check for working CXX compiler: /usr/lib/colorgcc/bin/c++ -- works
-- Detecting CXX compiler ABI info
-- Detecting CXX compiler ABI info - done
-- Found Urho3D: /home/zakk/sources/Urho3D/Lib/libUrho3D.so
-- Configuring done
-- Generating done
-- Build files have been written to: /home/zakk/sources/hello_droid/Build
failed to create symbolic link 'Source/Android/assets/CoreData': No such file or directory
failed to create symbolic link 'Source/Android/assets/Data': No such file or directory

[/code]

Some broken links? some corrections by hand?

[code]

~/sources/hello_droid/Source$ ln -s ../../Urho3D/Source/Android/ Android

[/code]

Ok, no broken links anymore.

[code]

~/sources/hello_droid/android-Build$ android update project -p . -t 1
Updated and renamed default.properties to project.properties
Updated local.properties
Added file ./proguard-project.txt

~/sources/hello_droid/android-Build$ make -j 5
Scanning dependencies of target Main
[ 50%] [100%] Building CXX object CMakeFiles/Main.dir/Urho3DPlayer.cpp.o
Building C object CMakeFiles/Main.dir/home/zakk/sources/Urho3D/Source/ThirdParty/SDL/src/main/android/SDL_android_main.c.o
Linking CXX shared library libs/armeabi-v7a/libMain.so
Stripping libMain.so in library output directory

~/sources/hello_droid/android-Build$ find -iname "*.so"
./libs/armeabi-v7a/libMain.so

[/code]


And now ? I don't even get [i]libUrho3DPlayer.so[/i]
As it's compiled in the Urho3D git repository, i could copy it in [i]~/sources/hello_droid/android-Build/libs[/i].

But after ? What should i do before the final [b]ant debug[/b] ?
I guess i have at least two more things to do:
1) Putting my Lua scripts in the file hierarchy.
2) And perhaps, modify something in the java JNI ?

Thank you :slight_smile:

-------------------------

Mike | 2017-01-02 01:00:02 UTC | #4

Complimentary documentation is at [url]http://urho3d.github.io/documentation/_running.html[/url].

-------------------------

weitjong | 2017-01-02 01:00:02 UTC | #5

I see. I thought you were asking for how to get Android 'executable'. The Android build process could be better documented. You are welcome to contribute to update the page after you have succeeded :wink: .

The "rake scaffolding" as its name implies, just creates a basic project structure for your new project. You may also pass optional "project" and "target" parameters besides the "dir" parameter. Otherwise, you will get the default project name (Scaffolding) and target name (Main). The latter is why you get "libMain.so". You can name your target anything you like other than Urho3DPlayer and still be able to run Lua or AngelScript scripts. The ability to do that comes from the C++ source code, not from its name. The C++ source code is in "hello_droid/Source". Notice that "rake scaffolding" simply copies the Urho3DPlayer.cpp and Urho3DPlayer.h there as placeholders. Normally, you should replace these two files with your own project source files. But for you case, you can leave them because that is exactly what you want.

Regarding the broken symlinks, they are kind of intentional. The "rake scaffolding" does not do what you did because your project should have your own "hello_droid/Source/Android" directory with its own manifest file, assets, resources, etc. But arguably, we could enhance "rake scaffolding" to put some placeholders there than leave them missing as currently.

For playing Lua scripts, the scripts need to be put in the "hello_droid/Bin/Data/LuaScripts" directory. If you intent to keep Urho3DPlayer.cpp instead of writing your own code then you better peek into its content. At line 56-57, you would see it uses an external file called "Data/CommandLine.txt" to determine which script to run as entry point. By default, it plays our famous Ninja Snow War using AngelScript. So, obviously your next step is to change the content of that file.

HTH

-------------------------

zakk | 2017-01-02 01:00:03 UTC | #6

At first, thanks for your replies. Reading them carefully, i go further little by little. :slight_smile:

This time, i tried to package ?01_HelloWorld.lua?.

I won't maintain the suspense, the build was ok. BUT when i install the APK and launch it on emulator or real device, all i get is ?no activities? message, with the Urho3D Logo.

I put it here the whole build process. I'm waiting for your comments.

May be, there are things which are not mandatory, or that i could do in a better way.

That said, it's time to begin.


At the very beginning, i launch [b]rake[/b], with only the [i]dir[/i] parameter. I want to keep the default name, for avoiding class mismatch during the build.

[code]

 /  [master] ~/sources/Urho3D$ rake scaffolding dir=~/coding/libs/multimedia/urho3d/test_droid/ project=test_droid

New project created in /home/zakk/coding/libs/multimedia/urho3d/test_droid

[/code]


While i'm here, i export immediatly [i]URHO3D_HOME[/i]


[code]

 /  [master] ~/sources/Urho3D$ export URHO3D_HOME=$PWD

[/code]


Now, i go to my project directory, and copy the toolchain for Android.

[code]

 /  ~/coding/libs/multimedia/urho3d/test_droid$ mkdir -p Source/CMake/ToolChains
 /  ~/coding/libs/multimedia/urho3d/test_droid$ cp ~/sources/Urho3D/Source/CMake/Toolchains/android.toolchain.cmake Source/CMake/ToolChains/

[/code]


And generate CMake files with [i]cmake_gcc.sh[/i]

[code]

 /  ~/coding/libs/multimedia/urho3d/test_droid$ ./cmake_gcc.sh

[/code]


Now it's time to compile the Urho's player

[code]

 /  ~/coding/libs/multimedia/urho3d/test_droid/android-Build$ make
Scanning dependencies of target Main
(?)
[100%] Built target Main

[/code]

Look, it's here!

[code]

 /  ~/coding/libs/multimedia/urho3d/test_droid/android-Build$ ls libs/ -Rlh
libs/:
total 4,0K
drwxr-xr-x 2 zakk zakk 4,0K 13 ao?t  20:56 armeabi-v7a

libs/armeabi-v7a:
total 6,1M
-rwxr-xr-x 1 zakk zakk 6,1M 13 ao?t  20:56 libMain.so

[/code]

I go to the sources, and create Android subdirectory. Then, i put the [i]AndroidManifest.xml[/i] here. I also copy the Java sources. And [i]res/[/i] subdirectory. I don't know what is the purpose of res/ , but it seems to be mandatory in the packaging step.

[code]

 /  ~/coding/libs/multimedia/urho3d/test_droid/Source$ mkdir Android

(and copy AndroidManifest.xml here, and res/ and then java JNI sources)

[/code]


Look, everybody is here. I didn't include [i]assets[/i] directory, as i will directly put the assets in [i]Bin[/i] directory. So, what do we have in [i]Source/Android[/i] ?

[code]

 /  ~/coding/libs/multimedia/urho3d/test_droid/Source/Android$ tree
.
??? AndroidManifest.xml
??? build.xml
??? res
??? ??? drawable
??? ??? ??? logo_large.png
??? ??? drawable-hdpi
??? ??? ??? icon.png
??? ??? drawable-ldpi
??? ??? ??? icon.png
??? ??? drawable-mdpi
??? ??? ??? icon.png
??? ??? layout
??? ??? ??? samples_list_text_view.xml
??? ??? ??? samples_list.xml
??? ??? values
???     ??? strings.xml
??? src
    ??? com
    ??? ??? github
    ???     ??? urho3d
    ???         ??? SampleLauncher.java
    ???         ??? Urho3D.java
    ??? org
        ??? libsdl
            ??? app
                ??? SDLActivity.java

14 directories, 12 files

[/code]


I also put mandatory files in Bin directory. With only those one, [i]01_HelloWorld.lua[/i] must run.

[code]

 /  ~/coding/libs/multimedia/urho3d/test_droid/Bin$ tree
.
??? CoreData
??? ??? Shaders
???     ??? GLSL
???         ??? Basic.glsl
???         ??? Samplers.glsl
???         ??? Transform.glsl
???         ??? Uniforms.glsl
??? Data
    ??? CommandLine.txt
    ??? Fonts
    ??? ??? Anonymous Pro.ttf
    ??? LuaScripts
    ??? ??? 01_HelloWorld.lua
    ??? ??? Utilities
    ???     ??? Network.lua
    ???     ??? Sample.lua
    ???     ??? ScriptCompiler.lua
    ???     ??? Touch.lua
    ??? Textures
    ??? ??? UI.png
    ??? UI
        ??? DefaultStyle.xml

9 directories, 13 files

[/code]


Now, the final takes place in [i]android-Build[/i].
[b]android update project[/b] for generating with [i]AndroidManifest.xml[/i] some files needed (Gee, that's something!)

[code]

 /  ~/coding/libs/multimedia/urho3d/test_droid/android-Build$ android update project -p . -t 1
Updated and renamed default.properties to project.properties
Updated local.properties
Added file ./proguard-project.txt

[/code]

And finally, i launch the (in)famous [b]ant debug[/b]

[code]

 /  ~/coding/libs/multimedia/urho3d/test_droid/android-Build$ ant debug
Buildfile: /home/zakk/coding/libs/multimedia/urho3d/test_droid/android-Build/build.xml

-set-mode-check:

-set-debug-files:

-check-env:
 [checkenv] Android SDK Tools Revision 22.0.5
 [checkenv] Installed at /opt/android-sdk

-setup:
     [echo] Project Name: Urho3D
  [gettype] Project Type: Application

-set-debug-mode:

-debug-obfuscation-check:

-pre-build:

-build-setup:
[getbuildtools] Using latest Build Tools: 18.0.1
     [echo] Resolving Build Target for Urho3D...
[gettarget] Project Target:   Android 4.2.2
[dependency] Library dependencies:
[dependency] No Libraries
     [echo] ----------
     [echo] Building Libraries with 'debug'...
   [subant] No sub-builds to iterate on

-code-gen:
[mergemanifest] No changes in the AndroidManifest files.
     [echo] Handling aidl files...
     [aidl] No AIDL files to compile.
     [echo] ----------
     [echo] Handling RenderScript files...
[renderscript] No RenderScript files to compile.
     [echo] ----------
     [echo] Handling Resources...
     [aapt] Generating resource IDs...
     [echo] ----------
     [echo] Handling BuildConfig class...
[buildconfig] Generating BuildConfig class.

-pre-compile:

-compile:
    [javac] Compiling 5 source files to /home/zakk/coding/libs/multimedia/urho3d/test_droid/android-Build/bin/classes
    [javac] Note: /home/zakk/coding/libs/multimedia/urho3d/test_droid/android-Build/src/org/libsdl/app/SDLActivity.java uses or overrides a deprecated API.
    [javac] Note: Recompile with -Xlint:deprecation for details.

-post-compile:

-obfuscate:

-dex:
      [dex] input: /home/zakk/coding/libs/multimedia/urho3d/test_droid/android-Build/bin/classes
      [dex] Converting compiled files and external libraries into /home/zakk/coding/libs/multimedia/urho3d/test_droid/android-Build/bin/classes.dex...

-crunch:
   [crunch] Crunching PNG Files in source dir: /home/zakk/coding/libs/multimedia/urho3d/test_droid/android-Build/res
   [crunch] To destination dir: /home/zakk/coding/libs/multimedia/urho3d/test_droid/android-Build/bin/res
   [crunch] Processing image to cache: /home/zakk/coding/libs/multimedia/urho3d/test_droid/android-Build/res/drawable-hdpi/icon.png => /home/zakk/coding/libs/multimedia/urho3d/test_droid/android-Build/bin/res/drawable-hdpi/icon.png
   [crunch]   (processed image to cache entry /home/zakk/coding/libs/multimedia/urho3d/test_droid/android-Build/bin/res/drawable-hdpi/icon.png: 54% size of source)
   [crunch] Processing image to cache: /home/zakk/coding/libs/multimedia/urho3d/test_droid/android-Build/res/drawable-ldpi/icon.png => /home/zakk/coding/libs/multimedia/urho3d/test_droid/android-Build/bin/res/drawable-ldpi/icon.png
   [crunch]   (processed image to cache entry /home/zakk/coding/libs/multimedia/urho3d/test_droid/android-Build/bin/res/drawable-ldpi/icon.png: 0% size of source)
   [crunch] Processing image to cache: /home/zakk/coding/libs/multimedia/urho3d/test_droid/android-Build/res/drawable-mdpi/icon.png => /home/zakk/coding/libs/multimedia/urho3d/test_droid/android-Build/bin/res/drawable-mdpi/icon.png
   [crunch]   (processed image to cache entry /home/zakk/coding/libs/multimedia/urho3d/test_droid/android-Build/bin/res/drawable-mdpi/icon.png: 59% size of source)
   [crunch] Processing image to cache: /home/zakk/coding/libs/multimedia/urho3d/test_droid/android-Build/res/drawable/logo_large.png => /home/zakk/coding/libs/multimedia/urho3d/test_droid/android-Build/bin/res/drawable/logo_large.png
   [crunch]   (processed image to cache entry /home/zakk/coding/libs/multimedia/urho3d/test_droid/android-Build/bin/res/drawable/logo_large.png: 92% size of source)
   [crunch] Crunched 4 PNG files to update cache

-package-resources:
     [aapt] Creating full resource package...

-package:
[apkbuilder] Current build type is different than previous build: forced apkbuilder run.
[apkbuilder] Creating Urho3D-debug-unaligned.apk and signing it with a debug key...

-post-package:

-do-debug:
 [zipalign] Running zip align on final apk...
     [echo] Debug Package: /home/zakk/coding/libs/multimedia/urho3d/test_droid/android-Build/bin/Urho3D-debug.apk
[propertyfile] Creating new property file: /home/zakk/coding/libs/multimedia/urho3d/test_droid/android-Build/bin/build.prop
[propertyfile] Updating property file: /home/zakk/coding/libs/multimedia/urho3d/test_droid/android-Build/bin/build.prop
[propertyfile] Updating property file: /home/zakk/coding/libs/multimedia/urho3d/test_droid/android-Build/bin/build.prop
[propertyfile] Updating property file: /home/zakk/coding/libs/multimedia/urho3d/test_droid/android-Build/bin/build.prop

-post-build:

debug:

BUILD SUCCESSFUL
Total time: 3 seconds

[/code]


[b]BUILD SUCCESSFUL[/b] !

But there's still to do, for example, succeed in running it on Android device :slight_smile:

-------------------------

weitjong | 2017-01-02 01:00:03 UTC | #7

You need to include "assets" directory. The "Android" sub-directory structure is not determined by Urho3D but by Google. Read this [developer.android.com/tools/projects/index.html](http://developer.android.com/tools/projects/index.html), if you have not done so.
For this case, you can make a symlink for the "assets" directory to point to "Bin" directory. Whatever you do, when performing "ls assets" it should output "CoreData" and "Data" at the minimal.

You may also want to use adb logcat to view the log to see why your app does not run. Alternatively, use Android IDE such as Eclipse.

-------------------------

zakk | 2017-01-02 01:00:06 UTC | #8

Hello, thank to the advices and hints given here, i've managed to sort out Android apk generation.

I'd like to add this to the wiki, but? where is the wiki ?
The closest subject i've found is the building instructions:
[urho3d.github.io/documentation/H ... lding.html](http://urho3d.github.io/documentation/HEAD/_building.html)

So, i post in this topic for the moment.

All instructions are for Linux environment.


[size=200]Android: building your own Urho3DPlayer package[/size]

We want to use Urho3DPlayer on Android, for AngelScript or Lua execution.

Before all, you will need to build the Urho3D library for Android.
This part is well explained in Urho3D documentation (short version: use [i]cmake_gcc.sh[/i]).

We are going to use the first Lua demo ([i]01_HelloWorld.lua[/i]).

As it's just for packaging demo purpose, the simpler, the better.




[size=150]Preparing project files and directories[/size]

At first, create a new directory for hosting all the needed files.

[code]

~/projects/urho3d$ mkdir hello_droid

[/code]

Now go to the root of Urho3D sources.

We are using ?rake? tool for generating a blank project.

[code]

Usage: rake scaffolding dir=/path/to/new/project/root [project=your-project-name] [target=your-target-name]' unless ENV['dir']

[/code]

Default paramters, if nothing given on command-line:
  project = ENV['project'] || 'Scaffolding'
  target = ENV['target'] || 'Main'

Quoting Weitjong:
[i]
Notice that "rake scaffolding" simply copies the Urho3DPlayer.cpp and
Urho3DPlayer.h there as placeholders. Normally, you should replace these two
files with your own project source files. But for you case, you can leave them
because that is exactly what you want.
[/i]


[code]

~/sources/Urho3D$ rake scaffolding dir=~/projects/urho3d/hello_droid/ project=hello_my_droid

New project created in /home/zakk/projects/urho3d/hello_droid

To build the new project, you may need to first define and export either 'URHO3D_HOME' or 'CMAKE_PREFIX_PATH' environment variable
Please see http://urho3d.github.io/documentation/_using_library.html for more detail. For example:

$ URHO3D_HOME=/home/zakk/sources/Urho3D; export URHO3D_HOME
$ cd /home/zakk/projects/urho3d/hello_droid
$ ./cmake_gcc.sh -DURHO3D_64BIT=1 -DURHO3D_LUAJIT=1
$ cd Build
$ make

[/code]

Let's go back in our project's location:

[code]

~/projects/urho3d/hello_droid$ export URHO3D_HOME=/home/zakk/sources/Urho3D
~/projects/urho3d/hello_droid$ ./cmake_gcc.sh -DURHO3D_LUA=1

[/code]

At the end of [i]cmake_gcc.sh[/i] execution, you will see:

failed to create symbolic link 'Source/Android/assets/CoreData': No such file or directory
failed to create symbolic link 'Source/Android/assets/Data': No such file or directory

That's okay. It's your duty to fill Source with code and data.




[size=150]Filling Source/Android[/size]

Well let's begin with creating ?Android? in the Source directory.
After that, some cleaning in ?Bin?: I choose to erase the symlinks to [i]CoreData[/i] and [i]Data[/i] (point to the Urho3D sources). [i]CoreData[/i] and [i]Data[/i] will be put directly in Android/assets, as ?true? directories.

Cleaning [i]Bin[/i]:

[code]

~/projects/urho3d/hello_droid/Bin$ rm CoreData
~/projects/urho3d/hello_droid/Bin$ rm Data

[/code]

Populating [i]Source[/i] directory:

[code]

~/projects/urho3d/hello_droid/Source$ mkdir Android
~/projects/urho3d/hello_droid/Source$ mkdir Android/assets
~/projects/urho3d/hello_droid/Source$ mkdir Android/assets/CoreData
~/projects/urho3d/hello_droid/Source$ mkdir Android/assets/Data
~/projects/urho3d/hello_droid/Source$ mkdir Android/res
~/projects/urho3d/hello_droid/Source$ mkdir Android/src

[/code]

I've copied the whole content of:
[i] ~/sources/Urho3D/Source/Android/res[/i]
[i] ~/sources/Urho3D/Source/Android/src[/i]
in [i]res[/i] and [i]src[/i] of [i]hello_droid[/i].

[b]res/[/b] : contains icons and paramaters (app behaviour, app name?).
[b]src/[/b] : Java sources used for doing the link with the NDK (the JNI).
[b]assets/[/b] : all that's related with Urho3D (Lua scripts, data).

What to put in ?assets? ?
Scripts must go to [i]Data/LuaScripts[/i].

You must also modify [i]Data/CommandLine.txt[/i], for putting name and location of the script to launch with Urho3DPlayer.

[code]

~/projects/urho3d/hello_droid/Bin$ cat Source/Android/assets/Data/CommandLine.txt
LuaScripts/01_HelloWorld.lua

[/code]

You have to create or copy (which is easier) the file [i]AndroidManifest.xml[/i].
Its purpose is to be used as config file for [i]ant[/i]. It's a sort of Makefile generator.
Put it at the root of Android's sources.

Now, we have:

[code]

~/projects/urho3d/hello_droid$ ls -1FX Source/Android/
assets/
res/
src/
AndroidManifest.xml

[/code]




[size=150]Creating ant environment[/size]

[code]

 ~/projects/urho3d/hello_droid/android-Build$ android update project -p . -t 1
Updated and renamed default.properties to project.properties
Updated local.properties
Added file ./proguard-project.txt

[/code]

[i]android update project[/i] will be necessary only one time.
Note that you must redo this operation if [i]AndroidManifest.xml[/i] is modified.

For changing the APK filename:
Change first line of [i]build.xml[/i] :
<project name="SampleLauncher" default="help">
it becomes :
<project name="hello_droid" default="help">

This will only change the APK filename. The name of the application (as seen on your phone screen) won't be changed.
Neither will the unique name of the package. See the name with [i]adb shell pm list packages -3[/i]. By default, it's [b]com.github.urho3d[/b].

Now that we have everything configurated, we can build the Uhro player, and generating the package.




[size=150]Building Urho3DPlayer[/size]

[code]

 ~/projects/urho3d/hello_droid/android-Build$ make
Scanning dependencies of target Main
[ 50%] Building CXX object CMakeFiles/Main.dir/Urho3DPlayer.cpp.o
[100%] Building C object CMakeFiles/Main.dir/home/zakk/sources/Urho3D/Source/ThirdParty/SDL/src/main/android/SDL_android_main.c.o
Linking CXX shared library libs/armeabi-v7a/libMain.so
Stripping libMain.so in library output directory
[100%] Built target Main

~/projects/urho3d/hello_droid/android-Build$ ls libs/armeabi-v7a/libMain.so -lh
-rwxr-xr-x 1 zakk zakk 6,8M 17 ao?t  20:18 libs/armeabi-v7a/libMain.so

[/code]




[size=150]Creating the APK[/size]

[code]

~/projects/urho3d/hello_droid/android-Build$ ant debug

[/code]

Now, we can send the package to an emulator, or an android-phone.

[code]

~/projects/urho3d/hello_droid/android-Build$ adb install -r bin/hello_droid-debug.apk
3595 KB/s (3446988 bytes in 0.936s)
        pkg: /data/local/tmp/hello_droid-debug.apk
Success

[/code]

For getting logs, and solve more easily the problems which will rise for sure:

[code]

$ adb logcat -c # just before launching your app. It cleans the logs.
$ adb logcat    # then, launch your app.

[/code]


Well, i hope that it will help somebody. I had myself serious troubles figuring out how to create an APK with Urho3D scripts. WIth that, it should be easier for you  :smiley:

-------------------------

weitjong | 2017-01-02 01:00:06 UTC | #9

Thanks for contributing back to the community. Our Wiki page on GitHub has been disabled temporarily because lack of good content in the past. If we have more content such as this one then we can propose to reenable it.

-------------------------

friesencr | 2017-01-02 01:00:06 UTC | #10

We can just as easily start a community wiki.  The Urho3D engine codebase is very well kept up and has high standards.  There is also an implicit expectation that it is maintained.  I would think a community wiki could have a similar result without adding further burdon to urho devs.

-------------------------

