rogerdv | 2017-01-02 01:03:17 UTC | #1

I have found a problem when testing my application in another PC: Im getting an error that it is not a valid win32 application. I tried to recompile Urho and the application, forcing URHO_64BIT=0, but the error persist. The same exe file runs perfectly in the PC where I compile it: Windows 7 64 bits, Visual Studio Express 2012.
Any idea about whats failing here?

-------------------------

thebluefish | 2017-01-02 01:03:17 UTC | #2

Did you install the C++ runtimes on the target PC? You can download the redistributables here: [microsoft.com/en-us/download ... x?id=30679](http://www.microsoft.com/en-us/download/details.aspx?id=30679)

-------------------------

cadaver | 2017-01-02 01:03:17 UTC | #3

Alternatively, if you don't use Urho3D as a DLL you can use the CMake option -DURHO3D_STATIC_RUNTIME=1 to avoid depending on the runtime DLL and link it statically to your exe instead. You'll need to use that option both in your Urho build, and your application.

-------------------------

rogerdv | 2017-01-02 01:03:18 UTC | #4

Tried both solutions, same problem.

-------------------------

OvermindDL1 | 2017-01-02 01:03:18 UTC | #5

[quote="rogerdv"]Tried both solutions, same problem.[/quote]
List the library filenames that the application links with.  You can do this in a variety of ways from the Visual Studio commandline tool to DependencyWalker that you can download free.

-------------------------

