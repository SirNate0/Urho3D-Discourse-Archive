mygrandmawheels | 2017-11-14 12:49:29 UTC | #1

Hello, I'm a newby of Urho, it seems very well structured.
While I have no problem compiling a sample project via NetBeans on linux, I can't make the same on Windows 10 via NetBeans + MinGW (I have strange errors with stdlib).

So I would like to try it by Visual Studio Community, 2015/2017.
My first attemps gone wrong, does anyone have an example ready?

Thanks so much!

-------------------------

Miegamicis | 2017-11-14 13:48:12 UTC | #2

I use VS2015 and ussualy do this:
1. Open terminal
2. Go to Urho3D directory
3. Run "cmake_vs2015.bat build"
4. Then go to "build" directory in file explorer and launch Urho3D.sln in VS2015

-------------------------

mygrandmawheels | 2017-11-14 16:44:39 UTC | #3

ok, probably I'm making a little mess.. do I need to add Urho3D to my path?
I'm using this version:
Urho3D-1.7-Windows-64bit-STATIC-3D11
and the cmake_vs2015.bat is on the subpath .\share\Scripts

so I have  this:

C:\Urho3D-1.7-Windows-64bit-STATIC-3D11>.\share\Scripts\cmake_vs2015.bat build
CMake Error: The source directory "C:/Urho3D-1.7-Windows-64bit-STATIC-3D11/share/Scripts" does not appear to contain CMakeLists.txt.
Specify --help for usage, or press the help button on the CMake GUI.


Many thanks for your help!

-------------------------

weitjong | 2017-11-15 01:38:27 UTC | #4

If you want to build from source (recommended) then you should clone the release tag from GitHub or download the source package from SF.net (instead of prebuilt binary package).

-------------------------

mygrandmawheels | 2017-11-15 08:53:23 UTC | #5

So the hint given by Miegamicis is referred to the github cloned directory; Obviously, I'll have to build the Urho.. Ok, many thanks for now!

-------------------------

mygrandmawheels | 2017-11-16 10:32:50 UTC | #6

I did it the first time, in the end it was really trivial.. :blush:
I've lost myself with downloading the binary files from the site, which in the end do not understand what their use is.. 
anyway: thanks to everyone, Urho3d rocks!!! :sunglasses::grinning:

-------------------------

