shu | 2017-01-02 01:00:29 UTC | #1

Hi all,

warning: last time I used C++ was 1998. Yesterday was the first time I used cmake. :slight_smile:

I managed to build Urho3D for 64bit Desktop like described here: urho3d.github.io/documentation/HEAD/_building.html ( I'm not allowed to post URLs)

Now I want to create an empty solution/project for Visual Studio. Could somebody describe how to do this? I tried to generate a project with this description (urho3d.github.io/documentation/HEAD/_using_library.html), but ended with an error.

What I did:
I created the folders for my project as described, I created the CMakeLists.txt-file in the source-folder and replaced the names for project and executable (both 'Sector' as name). I defined URHO3D_HOME with the correct path.

But when I run cmake -G "Visual Studio 12 2013" this happens:

[code]CMake Error at d:/dev/hvfn/cpp/Urho3D-1.31/Source/CMake/Modules/Urho3D-CMake-common.cmake:451 (add_executable):
  add_executable called with incorrect number of arguments, no sources provided
Call Stack (most recent call first):
  d:/dev/hvfn/cpp/Urho3D-1.31/Source/CMake/Modules/Urho3D-CMake-common.cmake:544
 (setup_executable)
  CMakeLists.txt:28 (setup_main_executable)

CMake Error at d:/dev/hvfn/cpp/Urho3D-1.31/Source/CMake/Modules/Urho3D-CMake-common.cmake:546 (set_target_properties):
  set_target_properties Can not find target to add properties to: Sector
Call Stack (most recent call first):
  CMakeLists.txt:28 (setup_main_executable)

-- Configuring incomplete, errors occurred!
See also "D:/dev/hvfn/cpp/Sector/Source/CMakeFiles/CMakeOutput.log".[/code]

The CMakeLists.txt looks like this

[code]
# Set project name
project (Sector)
# Set minimum version
cmake_minimum_required (VERSION 2.8.6)
if (COMMAND cmake_policy)
cmake_policy (SET CMP0003 NEW)
if (CMAKE_VERSION VERSION_GREATER 2.8.12 OR CMAKE_VERSION VERSION_EQUAL 2.8.12)
cmake_policy (SET CMP0022 NEW) # INTERFACE_LINK_LIBRARIES defines the link interface
endif ()
if (CMAKE_VERSION VERSION_GREATER 3.0.0 OR CMAKE_VERSION VERSION_EQUAL 3.0.0)
cmake_policy (SET CMP0026 OLD) # Disallow use of the LOCATION target property - therefore we set to OLD as we still need it
cmake_policy (SET CMP0042 NEW) # MACOSX_RPATH is enabled by default
endif ()
endif ()
# Set CMake modules search path
set (CMAKE_MODULE_PATH $ENV{URHO3D_HOME}/Source/CMake/Modules CACHE PATH "Path to Urho3D-specific CMake modules")
# Include Urho3D Cmake common module
include (Urho3D-CMake-common)
# Find Urho3D library
find_package (Urho3D REQUIRED)
include_directories (${URHO3D_INCLUDE_DIRS})
# Define target name
set (TARGET_NAME Sector)
# Define source files
define_source_files ()
# Setup target with resource copying
setup_main_executable ()
[/code]

What's wrong? I'm somewhat confused... is there an easier way than this?

-------------------------

friesencr | 2017-01-02 01:00:29 UTC | #2

I can't tell you why you why it doesn't work but if you want to get going fast and don't care why then:

- Go download the sdk: [microsoft.com/en-us/download ... px?id=6812](http://www.microsoft.com/en-us/download/details.aspx?id=6812)
- and run cmake_vs2013.bat in the root folder.

-------------------------

thebluefish | 2017-01-02 01:00:30 UTC | #3

I don't see a reason to use CMake for your own personal project if your goal is to get a Visual Studio 2013 project out of it.

What I did is I created a blank C++ project in Visual Studio. I then added the proper include directories, preprocessor definitions, and linker dependencies.

-------------------------

shu | 2017-01-02 01:00:30 UTC | #4

friesencr, thanks, but I already did that. That was the part that worked. :slight_smile:

thebluefish: I tried that before, but I got errors. Could you describe in short what to do?

-------------------------

rasteron | 2017-01-02 01:00:30 UTC | #5

You can also try the CMake GUI (included in your CMake installation) if you're not very much familiar or new with CMake. You can then add missing entries so you can figure out your build issues.

BTW, in your CMakeLists above, you forgot to replace this

set (CMAKE_MODULE_PATH $ENV{URHO3D_HOME}/Source/CMake/Modules CACHE PATH "[b][u]Path to Urho3D-specific CMake modules[/u][/b]")

pointing to your cache path, and don't forgot to add some actual source files in your project root directory, hence the [b]"no sources provided"[/b] error you got there :wink: 

Here's a recent build snapshot I tested earlier. I just copied the Hello example 1 sources/headers to my project root directory as an example. I'm using VC11 (2012)..

[img]http://i.imgur.com/Gtn3oSel.png[/img]

CMakeLists.txt here:

[code]
# Set project name
project (Sample)
# Set minimum version
cmake_minimum_required (VERSION 2.8.6)
if (COMMAND cmake_policy)
    cmake_policy (SET CMP0003 NEW)
    if (CMAKE_VERSION VERSION_GREATER 2.8.12 OR CMAKE_VERSION VERSION_EQUAL 2.8.12)
        cmake_policy (SET CMP0022 NEW) # INTERFACE_LINK_LIBRARIES defines the link interface
    endif ()
    if (CMAKE_VERSION VERSION_GREATER 3.0.0 OR CMAKE_VERSION VERSION_EQUAL 3.0.0)
        cmake_policy (SET CMP0026 OLD) # Disallow use of the LOCATION target property - therefore we set to OLD as we still need it
        cmake_policy (SET CMP0042 NEW) # MACOSX_RPATH is enabled by default
    endif ()
endif ()
# Set CMake modules search path
set (CMAKE_MODULE_PATH $ENV{URHO3D_HOME}/Source/CMake/Modules CACHE PATH "C:/Urho3D-master/Source")
# Include Urho3D Cmake common module
include (Urho3D-CMake-common)
# Find Urho3D library
find_package (Urho3D REQUIRED)
include_directories (${URHO3D_INCLUDE_DIRS})
# Define target name
set (TARGET_NAME MyProject)
# Define source files
define_source_files ()
# Setup target with resource copying
setup_main_executable ()
[/code]


Hope that helps  :slight_smile:

-------------------------

shu | 2017-01-02 01:00:30 UTC | #6

Yay! It works! 

I added some source-Files  :blush:  :smiley: , edited the CACHE PATH in the CMakeLists.txt, used cmake-gui and added URHO3D_64BIT and now I got a working solution-File! 

Thanks a lot, rasteron! That really helped! :slight_smile:

-------------------------

weitjong | 2017-01-02 01:00:30 UTC | #7

First of all, welcome to our forum. Glad to hear you have figured out how the build system works.

I just want to comment that there is no need to alter the "documentation string" that follows the "CACHE PATH" option of the set() command. Leave the documentation string as it is.

-------------------------

shu | 2017-01-02 01:00:30 UTC | #8

Oh, ok, so that is for documentation. 
Thanks for the correction!

-------------------------

rasteron | 2017-01-02 01:00:30 UTC | #9

Sure thing shu, I'm glad it worked for you now.  :sunglasses: 

[b]@weitjong[/b]

Oh yes I forgot that was the tool tip and did not notice after I set the URHO3D_HOME and restart  :unamused:

-------------------------

