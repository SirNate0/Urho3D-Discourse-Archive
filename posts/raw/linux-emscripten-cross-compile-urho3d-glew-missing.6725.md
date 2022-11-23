nickwebha | 2021-02-23 13:15:11 UTC | #1

When I try to compile Urho3D for the web (`cmake -DWEB=1 .`) I get the following error:
>     In file included from /home/nick/Urho3D-1.7.1/Source/Urho3D/Graphics/../Graphics/GraphicsImpl.h:29,
>                      from /home/nick/Urho3D-1.7.1/Source/Urho3D/Graphics/Batch.cpp:28:
>     /home/nick/Urho3D-1.7.1/Source/Urho3D/Graphics/../Graphics/OpenGL/OGLGraphicsImpl.h:39:10: fatal error: GLEW/glew.h: No such file or directory
>        39 | #include <GLEW/glew.h>
>           |          ^~~~~~~~~~~~~
after over half of it compiles. A "regular" compile (with no switches) compiles just fine.

I see GLEW in to Urho3D zip I downloaded under the ThirdParty folder. I even installed the *dev* packages on Ubuntu 20.04.

What am I missing?

-------------------------

SirNate0 | 2021-02-22 22:28:54 UTC | #2

Is it actually using emscripten to compile it? What version of emscripten?

What are the undefined symbols from your Edit? With the new build did you also update all of the included headers from the new build? I've had some issues before from changing the source (switching git branches) changing the included files while not building a new copy of the library archive giving me undefined symbols.

Also, I would strongly recommend using the master branch and not the 1.7.1 release, which I think is now a couple of years old code (maybe with a small bugfix since then to deal with compilers making a breaking change).

-------------------------

nickwebha | 2021-02-23 13:41:02 UTC | #3

*Sorry, in a haze yesterday I put two problems in one thread. Let us focus on the Emscripten issue(s). I have cleaned up my first post.*

Switching from the v1.7.1 version on the main site to the master branch from Github got rid of my "no GLEW" error. Urho3D seems to compile fine now. I would have never thought to have done that, thinking the latest version on the website would be the latest stable available. Not sure I like the idea of cloning the git repository now and again some time in the future-- say, after a fresh install of my OS-- without knowing what changed in between or any way to track versions. Any way...

I am not sure how to tell if it is using Emscripten to compile or not. It is producing a static library without errors if that makes any difference. When I look at htop I see `/usr/lib/gcc/x86_64-linux-gnu/9/cc1plus` using all my CPU so I guess not? Should I have expected to see `clang` or `em++` or something?

**Update**
Strange thing just happened. I ran `cmake -DWEB=1 && make` once and it compiled fine (as described above). I deleted the directory, re-cloned it from Github, and ran the same commands again and now it is complaining it is missing GLEW again. Whatever the issue it seems intermittent.

    In file included from /home/nick/Urho3D/Source/Urho3D/Graphics/../Graphics/GraphicsImpl.h:29,
                     from /home/nick/Urho3D/Source/Urho3D/Graphics/Batch.cpp:28:
    /home/nick/Urho3D/Source/Urho3D/Graphics/../Graphics/OpenGL/OGLGraphicsImpl.h:39:10: fatal error: GLEW/glew.h: No such file or directory
       39 | #include <GLEW/glew.h>
          |          ^~~~~~~~~~~~~

A personal thought:
I really, really want to use Urho3D because of how lightweight it is and I love the layout of it. However with these compilation problems on a fresh install (!) and the lack of documentation make it is very difficult. Once I figure out all the in's and out's that may change but right now all I have in frustration. Thank God for the active community here on the forums.

-------------------------

1vanK | 2021-02-23 15:09:57 UTC | #4

try old version of emscripten https://discourse.urho3d.io/t/emscripten-windows/6719/2?u=1vank

-------------------------

nickwebha | 2021-02-23 15:54:48 UTC | #5

Thanks for the tip.

However `./emsdk install 2.0.8` just hangs on Linux. Besides, downgrading will effect all my other projects using Emscripten since this is a global change.

The build system does not seem to be using Emscripten to build the static library. I compared the sizes of the one it output without parameters and the one output with `-DWEB=1`. They are the same size which seems to indicate to me that it just build the generic one.

-------------------------

SirNate0 | 2021-02-23 20:31:34 UTC | #6

