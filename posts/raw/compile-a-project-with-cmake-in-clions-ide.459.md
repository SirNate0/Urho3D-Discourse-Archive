shu | 2017-01-02 01:00:35 UTC | #1

Hi  

there's a new IDE called Clions by JetBrains in an 'Early Access'-program and I want to work with it. It already has great refactoring support and after coding in Java/Scala for a long time that is something I miss a lot in VisualStudio Express.

At the moment Clions uses cmake to create a project, there is no other way yet. You have to create a CMakeLists.txt with all necessary info in it. 

I set up a very simple test and it does compile, but when linking starts I get loads of 'undefined references' to Urho3D. 

I tried this first with a Urho3D-build from Visual Studio and thought this might have to do with Clion using mingW64-g++ (btw: is that idea correct?). So I build Urho3D with mingW64, but nothing changed. (and also I got a libUrho3D.a which won't work on Windows, right?)

It's totally possible that I make a stupid mistake somewhere or it could be a problem with the IDE. Do you have an idea? Does this look like it [i]should[/i] work? :slight_smile:

Do I have to build Urho3D.lib with mingW64? 

This is the CMakeLists.txt I use: 
[code]
cmake_minimum_required(VERSION 2.8.4)
project(test)

set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -std=c++11")


include_directories(D:/dev/hvfn/cpp/Urho3D-1.31/Source/Engine
					D:/dev/hvfn/cpp/Urho3D-1.31/Source/Engine/Core
					D:/dev/hvfn/cpp/Urho3D-1.31/Source/Engine/Audio
					D:/dev/hvfn/cpp/Urho3D-1.31/Source/Engine/Container
					D:/dev/hvfn/cpp/Urho3D-1.31/Source/Engine/Engine
					D:/dev/hvfn/cpp/Urho3D-1.31/Source/Engine/Graphics
					D:/dev/hvfn/cpp/Urho3D-1.31/Source/Engine/Input
					D:/dev/hvfn/cpp/Urho3D-1.31/Source/Engine/IO
					D:/dev/hvfn/cpp/Urho3D-1.31/Source/Engine/LuaScript
					D:/dev/hvfn/cpp/Urho3D-1.31/Source/Engine/Math
					D:/dev/hvfn/cpp/Urho3D-1.31/Source/Engine/Navigation
					D:/dev/hvfn/cpp/Urho3D-1.31/Source/Engine/Network
					D:/dev/hvfn/cpp/Urho3D-1.31/Source/Engine/Physics
					D:/dev/hvfn/cpp/Urho3D-1.31/Source/Engine/Resource
					D:/dev/hvfn/cpp/Urho3D-1.31/Source/Engine/Scene
					D:/dev/hvfn/cpp/Urho3D-1.31/Source/Engine/Script
					D:/dev/hvfn/cpp/Urho3D-1.31/Source/Engine/UI
					D:/dev/hvfn/cpp/Urho3D-1.31/Source/Engine/Urho2D
					d:/dev/hvfn/cpp/Urho3D-1.31/Source/ThirdParty/Bullet/src
					d:/dev/hvfn/cpp/Urho3D-1.31/Source/ThirdParty/kNet/include
					d:/dev/hvfn/cpp/Urho3D-1.31/Source/ThirdParty/SDL/include
					d:/dev/hvfn/cpp/Urho3D-1.31/Source/ThirdParty/AngelScript/include
					d:/dev/hvfn/cpp/Urho3D-1.31/Build/Engine
					"d:/dev/bin/Microsoft DirectX SDK (June 2010)/Include" )



link_directories( "d:/dev/bin/Microsoft DirectX SDK (June 2010)/Lib/x64"
                  "C:/Program Files (x86)/Microsoft SDKs/Windows/v7.1A/Lib"
                                     )


set(SOURCE_FILES Test.cpp Test.h)
add_executable(test ${SOURCE_FILES})

target_link_libraries (test
    D:/dev/hvfn/cpp/Urho3D-1.31/Lib/Urho3D_d.lib
    d3d9.lib
    d3dcompiler.lib
    kernel32.lib
    user32.lib
    gdi32.lib
    winspool.lib
    shell32.lib
    ole32.lib
    oleaut32.lib
    uuid.lib
    comdlg32.lib
    advapi32.lib
    winmm.lib
    imm32.lib
    version.lib
    ws2_32.lib
    dbghelp.lib )

[/code]


and the output when building: 
[code]
D:\dev\bin\clion-138.2344.15\bin\cmake\bin\cmake.exe --build C:\Users\shu\.clion10\system\cmake\generated\6e94f7d7\6e94f7d7\Debug --target test -- -j 4
[35m[1mScanning dependencies of target test
[0m[100%] [32mBuilding CXX object CMakeFiles/test.dir/Test.cpp.obj
[0m[31m[1mLinking CXX executable test.exe
[0mCMakeFiles\test.dir/objects.a(Test.cpp.obj): In function `Z14RunApplicationv':
D:/dev/hvfn/cpp/untitled/Test.h:22: undefined reference to `_imp___ZN6Urho3D7ContextC1Ev'
D:/dev/hvfn/cpp/untitled/Test.h:22: undefined reference to `_imp___ZN6Urho3D11Application3RunEv'
CMakeFiles\test.dir/objects.a(Test.cpp.obj): In function `main':
D:/dev/hvfn/cpp/untitled/Test.h:22: undefined reference to `_imp___ZN6Urho3D14ParseArgumentsEiPPc'
CMakeFiles\test.dir/objects.a(Test.cpp.obj): In function `ZN4TestC2EPN6Urho3D7ContextE':
D:/dev/hvfn/cpp/untitled/Test.cpp:4: undefined reference to `_imp___ZN6Urho3D11ApplicationC2EPNS_7ContextE'
CMakeFiles\test.dir/objects.a(Test.cpp.obj): In function `ZN4Test5StartEv':
D:/dev/hvfn/cpp/untitled/Test.cpp:17: undefined reference to `_imp___ZN6Urho3D6Object16SubscribeToEventENS_10StringHashEPNS_12EventHandlerE'
CMakeFiles\test.dir/objects.a(Test.cpp.obj): In function `ZN4Test13HandleKeyDownEN6Urho3D10StringHashERNS0_7HashMapINS0_15ShortStringHashENS0_7VariantEEE':
D:/dev/hvfn/cpp/untitled/Test.cpp:31: undefined reference to `_imp___ZN6Urho3D6Engine4ExitEv'
CMakeFiles\test.dir/objects.a(Test.cpp.obj): In function `_static_initialization_and_destruction_0':
D:/dev/hvfn/cpp/Urho3D-1.31-gcc/Source/Engine/Input/InputEvents.h:35: undefined reference to `_imp___ZN6Urho3D10StringHashC1EPKc'
D:/dev/hvfn/cpp/Urho3D-1.31-gcc/Source/Engine/Input/InputEvents.h:37: undefined reference to `_imp___ZN6Urho3D15ShortStringHashC1EPKc'
D:/dev/hvfn/cpp/Urho3D-1.31-gcc/Source/Engine/Input/InputEvents.h:38: undefined reference to `_imp___ZN6Urho3D15ShortStringHashC1EPKc'

[and so on...]
[/code]

-------------------------

gwald | 2017-01-02 01:00:35 UTC | #2

[quote="shu"]Do I have to build Urho3D.lib with mingW64? [/quote]
I would start from the begining and building all of Urho3D with that IDE.
Edit: Interesting features on the IDE [jetbrains.com/clion/quickstart/](http://www.jetbrains.com/clion/quickstart/)

[quote]
CLion supports GCC and Clang compilers. 
This means that on Windows you can select between MinGW (or MinGW-W64) and Cygwin tool sets.
[/quote]

-------------------------

shu | 2017-01-02 01:00:36 UTC | #3

[quote="gwald"]
I would start from the begining and building all of Urho3D with that IDE.
[/quote]

I have only the vaguest idea howto build Urho3D inside Clion... I would have to write a CMakeLists.txt for all of Urho3D. I can't see me manage that. :slight_smile:

But I have another question: I build Urho3D with the cmake_mingw.bat on my Windows 7. Then I start 'mingw32-make -j4' in the Build-Directory. That works, but at the end it links a 'libUrho3D.a' - File. But I think I need 'Urho3D.lib' and the debug version 'Urho3D_d.lib' to get everything to work on windows. Right?

Is there a switch to change the build to a windows '.lib' somehow? 

I use Mingw64 (i686-4.9.1-posix-dwarf-rt_v3-rev1) to compile and link.

-------------------------

gwald | 2017-01-02 01:00:36 UTC | #4

[quote="shu"]

But I have another question: I build Urho3D with the cmake_mingw.bat on my Windows 7. Then I start 'mingw32-make -j4' in the Build-Directory. That works, but at the end it links a 'libUrho3D.a' - File. But I think I need 'Urho3D.lib' and the debug version 'Urho3D_d.lib' to get everything to work on windows. Right?

Is there a switch to change the build to a windows '.lib' somehow? 

I use Mingw64 (i686-4.9.1-posix-dwarf-rt_v3-rev1) to compile and link.[/quote]

to get the debug lib you'll need 
cmake_clean.bat 
cmake_mingw.bat -DCMAKE_BUILD_TYPE=1 

If mingw is creating a .a library then change your cmake file:
  D:/dev/hvfn/cpp/Urho3D-1.31/Lib/Urho3D_d.lib
to 
  D:/dev/hvfn/cpp/Urho3D-1.31/Lib/Urho3D.a


[quote="shu"]
I have only the vaguest idea howto build Urho3D inside Clion...[/quote]

Maybe try checking out the github source via the IDE.. '[b]might[/b]' auto create a cmake file 
[jetbrains.com/clion/quickstart/](http://www.jetbrains.com/clion/quickstart/) Step 1. Open/Create a project in CLion

Sorry, i'm not a cmake expert, having cmake issues with qtCreator myself  :laughing:


Edit: looks like they just added Mingw64 in last few days, you might need to update to that version

-------------------------

shu | 2017-01-02 01:00:36 UTC | #5

Thanks gwald!

Yes, I use the newest Clion-Version with mingw64 support. 

Your other suggestions sadly didn't work. Clion doesn't know how to build Urho, checking it out from github or importing the sources can't work. And using the libUrho3D.a in Clion doesn't work either, it leads to the same undefined references as described in my first post. 

I also tried to generate a Code-Blocks-project with MingW-make-files and build it inside Code::Blocks to get a windows '.lib', but that builds an '.a'-Lib too.

Hm. I think I'll try to find out more about make and building on windows.

EDIT: Ah, you were right! I can build Urho3D inside Clion, by using the CMakeLists.txt in the /Source-Folder and use that to import it as project! Then I can build the Urho library inside Clion... but it still is in Linux-format (libUrho3D.a). :smiley: Damn.

-------------------------

existentia | 2017-01-02 01:00:36 UTC | #6

MinGW and Cygwin use ".a" for link libraries, even on Windows. 

".lib" is MSVC's format.

There are allegedly tools to convert the two formats, but I haven't tried it yet.

-------------------------

shu | 2017-01-02 01:00:36 UTC | #7

Hi existentia, thanks for the info! 
So that's not the problem. Perhaps I'll have to wait until Clion is a bit more convenient in that regard.

-------------------------

shu | 2017-01-02 01:00:37 UTC | #8

It works! Oh man, I'm so blind...

Basically the section [url=http://urho3d.github.io/documentation/HEAD/_using_library.html]"From Urho3D project root tree[/url]" is working perfectly, when Urho3D was also build in Clion... :smiley: 
I used the CMakeLists.txt from there, set the environment variable URHO3D_HOME and could compile the project. 

Well, at least I learned a bit about cmake, make, mingw and the build process today! :slight_smile:

-------------------------

yzkuris | 2018-04-25 17:44:15 UTC | #9

Hello, how do you exactly set the environment variable URHO3D_HOME

-------------------------

jmiller | 2018-04-26 02:57:26 UTC | #10

[quote="yzkuris, post:9, topic:459, full:true"]
Hello, how do you exactly set the environment variable URHO3D_HOME
[/quote]

Hi,

Among [url="https://duckduckgo.com/?q=set+environment+variable"]many ways to set an environment variable[/url], in CLion you can do this at `Settings > Build > CMake > Environment`

-------------------------

weitjong | 2018-04-26 05:17:38 UTC | #11

In Clion you can also use the IDE setting to configure the build option for CMake. Use “-DURHO3D_HOME=/path/to/urho/build/tree”.

-------------------------

yzkuris | 2018-04-27 16:08:33 UTC | #12

![Screenshot%20from%202018-04-27%2012-07-38|690x270](upload://mScgpJjlpP7G7O3VW1hOsqX2xjm.png)

Is this how I set the environment variable?

-------------------------

jmiller | 2018-04-29 02:52:58 UTC | #13

[quote="yzkuris, post:12, topic:459"]
Is this how I set the environment variable?
[/quote]

That is the one method I was describing. In most cases it's unnecessary and one can use the cmake option as @weitjong described.

Note that `URHO3D_HOME` is a build tree path (not where urho3d source is) and contents of that directory may be overwritten by cmake. I would expect a path more like /home/yzkuris/urho3d/build-debug, where urho3d is the source tree and build-debug is an 'in-source' build tree.

-------------------------

