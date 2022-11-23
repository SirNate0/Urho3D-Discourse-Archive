jjd | 2017-01-02 00:59:27 UTC | #1

Hi,

I'm trying to use Urho3d as an external library. I have followed the guide: /documentation/a00004.html and got everything working fine for vs2012 but can't get cmake_android.bat working. I get the an error "Could not find Urho3D library in default SDK installation location..." 

Does anyone know what I'm missing to get an external android build working? sorry this is all new to me. 

Here is the full log of the FindUrho3D.cmake

[code]
D:/Projects/GameDev/MyGame/Source/CMakeLists.txt(13):  find_package(Urho3D REQUIRED )
D:/Projects/GameDev/Urho3D/Source/CMake/Modules/FindUrho3D.cmake(33):  if(URHO3D_FOUND )
D:/Projects/GameDev/Urho3D/Source/CMake/Modules/FindUrho3D.cmake(38):  if(NOT URHO3D_LIB_TYPE STREQUAL URHO3D_FOUND_LIB_TYPE )
D:/Projects/GameDev/Urho3D/Source/CMake/Modules/FindUrho3D.cmake(48):  set(URHO3D_LIB_NAMES Urho3D )
D:/Projects/GameDev/Urho3D/Source/CMake/Modules/FindUrho3D.cmake(49):  if(WIN32 )
D:/Projects/GameDev/Urho3D/Source/CMake/Modules/FindUrho3D.cmake(53):  if(CMAKE_PROJECT_NAME STREQUAL Urho3D AND PROJECT_ROOT_DIR )
D:/Projects/GameDev/Urho3D/Source/CMake/Modules/FindUrho3D.cmake(56):  elseif(NOT URHO3D_HOME AND DEFINED ENV{URHO3D_HOME} )
D:/Projects/GameDev/Urho3D/Source/CMake/Modules/FindUrho3D.cmake(60):  if(URHO3D_HOME )
D:/Projects/GameDev/Urho3D/Source/CMake/Modules/FindUrho3D.cmake(62):  find_file(URHO3D_SOURCE_TREE Urho3D.h.in ${URHO3D_HOME}/Source/Engine DOC Path to Urho3D project source tree NO_DEFAULT_PATH NO_CMAKE_FIND_ROOT_PATH )
D:/Projects/GameDev/Urho3D/Source/CMake/Modules/FindUrho3D.cmake(63):  if(URHO3D_SOURCE_TREE )
D:/Projects/GameDev/Urho3D/Source/CMake/Modules/FindUrho3D.cmake(64):  get_filename_component(URHO3D_SOURCE_TREE ${URHO3D_SOURCE_TREE} PATH )
D:/Projects/GameDev/Urho3D/Source/CMake/Modules/FindUrho3D.cmake(65):  set(URHO3D_INCLUDE_DIRS ${URHO3D_SOURCE_TREE} )
D:/Projects/GameDev/Urho3D/Source/CMake/Modules/FindUrho3D.cmake(66):  foreach(DIR Audio Container Core Engine Graphics Input IO LuaScript Math Navigation Network Physics Resource Scene Script UI Urho2D )
D:/Projects/GameDev/Urho3D/Source/CMake/Modules/FindUrho3D.cmake(67):  list(APPEND URHO3D_INCLUDE_DIRS ${URHO3D_SOURCE_TREE}/${DIR} )
D:/Projects/GameDev/Urho3D/Source/CMake/Modules/FindUrho3D.cmake(67):  list(APPEND URHO3D_INCLUDE_DIRS ${URHO3D_SOURCE_TREE}/${DIR} )
D:/Projects/GameDev/Urho3D/Source/CMake/Modules/FindUrho3D.cmake(67):  list(APPEND URHO3D_INCLUDE_DIRS ${URHO3D_SOURCE_TREE}/${DIR} )
D:/Projects/GameDev/Urho3D/Source/CMake/Modules/FindUrho3D.cmake(67):  list(APPEND URHO3D_INCLUDE_DIRS ${URHO3D_SOURCE_TREE}/${DIR} )
D:/Projects/GameDev/Urho3D/Source/CMake/Modules/FindUrho3D.cmake(67):  list(APPEND URHO3D_INCLUDE_DIRS ${URHO3D_SOURCE_TREE}/${DIR} )
D:/Projects/GameDev/Urho3D/Source/CMake/Modules/FindUrho3D.cmake(67):  list(APPEND URHO3D_INCLUDE_DIRS ${URHO3D_SOURCE_TREE}/${DIR} )
D:/Projects/GameDev/Urho3D/Source/CMake/Modules/FindUrho3D.cmake(67):  list(APPEND URHO3D_INCLUDE_DIRS ${URHO3D_SOURCE_TREE}/${DIR} )
D:/Projects/GameDev/Urho3D/Source/CMake/Modules/FindUrho3D.cmake(67):  list(APPEND URHO3D_INCLUDE_DIRS ${URHO3D_SOURCE_TREE}/${DIR} )
D:/Projects/GameDev/Urho3D/Source/CMake/Modules/FindUrho3D.cmake(67):  list(APPEND URHO3D_INCLUDE_DIRS ${URHO3D_SOURCE_TREE}/${DIR} )
D:/Projects/GameDev/Urho3D/Source/CMake/Modules/FindUrho3D.cmake(67):  list(APPEND URHO3D_INCLUDE_DIRS ${URHO3D_SOURCE_TREE}/${DIR} )
D:/Projects/GameDev/Urho3D/Source/CMake/Modules/FindUrho3D.cmake(67):  list(APPEND URHO3D_INCLUDE_DIRS ${URHO3D_SOURCE_TREE}/${DIR} )
D:/Projects/GameDev/Urho3D/Source/CMake/Modules/FindUrho3D.cmake(67):  list(APPEND URHO3D_INCLUDE_DIRS ${URHO3D_SOURCE_TREE}/${DIR} )
D:/Projects/GameDev/Urho3D/Source/CMake/Modules/FindUrho3D.cmake(67):  list(APPEND URHO3D_INCLUDE_DIRS ${URHO3D_SOURCE_TREE}/${DIR} )
D:/Projects/GameDev/Urho3D/Source/CMake/Modules/FindUrho3D.cmake(67):  list(APPEND URHO3D_INCLUDE_DIRS ${URHO3D_SOURCE_TREE}/${DIR} )
D:/Projects/GameDev/Urho3D/Source/CMake/Modules/FindUrho3D.cmake(67):  list(APPEND URHO3D_INCLUDE_DIRS ${URHO3D_SOURCE_TREE}/${DIR} )
D:/Projects/GameDev/Urho3D/Source/CMake/Modules/FindUrho3D.cmake(67):  list(APPEND URHO3D_INCLUDE_DIRS ${URHO3D_SOURCE_TREE}/${DIR} )
D:/Projects/GameDev/Urho3D/Source/CMake/Modules/FindUrho3D.cmake(67):  list(APPEND URHO3D_INCLUDE_DIRS ${URHO3D_SOURCE_TREE}/${DIR} )
D:/Projects/GameDev/Urho3D/Source/CMake/Modules/FindUrho3D.cmake(69):  set(DIRS Box2D Bullet/src kNet/include SDL/include )
D:/Projects/GameDev/Urho3D/Source/CMake/Modules/FindUrho3D.cmake(70):  if(URHO3D_ANGELSCRIPT )
D:/Projects/GameDev/Urho3D/Source/CMake/Modules/FindUrho3D.cmake(71):  list(APPEND DIRS AngelScript/include )
D:/Projects/GameDev/Urho3D/Source/CMake/Modules/FindUrho3D.cmake(73):  foreach(DIR ${DIRS} )
D:/Projects/GameDev/Urho3D/Source/CMake/Modules/FindUrho3D.cmake(74):  list(APPEND URHO3D_INCLUDE_DIRS ${URHO3D_HOME}/Source/ThirdParty/${DIR} )
D:/Projects/GameDev/Urho3D/Source/CMake/Modules/FindUrho3D.cmake(74):  list(APPEND URHO3D_INCLUDE_DIRS ${URHO3D_HOME}/Source/ThirdParty/${DIR} )
D:/Projects/GameDev/Urho3D/Source/CMake/Modules/FindUrho3D.cmake(74):  list(APPEND URHO3D_INCLUDE_DIRS ${URHO3D_HOME}/Source/ThirdParty/${DIR} )
D:/Projects/GameDev/Urho3D/Source/CMake/Modules/FindUrho3D.cmake(74):  list(APPEND URHO3D_INCLUDE_DIRS ${URHO3D_HOME}/Source/ThirdParty/${DIR} )
D:/Projects/GameDev/Urho3D/Source/CMake/Modules/FindUrho3D.cmake(74):  list(APPEND URHO3D_INCLUDE_DIRS ${URHO3D_HOME}/Source/ThirdParty/${DIR} )
D:/Projects/GameDev/Urho3D/Source/CMake/Modules/FindUrho3D.cmake(78):  if(IS_INTERNAL )
D:/Projects/GameDev/Urho3D/Source/CMake/Modules/FindUrho3D.cmake(80):  elseif(ANDROID AND CMAKE_HOST_WIN32 AND NOT URHO3D_MKLINK )
D:/Projects/GameDev/Urho3D/Source/CMake/Modules/FindUrho3D.cmake(81):  set(BINARY_DIR ${URHO3D_HOME}/Source/Android )
D:/Projects/GameDev/Urho3D/Source/CMake/Modules/FindUrho3D.cmake(85):  list(APPEND URHO3D_INCLUDE_DIRS ${BINARY_DIR}/Engine )
D:/Projects/GameDev/Urho3D/Source/CMake/Modules/FindUrho3D.cmake(86):  if(ANDROID )
D:/Projects/GameDev/Urho3D/Source/CMake/Modules/FindUrho3D.cmake(87):  if(IS_INTERNAL )
D:/Projects/GameDev/Urho3D/Source/CMake/Modules/FindUrho3D.cmake(89):  else()
D:/Projects/GameDev/Urho3D/Source/CMake/Modules/FindUrho3D.cmake(90):  set(URHO3D_LIB_SEARCH_PATH ${BINARY_DIR}/libs/${ANDROID_NDK_ABI_NAME} )
D:/Projects/GameDev/Urho3D/Source/CMake/Modules/FindUrho3D.cmake(95):  if(TARGET Urho3D )
D:/Projects/GameDev/Urho3D/Source/CMake/Modules/FindUrho3D.cmake(98):  else()
D:/Projects/GameDev/Urho3D/Source/CMake/Modules/FindUrho3D.cmake(99):  find_library(URHO3D_LIBRARIES NAMES ${URHO3D_LIB_NAMES} PATHS ${URHO3D_LIB_SEARCH_PATH} NO_DEFAULT_PATH NO_CMAKE_FIND_ROOT_PATH )
D:/Projects/GameDev/Urho3D/Source/CMake/Modules/FindUrho3D.cmake(100):  if(WIN32 )
D:/Projects/GameDev/Urho3D/Source/CMake/Modules/FindUrho3D.cmake(143):  if(WIN32 )
D:/Projects/GameDev/Urho3D/Source/CMake/Modules/FindUrho3D.cmake(154):  if(URHO3D_INCLUDE_DIRS AND URHO3D_LIBRARIES )
D:/Projects/GameDev/Urho3D/Source/CMake/Modules/FindUrho3D.cmake(161):  if(URHO3D_FOUND )
D:/Projects/GameDev/Urho3D/Source/CMake/Modules/FindUrho3D.cmake(164):  else()
D:/Projects/GameDev/Urho3D/Source/CMake/Modules/FindUrho3D.cmake(165):  if(Urho3D_FIND_REQUIRED )
D:/Projects/GameDev/Urho3D/Source/CMake/Modules/FindUrho3D.cmake(166):  message(FATAL_ERROR Could not find Urho3D library in default SDK installation location or Urho3D project root tree.  For searching in a non-default Urho3D SDK installation, use 'URHO3D_INSTALL_PREFIX' environment variable to specify the prefix path of the installation location.  For searching in a build tree of Urho3D project, use 'URHO3D_HOME' environment variable to specify the Urho3D project root directory. The Urho3D library itself must already be built successfully. )
CMake Error at D:/Projects/GameDev/Urho3D/Source/CMake/Modules/FindUrho3D.cmake:166 (message):
  Could not find Urho3D library in default SDK installation location or
  Urho3D project root tree.  For searching in a non-default Urho3D SDK
  installation, use 'URHO3D_INSTALL_PREFIX' environment variable to specify
  the prefix path of the installation location.  For searching in a build
  tree of Urho3D project, use 'URHO3D_HOME' environment variable to specify
  the Urho3D project root directory.  The Urho3D library itself must already
  be built successfully.
