vivienneanthony | 2017-01-02 01:04:22 UTC | #1

Hi

I'm trying to compile Scorvi IDE but I first attempted to download the new master. I'm getting this error [b]"An error has occured, build tree has to be provided as the first argument OR call this script in a build tree itself"[/b] when I do a ./cmake_clean.sh. Usually, I do that command and ./cmake_codeblocks.sh to make the codeblock project.

[code]total 200
drwxrwxr-x 5 vivienne vivienne  4096 Mar 22 21:30 Android
drwxrwxr-x 4 vivienne vivienne  4096 Mar 23 22:03 bin
drwxrwxr-x 4 vivienne vivienne  4096 Mar 22 21:30 CMake
-rw-rw-r-- 1 vivienne vivienne  1169 Mar 22 21:30 cmake_android.bat
-rwxr-xr-x 1 vivienne vivienne  1206 Mar 22 21:30 cmake_android.sh
-rw-rw-r-- 1 vivienne vivienne  1644 Mar 22 21:30 cmake_clean.bat
-rwxr-xr-x 1 vivienne vivienne  1553 Mar 22 21:30 cmake_clean.sh
-rw-rw-r-- 1 vivienne vivienne  1191 Mar 22 21:30 cmake_codeblocks.bat
-rwxr-xr-x 1 vivienne vivienne  1227 Mar 22 21:30 cmake_codeblocks.sh
-rwxr-xr-x 1 vivienne vivienne  1493 Mar 22 21:30 cmake_eclipse.sh
-rw-rw-r-- 1 vivienne vivienne  1172 Mar 22 21:30 cmake_emscripten.bat
-rwxr-xr-x 1 vivienne vivienne  1209 Mar 22 21:30 cmake_emscripten.sh
-rw-rw-r-- 1 vivienne vivienne  2870 Mar 22 21:30 cmake_generic.bat
-rwxr-xr-x 1 vivienne vivienne  2986 Mar 22 21:30 cmake_generic.sh
-rwxr-xr-x 1 vivienne vivienne  1201 Mar 22 21:30 cmake_ios.sh
-rw-rw-r-- 1 vivienne vivienne  7872 Mar 22 21:30 CMakeLists.txt
-rwxr-xr-x 1 vivienne vivienne  1203 Mar 22 21:30 cmake_macosx.sh
-rw-rw-r-- 1 vivienne vivienne  1178 Mar 22 21:30 cmake_mingw.bat
-rwxr-xr-x 1 vivienne vivienne  1204 Mar 22 21:30 cmake_mingw.sh
-rw-rw-r-- 1 vivienne vivienne  1168 Mar 22 21:30 cmake_ninja.bat
-rwxr-xr-x 1 vivienne vivienne  1205 Mar 22 21:30 cmake_ninja.sh
-rwxr-xr-x 1 vivienne vivienne  1202 Mar 22 21:30 cmake_rpi.sh
-rw-rw-r-- 1 vivienne vivienne  1170 Mar 22 21:30 cmake_vs2008.bat
-rw-rw-r-- 1 vivienne vivienne  1164 Mar 22 21:30 cmake_vs2010.bat
-rw-rw-r-- 1 vivienne vivienne  1164 Mar 22 21:30 cmake_vs2012.bat
-rw-rw-r-- 1 vivienne vivienne  1164 Mar 22 21:30 cmake_vs2013.bat
-rw-rw-r-- 1 vivienne vivienne  1164 Mar 22 21:30 cmake_vs2015.bat
drwxrwxr-x 2 vivienne vivienne  4096 Mar 22 21:30 Docs
-rw-rw-r-- 1 vivienne vivienne 26911 Mar 22 21:30 License.txt
-rw-rw-r-- 1 vivienne vivienne 40238 Mar 22 21:30 Rakefile
-rw-rw-r-- 1 vivienne vivienne  5201 Mar 22 21:30 README.md
drwxrwxr-x 7 vivienne vivienne  4096 Mar 23 22:04 Source
drwxrwxr-x 2 vivienne vivienne  4096 Mar 22 21:30 SourceAssets
vivienne@vivienne-System-Product-Name:/media/home2/vivienne/Urho3D-mastercurrent$ ./cmake_clean.sh
An error has occured, build tree has to be provided as the first argument OR call this script in a build tree itself
vivienne@vivienne-System-Product-Name:/media/home2/vivienne/Urho3D-mastercurrent$ 
[/code]

