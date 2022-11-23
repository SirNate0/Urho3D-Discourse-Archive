Elendil | 2017-12-12 18:21:03 UTC | #1

How can I use Urho in MSVC 2015 as static linking?
I download windows prebuild STATIC 64bit, create project with msvc and add include headers, library, and set up linker with Urho3D.lib
copy-paste first project and build. I got lot errors about missing SDL input headers.

Then I found there some tutorial for set up project in Wiki and download Urho3d-master. It looks easy but following steps are not complete (set up path for urho is missing) and there is old link to 1.6 version. 1.7 is written little differently and there different CMakeLists.txt code.
And in documentation there is written it is for external library. I don't know what it means, as DLL?
After all i try follow documentation and got this error:
> CMake Error at CMake/Modules/FindUrho3D.cmake:346 (message):
>   Could NOT find compatible Urho3D library in Urho3D SDK installation or
>   build tree.  Use URHO3D_HOME environment variable or build option to
>   specify the location of the non-default SDK installation or build tree.
>   Ensure the specified location contains the Urho3D library of the requested
>   library type.
> Call Stack (most recent call first):
>   CMake/Modules/UrhoCommon.cmake:231 (find_package)
>   CMakeLists.txt:21 (include)

I tried set up URHO3D_HOME  variable in windows, but without effect. On google I found this:
`# set(URHO3D_HOME "c:/pathTo/Urho3D-master-BUILD")`
I change it to
`set(URHO3D_HOME "d:/MyPathTo/Urho 3d/Urho3D-master-BUILD")`
but without succes.

Can I set up project only with msvc or I need it with CMake?

-------------------------

1vanK | 2017-12-12 18:40:20 UTC | #2

```
set (ENV{URHO3D_HOME} d:/MyGames/Engine/Build)
set (CMAKE_MODULE_PATH d:/MyGames/Engine/Urho3D/CMake/Modules)
```

-------------------------

1vanK | 2017-12-12 19:00:49 UTC | #3

[quote="Elendil, post:1, topic:3839"]
Can I set up project only with msvc
[/quote]

Theoretically yes. but you need set all egine options as defines manually

Project properties > c++ > Preprocessor > definitions
```
UHO3D_LOGGING;URHO3D_MINIDUMPS;URHO3D_PROFILING;URHO3D_THREADING;etc
```

-------------------------

Elendil | 2017-12-12 19:33:41 UTC | #4

[quote="1vanK, post:2, topic:3839, full:true"]
set (ENV{URHO3D_HOME} d:/MyGames/Engine/Build)
set (CMAKE_MODULE_PATH d:/MyGames/Engine/Urho3D/CMake/Modules)
[/quote]
CMAKE_MODULE_PATH was ok, if I change it, it produce another problem.

Only this helped
> set (ENV{URHO3D_HOME} "d:/PathTo/UrhoEngine-Build")
because I had empty space in path. I have engine under "Urho 3d"

Thanks.

-------------------------

Elendil | 2017-12-12 19:38:16 UTC | #5

And last question (maybe). After CMake build and open sln in msvc, I have 4 project inside. ALL, INSTALL, MyProject, ZERO_CHECK. What are other means (INSTALL, ZEROCHECK)? Why they are here?

-------------------------

Eugene | 2017-12-12 20:00:09 UTC | #6

[quote="Elendil, post:5, topic:3839"]
What are other means (INSTALL, ZEROCHECK)? Why they are here?
[/quote]

Just CMake technical stuff, don't think about it. AFAIK ZEROCHECK prevents projects from being out-of-date, and INSTALL is some useless stuff I've never used.

-------------------------

Elendil | 2017-12-12 20:12:09 UTC | #7

Thanks.

I forgot ask, when I compile MyProject with firstProject Tutorial code example, it create exe file under bin folder. That means if I finish project, everything will be under bin? Can then take all files from it and rename bin in to my project?

Can I change reasource path in project later? For example, there is bin/Data bin/CoreData and I change it to bin/Data bin/EngineData etc..

-------------------------

weitjong | 2017-12-13 01:48:09 UTC | #8

The INSTALL and all the other built-in target in the solution file are not useless. They have their own purpose or they would not be there in the first place. The INSTALL target installs the binary to your file system, as it’s name implies, for example.

Windows platform does not support RPATH like the *Nix does, so as long as you keep all the binaries and DLL if any in one place then you can move them around anywhere you like. The resource path can be adjusted in the engine parameter during compile time and/or runtime. Check our documentation on resource path.

-------------------------

