rahulsanjay18 | 2018-11-12 04:03:10 UTC | #1

Hello,

I want to include the use of GNU Octave in my Urho application. I found [this](https://octave.org/doc/v4.2.2/Standalone-Programs.html) for compiling it for standalone programs, but it uses a different command to build those files. How do I incorporate that into Urho's build system (what to edit, what to put in, etc.), or at the very least, can someone point me in the right direction?

-------------------------

Modanung | 2018-11-12 10:54:23 UTC | #2

You can build Urho seperately from your project.
As an example: I use _cmake_ to build Urho, but _qmake_ to build the software I use the engine for.

-------------------------

rahulsanjay18 | 2018-11-12 18:59:52 UTC | #3

Right, but how do i link the .o files from my urho application with the .o files from the Octave part? What command can i use?

-------------------------

Sinoid | 2018-11-12 19:29:28 UTC | #4

You won't link the object files, you'll link your precompiled octave static/dynamic library (plus the 100+ GNU dependencies it probably has) and specify the header paths for it.

Ideally you just port the makefiles over to CMake, but it's a *GNU* project so that's a pipe-dream.

-------------------------

