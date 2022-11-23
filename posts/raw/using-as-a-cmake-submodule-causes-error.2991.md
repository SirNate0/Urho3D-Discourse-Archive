emersont1 | 2017-04-07 14:02:32 UTC | #1

Hello, I am trying to use Urho3D through an add_subdirectory command, yet the CMake gives me the error:  

     CMake Error at Urho3D/CMake/Modules/FindUrho3D.cmake:344 (message):
      Could NOT find compatible Urho3D library in Urho3D SDK installation or
      build tree.  Use URHO3D_HOME environment variable or build option to
      specify the location of the non-default SDK installation or build tree.
    Call Stack (most recent call first):
      Urho3D/CMake/Modules/UrhoCommon.cmake:200 (find_package)
      Urho3D/CMakeLists.txt:43 (include)

The master branch is located at `<ROOT>/Urho3D` and the listing for the CMakeLists in the root is as follows
```
cmake_minimum_required(VERSION 3.2)
set (CMAKE_MODULE_PATH ${CMAKE_MODULE_PATH} ${CMAKE_CURRENT_SOURCE_DIR}/CMake/Modules)
set(URHO3D_HOME ${CMKAE_BINARY_DIR})
add_subdirectory(Urho3D)
```
I have also changed line 40 in `ROOT/Urho3D/CMakeLists.txt` to 
```
set (CMAKE_MODULE_PATH ${CMAKE_MODULE_PATH} ${CMAKE_CURRENT_SOURCE_DIR}/CMake/Modules)
# from 
set (CMAKE_MODULE_PATH ${CMAKE_SOURCE_DIR}/CMake/Modules)
```
I've tried with various different values for `URHO3D_HOME`, including `ROOT/Urho3D` and `BINARY_DIR/Urho3D` 
This is probably a really simple fix, so any help would be greatly appreciated

-------------------------

jmiller | 2017-04-07 17:40:27 UTC | #2

[quote="emersont1, post:1, topic:2991"]
set(URHO3D_HOME ${CMKAE_BINARY_DIR})
[/quote]

I'm sure you meant [b]CMAKE_BINARY_DIR[/b], which for me points to the build tree.

Just some related discussion
  http://discourse.urho3d.io/t/embedding-the-engine-as-a-submodule-and-cmake-module/1636

-------------------------

