Bluemoon | 2017-01-02 01:06:42 UTC | #1

I'm trying to build an Emscripten version of Urho3D but am getting an error that I can't really explain well . This is my first time trying out emscripten and I'm sure am definitely doing something wrong. This error shows up when the build reaches the stage for building samples
[code]
Linking CXX executable ..\..\..\bin\01_HelloWorld.html
WARNING  root: loading from archive C:\Urho3D_Build\Urho3D_Git\Build\lib\libUrho
3D.a, which has duplicate entries (files with identical base names). this is dan
gerous as only the last will be taken into account, and you may see surprising u
ndefined symbols later. you should rename source files to avoid this problem (or
 avoid .a archives, and just link bitcode together to form libraries for later l
inking)
WARNING  root:    duplicate: merge.bat
Traceback (most recent call last):
  File "C:\PROGRA~1\EMSCRI~1\EMSCRI~1\134~1.1\emcc", line 1260, in <module>
    shared.Building.llvm_opt(final, link_opts)
  File "C:\PROGRA~1\EMSCRI~1\EMSCRI~1\134~1.1\tools\shared.py", line 1429, in ll
vm_opt
    assert os.path.exists(target), 'Failed to run llvm optimizations: ' + output

AssertionError: Failed to run llvm optimizations:
Source\Samples\01_HelloWorld\CMakeFiles\01_HelloWorld.dir\build.make:91: recipe
for target 'bin/01_HelloWorld.html' failed
mingw32-make[2]: *** [bin/01_HelloWorld.html] Error 1
CMakeFiles\Makefile2:1073: recipe for target 'Source/Samples/01_HelloWorld/CMake
Files/01_HelloWorld.dir/all' failed
mingw32-make[1]: *** [Source/Samples/01_HelloWorld/CMakeFiles/01_HelloWorld.dir/
all] Error 2
makefile:135: recipe for target 'all' failed
mingw32-make: *** [all] Error 2
[/code]

-------------------------

weitjong | 2017-01-02 01:06:44 UTC | #2

We (at least I) haven't upgraded and tried the build with 1.34.x. Emscripten team is busy at work as usual. It is not the first time I found their newer releases break our build requiring us to make corresponding adjustment on our side and/or forcing us to send PR upstream to fix them. But I am not sure yet if that is your problem here. Could you temporarily downgrade to 1.33.x and see how far you can go with that version. If it is ok with 1.33 then you know you haven't done something wrong with your setup.

-------------------------

weitjong | 2017-01-02 01:06:50 UTC | #3

Got time to investigate the SDK master branch release 1.34 today. It built fine on my Linux host system. I am upgrading the Emscripten toolchain for our CI build from 1.33.1 (incoming) to 1.34 (master) as I speak. If everything goes smoothly then the next Emscripten CI build will be using 1.34.

-------------------------

Bluemoon | 2017-12-11 18:09:35 UTC | #4

So I came back again to try emscripten on my Windows 10 machine but made no head way. cmake_emscripten.bat won't even run given me error of

> CMake Error at CMake/Toolchains/Emscripten.cmake:68 (message):
  Could not find Emscripten cross compilation tool.  Use EMSCRIPTEN_ROOT_PATH
  environment variable or build option to specify the location of the
  toolchain.  Or use the canonical EMSCRIPTEN environment variable by calling
  emsdk_env script.
Call Stack (most recent call first):
  C:/Program Files (x86)/CMake/share/cmake-3.5/Modules/CMakeDetermineSystem.cmake:98 (include)
  CMakeLists.txt:39 (project)
CMake Error: CMAKE_C_COMPILER not set, after EnableLanguage
CMake Error: CMAKE_CXX_COMPILER not set, after EnableLanguage
-- Configuring incomplete, errors occurred!

I actually ran it as 
>cmake_emscripten.bat ../urho_web  EMSCRIPTEN_ROOT_PATH=C:\emsdk\emscripten\1.37.22

My Urho3D version is the master as at 2017-12-10 (yesterday at the time of this post) and my emscripten version is 1.37.22. I actually followed the installation guide of emscripten carefully and equally set up its environment variable but somehow the value of EMSCRIPTEN_ROOT_PATH in  CMake/Toolchains/Emscripten.cmake evaluates to C:/Program Files/Emscripten/emscripten/1.34.4. I have no idea where that came from.

A few guidance would be highly appreciated :sweat_smile::sweat_smile::sweat_smile:

-------------------------

weitjong | 2017-12-12 02:26:04 UTC | #5

Clearly it’s just a development environment setup problem. I have not tried to target Web platform on Windows host but I believe the environment setup should be similar to Linux.

* Download the EM portable SDK (manager)
* Activate one of the EM SDK (and Binaryen as well if want to use WASM instead of asm.js)
* Invoke the `emsdk_env` shell/batch file which sets the environment variables (only required to do for subsequent environment setup, unless you have hard-wired those variables in your account’s profile which get set each time you login)
* Invoke our CMake script and make as usual. On my box this is achieved in a one liner: `rake cmake web && rake make web`

Note the common cross-compiling pitfall on Windows though. Our build system requires both cross-compiler and native compiler toolchains to be available in the system PATH. This is almost the case for any Linux host with dev packages installed. On Windows this is not so, and you have to take care of it yourself. Usually by having a MinGW compiler toolchain in your path would help. Good luck.

