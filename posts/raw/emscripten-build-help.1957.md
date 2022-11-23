miz | 2017-01-02 01:11:49 UTC | #1

I can't seem to get the samples to work with emscripten.

I have followed instructions at the end of this post [url]http://discourse.urho3d.io/t/emscripten-support/812/105[/url]

(I am on Windows and already have Mingw installed and added to my path)

Steps I have taken:
- Installed Emscripten
- set EMSCRIPTEN_ROOT_PATH
- cd into Urho3d folder
- run cmake_emscipten.bat ../WebBuild
- cd ../WebBuild
- mingw32-make

everything seems to build fine until the error:

[ 48%] Performing build step for 'tolua++'
'C:/Program' is not recognized as an internal or external command,
operable program or batch file.
Source\Urho3D\CMakeFiles\tolua++.dir\build.make:109: recipe for target 'Source/Urho3D/tolua++-prefix/src/tolua++-stamp/tolua++-build' failed
mingw32-make[2]: *** [Source/Urho3D/tolua++-prefix/src/tolua++-stamp/tolua++-build] Error 1
CMakeFiles\Makefile2:1091: recipe for target 'Source/Urho3D/CMakeFiles/tolua++.dir/all' failed
mingw32-make[1]: *** [Source/Urho3D/CMakeFiles/tolua++.dir/all] Error 2
Makefile:148: recipe for target 'all' failed
mingw32-make: *** [all] Error 2


I can't find where it's trying to use something with 'C:/Program' in it. I presume it is a reference to 'C:/Program Files' but without quotes that's making it break but I can't find how/where to change something.

Any Ideas?
Thanks

-------------------------

weitjong | 2017-01-02 01:11:49 UTC | #2

I may not able to help you much because I don't do Emscripten build on Windows host but you should be able to troubleshoot this yourself step by step. The requirement to also have native compiler toolchain setup besides Emscripten is due to our build system now configures to use Lua subsystem by default, which forces our build system to build a host tool (using native compiler) in order to generate Lua script API binding on the fly during build. When it works then it works beautifully but when it does not then it needs more time to troubleshoot. So, to get started slowly, I would suggest you to regenerate your build tree from scratch again but without the enabling the Lua subsystem (use -DURHO3D_LUA=0 if you are using CLI) this time. Verify your build is OK first with Emscripten compiler toolchain alone.

Once you get that work out then you can reconfigure your build tree to re-enable the Lua subsystem again later. Probably you will get the same problem afterward (if you have not changed any of your setup). Use the log messages to troubleshoot. This line clearly shows where the problem was.

[code]Source\Urho3D\CMakeFiles\tolua++.dir\build.make:109: recipe for target 'Source/Urho3D/tolua++-prefix/src/tolua++-stamp/tolua++-build'[/code]

 It even gave the line number, 109. That "Source\Urho3D\CMakeFiles\tolua++.dir\build.make" should be in your build tree. Your suspicion that it has something to do "Program Files"  is as good as any of our guess. Our build system has been tested with spaces in the source tree and build tree paths previously, but I am not surprise if there is still bug here and there especially on Windows host system.

-------------------------

miz | 2017-01-02 01:11:50 UTC | #3

Just to update, I managed to build samples etc. with -DURHO3D_LUA=0 and -DURHO3D_PACKAGING=0.

-------------------------

hdunderscore | 2017-01-02 01:11:50 UTC | #4

Did you happen to run emmake?

-------------------------

miz | 2017-01-02 01:11:50 UTC | #5

I did not run emmake. Have you used it? How?

-------------------------

hdunderscore | 2017-01-02 01:11:50 UTC | #6

Nah I was getting an error like that when I was used emmake, you shouldn't use it at all on the latest urho.

-------------------------

cadaver | 2017-01-02 01:11:53 UTC | #7

Hmm, I was trying to build on Emscripten 1.35.0 on Windows to test the vertexdeclaration branch, however I got a situation where SDL's CMake fails to find OpenGL ES, which results in the Emscripten video code not compiled and later missing reference errors. Anyone seen similar? Tested also a clean checkout of the master branch, with same result. I believe I built successfully a few weeks ago, when testing the input changes.

[code]
D:\Lasse\Programs\urho3d\Source\ThirdParty\SDL\src\video\emscripten\SDL_emscript
envideo.c:106:30: error:
      use of undeclared identifier 'Emscripten_GLES_LoadLibrary'
    device->GL_LoadLibrary = Emscripten_GLES_LoadLibrary;
                             ^
D:\Lasse\Programs\urho3d\Source\ThirdParty\SDL\src\video\emscripten\SDL_emscript
envideo.c:107:33: error:
      use of undeclared identifier 'Emscripten_GLES_GetProcAddress'
    device->GL_GetProcAddress = Emscripten_GLES_GetProcAddress;
                                ^
D:\Lasse\Programs\urho3d\Source\ThirdParty\SDL\src\video\emscripten\SDL_emscript
envideo.c:108:32: error:
      use of undeclared identifier 'Emscripten_GLES_UnloadLibrary'
    device->GL_UnloadLibrary = Emscripten_GLES_UnloadLibrary;
                               ^
D:\Lasse\Programs\urho3d\Source\ThirdParty\SDL\src\video\emscripten\SDL_emscript
envideo.c:109:32: error:
      use of undeclared identifier 'Emscripten_GLES_CreateContext'; did you mean

      'emscripten_webgl_create_context'?
    device->GL_CreateContext = Emscripten_GLES_CreateContext;
                               ^~~~~~~~~~~~~~~~~~~~~~~~~~~~~
                               emscripten_webgl_create_context
