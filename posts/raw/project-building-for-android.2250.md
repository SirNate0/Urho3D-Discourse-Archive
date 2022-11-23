itisscan | 2017-01-02 01:14:15 UTC | #1

My folders organization in project is following - [url]http://imgur.com/a/nTGa8[/url]. In folders are other source code.
I have generated project on android using cmake_android.bat, then i look Makefile in build folder and see that rules are created only for 4 files. (SimulationApplicatin.cpp/.h, and SimulationStd.cpp/.h) , but i need to compile also other files that are located in SimulationLogic, UserInterface and Utility directory.

I see two solutions - copy all source files in one folder and then generate project. In this case, i lose directory organization. The second way create makefile rules manually.

It would be nice, if cmake automatically create makefile rules for another files that sit in subdirs. 
Is it possible ? 
Thanks.

-------------------------

itisscan | 2017-01-02 01:14:33 UTC | #2

I solved my problem.

I manually added some cmake instructions in end of the CMakeLists.txt file, which generates my project. 

[code]include_directories(${CMAKE_SOURCE_DIR})

set(SOURCES 
  SimulationStd.cpp
  ${CMAKE_SOURCE_DIR}/SimulationStd.h

  SimulationApplication.cpp
  ${CMAKE_SOURCE_DIR}/SimulationApplication.h

  SimulationLogic/BaseSimLogic.cpp
  ${CMAKE_SOURCE_DIR}/SimulationLogic/BaseSimLogic.h

  SimulationLogic/LevelManager/LevelManager.cpp
  ${CMAKE_SOURCE_DIR}/SimulationLogic/LevelManager/LevelManager.h

  SimulationLogic/HotAirBalloonLogic/HotAirBalloonLogic.cpp
  ${CMAKE_SOURCE_DIR}/SimulationLogic/HotAirBalloonLogic/HotAirBalloonLogic.h

  Utility/Touch.cpp
  ${CMAKE_SOURCE_DIR}/Utility/Touch.h

  UserInterface/UserInterface.cpp
  ${CMAKE_SOURCE_DIR}/UserInterface/UserInterface.h

  UserInterface/CharacterView/CharacterView.cpp
  ${CMAKE_SOURCE_DIR}/UserInterface/CharacterView/CharacterView.h

  UserInterface/HumanView/HumanView.cpp
  ${CMAKE_SOURCE_DIR}/UserInterface/HumanView/HumanView.h

  UserInterface/ScreenElement/LoadingUI.cpp
  ${CMAKE_SOURCE_DIR}/UserInterface/ScreenElement/LoadingUI.h

  UserInterface/SelectSceneView/SelectSceneView.cpp
  ${CMAKE_SOURCE_DIR}/UserInterface/SelectSceneView/SelectSceneView.h
)
target_sources(Simulation PUBLIC ${SOURCES})
[/code]

As you see, it takes some time to add new instructions in order to generate right rules for makefile, but in the result you keep folders organization.

-------------------------

Sir_Nate | 2017-01-02 01:14:34 UTC | #3

I'm not certain what exactly you want, but you can try doing something like this to get it to work:
[code]# Define source files    try adding RECURSE
define_source_files ( GLOB_CPP_PATTERNS *.cpp ./Overworld/*.cpp ./Characters/*.cpp ./Characters/Editors/*.cpp ./Overworld/SkyX/*.cpp ./Overworld/ProcSky/*.cc ./Overworld/ProcSky/*.cpp ./UI/*.cpp ./Characters/Battle/*.cpp ./toml/*.cpp)
[/code]
Note that each child dircetory with sources would need an entry, but I think with the RECURSE optiion that isn't needed (I can't use it as I have some source files that cannot be built hidden deep within the build directory). You can also try using the ** glob pattern, though I haven't had the best luck with it...

-------------------------

weitjong | 2017-01-02 01:14:36 UTC | #4

[quote="Sir Nate"]Note that each child dircetory with sources would need an entry, but I think with the RECURSE optiion that isn't needed (I can't use it as I have some source files that cannot be built hidden deep within the build directory). You can also try using the ** glob pattern, though I haven't had the best luck with it...[/quote]
The macro is basically just populating a CMake variable (SOURCE_FILES) in a list context. If you cannot work out a glob pattern and/or the recurse option produces undesired result in the list, you can always use a list operation to remove the unwanted items before calling the target setting macros.  :wink:

-------------------------

