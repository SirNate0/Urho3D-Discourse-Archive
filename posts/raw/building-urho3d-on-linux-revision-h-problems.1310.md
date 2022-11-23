tty6 | 2017-01-02 01:06:44 UTC | #1

Hello everyone.
I have met Urho3d review in web and decided to try it  :wink: 
I am on Ubuntu 14.04 amd64,
cloned source tree from github 
gcc 4.8.4
run cmake with keys 
[code]
./cmake_generic.sh ~/urho3d/build/ CMAKE_INSTALL_PREFIX=~/urho3d/inst/  -DURHO3D_STATIC_RUNTIME=ON -URHO3D_SAMPLES=ON -URHO3D_LUA=ON -URHO3D_C++11=ON
[/code]
after that :
[code]
cd ~/urho3d/build
make 
[/code]
and output is
[code]
[ 52%] Building CXX object Source/Urho3D/CMakeFiles/Urho3D.dir/Revision.cpp.o
/home/sergboec/urho3d/src/Urho3D/Source/Urho3D/Revision.cpp: In function ?const char* Urho3D::GetRevision()?:
/home/sergboec/urho3d/src/Urho3D/Source/Urho3D/Revision.cpp:33:12: error: ?revision? was not declared in this scope
     return revision;
            ^
[/code]
I really can't understand where revision declared  :smiley:

-------------------------

rasteron | 2017-01-02 01:06:44 UTC | #2

Hello tty6 and welcome :slight_smile:

If you're just new to Urho3D, I suggest you use CMake without any flags first and run it default. This way you might encounter some bugs to report or simply just a misconfiguration during your setup process.

You can also try building in the source path as it works all the time.

-------------------------

weitjong | 2017-01-02 01:06:45 UTC | #3

I was not able to reproduce your problem, even when I replicate all your commands including those mistakes that you made. Still I am able to build the library successfully in the ~/urho3d/build. The error in your output suggests that a supposedly auto-generated header named "librevision.h" was somehow missing in your build directory. This file should be in ~/urho3d/build/Source/Urho3D/ directory in your case. However, in my test, this file always gets regenerated even after I deliberately delete it.

I agree with what rasteron said. Try not to use any build options first to test the water. Then customize the build by using those options when you have a working build environment. About the mistakes I mentioned earlier, all the build options must be prefixed by "-D". This is how CMake works. e.g. -DURHO3D_SAMPLES=ON. Another minor mistake was turning on the URHO3D_STATIC_RUNTIME option on Linux build. As per our documentation, this option is only applicable for Visual Studio, so it just got ignored by our build system on Linux. Also, there is no need for you to explicitly turn on the URHO3D_C++11 option, at least for now. Urho3D library code base does not not rely on any C++11 standard (yet). The C++11 standard is only required by one of the 3rd party library (nanodbc) when database subsystem is enabled for the build, so it gets turn on implicitly only when it is needed. You  get more compiler warnings with the C++11 standard turn on, but get no extra benefit in return (well, aside from enabling the compilation of nanodbc).

Our build system supports both out-of-source (recommended) and non out-of-source build. Both work all the time.  :wink:

-------------------------

tty6 | 2017-01-02 01:06:45 UTC | #4

[quote="weitjong"]I was not able to reproduce your problem, even when I replicate all your commands including those mistakes that you made. Still I am able to build the library successfully in the ~/urho3d/build. The error in your output suggests that a supposedly auto-generated header named "librevision.h" was somehow missing in your build directory. This file should be in ~/urho3d/build/Source/Urho3D/ directory in your case. However, in my test, this file always gets regenerated even after I deliberately delete it.

I agree with what rasteron said. Try not to use any build options first to test the water. Then customize the build by using those options when you have a working build environment. About the mistakes I mentioned earlier, all the build options must be prefixed by "-D". This is how CMake works. e.g. -DURHO3D_SAMPLES=ON. Another minor mistake was turning on the URHO3D_STATIC_RUNTIME option on Linux build. As per our documentation, this option is only applicable for Visual Studio, so it just got ignored by our build system on Linux. Also, there is no need for you to explicitly turn on the URHO3D_C++11 option, at least for now. Urho3D library code base does not not rely on any C++11 standard (yet). The C++11 standard is only required by one of the 3rd party library (nanodbc) when database subsystem is enabled for the build, so it gets turn on implicitly only when it is needed. You  get more compiler warnings with the C++11 standard turn on, but get no extra benefit in return (well, aside from enabling the compilation of nanodbc).

Our build system supports both out-of-source (recommended) and non out-of-source build. Both work all the time.  :wink:[/quote]

Thank you for your explanation :slight_smile:
Successfully assembled Urho3d

-------------------------

