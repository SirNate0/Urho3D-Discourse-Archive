wllo10 | 2019-03-21 12:51:38 UTC | #1

Viewing the 3d samples always results in models being squashed on linux. For example grabbing the repository from git and executing NinjaSnowWar always result with models similar to the ones seen in the picture. Similar to other problems I tried fixing it with removing the -ffast-math option from UrhoCommon.cmake but that doesn't change anything. It works fine on windows10.
Downloading the tar from the website results in the same problem. Removing the -ffast option fixes the problem for a short time. The problem persists later on when one recompiles with make. ![urho_sample_18|642x500](upload://j5GGynRZpfqp1qEtX6IWmycvmyg.png) .

-------------------------

dertom | 2019-03-21 14:22:54 UTC | #2

Strange. Just tried Sample18 on latest master (ubuntu18.04). And it worked as expected. Also strange that your cam is upside down!? Sry, that I'm no help to you...

-------------------------

weitjong | 2019-03-21 14:36:14 UTC | #3

This is a known issue with release 1.7 when build using GCC 8.x. There is a patch in the master branch that fixes this. But removing the -ffast-math compiler option should be the gist of the fix. Have you regenerated the build tree before invoking make?

-------------------------

wllo10 | 2019-03-21 15:56:06 UTC | #4

[quote="weitjong, post:3, topic:5045"]
removing the -ffast-math compiler option should be the gist of the fix
[/quote]
I have tried this it doesn't seem to work for the master branch. If there is a patch how do I apply it?
[quote="weitjong, post:3, topic:5045"]
Have you regenerated the build tree before invoking make?
[/quote]
How do I do this? Is there a way to use clang instead of gcc? ![Screenshot_20190321_164704|690x388](upload://nJ99nt7uMwFLRt8qcKGhDMQZWC8.jpeg)

-------------------------

weitjong | 2019-03-21 16:35:48 UTC | #5

What GCC version are you using? It is weird when you said you also faced this problem even on the master branch, as this is unheard of so far.

Are you using out of source build? If yes, it is just a simple ‘rm’ operation of the previously generated build tree and redo the initial CMake configuration and generation again. And you can use Clang by exporting ‘CC’ and ‘CXX’ env-var to use ‘clang’ and ‘clang++’ as usual as in any other software building. Do that before reinvoking inital CMake configuration. Once the build tree is generated for one compiler toolchain, it cannot be changed to the other.

-------------------------

wllo10 | 2019-03-21 19:22:08 UTC | #6

I am using gcc 8.2. I followed the instructions on the github 
git clone https://github.com/urho3d/Urho3D
cd Urho3d 
cmake .
make
Doing so there is no -ffmath in Urho3D/CMake/Modules/UrhoCommon.cmake yet 3d does not work as intended. Which files do I modify to change the env-variables to 'clang' and 'clang++' ?

-------------------------

weitjong | 2019-03-22 00:19:48 UTC | #7

That version should be OK. Your steps will generate non out-of-source build tree, but that's fine too and should not cause this issue. But I am out of idea what wrong with you build environment. BTW, I am using GCC 8.3.1 and cannot reproduce the error.

-------------------------

Modanung | 2019-03-22 06:46:50 UTC | #8

*Seemingly* identical glitches earlier this year:

https://discourse.urho3d.io/t/incorrect-camera-transforms-1-7-1-example-projects/5016

https://discourse.urho3d.io/t/problems-with-3d-samples-on-win10/4894

-------------------------

weitjong | 2019-03-23 02:31:23 UTC | #9

[quote="wllo10, post:6, topic:5045"]
Which files do I modify to change the env-variables to ‘clang’ and ‘clang++’ ?
[/quote]

You don't modify any source files in this case. The "environment variable" refers to variable that you set at the host environment level. You may have come across with "PATH" environment variable before, right? The "CC" and "CXX" are the same thing. I purposely being vague on how to export those because different host/shell have different way of doing that. Google is your best friend. Usually for bash shell user, it is as simple as "export CC=clang CXX=clang++".

-------------------------

wllo10 | 2019-03-23 09:45:46 UTC | #10

Thanks for the help it worked only had to set 
elseif (CMAKE_CXX_COMPILER_ID MATCHES Clang)
	set (CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -std=c++11 -Wno-argument-outside-range")
in Urhocommon to successfully compile with clang. Now everything works fine.

-------------------------

weitjong | 2019-03-23 11:15:24 UTC | #11

Now I think I understand why you guys need the extra flag. I am still using Clang 6.0 and so does our CI. Clang 7.0 introduces a new diagnostic check and break the Bullet build.

https://github.com/bulletphysics/bullet3/issues/2114

-------------------------

wllo10 | 2019-03-23 14:24:12 UTC | #12

Kinda funny now opening the Editor doesn't work. Maybe I shouldn't run make install? It seemed fine before. Console output is 
> [Sat Mar 23 15:19:36 2019] INFO: Opened log file /home/pex/.local/share/urho3d/logs/Editor.as.log
> [Sat Mar 23 15:19:36 2019] INFO: Created 1 worker thread
> [Sat Mar 23 15:19:36 2019] INFO: Added resource path /usr/local/bin/../share/Urho3D/Resources/Data/
> [Sat Mar 23 15:19:36 2019] INFO: Added resource path /usr/local/bin/../share/Urho3D/Resources/CoreData/
> [Sat Mar 23 15:19:36 2019] INFO: Added resource path /usr/local/bin/../share/Urho3D/Resources/Autoload/LargeDat
> a/
> [Sat Mar 23 15:19:36 2019] INFO: Adapter used Intel Open Source Technology Center Mesa DRI Intel(R) HD Graphics
> 520 (Skylake GT2) &#160;
> [Sat Mar 23 15:19:36 2019] INFO: Set screen mode 1024x768 windowed monitor 0 resizable
> [Sat Mar 23 15:19:36 2019] INFO: Initialized input
> [Sat Mar 23 15:19:36 2019] INFO: Initialized user interface
> [Sat Mar 23 15:19:36 2019] INFO: Initialized renderer
> [Sat Mar 23 15:19:36 2019] INFO: Set audio mode 44100 Hz stereo interpolated
> [Sat Mar 23 15:19:36 2019] INFO: Initialized engine
> [Sat Mar 23 15:19:36 2019] INFO: Scripts/Editor/EditorTerrain.as:484,5 Compiling void TerrainEditor::UpdateTerr
> ainRaiseLower(Image@, IntVector2, TerrainEditorUpdateChanges@)
> [Sat Mar 23 15:19:36 2019] WARNING: Scripts/Editor/EditorTerrain.as:503,27 Signed/Unsigned mismatch
> [Sat Mar 23 15:19:36 2019] WARNING: Scripts/Editor/EditorTerrain.as:505,31 Signed/Unsigned mismatch
> [Sat Mar 23 15:19:36 2019] INFO: Scripts/Editor/EditorTerrain.as:526,5 Compiling void TerrainEditor::UpdateTerr
> ainSmooth(Image@, IntVector2, TerrainEditorUpdateChanges@)
> [Sat Mar 23 15:19:36 2019] WARNING: Scripts/Editor/EditorTerrain.as:541,27 Signed/Unsigned mismatch
> [Sat Mar 23 15:19:36 2019] WARNING: Scripts/Editor/EditorTerrain.as:543,31 Signed/Unsigned mismatch
> [Sat Mar 23 15:19:36 2019] INFO: Scripts/Editor/EditorTerrain.as:588,5 Compiling void TerrainEditor::UpdateTerr
> ainSetHeight(Image@, IntVector2, TerrainEditorUpdateChanges@)
> [Sat Mar 23 15:19:36 2019] WARNING: Scripts/Editor/EditorTerrain.as:605,27 Signed/Unsigned mismatch
> [Sat Mar 23 15:19:36 2019] WARNING: Scripts/Editor/EditorTerrain.as:607,31 Signed/Unsigned mismatch
> [Sat Mar 23 15:19:36 2019] INFO: Scripts/Editor/EditorScene.as:1131,1 Compiling uint SceneFindChildIndex(Node@,
> Node@)
> [Sat Mar 23 15:19:36 2019] WARNING: Scripts/Editor/EditorScene.as:1139,12 Implicit conversion changed sign of v
> alue
> [Sat Mar 23 15:19:36 2019] INFO: Scripts/Editor/EditorScene.as:1142,1 Compiling uint SceneFindComponentIndex(No
> de@, Component@)
> [Sat Mar 23 15:19:36 2019] WARNING: Scripts/Editor/EditorScene.as:1150,12 Implicit conversion changed sign of v
> alue
> [Sat Mar 23 15:19:37 2019] INFO: Scripts/Editor/EditorViewSelectableOrigins.as:91,1 Compiling void UpdateOrigin
> s()
> [Sat Mar 23 15:19:37 2019] WARNING: Scripts/Editor/EditorViewSelectableOrigins.as:98,59 Signed/Unsigned mismatc
> h
> [Sat Mar 23 15:19:37 2019] WARNING: Scripts/Editor/EditorViewSelectableOrigins.as:133,37 Signed/Unsigned mismat
> ch
> [Sat Mar 23 15:19:37 2019] WARNING: Scripts/Editor/EditorViewSelectableOrigins.as:160,33 Signed/Unsigned mismat
> ch
> [Sat Mar 23 15:19:37 2019] WARNING: Scripts/Editor/EditorViewSelectableOrigins.as:193,51 Signed/Unsigned mismat
> ch
> [Sat Mar 23 15:19:37 2019] INFO: Scripts/Editor/EditorViewSelectableOrigins.as:204,1 Compiling bool isThisNodeO
> neOfSelected(Node@)
> [Sat Mar 23 15:19:37 2019] WARNING: Scripts/Editor/EditorViewSelectableOrigins.as:208,23 Signed/Unsigned mismat
> ch
> [Sat Mar 23 15:19:37 2019] INFO: Scripts/Editor/EditorViewSelectableOrigins.as:217,1 Compiling void ShowSelecte
> dNodeOrigin(Node@, int)
> [Sat Mar 23 15:19:37 2019] WARNING: Scripts/Editor/EditorViewSelectableOrigins.as:236,28 Signed/Unsigned mismat
> ch
> [Sat Mar 23 15:19:37 2019] INFO: Scripts/Editor/EditorViewSelectableOrigins.as:254,1 Compiling void CreateOrigi
> n(int, bool = false)
> [Sat Mar 23 15:19:37 2019] WARNING: Scripts/Editor/EditorViewSelectableOrigins.as:256,29 Signed/Unsigned mismat
> ch
> [Sat Mar 23 15:19:37 2019] INFO: Scripts/Editor/EditorViewSelectableOrigins.as:284,1 Compiling void MoveOrigin(
> int, bool = false)
> [Sat Mar 23 15:19:37 2019] WARNING: Scripts/Editor/EditorViewSelectableOrigins.as:286,29 Signed/Unsigned mismat
> ch
> [Sat Mar 23 15:19:37 2019] INFO: Scripts/Editor/EditorViewSelectableOrigins.as:329,1 Compiling bool IsSceneOrig
> in(UIElement@)
> [Sat Mar 23 15:19:37 2019] WARNING: Scripts/Editor/EditorViewSelectableOrigins.as:333,21 Signed/Unsigned mismat
> ch
> [Sat Mar 23 15:19:37 2019] INFO: Scripts/Editor/EditorViewSelectableOrigins.as:371,1 Compiling String NodeInfo(
> Node&amp;inout, int)
> [Sat Mar 23 15:19:37 2019] WARNING: Scripts/Editor/EditorViewSelectableOrigins.as:385,27 Signed/Unsigned mismat
> ch
> [Sat Mar 23 15:19:37 2019] INFO: Scripts/Editor/EditorViewPaintSelection.as:46,1 Compiling void UpdatePaintSele
> ction()
> [Sat Mar 23 15:19:37 2019] WARNING: Scripts/Editor/EditorViewPaintSelection.as:53,67 Signed/Unsigned mismatch
> [Sat Mar 23 15:19:37 2019] WARNING: Scripts/Editor/EditorViewPaintSelection.as:74,110 Float value truncated in
> implicit conversion to integer
> [Sat Mar 23 15:19:37 2019] WARNING: Scripts/Editor/EditorViewPaintSelection.as:74,60 Float value truncated in i
> mplicit conversion to integer
> [Sat Mar 23 15:19:37 2019] INFO: Scripts/Editor/EditorViewPaintSelection.as:118,1 Compiling void SelectOriginsB
> yPaintSelection(IntVector2, float, bool = true)
> [Sat Mar 23 15:19:37 2019] WARNING: Scripts/Editor/EditorViewPaintSelection.as:122,21 Signed/Unsigned mismatch
> [Sat Mar 23 15:19:37 2019] INFO: Compiled script module Scripts/Editor.as
> [Sat Mar 23 15:19:37 2019] WARNING: Localization::Get("Import animation...") not found translation, language="e
> n"
> [Sat Mar 23 15:19:37 2019] WARNING: Localization::Get("Inverse Kinematics") not found translation, language="en
> "
> [Sat Mar 23 15:19:37 2019] WARNING: Localization::Get("Resource browser") not found translation, language="en"
> [Sat Mar 23 15:19:37 2019] WARNING: Localization::Get("Terrain editor") not found translation, language="en"
> [Sat Mar 23 15:19:37 2019] WARNING: Localization::Get("ShowOrigin") not found translation, language="en"
> [Sat Mar 23 15:19:37 2019] WARNING: Localization::Get("Replicated Node") not found translation, language="en"
> [Sat Mar 23 15:19:37 2019] WARNING: Localization::Get("Local Node") not found translation, language="en"
> [Sat Mar 23 15:19:37 2019] WARNING: Localization::Get("RibbonTrail") not found translation, language="en"
> [Sat Mar 23 15:19:37 2019] WARNING: Localization::Get("Shader compile defines") not found translation, language
> ="en"
> [Sat Mar 23 15:19:37 2019] WARNING: Localization::Get("Shader compile defines") not found translation, language
> ="en"
> /usr/local/bin/Editor.sh: line 3: 14914 Segmentation fault &#160;&#160;&#160;&#160;&#160;(core dumped) $(dirname $0)/Urho3DPlayer Script
> s/Editor.as $OPT1 $@

-------------------------

