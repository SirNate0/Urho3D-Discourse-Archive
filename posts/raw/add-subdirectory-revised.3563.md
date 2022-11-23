rku | 2017-09-14 10:49:03 UTC | #1

I gave another stab at supporting `add_subdirectory()` and this time i got it working to the point where CI builds are green and SDK installation works.

It is not perfect though. This is sample project:
```cmake
# We can use our own project name as one would expect
project(Urho3DAsLibraryExample)

# Add game engine to the project.
add_subdirectory(Urho3D)
# Still need to append module path so UrhoCommon can be found
list(APPEND CMAKE_MODULE_PATH ${CMAKE_SOURCE_DIR}/Urho3D/CMake/Modules)
# This is required, but once engine build system start properly using target_include_directories() / target_compile_options() / target_link_libraries() this should be no longer needed.
find_package(Urho3D REQUIRED)

set(SOURCE_FILES main.cpp)
add_executable(Urho3DAsLibraryExample WIN32 ${SOURCE_FILES})
target_include_directories(Urho3DAsLibraryExample PRIVATE ${URHO3D_INCLUDE_DIRS})
target_link_libraries (Urho3DAsLibraryExample ${URHO3D_LIBRARIES} -lpthread)
```

Code: https://github.com/rokups/Urho3D/tree/add_subdirectory
CI build: https://travis-ci.org/rokups/Urho3D/builds/275409253

@weitjong does this have a chance to be accepted now?

-------------------------

weitjong | 2017-09-14 11:16:06 UTC | #2

Thanks for your work. I have a quick glance on the commit and see the majority of the changes are just the variable replacement. So, my answer is the same like last time. If it was just this replacements, we would have done it long time ago.

-------------------------

rku | 2017-09-14 11:50:39 UTC | #3

Of course majority of changes are just variable replacements, because in context of parent project `CMAKE_SOURCE_DIRECTORY` is no longer valid, however it is not just variable replacements. I took time to make sure everything works in all cases of engine build, which was not the case after just replacing variables. Building some tools as native when crosscompiling works. SDK installation and detection works. Embedding engine as subproject works. It is true that build system is not in a shape we would all prefer, but is this not a good stepping stone towards that direction? Last time we were discussing this matter problem was clear: SDK builds were broken. Since now nothing is broken could you please clarify actual reason why this cant be merged?

-------------------------

weitjong | 2017-09-15 01:19:21 UTC | #4

Of course I also see you made other changes but my view is the same. More work is needed. You may not take my words for it and submit the PR and let other core devs to review it. I will take no part with this review again as I already did. 

Do not get me wrong. We really would like to support that use case officially. However, I would rather to say our build system does not support it than to have a half-baked support for it.

-------------------------

weitjong | 2017-09-15 00:28:23 UTC | #5

[quote="rku, post:1, topic:3563"]
target_link_libraries (Urho3DAsLibraryExample ${URHO3D_LIBRARIES} -lpthread)
[/quote]

Ideally this line should just be

`
target_link_libraries (your-target Urho3D)
`

And CMake would automatically transitively add all the dependencies needed by Urho to your target regardless of the platform. On Linux it may be `pthread`, but on macOS it may be a list of Apple frameworks, and so on. If you can achieve that then I will say it is ready.

-------------------------

rku | 2017-09-15 10:45:07 UTC | #6

Indeed, I will try to get other things cleared up, primary target being getting rid of `define_dependency_lib()` as you said in your previous discussion. Solving this would make `find_package()` obsolete in this situation as well.

I could use some guidance too. Seems like AppVeyor is once again stuck on following:
> setup_test (NAME ExternalLibAS OPTIONS Scripts/12_PhysicsStressTest.as -w)

Could you tell me how exactly this sample is supposed to exit? Because i can see nothing in script that would quit sample after certain period of time. Also how do i setup testcase that AppVeyor is trying to run? I can see `CMakeLists.txt` content in `Rakefile`, but what source files are used for the test? I cant really tell that from ruby script.

Edit:
Also what should be the strategy to detect system link libraries in SDK builds that are not based on CMake?
Doing that through `add_subdirectory()` is easy because CMake takes care of it.
Doing that through pkg-config is easy because we can write libs to `LDFLAGS` in `Urho3D.pc`.
No idea what to do with this in case of using CMake without pkg-config.

Edit:
Maybe `FindUrho3D.cmake` could import libs/defines/includes from generated pkg-config script?

