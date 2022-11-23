misc | 2019-11-29 08:09:48 UTC | #1

I get the error below when I compile with clang but it doesn't happen with gcc.

> CMake Error at Source/ThirdParty/SDL/cmake/macros.cmake:73 (message):
>   *** ERROR: Missing Xext.h, maybe you need to install the libxext-dev
>   package?
> Call Stack (most recent call first):
>   Source/ThirdParty/SDL/cmake/sdlchecks.cmake:441 (message_error)
>   Source/ThirdParty/SDL/CMakeLists.txt:1076 (CheckX11)

I know there are similar posts but I tried the solution in those posts to no avail.
I tried cleaning the build tree, deleting it entirely and even cleaning the local repo with git-clean -fxd.

I am no expert but when I compile with clang, cmake's configuration finishes quicker as if its cached (even if its the first time configuring it). Is it possible its cached somewhere outside the urho3d directory?? I'm using ubuntu bionic.

-------------------------

weitjong | 2019-11-29 14:08:04 UTC | #2

It does not make too much sense. Clang is designed to be a drop-in replacement for GCC, so it should see the same thing as GCC. In other words, your build environment either has that header file already installed or it hasn’t. Both Clang and GCC are looking at a same place to find it.

CMake caches things in generated build tree. If you use a newly generated build tree then there should not be any cached result from CMake. 

Our build system is capable of speeding up the build by using “ccache”. But I doubt you have configured your build environment to use it yet.  Even if you do, you don’t usually need to worry about the object cache stored by “ccache”. It knows when to invalidate them.

-------------------------

SirNate0 | 2019-11-30 06:11:34 UTC | #3

I don't know if it's related, but how are you specifying which compiler to use?

-------------------------

misc | 2019-12-03 13:00:26 UTC | #4

I set it by -DCMAKE_CXX_COMPILER=clang++

-------------------------

SirNate0 | 2019-12-03 13:17:41 UTC | #5

Did you also set the C compiler to be clang? And you set it when first creating the build tree, right?

-------------------------

misc | 2019-12-03 13:45:43 UTC | #6

Yes, I did.

I think I'll just reinstall my OS. It's in a separate partition anyway. This is probably due to installing/uninstalling packages when I was trying different frameworks.

-------------------------

weitjong | 2019-12-04 10:21:17 UTC | #7

[quote="misc, post:6, topic:5739"]
I think I’ll just reinstall my OS. It’s in a separate partition anyway.
[/quote]

There is absolutely no need for that. If I were you I will just make sure the source tree is pristine without any generated stuffs from CMake. Sometimes first time user forget to instruct CMake to generate out-of-source build tree initially and in doing so messing up the Urho3D source tree. When in doubt, it would be much quicker to just delete the Urho3D project source tree and re clone it again. And retry the CMake initial configuration and generation step. For Clang, I would do it like this:

```
$ CC=clang CXX=clang++ build_tree=build/clang rake cmake
```

And if you have docker engine and would like to use one of our prepared docker images then you can try:

```
$ CC=clang CXX=clang++ build_tree=build/clang script/dockerized.sh native
```

The latter approach takes care of all the build dependencies for you, i.e. you do not need to install the Urho3D prerequisite development packages yourself into your build environment before anything else.

-------------------------

misc | 2019-12-04 03:13:53 UTC | #8

It worked, thanks.

I've been planning to try a different Ubuntu flavor for next year though :)

-------------------------

Modanung | 2019-12-04 10:21:59 UTC | #9

[quote="misc, post:8, topic:5739"]
I’ve been planning to try a different Ubuntu flavor for next year though :slight_smile:
[/quote]

I like [Mint](https://linuxmint.com/).

Also, welcome to the forums! :confetti_ball: :slightly_smiling_face:

-------------------------