Make sure you actually activate the emsdk. Further, use the bash scripts for the initial build directory CMake call, as they set up things like the toolchain file for the web build (e.g. call `script/cmake_emscripten.sh WebBuild` for that initial build). I got it working with emscripten 2.0.12, though I'm not sure how old that is. To do that, though, I had to manually specify the EMSCRIPTEN_ROOT_PATH as the later versions of emscripten don't set one of the environment variables we were using previously (I think that is the cause at least). So for example, I call
`rm -r WebBuild; EMSCRIPTEN_ROOT_PATH=~/tools/emsdk/upstream/emscripten URHO3D_HOME=~/builds/Urho3D/WebBuild/ script/cmake_emscripten.sh WebBuild` from my project directory, and it would be similar for the library build itself except without the `URHO3D_HOME` specification. The rm -r WebBuild is because I ended up getting parts of it wrong a lot, and you need to start from a clean directory each time with a lot of the errors in setting a compiler (because of some particularity of CMake, I think).

After the initial successful generation, you should be able to modify most things (like Debug or Release builds and such) directly through cmake without calling the scripts, as the relevant parts will have been saved to the CMakeCache.txt file by CMake. 

As to the documentation, I think it's generally pretty good for how to build the library, with the exception of the emscripten build, which is rather sparse in the details.

Also, for the web build, if you build the samples/tools you should get an html file (and js and wasm and pak files) in the WebBuild/bin directory, rather than regular executables (as a better check than file size, if you ask me).

-------------------------

nickwebha | 2021-02-24 02:09:21 UTC | #7

I was completely unaware of what `cmake_emscripten.sh` was for! Saw it there but never thought to use it for this. I can confirm it is using `emcc` and `em++` now.

`EMSCRIPTEN_ROOT_PATH=/home/nick/emsdk/upstream/emscripten ../script/cmake_emscripten.sh .` include a build directory I made inside the Urho3D root starts the process but during cmake I get:

    In file included from /home/nick/Urho3D/Source/Urho3D/Precompiled.h:28:
    In file included from /home/nick/Urho3D/Source/Urho3D/Container/HashMap.h:25:
    In file included from /home/nick/Urho3D/Source/Urho3D/Container/../Container/HashBase.h:31:
    /home/nick/Urho3D/Source/Urho3D/Container/../Container/Allocator.h:31:10: fatal error: 'cstddef' file not found
    #include <cstddef>
             ^~~~~~~~~

I did not want to start copying files all around and making a mess. How could such a standard file be missing?

I plan on writing a few short how-to's on my blog once I figure all this out. Help contribute to the lack of documentation.

-------------------------

JTippetts1 | 2021-02-24 01:38:17 UTC | #8

If your emsdk is properly set up, you shouldn't have to copy standard headers around. The fact it can't find cstddef tells me your emsdk is screwed up somehow, either in how it is configured or in how the build system sees it.

Make sure your emsdk is correctly installed and activated. Also, if you continue to have problems, try updating cmake. In the past, I have had web build issues that were resolved by updating to a newer version of cmake. I build my web game under Linux for Windows, using cmake version 3.18.0 and emsdk version 1.39.17 and everything works pretty flawlessly right out of the box.

-------------------------

nickwebha | 2021-02-24 16:10:42 UTC | #9

I spent the morning installing a fresh VM.

