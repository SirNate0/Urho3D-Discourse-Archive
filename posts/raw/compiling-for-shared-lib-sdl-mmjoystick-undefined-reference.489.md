kestli | 2017-01-02 01:00:50 UTC | #1

Hello my friends
I have a small problem of reference when I compile Urho3D with SHARED option.
When I compile for STATIC lib, I do not have any problem. 
Thanks for any answer...

[quote]
C:\mingw64\bin\x86_64-w64-mingw32-g++.exe     -static -shared -o E:\Downloads\Urho3D-1.31\Bin\Urho3D.dll -Wl,--out-implib,E:\Downloads\Urho3D-1.31\Lib\libUrho3D.dll.a -Wl,--major-image-version,0,--minor-image-version,0 -Wl,--whole-archive CMakeFiles\Urho3D.dir/objects.a -Wl,--no-whole-archive -luser32 -lgdi32 -lwinmm -limm32 -lole32 -loleaut32 -lversion -luuid -lws2_32 -lwinmm -lopengl32 -Wl,--whole-archive ..\ThirdParty\Bullet\\libBullet.a ..\ThirdParty\Civetweb\\libCivetweb.a ..\ThirdParty\Detour\\libDetour.a ..\ThirdParty\FreeType\\libFreeType.a ..\ThirdParty\JO\\libJO.a ..\ThirdParty\kNet\\libkNet.a ..\ThirdParty\LZ4\\libLZ4.a ..\ThirdParty\PugiXml\\libPugiXml.a ..\ThirdParty\Recast\\libRecast.a ..\ThirdParty\SDL\\libSDL.a ..\ThirdParty\StanHull\\libStanHull.a ..\ThirdParty\STB\\libSTB.a ..\ThirdParty\AngelScript\\libAngelScript.a ..\ThirdParty\GLEW\\libGLEW.a ..\ThirdParty\LibCpuId\\libLibCpuId.a -Wl,--no-whole-archive -limm32 -lole32 -loleaut32 -lversion -luuid -lws2_32 -lopengl32 ..\ThirdParty\Bullet\\libBullet.a ..\ThirdParty\Civetweb\\libCivetweb.a ..\ThirdParty\Detour\\libDetour.a ..\ThirdParty\FreeType\\libFreeType.a ..\ThirdParty\JO\\libJO.a ..\ThirdParty\kNet\\libkNet.a ..\ThirdParty\LZ4\\libLZ4.a ..\ThirdParty\PugiXml\\libPugiXml.a ..\ThirdParty\Recast\\libRecast.a ..\ThirdParty\SDL\\libSDL.a ..\ThirdParty\StanHull\\libStanHull.a ..\ThirdParty\STB\\libSTB.a ..\ThirdParty\AngelScript\\libAngelScript.a ..\ThirdParty\GLEW\\libGLEW.a ..\ThirdParty\LibCpuId\\libLibCpuId.a -lkernel32 -luser32 -lgdi32 -lwinspool -lshell32 -lole32 -loleaut32 -luuid -lcomdlg32 -ladvapi32 
..\ThirdParty\SDL\\libSDL.a(SDL_mmjoystick.c.obj):SDL_mmjoystick.c:(.text+0x4a): undefined reference to `__imp_joyGetNumDevs'
..\ThirdParty\SDL\\libSDL.a(SDL_mmjoystick.c.obj):SDL_mmjoystick.c:(.text+0x7b): undefined reference to `__imp_joyGetPosEx'
..\ThirdParty\SDL\\libSDL.a(SDL_mmjoystick.c.obj):SDL_mmjoystick.c:(.text+0xe1): undefined reference to `__imp_joyGetDevCapsA'
..\ThirdParty\SDL\\libSDL.a(SDL_mmjoystick.c.obj):SDL_mmjoystick.c:(.text+0x655): undefined reference to `__imp_joyGetPosEx'
c:/mingw64/bin/../lib/gcc/x86_64-w64-mingw32/4.7.3/../../../../x86_64-w64-mingw32/bin/ld.exe: ..\ThirdParty\SDL\\libSDL.a(SDL_mmjoystick.c.obj): bad reloc address 0x0 in section `.pdata'
collect2.exe: error: ld returned 1 exit status
Engine\CMakeFiles\Urho3D.dir\build.make:4842: recipe for target `E:/Downloads/Urho3D-1.31/Bin/Urho3D.dll' failed
mingw32-make[2]: *** [E:/Downloads/Urho3D-1.31/Bin/Urho3D.dll] Error 1
mingw32-make[2]: Leaving directory `E:/Downloads/Urho3D-1.31/Build'
CMakeFiles\Makefile2:885: recipe for target `Engine/CMakeFiles/Urho3D.dir/all' failed
mingw32-make[1]: *** [Engine/CMakeFiles/Urho3D.dir/all] Error 2
mingw32-make[1]: Leaving directory `E:/Downloads/Urho3D-1.31/Build'
makefile:136: recipe for target `all' failed
mingw32-make: *** [all] Error 2
[/quote]

-------------------------

weitjong | 2017-01-02 01:00:50 UTC | #2

I am not able to reproduce your problem with the SHARED lib type MinGW build on my Win7 (virtual) host system. How did you generate the MinGW makefile? Did you use our CMake build script?

-------------------------

kestli | 2017-01-02 01:00:51 UTC | #3

Hallo  weitjong, thanks for your time. 
I have used Cmake-GUI to generate the project for Eclipse but sight your answer-question have compiled with the script and executed mingw32-make from the commands line and this time has not given to me herror any.
Sometimes one chooses the most difficult and less suitable way to do the things.

-------------------------

