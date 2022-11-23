Ka-Wiz | 2017-09-10 14:24:48 UTC | #1

Hi there, I've never used CMake before so I'm a little confused as to how to use the Urho3D build system to make my project cross-platform. I've read "building urho3d library", "using urho3d library", and [Setting up a Project (CMake)](https://github.com/urho3d/Urho3D/wiki/Setting-up-a-Project-(CMake)) several times and this is my understanding of the process:

1. Download Urho3D source, this is the universal package for any platform
2. Run one of the .bat, .sh, or cmake-gui to create a platform- and IDE-specific "build tree"
3. Open VS solution/use make/etc to build engine from the build tree
4. Create own project, use same scripts but specify URHO3D_HOME to use built engine

From my understanding of this, my C++ files would be too far "downstream" to be moved to a different platform easily, since they're in a project that is attached to a platform-specific build. First of all, is that a correct assessment? If so, I feel like a possible solution would be to edit the CMake files of the original Urho source to include my files, so whenever I use CMake to generate a build tree for whatever platform, my files are already in there. However, I don't know if this is the actual "correct" solution, and if it is I don't know enough CMake to know how to do that. Another way that might work would be to manually move my code between pre-built build trees; it seems messy but I'll do it if that's what I gotta do. **Ideally I'd like to have one folder I can move around onto any platform and have the CMake scripts generate the files I need for whatever build system, just like the source does now but with my project included.**

Some minor questions that are less important than my main one and can be ignored: I am also confused about the necessity of "project scaffolding" as described in "using Urho3D library". It seems like CMake already generates all the folders for you - why would you need to create them yourself? Also, what is the difference between Urho3D and Urho3D SDK? Is the term SDK used to mean one of the pre-built things you can download instead of the source?

Thanks for reading, I know I'm a little stupid (I think I confused myself even more in writing this post) and more than likely am missing something obvious, but I've been stuck reading those 3 guides for the past 2 days and I can't wrap my head around it. Any clarification of things I've misunderstood is extremely welcome, and I just wanna say from spending a couple weeks going through the source and playing around editing samples (in Windows and Linux) I am absolutely in love with this engine and want to learn it from the inside out, and hopefully get good enough to contribute!

-------------------------

johnnycable | 2017-09-10 19:13:15 UTC | #2

First of all, try not to tamper with cmake at all. That's the solution of last resort.
If you have your own software/library, you can always include them directly into a project of your own. Simply duplicate an example you think is near and add the code to it.
Of course this requires basic understanding of how c++ building process work. You cannot have st like an universal binary, that is st you can carry around like portable because every system (osx, linux, windows, android...) has a differenti ABI so they're not compatible. You have to build the solution you need for every system.
Start simple. Build the examples for your native platform, tweak one, and so on. First things first.

-------------------------

Ka-Wiz | 2017-09-10 21:41:49 UTC | #3

Thanks for the reply, but I think there was a little confusion. I know that there's no such thing as a universal binary. What I'm asking about is project structure, this is a question specifically about how Urho's CMake system is intended to be used. I know that my C++ code has to be compiled on each platform, what I'm asking is how to structure a project to be able to do that easily. My understanding of the guides I read is that they're for setting up a project on a specific platform, whereas I'd like to know the best way to structure a project meant to compile on any platform. Is that clearer? I may be misunderstanding something fundamental about how CMake works, in which case that's why my inquiry is so muddled as I've never used it before.

-------------------------

Ka-Wiz | 2017-09-11 02:30:59 UTC | #4

Aha, I figured it out.

"...my C++ files would be too far "downstream" to be moved to a different platform easily, since they're in a project that is attached to a platform-specific build. First of all, is that a correct assessment?"

That was an incorrect assessment. When I said "attached to a platform-specific build" I was confusing the library build directory with the project directory. But after more careful reading of the guides (I swear I've read them over and over...) I figured out the workflow:

1. use cmake on source to configure and generate library project files
2. compile library for platform
3. create project as per "project scaffolding"
4. use cmake again, but set "where is the source code" to the folder of the created project and URHO3D_HOME to lib
5. open whatever IDE solution you generated, compile, enjoy

CMake threw me for such a loop that I was basically asking if I could build the library and my project at the same time, or even create a project that I could move between platforms without compiling the library for that platform first :stuck_out_tongue: told you I'm a little stupid.

oh, and to @johnnycable , now I can see why you thought I wanted a universal binary, what I was almost asking for was a universal library and I don't understand why I would ever ask for that either :rofl:

-------------------------

weitjong | 2017-09-11 02:30:59 UTC | #5

Glad to hear you figured it out. Some of the texts in the documentation were written by non-native English speaker (me :-), so contributions are welcome to make them clearer.

Just in case you or someone else still need the answers. The project scaffolding prepares a project "source tree", which you should then populate it with portable C++ code. The CMake invocation (via CLI or GUI) generates the project "build tree" for a specific target platform from this source tree. When cross-compiling ensures the cross-compiler toolchain is in the PATH of the host environment. The generated build tree can then be used to build the binaries for a specific platform. Multiple build tree can be generated from a single source tree. Use separate build tree path, naturally. This applies to both your own project and Urho3D project (aside from you just clone the source tree instead of scaffolding it yourself).

Your own project could depend on the Urho3D library directly from its build tree or from an installed location. The latter is what we referred as SDK in our documentation. If you are cross-compiling a lot, using built tree directly has an advantage as you can easily use URHO3D_HOME to point to one of many build trees you may have containing the Urho lib.

-------------------------

Ka-Wiz | 2017-09-11 02:45:30 UTC | #6

Thank you very much for the clarification, that was exactly what I was looking for, as I had thought the library build tree was supposed to be used as the project source tree. But yes, I will be cross-compiling a lot, and now I know that I can move around my project folder like I wanted and change it to point to different library build tree each platform :slight_smile:

-------------------------

