ppsychrite | 2017-05-24 12:11:29 UTC | #1

Hello!
I've recently built Urho3D from source with the linux tutorial and made it external using this tutorial 
https://urho3d.github.io/documentation/HEAD/_using_library.html
Building Urho3D has worked fine but when I build my project using "cmake ." it gives me this error `"CMake Error: Could not find cmake module file: CMakeDetermineHillCompiler.cmake
CMake Error: Error required internal CMake variable not set, cmake may not be built correctly.
Missing variable is:
CMAKE_Hill_COMPILER_ENV_VAR
CMake Error: Error required internal CMake variable not set, cmake may not be built correctly.
Missing variable is:
CMAKE_Hill_COMPILER
CMake Error: Could not find cmake module file: /home/ppsychrite/Desktop/Project/CMakeFiles/3.8.1/CMakeHillCompiler.cmake
CMake Error at CMakeLists.txt:2 (project):
  No CMAKE_Hill_COMPILER could be found.

  Tell CMake where to find the compiler by setting the CMake cache entry
  CMAKE_Hill_COMPILER to the full path to the compiler, or to the compiler
  name if it is in the PATH.


CMake Error: Could not find cmake module file: CMakeHillInformation.cmake
CMake Error: CMAKE_Hill_COMPILER not set, after EnableLanguage
-- Configuring incomplete, errors occurred!
See also "/home/ppsychrite/Desktop/Project/CMakeFiles/CMakeOutput.log".
See also "/home/ppsychrite/Desktop/Project/CMakeFiles/CMakeError.log"."`

I also tried the prebuilt SDK .deb package but when I make a basic application and run it it complains about missing GL/glew.h
Is there something I'm missing? Because I believe I'm following the steps correctly

-------------------------

weitjong | 2017-05-24 14:11:15 UTC | #2

Probably your project does not have the correct structure as expected by our build system. If you want to reuse our build system then you have to scaffold your project similar to Urho3D project. If you are using Linux, the easiest way to do that is by executing "rake scaffolding dir=/path/to/new/project" in a terminal after cd to Urho3D project directory.

-------------------------

ppsychrite | 2017-05-24 21:11:46 UTC | #3

Thank you! That worked. :slight_smile:
I found out that the Urho3D include in /usr/local/ was linking GLEW/glew.h instead of GL/glew.h so I went in there and changed it. Few more thing's like ik/quat.h it's complaining about missing that I can maybe find on my own.

-------------------------

