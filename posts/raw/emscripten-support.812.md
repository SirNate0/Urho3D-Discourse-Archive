badpixels | 2017-01-02 01:03:04 UTC | #1

Hi,

I've made a port of the Urho3D engine to Emscripten. The github repo is at github.com/badpixels/Urho3D/tree/1.32-emscripten

It's based on the 1.32 tag. Many of the changes came from the Atomic Runtime repo. (Thank you Atomic dev(s)). Most of the samples work at some level but there are a few unsolved problems:
* no sound
* terrain doesn't render
* mouse locking fails
* no networking. As far as I know, javascript only supports http and websockets and I don't think kNet will work over websockets. (I could be wrong)
* Angelscript fails. I think it has something to do with generic calling conventions but not sure.
* anything else I haven't tried.

The built samples can be viewed at di01.wwweb3d.net/urho/

I've put this up in this state as I don't have much more time to spend on it in the near term and I thought others might be interested in helping. I would have created a pull request but I don't know if it's in a acceptable state of functionality yet and I would need some help rebasing it to HEAD and getting it to work with the new build system.

Most of the changes to the engine source are quite simple and are separated by #if defined(EMSCRIPTEN) directives. I had to move the files Controls.cpp and Controls.h from the Source/Engine/Network directory to Source/Engine/Input but this move doesn't seem to affect any of the rest of Urho so I assume it's an acceptable change.

If this is acceptable for a pull request, let me know here and I'll create one.

Enjoy :slight_smile:

-------------------------

weitjong | 2017-01-02 01:03:04 UTC | #2

Welcome to our forum.

Great work! I happen to monitor your work at your fork a few hours earlier. I have been thinking of creating the Urho3D emscripten port too and stumbled upon your fork.

-------------------------

cadaver | 2017-01-02 01:03:04 UTC | #3

Extremely good work! AngelScript failing is exactly because of missing generic calling convention bindings, and that won't be necessary for the PR to be accepted. We can mark the emscripten support as experimental and keep improving it as time goes on.

-------------------------

hdunderscore | 2017-01-02 01:03:04 UTC | #4

Nice work badpixels !

Just to note: badpixels is a regular on the irc for a long time, always helpful.

I seemed to be able to rebase to master without much trouble, however I didn't build samples yet. Looking forward to building this myself !

-------------------------

badpixels | 2017-01-02 01:03:04 UTC | #5

I think the code should rebase quite easily, but the problem I had when I tried it was it would try to use the gnu compiler to build a native executable and would not use emcc (the emscripten compiler frontend). I poked around a while in the various cmake files but did not find a reason why. It does have the file Source/CMake/Toolchains/emscripten.toolchain.cmake which should tell it which compiler to use but that info apparently didn't make it into the various Makefiles.

I haven't tried building this on windows at all.

-------------------------

weitjong | 2017-01-02 01:03:04 UTC | #6

I can reproduce your success in my 64-bit Linux host system. There are still quite a number of compiler warnings from the Urho3D library side though which I think need to be cleaned.

Last night I have tested the water also on the Travis-CI to see whether their servers are capable of automate CI building with Emscripten compiler toolchain. The Linux OS environment using *OLD* Ubuntu LTS 12.04 is not able to build the tools, not surprisingly. The Mac OS X environment using Xcode 6.1 and OSX 10.10, however, shows some promising result. It appears to me that the emsdk when runs on Mac OS X host would actually just download the pre-built binaries for all the tools, so the whole update/install/activate things lasted just about a minute. I reckon it is fast enough to perform all these three steps at the start of each CI build. Earlier I thought we need to "install" the toolchain in one of our Github repo first, just like how we do it for android-ndk toolchain. Anyway, I am very confident that if we want to support Emscripten port officially then we have no problem in setting up the CI build for it. We could even upload the build artifacts (the html + data files) to our Github pages.

-------------------------

hdunderscore | 2017-01-02 01:03:07 UTC | #7

@weitjong: 
I guess you're focusing on getting linux build going first, but just fyi there is an issue with building via cmake (Windows 7): [pastebin.com/jLYNDJ9U](http://pastebin.com/jLYNDJ9U)

I saw a similar error when I updated emscripten to master, however I could avoid it with mingw makefiles. I double checked and the error isn't in master for Unix Makefiles or Mingw Makefiles.

-------------------------

weitjong | 2017-01-02 01:03:08 UTC | #8

Which generator did you choose when generating the project using cmake-gui? I have added cmake_emscripten.bat yesterday to specifically instructs CMake to choose "MinGW Makefiles" generator. But you are correct to say that at the moment I mainly tested my changes on main workstation running on Linux. You are all welcome to test the branch on other host systems and contribute to make the change. I think we should get there faster if all work together.

-------------------------

friesencr | 2017-01-02 01:03:08 UTC | #9

I am getting a build error:

[code]
/usr/include/stdc-predef.h:59:1: error: one or more PCH files were found, but they were invalid
 #endif
 ^
/usr/include/stdc-predef.h:59:1: error: use -Winvalid-pch for more information
/usr/include/stdc-predef.h:59:1: fatal error: AssimpPCH.h: No such file or directory
compilation terminated.
[/code]

This is the normal build cmake_generic on linux with gcc.

I also noticed that the emscripten build doesn't respect the folder specified in the build.  It always targets the root folder.

-------------------------

weitjong | 2017-01-02 01:03:08 UTC | #10

[quote="friesencr"]I am getting a build error:

[code]
/usr/include/stdc-predef.h:59:1: error: one or more PCH files were found, but they were invalid
 #endif
 ^
/usr/include/stdc-predef.h:59:1: error: use -Winvalid-pch for more information
/usr/include/stdc-predef.h:59:1: fatal error: AssimpPCH.h: No such file or directory
compilation terminated.
[/code]

This is the normal build cmake_generic on linux with gcc.[/quote]
I think you should recreate your build tree from scratch. The Assimp library (only used by AssetImporter tool) should not be added as a CMake target in the first place. If you have pulled the latest code in the branch, our CMake common module should have prevented the tool targets from being added into the build tree, regardless of whether the URHO3D_TOOLS build option is set or not as this option should be ignored for Emscripten.

[quote="friesencr"]I also noticed that the emscripten build doesn't respect the folder specified in the build.  It always targets the root folder.[/quote]
Not sure what do you mean by that. I am now very accustomed to the rake tasks. I just do: "rake cmake emscripten URHO3D_SAMPLES=1 && rake make emscripten". The build tree is generated in the "../emscripten-Build" relative to my Urho3D project root path, which is as expected.

-------------------------

friesencr | 2017-01-02 01:03:08 UTC | #11

I should be been clearer.  This is on master.  I needed to build the packaging tool so i could bundle the Data/CoreData pak files with the emscripten stuff.  I reset/deleted everything and am still getting the same error.

-------------------------

weitjong | 2017-01-02 01:03:08 UTC | #12

Question about license.

I originally intended to add Emscripten license text in our existing License.txt. However, I did not check that in in the end because I realize that so far we only add licenses from third party libraries that we use when building Urho3D and we do not include any licenses from the compiler toolchains (which arguably are downloaded and installed by users into their host system instead of provided by Urho3D). Let us know if you think differently.

-------------------------

weitjong | 2017-01-02 01:03:08 UTC | #13

[quote="friesencr"]I should be been clearer.  This is on master.  I needed to build the packaging tool so i could bundle the Data/CoreData pak files with the emscripten stuff.  I reset/deleted everything and am still getting the same error.[/quote]
I am sorry that I cannot reproduce it. I just nuke my native build tree and rake cmake and rake make it successfully. All tools and samples are rebuilt OK. Before you wonder, no, there is no difference in using rake tasks or normal cmake_generic.sh build script to configure/generate the build tree.

-------------------------

friesencr | 2017-01-02 01:03:08 UTC | #14

I pulled down a fresh copy and the build works.  There must be a hidden file or something I missed.   

I also had to move my ~/.emscripten_cache/ports-builds/sdl2/include/sdl2 folder to get the compile to work.  Package managers seem to prefer the SDL2 folder.  I would bet things like the steam runtime would look there too.  It might not be a bad move to use the <SDL/SDL2> path to make it easier to dropin different sdls.  Hopefully we can use vanilla sdl someday.

-------------------------

hdunderscore | 2017-01-02 01:03:08 UTC | #15

[quote="weitjong"]Which generator did you choose when generating the project using cmake-gui? I have added cmake_emscripten.bat yesterday to specifically instructs CMake to choose "MinGW Makefiles" generator. But you are correct to say that at the moment I mainly tested my changes on main workstation running on Linux. You are all welcome to test the branch on other host systems and contribute to make the change. I think we should get there faster if all work together.[/quote]
The error is when loading the emscripten toolchain file on both Unix Makefiles and Mingw Makefiles generators (that particular error was with Mingw Makefile). Without the toolchain, cmake will configure and generate normally (although without the correct toolchain of course). The error also occurs with the cmake_emscripten.bat

I'll look further into it and let you know if I come to any solution.

[quote="friesencr"]I also had to move my ~/.emscripten_cache/ports-builds/sdl2/include/sdl2 folder to get the compile to work.  Package managers seem to prefer the SDL2 folder.  I would bet things like the steam runtime would look there too.  It might not be a bad move to use the <SDL/SDL2> path to make it easier to dropin different sdls.  Hopefully we can use vanilla sdl someday.[/quote]
I believe weitjong has set it up for Urho to build it's own SDL : [github.com/urho3d/Urho3D/blob/e ... ts.txt#L54](https://github.com/urho3d/Urho3D/blob/emscripten-port/Source/CMakeLists.txt#L54)

Also supported by the latest commit where -s USE_SDL=2 was removed. I'm not entirely sure this will prevent emscripten from including some version of SDL however.

-------------------------

friesencr | 2017-01-02 01:03:08 UTC | #16

Yeah was kind of used to doing things the old way.  I am getting it slower than my ego would like.

The executable type in the toolchain 'js' isn't being respected:
[code]
/home/chris/emscripten/emscripten/master/em++    -Wno-invalid-offsetof -ffast-math -m32 -Wno-warn-absolute-paths -Wno-unknown-warning-option -O3 -DNDEBUG    CMakeFiles/38_SceneAndUILoad.dir/SceneAndUILoad.cpp.o  -o ../../../bin/38_SceneAndUILoad -rdynamic ../../../lib/libUrho3D.a -lGL 
[/code]