Call Stack (most recent call first):
  CMakeLists.txt:13 (find_package)
[/code]

cmake variables

[code]
// Setup build for iOS platform
IOS:BOOL=OFF

// root for library output, set this to change where android libs are installed to
LIBRARY_OUTPUT_PATH_ROOT:PATH=D:/Projects/GameDev/WorldCupBounce/android-Build

// Setup build for Raspberry Pi platform
RASPI:BOOL=OFF

// Enable 64-bit build
URHO3D_64BIT:BOOL=OFF

// Enable AngelScript scripting support
URHO3D_ANGELSCRIPT:BOOL=ON

// Path to Urho3D project root tree
URHO3D_HOME:PATH=D:/Projects/GameDev/Urho3D

// Path to a library.
URHO3D_LIBRARIES:FILEPATH=URHO3D_LIBRARIES-NOTFOUND

// Specify Urho3D library type, possible values are STATIC (default) and SHARED
URHO3D_LIB_TYPE:STRING=STATIC

// Enable logging support
URHO3D_LOGGING:BOOL=ON

// Enable additional Lua scripting support
URHO3D_LUA:BOOL=OFF

// Enable Lua scripting support using LuaJIT (check LuaJIT's CMakeLists.txt for more options)
URHO3D_LUAJIT:BOOL=OFF

