weitjong | 2019-10-20 16:07:53 UTC | #1

Today I have updated the Web DBE for Urho3D to switch from Fastcomp backend to upstream LLVM backend. This latest LLVM upstream can be installed and activated explicitly using EMSDK. It is not the default yet. I am using EMCC 1.39.0 in my experiment. With a few manual tweaks on the CMake build script, I was able to use the new compiler toolchain to compile the Urho3D library, however, it failed to link the library with the sample targets. This was the linker error I got for STATIC build config. Similar assertion error happened for SHARED build config too.

```
[100%] Linking CXX executable ../../../bin/Urho3DPlayer.html
wasm-ld: /b/s/w/ir/cache/builder/emscripten-releases/llvm-project/lld/wasm/SyntheticSections.cpp:468: virtual void lld::wasm::LinkingSection::writeBody(): Assertion `isec->getComdatName() == comdat' failed.
Stack dump:
0.	Program arguments: /emsdk-master/upstream/bin/wasm-ld -o ../../../bin/Urho3DPlayer.html --allow-undefined --lto-O0 -L/emsdk-master/upstream/emscripten/system/local/lib CMakeFiles/Urho3DPlayer.dir/Urho3DPlayer.cpp.o -L/emsdk-master/upstream/emscripten/system/lib ../../../lib/libUrho3D.a --import-memory --import-table -mllvm -combiner-global-alias-analysis=false -mllvm -enable-emscripten-sjlj -mllvm -disable-lsr --export __wasm_call_ctors --export __data_end --export main --export malloc --export free --export setThrew --export __errno_location -z stack-size=5242880 --initial-memory=134217728 --no-entry --global-base=1024 --relocatable 
 #0 0x00007fec59b09254 PrintStackTraceSignalHandler(void*) (/emsdk-master/upstream/bin/../lib/libLLVM-10svn.so+0x709254)
 #1 0x00007fec59b06fde llvm::sys::RunSignalHandlers() (/emsdk-master/upstream/bin/../lib/libLLVM-10svn.so+0x706fde)
 #2 0x00007fec59b09508 SignalHandler(int) (/emsdk-master/upstream/bin/../lib/libLLVM-10svn.so+0x709508)
 #3 0x00007fec5caea890 __restore_rt (/lib/x86_64-linux-gnu/libpthread.so.0+0x12890)
 #4 0x00007fec5870ee97 raise (/lib/x86_64-linux-gnu/libc.so.6+0x3ee97)
 #5 0x00007fec58710801 abort (/lib/x86_64-linux-gnu/libc.so.6+0x40801)
 #6 0x00007fec5870039a (/lib/x86_64-linux-gnu/libc.so.6+0x3039a)
 #7 0x00007fec58700412 (/lib/x86_64-linux-gnu/libc.so.6+0x30412)
 #8 0x00000000006e7799 lld::wasm::LinkingSection::writeBody() (/emsdk-master/upstream/bin/wasm-ld+0x6e7799)
 #9 0x00000000006d699a lld::wasm::SyntheticSection::finalizeContents() (/emsdk-master/upstream/bin/wasm-ld+0x6d699a)
