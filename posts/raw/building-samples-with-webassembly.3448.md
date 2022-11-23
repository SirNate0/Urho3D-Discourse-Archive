Synex | 2017-08-24 19:17:59 UTC | #1

**Hi everyone,**

I have been trying to build the Urho3D samples into **WebAssembly** using the **`-DEMSCRIPTEN_WASM=1`** option on Windows 10, to test out the contribution from **weitjong** earlier this year at `(https://discourse.urho3d.io/t/targeting-webassembly/2821)`

However I have been having issues for a few hours now so I am wondering if anyone else has gotten this to work? The full CMake configuration for Urho3D is done like this:

### Urho3D CMake configuration parameters (cmake_emscripten.bat)

[spoiler]
cmake_emscripten %pxyz%\build\WebBuild -DURHO3D_SAMPLES:BOOL=ON -DURHO3D_LUA:BOOL=OFF -DURHO3D_ANGELSCRIPT:BOOL=OFF -DURHO3D_C++11:BOOL=ON -DURHO3D_PHYSICS:BOOL=OFF -DURHO3D_IK:BOOL=OFF -DURHO3D_NAVIGATION:BOOL=OFF -DURHO3D_PCH:BOOL=OFF -DURHO3D_THREADING:BOOL=OFF -DEMSCRIPTEN_WASM=1
[/spoiler]

I want to note I updated the Emscripten SDK using **`emsdk install sdk-1.37.18-64bit`** beforehand.

My current Emscripten SDK activated environment looks like this:

### Output of: emsdk active --global 
[spoiler]
LLVM_ROOT='C:/Program Files/Emscripten/clang/e1.37.18_64bit'
EMSCRIPTEN_NATIVE_OPTIMIZER='C:/Program Files/Emscripten/clang/e1.37.18_64bit/optimizer.exe'
BINARYEN_ROOT='C:/Program Files/Emscripten/clang/e1.37.18_64bit/binaryen'
NODE_JS='C:/Program Files/Emscripten/node/4.1.1_64bit/bin/node.exe'
PYTHON='C:/Program Files/Emscripten/python/2.7.5.3_64bit/python.exe'
JAVA='C:/Program Files/Emscripten/java/7.45_64bit/bin/java.exe'
SPIDERMONKEY_ENGINE='C:/Program Files/Emscripten/spidermonkey/37.0.1_64bit/js.exe'
EMSCRIPTEN_ROOT='C:/Program Files/Emscripten/emscripten/1.37.18'
CRUNCH='C:/Program Files/Emscripten/crunch/1.03/crunch.exe'
MINGW_ROOT='C:/Program Files/Emscripten/mingw/7.1.0_64bit'
V8_ENGINE = ''
TEMP_DIR = 'c:/users/user/appdata/local/temp'
COMPILER_ENGINE = NODE_JS
JS_ENGINES = [NODE_JS]

Setting environment variables:
EMSDK = C:/Program Files/Emscripten
[/spoiler]

The engine web lib file builds fine, but samples **fail** with like the following console output:
### Console output of Sample Build Failure
[spoiler]
mingw32-make 05_AnimatingScene
[  1%] Built target PackageTool
[  1%] Checking and packaging resource directories
Packaging C:/dev/proj/client/libsrc/Urho3D-1.6/bin/CoreData...
Packaging C:/dev/proj/client/libsrc/Urho3D-1.6/bin/Data...
[  1%] Built target RESOURCE_CHECK
[ 12%] Built target Box2D
[ 12%] Built target JO
[ 22%] Built target FreeType
[ 22%] Built target rapidjson
[ 23%] Built target PugiXml
[ 24%] Built target LZ4
[ 25%] Built target StanHull
[ 47%] Built target SDL
[ 47%] Built target STB
[ 98%] Built target Urho3D
Scanning dependencies of target 05_AnimatingScene
[ 98%] Building CXX object Source/Samples/05_AnimatingScene/CMakeFiles/05_AnimatingScene.dir/AnimatingScene.cpp.o
[100%] Building CXX object Source/Samples/05_AnimatingScene/CMakeFiles/05_AnimatingScene.dir/Rotator.cpp.o
[100%] Linking CXX executable ..\..\..\bin\05_AnimatingScene.js
Traceback (most recent call last):
  File "C:\PROGRA~1\EMSCRI~1\EMSCRI~1\137~1.18\\em++", line 16, in <module>
    emcc.run()
  File "C:\PROGRA~1\EMSCRI~1\EMSCRI~1\137~1.18\emcc.py", line 622, in run
    options, settings_changes, newargs = parse_args(newargs)
  File "C:\PROGRA~1\EMSCRI~1\EMSCRI~1\137~1.18\emcc.py", line 1873, in parse_args
    options.pre_js += open(newargs[i+1]).read() + '\n'
