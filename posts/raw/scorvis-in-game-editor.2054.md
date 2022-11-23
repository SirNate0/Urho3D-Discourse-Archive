Lumak | 2017-09-29 18:15:25 UTC | #1

I recently started working with scorbi's in-game editor found in his samples, [url=https://github.com/scorvi/Urho3DSamples/tree/master/06_InGameEditor]06_InGameEditor[/url].
When I was looking for his lost github link, I discovered that he also has Urho3DIDE repository, doh!
His IDE says "WIP does not work" and hasn't been updated for a year?

Anyway, I just converted the gizmo.as to c++ and have that working in the editor, see pic below (nothing impressive, just a terrain lvl with gizmo).
I'm curious if there are others doing the same work and would like to corroborate our efforts.

[details="pic"][img]http://i.imgur.com/gzZ1B2R.jpg?1[/img][/details]

-------------------------

Lumak | 2017-01-02 01:12:36 UTC | #2

I made a process of adding the in-game editor to any game or application easy by simply adding a few lines to a CMakeLists.txt.

Using 19 vehicle demo as an example:
[code]
# Define target name
set (TARGET_NAME 19_VehicleDemo)

# Define source files
define_source_files (EXTRA_H_FILES ${COMMON_SAMPLE_H_FILES})

#=================
# BEG: in-game editor
#=================
include_directories ( ../../Tools/InGameEditor/Source )  
include_directories ( ../../Tools/InGameEditor/Source/UI )  
file (GLOB IGE_CPP_FILES ../../Tools/InGameEditor/Source/*.cpp ../../Tools/InGameEditor/Source/UI/*.cpp  )
file (GLOB IGE_H_FILES ../../Tools/InGameEditor/Source/*.h ../../Tools/InGameEditor/Source/UI/*.h  )
source_group ("Source Files\\InGameEditor" FILES ${IGE_CPP_FILES})
source_group ("Header Files\\InGameEditor" FILES ${IGE_H_FILES})
### set ###
set (SOURCE_FILES ${CPP_FILES} ${H_FILES} ${IGE_CPP_FILES} ${IGE_H_FILES})
#=================
# END
#=================

# Setup target with resource copying
if (EMSCRIPTEN)
    # Override the Urho3D default
    math (EXPR EMSCRIPTEN_TOTAL_MEMORY "64 * 1024 * 1024")
    if (URHO3D_TESTING AND URHO3D_TEST_TIMEOUT LESS 15)
        set (URHO3D_TEST_TIMEOUT 15)
    endif ()
endif ()
setup_main_executable ()

# Setup test cases
setup_test ()
[/code]

The in-game editor code is built with whatever game you add to it. It's not a stand alone lib/so/dll that you link with.
There are changes that you need to add to your game code:
Add: 
    // 1) add to your constructor
    RegisterInGameEditor(context);

    // 2) add after you've created the game scene
    context_->RegisterSubsystem(new InGameEditor(context_));
    GetSubsystem<InGameEditor>()->SetGlobalScene( scene_ );

    // 3) in your HandleUpdate(...) func.
    if ( GetSubsystem<InGameEditor>()->IsVisible() ) return;

That's it. Very simple process.

Here's the outcome:

[img]http://i.imgur.com/Xo2lTcv.jpg?1[/img]

Comments and/or feedback welcome.

-------------------------

Lumak | 2017-01-02 01:12:37 UTC | #3

I've looked at scorvi's Urho3DIDE repository and it looks like he made lots of improvements from the original 06_ingameeditor.
I'll be merging those changes.

-------------------------

sabotage3d | 2017-01-02 01:12:38 UTC | #4

Nice. I played with this long time ago and I was quite useful.

-------------------------

Lumak | 2017-01-02 01:12:39 UTC | #5

[quote="sabotage3d"]Nice. I played with this long time ago and I was quite useful.[/quote]

I agree. It is useful.

I've built and ran scorvi's Urho3DIDE and it works.  Although there are some bugs, he's put in lots of good code base to work off of.

-------------------------

Lumak | 2017-01-02 01:12:39 UTC | #6

This is becoming more like a blog, ha.

Anyway, I got to thinking why rewrite the editor scripts to c++ when there are people who maintains and updates it.  

Doing a small experiment, I was able to call the editor script, similar to how urho3dplayer does it, from my game and loaded it no problem. Only small change to the script was to pass my game's scene and have it not reset the scene. I have a fully functional editor running in my game.

I will no longer be pursuing the c++ editor.

-------------------------

dakilla | 2017-09-29 13:55:30 UTC | #7

Amazing. Works really well :+1:

I thought that a new c++ editor would be nice, but I really like much an ingame editor, furthermore it's already fully functional.

could not it be integrated by default in the engine with a compile flag maybe ?

-------------------------

Lumak | 2017-10-09 02:06:49 UTC | #8

I never posted the link for it, but I think you're referring to this: https://github.com/Lumak/Urho3D-InGameEditor

-------------------------

Eugene | 2017-09-29 14:37:40 UTC | #9

[I hope I'll write some news about the subject in the nearest future]

-------------------------

