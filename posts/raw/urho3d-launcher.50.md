Hevedy | 2017-01-02 00:57:36 UTC | #1

Hi.
I'm working this week in a launcher for Urho3D, to launch the demos, the editor, configure and other thinks...
Created in C++ with QT, the license of the launcher in MIT and the QT is LGPL but is for internal use(for dev) or for create launcher for games external to the game and engine...

[img]https://github.com/Hgdavidy/Urho3D_Launcher_Tools/raw/master/Urho3D_Launcher.png[/img]

Here the Github: (Work in progress)(Some days to end the base) :wink: 
[url]https://github.com/Hgdavidy/Urho3D_Launcher_Tools[/url]


Thanks.

-------------------------

Hevedy | 2017-01-02 00:57:36 UTC | #2

No replys  :frowning: 
Ok all base is completed, and all work.

Ty.

-------------------------

Mike | 2017-01-02 00:57:36 UTC | #3

Looks really cool, but when executing Urho3D_Launcher.exe I get an error message (...is not a valid Win32 application). Did you compile for 64 bits?

-------------------------

Hevedy | 2017-01-02 00:57:36 UTC | #4

[quote="Mike"]Looks really cool, but when executing Urho3D_Launcher.exe I get an error message (...is not a valid Win32 application). Did you compile for 64 bits?[/quote]

I compiled this for Win32, run for me in x32 and x64.
What windows are you using ? Need copy all .dlls and the folder /platforms with .dlls.

-------------------------

cadaver | 2017-01-02 00:57:36 UTC | #5

This looks nice. One suggestion I would have to not hardcode example names, you could instead scan for filenames that start with pattern xx_ where xx are digits 0-9 (for both script & C++ examples)

-------------------------

Hevedy | 2017-01-02 00:57:36 UTC | #6

[quote="cadaver"]This looks nice. One suggestion I would have to not hardcode example names, you could instead scan for filenames that start with pattern xx_ where xx are digits 0-9 (for both script & C++ examples)[/quote]

Ok thanks. I have to look that when i have time, yes.  :wink: 
The code is open to all, if like make changes or give ideas...

1? Question, how compile the c++ samples ?(Where change and what file for enable samples)
I run the cmake_vs2010.bat, because the 2012 get a error at compile using VSExpress 2012 Desktop, W7.

Thanks.  :smiley:

-------------------------

cadaver | 2017-01-02 00:57:36 UTC | #7

You need to run the CMake bat with the parameter -DENABLE_SAMPLES=1. This and the rest of the CMake options are documented in the "Building Urho3D" section of readme and the documentation (see bottom of [url]http://urho3d.github.io/documentation/a00001.html[/url])

-------------------------

Hevedy | 2017-01-02 00:57:38 UTC | #8

[quote="cadaver"]You need to run the CMake bat with the parameter -DENABLE_SAMPLES=1. This and the rest of the CMake options are documented in the "Building Urho3D" section of readme and the documentation (see bottom of [url]http://urho3d.github.io/documentation/a00001.html[/url])[/quote]

Ok thanks, i going to try.

-------------------------

Hevedy | 2017-01-02 00:58:15 UTC | #9

Here the idea for next pack of launcher and other external tools for Urho 3D/2D:

[img]https://dl.dropboxusercontent.com/u/28070491/URho3D/LauncherB.png[/img]

-------------------------