IOError: [Errno 2] No such file or directory: 'C:/Program'
Source\Samples\05_AnimatingScene\CMakeFiles\05_AnimatingScene.dir\build.make:126: recipe for target 'bin/05_AnimatingScene.js' failed
mingw32-make[3]: *** [bin/05_AnimatingScene.js] Error 1
CMakeFiles\Makefile2:1165: recipe for target 'Source/Samples/05_AnimatingScene/CMakeFiles/05_AnimatingScene.dir/all' failed
mingw32-make[2]: *** [Source/Samples/05_AnimatingScene/CMakeFiles/05_AnimatingScene.dir/all] Error 2
CMakeFiles\Makefile2:1177: recipe for target 'Source/Samples/05_AnimatingScene/CMakeFiles/05_AnimatingScene.dir/rule' failed
mingw32-make[1]: *** [Source/Samples/05_AnimatingScene/CMakeFiles/05_AnimatingScene.dir/rule] Error 2
Makefile:391: recipe for target '05_AnimatingScene' failed
mingw32-make: *** [05_AnimatingScene] Error 2
[/spoiler]


----------

So to summarise **(LD;DR)**
- I pulled recently the latest master of Urho3D
- You can see I am using Emscripten SDK version 1.37.18 64bit.
- Web Library build is successful
- **But Samples do *not* build successfully**

I would be happy to provide more information if any wants it. If I can get this to work I will update it here. I think being able to build to WebAssembly is really something awesome and I hope maybe its a thing we can see working at least in 1.7?

P.S. In the mentioned thread I know **cadaver** managed to get building into WebAssembly working, however I have not been able to replicate his process to success obviously. Perhaps I am missing something stupid or using the wrong version of something somewhere?

-------------------------

weitjong | 2017-08-14 15:23:22 UTC | #2

We have CI jobs on WASM build which test build just fine, however, it uses Linux host system and SDK 1.37.12. Personally, I seldom test build on Windows host system and especially when targeting Web platform, so sorry for not able to be more helpful than this. Perhaps try to use a build tree without space and see if it works, probably you have found a bug if that is turned out to be the case.

-------------------------

cadaver | 2017-08-14 15:35:28 UTC | #3

Remembered that my build & Emscripten install paths don't have space in them, so yes, I'd suspect that too.

-------------------------

Synex | 2017-08-14 20:54:53 UTC | #4

I just want to confirm that I was able to build the samples with WebAssembly when using an Emscripten install path that has **no spaces**!

Note the build does not output a .html file for each sample unless you do the following: 
- Specify the flag `URHO3D_TESTING=1` when building 
- **OR** by using the `add_html_shell()` in the appropriate sample/project CMakeList.txt **BEFORE** the `setup_main_executable ()` macro.

An example on using the `add_html_shell ()` macro see below:
### Example of CMakeLists.txt for 02_HelloGUI Sample
[spoiler]
set (TARGET_NAME 02_HelloGUI)

define_source_files (EXTRA_H_FILES ${COMMON_SAMPLE_H_FILES})

add_html_shell ()

setup_main_executable ()

setup_test ()
[/spoiler]

-------------------------

weitjong | 2017-08-15 04:01:05 UTC | #5

That is the expected result. In the previous release, the default output for Web platform was HTML with an unconfigurable basic shell (without modifying the build scripts). In the future release (in master branch now), the default output is either asm.js or WASM depending on the build option. Developers can write their own HTML shell after the fact to integrate with the output. Or use the add_html_shell() macro providing the path to the custom shell to let our build system integrate them for you.

-------------------------

weitjong | 2017-08-19 06:00:34 UTC | #6

I am able to reproduce this error on Linux host system when my test build tree path has spaces. So, I will raise this as an issue.

-------------------------

weitjong | 2017-08-19 07:51:07 UTC | #7

@Synex Could you try the latest commit in the master branch and report back. It should now build correctly with build tree path containing spaces.

-------------------------

Synex | 2017-08-24 19:17:43 UTC | #8

@weitjong I can confirm that the latest commit in master has fixed the issue regarding the build path containing spaces when building on Windows 10

-------------------------

