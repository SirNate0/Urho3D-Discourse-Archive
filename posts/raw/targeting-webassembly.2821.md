weitjong | 2017-02-25 14:45:15 UTC | #1

Successfully tweaked our build system to target WebAssembly today and it worked without much effort. Tested the 12_PhysicsStressTest using the Firefox Nightly confirmed the generated wasm file work. In my brief test I can see it has higher performance than the asm.js version. This is achieved without changing anything else yet in the code. Smaller output size is already a win.

I will commit my tweak into the "refactor-buildsystem" branch shortly. If you want to experiment with it now, you have to upgrade your Emscripten compiler toolchain to the bleeding edge (they have not been released yet) as follows:

    $ git clone https://github.com/juj/emsdk.git
    $ cd emsdk
    $ ./emsdk install sdk-incoming-64bit binaryen-master-64bit
    $ ./emsdk activate sdk-incoming-64bit binaryen-master-64bit

And when configuring/generating the Urho3D build tree, simply passing in an extra new build option called "EMSCRIPTEN_WASM" and set it to enabled. That's it!

-------------------------

weitjong | 2017-02-27 15:40:07 UTC | #2

Not sure if it is a bug in Emscripten or just in my build environment, but it seems like when WASM mode is requested then EMCC does not minify/uglify the generated JS file anymore, where as it would when using asm.js. I wonder I should file a bug report upstream.

