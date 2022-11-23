syjgin | 2017-01-02 01:02:05 UTC | #1

Hello. I am reading Urho3D documentation and I am trying to setup project. I have created Cmake file, as described there: urho3d.github.io/documentation/1.32/_using_library.html. Because I have already installed the engine, I changed 
cmake module path to: [code]
# Set CMake modules search path
set (CMAKE_MODULE_PATH $ENV{CMAKE_PREFIX_PATH}/share/CMake/Modules CACHE PATH "Path to Urho3D-specific CMake modules")
[/code]
I also added an environment variable URHO3D_HOME, which points to engine's installation directory (non-default). After that, when configure in cmake, I saw the following error:[code]CMake Error at CMakeLists.txt:19 (include):
  include could not find load file:

    Urho3D-CMake-common


CMake Error at CMakeLists.txt:21 (find_package):
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
[/code]
I was trying to change CMAKE_PREFIX_PATH to Urho installation directory, and, because there are no "share" folder in that directory, I changed it to "Sources". After all, my CmakeLists.txt contains these:
[code]# Set project name
project (helloUrho)
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
set (CMAKE_PREFIX_PATH "e:/Urho3D-1.32" )
# Set CMake modules search path
set (CMAKE_MODULE_PATH $ENV{CMAKE_PREFIX_PATH}/Source/CMake/Modules CACHE PATH "Path to Urho3D-specific CMake modules")
# Include Urho3D Cmake common module
include (Urho3D-CMake-common)
# Find Urho3D library
find_package (Urho3D REQUIRED)
include_directories (${URHO3D_INCLUDE_DIRS})
# Define target name
set (TARGET_NAME helloUrho)
# Define source files
define_source_files ()
# Setup target with resource copying
setup_main_executable ()[/code]
Maybe someone knows, what's wrong?

-------------------------

syjgin | 2017-01-02 01:02:05 UTC | #2

I solved it, maybe this will be helpfull to someone with same error:
[code]# Set project name
project (helloUrho)
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
set (TARGET_NAME helloUrho)
# Define source files
define_source_files ()
# Setup target with resource copying
setup_main_executable ()[/code]
Add "using" here:
[code]
#include "Application.h"
#include "Engine.h"
#include "InputEvents.h"
using namespace Urho3D;

class MyApp : public Application
{
public:
    MyApp(Context* context) :
        Application(context)
    {
    }
    virtual void Setup()
    {
        // Called before engine initialization. engineParameters_ member variable can be modified here
    }
    virtual void Start()
    {
        // Called after engine initialization. Setup application & subscribe to events here
        SubscribeToEvent(E_KEYDOWN, HANDLER(MyApp, HandleKeyDown));
    }
    virtual void Stop()
    {
        // Perform optional cleanup after main loop has terminated
    }
    
    void HandleKeyDown(StringHash eventType, VariantMap& eventData)
    {
        using namespace KeyDown;
        // Check for pressing ESC. Note the engine_ member variable for convenience access to the Engine object
        int key = eventData[P_KEY].GetInt();
        if (key == KEY_ESC)
            engine_->Exit();
    }
};
DEFINE_APPLICATION_MAIN(MyApp)
[/code]

-------------------------

