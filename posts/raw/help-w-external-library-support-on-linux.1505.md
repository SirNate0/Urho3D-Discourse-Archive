coffee | 2017-01-02 01:08:10 UTC | #1

Building Urho3D has been pretty easy. No problems there. But I'm embarrassed to admit how long I've been working to get the cmake system to work properly with Urho3D as an external library, on Linux.

What I've done:
Cloned the repo
created Urho3D/build
configured cmake via cmake-gui to use build.
Made Urho3D into build as a static library.

At this point all the demos in build/bin work without issue. Cool beans! Next I create an external project directory. I reference [http]://urho3d.github.io/documentation/1.5/_using_library.html. I specifically note this part of the page.

[quote]You must adjust the URHO3D_HOME environment variable in your build. In release 1.4 onward, the URHO3D_HOME environment variable is supposed to [b]point to the build tree of the Urho3D project.[/b] In prior releases, the URHO3D_HOME was supposed to point to Urho3D project root itself.[/quote]

So I, "export URHO3D_HOME=/home/blah/project/Urho3D/build". Side note, setting this or changing its value doesn't seem to have any impact.
I create my CMakeLists.txt per the instructions.
No mention of a build directory is made on the page, but I go ahead and create one. I've also tried without. No change.
So, via cmake-gui, the source directory is set as the root of my project and the build directory is set as the build directory.
Tell it to configure. Get errors:
[quote]
The C compiler identification is GNU 4.8.4
The CXX compiler identification is GNU 4.8.4
Check for working C compiler: /usr/bin/cc
Check for working C compiler: /usr/bin/cc -- works
Detecting C compiler ABI info
Detecting C compiler ABI info - done
Check for working CXX compiler: /usr/bin/c++
Check for working CXX compiler: /usr/bin/c++ -- works
Detecting CXX compiler ABI info
Detecting CXX compiler ABI info - done
CMake Error at CMakeLists.txt:24 (include):
  include could not find load file:

    Urho3D-CMake-common


CMake Error at CMakeLists.txt:27 (find_package):
  By not providing "FindUrho3D.cmake" in CMAKE_MODULE_PATH this project has
  asked CMake to find a package configuration file provided by "Urho3D", but
  CMake did not find one.

  Could not find a package configuration file provided by "Urho3D" with any
  of the following names:

    Urho3DConfig.cmake
    urho3d-config.cmake

  Add the installation prefix of "Urho3D" to CMAKE_PREFIX_PATH or set
  "Urho3D_DIR" to a directory containing one of the above files.  If "Urho3D"
  provides a separate development package or SDK, be sure it has been
  installed.


Configuring incomplete, errors occurred!
[/quote]

Interestingly enough, neither of those files exist inside the Urho3D tree. So no idea why it says it needs to locate files which simply don't exist.

So, moving on, I set CMAKE_BUILD_TYPE to "Debug". Now I'm specifically left with Urho3D_DIR. I've tried just about every combination I can imagine and nothing seems to make it happy. Regardless of the assigned value it's always reset back to 'Urho3D_DIR-NOTFOUND'. Which I guess it makes sense as the comments imply it should find of the files which has never existed.

Now then, I eventually did get things to work, but that was with actually installing things into /usr/local, via, "make install", however, that's not what I desire.

So, please feel free to kick me in the seat and tell me what I'm doing wrong. And in case it's not clear, heeeeellllpppp!  :frowning: 

Thanks,

-------------------------

ghidra | 2017-01-02 01:08:10 UTC | #2

Ok, so you have the Urho3D source folder, and a build folder. And set the URHO3D_HOME environment variable.
so far so good.

This is what I do.

I have a project folder, example "/urho_project".
Inside this folder I have a "/bin" folder and a "/src" folder.
And from the docs a "CMakeLists.txt"
as well, I have this script, that I call "/link.sh"
So I have so far:

[ul]
/urho_project
/urho_project/bin
/urho_project/src
/urho_project/link.sh
/urho_project/CMakeLists.txt
[/ul]

Use the script passing in the path to the Urho3D source directory.

[code]
sh ./link.sh /Urho3D
[/code]

Pardon my bash, but it works:
[code]
#!/bin/bash

#i need to create a bin folder if it does not exists

#setup.sh /Urho3D_Source
#needs 1 arguents, the urho source folder

