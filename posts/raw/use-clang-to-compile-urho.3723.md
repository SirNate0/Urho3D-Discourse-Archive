godan | 2017-11-09 18:57:49 UTC | #1

Hey CMake/Build System experts (@weitjong I'm looking at you :slight_smile: )!

Is it possible to specify clang as the compiler to use for building Urho? If not, I need to create a custom cmake toolchain, right? Can the MinGW toolchain be hijacked for this?

I want to do this for a little proof of concept: Urho + [cling](https://github.com/root-project/cling) ([opengl demo here](https://www.youtube.com/watch?v=eoIuqLNvzFs)). I've got cling working (no small task) and I want to link Urho and start written some Urho code in the live interpreter. I'm pretty sure that all I need to do on the cling end is:

`./cling .L Urho3D`

Not surprisingly, when I just try to link my VS2015 compile Urho lib, a bunch of errors get thrown.

SO, I first need to compile Urho with clang. Any thoughts?

-------------------------

godan | 2017-11-09 21:54:31 UTC | #2

Working windows build here: https://github.com/MeshGeometry/cling-win

-------------------------

weitjong | 2017-11-10 00:17:37 UTC | #3

Clang is being designed as a drop-in replacement for GCC as far as build system is concerned. Thus, there is no need for different CMake toolchain file, just substitute the CC and CXX environment variables to point to `clang` and `clang++`, respectively, before invoking anything else to prep the environment. We have Clang CI build setup that way. You can have a look how it's done there in `.travis.yml`. Good luck.

-------------------------

johnnycable | 2017-11-10 13:40:17 UTC | #4

Using Os X here, I've built Urho with Apple Clang since 1.6. There's no different setup, except what @weitjong said about settings, as supposedly you're on Ubuntu or Win...

-------------------------

godan | 2017-11-10 14:20:48 UTC | #5

Good news that it is the same build process. Just to be clear, the process would be this (on windows):

- Clang/LLVM binaries (i.e. clang.exe and clang++.exe) are installed at: `C:\Dev\clang\bin`
- Urho is at `C:\Dev\Urho3D`
- run `cd C:\Dev\Urho3D`
- run: 

```
cmake_mingw build-clang -DCMAKE_CXX_COMPILER=C:\Dev\clang\bin -DCMAKE_CC_COMPILER=C:\Dev\clang\bin -DURHO3D_64BIT=1
```

- `cd build-clang`
- `make`

Does that look right? I know that ideally you would set the CC and CXX env variables instead of the CMAKE_CXX_COMPILER variable, but this doesn't seem to work so well on Windows (local scope environment variables don't seem to work, and setting the system wide variable is not ideal).

For example, here is the result when I use the local "set" method (I'm not building urho here, just a little test). MinGW still picks up it's own compiler:

![gcc_c|690x100](upload://1dNoeQ7JomqNnKjMrAB5yANpYiV.png)

But when I use the CMAKE_CXX_COMPILER method, I get:

![clang_c|690x111](upload://1wVNxzr1hn9VL1bALcAqBe9fsFc.png)

No idea why clang is failing to compile a test...

-------------------------

weitjong | 2017-11-10 14:38:40 UTC | #6

I have never used Clang on Windows before, so I am afraid you are on your own on this one. However, if I were you then I would not use CMake/MinGW variant of the generator for this purpose. Instead use CMake/Ninja generator which should not have any assumption on which compiler toolchain to use. And I would also make sure your Clang compiler toolchain actually works before hand. Try to compile/link a simple HelloWorld.c with it manually. Again, good luck.

-------------------------

godan | 2017-11-11 19:01:01 UTC | #7

OK, I made some progress! Turns out you don't need to compile Urho with clang. I can just load my Urho3D.dll (VS2015) in to Cling. I think this only works because I compiled Cling/Clang/LLVM with VS2015 as well. Otherwise it would be magic, right? 

Here is a little video of live loading Urho, creating a context, engine, some parameters and initializing:

https://youtu.be/VUJAx-a1DBQ

Despite this being really cool, it is still quite awkward to actually do some coding like this. Need to think on it...

-------------------------

godan | 2017-11-24 16:23:46 UTC | #8

Still very early days, but DAMN, live C++ coding is a lot of fun....

https://youtu.be/j9qTo5Upztg

-------------------------

johnnycable | 2017-11-24 20:13:33 UTC | #9

Wonderful! I'm not a great fan of scripting, but this looks awesome!
So compiling with Clang on Win is ok. Definitely the way to go.

-------------------------