Also, doing cmake_codeblocks.sh produces this result

[code]vivienne@vivienne-System-Product-Name:/media/home2/vivienne/Urho3DIDE-master$ sudo ./cmake_codeblocks.sh
./cmake_gcc.sh: line 29: ./.bash_helpers.sh: No such file or directory
./cmake_gcc.sh: line 52: msg: command not found
vivienne@vivienne-System-Product-Name:/media/home2/vivienne/Urho3DIDE-master$ 
[/code]
What's going on? The one I build Existence works fine. Does anyone have any clue how I can get it to work from the command line. Doesn't "bin". 


Vivienne

-------------------------

vivienneanthony | 2017-01-02 01:04:22 UTC | #2

Is this correct?

[b] ./cmake_codeblocks.sh install  -DURHO3D_64BIT=1 -DURHO3D_SAMPLES=1 -DCMAKE_BUILD_TYPE=RelWithDebInfo[/b]

Before I did not have to specify install but it doesn't work unless I put it.  

Secondly, is this just another build directly. My code is in the main /Source folder for Existence do I know have to manually put it in the Source of install or in the main Source. I modifed the old cmake.txt files so I guess I edit/copy the main ones and then it's replicated in /install.

[code]/media/home2/vivienne/Urho3D-mastercurrent/install$ [/code]

Just several questions.

Vivienne

-------------------------

vivienneanthony | 2017-01-02 01:04:22 UTC | #3