// Enable profiling support
URHO3D_PROFILING:BOOL=ON

// Path to Urho3D project source tree
URHO3D_SOURCE_TREE:FILEPATH=D:/Projects/GameDev/Urho3D/Source/Engine/Urho3D.h.in

// Enable SSE instruction set
URHO3D_SSE:BOOL=ON

// Enable testing support
URHO3D_TESTING:BOOL=OFF
[/code]

I have built Urho3D from source and also ran cmake_android.bat which worked fine internally (built Urho3Dplayer)

Thanks
James

-------------------------

weitjong | 2017-01-02 00:59:28 UTC | #2

It is not clear whether you have built the Urho3D library for Android platform or not in your post. If you use cmake_vs2012.bat, you only built Urho3D static library for Windows platform. You need to use cmake_android.bat to target for Android platform. Basically you need to use cmake_android.bat twice. Once for configuring and generating a project file which builds Urho3D library for Android platform; and the second time for configuring and generating another project file which builds your own application using Urho3D as external library.

-------------------------

jjd | 2017-01-02 00:59:28 UTC | #3

I think I have built the Urho3D library for Android. My steps:

[b]Urho3D[/b]
run cmake_vs2012
Compile in vs2012
run cmake_android

[b]My Application[/b]
Create CMakeLists.txt in my application/source directory (From guide)
Copy all the cmake_*.bat scripts from Urho3D to the root of my application
run my application/cmake_vs2012
Compile in vs2012
run my application/cmake_android [b]Fails[/b]

