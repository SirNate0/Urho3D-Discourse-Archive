johnnycable | 2018-04-04 10:14:37 UTC | #1

I'm trying to use Asset Importer to import some Blender asset. Anyway, it looks like it fails on exporting animation. I'm on 1.7. Now if I'm not mistaken, I remember the tool worked fine on 1.6, so I decided to give that a try.
But I cannot compile 1.6, because of a problem: 

    AssetImporter.cpp:1191:39: error: ordered
      comparison between pointer and zero ('aiVectorKey *' and 'int')

this is because I'm using XCode 9 toolchain, which bumped up clang error detection. So while 1.6 compilation worked with XCode 8, it doesn't anymore.
Anyway I have gcc and ninja installed with Brew on my Os X so I could try compiling with that. Compiling with ninja works without problem with 1.7, but still using clang.
My question: how do I switch to gcc using urho build system? What is the cmake option to be used?

-------------------------

weitjong | 2018-04-04 11:30:46 UTC | #2

There is none. I believe when you are using Makefile generator then CMake will just use the first compiler toolchain that it found in the PATH env var. And when you have more than one in the PATH and you want to use the alternative then you may have to export CC and CXX env vars to point to it. HTH.

-------------------------

johnnycable | 2018-04-04 11:30:42 UTC | #3

Guess so. There's anyway the usual Apple horror story: XCode doesn't like path tinkering with CXX and CC env vars... ([here](https://cmake.org/Wiki/CMake_FAQ#How_do_I_use_a_different_compiler.3F)) That's why I asked. 
Think I have to do the usual cmake heart operation...:wink: thank you anyway.

-------------------------

johnnycable | 2018-04-04 16:08:55 UTC | #4

Added:

    -DCMAKE_C_COMPILER=gcc-7 -DCMAKE_CXX_COMPILER=g++-7

to my cmake definitions and it worked.
Anyway I get load of errors because gcc doesn't reconise Os X libs... some setup is missing...

-------------------------

weitjong | 2018-04-05 00:36:31 UTC | #5

Forgotten about those two. To me, setting those or setting the two env vars I mentioned earlier during initial build tree generation does the same thing. In our CI for MacOS, we have build test for Makefile too and it works without any building issue. In other words, once you solved the hurdle of choosing the correct compiler toolchain that you want to use for your build, you still have to pass the other Urho3D build options to let the build system knows you are building for MacOS. For that I think you need GCC provided by Apple developer tools.

-------------------------

