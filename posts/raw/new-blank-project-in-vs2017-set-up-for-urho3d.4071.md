hvince95 | 2019-01-15 23:18:10 UTC | #1

Hi, I'm new to the forums and Urho3D and am posting this as I am struggling to get Urho3D working with a new project.

I have never used CMake but have managed to get the samples to build and have been through and had a quick look at them all.

I want to start a new project with so that I can get up and running with Urho3D and start developing right away! I have tried building Urho3D through CMake without the samples but when I open the Urho3D solution in visual studio I am faced with about 25 different projects, sdl and bullet etc etc..!! should these be here?

I have tried to use Urho3D as an external library, but get all sorts of errors (PATH variables have been set correctly, i believe)

I have also tried following this tutorial to the t: https://urho3d.github.io/documentation/1.7/_using_library.html
but am unsure how to get this integrated with a visual studio project/solution.

Is there a very simple template that has either all the cmake requirements done? or a template that i can download with the external library set up already?

Thankyou.

-------------------------

Modanung | 2018-03-04 11:01:16 UTC | #2

There's this wizard I made for QtCreator:
https://discourse.urho3d.io/t/wrench-class-and-project-wizards-for-qtcreator/2076

And welcome to the forums! :confetti_ball:

-------------------------

Sinoid | 2018-03-04 11:11:07 UTC | #3

> I have tried to use Urho3D as an external library, but get all sorts of errors (PATH variables have been set correctly, i believe)

Show us the error messages please.

---

I just do it the explicit way and set it all up through visual studio manually after I've built the Urho3D project externally.

-------------------------

hvince95 | 2018-03-04 11:18:21 UTC | #4

Thankyou Modanung and JSandusky.
I found this video which describes the process I have gone through exactly (but with master Urho and updated CMakeLists file):
https://www.youtube.com/watch?v=yImFcDZ61Lk
Everything goes fine until the build of the project. This is the first few lines of the output:
*     1>------ Build started: Project: MyExecutableName, Configuration: Debug x64 ------
*     1>Urho3D.lib(Allocator.obj) : error LNK2038: mismatch detected for '_ITERATOR_DEBUG_LEVEL': value '0' doesn't match value '2' in Main.obj
*     1>Urho3D.lib(Allocator.obj) : error LNK2038: mismatch detected for 'RuntimeLibrary': value 'MD_DynamicRelease' doesn't match value 'MDd_DynamicDebug' in Main.obj
*     1>Urho3D.lib(HashBase.obj) : error LNK2038: mismatch detected for '_ITERATOR_DEBUG_LEVEL': value '0' doesn't match value '2' in Main.obj
*     1>Urho3D.lib(HashBase.obj) : error LNK2038: mismatch detected for 'RuntimeLibrary': value 'MD_DynamicRelease' doesn't match value 'MDd_DynamicDebug' in Main.obj
*     1>Urho3D.lib(RefCounted.obj) : error LNK2038: mismatch detected for '_ITERATOR_DEBUG_LEVEL': value '0' doesn't match value '2' in Main.obj
*     1>Urho3D.lib(RefCounted.obj) : error LNK2038: mismatch detected for 'RuntimeLibrary': value 'MD_DynamicRelease' doesn't match value 'MDd_DynamicDebug' in Main.obj
*     1>Urho3D.lib(StringHash.obj) : error LNK2038: mismatch detected for '_ITERATOR_DEBUG_LEVEL': value '0' doesn't match value '2' in Main.obj
*     1>Urho3D.lib(StringHash.obj) : error LNK2038: mismatch detected for 'RuntimeLibrary': value 'MD_DynamicRelease' doesn't match value 'MDd_DynamicDebug' in Main.obj

- All error code LNK2038.
I feel like I'm so close!

Is this the explicit way that you go about it JSandusky?

-------------------------

Sinoid | 2018-03-04 12:00:01 UTC | #5

> Is this the explicit way that you go about it JSandusky?

Nope. I start a command line project and manually (not really, I use tools) add the Urho3D.lib, include and library directories to it. It's not ideal but I have my specific reasons for it.

---

You have an iterator mismatch. Two major causes of that are:

- Genuinely different settings between linked projects 
    - Check in `Configuration Settings -> C/C++ -> Preprocessor -> Preprocessor Definitions`
- Mismatched debug/release builds (release referencing debug, or vice-versa)
    - Looks pretty suspect based on the other errors ... no idea how you would have accomplished that, avoiding those sorts of things is one of the major boons to CMake

-------------------------

weitjong | 2018-03-04 13:58:20 UTC | #6

