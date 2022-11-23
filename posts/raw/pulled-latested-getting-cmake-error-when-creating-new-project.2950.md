umen | 2017-03-26 02:54:45 UTC | #1

Hello 
i followed the documentetion : https://urho3d.github.io/documentation/1.4/_using_library.html
creating new project using static lib . 
but im getting CMAKE errors 
i compiled the Urho3D lib using VS 2015 succefuly using CMAKE 

the cmake command is : 
`cmake_vs2015.bat d:\dev\cpp\3d\urho3d\UrhoSampleProject\build  -DURHO3D_WIN32_CONSOLE=1 -DURHO3D_HOME=d:\dev\cpp\3d\urho3d\Urho3D\build`

and im getting : 
-- The C compiler identification is MSVC 19.0.23026.0
-- The CXX compiler identification is MSVC 19.0.23026.0
-- Check for working C compiler: C:/Program Files (x86)/Microsoft Visual Studio 14.0/VC/bin/cl.exe
-- Check for working C compiler: C:/Program Files (x86)/Microsoft Visual Studio 14.0/VC/bin/cl.exe -- works
-- Detecting C compiler ABI info
-- Detecting C compiler ABI info - done
-- Check for working CXX compiler: C:/Program Files (x86)/Microsoft Visual Studio 14.0/VC/bin/cl.exe
-- Check for working CXX compiler: C:/Program Files (x86)/Microsoft Visual Studio 14.0/VC/bin/cl.exe -- works
-- Detecting CXX compiler ABI info
-- Detecting CXX compiler ABI info - done
-- Detecting CXX compile features
-- Detecting CXX compile features - done
CMake Error at CMakeLists.txt:21 (include):
  include could not find load file:

    Urho3D-CMake-common


-- Found Urho3D: D:/dev/cpp/3d/urho3d/Urho3D/build/lib/Urho3D_d.lib (found version "1.6-720-g2e19e8a")
CMake Error at CMakeLists.txt:28 (define_source_files):
  Unknown CMake command "define_source_files".


-- Configuring incomplete, errors occurred!
See also "D:/dev/cpp/3d/urho3d/UrhoSampleProject/build/CMakeFiles/CMakeOutput.log". 


this is my files structure : 
<img src="//cdck-file-uploads-global.s3.dualstack.us-west-2.amazonaws.com/standard17/uploads/urho3d/original/1X/1ac1a2d4fb9c19eccb2b2b35053ecd749de9aaf2.png" width="363" height="392">


and this is my CmakeLists.txt 


    # Set project name
    project (MyProjectName)
    # Set minimum version
    cmake_minimum_required (VERSION 2.8.6)
    if (COMMAND cmake_policy)
        cmake_policy (SET CMP0003 NEW)
        if (CMAKE_VERSION VERSION_GREATER 2.8.12 OR CMAKE_VERSION VERSION_EQUAL 2.8.12)
            # INTERFACE_LINK_LIBRARIES defines the link interface
            cmake_policy (SET CMP0022 NEW)
        endif ()
        if (CMAKE_VERSION VERSION_GREATER 3.0.0 OR CMAKE_VERSION VERSION_EQUAL 3.0.0)
            # Disallow use of the LOCATION target property - therefore we set to OLD as we still need it
            cmake_policy (SET CMP0026 OLD)
            # MACOSX_RPATH is enabled by default
            cmake_policy (SET CMP0042 NEW)
        endif ()
    endif ()
    # Set CMake modules search path
    set (CMAKE_MODULE_PATH ${CMAKE_SOURCE_DIR}/CMake/Modules)
    # Include Urho3D Cmake common module
    include (Urho3D-CMake-common)
    # Find Urho3D library
    find_package (Urho3D REQUIRED)
    include_directories (${URHO3D_INCLUDE_DIRS})
    # Define target name
    set (TARGET_NAME MyExecutableName)
    # Define source files
    define_source_files ()
    # Setup target with resource copying
    setup_main_executable ()


what is wrong here ?
Thanks

-------------------------

TheComet | 2017-03-26 03:01:22 UTC | #2

The file `Urho3D-CMake-common.cmake` was recently renamed to `UrhoCommon.cmake`. In your CMakeLists.txt script you will have to change this:
```
# Include Urho3D Cmake common module
include (Urho3D-CMake-common)
```
to this
```
# Include Urho3D Cmake common module
include (UrhoCommon)
```

-------------------------

umen | 2017-03-25 11:48:05 UTC | #3

Thanks 
Why the documention not updated ? 
Or where can I fined up to date documentions?

-------------------------

weitjong | 2017-03-26 03:01:22 UTC | #4

Also use the doc-version switcher to choose 'HEAD' version of the online doc when you are tracking master branch development. The HEAD version is updated in tandem as the master branch moves.

-------------------------

umen | 2017-03-25 13:04:52 UTC | #5

Thanks for the replay but I'm not Git person 
And I know only how to pull sources nothing more . 
That means I don't understand all this " HEAD" jargon ......
In simple words why it is not updated in the wiki ? As this the first place developers looking for . New developers ... 
thanks

-------------------------

TheComet | 2017-03-25 13:08:47 UTC | #6

He means click here

<img src="//cdck-file-uploads-global.s3.dualstack.us-west-2.amazonaws.com/standard17/uploads/urho3d/original/1X/b89f13423d969b4d8823e41191975cbe27554517.png" width="690" height="271">

The docs were updated, but you were reading the 1.6 docs and not the HEAD docs. HEAD in git is the most recent version of a branch.

-------------------------

umen | 2017-03-25 18:25:16 UTC | #7

yeah found it very confusing , should be the default 
Thanks!

-------------------------

Modanung | 2017-03-26 02:58:30 UTC | #8

By default it s set to the latest release version. Which makes sense for people who are not building Urho3D from source.

-------------------------