[quote="weitjong"] the second time for configuring and generating another project file which builds your own application using Urho3D as external library.[/quote]

I must be doing this step wrong?

-------------------------

weitjong | 2017-01-02 00:59:28 UTC | #4

If you just target Android platform, you don't need to execute cmake_vs2012.bat

[b]Urho3D library[/b]
run cmake_android
build the project by using Android NDK or via Eclipse ADT.

[b]My Application[/b]
Create CMakeLists.txt in my application/source directory (From guide)
Copy all the cmake_*.bat scripts from Urho3D to the root of my application
Set the URHO3D_HOME (which I think you already did)
run my application/cmake_android
build the project by using Android NDK+SDK or via Eclipse ADT.

The cmake_* bat/scripts and the Urho3D CMake modules are designed in such a way that they work for both Urho3D project and any external (i.e. your own) project.

If you still have problem, check the content of the Android library directory in %URHO3D_HOME%\android-Build\libs\ to see you have any android library files generated there.

-------------------------

jjd | 2017-01-02 00:59:28 UTC | #5

Solved

[quote]check the content of the Android library directory in %URHO3D_HOME%\android-Build\libs\ to see you have any android library files generated there.[/quote]

This pointed me in the right direction. I did have android library files generated in %URHO3D_HOME%\android-Build\libs\ but  FindUrho3D.cmake is looking for the library files in ${URHO3D_HOME}/Source/Android. 

FindUrho3D.cmake code:
[code]
 # For non Urho3D project using Urho3D as external library, Urho3D project itself must be built using predefined build directory as per specified in the provided build scripts.
        if (IS_INTERNAL)
            set (BINARY_DIR ${CMAKE_BINARY_DIR})
        elseif (ANDROID AND CMAKE_HOST_WIN32 AND NOT URHO3D_MKLINK)
            set (BINARY_DIR ${URHO3D_HOME}/Source/Android)
        else ()
            set (BINARY_DIR ${URHO3D_HOME}/${PLATFORM_PREFIX}Build)
[/code]

I am running "cmake_android.bat -DURHO3D_MKLINK=1" so not sure why the FindUrho3D is detecting that I don't have URHO3D_MKLINK set. Anyway my work around was to replace  set (BINARY_DIR ${URHO3D_HOME}/Source/Android) with  set (BINARY_DIR ${URHO3D_HOME}/${PLATFORM_PREFIX}Build) and everything worked.

Thanks for your help.

-------------------------

