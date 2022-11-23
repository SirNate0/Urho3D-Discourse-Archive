weitjong | 2021-06-13 04:50:55 UTC | #1

It has been awhile since I last build from the main branch. I observe there is now a huge delay in the linking phase for the Urho3D library when the Angelscript subsystem is enabled. In the past I did not recall there is such massive different between have it enabled or disabled. Does anyone else have similar observation? My observation is conducted by first removing the test build tree each time.

-------------------------

weitjong | 2021-06-14 15:54:43 UTC | #2

@1vanK, do you know what could be the cause? Even if we have more complete AS script API binding now with your new generator, it still does not explain why because the time difference is really big. I have an Octa-core machine and it is still extremely slow to link the library with AS enabled now.

-------------------------

1vanK | 2021-06-14 19:03:08 UTC | #3

It probably depends on the compiler. I did not take measurements, because I did not have such a problem.

-------------------------

1vanK | 2021-06-14 21:07:51 UTC | #4

May be this is related https://github.com/urho3d/Urho3D/blob/master/Source/Urho3D/CMakeLists.txt#L45-L48

-------------------------

weitjong | 2021-06-15 01:41:40 UTC | #5

Thanks for your prompt reply. For me, this happened on a few compiler toolchains I have tried, but all using DBE. Still, like I said before I have never observed such massive linking time in the past. Originally I want to record some terminal sessions as the new assets for the website. Watching everything else just flying by makes this issue very glaring in my recordings. Later I will try using my host machine natively to build and compare the result and see whether any compiler flags tweak is necessary, if the large object is indeed the root cause.

-------------------------

George1 | 2021-06-15 14:23:29 UTC | #6

I also experienced this in the latest branch. After configured with CMake,  everytime we build a single example project in visual studio and run debug on it,  the whole library is rebuild again before the project is loaded.

-------------------------

weitjong | 2021-06-15 14:43:17 UTC | #7

I have created 2 new test build trees with native compiler toolchains, GCC 10.3.1 and Clang 11.0.0. I have observed the same slowness when linking the Urho3D library with AS enabled, which is consistent with what I have observed previously using DBE approach.

Checking on the large object files in the build tree, I did find one really huge on each build tree.

GCC build tree
```
-rw-rw-r--. 1 weitjong weitjong   12M Jun 15 22:02 build/linux/Source/Urho3D/CMakeFiles/Urho3D.dir/AngelScript/Generated_Classes.cpp.o
```

Clang build tree
```
-rw-rw-r--. 1 weitjong weitjong   12M Jun 15 22:21 ./Source/Urho3D/CMakeFiles/Urho3D.dir/AngelScript/Generated_Classes.cpp.o
```

The other object files do not even come close. The second largest produced by the code inside the `Source/Urho3D` is the `GraphicsLuaAPI.cpp.o` at 1010K.

Both GCC and Clang do not need any extra compiler flag to handle big object file, unlike MSVC. The build result also seems to be fine. I was able to run NSW and Editor without any runtime error. So, the only issue here is that it just takes too long (relatively speaking) to link the library now as compared to the past.

@1vanK Is it possible to break the `Generated_Classes.cpp` into a few smaller translation units?

-------------------------

weitjong | 2021-06-15 16:17:39 UTC | #8

hmm, I am not able to reproduce this one. It could be VS specific. I am using Makefile generator, touching a single cpp file in the sample project and build would only rebuild that single target executable without rebuilding the library again, as expected.

-------------------------

1vanK | 2021-06-16 01:04:48 UTC | #9

[quote="weitjong, post:7, topic:6892"]
Is it possible to break the `Generated_Classes.cpp` into a few smaller translation units?
[/quote]

It is possible , but I don’t have time for this yet

-------------------------

weitjong | 2021-06-16 01:13:27 UTC | #10

Take your time. It is just a hunch anyway. Hopefully it will solve the issue. Building for Android platform is extremely painful to wait now as it has to go though the linking phase a few times for each build configs in the universal build.

-------------------------

George1 | 2021-06-16 05:24:02 UTC | #11

I see, but debug does take too long compare to older rev.

-------------------------

weitjong | 2021-07-07 18:02:22 UTC | #12

I notice the build cache is not working correctly anymore in the GitHub Action. The build cache for each job is evicted sooner than expected. I suspect the build cache is now getting too large and as such the cache from each build job is thrashing each other as it hits the quota limit of our free account. And, I suspect the large object file is the culprit. We use `ccache` which caches the compiled object files to speed up the CI build. Now only a few builds still have a good cache hit.

-------------------------

