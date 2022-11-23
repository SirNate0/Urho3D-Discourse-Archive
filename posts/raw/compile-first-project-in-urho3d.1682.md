ook | 2017-01-02 01:09:28 UTC | #1

I have run make && make install to create a new Urho3D project successfully. However, I cannot make the project compile the new Main.cpp file that I added into the root of the new project directory. The Main.cpp file contains the code I obtained from (http://)urho3d.wikia.com/wiki/First_Project. I ran cmake, make && make install again but there was no Main.sh generated in the bin folder. 

I am using Urho3D 1.5 on Linux with Eclipse IDE. The samples run fine but I don't know the way on how to create my own executable file in the project.

Please help.

-------------------------

jmiller | 2017-01-02 01:09:28 UTC | #2

Hi,
General documentation on creating a project using Urho3D 1.5
[urho3d.github.io/documentation/1 ... brary.html](http://urho3d.github.io/documentation/1.5/_using_library.html)

Maybe there is something missing around your CMake stage.. Are there any CMake/make errors? More specific info could help.

Is your makefile not referencing your source files at all? In your CMakeLists.txt, the default define_source_files() macro will glob for *.cpp *.h I think, but it is flexible, e.g.
define_source_files(RECURSE GLOB_CPP_PATTERNS "src/*.cpp" "src/*.cc" GLOB_H_PATTERNS "src/*.h")

-------------------------

ook | 2017-01-02 01:09:28 UTC | #3

Hello

Thank you for your help. I did know that I was trying to use Urho3D as external library so I didn't read that page at all.

Thank you. It should work fine now.

-------------------------