-------------------------

friesencr | 2017-01-02 01:03:08 UTC | #17

when running make against the samples the output doesn't have an extension.

renaming the output to 01_HelloWorld.bc and using emcc:
emcc bin/01_HelloWorld.bc -o 01_HelloWorld.html --preload-file Data.pak --preload-file CoreData.pak -s ALLOW_MEMORY_GROWTH=1 

this seems to work.

I get a runtime error in the browser:
Assertion failed: you need to wait for the runtime to be ready (e.g. wait for main() to be called)

-------------------------

weitjong | 2017-01-02 01:03:08 UTC | #18

[quote="hd_"][quote="weitjong"]Which generator did you choose when generating the project using cmake-gui? I have added cmake_emscripten.bat yesterday to specifically instructs CMake to choose "MinGW Makefiles" generator. But you are correct to say that at the moment I mainly tested my changes on main workstation running on Linux. You are all welcome to test the branch on other host systems and contribute to make the change. I think we should get there faster if all work together.[/quote]
The error is when loading the emscripten toolchain file on both Unix Makefiles and Mingw Makefiles generators (that particular error was with Mingw Makefile). Without the toolchain, cmake will configure and generate normally (although without the correct toolchain of course). The error also occurs with the cmake_emscripten.bat

I'll look further into it and let you know if I come to any solution.

[quote="friesencr"]I also had to move my ~/.emscripten_cache/ports-builds/sdl2/include/sdl2 folder to get the compile to work.  Package managers seem to prefer the SDL2 folder.  I would bet things like the steam runtime would look there too.  It might not be a bad move to use the <SDL/SDL2> path to make it easier to dropin different sdls.  Hopefully we can use vanilla sdl someday.[/quote]
I believe weitjong has set it up for Urho to build it's own SDL : [github.com/urho3d/Urho3D/blob/e ... ts.txt#L54](https://github.com/urho3d/Urho3D/blob/emscripten-port/Source/CMakeLists.txt#L54)

Also supported by the latest commit where -s USE_SDL=2 was removed. I'm not entirely sure this will prevent emscripten from including some version of SDL however.[/quote]
I have to temporarily remove that Emscripten-specific compiler flag first in order to enable the em++ to precompile the header. With the "-s USE_SDL=2' some how it does not work. I have added in the code a comment that this is still in my todo list. From what I have read in my own research, I agree with you that this flag should be set to inform Emscripten to use SDL2.

-------------------------

weitjong | 2017-01-02 01:03:09 UTC | #19

[quote="friesencr"]when running make against the samples the output doesn't have an extension.[/quote]
I am aware of that. I only said the branch is ready for "early" testing. I did not say the work has completed.  :slight_smile:

-------------------------

friesencr | 2017-01-02 01:03:09 UTC | #20

if you run emcc with -v you can see it adds a hidden path ~/.ecmascripten_cache/port-builds or something like that too the compile.  emcc is a rather intrusive animal it seems.

another suggestion is that the build is using -O3 which might not work and might make debugging harder. using -O2 or lower while we test would be good.

EDIT: the reason i was confused is because the docs say to go look in the bin folder for html files.

-------------------------

weitjong | 2017-01-02 01:03:09 UTC | #21

[quote="friesencr"]EDIT: the reason i was confused is because the docs say to go look in the bin folder for html files.[/quote]
Ah I see. What has been documented is the end goal. Kind of like a "technical specification".  :slight_smile:

-------------------------

friesencr | 2017-01-02 01:03:09 UTC | #22

Another posible solution to the sdl problem is to upgrade to 2.04.  2.04 is supposed to work out of the box.  That would let us control our own version like we have been using.

