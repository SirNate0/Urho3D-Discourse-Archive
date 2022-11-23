msim | 2017-01-02 01:13:48 UTC | #1

Hi,

I was following this tutorial:
[youtube.com/watch?v=yImFcDZ61Lk](https://www.youtube.com/watch?v=yImFcDZ61Lk)

And encountered the following problem, which differs from the one in the video:
[postimg.org/image/88gob4mun/](https://postimg.org/image/88gob4mun/)

* I tried different generators.

Please help me ! :slight_smile:

-------------------------

rbnpontes | 2017-01-02 01:13:48 UTC | #2

You need to set these vars in cmake
Example: 
URHO_HOME= director of urho
You need set manual values and hit Generate
Sorry for english, my english is not good

-------------------------

jmiller | 2017-01-02 01:13:48 UTC | #3

Noting the "Use URHO3D_HOME environment variable or build option to specify the location of the non-default SDK installation or build tree."..
What is visible of your setting seems to point incorrectly to [...]CMake/Modules. It should be set to your Urho3D build tree/directory.

And (just in case) don't forget the official docs, as it is easy to miss something, and the build system sees some frequent changes. Let us know how it goes...
[urho3d.github.io/documentation/ ... brary.html](https://urho3d.github.io/documentation/HEAD/_using_library.html)

-------------------------

1vanK | 2017-01-02 01:13:48 UTC | #4

Add to CMakeLists.txt
[code]
set (ENV{URHO3D_HOME} d:/path/to/compiled/version/of/engine)
[/code]

example: [github.com/1vanK/PuddleSimulato ... eLists.txt](https://github.com/1vanK/PuddleSimulator/blob/master/GameSrc/CMakeLists.txt)

-------------------------