[/code]

-------------------------

weitjong | 2017-01-02 01:11:53 UTC | #8

I have not seen this error. How did you know the error was caused by SDL's CMake detection failure? Did you use the generated SDL_config.h in the build tree to verify that? Here are some values that should exist in that file.

[code]#define SDL_VIDEO_DRIVER_EMSCRIPTEN 1

#define SDL_VIDEO_RENDER_OGL_ES 1
#define SDL_VIDEO_RENDER_OGL_ES2 1

#define SDL_VIDEO_OPENGL_ES 1
#define SDL_VIDEO_OPENGL_ES2 1

#define SDL_VIDEO_OPENGL_EGL 1
[/code]

I am using 1.36.0 on my Linux host system. Those are my auto-detected values.

-------------------------

cadaver | 2017-01-02 01:11:54 UTC | #9

I just looked at the log output it printed while configuring, all OpenGL & GLES related prints indicated false. I will try compiling Emscripten 1.36.0 next, in case that's the culprit.

-------------------------

cadaver | 2017-01-02 01:11:54 UTC | #10

Ok, I've pinpointed the commit where this issue starts happening for me on Windows. It's 929d8acbae0627ebec57b343775e6d6f67f60675 (27th March). Using Emscripten 1.36.0 didn't fix it. The output I get is

[code]
-- Performing Test HAVE_VIDEO_OPENGL_EGL
-- Performing Test HAVE_VIDEO_OPENGL_EGL - Failed
-- Performing Test HAVE_VIDEO_OPENGLES_V1
-- Performing Test HAVE_VIDEO_OPENGLES_V1 - Failed
-- Performing Test HAVE_VIDEO_OPENGLES_V2
-- Performing Test HAVE_VIDEO_OPENGLES_V2 - Failed
...
--   VIDEO_COCOA            (Wanted: OFF): OFF
--   VIDEO_DIRECTFB         (Wanted: OFF): OFF
--   VIDEO_DUMMY            (Wanted: ON): ON
--   VIDEO_MIR              (Wanted: ON): OFF
--   VIDEO_OPENGL           (Wanted: ON): OFF
--   VIDEO_OPENGLES         (Wanted: ON): OFF
--   VIDEO_RPI              (Wanted: OFF): OFF
--   VIDEO_VIVANTE          (Wanted: ON): OFF
--   VIDEO_WAYLAND          (Wanted: ON): OFF
--   VIDEO_WAYLAND_QT_TOUCH (Wanted: OFF): OFF
--   VIDEO_X11              (Wanted: ON): OFF
[/code]
In previous revisions it wouldn't run the OpenGL tests as part of SDL's CMake at all for Emscripten. I wonder if it's actually inspecting the native compiler's capability for GLES support (which would likely be false on Windows) instead of Emscripten's. A simple hack fix would probably be to always assume GLES support when compiling for Emscripten?

-------------------------

cadaver | 2017-01-02 01:11:54 UTC | #11

Ah, indeed it used to do that, as that commit changed

[code]
      set(SDL_VIDEO_OPENGL_EGL 1)
      set(HAVE_VIDEO_OPENGLES TRUE)
      set(SDL_VIDEO_OPENGL_ES2 1)
      set(SDL_VIDEO_RENDER_OGL_ES2 1)
[/code]
to:

[code]
      CheckOpenGLES()
[/code]

-------------------------

weitjong | 2017-01-02 01:11:54 UTC | #12

I tried to minimize hard-coding and reuse the checking/detecting code as much as possible. At the time I was doing this, I was always asking myself with this question: why or how much should it be auto-detected? For a "closed" platform with a "closed" compiler toolchain, what being detected in my CMake should be the same as anyone else. So, arguably we could just reuse the same generated "SDL_config_<platform>.h" as in the way of the past. The generated "SDL_config.h" file would only be different for those "open" platforms or those with variety of compiler toolchains. However, as I have spent too much time already on this, I just left the things as the "original" SDL's CMakeLists.txt intended to do, i.e. auto-detect on each platforms (closed or open).

Anyway, I see no particular reason why Emscripten on Windows could not pass the test. The check in question should be already using target compiler toolchain (not host/native compiler toolchain). In this case, I think the SYSROOT could be wrongly set and cause the "#include <EGL/egl.h>" or "#include <GLES/gl.h>" preprocessors not able to find the headers and failed the test. Could you output the the SYSROOT variable value and browse to that location on your host system to see whether it points to correct system root for Emscripten? Another possibility is the SYSROOT path contains a space?

-------------------------

weitjong | 2017-01-02 01:11:54 UTC | #13

In a quick test on my Linux host system, I found that Emscripten compiler toolchain actually does not rely on "--sysroot" compiler flag. It seems it has hard-wired that path somehow. So, the check would be successful anyway when the whole "--sysroot=${SYSROOT}" is being removed. However, we could not remove this because other compilers may require it. Still, there was a bug in the CMake module when dealing a SYSROOT path with a space and I have just fixed that. Can you try again to see if it fixes your problem.

-------------------------

cadaver | 2017-01-02 01:11:55 UTC | #14

It works now, thanks! Indeed my sysroot contained a space as it's the default install path (C:/Program Files/Emscripten/emscripten/tag-1.36.0/system)

-------------------------

