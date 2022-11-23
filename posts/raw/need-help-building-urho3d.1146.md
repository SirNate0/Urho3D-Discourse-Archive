krstefan42 | 2017-01-02 01:05:42 UTC | #1

Hi, I'm trying to build Urho3D for 64-bit Windows 8.1, but I'm running into some trouble.

I have mingw-w64 installed. I donwloaded the source right off the main page. Then I downloaded cmake. I ran the CMake GIU and put "Urho3D-1.4/Source" for the source directory, and "Urho3D-1.4/Build" as the build directory (after making the Build folder). Then I go to configure, and set "MinGW Makefiles" as the project Generator.

Everything seems to go fine, it gets to "looking for include file stdint.h - found". Then It gives this error: [i]CMake Error at ThirdParty/FreeType/CMakeLists.txt:80 (setup_library):
  Unknown CMake command "setup_library".[/i]

In the window above, everything looks fine, except that the CMAKE_SH field says "CMAKE_SH-NOTFOUND". I replaced it with the directory for make, and I still get the error.

I don't know what else I can do. Compilers, Building, Installing Libraries, etc. has always been a bit of a nightmare for me. Thanks for any help!

-------------------------

weitjong | 2017-01-02 01:05:42 UTC | #2

Welcome to our forum.

I think you only made one mistake. In release 1.4, when using CMake GUI you should put "Urho3D-1.4" or what have you as the source directory but you can specify anywhere you like for the build directory. Preferably, put the build directory outside of the "Urho3D-1.4".

In the release prior to 1.4, we used to have the main CMakeLists.txt located in the "Source" subdirectory. Now in 1.4 the main CMakeLists.txt is located in the root of the project. In the release prior to 1.4 user was not able to specify the build tree path freely as it is now in 1.4. So, if you are reading an old online guide from sources outside of our project, please tell the author of the guide to update it. If the guide you are using is one maintained by us in our project then please file a bug report in our issue tracker.

-------------------------

krstefan42 | 2017-01-02 01:05:43 UTC | #3

Thanks! I got it to build. I couldn't build it with LuaJIT, though, there was an error that I think was some kind of 32/64-bit incompatibility issue.

-------------------------

weitjong | 2017-01-02 01:05:43 UTC | #4

We have not received any issue report on build with LuaJIT enabled due to 32/64-bit incompatibility issue before. Unfortunately we can only test CI build with only Lua enabled (not LuaJIT) on our CI server because the MinGW compiler version available in the CI server is too old. Personally I have no problem with 64-bit MinGW build with LuaJIT enabled on my Linux host system. If you can post more information on the problem you encountered here then probably one of us could help you.

-------------------------

krstefan42 | 2017-01-02 01:05:49 UTC | #5

I think the problem was that I forgot to check the URHO3D_64BIT option. Doh. But now I get a new error when compiling. It says that "LuaJIT requires a c compiler with native exceptions", or something to that effect. I tried adding -fexceptions to the CMAKE_C_FLAGS field, but it doesn't help. 

Looking into it, apparently there are 3 methods for exception handling with MinGW-w64: SJLJ, DWARF and SEH([url]https://wiki.qt.io/MinGW-64-bit[/url]). Do I need to use a particular one of these?

-------------------------

krstefan42 | 2017-01-02 01:05:49 UTC | #6

One other problem I've been having is that when I generate the makefiles with CMake, I get the error: "Building SDL without DX joystick support due to missing wbemcli.h". Well, I found wbemcli.h online and put it in my MinGW include folders, and it still gives the error. I thought it was just CMake being quirky, So I went into the SDL CMakeLists.txt file and removed the check for wbemcli.h. Now it compiles fine. But I have no idea whether it actually found the wbemcli.h file... the compiler would give an error if it didn't find it, right?

-------------------------

weitjong | 2017-01-02 01:05:49 UTC | #7

[quote="krstefan42"]I think the problem was that I forgot to check the URHO3D_64BIT option. Doh. But now I get a new error when compiling. It says that "LuaJIT requires a c compiler with native exceptions", or something to that effect. I tried adding -fexceptions to the CMAKE_C_FLAGS field, but it doesn't help. 

Looking into it, apparently there are 3 methods for exception handling with MinGW-w64: SJLJ, DWARF and SEH([url]https://wiki.qt.io/MinGW-64-bit[/url]). Do I need to use a particular one of these?[/quote]
We don't have this issue with MinGW-W64 cross-compiler toolchain on Linux hosted build server. I also do not have this issue with MinGW-W64 compiler on my Win7 VM personally. I believe I use the default option when I installed it last time. I have something like this in my installation path: x86_64-4.9.1-posix-seh-rt_v3-rev0. I think it means I use SEH.

About the DirectX headers for SDL, I think SDL team has explained that in one of their README file ([libsdl.org/extras/win32/mingw32/README.txt](http://www.libsdl.org/extras/win32/mingw32/README.txt)). HTH.

-------------------------

