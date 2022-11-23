Lunarovich | 2022-02-20 12:49:25 UTC | #1

Hello! As title says, I want to be able to build Urho3D to use OpenGL on Windows. How does one achieve this with the rake script? 

I've tried setting `URHO3D_OPENGL` env var as well as specifying rake option with `rake build install URHO3D_OPENGL=1` but both fail to work. 

Thank you!

-------------------------

weitjong | 2022-02-20 17:52:59 UTC | #2

On Windows it is not possible to set the env-var on the fly just before invoking the rake command. That is, below only works on *nix host systems and not on Windows.

```
URHO3D_OPENGL=1 rake clean build install
```

The closest you can get on Windows host system is something like this:

```
set "URHO3D_OPENGL=1" && rake clean build install
```

In the past I had use a "hack" to feed the rake parameters that looks like "key=value" back into the build system to achieve the feature parity between the systems. However, it was at a cost that the rake could only invoke one task at a time.

```
rake cmake URHO3D_OPENGL=1 && rake make
```

The latest rake build script in the main branch does not use this hack anymore. But as you can see it can now chain many tasks in one line. And user on the *nix host systems do not lose anything aside from setting the env-var earlier on in the command line.

BTW, you can always fallback to invoke "cmake" directly in the command line and that's when you need to prefix the option with "-D".

-------------------------

Lunarovich | 2022-02-21 00:06:40 UTC | #3

[quote="weitjong, post:2, topic:7196"]
`rake clean build install`
[/quote]

Thank you very much for this clarification. I did the following in Developer PowerShell VS 2019:

```
$env:URHO3D_OPENGL=1
rake clean build install
```
However, my build still uses HLSL shaders... Do I need to use cmd prompt for this to work?

EDIT: I've just tried `set "URHO3D_OPENGL=1" && rake clean build install` in the Developer Cmd Promt VS 2019 and it still does not build with the OpenGL backend. The apps still use HLSL.

-------------------------

SirNate0 | 2022-02-21 07:26:00 UTC | #4

Are you sure your app is building against the OpenGL built library, and not another version you have installed?

I don't use the rake tools myself, but I believe you still end up with a CMakeCache.txt somewhere, right? If you look in it, is the URHO3D_OPENGL flag set?

-------------------------

Lunarovich | 2022-02-21 11:08:28 UTC | #5

I've manged to build a library with an OpenGL renderer by using CMake GUI and settings `URHO3D_OPENGL` there. 

I'm now trying to use `ninja` generator with the following command in my project 
```
cmake.exe -GNinja .. -DCMAKE_EXPORT_COMPILE_COMMANDS=ON -DCMAKE_MAKE_PROGRAM:STRING="c:/Program Files (x86)/Microsoft Visual Studio/2019/BuildTools/Common7/IDE/CommonExtensions/Microsoft/CMake/Ninja/ninja.exe" -DURHO3D_HOME='C:/Users/darko/.urho3d/install/win'
```
The main reason I'm doing this is to get `compile_commands.json` file to use it with Emacs (my preferred editor) for linting. However, I get this error: "Could NOT find compatible Urho3D library in Urho3D SDK installation". I've also tried setting the env var in PowerShell, but does not seem to work.

-------------------------

weitjong | 2022-02-21 11:14:00 UTC | #6

I don't know what exactly happened to your case, but I can confirm that setting the "URHO3D_OPENGL" env-var to 1 in the last CI/CD build on the main branch still does the build with expected build combination.