#10 0x00000000006d0d88 lld::wasm::(anonymous namespace)::Writer::run() (/emsdk-master/upstream/bin/wasm-ld+0x6d0d88)
#11 0x00000000006c9831 lld::wasm::writeResult() (/emsdk-master/upstream/bin/wasm-ld+0x6c9831)
#12 0x00000000006ab67a lld::wasm::(anonymous namespace)::LinkerDriver::link(llvm::ArrayRef<char const*>) (/emsdk-master/upstream/bin/wasm-ld+0x6ab67a)
#13 0x00000000006a61d8 lld::wasm::link(llvm::ArrayRef<char const*>, bool, llvm::raw_ostream&) (/emsdk-master/upstream/bin/wasm-ld+0x6a61d8)
#14 0x000000000041f61b main (/emsdk-master/upstream/bin/wasm-ld+0x41f61b)
#15 0x00007fec586f1b97 __libc_start_main (/lib/x86_64-linux-gnu/libc.so.6+0x21b97)
#16 0x000000000041f1a9 _start (/emsdk-master/upstream/bin/wasm-ld+0x41f1a9)
shared:ERROR: '/emsdk-master/upstream/bin/wasm-ld -o ../../../bin/Urho3DPlayer.html --allow-undefined --lto-O0 -L/emsdk-master/upstream/emscripten/system/local/lib CMakeFiles/Urho3DPlayer.dir/Urho3DPlayer.cpp.o -L/emsdk-master/upstream/emscripten/system/lib ../../../lib/libUrho3D.a --import-memory --import-table -mllvm -combiner-global-alias-analysis=false -mllvm -enable-emscripten-sjlj -mllvm -disable-lsr --export __wasm_call_ctors --export __data_end --export main --export malloc --export free --export setThrew --export __errno_location -z stack-size=5242880 --initial-memory=134217728 --no-entry --global-base=1024 --relocatable' failed (-6)
Source/Tools/Urho3DPlayer/CMakeFiles/Urho3DPlayer.dir/build.make:86: recipe for target 'bin/Urho3DPlayer.html' failed
make[3]: *** [bin/Urho3DPlayer.html] Error 1
CMakeFiles/Makefile2:1426: recipe for target 'Source/Tools/Urho3DPlayer/CMakeFiles/Urho3DPlayer.dir/all' failed
make[2]: *** [Source/Tools/Urho3DPlayer/CMakeFiles/Urho3DPlayer.dir/all] Error 2
CMakeFiles/Makefile2:1438: recipe for target 'Source/Tools/Urho3DPlayer/CMakeFiles/Urho3DPlayer.dir/rule' failed
make[1]: *** [Source/Tools/Urho3DPlayer/CMakeFiles/Urho3DPlayer.dir/rule] Error 2
Makefile:485: recipe for target 'Urho3DPlayer' failed
make: *** [Urho3DPlayer] Error 2
```

Is there anyone here experiment with the upstream LLVM backend too? Probably I should file a bug report to Emscripten.

-------------------------

weitjong | 2019-10-26 05:30:05 UTC | #2

It is simpler than I thought to get it working. Just need to **bump the CMake minimum required version** to something higher than what we have currently. No manual tweaking the build tree and no more linking error. All sample targets built cleanly. Tested the skeletal animation sample locally and it looked good. I didn't time the build time just now but I feel the link time is much faster, which is what I hope for. This should help to resolve the Web CI build running out of time issue.

-------------------------

weitjong | 2019-10-28 10:13:47 UTC | #3

With the new backend, the STATIC/WASM build config is so much efficient than before. Previously we could not use all the logical CPU to perform the web build because they would get choked during linking phase, now that is not true anymore (at least on my test). I have now modified the 'make' task in Rakefile to take advantage of all the available logical unit automatically, and also altered the Web CI build to use 4 parallel threads instead of 2. The Web CI can now build all the samples (without any exclusion) and still have plenty of time left. That's the good news.

The bad news are, 1) Emscripten does not support asm.js anymore and 2) the SHARED lib type still hit by the linker error.

From what I have read, the new backend when configured with WASM=0 will emit plain JS as output instead of asm.js. The Emscripten keeps WASM=0 mode for older browsers that do not support WASM (those that support asm.js also support WASM anyway). In my experiment that took forever to complete for our sample build targets. Thus, if there is no objections from others then as part of the migration to the new backend, I will modify Urho3D build system to drop the support for EMSCRIPTEN_WASM=0. Effectively removing that build option all together because WASM will be enabled by default all the way. I will also drop the other experimental build option to build Urho3D as a "MODULE" lib type. It was introduced by me at the time it looked like a nice idea because Emscripten's linking phase was so slow. So, that will be gone too.

As for the SHARED lib type linker error, I have logged it as an issue in the upstream Emscripten. See https://github.com/emscripten-core/emscripten/issues/9726.

BTW, all the changes are currently only available in my personal fork. I am thinking of merging them into upstream Urho3D before releasing 1.8, despite it maybe a breaking change to some. Again, only when I don't hear anyone making a noise about this plan.

-------------------------

JTippetts | 2019-10-29 22:17:19 UTC | #4

It works pretty well for my unfinished little Reactor Idle clone [experiment](https://jtippetts.github.io/GoldRush.html). It used to take about 2 or 3 minutes to link, but it links in about 20 seconds now. The execution *seems* a bit punchier, but that's pretty hard to quantify in this case since I have made a lot of code changes since I last tested a build. I'm fine with merging the changes, and thanks for your work on this.

-------------------------

weitjong | 2020-01-11 06:51:21 UTC | #5

I have some free time to continue the experiment this week in my fork. Since there is no objection, I will proceed to remove the EMSCRIPTEN_WASM as a build option, i.e. WASM is always enabled and the only supported mode after this change. The SHARED and MODULE lib type will be removed too.

edit: Also bumped the minimum Emscripten SDK version required to 1.39.0.

edit: I think I have completed the refactoring on the build script side of things.

-------------------------

weitjong | 2020-01-12 02:14:03 UTC | #6

Just tested build with EMCC 1.39.5 and got a runtime error although the build went fine. It appears the latest 1.39.5 has a breaking change and caused an exception to be thrown. The EMCC 1.39.0 to 1.39.4 does not have this problem. Fortunately, the (quick) fix is simple. I have made another commit to add a setting to revert back the generated JS script to its previous behavior. Proper fix to switch to the new behavior can wait until someone has time to do it.

I have tested the Water sample also. It still has the same rendering artifacts as before due to WebGL but I did not able to crash it anymore with mouse move event. I recall this sample will crash using the fastcomp backend with the trap mode leave to "allow", its default. So, it could mean the new LLVM backend has different kind of behavior by default. I found this explanation in the Emscripten documentation, which may be relevant (https://emscripten.org/docs/compiling/WebAssembly.html#llvm-wasm-backend). And if so, I think I will leave it to LLVM backend default, i.e. letting users to override to pass the `-mnontrapping-fptoint` for their own project if it is desired. It is anyway always easier to script for adding more flags at the downstream project than to script for editing/modifying the inherited flags. And besides, it seems the code generated by LLVM WASM backend is fast in its current default setting.

Edit: Oops! Accidentally my fork’s CI job has uploaded the new web samples to Urho3D main website (https://urho3d.github.io/samples/). 😅 No harm done though.

-------------------------

weitjong | 2020-01-12 14:57:50 UTC | #7

All the relevant changes are cherry-picked to Urho3D upstream repo under "web-build-with-LLVM-backend" test branch now. They will be merged soon to master branch after CI clearing them and also when no one else raises any issues in the meantime.

Edit: it is done.

-------------------------