[quote="Sinoid"]See this thread for details and history: [topic729.html](http://discourse.urho3d.io/t/new-build-system/715/1)

The most recent way of building creates everything in a target directory (called the build tree, where generated files are placed).

On windows I use:
[code]cmake_vs2013 C:\dev\UrhoWin[/code]

The "C:\dev\UrhoWin" is the build tree. IIRC, it checks for the build tree as a parameter first, and then tries to use an environment variable.

Makes it a lot easier to use Urho as a library and a lot easier/cleaner to work on multiple platforms simultaneously off of a single Urho root. Not everyone is going to dig it though.[/quote]

I did this addhoc to the ./cmake_codeblocks.sh

Usually I use the root as the main directory.

[b]$(dirname $0)/cmake_generic.sh $(dirname $0) $@ -G "CodeBlocks - Unix Makefiles"[/b]

-------------------------

vivienneanthony | 2017-01-02 01:04:22 UTC | #4

If I use

[code] ./cmake_generic.sh /media/home2/vivienne/Urho3D-mastercurrent/Urho3D  -DURHO3D_64BIT=1 -DURHO3D_SAMPLES=1 -DCMAKE_BUILD_TYPE=RelWithDebInfo[/code]

It doesn't compile completely if I use "make" and "make install"

but  works if I put

[code]./cmake_generic.sh /media/home2/vivienne/Urho3D-mastercurrent  -DURHO3D_64BIT=1 -DURHO3D_SAMPLES=1 -DCMAKE_BUILD_TYPE=RelWithDebInfo[/code]

but make install places  the binaries at /usr/local/bin/ not the shared folder of Urho3D which has all the resources  or does something has to be set.

-------------------------

weitjong | 2017-01-02 01:04:23 UTC | #5

Read the updated documentation that come together with the new build system, especially on this section [urho3d.github.io/documentation/H ... ing_Native](http://urho3d.github.io/documentation/HEAD/_building.html#Building_Native) regarding how to bring your assets to the executable binaries. Prior to the new build system refactoring, we had no viable way to bring asset dirs to the binaries, and so we were forced to install them together under the /usr/local/share/Urho3D. But since we have a way now to bring both together elegantly, the new build system now install the binaries to the /usr/local/bin as it should in the first place and leave the asset dirs in the /usr/local/share. As documented in the above section, there are more than one way to bring assets to the binaries, the installer does not know (or need to know) which one you would use, so after the 'make install' or after building the binaries in the build tree then you have to manually set this up afterwards (unless you have chosen to use URHO3D_PACKAGING build option).

-------------------------

vivienneanthony | 2017-01-02 01:04:23 UTC | #6

Hmmm. Okay.

 i get that. Just different then how i build the Existence client. I build it with all the complete source considering that would be the root path no matter what system.

So, I'm assuming it's installing as intended and I need to figure out why I can't get scorvi code to compile.

-------------------------

vivienneanthony | 2017-01-02 01:04:23 UTC | #7

[quote="weitjong"]Read the updated documentation that come together with the new build system, especially on this section [urho3d.github.io/documentation/H ... ing_Native](http://urho3d.github.io/documentation/HEAD/_building.html#Building_Native) regarding how to bring your assets to the executable binaries. Prior to the new build system refactoring, we had no viable way to bring asset dirs to the binaries, and so we were forced to install them together under the /usr/local/share/Urho3D. But since we have a way now to bring both together elegantly, the new build system now install the binaries to the /usr/local/bin as it should in the first place and leave the asset dirs in the /usr/local/share. As documented in the above section, there are more than one way to bring assets to the binaries, the installer does not know (or need to know) which one you would use, so after the 'make install' or after building the binaries in the build tree then you have to manually set this up afterwards (unless you have chosen to use URHO3D_PACKAGING build option).[/quote]

I read the document some.

I rebuilt mastercurrent with "./cmake_generic.sh /media/home2/vivienne/Urho3D-mastercurrent  -DURHO3D_64BIT=1 -DURHO3D_SAMPLES=1 -DCMAKE_BUILD_TYPE=RelWithDebInfo" then "make" and also "make install"

I went back and installed the mastercurrent which puts the binaries in "/usr/local/bin". The shared files are located at "/usr/local/shared/Urho3D".

I then edited .bashrc and .profile with the additional line "export URHO3D_HOME=/usr/local/share/Urho3D"

Afterward I cleaned Scorvi files and redid cmake_generic.sh and this is the results
[code]
vivienne@vivienne-System-Product-Name:/media/home2/vivienne/Urho3DIDE-master$ sudo ./cmake_clean.sh
vivienne@vivienne-System-Product-Name:/media/home2/vivienne/Urho3DIDE-master$ sudo ./cmake_generic.sh
./cmake_generic.sh: line 31: /media/home2/vivienne/Urho3DIDE-master/.bash_helpers.sh: No such file or directory
-- The C compiler identification is GNU
-- The CXX compiler identification is GNU
-- Check for working C compiler: /usr/bin/gcc
-- Check for working C compiler: /usr/bin/gcc -- works
-- Detecting C compiler ABI info
-- Detecting C compiler ABI info - done
-- Check for working CXX compiler: /usr/bin/c++
-- Check for working CXX compiler: /usr/bin/c++ -- works
-- Detecting CXX compiler ABI info
-- Detecting CXX compiler ABI info - done
CMake Error at CMake/Modules/FindUrho3D.cmake:143 (message):
  Could not find Urho3D library in Urho3D build tree or SDK installation.
  Use URHO3D_HOME environment variable or build option to specify the
  location of the build tree or SDK installation.
Call Stack (most recent call first):
  CMakeLists.txt:53 (find_package)


-- Configuring incomplete, errors occurred!
vivienne@vivienne-System-Product-Name:/media/home2/vivienne/Urho3DIDE-master$ echo "$URHO#D_HOME"
#D_HOME
vivienne@vivienne-System-Product-Name:/media/home2/vivienne/Urho3DIDE-master$ echo "$URHO3D_HOME"
/usr/local/share/Urho3D
vivienne@vivienne-System-Product-Name:/media/home2/vivienne/Urho3DIDE-master$ 
[/code]

-------------------------

vivienneanthony | 2017-01-02 01:04:23 UTC | #8

More information of locations

[code]vivienne@vivienne-System-Product-Name:/usr/local/bin$ ls
01_HelloWorld         11_Physics            21_AngelScriptIntegration  32_Urho2DConstraints        Editor.sh        PackageTool     
02_HelloGUI           12_PhysicsStressTest  23_Water                   33_Urho2DSpriterAnimation   ffmpeg           RampGenerator   
03_Sprites            13_Ragdolls           24_Urho2DSprite            34_DynamicGeometry          ffplay           ScriptCompiler  
04_StaticScene        14_SoundEffects       25_Urho2DParticle          35_SignedDistanceFieldText  ffprobe          SpritePacker    
05_AnimatingScene     15_Navigation         26_ConsoleInput            36_Urho2DTileMap            ffserver         Urho3DPlayer
06_SkeletalAnimation  16_Chat               27_Urho2DPhysics           37_UIDrag                   gcore            x264
07_Billboards         17_SceneReplication   28_Urho2DPhysicsRope       38_SceneAndUILoad           gdb              youtube-dl
08_Decals             18_CharacterDemo      29_SoundSynthesis          AssetImporter               gdbserver
09_MultipleViewports  19_VehicleDemo        30_LightAnimation          CoreData                    NinjaSnowWar.sh
10_RenderToTexture    20_HugeObjectCount    31_MaterialAnimation       Data                        OgreImporter
vivienne@vivienne-System-Product-Name:/usr/local/bin$ cd /usr/local/share/
vivienne@vivienne-System-Product-Name:/usr/local/share$ cd Urho3D
vivienne@vivienne-System-Product-Name:/usr/local/share/Urho3D$ ls
CMake  CMakeCache.txt  CMakeFiles  Docs  Resources  Scripts
vivienne@vivienne-System-Product-Name:/usr/local/share/Urho3D$ ls -l
total 32
drwxr-xr-x 4   4096 Mar 24 09:46 CMake
-rw-r--r-- 1  12228 Mar 24 10:21 CMakeCache.txt
drwxr-xr-x 5   4096 Mar 24 10:21 CMakeFiles
drwxr-xr-x 2   4096 Mar 24 09:47 Docs
drwxr-xr-x 4   4096 Mar 24 09:46 Resources
drwxr-xr-x 2   4096 Mar 24 09:46 Scripts
vivienne@vivienne-System-Product-Name:/usr/local/share/Urho3D$ cd CMakeFiles
vivienne@vivienne-System-Product-Name:/usr/local/share/Urho3D/CMakeFiles$ ls
CMakeCCompiler.cmake  CMakeCXXCompiler.cmake           CMakeDetermineCompilerABI_CXX.bin  CMakeSystem.cmake  CompilerIdC
cmake.check_cache     CMakeDetermineCompilerABI_C.bin  CMakeOutput.log                    CMakeTmp           CompilerIdCXX
vivienne@vivienne-System-Product-Name:/usr/local/share/Urho3D/CMakeFiles$ cd /usr/local/include/Urho3D
vivienne@vivienne-System-Product-Name:/usr/local/include/Urho3D$ ls -l
total 100
drwxr-xr-x 2  4096 Mar 24 09:46 Audio
drwxr-xr-x 3  4096 Mar 24 09:46 CMakeFiles
drwxr-xr-x 2  4096 Mar 24 09:46 Container
drwxr-xr-x 2  4096 Mar 24 09:46 Core
-rw-r--r-- 1  1400 Mar 22 21:30 DebugNew.h
drwxr-xr-x 2  4096 Mar 24 09:46 Engine
drwxr-xr-x 4  4096 Mar 24 09:46 Graphics
drwxr-xr-x 2  4096 Mar 24 09:46 Input
drwxr-xr-x 2  4096 Mar 24 09:46 IO
-rw-r--r-- 1    36 Mar 24 01:17 librevision.h
drwxr-xr-x 3  4096 Mar 24 09:46 LuaScript
drwxr-xr-x 2  4096 Mar 24 09:46 Math
drwxr-xr-x 2  4096 Mar 24 09:46 Navigation
drwxr-xr-x 2  4096 Mar 24 09:46 Network
drwxr-xr-x 2  4096 Mar 24 09:46 Physics
-rw-r--r-- 1  1267 Mar 22 21:30 Precompiled.h
drwxr-xr-x 2  4096 Mar 24 09:46 Precompiled.h.gch
drwxr-xr-x 2  4096 Mar 24 09:46 Resource
-rw-r--r-- 1  1272 Mar 22 21:30 Revision.h
drwxr-xr-x 2  4096 Mar 24 09:46 Scene
drwxr-xr-x 2  4096 Mar 24 09:46 Script
drwxr-xr-x 7  4096 Mar 24 09:46 ThirdParty
drwxr-xr-x 2  4096 Mar 24 09:46 UI
drwxr-xr-x 2  4096 Mar 24 09:46 Urho2D
-rw-r--r-- 1  1927 Mar 23 23:38 Urho3D.h
vivienne@vivienne-System-Product-Name:/usr/local/include/Urho3D$ [/code]

-------------------------

weitjong | 2017-01-02 01:04:23 UTC | #9

If you install the SDK to the system-wide location then you don't need the URHO3D_HOME defined in order to use Urho3D library. Read the updated section on the Using Library  documentation page too.

-------------------------