EDIT: krypken has beat me to it, see [Minify JS in WASM mode #4702](https://github.com/kripken/emscripten/issues/4702).

-------------------------

weitjong | 2017-03-02 01:28:27 UTC | #3

For those who want to try but don't have patience to build the Emscripten SDK, you can experiment with our pre-built SDK in GitHub [here](https://github.com/urho3d/emscripten-sdk/tree/incoming?files=1). Clone the "incoming" branch and just use the last command in the first post above to activate the SDK locally. The pre-built binary is for 64-bit Linux host system only. Sorry. 

It was newly built early this morning and I haven't tested it yet but I plan to use it to setup the WebAssembly CI build in the next few days.

-------------------------

cadaver | 2017-03-02 09:20:50 UTC | #4

Sweet! I hope to test this eventually.

-------------------------

weitjong | 2017-03-03 14:02:51 UTC | #5

The setup seems to work and the new CI jobs are now building. However, I think we need to change on how we upload the web samples so that both asmjs and wasm versions can coexist.

-------------------------

weitjong | 2017-03-05 01:21:16 UTC | #6

The build option to target WebAssembly is now available in master branch. We need your help to test this one out to see if there are any issues before the master branch is being tagged for Urho3D r1.7.

-------------------------

cadaver | 2017-03-23 08:01:56 UTC | #7

Finally had time to install Emscripten incoming SDK.

I had some weird trouble where (on Windows) CMake would act as if the WEB variable wasn't specified by cmake_emscripten.bat, and for example boost wouldn't get installed for AngelScript generic bindings. So I had to specify it manually. Also had to specify something to NATIVE_PREDEFINED_MACROS or CMake would barf at "Could not check compiler toolchain as it does not handle '-E -dM' compiler flags correctly"

For WebAssembly, had to disable URHO3D_THREADING as otherwise the compilation would complain of pthreads not being supported. WebAssembly also needed to be disabled during initial CMake run or otherwise I'd get a lot of "asm2wasm.exe has stopped working" during the C/C++ feature check phase.

I still need to retest on a clean checkout to make sure none of these weren't due to stale stuff in the checkout. But even with these, I managed to get a working compile in the end.

-------------------------

weitjong | 2017-03-23 14:03:39 UTC | #8

I just pushed a fix into master branch. Please kindly retry the build on Windows host when you have time. If you reuse the build tree then you need to clean the CMake cache first.

-------------------------

cadaver | 2017-03-23 21:29:34 UTC | #9

Non-WebAssembly build went now flawlessly on Windows with defaults. Will try WebAssembly build next. Thanks!

-------------------------

cadaver | 2017-03-23 22:42:54 UTC | #10

WebAssembly build was also fine by specifying nothing more than -DEMSCRIPTEN_WASM=1 once I already had the previous (non-WASM) build in place. Doing it without the previous build's cmake cache would still cause asm2wasm crashes. But I suppose that is Emscripten's problem which they may fix in the future, nothing to do with Urho3D itself.

-------------------------

weitjong | 2017-03-24 00:39:35 UTC | #11

Glad to hear that. I still don't like the fact you need two steps process in order to get WASM build properly though. On Linux host the WASM build tree can be generated in one go. Could you paste me a sample of how the actual error looks like? Thanks.

-------------------------

cadaver | 2017-03-24 08:44:22 UTC | #12

I tested on Windows 7 and it's just the program crash dialog "asm2wasm.exe has stopped working". After closing the dialog, the corresponding CMake test (e.g. Looking for malloc.h) reports back as failed. There's no other error message.

-------------------------

weitjong | 2017-03-24 11:50:17 UTC | #13

Actually I have setup things slightly differently in the refactoring branch now that may fix this. However, the branch is still in a flux state.

-------------------------

weitjong | 2017-03-25 05:05:51 UTC | #14

It was an oversight on my part. Even though on Linux host the asm2wasm from Binaryen does not crash, the wasm-validator actually prevented some of the functions from being detected correctly too in WASM build for Linux. Which is to say, previously I was actually testing on sub-optimal wasm build artifacts because I believe SDL substituted the missing standard C functions with their own implementation. In other words, after this fix our WASM build should produce even better result.

I see if I could push my local refactoring branch out and merge with master soon. I am actually (when I have time) working on bringing the main/side module feature in for Emscripten build. If I could not do that soon enough then I may cherry pick just the required bit that should fix the asm2wasm.exe crash on Windows host. I don't want to do that now to master branch because it may introduce conflict later on the refactoring-buildsystem branch, so I want to avoid that if I could.

-------------------------

weitjong | 2017-03-26 14:25:51 UTC | #15

I have just done a merge to the master branch. I believe you should be able to generate the initial WASM build tree in one step now.

-------------------------

cadaver | 2017-03-27 08:37:50 UTC | #16

Thanks! Should be able to try today.

-------------------------

cadaver | 2017-03-28 18:02:49 UTC | #17

No more crashes when configuring the build for WebAssembly after a clean clone. However, now I notice no .html file being produced when I run CMake, then build a single sample (e.g. 04_StaticScene)? Seems this happens also without WebAssembly.

-------------------------

weitjong | 2017-03-29 14:51:09 UTC | #18

Yes, that's the expected result now for the default build option. I forgot to give a head up. My apology. The default output format for web build is now .js (when using asm.js mode) or .wasm (when using WebAssembly mode). It is now the responsibility of the user to define the HTML shell of their choice and design. For more sophisticated web app the lib user may bundle the .js/.wasm module(s) using external tool like Webpack or SystemJS into their external (one-page) HTML file. However for simpler web app, user can still indicate to let our build system to generate the shell like it used to by calling "add_html_shell()" macro explicitly without passing any argument. If an argument is provided then it will be used as the path to user own customized HTML shell file. And for those users who just want to quickly test then they can turn on the "URHO3D_TESTING" build option. This option tells our build system to generate artifact with emrun's prologue and epilogue. As the artifact must be "runnable" by emrun, our build system will ensure the shell is added automatically if user hasn't added one. 

Let me know what you think with the new default settings.

-------------------------

cadaver | 2017-03-29 08:50:26 UTC | #19

Thanks for the explanation, that sounds fine because the .js / .wasm is arguably the proper executable.

-------------------------

weitjong | 2017-04-02 04:45:23 UTC | #20

Finally I am able to use the latest version of CLion (2017.1) to do a "proper" cross-compiling build to target Web platform and to target WebAssembly. In the past I was using vi as editor and terminal as IDE when cross-compiling. :slight_smile:

-------------------------