-------------------------

weitjong | 2017-09-15 13:13:13 UTC | #7

[quote="rku, post:6, topic:3563"]
Could you tell me how exactly this sample is supposed to exit?
[/quote]
In our CI build we simply turn on the URHO3D_TESTING build option. The engine is rigged internally when that build option is turned on whereby it auto-exits when a predefined time out period has been reached after the first frame is rendered.

We should not depends on pkg-config. The Urho3D.pc is a by-product only.

-------------------------

rku | 2017-09-15 13:04:42 UTC | #8

[quote="weitjong, post:7, topic:3563"]
We should not depends on pkg-config. The Urho3D.pc is a by-product only.
[/quote]

What then? I asked on CMake irc channel and there is no sane way of defining dependency libs automatically in `FindUrho3D.cmake` script other than defining these libs in there, which means having them defined in two places. Should build system write relevant information to a text file and store it in SDK for `FindUrho3D.cmake` to read it? It would be same thing as using pkg-config, except more code would have to be written and maintenance burden would increase. Using pkg-config appears to be working though, you can peek at [CI builds](https://travis-ci.org/rokups/Urho3D/builds/275876255) going green. I do agree it is not an ideal solution, but i can not think of better one.

-------------------------

weitjong | 2017-09-15 13:28:42 UTC | #9

As you already pointed out not all platform has pkg-config tool support, so that alone is pretty much ruling it out as the base for the configuration. All I can tell you is that, I won't go that route. It is difficult for me to elaborate what my solution will/would be, plus I may not have all the answers until I am actually there to tackle it. Having said that, my way of solving the problem may or may not actually work. So rather than telling you what then, it may be more beneficial to have you trying to tackle the problem from your own (fresh) idea. In short, take my comment with a pinch of salt. I will be happy to be proven wrong. The truth is, I am also searching for my successor for the build system maintainer.

-------------------------

rku | 2017-09-19 14:04:44 UTC | #10

Hey @weitjong i think you may be interested in seeing this. I probably got a little bit carried away here.. but instead of fixing old build system i just rewrote build scripts. Figured it would be easier just to write lean and mean build than taming behemoth that current build system is. It sure does not have macos/ios/android/angelscript/lua/tests/other bells and whistles, but i got CI builds for linux/mingw/msvc going and at least android should not be too much of a problem. Your work on current build system was a great inspiration as well as how-to guide. As it is now it totally is not PR-able, but maybe you can see something useful in there.

https://github.com/rokups/Urho3D/tree/build-system
https://travis-ci.org/rokups/Urho3D
https://ci.appveyor.com/project/rokups/urho3d

-------------------------

weitjong | 2017-09-19 14:45:25 UTC | #11

Well done. I don't have time to study all the build scripts but at a glance I can tell they are definitely different. I spotted a few concerns though. Mostly due to hard-coded path that looks to me to be too *nix specific. If you have followed our GitHub issue tracker then you may already know that I too have planned to rewrite (modernize) our existing build scripts and jump the minimum version to 3.8.2 (to take the advantage of the CMake C++11 compiler feature support). Having said that, I found I have no time nor energy/health/stamina to keep going or simply because I chose to pursuing other thing that interests me more in my free time. So, I will encourage you to continue what you have started. Who knows you can make your build system works for all the Urho3D supported platforms sooner or better than me. When I have time to pick up this again, I will definitely come back to check out your work again.

-------------------------

rku | 2017-11-10 16:37:50 UTC | #12

I took another stab at this problem and i am like 99% there. Last remaining issue is appveyor getting stuck with script tests when testing SDK builds. These tests do not time out properly. This only happens on windows. On linux very same builds time out properly.

~~@weitjong any idea where i could look for a problem? Seems like i checked it all - verified that windows CI builds build with `URHO3D_TESTING` and that timeout variable is set when doing scaffolding test build.. I am stuck.~~

Actually i just figured out why it fails. Will be done with this soon ^_^

-------------------------

godan | 2017-11-10 18:42:34 UTC | #13

Definitely looking forward to this - nice work!

-------------------------

smellymumbler | 2017-11-10 20:39:48 UTC | #14

Me too! Thanks a lot.

-------------------------

rku | 2017-11-12 08:50:14 UTC | #15

Just in case anyone wants to stalk the progress: now that CI builds are green i submitted a [PR](https://github.com/urho3d/Urho3D/pull/2170)

-------------------------

