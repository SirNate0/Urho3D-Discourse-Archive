grant0417 | 2017-01-02 01:05:31 UTC | #1

When ever I try to use CMake to build my project and use Urho3D as an external library I get this error in my CMake log, I have tried to Google the issue but I cant fix it.

[code]
The C compiler identification is MSVC 19.0.22816.0
The CXX compiler identification is MSVC 19.0.22816.0
Check for working C compiler using: Visual Studio 14 2015
Check for working C compiler using: Visual Studio 14 2015 -- works
Detecting C compiler ABI info
Detecting C compiler ABI info - done
Check for working CXX compiler using: Visual Studio 14 2015
Check for working CXX compiler using: Visual Studio 14 2015 -- works
Detecting CXX compiler ABI info
Detecting CXX compiler ABI info - done
Detecting CXX compile features
Detecting CXX compile features - done
DirectX SDK not found. This is not fatal if a recent Windows SDK is installed
Configuring done
CMake Error: CMake can not determine linker language for target: MyExecutableName
Generating done[/code]

Here is my CMakeList.txt

[code]# Set project name
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
setup_main_executable ()[/code]

-------------------------

weitjong | 2017-01-02 01:05:31 UTC | #2

It seems that your project main CMakeLists.txt is already as expected. What is the installed CMake version in your system? Could you update it to the latest if it is below 3.0.2. And also do you actually have source files (cpp + h) in your project root?

-------------------------

grant0417 | 2017-01-02 01:05:31 UTC | #3

Oh, I forgot the cpp + h. Thank you for the help.

-------------------------

