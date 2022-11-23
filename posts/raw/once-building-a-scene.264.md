vivienneanthony | 2017-01-02 00:59:14 UTC | #1

Hi,

By the way, Thanks for everyone help.

So, I'm almost done with one building so I have to play with the texture. Now, what is the best way to create a executable.

I have Ubuntu 12.04 with C/C++ codeblocks. I'm familiar with C++ so if I can link Urho3D as a library then it should be straight forward. Are there any examples? Additionally, what do I need to build to make it work. (I just have to do the coding part).

Vivienne

-------------------------

friesencr | 2017-01-02 00:59:14 UTC | #2

There are a ludicris amount of cpp samples generously provided.  

[github.com/urho3d/Urho3D/tree/m ... ce/Samples](https://github.com/urho3d/Urho3D/tree/master/Source/Samples)

There is a DEFINE_APPLICATION macro which require a class with a small amount of implementation.  Setting up a cmake project would be the fastest way to get all the includes/linker sorted out.  It has the added benefit of making your project easier to work on many platforms.  I am on windows/mac/linux depending on my blood sugar, locality of nearest computer, and the whims of astral forces.

I am personally using a slightly modified copy/paste of the samples code and am using an the 'external library' feature as described here: [urho3d.github.io/documentation/a00004.html](http://urho3d.github.io/documentation/a00004.html). As I take on more cpp code I will probably migrate from using the library method to maintaining a fork of urho3d.

-------------------------

vivienneanthony | 2017-01-02 00:59:17 UTC | #3

[quote="friesencr"]There are a ludicris amount of cpp samples generously provided.  

[github.com/urho3d/Urho3D/tree/m ... ce/Samples](https://github.com/urho3d/Urho3D/tree/master/Source/Samples)

There is a DEFINE_APPLICATION macro which require a class with a small amount of implementation.  Setting up a cmake project would be the fastest way to get all the includes/linker sorted out.  It has the added benefit of making your project easier to work on many platforms.  I am on windows/mac/linux depending on my blood sugar, locality of nearest computer, and the whims of astral forces.

I am personally using a slightly modified copy/paste of the samples code and am using an the 'external library' feature as described here: [urho3d.github.io/documentation/a00004.html](http://urho3d.github.io/documentation/a00004.html). As I take on more cpp code I will probably migrate from using the library method to maintaining a fork of urho3d.[/quote]

I'm trying to figure it out because I usually use Codeblocks.

Using the cmake.  I created the .txt files and the directory structure. This is what I get when running Cmake. I know the includes are located in /usr/local/includes/Urho3d/ and core root 

[quote]vivienne@vivienne-System-Product-Name:/media/home2/vivienne/urho3dapplications/HelloGui/Source$ cmake CmakeLists.txt
-- The C compiler identification is GNU 4.6.3
-- The CXX compiler identification is GNU 4.6.3
-- Check for working C compiler: /usr/bin/cc
-- Check for working C compiler: /usr/bin/cc -- works
-- Detecting C compiler ABI info
-- Detecting C compiler ABI info - done
-- Check for working CXX compiler: /usr/bin/c++
-- Check for working CXX compiler: /usr/bin/c++ -- works
-- Detecting CXX compiler ABI info
-- Detecting CXX compiler ABI info - done
CMake Error at CMakeLists.txt:11 (include):
  include could not find load file:

    Urho3D-CMake-common


CMake Error at CMakeLists.txt:13 (find_package):
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


-- Configuring incomplete, errors occurred!
See also "/media/home2/vivienne/urho3dapplications/HelloGui/Source/CMakeFiles/CMakeOutput.log".
vivienne@vivienne-System-Product-Name:/media/home2/vivienne/urho3dapplications/HelloGui/Source$ [/quote]

Core Files
[quote]
vivienne@vivienne-System-Product-Name:/usr/local/share/Urho3D$ ls -l                                                                                                                                       
total 20                                                                                                                                                                                                   
drwxr-xr-x 4 root root 4096 May 15 11:12 Bin                                                                                                                                                               
drwxr-xr-x 4 root root 4096 May 15 11:12 CMake                                                                                                                                                             
drwxr-xr-x 2 root root 4096 May 15 11:12 Docs                                                                                                                                                              
drwxr-xr-x 2 root root 4096 May 15 11:12 Scripts                                                                                                                                                           
drwxr-xr-x 3 root root 4096 May 15 11:12 templates              

vivienne@vivienne-System-Product-Name:/media/home2/vivienne/urho3dapplications/HelloGui/Source$ echo $URHO3D_HOME
/usr/local/share/Urho3D/
vivienne@vivienne-System-Product-Name:/media/home2/vivienne/urho3dapplications/HelloGui/Source$ 

[/quote]

-------------------------

vivienneanthony | 2017-01-02 00:59:18 UTC | #4

After I fixed the cmake file. This is the new prompt

[quote]
vivienne@vivienne-System-Product-Name:/media/home2/vivienne/urho3dapplications/HelloGui/Source$ cmake CmakeLists.txt
-- The C compiler identification is GNU 4.6.3
-- The CXX compiler identification is GNU 4.6.3
-- Check for working C compiler: /usr/bin/cc
-- Check for working C compiler: /usr/bin/cc -- works
-- Detecting C compiler ABI info
-- Detecting C compiler ABI info - done
-- Check for working CXX compiler: /usr/bin/c++
-- Check for working CXX compiler: /usr/bin/c++ -- works
-- Detecting CXX compiler ABI info
-- Detecting CXX compiler ABI info - done
CMake Error at /usr/local/share/Urho3D/CMake/Modules/FindUrho3D.cmake:166 (message):
  Could not find Urho3D library in default SDK installation location or
  Urho3D project root tree.  For searching in a non-default Urho3D SDK
  installation, use 'URHO3D_INSTALL_PREFIX' environment variable to specify
  the prefix path of the installation location.  For searching in a build
  tree of Urho3D project, use 'URHO3D_HOME' environment variable to specify
  the Urho3D project root directory.  The Urho3D library itself must already
  be built successfully.
Call Stack (most recent call first):
  CMakeLists.txt:13 (find_package)
[/quote]

-------------------------

vivienneanthony | 2017-01-02 00:59:18 UTC | #5

So, I copied the Source, Lib, Build folders in my directory to /usr/local/share/Urho3D. It seemed to work but the latest bug I get is.
Not sure why add executable is adding wrong parameters... 

Any clue?

[quote]vivienne@vivienne-System-Product-Name:/media/home2/vivienne/urho3dapplications/HelloGui/Source$ cmake CmakeLists.txt
-- The C compiler identification is GNU 4.6.3
-- The CXX compiler identification is GNU 4.6.3
-- Check for working C compiler: /usr/bin/cc
-- Check for working C compiler: /usr/bin/cc -- works
-- Detecting C compiler ABI info
-- Detecting C compiler ABI info - done
-- Check for working CXX compiler: /usr/bin/c++
-- Check for working CXX compiler: /usr/bin/c++ -- works
-- Detecting CXX compiler ABI info
-- Detecting CXX compiler ABI info - done
CMake Error at /usr/local/share/Urho3D/CMake/Modules/Urho3D-CMake-common.cmake:481 (add_executable):
  add_executable called with incorrect number of arguments
Call Stack (most recent call first):
  /usr/local/share/Urho3D/CMake/Modules/Urho3D-CMake-common.cmake:579 (setup_executable)
  CMakeLists.txt:20 (setup_main_executable)


-- Configuring incomplete, errors occurred!
See also "/media/home2/vivienne/urho3dapplications/HelloGui/Source/CMakeFiles/CMakeOutput.log".
vivienne@vivienne-System-Product-Name:/media/home2/vivienne/urho3dapplications/HelloGui/Source$ 
[/quote]

The offending code seems to be somewhere here

[quote]macro (setup_executable)
    # Parse extra arguments
    cmake_parse_arguments (ARG "NODEPS" "" "" ${ARGN})

    add_executable (${TARGET_NAME} ${ARG_UNPARSED_ARGUMENTS} ${SOURCE_FILES})
    if (ARG_NODEPS)
        define_dependency_libs (Urho3D-nodeps)
    else ()
        define_dependency_libs (Urho3D)
    endif ()
    setup_target ()[/quote]

-------------------------

rasteron | 2017-01-02 00:59:18 UTC | #6

As Chris already mentioned, you may want to try out the Sample codes to get a firm grasp on how to build it static/dynamic.

Given you already have all the requirements, just edit the cmake_gcc.sh and replace the first (or all) instance of "Unix Makefiles" to "CodeBlocks - Unix Makefiles" save it and run

[code]./cmake_gcc.sh -DURHO3D_SAMPLES=1[/code]

This will generate the CodeBlocks .cbp file for building with the sample executables.

-------------------------

vivienneanthony | 2017-01-02 00:59:18 UTC | #7

[quote="rasteron"]As Chris already mentioned, you may want to try out the Sample codes to get a firm grasp on how to build it static/dynamic.[/quote]

I will just need to get it to compile firstly cmakke. So I can start doing the examples and samples.

-------------------------

vivienneanthony | 2017-01-02 00:59:18 UTC | #8

Hi

The following produces lines. Which is odd because SOURCE_FILES and ARG_UNPARSED_ARGUMENTS comes out to be blank. Maybe someone has a idea what's going on?

Vivienne


[quote]
    # Parse extra arguments

   cmake_parse_arguments (ARG "NODEPS" "" "" ${ARGN})

   message ("Attempt to add_executable")
   message ("${TARGET_NAME}")
   message ("${ARG_UNPARSED_ARGUMENTS}")
   message ("${SOURCE_FILES}")

    add_executable (${TARGET_NAME} ${ARG_UNPARSED_ARGUMENTS} ${SOURCE_FILES})
[/quote]

Outputs this to the console

[b]-- Configuring incomplete, errors occurred!
See also "/media/home2/vivienne/urho3dapplications/HelloGui/Source/CMakeFiles/CMakeOutput.log".
vivienne@vivienne-System-Product-Name:/media/home2/vivienne/urho3dapplications/HelloGui/Source$ cmake CmakeLists.txt
Attempt to add_executable
MyExecutableName


CMake Error at /usr/local/share/Urho3D/Source/CMake/Modules/Urho3D-CMake-common.cmake:488 (add_executable):
  add_executable called with incorrect number of arguments
Call Stack (most recent call first):
  /usr/local/share/Urho3D/Source/CMake/Modules/Urho3D-CMake-common.cmake:586 (setup_executable)
  CMakeLists.txt:20 (setup_main_executable)


-- Configuring incomplete, errors occurred!
See also "/media/home2/vivienne/urho3dapplications/HelloGui/Source/CMakeFiles/CMakeOutput.log".
[/b]

-------------------------

vivienneanthony | 2017-01-02 00:59:18 UTC | #9

Hello World worked!

-------------------------

rasteron | 2017-01-02 00:59:18 UTC | #10

Nice, but please check my updated reply above, as this will instruct cmake to build with all samples under CodeBlocks  :slight_smile:


[img]http://i.imgur.com/4doBR92.jpg[/img]

-------------------------

vivienneanthony | 2017-01-02 00:59:18 UTC | #11

[quote="rasteron"]Nice, but please check my updated reply above, as this will instruct cmake to build with all samples under CodeBlocks  :slight_smile:


[img]http://i.imgur.com/4doBR92.jpg[/img][/quote]

Okay. Thanks.

-------------------------

vivienneanthony | 2017-01-02 00:59:19 UTC | #12

[quote="rasteron"]Nice, but please check my updated reply above, as this will instruct cmake to build with all samples under CodeBlocks  :slight_smile:


[img]http://i.imgur.com/4doBR92.jpg[/img][/quote]

I'm looking through it now and will play through the samples. I'm assuming to build something on my own. I can copy the folder and strip the Codeblock project of the additional Tools and Samples then go from there.

-------------------------

vivienneanthony | 2017-01-02 00:59:20 UTC | #13

[quote="rasteron"]Nice, but please check my updated reply above, as this will instruct cmake to build with all samples under CodeBlocks  :slight_smile:
[/quote]

So, I took that project created as a template. I modified the CMakeLists.txt lines with 64 bit suffix(etc!) and samples with only one sample which is the HelloGui. I think I have to edit the common file also to default 64 bit and samples. Renaming "Samples" to my "Gamecore".

I was thinking of keeping that layout. Change the project name to the Existence then make the sample folder as the main game executables. The tools can be additional executables for now. I would have to strip a lot of unnecessary code because I don't want a "make install" to work.

Update 

[b]I tried adding the following lines in CMakeLists.txt. I tried that way and with =1 added. Wouldn't that be the same as "./cmake... --DURHO3D_64BIT" or any other flag
[/b]

SAMPLES would be changed to GAMECORE

[quote]# Set flags
add_definitions(-DURHO3D_ANGELSCRIPT)
add_definitions(-DURHO3D_64BIT)
add_definitions(-DURHO3D_SAMPLES)
[/quote]Vivienne

-------------------------

