hsl9999 | 2017-01-02 01:08:23 UTC | #1

Can compile the android version of the APP
Support for c + + 11?
how to modify make?

-------------------------

Sir_Nate | 2017-01-02 01:08:28 UTC | #2

As a guess, I would say try the flag in cmake for allowing Urho to use C++11 (the URHO3D_C++11 option), and if that doesn't work look for the g++ or c++ compiler flags and add -std=c++11 in the Makefile

-------------------------

TikariSakari | 2017-01-02 01:08:28 UTC | #3

I have added my own project folder under the source-folder called myproj. In file Source/myproj/CMakeLists.txt I have added the following line to enable c++11 support on all the projects in myproj-folder.

[code]
#Enable C++11 Support
set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -std=c++11")
[/code]

-------------------------

