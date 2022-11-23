tomarlo4 | 2018-08-13 21:41:12 UTC | #1

I was using angelscript but, im interested to use the source now
i already tried to do all, reading wiki and seeing youtube videos, and in the cmake i just get compile error and "red" lines

I got CMAKe (3.8.1), Mingw64 (8.1.0), Urho3D 1.7 and Codeblocks (last) (mingw separated, cause i use mingw64 to others sources)

it would be nice for someone to do a new tutorial demonstrating, at least in a virtual machine, what progress to download and install dependencies for urho3d and compiling at the end, not just compiling

im using windows. thx for read guys

-------------------------

S.L.C | 2018-08-13 20:55:02 UTC | #2

There are no dependencies to download. Everything is next to the engine source in the third party folder. All you need to do is to download mingw ([32](https://sourceforge.net/projects/mingw-w64/files/Toolchains%20targetting%20Win32/Personal%20Builds/mingw-builds/)/[64](https://sourceforge.net/projects/mingw-w64/files/Toolchains%20targetting%20Win64/Personal%20Builds/mingw-builds/)) and extract it to a folder. After that, add the `bin` folder to your `Path` environment variable so that CMake can find MinGW. Then simply use CMake to generate either a CodeBlocks project or a simple make script if you don't need the IDE. And if you go with the later, all you need is to type `mingw32-make` into a terminal in the folder where you generated the build. And wait for it to compile. And that's it.

Normally I'd also install [Git](https://git-scm.com/) and use the terminal from that. But whatever works for you.

Urho is one of the simplest engines to compile. You should've tried Ogre back in the days.

-------------------------

tomarlo4 | 2018-08-13 21:40:51 UTC | #3

Oh, thx!
But idk why... my cmake cache was looking different from now
Maybe cause today i downgrade my mingw64 to 5.3.0-posix-seh and i get urho 1.32 (to 3d performance low n medium)? idk

Now was asking just for CMAKE_MINGW_MAKE and CMAKE_SH
So...
Just realized that sh = bash and just install cygwin64 with bash
Put Urho3D_HOME in environment like in the wiki and cygwin64 in the PATH
and done...
the "CodeBlocks - MinGW Makefiles" runned smooth :thinking:
Just needed click configure 2 times and to put codeblocks.exe location before "generate" :man_shrugging:

-------------------------

megapunchself | 2018-08-13 23:15:30 UTC | #4

@tomarlo4 i think that the conversation here is a tutorial by itself :upside_down_face:

-------------------------

