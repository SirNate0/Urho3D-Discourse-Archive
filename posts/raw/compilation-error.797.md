rogerdv | 2017-01-02 01:02:57 UTC | #1

Most of my game code is written in AS, I just have a basic launcher in C++, mostly based on Urho3d player. As I keep updating the engine from repos every day, I decided to recompile my code, something I havent done since the code was reorganized. But, I get this error:

[code]In file included from /home/roger/projects/Urho3D/include/Urho3D/Engine/../Core/Object.h:25:0,
                 from /home/roger/projects/Urho3D/include/Urho3D/Engine/Engine.h:25,
                 from /home/roger/projects/keyw/Source/UrhoQuickStart.cpp:1:
/home/roger/projects/Urho3D/include/Urho3D/Engine/../Core/../Container/LinkedList.h:29:19: error: variable ?Urho3D::URHO3D_API Urho3D::LinkedListNode? has initializer but incomplete type
 struct URHO3D_API LinkedListNode
                   ^
/home/roger/projects/Urho3D/include/Urho3D/Engine/../Core/../Container/LinkedList.h:29:19: warning: extended initializer lists only available with -std=c++11 or -std=gnu++11 [enabled by default]
/home/roger/projects/Urho3D/include/Urho3D/Engine/../Core/../Container/LinkedList.h:32:22: error: expected ?}? before ?:? token
     LinkedListNode() :
                      ^
/home/roger/projects/Urho3D/include/Urho3D/Engine/../Core/../Container/LinkedList.h:32:22: error: expected ?,? or ?;? before ?:? token
/home/roger/projects/Urho3D/include/Urho3D/Engine/../Core/../Container/LinkedList.h:38:5: error: ?LinkedListNode? does not name a type
     LinkedListNode* next_;
     ^
/home/roger/projects/Urho3D/include/Urho3D/Engine/../Core/../Container/LinkedList.h:171:1: error: expected declaration before ?}? token
 }
 ^
make[2]: *** [CMakeFiles/keyw.dir/UrhoQuickStart.cpp.o] Error 1
make[1]: *** [CMakeFiles/keyw.dir/all] Error 2
make: *** [all] Error 2
[/code]

Whats happening here?

-------------------------

devrich | 2017-01-02 01:02:58 UTC | #2

Don't know if this is anywhere near the right answer but I have encountered this sort of thing before when doing a lot of includes and then missing a semi-colon or a brace and sometime i have typed in 2 quotes by axident when i meant to only type in 1 quote.

Try checking your "UrhoQuickStart.cpp" file for one of the lines that tries to use the URHO3D_API LinkedListNode

hmmmmm although come to think about it; it might be that something changed in the Urho3D repo since the last time you downloaded it which causes that issue.  Does the "URHO3D_API LinkedListNode" still have the same aruments and argument types as what youre quickstart cpp uses ?

Don't know if any of that helps but hopfully :slight_smile:

-------------------------

rogerdv | 2017-01-02 01:02:58 UTC | #3

This code compiled perfectly last January 7. And here is the code, pretty minimal:

[code]#pragma once
#include "Urho3D/Engine/Application.h"

using namespace Urho3D;

class UrhoQuickStart : public Application
{
	OBJECT(UrhoQuickStart);
    public:
        UrhoQuickStart(Context* context);
        virtual void Start();
    private:
		/// Script file.
		SharedPtr<ScriptFile> scriptFile_;

		/// Handle reload start of the script file.
		void HandleScriptReloadStarted(StringHash eventType, VariantMap& eventData);
		/// Handle reload success of the script file.
		void HandleScriptReloadFinished(StringHash eventType, VariantMap& eventData);
		/// Handle reload failure of the script file.
		void HandleScriptReloadFailed(StringHash eventType, VariantMap& eventData);
};
[/code]

[code]#include "Urho3D/Engine/Engine.h"
#include "Urho3D/IO/FileSystem.h"
#include "Urho3D/IO/Log.h"
#include "Urho3D/Core/Main.h"
#include "Urho3D/Core/ProcessUtils.h"
#include "Urho3D/Resource/ResourceCache.h"
#include "Urho3D/Resource/ResourceEvents.h"
#include "Urho3D/Resource/XMLFile.h"
#include "Urho3D/Graphics/Renderer.h"
#include "Urho3D/Script/ScriptFile.h"
#include "Urho3D/Script/Script.h"

#include "UrhoQuickStart.h"

DEFINE_APPLICATION_MAIN(UrhoQuickStart)

UrhoQuickStart::UrhoQuickStart(Context* context) : Application(context)
{
	engineParameters_["WindowTitle"] = GetTypeName();
  engineParameters_["FullScreen"]  = true;
  engineParameters_["Headless"]    = false;
}

