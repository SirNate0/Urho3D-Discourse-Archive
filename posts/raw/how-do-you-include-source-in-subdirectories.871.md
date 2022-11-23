practicing01 | 2017-01-02 01:03:40 UTC | #1

So far I've been putting all my code in the same directory as Urho3DPlayer.cpp and running cmake_x.sh will add them to the makefile.  How can I make cmake find code within subfolders?

-------------------------

TikariSakari | 2017-01-02 01:03:40 UTC | #2

This is probably less ideal thing, but what I used is to create project with samples. Then copying one sample I want to modify, and then changing the Sample-folders CMakeList.txt by adding a new subdirectory to the new project I am using. After thinking this a bit, I guess it would make more sense to actually modify the cmakelist.txt that is inside source-folder and add subdirectory in there.

-------------------------

jmiller | 2017-01-02 01:03:41 UTC | #3

You can set SOURCE_FILES in your CMakeLists.txt:

[code]file (GLOB CPP_FILES src/*.cpp src/*.cc)
file (GLOB H_FILES src/*.h)
set (SOURCE_FILES ${CPP_FILES} ${H_FILES})[/code]

-------------------------

weitjong | 2017-01-02 01:03:42 UTC | #4

You can pass the glob patterns directly to the define_source_files() macro too. Using carnalis's example, you can write:
[code]define_source_files (GLOB_CPP_PATTERNS src/*.cpp src/*.cc GLOB_H_PATTERNS src/*.h)[/code]

-------------------------

TikariSakari | 2017-01-02 01:03:43 UTC | #5

[quote="weitjong"]You can pass the glob patterns directly to the define_source_files() macro too. Using carnalis's example, you can write:
[code]define_source_files (GLOB_CPP_PATTERNS src/*.cpp src/*.cc GLOB_H_PATTERNS src/*.h)[/code][/quote]

Seems that this works, but If I use this, is there a way to define the different folders into a filter for visual studio? Now when/if I have to change the cmakefile, like add more to the structure, then when the visual studio updates the project, it completely wipes the filter structure that I have set up. So every file is just either in source or header-filter. Like lets say I have
[code]
States/GameStateManager.cpp & h
States/BaseState.cpp & h
TheGame.cpp & h
[/code]

After it reloads the cmakelists.txt in visual studio it looks as:
[code]
Header Files:
  GameStateManager.cpp
  BaseState.cpp
  TheGame.cpp

Source Files:
  GameStateManager.h
  BaseState.h
  TheGame.h
[/code]

So the structure is completely gone that I set up as in the files. Is there some "easy" way to define it, so that for example files in States-folder are inside filter called states in visual studio automatically after the cmakelists.txt has been reloaded by visual studio?

-------------------------

weitjong | 2017-01-02 01:03:43 UTC | #6

If I understand you correctly then you want the "grouping". The answer is yes and no. If you have physically structured your source files into sub-dirs then yes, you can pass the 'GROUP' option to the macro to tell it to group the source files based on the sub-dirs relative path to the parent directory. If, however, your source files are just located in a single directory, say src/, then you will have to create the group manually by calling CMake's source_group() command. HTH.

-------------------------

TikariSakari | 2017-01-02 01:03:43 UTC | #7

Thanks, yup i have folder structure on my project. Using the sample.h kind of explodes to show whole folder structure from f:/.... instead of ../sample.h, but that is fine, since I should anyways at some point make my own base application file anyways.

This really helps me, and hopefully other as clueless people as me. The make files are just, well something I hope I do not have a lot to deal with in the future.
[code]
# Define source files
define_source_files (EXTRA_H_FILES ${COMMON_SAMPLE_H_FILES} 
	GLOB_CPP_PATTERNS *.cpp src/*.cpp ui/*.cpp states/*.cpp src/*.cpp 
	GLOB_H_PATTERNS *.h src/*.h ui/*.h states/*.h GROUP )
[/code]

Browsing the makefiles from urho3d-folder for how to use the GROUP option, I found even better one for me:
[code]
# Define source files
define_source_files (EXTRA_H_FILES ${COMMON_SAMPLE_H_FILES} 
	GLOB_CPP_PATTERNS *.c* 
	GLOB_H_PATTERNS *.h* RECURSE GROUP )
[/code]
As long as I keep just source codes under the main folder, this will recursively add all c-type files and h-type files in their respective folders inside visual studio.

-------------------------

weitjong | 2017-01-02 01:03:44 UTC | #8

The RECURSE option is relatively new. Glad you find it useful. You may also want to know that the recurse option works on the list of glob patterns you provide, so it does not limit your project to have all the source files in just one main folder.

-------------------------

