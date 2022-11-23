Ka-Wiz | 2020-07-10 21:53:10 UTC | #1

Hi there, when I first started my project 3 years ago I didn't know anything about using cmake or doing proper project structure, but I managed to throw together enough to get my client, server, and urho to build and share a resource directory.

Now I am in the position of wanting to do a "Release" client that I can give to people to try out my game, but I don't know how to build it separate from the other parts and have no clue where to start...

Inside my project folder, I have two folders, Source and Builds. In Source there's Client, Server, and Urho folders that have the respective sources, and then I use CMake to generate the project files in Builds/platform/Client||Server||Urho and compile from there, building urho first so that I can specify URHO3D_HOME when I CMake the client and server projects.

So yeah, that's the structure of how I do things now. Can anyone point me in the right direction as to how I put together a "clean" release client for distribution? Thanks!

EDIT: I've tried some simple things like just taking the Client folder out of builds but that breaks everything, and isn't what I'm going for since that still has all the visual studio project files in it and stuff

-------------------------

Ka-Wiz | 2020-07-11 02:45:09 UTC | #2

Okay, after messing around with it a bit I think I can clarify this question:

The client is setup as a downstream project as per "Using Urho3D Library" documentation. I think my main problem is figuring out how to package my built Urho library with the client. Which files do I need to include with the client and how do i tell it to use them? The goal is to have a self-contained game folder that I can zip up and redistribute and have everything work out of the box.

Hope that is less word salad haha

-------------------------

SirNate0 | 2020-07-11 02:50:09 UTC | #3

Are you using a shared or static library build? If it's static you should just need the executable and the reasource directories/packages. If it's shared make sure you include the necessary DLLs as well. Try just zipping `bin` and seeing if that works.

-------------------------

jmiller | 2020-07-11 03:33:06 UTC | #4

If you happen to want to change the binary output directory, a couple examples:

Setting output to source dir, using CMakeLists.txt
`set(CMAKE_RUNTIME_OUTPUT_DIRECTORY ${CMAKE_CURRENT_SOURCE_DIR})`

Or up one directory
`${CMAKE_BINARY_DIR}/..`

Setting output dir of a specific configuration, appended, using cmake command line
 `-D CMAKE_RUNTIME_OUTPUT_DIRECTORY_RELEASE=string:dir`

(searching these terms finds a lot of related info, cmake docs or stackexchange, for example)

-------------------------

Ka-Wiz | 2020-07-11 03:27:42 UTC | #5

@SirNate0 That's what I was trying at first, but the screen would always be black and nothing would happen if the directory was anywhere other than where I built it. I assumed there was some complex build thing I was missing.

I did, however, just try rebuilding the engine with URHO3D_STATIC_RUNTIME set as well (it wasn't before, don't know if that made a difference) and then recompiling client, zipping up bin, sending it to my other computer and it worked!!! Thanks so much!

@jmiller  Thanks for that as well! cmake is really arcane to someone like me who is unfamiliar with big projects like this, so it's a huge help to have some pointers on how to do stuff like that!

-------------------------

