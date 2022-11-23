roli | 2017-01-02 01:13:58 UTC | #1

Hello, I took an interest in urho3d some time ago, however I hadn't have a chance to check it on my own until now. 

I have two hardware configuration:
Notebook with win7 64 nvidia (dx9c) card and Urho 1.5 built (openGL) - everything works great.
PC win 10 64, intel HD Graphic 530 and Urho 1.5 and 1.6 built (openGL) - graphical artifacts.

In both cases QT Creator (MinGW) was used to build Urho. 

At PC building process was completed without any errors, however I found some issues if its come about Urho3DPlayer.exe. Whenever I run Editor.bat / NinjaSnowWar.bat on 1.6 version I gets an information that Urho3DPlayer has stopped working. In version 1.5 player can be run but it has graphical artifacts.
Most of samples works correctly, but some of them have an artifacts on PC.

Screenshots:
cant post link  :slight_smile: check post bellow please.

So on PC urho v1.5 compiled samples has artifacts and Urho3DPlayer launch without error (but with artifacts as well).
In v1.6 some samples have artifacts and Urho3DPlayer cannot be launched.
I have no idea what is the reason, maybe some hardware issues?

-------------------------

roli | 2017-01-02 01:13:58 UTC | #2

Can't post link in first message on forum (anti spam).
Screenshots:
[imgur.com/a/ie4MP](http://imgur.com/a/ie4MP)

Well it must be something with compilation i believe because running compiled projects from notebook works fine.

-------------------------

Sir_Nate | 2017-01-02 01:14:00 UTC | #3

I'm not saying it is your problem, but make sure you have the up-to-date assets (Data/ and CoreData/) for the version of Urho you're using (if you downloaded the packages it should be fine) -- when I transitioned from Urho1.4 to 1.5 it caused some errors because of missing materials/techniques

-------------------------

roli | 2017-01-02 01:14:01 UTC | #4

I just tried to build urho with several different configurations and any of it wasn't able to finish.
Compile output: [pastebin.com/qparxknU](http://pastebin.com/qparxknU)

There are several warnings in external libs such SDL, AngelScript
and errors:
[code]
Scanning dependencies of target Urho3DPlayer
[ 75%] Building CXX object Source/Tools/Urho3DPlayer/CMakeFiles/Urho3DPlayer.dir/Urho3DPlayer.cpp.obj
[ 75%] Linking CXX executable ..\..\..\bin\Urho3DPlayer.exe
../../../lib/libUrho3D.a(SDL_windowswindow.c.obj):SDL_windowswindow.c:(.text+0x5ac): undefined reference to `WIN_GL_SetupWindow'
collect2.exe: error: ld returned 1 exit status
Source\Tools\Urho3DPlayer\CMakeFiles\Urho3DPlayer.dir\build.make:97: recipe for target 'bin/Urho3DPlayer.exe' failed
mingw32-make.exe[2]: *** [bin/Urho3DPlayer.exe] Error 1
CMakeFiles\Makefile2:1515: recipe for target 'Source/Tools/Urho3DPlayer/CMakeFiles/Urho3DPlayer.dir/all' failed
Makefile:148: recipe for target 'all' failed
mingw32-make.exe[1]: *** [Source/Tools/Urho3DPlayer/CMakeFiles/Urho3DPlayer.dir/all] Error 2
mingw32-make.exe: *** [all] Error 2
19:11:25: The process "C:\Program Files (x86)\CMake\bin\cmake.exe" exited with code 2.
Error while building/deploying project Urho3D (kit: Desktop Qt 5.7.0 MinGW 32bit)
When executing step "Make"
[/code]
The same problem for dx9 and dx11. Somehow opengl compile without error but its has odd graphical artifacts.
Well i guess somehow linker cant find WIN_GL_SetupWindow function, maybe i do the compilation process incorrectly. Investigation in progress :ugeek:

linker errro ~_~
[code][ 74%] Linking CXX executable ..\..\..\bin\Urho3DPlayer.exe
F:/Qt/Tools/mingw492_32/bin/../lib/gcc/i686-w64-mingw32/4.9.2/../../../../i686-w64-mingw32/bin/ld.exe: cannot find -lD3DCompiler_47
F:/Qt/Tools/mingw492_32/bin/../lib/gcc/i686-w64-mingw32/4.9.2/../../../../i686-w64-mingw32/bin/ld.exe: cannot find -lD3DCompiler_47
collect2.exe: error: ld returned 1 exit status[/code]
D3DCompiler_47.dll exist in system32, im going to check what will happen when i change DIRECTX_D3DCOMPILER to D3DCompiler_43.dll
Well, i just returned to starting point :smiley:
[code]../../../lib/libUrho3D.a(SDL_windowswindow.c.obj):SDL_windowswindow.c:(.text+0x5ac): undefined reference to `WIN_GL_SetupWindow'
collect2.exe: error: ld returned 1 exit status[/code]
---
I just compiled with opengl and i dont have artifacts, however when i try to run editor / ninja snow example or even player itself it stops running and exit with segmentation fault >.<
[code]
[1]    2512 segmentation fault  ./Urho3DPlayer.exe
[/code]

-------------------------

roli | 2017-01-02 01:14:07 UTC | #5

I was able to find workaround and compiled engine with VS Preview 2015. For now I will use microsoft vs to play with urho but I really wanted to use QTCreator. 
Because of my lack of experience with Cmake I found some difficulties in setting environment configuration correctly to compile engine using mingw.

[size=75]Sorry for multi posting, but i wanted to bump thread up, I hope you wont be angry :slight_smile:[/size]

-------------------------

weitjong | 2017-01-02 01:14:08 UTC | #6

I think you should not mark the thread as SOLVED when you are still expecting answers from other readers. Anyway, I don't see any reason why our build system could not play nicely with QtCreator IDE. I am not a big fan of Qt but I had tested the QtCreator briefly in the past. If I recall correctly the QtCreator IDE basically just uses CMake/Code::Block generator to generate a project's build tree and uses MinGW as the compiler toolchain. And the fact is our build system supports MinGW rather quite well, both on Windows and Linux host systems. The only problem I can think of is different vendor seems to build and bundle MinGW compiler toolchain slightly differently and may have different dependencies to the version of "d3compiler.dll" depending on which "libd3dcompiler(_xx).a" is being used in the build. Sorry if this does not help you much. Personally I use standalone MinGW installation and use CLI to invoke "cmake" and "make" commands via rake task without any problems so far.

-------------------------

roli | 2017-01-02 01:14:08 UTC | #7

I have not had any issues with compiling project since Urho v1.3 (I believe) up to v1.5 and I used to be using QT creator. That why it was my first thought that the issue I experienced has to be related to the new hardware I bought lately or windows 10.
I will try to reinstall ide, cmake and mingw and install separately. 
Thanks for guidance  :sunglasses:

-------------------------

cadaver | 2017-01-02 01:14:08 UTC | #8

Newer versions of Urho use more graphics API features, which can lead into more problems on questionable GPU drivers. One thing in particular which was recently discovered was "seamless cubemap" which causes problems on some OpenGL configurations. See around line 2380 in OGLGraphics.cpp, and see if disabling the glEnable() makes a difference.  You could also try running in OpenGL 2 compatibility mode by specifying -gl2 command line option.

For OpenGL the used compiler shouldn't have a difference, for Direct3D11 I haven't been able to reliably compile on MinGW exactly due to the D3DCompiler functions not working as expected.

-------------------------

roli | 2017-01-02 01:14:09 UTC | #9

I just did as you said and removed
[code]
        // Enable seamless cubemap if possible
        // Note: even though we check the extension, this can lead to software fallback on some old GPU's
        // See https://github.com/urho3d/Urho3D/issues/1380 or
        // http://distrustsimplicity.net/articles/gl_texture_cube_map_seamless-on-os-x/
        // In case of trouble or for wanting maximum compatibility, simply remove the glEnable below.
//        if (gl3Support || GLEW_ARB_seamless_cube_map)
//            glEnable(GL_TEXTURE_CUBE_MAP_SEAMLESS);
[/code]
Urho3DPlayer started working correctly and all samples run without artifacts.
also I turned off:
SDL_RENDER and SDL_SHARED, im not sure if this affected the build process but your comment helped.

I'll try few different configurations to confirm if it's not random case.

edit
Maybe its not valuable information but the GPU on which I experienced this issues were Intel HD Graphic 530 and GTX 1070.

In the end removing glEnable(GL_TEXTURE_CUBE_MAP_SEAMLESS); don't change anything on default settings. 
The problem is SDL and turning off SDL_RENDER allow to compile without errors and run player without artifacts. It is hard to say any more details because I'm newbie.

-------------------------

