janstk | 2017-01-02 00:59:44 UTC | #1

rt

-------------------------

jmiller | 2017-01-02 00:59:47 UTC | #2

Hello,
I think Urho3D is like an SDK? Not hard for users to build. But you could... to go with your generator?  :sunglasses: 
[urho3d.github.io/documentation/a00001.html](http://urho3d.github.io/documentation/a00001.html)

Important files? I have only built from source, but some first thoughts:

Bin
Build/Engine/Urho3d.h
Docs/html, Docs/AngelScriptAPI.h
Lib (containing debug and release libs)
Source
.txt files
SourceAssets ?
.bat and .sh?

-------------------------

weitjong | 2017-01-02 00:59:49 UTC | #3

You build the Urho3D library (and its tools and optionally its samples) from source code by cloning the source code from GitHub or by downloading the source package from SourceForge. Either ways you will end up with the same project structure containing all the required project structures and files. Then follow the Readme.txt or [urho3d.github.io/documentation/a00001.html](http://urho3d.github.io/documentation/a00001.html) to configure and generate a suitable Urho3D project file for your targeted platform. Open the generated project file in the corresponding IDE to build the "ALL_BUILD" built-in target (which is the default target). To install the build artifacts (library and its dependency header files) locally, build one more time using "INSTALL" built-in target. It is equivalent to "configure; make; make install" on Unix world. It could not be simpler than that :slight_smile:.

-------------------------