void UrhoQuickStart::Start()
{
  ResourceCache *cache = GetSubsystem<ResourceCache>();

  GetSubsystem<Renderer>()->SetDefaultRenderPath(cache->GetResource<XMLFile>("RenderPaths/Deferred.xml"));
  // Instantiate and register the AngelScript subsystem
	context_->RegisterSubsystem(new Script(context_));
	// Hold a shared pointer to the script file to make sure it is not unloaded during runtime
  scriptFile_ = cache->GetResource<ScriptFile>("Scripts/keyw.as");

	// If script loading is successful, proceed to main loop
  if (scriptFile_ && scriptFile_->Execute("void Start()"))  {
    // Subscribe to script's reload event to allow live-reload of the application
    SubscribeToEvent(scriptFile_, E_RELOADSTARTED, HANDLER(UrhoQuickStart, HandleScriptReloadStarted));
    SubscribeToEvent(scriptFile_, E_RELOADFINISHED, HANDLER(UrhoQuickStart, HandleScriptReloadFinished));
    SubscribeToEvent(scriptFile_, E_RELOADFAILED, HANDLER(UrhoQuickStart, HandleScriptReloadFailed));
    return;
  }

}


void UrhoQuickStart::HandleScriptReloadStarted(StringHash eventType, VariantMap& eventData)
{
    if (scriptFile_->GetFunction("void Stop()"))
        scriptFile_->Execute("void Stop()");
}

void UrhoQuickStart::HandleScriptReloadFinished(StringHash eventType, VariantMap& eventData)
{
    // Restart the script application after reload
    if (!scriptFile_->Execute("void Start()"))
    {
        scriptFile_.Reset();
        ErrorExit();
    }

}

void UrhoQuickStart::HandleScriptReloadFailed(StringHash eventType, VariantMap& eventData)
{
    scriptFile_.Reset();
    ErrorExit();
}
[/code]

-------------------------

devrich | 2017-01-02 01:02:58 UTC | #4

I'm looking over the linkedlist source now but did you try compiling using:

[code]-std=c++11[/code]

in your command line ?  the error says that it needs that in order to use linked list

-------------------------

devrich | 2017-01-02 01:02:58 UTC | #5

Also it has been recently modified so maybe that had somehtig to do with it but I don't know enough about Urho3D yet to have any better guesses.....

see [url]https://github.com/urho3d/Urho3D/commits/master/Source/Urho3D/Container/LinkedList.h[/url]

-------------------------

rogerdv | 2017-01-02 01:02:58 UTC | #6

[quote="devrich"]I'm looking over the linkedlist source now but did you try compiling using:

[code]-std=c++11[/code]

in your command line ?  the error says that it needs that in order to use linked list[/quote]

Noticed that too and added SET (CMAKE_CXX_FLAGS "-std=gnu++0x") to CmakeLists.txt, but that didnt solved the problem. Not sure if I did it in the right place. Here is the whole cmake file:

[code]# Set project name
project (keyw)
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
SET (CMAKE_CXX_FLAGS "-std=gnu++0x")
# Set CMake modules search path
set (CMAKE_MODULE_PATH $ENV{URHO3D_HOME}/CMake/Modules CACHE PATH "Path to Urho3D-specific CMake modules")
# Include Urho3D Cmake common module
include (Urho3D-CMake-common)
# Find Urho3D library
find_package (Urho3D REQUIRED)


include_directories (${URHO3D_INCLUDE_DIRS})# Define target name
set (TARGET_NAME keyw)
# Define source files
define_source_files ()
# Setup target with resource copying
setup_main_executable ()
[/code]

-------------------------

devrich | 2017-01-02 01:02:58 UTC | #7

hmm... maybe upgrade your version of GCC ? i've been using 4.9.2 since it came out...

also try changing that line to:
[code]-std=c++11[/code]

and I don't know if it'll help but I found this: [url]http://stackoverflow.com/questions/16886591/how-do-i-enable-c11-in-gcc[/url]

-------------------------

rogerdv | 2017-01-02 01:02:58 UTC | #8

Didnt worked. Im using gcc 4.8.2, which is the one included in Mint 17.1

-------------------------

JTippetts | 2017-01-02 01:02:58 UTC | #9

Try including <Urho3D/Urho3D.h> before you include any other headers. It's probably choking on URHO3D_API which is defined in the generated Urho3D.h header.

-------------------------

rogerdv | 2017-01-02 01:02:58 UTC | #10

Yes!! That solved the problem, thanks.

-------------------------