I installed Emscripten (per their [recommended steps](https://emscripten.org/docs/getting_started/downloads.html)). I ran `source ~/emsdk/emsdk_env.sh`. I installed the latest version of cmake from [their PPA](https://apt.kitware.com/) (v3.16.3). I grabbed Urho3D from GitHub, not the zip on the main site. I ran `EMSCRIPTEN_ROOT_PATH=/home/nick/emsdk/upstream/emscripten ../script/cmake_emscripten.sh .` in the build folder I created under the Urho3D root (I also tried running it in the root just to be sure).

I keep getting this missing header (`cstddef`).

When this is all done I am writing a blog post documenting how to do this correctly.

**Edit 1**
I downgraded Emscripten to 2.0.8 as suggested previously. The fresh VM install is now compiling so this seems to be an issue with the newest Emscripten (they changed something).

**Edit 2**
I got the Urho3D source and samples built! Thank you guys so much for your help there!

For anyone show comes across this later:
`EMSCRIPTEN_ROOT_PATH=/home/nick/emsdk/upstream/emscripten ../script/cmake_emscripten.sh .`
`make`
Adjust for your own paths. It is that simple.

-------------------------

nickwebha | 2021-02-24 20:32:46 UTC | #10

My project compiles fine. However when I try to run it in the browser (both Chrome and Firefox) I get (from Chrome):
>     exception thrown: RuntimeError: abort(alignment fault) at Error
>         at jsStackTrace (https://localhost/project.js:2389:14)
>         at stackTrace (https://localhost/project.js:2404:11)
>         at abort (https://localhost/project.js:1400:43)
>         at alignfault (https://localhost/project.js:780:2)
>         at SAFE_HEAP_STORE_i64_8_8 (https://localhost/project.wasm:wasm-function[43311]:0x42ef01)
>         at Urho3D::ResourceGroup::ResourceGroup() (https://localhost/project.wasm:wasm-function[19563]:0x1686a4)
>         at Urho3D::HashMap<Urho3D::StringHash, Urho3D::ResourceGroup>::KeyValue::KeyValue() (https://localhost/project.wasm:wasm-function[19686]:0x16b928)
>         at Urho3D::HashMap<Urho3D::StringHash, Urho3D::ResourceGroup>::Node::Node() (https://localhost/project.wasm:wasm-function[19685]:0x16b913)
>         at Urho3D::HashMap<Urho3D::StringHash, Urho3D::ResourceGroup>::ReserveNode() (https://localhost/project.wasm:wasm-function[19510]:0x1671e0)
>         at Urho3D::HashMap<Urho3D::StringHash, Urho3D::ResourceGroup>::HashMap() (https://localhost/project.wasm:wasm-function[19501]:0x166f7c),RuntimeError: abort(alignment fault) at Error
>         at jsStackTrace (https://localhost/project.js:2389:14)
>         at stackTrace (https://localhost/project.js:2404:11)
>         at abort (https://localhost/project.js:1400:43)
>         at alignfault (https://localhost/project.js:780:2)
>         at SAFE_HEAP_STORE_i64_8_8 (https://localhost/project.wasm:wasm-function[43311]:0x42ef01)
>         at Urho3D::ResourceGroup::ResourceGroup() (https://localhost/project.wasm:wasm-function[19563]:0x1686a4)
>         at Urho3D::HashMap<Urho3D::StringHash, Urho3D::ResourceGroup>::KeyValue::KeyValue() (https://localhost/project.wasm:wasm-function[19686]:0x16b928)
>         at Urho3D::HashMap<Urho3D::StringHash, Urho3D::ResourceGroup>::Node::Node() (https://localhost/project.wasm:wasm-function[19685]:0x16b913)
>         at Urho3D::HashMap<Urho3D::StringHash, Urho3D::ResourceGroup>::ReserveNode() (https://localhost/project.wasm:wasm-function[19510]:0x1671e0)
>         at Urho3D::HashMap<Urho3D::StringHash, Urho3D::ResourceGroup>::HashMap() (https://localhost/project.wasm:wasm-function[19501]:0x166f7c)
>         at abort (https://localhost/project.js:1402:10)
>         at alignfault (https://localhost/project.js:780:2)
>         at SAFE_HEAP_STORE_i64_8_8 (https://localhost/project.wasm:wasm-function[43311]:0x42ef01)
>         at Urho3D::ResourceGroup::ResourceGroup() (https://localhost/project.wasm:wasm-function[19563]:0x1686a4)
>         at Urho3D::HashMap<Urho3D::StringHash, Urho3D::ResourceGroup>::KeyValue::KeyValue() (https://localhost/project.wasm:wasm-function[19686]:0x16b928)
>         at Urho3D::HashMap<Urho3D::StringHash, Urho3D::ResourceGroup>::Node::Node() (https://localhost/project.wasm:wasm-function[19685]:0x16b913)
>         at Urho3D::HashMap<Urho3D::StringHash, Urho3D::ResourceGroup>::ReserveNode() (https://localhost/project.wasm:wasm-function[19510]:0x1671e0)
>         at Urho3D::HashMap<Urho3D::StringHash, Urho3D::ResourceGroup>::HashMap() (https://localhost/project.wasm:wasm-function[19501]:0x166f7c)
>         at Urho3D::ResourceCache::ResourceCache(Urho3D::Context*) (https://localhost/project.wasm:wasm-function[19500]:0x166e7b)
>         at Urho3D::Engine::Engine(Urho3D::Context*) (https://localhost/project.wasm:wasm-function[4069]:0x59f78)
>     printErr @ index.js:108

It seems Urho3D is doing something that neither asm.js nor WASM like with its casting/alignment. Of course the samples built and run fine so something is different when I do it.

-------------------------

SirNate0 | 2021-02-24 17:15:45 UTC | #11

Do you get any issues running the samples? Both the ones that you have built and the ones on the website.

-------------------------

nickwebha | 2021-02-24 21:17:03 UTC | #12

The ones that compiled with Urho3D run great. The ones I compile with the `libUrho3D.a` that was generated have the same issue.

Do the samples not use the same file?

I am going to play around with the flags.

-------------------------

SirNate0 | 2021-02-24 21:20:33 UTC | #13

They should use the same library and header files. Make sure you are seetting up all the build flags correctly on your project (mostly compiler flags, though I think they may possibly get saved to Urho3D.h now).

If you want the build flags you should use without using CMake I would make one of the samples with VERBOSE=1 and then just copy the compiler defines and such. I personally recommend using CMake, though.

I asked about the samples mainly because I wanted to make sure your build setup was actually successful. At this point it could be something in your project causing issues, though I'm not sure for the specific issue you saw with the alignment.

-------------------------

nickwebha | 2021-02-25 21:22:21 UTC | #14

I eventually figured it out.

For anyone who comes across this in the future set `-s SAFE_HEAP=0` for `em++`. I am not sure if this is recommended or not if there is a true alignment issue but there you go. For more on [SAFE_HEAP](https://emscripten.org/docs/porting/Debugging.html) see their page.

My thanks to everyone for their help. I could not have gotten this far without you.

-------------------------

nickwebha | 2021-07-30 15:04:33 UTC | #15

[quote="nickwebha, post:7, topic:6725"]
```
/home/nick/Urho3D/Source/Urho3D/Container/../Container/Allocator.h:31:10: fatal error: 'cstddef' file not found
#include <cstddef>
         ^~~~~~~~~
```
[/quote]
FYI

I can confirm that 2.0.12 was the last Emscripten version to not have this issue. I still have to experiment with the *dockerized.sh* script.

-------------------------

weitjong | 2021-07-30 16:31:03 UTC | #16

Thanks for the info. The current Web DBE image (with :master tag) still uses 2.0.8. But you can expect the next :latest tag of the DBE images to be available soon.

-------------------------

weitjong | 2021-08-19 16:41:40 UTC | #17

I have managed to upgrade the Web DBE image to use the latest EMCC 2.0.18 and adapt the `Emscripten.cmake` toolchain file that works with the new EMCC. I am able to build cleanly locally now. I haven't really tested it much as of this writing though.

The latest toolchain file can be found here: https://github.com/weitjong/cmake-toolchains. I cannot commit the change to Urho3D project yet as it may break the build with the current (old) Web DBE image used by GitHub Actions CI/CD workflow.

Since I am still in the process of upgrading the rest of DBE images, I won't be retagging the new DBE image for Urho3D project just yet. But for those who dare to try the bleeding edge, you can try the new Web DBE image by setting these env-vars before invoking:
```
DBE_NAME=weitjong/dockerized DBE_TAG=urho3d DBE_NAMING_SCHEME=tag script/dockerized.sh web
```

p.s. please do not use this "test" image in your CI as it may bust my Docker Hub download quota. Thanks.

p.p.s. my mistake. The "latest" version (or "tot") is actually 2.0.28. I have just changed the Dockerfile for the Web DBE so it uses 'tot' for installation. The new test Web IDE has EMCC 2.0.28 installed and activated as of this writing. Fortunately, Urho3D project still compiles cleanly with the adapted CMake toolchain file.

-------------------------

Bluemoon | 2022-05-05 23:21:53 UTC | #18

[quote="weitjong, post:17, topic:6725"]
The latest toolchain file can be found here: [GitHub - weitjong/cmake-toolchains: A collection of CMake toolchains for cross-compiling](https://github.com/weitjong/cmake-toolchains). I cannot commit the change to Urho3D project yet as it may break the build with the current (old) Web DBE image used by GitHub Actions CI/CD workflow.
[/quote]
@weitjong, I can confirm that using this provided toolchain on my windows 10 machine I was able to successfully build Urho3D with Emscripten version 3.1.9 (latest release as at this post). 

Any plan on committing this toolchain to Urho3D repo.

-------------------------

weitjong | 2022-05-07 11:48:32 UTC | #19

Thanks for confirming that. The CMake toolchain file is under MIT license. It is ok for me if you or anyone else who needs it to send a PR to merge it to the Urho3D main branch (if the old Web dockerized build environment can still work with it). The copyright notice can be changed from my personal name to “the Urho3D project” (Only for Urho3D project as I am part of that “entity”).

However, the current DBE is so out-dated now. I won’t be surprised that it may actually break with new toolchain file, although I haven’t actually tested it. While I am at it, the Android build needs to support newer Android plugin for Gradle too. The whole build system in general is stuck in time. Due to personal reason and capacity, I am not an active maintainer in this subject matter area anymore. New blood is needed.

-------------------------

Bluemoon | 2022-05-07 09:53:11 UTC | #20

Awesome, I wouldn't mind rising a PR too merge the new toolchain. 

On the other hand I would like to know how to go about updating the DBE, I could look into it if chance opens up.

-------------------------

weitjong | 2022-05-07 11:59:20 UTC | #21

Cool. Have a look here.

https://github.com/weitjong/dockerized

Check the commit logs to see which platforms require work or just simply assume all require more work as the last commit was already many moons ago.

Also note that upgrading the DBE images is one thing and upgrading the Urho3D build system to catch up with the other dependencies is totally another. The former just facilitates the build experimentation in an ephemeral container.

-------------------------

