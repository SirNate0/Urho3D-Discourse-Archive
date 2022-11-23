lexx | 2017-01-02 01:00:55 UTC | #1

I changed to VS2010 and deleted old solution and project files, created cmake file as explained here [urho3d.github.io/documentation/H ... brary.html](http://urho3d.github.io/documentation/HEAD/_using_library.html) 
then wrote    [b]cmake .[/b]    and got new project file which I added to urho3d solution. 
It didnt compile, I had to add   [b]C:\CPP\Urho3D\Engine[/b]     to   '[b]Additional Include Directories[/b]', 
otherwise it complains about missing   [b]Urho3D.h[/b] .  Then my project compiled again. 
Just for info.

-------------------------

cadaver | 2017-01-02 01:00:55 UTC | #2

When we're talking of solutions & projects created by CMake, transporting projects between solutions may not work well.

Rather, use Urho's solution only for building Urho, and your own project's solution for building your own project. Using CMake, you should treat solution/project files as essentially disposable while the authoritative project setup is all contained in your CMakeLists.txt.

-------------------------

lexx | 2017-01-02 01:00:55 UTC | #3

(I just used urho's solution because of the samples so they are 'near')

Ok, I removed all again and created new project and solution, then opened my project's solution, it still complains about Urho3D.h

[quote]
1>------ Build started: Project: ZERO_CHECK, Configuration: Debug Win32 ------
2>------ Build started: Project: Test, Configuration: Debug Win32 ------
2>  DrawIt.cpp
2>c:\cpp\urho3d\source\engine\math\Random.h(25): fatal error C1083: Cannot open include file: 'Urho3D.h': No such file or directory
2>  Main.cpp
2>c:\cpp\urho3d\source\engine\container\RefCounted.h(25): fatal error C1083: Cannot open include file: 'Urho3D.h': No such file or directory
2>  Sample.cpp
2>c:\cpp\urho3d\source\engine\container\RefCounted.h(25): fatal error C1083: Cannot open include file: 'Urho3D.h': No such file or directory
2>  Test3D.cpp
2>c:\cpp\urho3d\source\engine\math\Random.h(25): fatal error C1083: Cannot open include file: 'Urho3D.h': No such file or directory
2>  Generating Code...
========== Build: 1 succeeded, 1 failed, 0 up-to-date, 0 skipped ==========
[/quote]

-------------------------

cadaver | 2017-01-02 01:00:56 UTC | #4

Normally the Urho3D.h file should reside in URHO_HOME/Build/Engine after Urho3D has been built successfully. The CMake module FindUrho3D adds this directory as an include directory to the project. Do you have the file in that location? If you've configured Urho's CMake build differently (eg. not using the provided batch files, which use "Build" as the build output directory) then this assumption may not be true.

-------------------------

lexx | 2017-01-02 01:00:56 UTC | #5

Aha, that explains it. 
I used cmake-gui and Urho3D.sln and project files was in Urho3D/  dir. I now configured cmake-gui to use Build/ dir and now everything works, 
thanks.

-------------------------

weitjong | 2017-01-02 01:00:56 UTC | #6

When you use cmake-gui then you are advised to follow the instructions given in this section [urho3d.github.io/documentation/H ... _CMake_GUI](http://urho3d.github.io/documentation/HEAD/_building.html#Using_CMake_GUI). Or otherwise CMake would mistakenly generate a non out-of-source build tree, which is not supported by our build script anymore.

-------------------------

lexx | 2017-01-02 01:00:57 UTC | #7

Totally missed that, should read docs more carefully.

-------------------------

