niansa | 2021-11-03 11:49:51 UTC | #1

Hey, is there a template `CMakeLists.txt` for Urho3D projects? I am having some trouble getting stuff to work because my CMake skills are miserable.

This is my current file:

```cmake
cmake_minimum_required(VERSION 3.5)

project(phouse LANGUAGES CXX)

set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

add_executable(phouse main.cpp)

target_link_libraries(phouse PRIVATE Urho3D GL)
```
which ofc does not work!

-------------------------

Modanung | 2021-11-03 12:00:34 UTC | #2

> # [:books: Project scaffolding](https://urho3d.io/documentation/HEAD/_using_library.html)

-------------------------

niansa | 2021-11-05 15:33:50 UTC | #3

Oops, I should've RTFM.

-------------------------

