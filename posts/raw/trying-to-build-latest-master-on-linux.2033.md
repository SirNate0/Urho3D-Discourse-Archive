namic | 2017-01-02 01:12:26 UTC | #1

[code]
git clone git@github.com:urho3d/Urho3D.git
cd Urho3D
mkdir build
cd build
cmake .. -DURHO3D_SAMPLES=1 -DURHO3D_C++11=1 

CMake Error at Source/ThirdParty/SDL/cmake/macros.cmake:73 (message):
  *** ERROR: Missing Xext.h, maybe you need to install the libxext-dev
  package?
Call Stack (most recent call first):
  Source/ThirdParty/SDL/cmake/sdlchecks.cmake:380 (message_error)
  Source/ThirdParty/SDL/CMakeLists.txt:923 (CheckX11)
[/code]

I have installed all the libraries mentioned in the docs: libx11-dev libxrandr-dev libasound2-dev and libxext-dev. The header file exists on my machine at /usr/include/X11/extensions/Xext.h. Maybe it's a problem with FindSDL.cmake?

-------------------------

rasteron | 2017-01-02 01:12:26 UTC | #2

[quote]cmake .. -DURHO3D_SAMPLES=1 -DURHO3D_C++11=1 [/quote]

IF you're not familiar with cmake and urho3d's build setup, it's always recommended to use the provided terminal or batch scripts. [b]Weitjong[/b] maintains and updates them regularly for a reason. :wink:

[github.com/urho3d/Urho3D/blob/m ... generic.sh](https://github.com/urho3d/Urho3D/blob/master/cmake_generic.sh)

Usage: cmake_generic.bat \path\to\build-tree [build-options]

Just cloned moments ago and generated with the same flags and without any issues.. (Ubuntu 14.04 LTS 32bit)

[img]http://i.imgur.com/rfjqI3pl.jpg[/img]

-------------------------