Have you considered to install the Ruby/Rake in your Windows host system? If you have that prerequisite also installed then you can build the Urho3D library as so, without even launching VS (of course you can also do that by opening the generated solution file).

```
cd /path/to/your/urho3d/source-tree
rake cmake vs2017 URHO3D_64BIT=1 URHO3D_LUAJIT=1 build_tree=/path/to/your/urho3d/build-tree
rake make build_tree=/path/to/your/urho3d/build-tree
```

Then to quickly scaffolding a new project.

```
rake scaffolding dir=/path/to/your/own/project/source-tree
```

Finally to build your own project.

```
cd /path/to/your/own/project/source-tree
rake cmake vs2017 URHO3D_64BIT=1 URHO3D_HOME=/path/to/your/urho3d/build-tree build_tree=/path/to/your/project/build-tree
rake make build_tree=/path/to/your/project/build-tree
```

You can leave the "build_tree" to the default, which is "../native-Build" for normal desktop native build configuration, instead of passing it explicitly. Passing URHO3D_HOME though is mandatory but only for the very first time you generate your own build tree.

Notice the similarity in building the Urho3D project and your own project. That's because the scaffolding rake task reuse the same build fixtures from Urho3D project.

HTH.

-------------------------

hvince95 | 2018-03-04 20:28:38 UTC | #7

Thanks again everyone, Im flat out for the next couple of days so I will let you know how I go when I get the chance. It does look like there was a bit of a mismatch between x86 and x64 versions along the way somewhere. I will definitely give rake a go!

-------------------------

hvince95 | 2018-03-16 21:47:51 UTC | #8

Ok, thanks all for your help, if it weren't for you all I would never have egged on to get this working. I now have a blank Visual Studio project with the mainloop example compiling and running! (did not want to deal with 64 bit anything so i just disabled all of that for 32 bit). 

For anyone else who is interested, but mainly for my own future reference :stuck_out_tongue_winking_eye:, here is the process I used:

1. download latest Urho3D from github and extract to directory (...\Urho-master)
download cmake

2. run cmake, source directory = build directory = ...\Urho-master 
navigate to that directory in command prompt and run the following command:
`cmake_vs2017.bat D:\Urho3D-master -DURHO3D_64BIT=0 -DURHO3DLUA=0 -DURHO3D_SAMPLES=0`

3. add (...\Urho-master) directory to environment variable: URHO3D_HOME (I dont know if this is actually needed, but hey)

4. open the Urho3D.sln file in visual studio and ALL_BUILD as both 'release' and 'debug'

5. Set up personal project directory as follows:
    - bin folder and subfolders are empty
    - copy and paste CMake folder from (...\Urho-master) with modules and toolchains and their contents
    - CMakeLists.txt from urho documentation (_using_library). set project name and executable name.

    <PROJECT_ROOT>/
     ├ bin/
     │  ├ Data/
     │  └ CoreData/
     ├ CMake/
     │  ├ Modules/
     │  └ Toolchains/
     ├ CMakeLists.txt
     ├ *.cpp and *.h
     └ *.bat or *.sh



6. add a .cpp file (Main.cpp) with code from 'Engine initialisation and main loop' documentation page

7. Open CMake gui. Source directory = build directory = <PROJECT_ROOT>/

8. Click configure

9. Make sure URHO3D_HOME is the correct directory (...\Urho-master), and select any functions that you want/need
Make sure Urho3D_DIR is the correct directory (...\Urho-master) (maybe, i dunno, but it works!)

10. Click generate

11. Go to <PROJECT_ROOT>/ and open projectname.sln

12. You can now build and run your project in debug/release mode!!!

-------------------------

hvince95 | 2018-03-08 10:34:11 UTC | #9

I just have a couple questions to ask:

* I get a heap of output in the following format:
`    'Project_Ares_Executable_d.exe' (Win32): Loaded 'C:\Windows\SysWOW64\user32.dll'. Cannot find or open the PDB file.`
and
'Project_Ares_Executable_d.exe' (Win32): Loaded 'C:\Windows\System32\DriverStore\FileRepository\c0318486.inf_amd64_11ba0b4b7cc81d52\aticfx32.dll'. Cannot find or open the PDB file.

  Is this a concern?

* I have my Visual Studio Solution, I have MyProject as well as 3 others, ALL_BUILD, INSTALL, and ZERO_CHECK
  * ALL_BUILD is self explanatory
  * INSTALL does this produce an installer for MyProject?
  * ZERO_CHECK i simply have no idea!

-------------------------

