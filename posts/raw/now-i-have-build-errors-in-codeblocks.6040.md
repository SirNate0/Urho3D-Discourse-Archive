MZoltan32 | 2020-04-01 12:04:13 UTC | #1

the CMake with those error messages was building correctly i added nothing to the options just generated files

i open the cbp file in codeblocks and try to build the project it goes on well for a while then it gives these errors:

"||=== Build: all in Urho3D (compiler: GNU GCC Compiler) ===|
E:\tar\games\developedgames\Urho3D-1.7.1\Source\ThirdParty\SDL\src\SDL_log.c|309|warning: 'consoleAttached' defined but not used [-Wunused-variable]|
E:\tar\games\developedgames\Urho3D-1.7.1\Source\ThirdParty\SDL\src\SDL_log.c|312|warning: 'stderrHandle' defined but not used [-Wunused-variable]|
E:\tar\games\developedgames\Urho3D-1.7.1\Source\ThirdParty\SDL\src\audio\winmm\SDL_winmm.c||In function 'DetectWaveOutDevs':|
E:\tar\games\developedgames\Urho3D-1.7.1\Source\ThirdParty\SDL\src\audio\winmm\SDL_winmm.c|57|error: unknown type name 'WAVEOUTCAPS2W'|
E:\tar\games\developedgames\Urho3D-1.7.1\Source\ThirdParty\SDL\src\audio\winmm\SDL_winmm.c|44|note: in definition of macro 'DETECT_DEV_IMPL'|
E:\tar\games\developedgames\Urho3D-1.7.1\Source\ThirdParty\SDL\src\audio\winmm\SDL_winmm.c|48|error: request for member 'szPname' in something not a structure or union|
E:\tar\games\developedgames\Urho3D-1.7.1\Source\ThirdParty\SDL\src\audio\winmm\SDL_winmm.c|57|note: in expansion of macro 'DETECT_DEV_IMPL'|
E:\tar\games\developedgames\Urho3D-1.7.1\Source\ThirdParty\SDL\src\audio\winmm\SDL_winmm.c|48|error: request for member 'NameGuid' in something not a structure or union|
E:\tar\games\developedgames\Urho3D-1.7.1\Source\ThirdParty\SDL\src\audio\winmm\SDL_winmm.c|57|note: in expansion of macro 'DETECT_DEV_IMPL'|
E:\tar\games\developedgames\Urho3D-1.7.1\Source\ThirdParty\SDL\src\audio\winmm\SDL_winmm.c||In function 'DetectWaveInDevs':|
E:\tar\games\developedgames\Urho3D-1.7.1\Source\ThirdParty\SDL\src\audio\winmm\SDL_winmm.c|58|error: unknown type name 'WAVEINCAPS2W'|
E:\tar\games\developedgames\Urho3D-1.7.1\Source\ThirdParty\SDL\src\audio\winmm\SDL_winmm.c|44|note: in definition of macro 'DETECT_DEV_IMPL'|
E:\tar\games\developedgames\Urho3D-1.7.1\Source\ThirdParty\SDL\src\audio\winmm\SDL_winmm.c|48|error: request for member 'szPname' in something not a structure or union|
E:\tar\games\developedgames\Urho3D-1.7.1\Source\ThirdParty\SDL\src\audio\winmm\SDL_winmm.c|58|note: in expansion of macro 'DETECT_DEV_IMPL'|
E:\tar\games\developedgames\Urho3D-1.7.1\Source\ThirdParty\SDL\src\audio\winmm\SDL_winmm.c|48|error: request for member 'NameGuid' in something not a structure or union|
E:\tar\games\developedgames\Urho3D-1.7.1\Source\ThirdParty\SDL\src\audio\winmm\SDL_winmm.c|58|note: in expansion of macro 'DETECT_DEV_IMPL'|
Source\ThirdParty\SDL\CMakeFiles\SDL.dir\build.make|1168|recipe for target 'Source/ThirdParty/SDL/CMakeFiles/SDL.dir/src/audio/winmm/SDL_winmm.c.obj' failed|
CMakeFiles\Makefile2|1963|recipe for target 'Source/ThirdParty/SDL/CMakeFiles/SDL.dir/all' failed|
E:\tar\games\developedgames\Urho3D-1.7.1\build\Makefile|150|recipe for target 'all' failed|
||=== Build failed: 9 error(s), 2 warning(s) (1 minute(s), 29 second(s)) ===|
"