make_alias(){
  #$1 FOLDER $2 LINKEDFOLDER $3 NEWFOLDER
  if [ ! -e $3 ];then
    #link does not exist, we can make it
    ln -s $2 $3
    echo "          -"$1" directory LINKED"
  else
    echo "          -"$1" link ALREADY EXISTS"
  fi
}

URHOPATH=$1
#first make sure that the given folder is good

if [ $# -eq 0 ];then
  echo "***********************************"
  echo "no arguments given, please provide:"
  echo "     -urho source path"
  echo "***********************************"
else
  if [ -d $URHOPATH ];then
  #if [[ ( -d $URHOPATH ) && ( -d $URHOBUILD ) ]];then

    echo "***********************************"
    echo "linking folders from urho source"

    # Absolute path this script is in, thus /home/user/bin
    SCRIPT=$(readlink -f "$0")
    SCRIPTPATH=$(dirname "$SCRIPT")

    #link the data and core data folder
    echo "     -link CMake, CoreData and Data folders"
    make_alias "CMake" $URHOPATH"/CMake" $SCRIPTPATH"/CMake"
    make_alias "CoreData" $URHOPATH"/bin/CoreData" $SCRIPTPATH"/bin/CoreData"
    make_alias "Data" $URHOPATH"/bin/Data" $SCRIPTPATH"/bin/Data"

    echo "***********************************"
    echo "create launch editor script"

    EDIT=$URHOPATH"/bin/Urho3DPlayer /Scripts/Editor.as -pp "$SCRIPTPATH"/bin -p \"CoreData;Data;Resources\" -w -s"
    EFILE=$SCRIPTPATH/editor.sh
    if [ -f "$EFILE" ];then
      printf "$EDIT" > $EFILE
      echo "     -editor.sh edited"
    else
      touch $EFILE
      printf "$EDIT" > $EFILE
      echo "     -editor.sh created"
    fi

    echo "***********************************"

  else
    echo "***********************************"
    echo "invalid path or paths given:"
    echo "     -source:" $URHOPATH
    echo "***********************************"
  fi
fi

[/code]

What this script does it a few things.
It makes some necessary symbolic links.

[ul]
/urho_project/bin/CoreData
/urho_project/bin/Data"
/urho_project/CMake
[/ul]

Side note: The bash script also creates another bash script called "editor.sh" I do this cause I usually modify it to pass in variables specific to my project as far as renderpaths that I want to editor to use, etc.

For completion, here is my CMakeLists.txt with a modification that searches sub folders in my "/src" directory:

[code]
# Set project name
project (your_urho_project_name)
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
set (TARGET_NAME urho_project_executable_name)

# Define source files
#define_source_files (GLOB_CPP_PATTERNS src/*.cpp src/*.cc GLOB_H_PATTERNS src/*.h)

define_source_files (GLOB_CPP_PATTERNS src/*.c* GLOB_H_PATTERNS src/*.h* RECURSE GROUP )

# Setup target with resource copying
setup_main_executable ()
[/code]

special attentions to the lines:

project (your_urho_project_name)
set (TARGET_NAME urho_project_executable_name)

-------------------------------------------------------

Add your code to src, and that should do it. It does it for me anyway.

-------------------------

coffee | 2017-01-02 01:08:10 UTC | #3

Thank you so much!

While I didn't mention it, I was already linking CoreData and Data. I wasn't, however, linking CMake at the root level. That instantly made everything happy.

[quote]You [u]may want[/u] to copy (or symlink) the 'CMake' subdir from Urho3D project root directory[/quote]

I double checked the reference documentation (link above) and the phrasing implies this is optional. Linking or copying the CMake directory is clearly mandatory and not something you may want to consider. In retrospect I should have given it a go since it is specifically mentioned as optional. Perhaps the documentation will be updated to indicate it is in fact mandatory, not optional?

Sweet! Thanks so much!

-------------------------

weitjong | 2017-01-02 01:08:10 UTC | #4

There is an even simpler way, especially since you are using Linux as Ruby/Rake is already preinstalled. Execute this in the Urho3D project root (Urho3D repo clone dir).
[code]
rake scaffolding dir=/path/to/your/own/project/root
[/code]

-------------------------

coffee | 2017-01-02 01:08:11 UTC | #5

I had to install ruby and rake to test. It too works fine.

Thanks!

-------------------------

