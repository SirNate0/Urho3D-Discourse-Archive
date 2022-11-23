gasp | 2017-01-02 00:58:33 UTC | #1

hello, i'm trying to build a c++ project with a library build from source .

What i have :
i've succesfuly make an out of source project ([urho3d.github.io/documentation/a00004.html](http://urho3d.github.io/documentation/a00004.html))

in my "Source" directory i've a Tools\mylib\src (with .hh & .cc for the lib)
this is the "CMakeLists.txt" from Source :
[quote]

# Set project name
project (MySuperDuperGame)
# Set minimum version
cmake_minimum_required (VERSION 2.8.6)
if (COMMAND cmake_policy)
cmake_policy (SET CMP0003 NEW)
endif ()

# Set CMake modules search path
set (CMAKE_MODULE_PATH $ENV{URHO3D_HOME}/Source/CMake/Modules CACHE PATH "Path to Urho3D-specific CMake modules")
# Include Urho3D Cmake common module
include (Urho3D-CMake-common)

# HERE IS MY ADDITION TO PARCSE THE LIBRARY FILE
add_subdirectory(Tools/mylib/src)



# Find Urho3D library
find_package (Urho3D REQUIRED)

include_directories (${URHO3D_INCLUDE_DIRS})

# Define target name
set (TARGET_NAME Main)
# Define source files
define_source_files ()
# Setup target with resource copying
setup_main_executable ()
[/quote]
and the "CMakeLists.txt" in the libdirectory :

[quote]
# Define target name
set (TARGET_NAME mylib)

# Define source files
file (GLOB C_FILES *.cc)
file (GLOB H_FILES *.hh)
set (SOURCE_FILES ${C_FILES} ${H_FILES})

# Define include directory
set (INCLUDE_DIRS_ONLY .)

# Setup target
setup_library ()
[/quote]

when i launch the "cmake_mingw.bat" cmake instruction in base directory it's ok, output :
[code]
-- The C compiler identification is GNU 4.8.1
-- The CXX compiler identification is GNU 4.8.1
-- Check for working C compiler: C:/MinGW-4.8.1/bin/gcc.exe
-- Check for working C compiler: C:/MinGW-4.8.1/bin/gcc.exe -- works
-- Detecting C compiler ABI info
-- Detecting C compiler ABI info - done
-- Check for working CXX compiler: C:/MinGW-4.8.1/bin/g++.exe
-- Check for working CXX compiler: C:/MinGW-4.8.1/bin/g++.exe -- works
-- Detecting CXX compiler ABI info
-- Detecting CXX compiler ABI info - done
-- Using SSE2 instead of SSE because SSE fails on some Windows ports of GCC
-- Disable SSE with the CMake option -DENABLE_SSE=0 if this is not desired
-- Found Urho3D: C:/Urho3D/Lib/libUrho3D.a
-- Configuring done
-- Generating done
-- Build files have been written to: C:/Urho3D/testProject/Build
[/code]

and now the "make" error  :
[code]
-- Using SSE2 instead of SSE because SSE fails on some Windows ports of GCC
-- Disable SSE with the CMake option -DENABLE_SSE=0 if this is not desired
-- Configuring done
-- Generating done
-- Build files have been written to: C:/Urho3D/testProject/Build
Scanning dependencies of target Main
[  7%] Building CXX object CMakeFiles/Main.dir/HelloWorld.cpp.obj
C:\Urho3D\testProject\Source\HelloWorld.cpp:32:21: fatal error: mylib.hh: No such file or directory
 #include "mylib.hh"
[/code]

i can add in include root "CMakeLists.txt" some include, but i want to use the same logic & tools the Urho3d build system use for his own library.

For me it didn't detect "main" depand on  "mylib".

Could you help me to solve this little case ?

-------------------------

weitjong | 2017-01-02 00:58:33 UTC | #2

This is more a CMake question than Urho3D related. You should be able to find your answer when you do searches in the CMake mailing list archives. But since you ask nicely... 

The target dependencies is not inferred by CMake by order of things in your CMakeLists.txt. You have to explicitly tell it that targetA depends on targetB by using add_dependencies() command or target_link_libraries() command; or indirectly by defining a custom command in targetA that depends on targetB using add_custom_command() command. In general, you probably only need to use one of the first two commands.

Secondly, the "include directories" has a scope. If you define it at the global scope (root CMakeLists.txt) then it will also be applicable in the sub-directory. If, however, you define it in a sub-directory (like in your case) then it would go out of scope when you leave the current CMakeLists.txt. That's why mylib.hh cannot be found in the Main directory/target because the "." is not in the include search path anymore after it leaves the Tools/mylib/src sub-directory. Note that the "." also loses its context when it is being evaluated outside of its current directory. In contrast, ${URHO3D_INCLUDE_DIRS} is being added at the global scope, so it is valid everywhere in the project.

HTH.

-------------------------

gasp | 2017-01-02 00:58:35 UTC | #3

thanks you for you'r reply, i was missing the local / global scope of the dir, this is the end of my root file (for reference) :

[quote]
# Define source files
define_source_files ()
# Setup target with resource copying
setup_main_executable ()
#myLib Part
add_subdirectory(Tools/mylib/src)
include_directories(Tools/mylib/src)
target_link_libraries(Main mylib)
[/quote]

now it work like a  charm (the CMakeLists.txt in the lib can compile himself).

Sorry for the question, i wanted to be sure to not interfec, you'r cmake is a little too complex for now for me, i wanted not to make mistake.

Thanks you again !

-------------------------