-------------------------

Bluemoon | 2020-10-06 12:58:17 UTC | #6

After some years I decided to return back to this and try emscripten once again. Long story short I still had build errors but I consider it as progress nonetheless. 

This error however is of the compiler complaining of redefinition of classes and I am confused why it should be so. 

Setup:
> os: win10
Emscripten SDK: v2.0.4
Urho3D version: current master as at time of reporting https://github.com/urho3d/Urho3D/tree/ebd7633f8916149212159d4a1cccfe1ac70c1da5 

Error output:
> [ 76%] Building CXX object Source/Urho3D/CMakeFiles/Urho3D.dir/Graphics/Model.cpp.o
> [ 77%] Building CXX object Source/Urho3D/CMakeFiles/Urho3D.dir/Graphics/OcclusionBuffer.cpp.o
> [ 77%] Building CXX object Source/Urho3D/CMakeFiles/Urho3D.dir/Graphics/Octree.cpp.o
> [ 77%] Building CXX object Source/Urho3D/CMakeFiles/Urho3D.dir/Graphics/OctreeQuery.cpp.o
> [ 77%] Building CXX object Source/Urho3D/CMakeFiles/Urho3D.dir/Graphics/OpenGL/OGLConstantBuffer.cpp.o
> [ 77%] Building CXX object Source/Urho3D/CMakeFiles/Urho3D.dir/Graphics/OpenGL/OGLGraphics.cpp.o
> In file included from C:\urho3d\urho3d_git\Source\Urho3D\Graphics\OpenGL\OGLGraphics.cpp:56:
> In file included from C:/urho3d/urho3d_git/web2/include/Urho3D/ThirdParty\../Input/Input.h:27:
> C:/urho3d/urho3d_git/web2/include/Urho3D/ThirdParty\../Input/../Container/FlagSet.h:46:7: error: redefinition of 'FlagSet'
> class FlagSet
>       ^
> C:\urho3d\urho3d_git\Source\Urho3D\Graphics\OpenGL/../../Graphics/../Container/FlagSet.h:46:7: note: previous definition is here
> class FlagSet
>       ^
> In file included from C:\urho3d\urho3d_git\Source\Urho3D\Graphics\OpenGL\OGLGraphics.cpp:56:
> In file included from C:/urho3d/urho3d_git/web2/include/Urho3D/ThirdParty\../Input/Input.h:28:
> In file included from C:/urho3d/urho3d_git/web2/include/Urho3D/ThirdParty\../Input/../Container/HashSet.h:25:
> In file included from C:/urho3d/urho3d_git/web2/include/Urho3D/ThirdParty\../Input/../Container/../Container/HashBase.h:31:
> C:/urho3d/urho3d_git/web2/include/Urho3D/ThirdParty\../Input/../Container/../Container/Allocator.h:40:8: error: redefinition of 'AllocatorBlock'
> struct AllocatorBlock
>        ^
> C:/urho3d\urho3d_git\Source\Urho3D\Container/../Container/Allocator.h:40:8: note: previous definition is here
> struct AllocatorBlock
>        ^
> In file included from C:\urho3d\urho3d_git\Source\Urho3D\Graphics\OpenGL\OGLGraphics.cpp:56:
> In file included from C:/urho3d/urho3d_git/web2/include/Urho3D/ThirdParty\../Input/Input.h:28:
> In file included from C:/urho3d/urho3d_git/web2/include/Urho3D/ThirdParty\../Input/../Container/HashSet.h:25:
> In file included from C:/urho3d/urho3d_git/web2/include/Urho3D/ThirdParty\../Input/../Container/../Container/HashBase.h:31:
> C:/urho3d/urho3d_git/web2/include/Urho3D/ThirdParty\../Input/../Container/../Container/Allocator.h:54:8: error: redefinition of 'AllocatorNode'
> struct AllocatorNode
>        ^
> C:/urho3d\urho3d_git\Source\Urho3D\Container/../Container/Allocator.h:54:8: note: previous definition is here
> struct AllocatorNode

Just to be sure nothing is wrong with the source files ( which I am assure I didn't touch any code in it) I had to build for windows platform using mingw and everything built well. 

From the little I could investigate, it turned out that the compiler was referencing two different sets of header files; one in ${urho3d-dir}/${build-folder}/include and the other header files in the same folder as their respective source file in  ${urho3d-dir}/Source/Urho3D.

I would really appreciate any assistance here to help me resolve this.

Thanks

-------------------------

Bluemoon | 2020-10-08 01:50:47 UTC | #7

:grinning:
So I finally got it resolved. Turns out that `Source/Urho3D/Graphics/OpenGL/OGLGraphics.cpp` had this line
```
#ifdef __EMSCRIPTEN__
#include "../Input/Input.h"
#include "../UI/Cursor.h"
#include "../UI/UI.h"
```

Which has a wrong relative include. So I changed it to
```
#ifdef __EMSCRIPTEN__
#include "../../Input/Input.h"
#include "../../UI/Cursor.h"
#include "../../UI/UI.h"
```
...and the build succeeded without errors. Just to be sure, I tried compiling a sample application with the resulting lib and it was successful too.

A PR with the fix has been submitted on github.

-------------------------

Modanung | 2020-10-08 08:01:59 UTC | #8

Good tidings. :slightly_smiling_face:

-------------------------