how should we fix these errors? maybe some of the missing things was essential within the configuration process?

-------------------------

Lys0gen | 2020-04-01 14:13:52 UTC | #2

What are you trying to build here? The Urho libs itself?
If so, why with codeblocks? Just use CMake to configure/generate and then build with mingw-make.
If you get similar errors there then you might have to update to a newer mingw version.
And when it correctly built just link the libraries in **your** actual codeblocks project.

-------------------------

MZoltan32 | 2020-04-01 14:38:07 UTC | #3

I have downloaded how it was instructed with Urho3d download page and now i am trying to build the Urho 3d projects including samples

-------------------------

Lys0gen | 2020-04-01 15:35:17 UTC | #4

Ok, so here is how I built it for MinGW/CodeBlocks:

0. Get Urho3D, extract it somewhere
1. Get CMake https://cmake.org/download/ install/extract it somewhere
2. Start cmake-gui.exe
3. In CMake, "Where is the source code" enter the Urho folder you just extracted, e.g. C:/libs/Urho3D
4. "Where to build the binaries" can be any folder, here will all the built libs be. I use different folders for Release & Debug, e.g. "C:/libs/Urho3D/build" & "C:/libs/Urho3D/buildDebug" (Make sure to switch CMAKE_BUILD_TYPE option)
5. Click "Configure" button near the bottom, specify the MakeFiles (should be default MinGW or change it to whatever you want to use/have installed), Finish.
6. **You'll likely get some errors during configuration *and* building**. I needed to do some tweaking. 
Issues I had:
* Cmake says "Error in configuration process..." because "CMake Error at CMake/Modules/FindDirectX.cmake:86 (message):
  Could not find MinGW system root.  Use MINGW_SYSROOT environment variable"
**Fix**: In CMake top right click "Add Entry" -> Name: "MINGW_SYSROOT" Type: "PATH" Value: wherever your mingw is, e.g. "C:/MinGW". Click on "Configure" again, should work now.
* You will get a lot of "Not Found/Found" stuff in the CMake output. If it is not a red error it should still build (unless it is a component you want/need installed - you can seIect those in the CMake configuration above the log). can't remember if it is necessary for Urho, but perhaps you need to download&install WinSDK and or other libraries, e.g. SDL but I think it all comes with the Urho package.
* The thirdparty Networking dependencies caused a lot of issues for me.
**Fix**: Since I don't need networking I just unchecked URHO3D -> URHO3D_NETWORK in the CMake options. If you need it, you need to check the errors during building. E.g. civetweb had undeclared uintptr_t usages and iirc there was also some issue where windows headers where not included the code files (and then I stopped bothering and just disabled it). Tweaking the thirdparty code files will fix it though. Googling the errors should help if you don't know whats wrong.
7. Click "Generate" next to "Configure", if "Generating done" you can now start building the libs.
8. For simplicity, create a .bat file in the Urho folder. Content:
	*cd ./build/
	mingw32-make clean
	mingw32-make
	pause*
**Note** that the *cd ./build/* folder is whatever you specified in step 4.; e.g. change it to *./buildDebug/* or whatever if you have a separate debug folder that you configured for.
9. Run the .bat file. If everything is setup correctly this should take some minutes and hopefully not create additional errors. If there are other errors feel free to let me know.
10. The libraries in your cbp project need to be in a specific order. Check how they are in the template here: https://discourse.urho3d.io/t/urho3d-codeblocks-wizard/1379
Using the wizard file there will save you a lot of headaches trying to figure out the correct order :slight_smile:

-------------------------

SirNate0 | 2020-04-01 17:54:05 UTC | #5

Which version of mingw are you using? It looks like someone ran into similar issues that were fixed by using mingw-w64.

https://discourse.urho3d.io/t/cmake-mingw-build-error/2961

-------------------------

MZoltan32 | 2020-04-01 16:00:44 UTC | #6

i have used the newest 32 bit version of mingw and get the same errors i will try using the 64 bit version

-------------------------

SirNate0 | 2020-04-01 17:57:33 UTC | #7

You also appear to be using the 1.7.1 release. Using the latest master branch on GitHub is recommended, as you'll probably end up running into some issues that have already been fixed in master. I don't know if that would solve your current problem, but it might help you avoid future problems.

-------------------------

