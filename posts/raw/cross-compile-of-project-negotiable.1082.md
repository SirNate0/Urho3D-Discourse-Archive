practicing01 | 2017-01-02 01:05:17 UTC | #1

Hello, one of my old projects was greenlit and I need it compiled on windows (I'm on linux and really don't want to deal with windows).  On linux, I've gone the route of using urho as a library, not sure if that'll work on other linux computers.  If not, I would need that too. 

Steam page: [steamcommunity.com/sharedfiles/f ... =119805935](http://steamcommunity.com/sharedfiles/filedetails/?id=119805935)
Source: [github.com/practicing01/Bitweb](https://github.com/practicing01/Bitweb)

-------------------------

alexrass | 2017-01-02 01:05:20 UTC | #2

Use cross compiler (mingw-w64)

-------------------------

thebluefish | 2017-01-02 01:05:20 UTC | #3

Send me details via PM and I can do it.

-------------------------

practicing01 | 2017-01-02 01:05:26 UTC | #4

On linux, I raked urho as documented here: [urho3d.github.io/documentation/H ... caffolding](http://urho3d.github.io/documentation/HEAD/_using_library.html#Scaffolding)  I bet it works the same way on windows.  I just need an executable.  Anybody willing to help?  I'm willing to negotiate for the exe.

-------------------------

weitjong | 2017-01-02 01:05:26 UTC | #5

I thought this is a platform porting issue instead of project scaffolding issue. If you already have a working set of CMakeLists.txt files with your project source files on Linux then there is no need to call "scaffolding" task again on other target platforms. CMake itself and Urho3D library (with all its CMake modules and toolchains) are portable. So, the only thing you have to worry about is, how portable your own custom CMakeLists.txt and your own source code are.

-------------------------

thebluefish | 2017-01-02 01:05:26 UTC | #6

Mang PM me the deets. I have you covered.

-------------------------

