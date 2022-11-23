att | 2021-08-14 15:51:46 UTC | #1

I downloaded the latest source and try to build for mac platform, but failed.
this is the failing log:

> Blockquote
ld: warning: ignoring file /usr/local/Cellar/readline/8.1/lib/libreadline.dylib, building for macOS-arm64 but attempting to link with file built for macOS-x86_64
Undefined symbols for architecture arm64:
  "_add_history", referenced from:
      _dotty in lua.o
  "_readline", referenced from:
      _pushline in lua.o
ld: symbol(s) not found for architecture arm64
clang: error: linker command failed with exit code 1 (use -v to see invocation)

Ld build/macos/Source/ThirdParty/Lua/Urho3D.build/Release/lua_interpreter.build/Objects-normal/x86_64/lua normal x86_64
    cd /Users/att/Work/Engines/Urho3D_Engine/Urho3D_Original
    /Applications/Xcode.app/Contents/Developer/Toolchains/XcodeDefault.xctoolchain/usr/bin/clang -target x86_64-apple-macos11.5 -isysroot /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX11.3.sdk -L/Users/att/Work/Engines/Urho3D_Engine/Urho3D_Original/build/macos/bin -F/Users/att/Work/Engines/Urho3D_Engine/Urho3D_Original/build/macos/bin -filelist /Users/att/Work/Engines/Urho3D_Engine/Urho3D_Original/build/macos/Source/ThirdParty/Lua/Urho3D.build/Release/lua_interpreter.build/Objects-normal/x86_64/lua.LinkFileList -Wl,-search_paths_first -Wl,-headerpad_max_install_names /Users/att/Work/Engines/Urho3D_Engine/Urho3D_Original/build/macos/Source/ThirdParty/Lua/Release/libLua.a -lm /usr/local/Cellar/readline/8.1/lib/libreadline.dylib -Xlinker -dependency_info -Xlinker /Users/att/Work/Engines/Urho3D_Engine/Urho3D_Original/build/macos/Source/ThirdParty/Lua/Urho3D.build/Release/lua_interpreter.build/Objects-normal/x86_64/lua_dependency_info.dat -o /Users/att/Work/Engines/Urho3D_Engine/Urho3D_Original/build/macos/Source/ThirdParty/Lua/Urho3D.build/Release/lua_interpreter.build/Objects-normal/x86_64/lua

** BUILD FAILED **

build env is:
macos big sur 11.5.2
xcode 12.5.1
cmake 3.20.0

compiled with command: rake install build

-------------------------

evolgames | 2021-08-14 17:38:39 UTC | #2

Is there a prebuilt binary for Mac? Just curious

-------------------------

weitjong | 2021-08-15 03:37:52 UTC | #3

This thread could be a duplicate of another. Use the provided "cmake_xcode.sh" script as it contains a crucial instruction to tell CMake to generate the Xcode project in legacy build system mode, which unfortunately the project is stuck with for now.

https://discourse.urho3d.io/t/unable-to-compile-urho3d-library-on-big-sur/6925

-------------------------

