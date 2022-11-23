esak | 2017-01-02 01:04:20 UTC | #1

I'm new to both Urho3D and CMake. I downloaded the sources and ran cmake_vs2013.bat (with flags ?DURHO3D_SAMPLES=1 ?DURHO3D_LUA=1 -DURHO3D_64BIT=1 -DURHO3D_OPENGL=1).
I opened the generated Urho3D.sln and built the project ALL_BUILD. This completed successfully.
But then I wanted to look at the C++ samples, but I couldn't find any VS project files for these (I can only find the C++ source code).
Shouldn't there have been project files created for these also?

-------------------------

scorvi | 2017-01-02 01:04:20 UTC | #2

Welcome to Urho3D ^^

CMake creates your solution files in the same order and folder structure as it is defined in the cmake file. 
So to find your samples solution files you have to look at "Build/Source/Samples/03_Sprites", if Build is your specified cmake build folder ...

hmm can you see the samples projects when you open Urho3d.sln ?

-------------------------

friesencr | 2017-01-02 01:04:20 UTC | #3

Was this master or 1.32?

-------------------------

GoogleBot42 | 2017-01-02 01:04:20 UTC | #4

All of the binaries are put in one place.  If you are using 1.32 it will be in the project root under "bin" (or maybe "Bin" i forget) if you are using the head branch the build process has changed a lot (and for the better).  It will be in the build directory you specified under a subdirectory under "bin".   :wink: 

If not then either you messed something up or there is a bug.  :slight_smile:

-------------------------

esak | 2017-01-02 01:04:21 UTC | #5

I downloaded the source zip-file dated to 2015-03-20.
In my specified build-directory I can't find any samples (they exists though in the original directory-structure).
I also cannot find the samples in the generated Urho3D.sln.
Can this be a bug?

-------------------------

GoogleBot42 | 2017-01-02 01:04:21 UTC | #6

