Sean221 | 2018-02-27 01:13:48 UTC | #1

Ok so i didnt word this post right the first time so i'll give it another go!

Essentially can anyone tell me what process they go through to compile a project using CMake and Visual Studio 2015?

I currently use CMakes GUI and every time I recompile I have to manually set URHO3D_HOME. So I was wondering if there is a way to automate having to manually set this?

-------------------------

weitjong | 2018-02-26 00:19:01 UTC | #2

Not sure what you are looking for, FWIW check our CI script for the Travis or Appveyor. The scripts prepare the VM from scratch till it becomes suitable build environment for Urho3D project and it’s downstream.

-------------------------

Sean221 | 2018-02-27 01:15:02 UTC | #3

I've reworded my post to hopefully make it clearer

-------------------------

Pencheff | 2018-02-27 09:40:25 UTC | #4

Many possible ways, for example using Urho3D as external project in CMake
[code]
ExternalProject_Add(urho3d
  GIT_REPOSITORY https://github.com/urho3d/Urho3D.git
  PREFIX urho3d
  UPDATE_COMMAND ""
  PATCH_COMMAND ${PATCHER} urho3d
  CMAKE_ARGS 
    -DCMAKE_INSTALL_PREFIX=${CMAKE_BINARY_DIR} 
    -DCMAKE_BUILD_TYPE=${CMAKE_BUILD_TYPE}
    -DURHO3D_SAMPLES=FALSE
    -DURHO3D_C++11=TRUE
)
[/code]

I personally prefer having my project's dependencies as a separate superproject, I pre-build once and automate my main project to always know where prebuild dependencies are. I don't use any environment variables for my projects, most of the settings are done either in CMake or in shell scripts.

-------------------------