[CI cmake step](https://github.com/urho3d/Urho3D/runs/5191218365?check_suite_focus=true#step:4:141)
[CI build step](https://github.com/urho3d/Urho3D/runs/5191218365?check_suite_focus=true#step:5:2333)

Our CI/CD uses the new rake build system, so it should work. Make sure you don't have something like "URHO3D_D3D11" env-var defined globally. Also, when in doubt, there is no harm to try to clear the CMake-cache or try build with a new build tree.

-------------------------

weitjong | 2022-02-22 13:57:45 UTC | #7

BTW, you can also invoke the rake `cmake ` task with GENERATOR env-var set to “ninja” in order to generate build tree with ninja-build. Unfortunately though, currently the default setup does not include CMAKE_EXPORT_COMPILE_COMMANDS and CMAKE_MAKE_PROGRAM as valid and processable build options in respect to rake build system. But that is easy to fix. Just simply add them as two new entries in the script/.build-options file and you should be all good.

```
GENERATOR=ninja CMAKE_EXPORT_COMPILE_COMMANDS=1 CMAKE_MAKE_PROGRAM=/path/to/custom/make rake cmake
```

Calling `build` task will automatically invoke `cmake` task as well, so you normally don’t need to invoke it explicitly. However, I just want to explain it here to let you guys know that rake build system understood task dependencies.

I just typed this post using my iPad without actually validating any of the command. It is just based on what I have remembered the capability of the new build system. You may need to adjust the command as required to get it run.

-------------------------

Lunarovich | 2022-02-22 15:05:50 UTC | #8

I've managed to congigure and generate `build.ninja` file with cmake-gui. However, I get this message:

```
[3/1386] Building C object Source/ThirdParty/SDL/CMakeFiles/SDL.dir/src/audio/SDL_audiocvt.c.obj
FAILED: Source/ThirdParty/SDL/CMakeFiles/SDL.dir/src/audio/SDL_audiocvt.c.obj
C:\PROGRA~1\LLVM\bin\clang.exe -DSDL_STATIC_LIB -DURHO3D_ANGELSCRIPT -DURHO3D_FILEWATCHER -DURHO3D_IK -DURHO3D_LOGGING -DURHO3D_LUA -DURHO3D_NAVIGATION -DURHO3D_NETWORK -DURHO3D_PHYSICS -DURHO3D_PHYSICS2D -DURHO3D_PROFILING -DURHO3D_STATIC_DEFINE -DURHO3D_THREADING -DURHO3D_URHO2D -DURHO3D_WEBP -DUSING_GENERATED_CONFIG_H -IC:/Users/darko/Documents/Urho3D/build/Source/ThirdParty/SDL/include/generated -IC:/Users/darko/Documents/Urho3D/Source/ThirdParty/SDL/include -mtune=generic  -march=native -msse3 -pthread -Qunused-arguments -fcolor-diagnostics -Wno-argument-outside-range  -I"C:/Users/darko/Documents/Urho3D/Source/ThirdParty/SDL/src/hidapi/hidapi" -fcommon -Wshadow -Wdeclaration-after-statement -Werror=declaration-after-statement -fno-strict-aliasing -Wall  -g -Xclang -gcodeview -O0 -D_DEBUG -D_DLL -D_MT -Xclang --dependent-lib=msvcrtd -DDEBUG -D_DEBUG -MD -MT Source/ThirdParty/SDL/CMakeFiles/SDL.dir/src/audio/SDL_audiocvt.c.obj -MF Source\ThirdParty\SDL\CMakeFiles\SDL.dir\src\audio\SDL_audiocvt.c.obj.d -o Source/ThirdParty/SDL/CMakeFiles/SDL.dir/src/audio/SDL_audiocvt.c.obj -c C:/Users/darko/Documents/Urho3D/Source/ThirdParty/SDL/src/audio/SDL_audiocvt.c
C:/Users/darko/Documents/Urho3D/Source/ThirdParty/SDL/src/audio/SDL_audiocvt.c:59:15: error: unknown type name '__m128'
```
and few other errors.

I probably miss some dependencies.

-------------------------

weitjong | 2022-02-23 02:09:49 UTC | #9

You don't provide us with much information to troubleshoot your build issue. You can use cmake-gui to freely turn on/off some build options at your own peril :slight_smile: Perhaps you have enabled SSE/AVX at too high a level that your CPU could support. I don't know for sure as you didn't mention anything on how you generated your build tree in detail.

-------------------------

Lunarovich | 2022-02-23 07:57:44 UTC | #10

@weitjong thnx for your effort!

I'm actually trying **to build Urho3D itself** with the **Ninja and Clang**. I don't do anything special. I just clone the repository, I fire the cmake-gui. I set the source to `C:/Users/darko/Documents/Urho3D` and build to `C:/Users/darko/Documents/Urho3D/build`. Then I specify the Ninja generator and run Configure twice, without changing any of the options, then I do Generate and I run `ninja` in `build` folder. 

I'm running a clean build and I'm running it in the Developer VS 2019 PowerShell. So, the build tree is actually just an official github repo.

-------------------------

1vanK | 2022-02-23 09:55:32 UTC | #11

Some time ago I experimented with Clang on Windows. It seems Windows SDK just is incompatible with Clang. So Visual Studio compiler and MinGW these are the only options available on Windows for building the engine

-------------------------

Lunarovich | 2022-02-23 13:25:24 UTC | #12

OK, thnx, I'll tryout mingw build. Basically, what I need is a `compile_commands.json` file to use with `clangd` language server (in Emacs editor). So if anyone knows how to get `compile_commands.json` without using mingw32-make or ninja, please let me know.

EDIT: In my project `build` directory, I have used all of the
```
URHO3D_HOME=/c/Users/darko/.urho3d/mingw/ cmake -G"MinGW Makefiles" ..
URHO3D_HOME=/c/Users/darko/.urho3d/mingw/ cmake -G"Ninja" ..
URHO3D_HOME=/c/Users/darko/.urho3d/mingw/ cmake -G"Unix Makefiles" ..
 ```
and everything works just fine. I can compile and link my executable with one of the following:
```
mingw32-make.exe # for -G"MinGW Makefiles"
ninja # for -G"Ninja"
```

However, I'm kind of puzzled by what exactly compiler and linker does these commands use. I guess they use `/mingw64/bin/gcc` for a compiler. But as to the linker, I am clueless. The only linker I can find is `C:\msys64\usr\bin\link.exe` but that linker belongs to the MSYS2 suite...

-------------------------

JTippetts1 | 2022-02-23 14:34:11 UTC | #13

mingw uses ar.exe to link.

-------------------------

weitjong | 2022-02-23 15:22:11 UTC | #14

1vanK is correct. Our current support matrix only supports Clang on Linux and Apple Clang on macOS/iOS/tvOS; and MSVC or MinGW-w64 on Windows. The Clang on Windows is not supported yet, although it is not entirely impossible. Someone just needs to get their hand dirty to undo the "wrong" assumption in the setup whenever configuring the Clang compiler toolchain in all the build script. For instance, we could have a block of logic where the setup is the same for Clang and GCC because the two are drop-in replacement of each other, however, that may not be true anymore when it is targeting Windows platform.

Re. the "CMAKE_EXPORT_COMPILE_COMMANDS", it appears since 3.17 CMake recognizes it as both CMake variable as well as CMake env-var. Thus, setting this env-var globally/locally will have similar effect during the initial build tree generation. Note that, once the build tree is generated then the value is already bake-in and changing the variable or env-var has no impact at all to the already generated build tree.

[CMAKE_EXPORT_COMPILE_COMMANDS as env-var](https://cmake.org/cmake/help/latest/envvar/CMAKE_EXPORT_COMPILE_COMMANDS.html#envvar:CMAKE_EXPORT_COMPILE_COMMANDS)
[CMAKE_EXPORT_COMPILE_COMMANDS as variable](https://cmake.org/cmake/help/latest/variable/CMAKE_EXPORT_COMPILE_COMMANDS.html#variable:CMAKE_EXPORT_COMPILE_COMMANDS)

In other words `CMAKE_EXPORT_COMPILE_COMMANDS=1 rake cmake` should work out of the box as CMake 3.17++ itself knows how to deal with it as env-var. And most importantly, do this on a blank sheet where the build tree has not been generated yet.

-------------------------

Lunarovich | 2022-02-23 16:26:07 UTC | #15

My problem consists in the fact that "CMAKE_EXPORT_COMPILE_COMMANDS" has no effect on MSVC generator. CMake simply ignores it. In order to get `compile_commands.json` one has to either generate project with Ninja, MingW or Make generator.

I've succeded in generating it witn MingW on Windows. Once I did it, I wanted to feed MingW's `clangd` with it. However, the `clangd` was constantly crashing (I did it by means of Emacs). Now, however, I've tried this in Powershell 

```
$env:URHO3D_HOME='C:\Users\darko\.urho3d\msvc\'
cmake -G"Ninja" .. -DURHO3D_ANGELSCRIPT=0 -DURHO3D_LUA=0 -DURHO3D_URHO2D=0 -DURHO3D_IK=0 -DURHO3D_NETWORK=0 -DURHO3D_PHYSICS2D=0 -DURHO3D_WEBP=0 -DCMAKE_MAKE_PROGRAM:STRING="c:/Program Files (x86)/Microsoft Visual Studio/2019/BuildTools/Common7/IDE/CommonExtensions/Microsoft/CMake/Ninja/ninja.exe" ..
```
and for some reason, it worked, i.e. i've succeded in configuring the build. However, the build itself does not work and fails with

```
PS C:\Users\darko\Development\persistence\ninja> & "c:/Program Files (x86)/Microsoft Visual Studio/2019/BuildTools/Common7/IDE/CommonExtensions/Microsoft/CMake/Ninja/ninja.exe"
[2/2] Linking CXX executable bin\Persistence_d.exe
FAILED: bin/Persistence_d.exe
cmd.exe /C "cd . && C:\PROGRA~1\LLVM\bin\CLANG_~1.EXE -fuse-ld=lld-link -nostartfiles -nostdlib -mtune=generic  -Wno-invalid-offsetof -march=native -msse3 -pthread -Qunused-arguments -fcolor-diagnostics -Wno-argument-outside-range -g -Xclang -gcodeview -O0 -D_DEBUG -D_DLL -D_MT -Xclang --dependent-lib=msvcrtd -DDEBUG -D_DEBUG -Xlinker /subsystem:windows CMakeFiles/Persistence.dir/Source/Application.cpp.obj -o bin\Persistence_d.exe -Xlinker /implib:Persistence_d.lib -Xlinker /pdb:bin\Persistence_d.pdb -Xlinker /version:0.0   C:/Users/darko/.urho3d/msvc/lib/Urho3D.lib  -luser32.lib  -lgdi32.lib  -lwinmm.lib  -limm32.lib  -lole32.lib  -loleaut32.lib  -lsetupapi.lib  -lversion.lib  -luuid.lib  -lws2_32.lib  -liphlpapi.lib  -lwinmm.lib  -lopengl32.lib  -limm32.lib  -lole32.lib  -loleaut32.lib  -lsetupapi.lib  -lversion.lib  -luuid.lib  -lws2_32.lib  -liphlpapi.lib  -lopengl32.lib  -lkernel32 -luser32 -lgdi32 -lwinspool -lshell32 -lole32 -loleaut32 -luuid -lcomdlg32 -ladvapi32 -loldnames && cd ."
lld-link: error: /failifmismatch: mismatch detected for '_ITERATOR_DEBUG_LEVEL':
>>> CMakeFiles/Persistence.dir/Source/Application.cpp.obj has value 2
>>> Urho3D.lib(Application.obj) has value 0
clang++: error: linker command failed with exit code 1 (use -v to see invocation)
ninja: build stopped: subcommand failed.
```

However, I got mine `compile_commands.json` that works well with windows native `clangd`.

So, to wrap it up, Ninja generator actually works on Windows, for projects and for Urho3D itself. However, the build files cannot be used to build Urho3D or project. Nevertheless, `compile_commands.json` is generated in the generate step.

-------------------------

weitjong | 2022-02-23 17:31:55 UTC | #16

I think you made a mistake in your command. You passed the path to ninja.exe into the variable that expecting a path to make program. 

As for the compile command export, I have no idea whether VS generator supports it. But I would believe ninja generator should, so does the Makefile generator.

-------------------------

Lunarovich | 2022-02-24 11:08:56 UTC | #17

> I think you made a mistake in your command. You passed the path to ninja.exe into the variable that expecting a path to make program.

Actually, this is a name of the executable of the any tool such as Ninja, Make, etc. Please see here [here ](https://cmake.org/cmake/help/latest/variable/CMAKE_MAKE_PROGRAM.html).

> As for the compile command export, I have no idea whether VS generator supports it. But I would believe ninja generator should, so does the Makefile generator.

I'm in a specific situation of wanting to use Emacs on Windows and that compilcates stuff. Makefile generators and ninja.build generators can make `compile_commands.json`. However, if you use MingW on Windows, your `compile_commands.json` will be compatible with the `clangd` of the mingw suite. In Emacs, `clangd` for mingw crashes for an unknown reason to me. But as I said, I was able to use Windows native ninja as a generator, so as long as the Ninja configure/generate works for Windows natively, I'm good to go.

-------------------------

weitjong | 2022-02-24 18:24:11 UTC | #19

I have deleted my earlier post :slight_smile: 
I think I was the one that got confused and the CMake document is correct about ninja generator.

-------------------------