Still not sure what version you have (the date doesn't necessarily help).  Could you post the list of files in your project root directory?

For example if I use "ls -a" (I am on linux you would use "dir" in windows) in the command line I get this:
[code]./                    cmake_emscripten.sh*  cmake_vs2013.bat
../                   cmake_generic.bat     cmake_vs2015.bat
Android/              cmake_generic.sh*     Docs/
.bash_helpers.sh      cmake_ios.sh*         .git/
bin/                  CMakeLists.txt        .gitignore
Build-Linux64/        CMakeLists.txt.user   License.txt
CMake/                cmake_macosx.sh*      PurpleprintKit-1.0.1/
cmake_android.bat     cmake_mingw.bat       Rakefile
cmake_android.sh*     cmake_mingw.sh*       README.md
cmake_clean.bat       cmake_ninja.bat       Source/
cmake_clean.sh*       cmake_ninja.sh*       SourceAssets/
cmake_codeblocks.bat  cmake_rpi.sh*         .travis.yml
cmake_codeblocks.sh*  cmake_vs2008.bat
cmake_eclipse.sh*     cmake_vs2010.bat
cmake_emscripten.bat  cmake_vs2012.bat[/code]

I am using the HEAD version of Urho3D so some of the files have changed an the binaries are not in "bin" but are in "Build-Linux64" (a name I chose).  If you were to use 1.32 of Urho3D make sure you have downloaded the zip from [url]http://www.urho3d.org[/url] NOT from the github repository.

Here is a direct link to the download of 1.32: [url]https://github.com/urho3d/Urho3D/archive/1.32.zip[/url]  Make sure you are using this one or just post the contents of you Urho3D root directory and we will be able to figure exactly where the binaries are.  :wink:

-------------------------

weitjong | 2017-01-02 01:04:21 UTC | #7

Just want to drop by to say we are not affiliated with urho3d.org although it looks like whoever owns that domain is kind enough to redirect it to our main website at urho3d.github.io.

-------------------------

GoogleBot42 | 2017-01-02 01:04:22 UTC | #8

[quote="weitjong"]Just want to drop by to say we are not affiliated with urho3d.org although it looks like whoever owns that domain is kind enough to redirect it to our main website at urho3d.github.io.[/quote]

Interesting I didn't know that... I won't direct people to it then.  :slight_smile:

-------------------------

esak | 2017-01-02 01:04:23 UTC | #9

Previously I downloaded the zip-file from sourceforge, but now I downloaded the master.zip file from github and ran this command:
[code]cmake_vs2013.bat Build ?DURHO3D_SAMPLES=1 ?DURHO3D_LUA=1 -DURHO3D_64BIT=1 -DURHO3D_OPENGL=1[/code]

My directory content after this is the following:
[code]
[.]                    [..]                   .bash_helpers.sh
.gitignore             .travis.yml            [Android]
[bin]                  [Build]                [CMake]
CMakeLists.txt         cmake_android.bat      cmake_android.sh
cmake_clean.bat        cmake_clean.sh         cmake_codeblocks.bat
cmake_codeblocks.sh    cmake_eclipse.sh       cmake_emscripten.bat
cmake_emscripten.sh    cmake_generic.bat      cmake_generic.sh
cmake_ios.sh           cmake_macosx.sh        cmake_mingw.bat
cmake_mingw.sh         cmake_ninja.bat        cmake_ninja.sh
cmake_rpi.sh           cmake_vs2008.bat       cmake_vs2010.bat
cmake_vs2012.bat       cmake_vs2013.bat       cmake_vs2015.bat
[Docs]                 License.txt            Rakefile
README.md              [Source]               [SourceAssets]
[/code]

Under the Build directory I opened Urho3D.sln, set the build type to debug and x64. Then I built the project ALL_BUILD.
The directory content in the Build directory after this is as follows:
[code]
[.]                          [..]
ALL_BUILD.vcxproj            ALL_BUILD.vcxproj.filters
[bin]                        CMakeCache.txt
[CMakeFiles]                 cmake_install.cmake
CPackConfig.cmake            CPackSourceConfig.cmake
[Docs]                       [include]
INSTALL.vcxproj              INSTALL.vcxproj.filters
[lib]                        PACKAGE.vcxproj
PACKAGE.vcxproj.filters      [Source]
Urho3D.sdf                   Urho3D.sln
[x64]                        ZERO_CHECK.vcxproj
ZERO_CHECK.vcxproj.filters
[/code]

Under Build\bin Urho3DPlayer_d.exe was created and under the subfolder tool the various tools were built.
But no samples have been built and under Build\Source there are no samples.
So the result is basically the same as the first time I did the exact same thing.
Am I'm missing something here? Feeling pretty stupid right now....

-------------------------

GoogleBot42 | 2017-01-02 01:04:24 UTC | #10

[quote="esak"]Under Build\bin Urho3DPlayer_d.exe was created and under the subfolder tool the various tools were built.
But no samples have been built and under Build\Source there are no samples.
So the result is basically the same as the first time I did the exact same thing.
Am I'm missing something here? Feeling pretty stupid right now....[/quote]

Ok... that does seem odd.  I haven't ever built Urho3D on windows but I think all the binaries should be under that bin directory where the Urho3DPlayer is... hmmmm.  Is this a bug, or are binaries placed in a different spot on windows, or was there some mistake in building...

This is the output of my binary directory (linux):
[code]googlebot42@comp ~/Desktop/Urho3D/Build-Linux64/bin (git)-[master] % ls
01_HelloWorld*         17_SceneReplication*        33_Urho2DSpriterAnimation*
02_HelloGUI*           18_CharacterDemo*           34_DynamicGeometry*
03_Sprites*            19_VehicleDemo*             35_SignedDistanceFieldText*
04_StaticScene*        20_HugeObjectCount*         36_Urho2DTileMap*
05_AnimatingScene*     21_AngelScriptIntegration*  37_UIDrag*
06_SkeletalAnimation*  22_LuaIntegration*          38_SceneAndUILoad*
07_Billboards*         23_Water*                   CoreData@
08_Decals*             24_Urho2DSprite*            Data@
09_MultipleViewports*  25_Urho2DParticle*          Editor.sh@
10_RenderToTexture*    26_ConsoleInput*            jit/
11_Physics*            27_Urho2DPhysics*           luajit*
12_PhysicsStressTest*  28_Urho2DPhysicsRope*       NinjaSnowWar.sh@
13_Ragdolls*           29_SoundSynthesis*          tool/
14_SoundEffects*       30_LightAnimation*          Urho3DPlayer*
15_Navigation*         31_MaterialAnimation*
16_Chat*               32_Urho2DConstraints*
[/code]

EDIT: Here is the cmake command I used...
[code]./cmake_generic.sh Build-Linux64 -DURHO3D_LUA=1 -DURHO3D_LUAJIT=1 -DURHO3D_LUAJIT_AMALG=1 -DURHO3D_SAFE_LUA=1 -DURHO3D_SAMPLES=1 -DURHO3D_EXTRAS=1 -DURHO3D_DOCS=1[/code]

-------------------------

weitjong | 2017-01-02 01:04:24 UTC | #11

[quote="esak"]Previously I downloaded the zip-file from sourceforge, but now I downloaded the master.zip file from github and ran this command:
[code]cmake_vs2013.bat Build ?DURHO3D_SAMPLES=1 ?DURHO3D_LUA=1 -DURHO3D_64BIT=1 -DURHO3D_OPENGL=1[/code][/quote]
At first I really thought you were on to something that there is a bug because I could reproduce your problem on my Win7 test VM. However, in the end I find the actual root cause is just a simple encoding-error. The code you have posted above is not correct although it "looks" correct. Retyping the command again manually should work. On my Linux host system I could use Vim in Hex editor mode to observe the difference. The first line is copy-pasted from your post and the second is from retyping. If this is an April fool joke then you are too early. :smiley: 

[code]cmake_vs2013.bat Build ?DURHO3D_SAMPLES=1 ?DURHO3D_LUA=1 -DURHO3D_64BIT=1 -DURHO3D_OPENGL=1
cmake_vs2013.bat Build -DURHO3D_SAMPLES=1 -DURHO3D_LUA=1 -DURHO3D_64BIT=1 -DURHO3D_OPENGL=1

0000000: 636d 616b 655f 7673 3230 3133 2e62 6174  cmake_vs2013.bat
0000010: 2042 7569 6c64 20e2 8093 4455 5248 4f33   Build ...DURHO3
0000020: 445f 5341 4d50 4c45 533d 3120 e280 9344  D_SAMPLES=1 ...D
0000030: 5552 484f 3344 5f4c 5541 3d31 202d 4455  URHO3D_LUA=1 -DU
0000040: 5248 4f33 445f 3634 4249 543d 3120 2d44  RHO3D_64BIT=1 -D
0000050: 5552 484f 3344 5f4f 5045 4e47 4c3d 310a  URHO3D_OPENGL=1.
0000060: 636d 616b 655f 7673 3230 3133 2e62 6174  cmake_vs2013.bat
0000070: 2042 7569 6c64 202d 4455 5248 4f33 445f   Build -DURHO3D_
0000080: 5341 4d50 4c45 533d 3120 2d44 5552 484f  SAMPLES=1 -DURHO
0000090: 3344 5f4c 5541 3d31 202d 4455 5248 4f33  3D_LUA=1 -DURHO3
00000a0: 445f 3634 4249 543d 3120 2d44 5552 484f  D_64BIT=1 -DURHO
00000b0: 3344 5f4f 5045 4e47 4c3d 310a            3D_OPENGL=1.[/code]

-------------------------

esak | 2017-01-02 01:04:25 UTC | #12

Retyping the command did the trick!
Sorry for the trouble I caused.  :frowning:  Feeling a little stupid...
(In my defence... I had copied part of the command from a web-page.)

-------------------------

GoogleBot42 | 2017-01-02 01:04:25 UTC | #13

[quote="esak"]Retyping the command did the trick!
Sorry for the trouble I caused. :frowning: Feeling a little stupid...
(In my defence... I had copied part of the command from a web-page.)[/quote]

It wasn't a stupid question.  :wink:   If it was it wouldn't have taken so long to answer.  Now the question has been answered for someone else.  :slight_smile:

-------------------------