[hg.libsdl.org/SDL/file/bb0b744f ... cripten.md](https://hg.libsdl.org/SDL/file/bb0b744fd1a6/docs/README-emscripten.md)

-------------------------

hdunderscore | 2017-01-02 01:03:09 UTC | #23

Well I found out why I got the errors that I was getting-- turns out the suffix was important in the toolchain file. I pushed the change.. but also with something extra, ahem  :blush: 

Now I'm getting some issues when building, relating to ar:
[gist]https://gist.github.com/hdunderscore/b1441caf45341b1fc3d1[/gist]

-------------------------

cadaver | 2017-01-02 01:03:09 UTC | #24

2.04 is not yet released, though it's probably quite stable already. Upgrading SDL is one of the most involved things you can do, so I'd prefer to do it once when 2.04 is out.

-------------------------

weitjong | 2017-01-02 01:03:09 UTC | #25

I suppose the debug print version of the Urho3D CMake common module is not intended to be checked in. About the ar or /usr/bin/ar, they are both just a temporary fix and not a permanent solution. These are "host compiler tool". In the cross-compiling build setup, we suppose to use the "target compiler tool", in this case emar. I suspect the problem is with the current implementation of emar, which is a python script, does not perform the standard input redirection correctly. In another words, it could be a bug from Emscripten side.

I am seriously considering that we should limit ourselves just to build Urho3D as shared lib type for Emscripten when there is no other better workaround could be found.

-------------------------

hdunderscore | 2017-01-02 01:03:09 UTC | #26

With this change: [github.com/urho3d/Urho3D/commit ... nt-9560499](https://github.com/urho3d/Urho3D/commit/416ed589d9522c58a8c3da614e392611e0c8a39e#commitcomment-9560499)

And reintroducing -USE_SDL=2, I could build samples again. Good enough for me to start with.

-------------------------

hdunderscore | 2017-01-02 01:03:11 UTC | #27

Here are some cmake hacks that I put together: [github.com/hdunderscore/Urho3D/ ... ipten-port](https://github.com/hdunderscore/Urho3D/tree/emscripten-port)

Probably needs a rework for cmake best practices..

-------------------------

weitjong | 2017-01-02 01:03:11 UTC | #28

If I may then please hold the thought to commit that changes in to the branch. I don't like how the current pak file is being preloaded without adding the dependency to the build. If done properly then when any asset resources change, it should trigger the linker to relink automatically. Both your solution and badpixel's one do not address this dependency issue.

In the meantime I have solved the emar issue. I have set our Emscripten/CMake toolchain file to use emar (or emar.bat on Windows) to produce the static archive correctly without the dirty hack to use the host tool /usr/bin/ar (or ar.exe on Windows). Just to keep you guys updated.

-------------------------

hdunderscore | 2017-01-02 01:03:11 UTC | #29

Sounds good, thanks for the update.

-------------------------

weitjong | 2017-01-02 01:03:11 UTC | #30

I am attempting to make the ALLOW_MEMORY_GROWTH becomes a build option, say "EMSCRIPTEN_ALLOW_MEMORY_GROWTH". It defaults to 0 instead of 1 because I think enabling memory grow implying disabling the asm.js (or some part of its optimization) which will hurt the performance. We also need to have a second build option "EMSCRIPTEN_TOTAL_MEMORY" to set the heap memory size if we do not let the heap to grow as per demand. What do you guys think is the "best" default size for Urho3D samples? As it will be a build option, user can specify different value to override this default or just turn on the first build option.

EDIT:
Alternatively, we could just set a sensible or typical memory size for Urho3D games/application in general as the default value for this new build option. The build option is nothing more than CMake variable which can be further fine tuned in the app's CMakeLists.txt. That is, if we want to then we can also set the EMSCRIPTEN_TOTAL_MEMORY variable differently on each of the Sample's CMakeLists.txt when one size cannot fit all. I want to ask just in case one of you already has this table of memory size per samples ready, so I don't have to spend time to find them again. Thanks.

-------------------------

hdunderscore | 2017-01-02 01:03:12 UTC | #31

It's a good idea to offer those options. I personally haven't got those numbers handy though. I guess a quick and dirty way is to open up the heaviest sample and use the numbers from there.

I'm currently working on the mouse input, using the Pointer Lock API exposed via emscripten to allow mouse trapping ([kripken.github.io/emscripten-sit ... ointerlock](http://kripken.github.io/emscripten-site/docs/api_reference/html5.h.html#pointerlock)). After that I'll look at the touch input.

-------------------------

weitjong | 2017-01-02 01:03:12 UTC | #32

[quote="hd_"]I'm currently working on the mouse input, using the Pointer Lock API exposed via emscripten to allow mouse trapping ([kripken.github.io/emscripten-sit ... ointerlock](http://kripken.github.io/emscripten-site/docs/api_reference/html5.h.html#pointerlock)). After that I'll look at the touch input.[/quote]
Nice!

I will start to work on the branch a little bit more later today. I got it working to build the Urho3D lib and samples in a single build correctly with html as output now but I want to do a host tool building for the PackageTool, so the *.pak could be generated on the fly. I will push my changes after this part is completed. I also find a regression issue with the current iOS build where it now fails to recognize resource modification to trigger a rebuild. I think CMake 3.1.1 Xcode generator behaves differently than previous versions, so our existing workaround to solve the resource dependency problem has to be revisited.

-------------------------

hdunderscore | 2017-01-02 01:03:14 UTC | #33

I've posted on my fork a preview of the work I've done for input: [github.com/hdunderscore/Urho3D/ ... 0e4b7c4c01](https://github.com/hdunderscore/Urho3D/commit/b6ffd2438173f39ffcef01eaee23990e4b7c4c01)
[quote]+/** HTML5 (Emscripten) is limited in the way it handles input. The EmscriptenInput class attempts to provide the glue between Urho3D Input behavior and HTML5, where SDL currently fails to do so.
+ *
+ * Mouse Input:
+ * - The OS mouse cursor position can't be set.
+ * - The mouse can be trapped within play area via 'PointerLock API', which requires a request and interaction between the user and browser.
+ *   - To request mouse lock, call SetMouseMode(MM_RELATIVE). The E_MOUSEMODECHANGED event will be sent if/when the user confirms the request.
+ *   - The user can press 'escape' key and browser will force user out of pointer lock. Urho will send the E_MOUSEMODECHANGED event.
+ *   - SetMouseMode(MM_ABSOLUTE) will leave pointer lock.
+ * - MM_WRAP is unsupported.[/quote]
I intend to follow the pattern for the other areas of input, so if you see something you think should be different or know of another way, let me know ! 

There are still some kinks that I haven't nailed down:
[ul][li]Going in and out of mouse relative (pointer lock) causes a strange mouse delta to be received (ie, causing a jump in camera view).[/li]
[li]The first time you enter mouse relative (pointer lock), there is a strange mouse delta received when you press a mouse button.[/li]
[li]Input focus isn't yet detected on page load (eg, urho will run if it's in the background on load), otherwise focus changes should be ok.[/li]
[li]If OS cursor is visible and page has no focus, urho still reads it (easy to change, but I didn't check if this is expected or consistent with non-emscripten builds).[/li][/ul]

I may leave these issues aside for the time being.

-------------------------

GoogleBot42 | 2017-01-02 01:03:15 UTC | #34

Great work so far!   :smiley:

-------------------------

weitjong | 2017-01-02 01:03:15 UTC | #35

Sorry for the delay. The host tool building took longer than I expected. But with these changes in the branch now, we can literally build everything in one go. It builds PackageTool (as host tool) while cross-compiling for Emscripten then use the host PackageTool to package the resource dirs on the fly and then use the *.pak in the final linking phase. As promise, this is done with proper resource dirs dependency check. Any asset changes in the resource dirs will trigger a rebuild as necessary. In Emscripten case, it should trigger the re-linking.

Since the resource dirs packaging is so useful, I have also taken time to make it avaiable for other platforms too. We have now a new URHO3D_PACKAGING build option. The resultant *.pak will be placed in the "bin" subdir in the build tree, which works quite nice since now executables in the "bin" in the build tree could run without setting up any resource prefix path even.

Note that I have only mainly tested my changes in Linux host, so there may still be a few teething issues on other host systems. I have temporarily set the total memory size to 256M (to be fine-tuned). It is probably on the high side for the samples. I have not also merged the changes from hd_ for the mouse input. @hd_, please kindly rebase your fork and push your work for the mouse input to the branch directly when you think it is ready (i.e. no debug print).

-------------------------

friesencr | 2017-01-02 01:03:15 UTC | #36

I am getting an error building the package tool:

[code]
[ 79%] Building CXX object CMakeFiles/PackageTool.dir/PackageTool.cpp.o
/home/chris/dev/Urho3D/Source/Tools/PackageTool/PackageTool.cpp:23:27: fatal error: Urho3D/Urho3D.h: No such file or directory
 #include <Urho3D/Urho3D.h>
                           ^
compilation terminated.
CMakeFiles/PackageTool.dir/build.make:57: recipe for target 'CMakeFiles/PackageTool.dir/PackageTool.cpp.o' failed
make[5]: *** [CMakeFiles/PackageTool.dir/PackageTool.cpp.o] Error 1
CMakeFiles/Makefile2:65: recipe for target 'CMakeFiles/PackageTool.dir/all' failed
make[4]: *** [CMakeFiles/PackageTool.dir/all] Error 2
Makefile:116: recipe for target 'all' failed
make[3]: *** [all] Error 2
Source/Tools/CMakeFiles/PackageTool.dir/build.make:108: recipe for target 'Source/Tools/PackageTool-prefix/src/PackageTool-stamp/PackageTool-build' failed
make[2]: *** [Source/Tools/PackageTool-prefix/src/PackageTool-stamp/PackageTool-build] Error 2
CMakeFiles/Makefile2:796: recipe for target 'Source/Tools/CMakeFiles/PackageTool.dir/all' failed
make[1]: *** [Source/Tools/CMakeFiles/PackageTool.dir/all] Error 2
Makefile:136: recipe for target 'all' failed
make: *** [all] Error 2

[/code]

-------------------------

friesencr | 2017-01-02 01:03:15 UTC | #37

had to add an include folder
[code]
diff --git a/Source/Tools/PackageTool/CMakeLists.txt b/Source/Tools/PackageTool/CMakeLists.txt
index 6346faf..a372321 100644
--- a/Source/Tools/PackageTool/CMakeLists.txt
+++ b/Source/Tools/PackageTool/CMakeLists.txt
@@ -100,7 +100,7 @@ if (NOT CMAKE_PROJECT_NAME STREQUAL Urho3D)
     add_subdirectory (${BAKED_CMAKE_SOURCE_DIR}/Source/ThirdParty/LibCpuId host/LibCpuId)
     add_subdirectory (${BAKED_CMAKE_SOURCE_DIR}/Source/ThirdParty/LZ4 host/LZ4)
     add_subdirectory (${BAKED_CMAKE_SOURCE_DIR}/Source/ThirdParty/SDL host/SDL)
-    set (INCLUDE_DIRS ${BAKED_CMAKE_BINARY_DIR}/include/Urho3D ${CMAKE_BINARY_DIR}/${DEST_INCLUDE_DIR}/ThirdParty)
+    set (INCLUDE_DIRS ${BAKED_CMAKE_BINARY_DIR}/include ${BAKED_CMAKE_BINARY_DIR}/include/Urho3D ${CMAKE_BINARY_DIR}/${DEST_INCLUDE_DIR}/ThirdParty)
     set (LIBS LibCpuId SDL)
 endif ()
[/code]

-------------------------

hdunderscore | 2017-01-02 01:03:15 UTC | #38

Same problem and solution as friesncr. A minor bug I also noticed when I did "make 13_Ragdolls -j4", I also had 01_HelloWorld build too.

Really nice job weitjong, very polished feel to the build process with those changes. I'll submit my work soon.

-------------------------

weitjong | 2017-01-02 01:03:16 UTC | #39

[quote="friesencr"]I am getting an error building the package tool:

[code]
[ 79%] Building CXX object CMakeFiles/PackageTool.dir/PackageTool.cpp.o
/home/chris/dev/Urho3D/Source/Tools/PackageTool/PackageTool.cpp:23:27: fatal error: Urho3D/Urho3D.h: No such file or directory
 #include <Urho3D/Urho3D.h>
                           ^
compilation terminated.
CMakeFiles/PackageTool.dir/build.make:57: recipe for target 'CMakeFiles/PackageTool.dir/PackageTool.cpp.o' failed
make[5]: *** [CMakeFiles/PackageTool.dir/PackageTool.cpp.o] Error 1
CMakeFiles/Makefile2:65: recipe for target 'CMakeFiles/PackageTool.dir/all' failed
make[4]: *** [CMakeFiles/PackageTool.dir/all] Error 2
Makefile:116: recipe for target 'all' failed
make[3]: *** [all] Error 2
Source/Tools/CMakeFiles/PackageTool.dir/build.make:108: recipe for target 'Source/Tools/PackageTool-prefix/src/PackageTool-stamp/PackageTool-build' failed
make[2]: *** [Source/Tools/PackageTool-prefix/src/PackageTool-stamp/PackageTool-build] Error 2
CMakeFiles/Makefile2:796: recipe for target 'Source/Tools/CMakeFiles/PackageTool.dir/all' failed
make[1]: *** [Source/Tools/CMakeFiles/PackageTool.dir/all] Error 2
Makefile:136: recipe for target 'all' failed
make: *** [all] Error 2

[/code][/quote]
Thanks for reporting this. Perhaps that is the only drawback of having Urho3D SDK installed in the system-wide default installation location. As my host system has the Urho3D.h in the /usr/local/include, it "masks" this problem from my test build tree. The fix will be pushed to the branch soon together with other small code clean up.

-------------------------

weitjong | 2017-01-02 01:03:16 UTC | #40

[quote="hd_"]Same problem and solution as friesncr. A minor bug I also noticed when I did "make 13_Ragdolls -j4", I also had 01_HelloWorld build too.

Really nice job weitjong, very polished feel to the build process with those changes. I'll submit my work soon.[/quote]
That is an unintended side effect. Originally I had setup all the main executable targets to depend on the RESOURCE_CHECK custom target (They share one custom target because their resource dirs are the same, or otherwise each main target would have a unique custom RESOURCE_CHECK_XXXX each). The RESOURCE_CHECK custom target invalidates the timestamp of the resource dirs when necessary which in turn would trigger a custom "resource packaging" step on each of the main executable target. But the problem was, in a concurrent build (e.g. make -j8), multiple custom "resource packaging" steps would spring into action as the result. Normally this is a good thing if they were really attempting to package different resource dirs to *.pak. In our sample case, however, they were just overwriting each other because the resource dirs list are the same and the target *.pak location are the same. In order to solve this, when sharing the same RESOURCE_CHECK custom target, it now depends on the first main target (whichever has created the custom RESOURCE_CHECK target) instead. In this case, 01_HelloWorld. It works nicely when you do an ALL_BUILD. But if you just build a single main target then you see it will attempt to build the first main target too. I didn't see that coming. Let me see if there is easy way to fix this or otherwise we have to live with it as in real life situation a project most probably will have only one main target or that multiple main targets do not share the same resource dirs.

I am eager to see your work to be merged.

-------------------------

friesencr | 2017-01-02 01:03:16 UTC | #41

Something that would be pretty cool is if we could get source maps built.  I set RelWithDebug info in CMAKE but it overrides the '-g' flag.  To get source maps the setting needs to be -g4.  

[kripken.github.io/emscripten-sit ... gging.html](http://kripken.github.io/emscripten-site/docs/porting/Debugging.html)

-------------------------

weitjong | 2017-01-02 01:03:17 UTC | #42

[quote="hd_"]Same problem and solution as friesncr. A minor bug I also noticed when I did "make 13_Ragdolls -j4", I also had 01_HelloWorld build too.

Really nice job weitjong, very polished feel to the build process with those changes. I'll submit my work soon.[/quote]
@hd_, I hope you will still spend time on the input subsystem to fix those kinks that you have observed. I think you are the best person in this area.

I have made a small tweak to the build system to fix the unintended side effect you reported earlier. Now if you build a single main target, it does not build the first main target (01_HelloWorld) unnecessarily anymore. The main target now only depends on other non-main targets, including RESOURCE_CHECK custom target. The RESOURCE_CHECK custom target now has dual functions: resource dirs checking and, if enabbled, also resource dirs packaging. This fix has also worked around the issue with resource packaging being triggered multiple times in a concurrent build cleanly. So, killing two birds with one stone.

You may want to try this resource dirs checking and packaging by performing this test on your host system:
[ul]
[li] rake cmake emcripten URHO3D_SAMPLES=1 (or use the usual ./cmake_emscripten.sh <build-tree> -DURHO3D_SAMPLES=1)[/li]
[li] rake make emscripten target=13_Ragdolls (or cd <build-tree> && make -j8 13_Ragdolls)[/li]
[li] [b]Verify the 13_Ragdolls.html is runnable at this point[/b][/li]
[li] touch -cm bin/Data/UI/DefaultStyle.xml (or modify any assets you would like to test)[/li]
[li] rake make emscripten target=13_Ragdolls[/li]
[li] [b]Verify that: 1) resource packaging is triggered and 2) re-linking is triggered.[/li][/ul][/b]I have tested this test case successfully on my Linux host.

-------------------------

weitjong | 2017-01-02 01:03:17 UTC | #43

I have attempted to enable the CI build for the Emscripten. See [travis-ci.org/urho3d/Urho3D/builds/50074852](https://travis-ci.org/urho3d/Urho3D/builds/50074852). It failed, I think due to concurrent build which tried to download sdl2 port in three different threads and overwriting the downloaded zip file. Anyone knows how to pre-download the sdl2 port into the emcc cache? If that could be done then sdl2 will be downloaded first before the Urho3D build starts. Thanks.

-------------------------

friesencr | 2017-01-02 01:03:17 UTC | #44

[quote="weitjong"]I have attempted to enable the CI build for the Emscripten. See [travis-ci.org/urho3d/Urho3D/builds/50074852](https://travis-ci.org/urho3d/Urho3D/builds/50074852). It failed, I think due to concurrent build which tried to download sdl2 port in three different threads and overwriting the downloaded zip file. Anyone knows how to pre-download the sdl2 port into the emcc cache? If that could be done then sdl2 will be downloaded first before the Urho3D build starts. Thanks.[/quote]

There are two hidden folders in the home folder
.emscripten_cache/  .emscripten_ports/

The file is downloaded in the ports folder and compiled, then is copied over to the cache folder.

-------------------------

weitjong | 2017-01-02 01:03:18 UTC | #45

The SDL2 port concurrent fetching issue has been resolved. It is easier than I thought. I could not find any other way to tell Emscripten to fetch the SDL2 port and intended to create another dummy custom target to force the compiler to fetch the SDL2 port then it strikes me that we already have a custom target for SDL in Emscripten build, so I just added the fetching step there.  :slight_smile: 

While researching for the answer, I actually find another useful Emscripten feature. It has its own packaging tool which the emcc/em++ compiler calls when processing "--preload-file" flag. From what I understand, we can use this tool to separate the processes between packaging the resource pak (the data) and linking the executable (the html+js). The linking phase in Emscripten is notoriously slow. So, we will get a big win when any assets changes would only trigger a "repackage" using Emcripten packaging tool instead of triggering a full re-link. I believe it is doable but I will do this more advance build setup when time permits.

-------------------------

hdunderscore | 2017-01-02 01:03:19 UTC | #46

Nice work with the build system, as far as I can see it's all running smooth now !

I'll look into the remaining two input issues I listed and then move onto touch input.

I did take a peek at the shadow issue, it seems like something that may be easy to fix if you know what you are doing, however that's not me. Perhaps cadaver could take a look?

-------------------------

weitjong | 2017-01-02 01:03:19 UTC | #47

I also propose to merge this topic branch to the master branch now although it is not yet 100% complete. Like Lasse has said before, we could mark somewhere that Emscripten port of Urho3D is still experimental. Only after merging to master branch, we can truly verify that those changes we have made for Emscripten platform do not cause any regression issues in other platforms.

The Emscripten-CI will be up and running soon too. I plan to conclude this before I am out of town for "Chinese New Year" holiday.  :smiley:

-------------------------

hdunderscore | 2017-01-02 01:03:19 UTC | #48

That sounds reasonable to me -- it would also help to get a better picture of what needs fixing from more users.

I have mostly fixed the issues I mentioned earlier, although I see Chrome handles things differently than Firefox, so the mouse jump on mouse mode switch is not handled well.

-------------------------

weitjong | 2017-01-02 01:03:20 UTC | #49

[quote="friesencr"]Something that would be pretty cool is if we could get source maps built.  I set RelWithDebug info in CMAKE but it overrides the '-g' flag.  To get source maps the setting needs to be -g4.  

[kripken.github.io/emscripten-sit ... gging.html](http://kripken.github.io/emscripten-site/docs/porting/Debugging.html)[/quote]
The -g4 flag is now set for Debug configuration build (only). I verify that it produces source code line numbers in the resultant *.js files.

-------------------------

weitjong | 2017-01-02 01:03:21 UTC | #50

We have a first successful Emscripten-CI build today. I have manually uploaded the build artifacts to Urho3D main website. The HTML5 samples link can be found here: [urho3d.github.io/pages.html](http://urho3d.github.io/pages.html). If I have more time, I could automate this upload to take place each time new Emscripten build artifacts are available.

-------------------------

GoogleBot42 | 2017-01-02 01:03:21 UTC | #51

Awesome!!!  Support is being added really quick!   :smiley:  Amazing job!

-------------------------

hdunderscore | 2017-01-02 01:03:22 UTC | #52

I did a quick test and it seems you can freely use the same data package across samples (that's expected) so it might be friendly for bandwidth to point to a shared data package.

A simple regex replace works to change all references manually, although if you want an alternative then : [kripken.github.io/emscripten-sit ... kager-tool](http://kripken.github.io/emscripten-site/docs/porting/files/packaging_files.html#packaging-using-the-file-packager-tool)

-------------------------

friesencr | 2017-01-02 01:03:22 UTC | #53

[quote="weitjong"]We have a first successful Emscripten-CI build today. I have manually uploaded the build artifacts to Urho3D main website. The HTML5 samples link can be found here: [urho3d.github.io/pages.html](http://urho3d.github.io/pages.html). If I have more time, I could automate this upload to take place each time new Emscripten build artifacts are available.[/quote]


weitjong awesome!!!  I almost have audio working.   I think with the right combination of candy and doritos it will happen.   Thanks for getting source maps in there too.  People will be so spoiled to be able to debug while seeing their c++ code.

-------------------------

weitjong | 2017-01-02 01:03:22 UTC | #54

[quote="hd_"]I did a quick test and it seems you can freely use the same data package across samples (that's expected) so it might be friendly for bandwidth to point to a shared data package.

A simple regex replace works to change all references manually, although if you want an alternative then : [kripken.github.io/emscripten-sit ... kager-tool](http://kripken.github.io/emscripten-site/docs/porting/files/packaging_files.html#packaging-using-the-file-packager-tool)[/quote]
That is a dirty hack. I have commented on this Emscripten packager tool before. If we really want to do it properly then it will not only avoid unnecessary re-linking when assets changes but also could enable the samples to share a same data file as you pointed out.

-------------------------

friesencr | 2017-01-02 01:03:22 UTC | #55

Audio is working.  [github.com/urho3d/Urho3D/commit ... 3aefb8a2e3](https://github.com/urho3d/Urho3D/commit/f3fe5894721761c2434d6ed6c103553aefb8a2e3)

Correction:  Flaming hot munchies and an ice cream sandwich.

-------------------------

devrich | 2017-01-02 01:03:22 UTC | #56

Are you guys building in support for us to script in JavaScript and use that on Android Apps and Linux Apps - like how Lua and AngelScript are done?  * hopes!! *

I have done my greatest work in JavaScript with another engine many years ago and would LOVE to get my JavaScript on again with Urho3D !

-------------------------

hdunderscore | 2017-01-02 01:03:22 UTC | #57

[quote="devrich"]Are you guys building in support for us to script in JavaScript and use that on Android Apps and Linux Apps - like how Lua and AngelScript are done?  * hopes!! *

I have done my greatest work in JavaScript with another engine many years ago and would LOVE to get my JavaScript on again with Urho3D ![/quote]
I don't think any of us are working on that angle at the moment -- this work allows us to target html5/webgl, for example:
[urho3d.github.io/HTML5-samples.html](http://urho3d.github.io/HTML5-samples.html)

You can see the Urho3D (C++) samples are running in the browser. That's pretty exciting for me !

At the moment it looks like AngelScript as a scripting language is out in Emscripten (however, I think it could be reasonable to support it via the Angelscript AOT work, which would be fantastic !) and Lua might be possible.

[quote="friesencr"]Audio is working.[/quote]
Works great, nice work !

-------------------------

friesencr | 2017-01-02 01:03:22 UTC | #58

[quote="devrich"]Are you guys building in support for us to script in JavaScript and use that on Android Apps and Linux Apps - like how Lua and AngelScript are done?  * hopes!! *

I have done my greatest work in JavaScript with another engine many years ago and would LOVE to get my JavaScript on again with Urho3D ![/quote]

There isn't going to be javascript unless someone makes bindings for it.  There isn't going to be angelscript or lua support on the initial release.  If you want js support in the near term you will probably want to check out Josh's fork, the Atomic Engine.

I hope we merge this soon so more people can play with it.  I am a little concerned about the cpu usage.  It pegs a core on my box.  The profiler doesn't hit the part of the code that is taking a long time either.

Update: my performance problems seem to be linux only.

-------------------------

devrich | 2017-01-02 01:03:23 UTC | #59

Well even still; that's pretty awesome to be able to have C++11 Urho3D projects export to HTML5/webGL for many reasons :slight_smile:

The two biggest I can think of for instance:

* Free Games ( of course )

* 3D Artist Portfolios ( moving their objects around in 3D and even applying animations to showcase their Artistic talents )

Excellent work guys!!

-------------------------

weitjong | 2017-01-02 01:03:23 UTC | #60

[quote="friesencr"]Audio is working.  [github.com/urho3d/Urho3D/commit ... 3aefb8a2e3](https://github.com/urho3d/Urho3D/commit/f3fe5894721761c2434d6ed6c103553aefb8a2e3)

Correction:  Flaming hot munchies and an ice cream sandwich.[/quote]
Sweeet!

-------------------------

weitjong | 2017-01-02 01:03:23 UTC | #61

[quote="friesencr"][quote="devrich"]Are you guys building in support for us to script in JavaScript and use that on Android Apps and Linux Apps - like how Lua and AngelScript are done?  * hopes!! *

I have done my greatest work in JavaScript with another engine many years ago and would LOVE to get my JavaScript on again with Urho3D ![/quote]

There isn't going to be javascript unless someone makes bindings for it.  There isn't going to be angelscript or lua support on the initial release.  If you want js support in the near term you will probably want to check out Josh's fork, the Atomic Engine.

I hope we merge this soon so more people can play with it.  I am a little concerned about the cpu usage.  It pegs a core on my box.  The profiler doesn't hit the part of the code that is taking a long time either.

Update: my performance problems seem to be linux only.[/quote]
@Lasse, do you have any objection that we merge this branch now to master branch?

-------------------------

Stinkfist | 2017-01-02 01:03:23 UTC | #62

Great work guys!

-------------------------

cadaver | 2017-01-02 01:03:23 UTC | #63

[quote="weitjong"]
@Lasse, do you have any objection that we merge this branch now to master branch?[/quote]
No objections.

-------------------------

weitjong | 2017-01-02 01:03:24 UTC | #64

[quote="cadaver"]No objections.[/quote]
The branch has been merged into master branch. Already the CI builds pick up a regression issue. Will wait until all the CI builds complete before submitting the corrective patch.

-------------------------

GoogleBot42 | 2017-01-02 01:03:25 UTC | #65

I got an error when building...  :frowning: 

[spoiler]googlebot@comp ~/Desktop/Urho3D (git)-[master] % make clean
googlebot@comp ~/Desktop/Urho3D (git)-[master] % ./cmake_emscripten.sh -D URHO3D_LUA=1 -D URHO3D_LUAJIT=1 -D URHO3D_SAFE_LUA=1 -D URHO3D_SAMPLES=1 -D URHO3D_EXTRAS=1 .
-- Configuring done
-- Generating done
-- Build files have been written to: /home/googlebot/Desktop/Urho3D
googlebot@comp ~/Desktop/Urho3D (git)-[master] % make
[  0%] Building C object Source/ThirdParty/FreeType/CMakeFiles/FreeType.dir/src/autofit/autofit.c.o
[  0%] Building C object Source/ThirdParty/FreeType/CMakeFiles/FreeType.dir/src/base/ftbase.c.o
[  1%] Building C object Source/ThirdParty/FreeType/CMakeFiles/FreeType.dir/src/base/ftbbox.c.o
[  1%] Building C object Source/ThirdParty/FreeType/CMakeFiles/FreeType.dir/src/base/ftbitmap.c.o
[  1%] Building C object Source/ThirdParty/FreeType/CMakeFiles/FreeType.dir/src/base/ftfstype.c.o
[  1%] Building C object Source/ThirdParty/FreeType/CMakeFiles/FreeType.dir/src/base/ftgasp.c.o
[  1%] Building C object Source/ThirdParty/FreeType/CMakeFiles/FreeType.dir/src/base/ftglyph.c.o
[  2%] Building C object Source/ThirdParty/FreeType/CMakeFiles/FreeType.dir/src/base/ftgxval.c.o
[  2%] Building C object Source/ThirdParty/FreeType/CMakeFiles/FreeType.dir/src/base/ftinit.c.o
[  2%] Building C object Source/ThirdParty/FreeType/CMakeFiles/FreeType.dir/src/base/ftlcdfil.c.o
[  2%] Building C object Source/ThirdParty/FreeType/CMakeFiles/FreeType.dir/src/base/ftmm.c.o
[  2%] Building C object Source/ThirdParty/FreeType/CMakeFiles/FreeType.dir/src/base/ftotval.c.o
[  3%] Building C object Source/ThirdParty/FreeType/CMakeFiles/FreeType.dir/src/base/ftpatent.c.o
[  3%] Building C object Source/ThirdParty/FreeType/CMakeFiles/FreeType.dir/src/base/ftpfr.c.o
[  3%] Building C object Source/ThirdParty/FreeType/CMakeFiles/FreeType.dir/src/base/ftstroke.c.o
[  3%] Building C object Source/ThirdParty/FreeType/CMakeFiles/FreeType.dir/src/base/ftsynth.c.o
[  3%] Building C object Source/ThirdParty/FreeType/CMakeFiles/FreeType.dir/src/base/ftsystem.c.o
[  4%] Building C object Source/ThirdParty/FreeType/CMakeFiles/FreeType.dir/src/base/fttype1.c.o
[  4%] Building C object Source/ThirdParty/FreeType/CMakeFiles/FreeType.dir/src/base/ftwinfnt.c.o
[  4%] Building C object Source/ThirdParty/FreeType/CMakeFiles/FreeType.dir/src/bdf/bdf.c.o
[  4%] Building C object Source/ThirdParty/FreeType/CMakeFiles/FreeType.dir/src/bzip2/ftbzip2.c.o
[  4%] Building C object Source/ThirdParty/FreeType/CMakeFiles/FreeType.dir/src/cache/ftcache.c.o
[  5%] Building C object Source/ThirdParty/FreeType/CMakeFiles/FreeType.dir/src/cff/cff.c.o
[  5%] Building C object Source/ThirdParty/FreeType/CMakeFiles/FreeType.dir/src/cid/type1cid.c.o
[  5%] Building C object Source/ThirdParty/FreeType/CMakeFiles/FreeType.dir/src/gxvalid/gxvalid.c.o
[  5%] Building C object Source/ThirdParty/FreeType/CMakeFiles/FreeType.dir/src/gzip/ftgzip.c.o
[  5%] Building C object Source/ThirdParty/FreeType/CMakeFiles/FreeType.dir/src/lzw/ftlzw.c.o
[  6%] Building C object Source/ThirdParty/FreeType/CMakeFiles/FreeType.dir/src/otvalid/otvalid.c.o
[  6%] Building C object Source/ThirdParty/FreeType/CMakeFiles/FreeType.dir/src/pcf/pcf.c.o
[  6%] Building C object Source/ThirdParty/FreeType/CMakeFiles/FreeType.dir/src/pfr/pfr.c.o
[  6%] Building C object Source/ThirdParty/FreeType/CMakeFiles/FreeType.dir/src/psaux/psaux.c.o
[  6%] Building C object Source/ThirdParty/FreeType/CMakeFiles/FreeType.dir/src/pshinter/pshinter.c.o
[  7%] Building C object Source/ThirdParty/FreeType/CMakeFiles/FreeType.dir/src/psnames/psmodule.c.o
[  7%] Building C object Source/ThirdParty/FreeType/CMakeFiles/FreeType.dir/src/raster/raster.c.o
[  7%] Building C object Source/ThirdParty/FreeType/CMakeFiles/FreeType.dir/src/sfnt/sfnt.c.o
[  7%] Building C object Source/ThirdParty/FreeType/CMakeFiles/FreeType.dir/src/smooth/smooth.c.o
[  7%] Building C object Source/ThirdParty/FreeType/CMakeFiles/FreeType.dir/src/truetype/truetype.c.o
[  8%] Building C object Source/ThirdParty/FreeType/CMakeFiles/FreeType.dir/src/type1/type1.c.o
[  8%] Building C object Source/ThirdParty/FreeType/CMakeFiles/FreeType.dir/src/type42/type42.c.o
[  8%] Building C object Source/ThirdParty/FreeType/CMakeFiles/FreeType.dir/src/winfonts/winfnt.c.o
Linking C static library libFreeType.a
[  8%] Built target FreeType
[  8%] Building CXX object Source/ThirdParty/JO/CMakeFiles/JO.dir/jo_jpeg.cpp.o
Linking CXX static library libJO.a
[  8%] Built target JO
[  8%] Building C object Source/ThirdParty/LZ4/CMakeFiles/LZ4.dir/lz4hc.c.o
[  9%] Building C object Source/ThirdParty/LZ4/CMakeFiles/LZ4.dir/lz4.c.o
Linking C static library libLZ4.a
[  9%] Built target LZ4
[  9%] Building CXX object Source/ThirdParty/PugiXml/CMakeFiles/PugiXml.dir/src/pugixml.cpp.o
Linking CXX static library libPugiXml.a
[  9%] Built target PugiXml
[  9%] Built target rapidjson
c++: error: USE_SDL=2: No such file or directory
Source/ThirdParty/SDL/CMakeFiles/SDL.dir/build.make:49: recipe for target 'Source/ThirdParty/SDL/CMakeFiles/SDL' failed
make[2]: *** [Source/ThirdParty/SDL/CMakeFiles/SDL] Error 1
CMakeFiles/Makefile2:382: recipe for target 'Source/ThirdParty/SDL/CMakeFiles/SDL.dir/all' failed
make[1]: *** [Source/ThirdParty/SDL/CMakeFiles/SDL.dir/all] Error 2
Makefile:137: recipe for target 'all' failed
make: *** [all] Error 2
make  39.97s user 1.18s system 97% cpu 42.268 total
2 googlebot@comp ~/Desktop/Urho3D (git)-[master] %[/spoiler]

The error stays even if I don't define any flags in cmake...

EDIT: It seems it is not just the enscripten build...
I cannot build urho3d at all... same error.

-------------------------

badpixels | 2017-01-02 01:03:25 UTC | #66

I see this made it into master. That's awesome!  :slight_smile:  TYVM for that. I was totally stuck on getting it to work with the post-1.32 build system. Looks like sharing what I had was obviously the right choice so the real experts could take it further! :smiley:

-------------------------

weitjong | 2017-01-02 01:03:25 UTC | #67

[quote="GoogleBot"]I got an error when building...  :frowning: 

[spoiler]googlebot@comp ~/Desktop/Urho3D (git)-[master] % make clean
googlebot@comp ~/Desktop/Urho3D (git)-[master] % ./cmake_emscripten.sh -D URHO3D_LUA=1 -D URHO3D_LUAJIT=1 -D URHO3D_SAFE_LUA=1 -D URHO3D_SAMPLES=1 -D URHO3D_EXTRAS=1 .
-- Configuring done
-- Generating done
-- Build files have been written to: /home/googlebot/Desktop/Urho3D
googlebot@comp ~/Desktop/Urho3D (git)-[master] % make
[  0%] Building C object Source/ThirdParty/FreeType/CMakeFiles/FreeType.dir/src/autofit/autofit.c.o
[  0%] Building C object Source/ThirdParty/FreeType/CMakeFiles/FreeType.dir/src/base/ftbase.c.o
[  1%] Building C object Source/ThirdParty/FreeType/CMakeFiles/FreeType.dir/src/base/ftbbox.c.o
[  1%] Building C object Source/ThirdParty/FreeType/CMakeFiles/FreeType.dir/src/base/ftbitmap.c.o
[  1%] Building C object Source/ThirdParty/FreeType/CMakeFiles/FreeType.dir/src/base/ftfstype.c.o
[  1%] Building C object Source/ThirdParty/FreeType/CMakeFiles/FreeType.dir/src/base/ftgasp.c.o
[  1%] Building C object Source/ThirdParty/FreeType/CMakeFiles/FreeType.dir/src/base/ftglyph.c.o
[  2%] Building C object Source/ThirdParty/FreeType/CMakeFiles/FreeType.dir/src/base/ftgxval.c.o
[  2%] Building C object Source/ThirdParty/FreeType/CMakeFiles/FreeType.dir/src/base/ftinit.c.o
[  2%] Building C object Source/ThirdParty/FreeType/CMakeFiles/FreeType.dir/src/base/ftlcdfil.c.o
[  2%] Building C object Source/ThirdParty/FreeType/CMakeFiles/FreeType.dir/src/base/ftmm.c.o
[  2%] Building C object Source/ThirdParty/FreeType/CMakeFiles/FreeType.dir/src/base/ftotval.c.o
[  3%] Building C object Source/ThirdParty/FreeType/CMakeFiles/FreeType.dir/src/base/ftpatent.c.o
[  3%] Building C object Source/ThirdParty/FreeType/CMakeFiles/FreeType.dir/src/base/ftpfr.c.o
[  3%] Building C object Source/ThirdParty/FreeType/CMakeFiles/FreeType.dir/src/base/ftstroke.c.o
[  3%] Building C object Source/ThirdParty/FreeType/CMakeFiles/FreeType.dir/src/base/ftsynth.c.o
[  3%] Building C object Source/ThirdParty/FreeType/CMakeFiles/FreeType.dir/src/base/ftsystem.c.o
[  4%] Building C object Source/ThirdParty/FreeType/CMakeFiles/FreeType.dir/src/base/fttype1.c.o
[  4%] Building C object Source/ThirdParty/FreeType/CMakeFiles/FreeType.dir/src/base/ftwinfnt.c.o
[  4%] Building C object Source/ThirdParty/FreeType/CMakeFiles/FreeType.dir/src/bdf/bdf.c.o
[  4%] Building C object Source/ThirdParty/FreeType/CMakeFiles/FreeType.dir/src/bzip2/ftbzip2.c.o
[  4%] Building C object Source/ThirdParty/FreeType/CMakeFiles/FreeType.dir/src/cache/ftcache.c.o
[  5%] Building C object Source/ThirdParty/FreeType/CMakeFiles/FreeType.dir/src/cff/cff.c.o
[  5%] Building C object Source/ThirdParty/FreeType/CMakeFiles/FreeType.dir/src/cid/type1cid.c.o
[  5%] Building C object Source/ThirdParty/FreeType/CMakeFiles/FreeType.dir/src/gxvalid/gxvalid.c.o
[  5%] Building C object Source/ThirdParty/FreeType/CMakeFiles/FreeType.dir/src/gzip/ftgzip.c.o
[  5%] Building C object Source/ThirdParty/FreeType/CMakeFiles/FreeType.dir/src/lzw/ftlzw.c.o
[  6%] Building C object Source/ThirdParty/FreeType/CMakeFiles/FreeType.dir/src/otvalid/otvalid.c.o
[  6%] Building C object Source/ThirdParty/FreeType/CMakeFiles/FreeType.dir/src/pcf/pcf.c.o
[  6%] Building C object Source/ThirdParty/FreeType/CMakeFiles/FreeType.dir/src/pfr/pfr.c.o
[  6%] Building C object Source/ThirdParty/FreeType/CMakeFiles/FreeType.dir/src/psaux/psaux.c.o
[  6%] Building C object Source/ThirdParty/FreeType/CMakeFiles/FreeType.dir/src/pshinter/pshinter.c.o
[  7%] Building C object Source/ThirdParty/FreeType/CMakeFiles/FreeType.dir/src/psnames/psmodule.c.o
[  7%] Building C object Source/ThirdParty/FreeType/CMakeFiles/FreeType.dir/src/raster/raster.c.o
[  7%] Building C object Source/ThirdParty/FreeType/CMakeFiles/FreeType.dir/src/sfnt/sfnt.c.o
[  7%] Building C object Source/ThirdParty/FreeType/CMakeFiles/FreeType.dir/src/smooth/smooth.c.o
[  7%] Building C object Source/ThirdParty/FreeType/CMakeFiles/FreeType.dir/src/truetype/truetype.c.o
[  8%] Building C object Source/ThirdParty/FreeType/CMakeFiles/FreeType.dir/src/type1/type1.c.o
[  8%] Building C object Source/ThirdParty/FreeType/CMakeFiles/FreeType.dir/src/type42/type42.c.o
[  8%] Building C object Source/ThirdParty/FreeType/CMakeFiles/FreeType.dir/src/winfonts/winfnt.c.o
Linking C static library libFreeType.a
[  8%] Built target FreeType
[  8%] Building CXX object Source/ThirdParty/JO/CMakeFiles/JO.dir/jo_jpeg.cpp.o
Linking CXX static library libJO.a
[  8%] Built target JO
[  8%] Building C object Source/ThirdParty/LZ4/CMakeFiles/LZ4.dir/lz4hc.c.o
[  9%] Building C object Source/ThirdParty/LZ4/CMakeFiles/LZ4.dir/lz4.c.o
Linking C static library libLZ4.a
[  9%] Built target LZ4
[  9%] Building CXX object Source/ThirdParty/PugiXml/CMakeFiles/PugiXml.dir/src/pugixml.cpp.o
Linking CXX static library libPugiXml.a
[  9%] Built target PugiXml
[  9%] Built target rapidjson
c++: error: USE_SDL=2: No such file or directory
Source/ThirdParty/SDL/CMakeFiles/SDL.dir/build.make:49: recipe for target 'Source/ThirdParty/SDL/CMakeFiles/SDL' failed
make[2]: *** [Source/ThirdParty/SDL/CMakeFiles/SDL] Error 1
CMakeFiles/Makefile2:382: recipe for target 'Source/ThirdParty/SDL/CMakeFiles/SDL.dir/all' failed
make[1]: *** [Source/ThirdParty/SDL/CMakeFiles/SDL.dir/all] Error 2
Makefile:137: recipe for target 'all' failed
make: *** [all] Error 2
make  39.97s user 1.18s system 97% cpu 42.268 total
2 googlebot@comp ~/Desktop/Urho3D (git)-[master] %[/spoiler]

The error stays even if I don't define any flags in cmake...

EDIT: It seems it is not just the enscripten build...
I cannot build urho3d at all... same error.[/quote]
It appears that you have reused the same build tree for desktop and emscripten build. You should NOT do that! Try to delete the corrupted build tree and recreate new one(s) from scratch.

-------------------------

weitjong | 2017-01-02 01:03:25 UTC | #68

[quote="badpixels"]I see this made it into master. That's awesome!  :slight_smile:  TYVM for that. I was totally stuck on getting it to work with the post-1.32 build system. Looks like sharing what I had was obviously the right choice so the real experts could take it further! :smiley:[/quote]
I am sorry if the new build system holds you back but the changes in the new build system are necessary to address our shortcomings in the previous build tree configuration and generation. You have made the right choice indeed. Perhaps, I should say, you also did it at the right time. Frankly speaking, some of us actually expect the contribution to the Urho3D upstream repo should have been made sooner. It is just a matter of time until one of us cannot wait any longer.

-------------------------

badpixels | 2017-01-02 01:03:26 UTC | #69

Oh no the new build system is awesome. I just lacked the necessary experience with cmake and emscripten.

-------------------------

devrich | 2017-01-02 01:03:26 UTC | #70

Now that you have emscripten merged into master and have other major improvements in now; could the team push 1.33 out with these major changes? :slight_smile:

-------------------------

weitjong | 2017-01-02 01:03:26 UTC | #71

Be patient, my friend. The major changes have yet to come. If you have followed the discussion in the other thread, Lasse is working on upgrading the rendering backend to support D3D11 which would open up the possibility for Windows Phone port too. @Lasse, no pressure.  :wink:  The upcoming Urho release could be the greatest of all.

-------------------------

cadaver | 2017-01-02 01:03:26 UTC | #72

Of course we *could* do an intermediate release without any renderer backend stuff yet but the Emscripten will need testing and stabilization too in any case, so I don't think a release needs to be rushed, and furthermore preparing it would take time away from the actual development. In the meanwhile you can always use the latest master branch.

-------------------------

cadaver | 2017-01-02 01:03:26 UTC | #73

Shadows on Emscripten should work now. The capability is for now the same as mobile devices, no cascades, as there was some odd trouble with selecting the rearmost cascades, will likely revisit this. Terrain also works; it's just the Water example that clips it too close, which possibly is due to the water render-to-texture and clip plane/reflection plane which is not properly handled on OpenGL ES.

-------------------------

GoogleBot42 | 2017-01-02 01:03:27 UTC | #74

[quote="weitjong"][quote="GoogleBot"]I got an error when building...  :frowning: 

[spoiler]googlebot@comp ~/Desktop/Urho3D (git)-[master] % make clean
googlebot@comp ~/Desktop/Urho3D (git)-[master] % ./cmake_emscripten.sh -D URHO3D_LUA=1 -D URHO3D_LUAJIT=1 -D URHO3D_SAFE_LUA=1 -D URHO3D_SAMPLES=1 -D URHO3D_EXTRAS=1 .
-- Configuring done
-- Generating done
-- Build files have been written to: /home/googlebot/Desktop/Urho3D
googlebot@comp ~/Desktop/Urho3D (git)-[master] % make
[  0%] Building C object Source/ThirdParty/FreeType/CMakeFiles/FreeType.dir/src/autofit/autofit.c.o
[  0%] Building C object Source/ThirdParty/FreeType/CMakeFiles/FreeType.dir/src/base/ftbase.c.o
[  1%] Building C object Source/ThirdParty/FreeType/CMakeFiles/FreeType.dir/src/base/ftbbox.c.o
[  1%] Building C object Source/ThirdParty/FreeType/CMakeFiles/FreeType.dir/src/base/ftbitmap.c.o
[  1%] Building C object Source/ThirdParty/FreeType/CMakeFiles/FreeType.dir/src/base/ftfstype.c.o
[  1%] Building C object Source/ThirdParty/FreeType/CMakeFiles/FreeType.dir/src/base/ftgasp.c.o
[  1%] Building C object Source/ThirdParty/FreeType/CMakeFiles/FreeType.dir/src/base/ftglyph.c.o
[  2%] Building C object Source/ThirdParty/FreeType/CMakeFiles/FreeType.dir/src/base/ftgxval.c.o
[  2%] Building C object Source/ThirdParty/FreeType/CMakeFiles/FreeType.dir/src/base/ftinit.c.o
[  2%] Building C object Source/ThirdParty/FreeType/CMakeFiles/FreeType.dir/src/base/ftlcdfil.c.o
[  2%] Building C object Source/ThirdParty/FreeType/CMakeFiles/FreeType.dir/src/base/ftmm.c.o
[  2%] Building C object Source/ThirdParty/FreeType/CMakeFiles/FreeType.dir/src/base/ftotval.c.o
[  3%] Building C object Source/ThirdParty/FreeType/CMakeFiles/FreeType.dir/src/base/ftpatent.c.o
[  3%] Building C object Source/ThirdParty/FreeType/CMakeFiles/FreeType.dir/src/base/ftpfr.c.o
[  3%] Building C object Source/ThirdParty/FreeType/CMakeFiles/FreeType.dir/src/base/ftstroke.c.o
[  3%] Building C object Source/ThirdParty/FreeType/CMakeFiles/FreeType.dir/src/base/ftsynth.c.o
[  3%] Building C object Source/ThirdParty/FreeType/CMakeFiles/FreeType.dir/src/base/ftsystem.c.o
[  4%] Building C object Source/ThirdParty/FreeType/CMakeFiles/FreeType.dir/src/base/fttype1.c.o
[  4%] Building C object Source/ThirdParty/FreeType/CMakeFiles/FreeType.dir/src/base/ftwinfnt.c.o
[  4%] Building C object Source/ThirdParty/FreeType/CMakeFiles/FreeType.dir/src/bdf/bdf.c.o
[  4%] Building C object Source/ThirdParty/FreeType/CMakeFiles/FreeType.dir/src/bzip2/ftbzip2.c.o
[  4%] Building C object Source/ThirdParty/FreeType/CMakeFiles/FreeType.dir/src/cache/ftcache.c.o
[  5%] Building C object Source/ThirdParty/FreeType/CMakeFiles/FreeType.dir/src/cff/cff.c.o
[  5%] Building C object Source/ThirdParty/FreeType/CMakeFiles/FreeType.dir/src/cid/type1cid.c.o
[  5%] Building C object Source/ThirdParty/FreeType/CMakeFiles/FreeType.dir/src/gxvalid/gxvalid.c.o
[  5%] Building C object Source/ThirdParty/FreeType/CMakeFiles/FreeType.dir/src/gzip/ftgzip.c.o
[  5%] Building C object Source/ThirdParty/FreeType/CMakeFiles/FreeType.dir/src/lzw/ftlzw.c.o
[  6%] Building C object Source/ThirdParty/FreeType/CMakeFiles/FreeType.dir/src/otvalid/otvalid.c.o
[  6%] Building C object Source/ThirdParty/FreeType/CMakeFiles/FreeType.dir/src/pcf/pcf.c.o
[  6%] Building C object Source/ThirdParty/FreeType/CMakeFiles/FreeType.dir/src/pfr/pfr.c.o
[  6%] Building C object Source/ThirdParty/FreeType/CMakeFiles/FreeType.dir/src/psaux/psaux.c.o
[  6%] Building C object Source/ThirdParty/FreeType/CMakeFiles/FreeType.dir/src/pshinter/pshinter.c.o
[  7%] Building C object Source/ThirdParty/FreeType/CMakeFiles/FreeType.dir/src/psnames/psmodule.c.o
[  7%] Building C object Source/ThirdParty/FreeType/CMakeFiles/FreeType.dir/src/raster/raster.c.o
[  7%] Building C object Source/ThirdParty/FreeType/CMakeFiles/FreeType.dir/src/sfnt/sfnt.c.o
[  7%] Building C object Source/ThirdParty/FreeType/CMakeFiles/FreeType.dir/src/smooth/smooth.c.o
[  7%] Building C object Source/ThirdParty/FreeType/CMakeFiles/FreeType.dir/src/truetype/truetype.c.o
[  8%] Building C object Source/ThirdParty/FreeType/CMakeFiles/FreeType.dir/src/type1/type1.c.o
[  8%] Building C object Source/ThirdParty/FreeType/CMakeFiles/FreeType.dir/src/type42/type42.c.o
[  8%] Building C object Source/ThirdParty/FreeType/CMakeFiles/FreeType.dir/src/winfonts/winfnt.c.o
Linking C static library libFreeType.a
[  8%] Built target FreeType
[  8%] Building CXX object Source/ThirdParty/JO/CMakeFiles/JO.dir/jo_jpeg.cpp.o
Linking CXX static library libJO.a
[  8%] Built target JO
[  8%] Building C object Source/ThirdParty/LZ4/CMakeFiles/LZ4.dir/lz4hc.c.o
[  9%] Building C object Source/ThirdParty/LZ4/CMakeFiles/LZ4.dir/lz4.c.o
Linking C static library libLZ4.a
[  9%] Built target LZ4
[  9%] Building CXX object Source/ThirdParty/PugiXml/CMakeFiles/PugiXml.dir/src/pugixml.cpp.o
Linking CXX static library libPugiXml.a
[  9%] Built target PugiXml
[  9%] Built target rapidjson
c++: error: USE_SDL=2: No such file or directory
Source/ThirdParty/SDL/CMakeFiles/SDL.dir/build.make:49: recipe for target 'Source/ThirdParty/SDL/CMakeFiles/SDL' failed
make[2]: *** [Source/ThirdParty/SDL/CMakeFiles/SDL] Error 1
CMakeFiles/Makefile2:382: recipe for target 'Source/ThirdParty/SDL/CMakeFiles/SDL.dir/all' failed
make[1]: *** [Source/ThirdParty/SDL/CMakeFiles/SDL.dir/all] Error 2
Makefile:137: recipe for target 'all' failed
make: *** [all] Error 2
make  39.97s user 1.18s system 97% cpu 42.268 total
2 googlebot@comp ~/Desktop/Urho3D (git)-[master] %[/spoiler]

The error stays even if I don't define any flags in cmake...

EDIT: It seems it is not just the enscripten build...
I cannot build urho3d at all... same error.[/quote]
It appears that you have reused the same build tree for desktop and emscripten build. You should NOT do that! Try to delete the corrupted build tree and recreate new one(s) from scratch.[/quote]

I freshly cloned the repo and now I get this error...

googlebot@comp ~/Desktop/Urho3D (git)-[master] % ./cmake_emscripten.sh
An error has occured, build tree has to be provided as the first argument OR call this script in a build tree itself
1 googlebot@comp ~/Desktop/Urho3D (git)-[master] %

-------------------------

cadaver | 2017-01-02 01:03:27 UTC | #75

In the new build system, you always need to specify the build tree path (like it says); to build to the source tree root, use ./cmake_emscripten.sh .

-------------------------

GoogleBot42 | 2017-01-02 01:03:27 UTC | #76

[quote="cadaver"]In the new build system, you always need to specify the build tree path (like it says); to build to the source tree root, use ./cmake_emscripten.sh .[/quote]

Thanks! Works now.

-------------------------

cadaver | 2017-01-02 01:03:27 UTC | #77

Emscripten cascaded shadows are now in; just needed to add an additional shader define (WEBGL) which makes the shaders compile for 4 cascades max. On actual mobile devices it's important to avoid selecting UV coordinates in pixel shaders, but in browsers with modern GPUs there should not be a noticeable performance impact.

-------------------------

weitjong | 2017-01-02 01:03:27 UTC | #78

[quote="cadaver"]Emscripten cascaded shadows are now in; just needed to add an additional shader define (WEBGL) which makes the shaders compile for 4 cascades max. On actual mobile devices it's important to avoid selecting UV coordinates in pixel shaders, but in browsers with modern GPUs there should not be a noticeable performance impact.[/quote]
Incredible!

-------------------------

weitjong | 2017-01-02 01:03:27 UTC | #79

[quote="GoogleBot"][quote="cadaver"]In the new build system, you always need to specify the build tree path (like it says); to build to the source tree root, use ./cmake_emscripten.sh .[/quote]

Thanks! Works now.[/quote]
Note that, you only have one source tree but can potentially have limitless number of build trees for different platforms and build configurations and library types IF you have the build tree generated out-of-source tree.

-------------------------

badpixels | 2017-01-02 01:03:27 UTC | #80

[quote="cadaver"]Emscripten cascaded shadows are now in; just needed to add an additional shader define (WEBGL) which makes the shaders compile for 4 cascades max. On actual mobile devices it's important to avoid selecting UV coordinates in pixel shaders, but in browsers with modern GPUs there should not be a noticeable performance impact.[/quote]

Is that a define that needs to be added to cmake or something? I built after your last commit* and it appears only the closest level is working. Best viewed on the vehicle demo here: [di01.wwweb3d.net/urho/19_VehicleDemo.html](http://di01.wwweb3d.net/urho/19_VehicleDemo.html) 
Anything not immediately near the camera looks like it's not indexing into the depth map correctly; i.e., in one direction most of the terrain is black and in the other direction I see pieces of shadows in the wrong places.

* using this version:
commit b7d87c613f1311eb23a4f89408c10abeae6f1b25
Author: Lasse ?örni <loorni@gmail.com>
Date:   Sat Feb 14 23:37:48 2015 +0200

    Refer to HTML5 platform more accurately.

-------------------------

weitjong | 2017-01-02 01:03:27 UTC | #81

The shadow cascade changes work for me. Tested with FF 35.0.1 on Linux host system having GTX 580 and Nvidia proprietary kernel module (driver) for Linux installed.

-------------------------

hdunderscore | 2017-01-02 01:03:27 UTC | #82

Nice one cadaver, the shadow cascades work great !

-------------------------

badpixels | 2017-01-02 01:03:28 UTC | #83

Ok after a git reset --hard and a git clean -f and deleting and recreating my build directory it seems to work. I guess maybe the old shader got stuck in there somehow or something.

TY for the shadow fix :smiley:

-------------------------

hdunderscore | 2017-01-02 01:03:28 UTC | #84

Got around to debugging the touch input issues I was noticing, bug-fix pushed.

-------------------------

weitjong | 2017-01-02 01:03:28 UTC | #85

It turns out that compiling Lua VM to javascript works out of the box, so the URHO3D_LUA build option is made available for Emscripten platform now. It still defaults to FALSE as the other platforms, so user will have to set the build option to TRUE to actually enable Lua in the build. Tested with 22_LuaIntegration.html and verified that the scripted rotating behavior is working correctly.

I have started the work to make AngelScript scripting available for Emscripten platform too. However, I don't think I am able to complete the manual work to finish all the generic bindings before I go on leave. Actually at this point, I still have no idea that the generic binding will work or it is in the right direction, so I will not push my partial changes on AngelScript just yet.

-------------------------

devrich | 2017-01-02 01:03:28 UTC | #86

[quote="weitjong"]It turns out that compiling Lua VM to javascript works out of the box, so the URHO3D_LUA build option is made available for Emscripten platform now. It still defaults to FALSE as the other platforms, so user will have to set the build option to TRUE to actually enable Lua in the build. Tested with 22_LuaIntegration.html and verified that the scripted rotating behavior is working correctly.

I have started the work to make AngelScript scripting available for Emscripten platform too. However, I don't think I am able to complete the manual work to finish all the generic bindings before I go on leave. Actually at this point, I still have no idea that the generic binding will work or it is in the right direction, so I will not push my partial changes on AngelScript just yet.[/quote]

Hey!! Many thanks for gettig Lua scripting to work!  That will help a lot of new comers since most new comers have at some point or another used Lua or JavaScript. :smiley:

btw; umm what do you mean by "leave" ?  ( im in usa so i'm not famililar with what you mean )

-------------------------

weitjong | 2017-01-02 01:03:28 UTC | #87

[quote="devrich"]Hey!! Many thanks for gettig Lua scripting to work!  That will help a lot of new comers since most new comers have at some point or another used Lua or JavaScript. :smiley:

btw; umm what do you mean by "leave" ?  ( im in usa so i'm not famililar with what you mean )[/quote]
I just want to say that I will be out of town for CNY holiday. For those who will be celebrating it, I wish you ????.

-------------------------

devrich | 2017-01-02 01:03:28 UTC | #88

ohhhhh, of course!  Hey Happy New Year!! :smiley:

-------------------------

cadaver | 2017-01-02 01:03:28 UTC | #89

devrich: note that running a script VM inside a browser is "double" performance penalty. So I'm not sure if it can be generally recommended to make apps (for example full games) in script when deploying to browser. But of course, from feature-completeness sense it's excellent to have script backends also in browser builds.

weitjong: the generic bindings approach is the right direction as far as I can tell. It will also help if we encounter another platform that has problems with the non-generic (assembly language) bindings. 

The most awesome would be to autogenerate both generic and non-generic bindings, but naturally that's a lot of work, and would also need to somehow take care of the specialities we've written to the bindings, like conversion of vectors/maps. Here's a C# tool written by my former co-worker for bindings generation, but don't know if we'd want to go that route: [github.com/juj/AngelscriptGenerator](https://github.com/juj/AngelscriptGenerator)

-------------------------

weitjong | 2017-01-02 01:03:28 UTC | #90

[quote="cadaver"]weitjong: the generic bindings approach is the right direction as far as I can tell. It will also help if we encounter another platform that has problems with the non-generic (assembly language) bindings. 

The most awesome would be to autogenerate both generic and non-generic bindings, but naturally that's a lot of work, and would also need to somehow take care of the specialities we've written to the bindings, like conversion of vectors/maps. Here's a C# tool written by my former co-worker for bindings generation, but don't know if we'd want to go that route: [github.com/juj/AngelscriptGenerator](https://github.com/juj/AngelscriptGenerator)[/quote]
Thanks for the confirmation on the approach. I merged the "automatic wrapper functions" header file provided by AngelScript in the Addons subdir into our own existing Addons.h file. So using the WRAP_XXX macro, I can quickly bind the methods and functions using generic convention. But as you can already guess, it will still be a laborious task to actually write those macro calls for each and every existing native convention bindings. I have only completed that manually for Script array/dictionary/string, and I already begin to doubt anyone should spend his/her time this way just to maintain the bindings. I totally agree with you that we need a better way going forward to automate the binding generation. I have quickly looked at the "juj" AngelScriptGenerator. If I understand it correctly then it relies on Doxygen to produce the XMLs representing the classes, similar to EmbindGenerator. How come you didn't say earlier that you have an Emscripten expert as your former co-worker :wink: . Re the automatic binding generation, not sure I have what it takes to do this but if I would spend time to tackle this perhaps I would look at LibClang.

-------------------------

devrich | 2017-01-02 01:03:50 UTC | #91

[quote="weitjong"]We have a first successful Emscripten-CI build today. I have manually uploaded the build artifacts to Urho3D main website. The HTML5 samples link can be found here: [urho3d.github.io/pages.html](http://urho3d.github.io/pages.html). If I have more time, I could automate this upload to take place each time new Emscripten build artifacts are available.[/quote]


 :astonished: nooo wayyyy woooow!!!  :smiley: ---- I confirm that: [url]http://urho3d.github.io/samples/12_PhysicsStressTest.html[/url] works on my system - Linux Mint 17.1 ( 32-bit ) a bit super slow like 1 frame per several seconds _BUT_ it works!!!! :smiley:

^-- But it shouldn't xD ---- This PC is a older PC with no video card other than onboard intel chip: 
[quote]Graphics:  Card: Intel 82Q963/Q965 Integrated Graphics Controller 
           X.Org: 1.15.1 drivers: intel (unloaded: fbdev,vesa) Resolution: 1920x1080@60.0hz 
           GLX Renderer: Mesa DRI Intel 965Q x86/MMX/SSE2 GLX Version: 2.1 Mesa 10.1.3[/quote]

-------------------------

devrich | 2017-01-02 01:03:50 UTC | #92

Hey,

Has anybody tried to use this on Android or iOS ?

Does it work on those mobile devices for you ?

-------------------------

friesencr | 2017-01-02 01:03:51 UTC | #93

[quote="devrich"]Hey,

Has anybody tried to use this on Android or iOS ?

Does it work on those mobile devices for you ?[/quote]

Yes it works.  I tried it in the early stage and might have had some input issues.  If you are on android you might need a different browser, the junk stock android browser might not cut it.

-------------------------

devrich | 2017-01-02 01:03:51 UTC | #94

[quote="friesencr"]Yes it works.  I tried it in the early stage and might have had some input issues.  If you are on android you might need a different browser, the junk stock android browser might not cut it.[/quote]

Agreed! I prefer FireFox for Android myself.  I realy need to get a better tablet -_-

-------------------------

devrich | 2017-01-02 01:03:51 UTC | #95

hmmmm actually... is there a way to pick and choose what features to use in our Urho3D->emscrpiten projects?

I am really considering going all out for a smaller project I have in mind using C++ instead of scripting so that I can get it ready for browser deployment so this question is most important to me :slight_smile:

I mean for things like "optimise for better performance at decreased rendering_options for lesser gpu_capable devices"

 --or--

"disable some Urho3D features to make emscripten faster for slower mobiles"

?

-------------------------

cadaver | 2017-01-02 01:03:52 UTC | #96

There aren't Urho features that consume performance just by being compiled in, but naturally you can use normal CMake options like -DURHO3D_URHO2D=0 or -DURHO3D_NAVIGATION=0 to exclude features you don't need; this will reduce compile & link time.

Emscripten uses the OpenGL ES rendering codepaths which are already the "lowest of the low" in terms of GPU features, and in the end the content decides the performance. Things you can do is to tweak / simplify the shaders, use simple models, use as few objects onscreen as possible, use vertex lighting ( Light::SetPerVertex(true) ) instead of per-pixel lighting.

But note that with mobile + emscripten you are fighting two layers of bad performance: the mobile hardware, and the browser. A dedicated mobile app will naturally perform better.

-------------------------

weitjong | 2017-01-02 01:03:55 UTC | #97

[quote="weitjong"][quote="hd_"]I did a quick test and it seems you can freely use the same data package across samples (that's expected) so it might be friendly for bandwidth to point to a shared data package.

A simple regex replace works to change all references manually, although if you want an alternative then : [kripken.github.io/emscripten-sit ... kager-tool](http://kripken.github.io/emscripten-site/docs/porting/files/packaging_files.html#packaging-using-the-file-packager-tool)[/quote]
That is a dirty hack. I have commented on this Emscripten packager tool before. If we really want to do it properly then it will not only avoid unnecessary re-linking when assets changes but also could enable the samples to share a same data file as you pointed out.[/quote]
The latest master branch now supports EMSCRIPTEN_SHARE_DATA build option. When enabled, it creates custom rule to invoke Emscripten's file packager tool and use the generated data file (shared for all the main targets) and JS file when linking. As usual, I have only tested it with Linux host system.

EDIT: Unfortunately though, the Emscripten's file_packager.py tool always generates a new package UUID. If the tool is reinvoked due to asset changes in the resource dirs, the share data file get updated correctly but with new UUID and so does the JS file. The JS files between invocation are actually identical except this UUID. The difference is enough to cause an unnecessary relink to take place. The only way to avoid this is, we need to modify the Emscripten's file_packager.py script to tell it that we want to reuse the existing UUID. Perhaps we have to log this as an issue to Emscripten upstream.

-------------------------

hdunderscore | 2017-01-02 01:03:57 UTC | #98

I just tested it, works well -- thanks for that weitjong :smiley:

-------------------------

thebluefish | 2017-01-02 01:03:57 UTC | #99

Ya it sounds like it would be best to file an issue, or even a pull request with the change. I'm sure it would be useful for other people's projects that use it.

-------------------------

weitjong | 2017-01-02 01:03:57 UTC | #100

In my earlier test, I have simplified my test case by simply touching (change timestamp) of a resource file in the asset dirs. So, I only see the UUID change in the diff. In a more realistic test case, the size of the asset could change as well, which would then ripple down to the *.pak and the *.js.data file, and also end up as fetching file size change in the output JS file. So, they are potential two diffs: UUID and fetch size. Python is not my cup of tea (I am a Perl guy), but I will try to see whether I can patch the tool to suit our need. If it goes as plan then it would be a boon to script kiddies for fast prototyping (only with Lua at the moment).

-------------------------

