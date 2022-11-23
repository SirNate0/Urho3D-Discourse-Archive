gunbolt | 2019-12-26 06:04:04 UTC | #1

I searched everywhere on google, discourse, there is absolutely no documentation/guide on how to build for webassembly or even android, mainly using Cmake_Gui.

So far I am only able to build for desktop projects using vs2015. Managed to build all the samples and also setup my own vs2015 projects.

Until today after years... still no proper docs/guide for android or webassembly build. I know urho3d can do these, but aside from links like these..

https://github.com/urho3d/Urho3D/wiki/Setting-up-Urho3D-on-Windows-with-Visual-Studio
https://github.com/urho3d/Urho3D/wiki/Setting-up-a-Project-(CMake)

These 2 links are the only ones that got me working with urho3d for desktop.

Until today I still have no clue how to build for the webassembly or android process, and every time I asked here, I get brushed off and told it's easy or sarcastically get my topic closed.

Why is there no proper guide/documentation similar to the 2 links above, but for webassembly or android build? 

It's immensely frustrating having to search and sieve through this discussion to find bits and pieces of information with many outdated and then getting brushed off for asking build questions.

Why is it so difficult to have articles/link similar to those 2 above on how to build/deploy for Android and webassembly ?

Many of us are on Windows and would like to build for Android or webassembly from those platform.

-------------------------

gunbolt | 2019-12-26 06:07:35 UTC | #2

On another note, when using CMAKE_Gui with the urho3d source, there're no options for emcc/emscripten generator even though I have wasm toolchains installed on my pc.

It's details like this that are making such a great library difficult to start out with or adopted. The build process needs to be detailed and documented brieftly for windows.

-------------------------

weitjong | 2019-12-26 07:58:37 UTC | #3

I think if you want some help from us, you will first have to learn your manner. Tone down a bit. The documentation for the build process for all the supported platforms is on our main website [here](https://urho3d.github.io/documentation/HEAD/_building.html). It uses CMake CLI as oppose to CMake GUI, but if CLI is not your forte and you must do it using GUI then for Web build you have to remember to apply the corresponding CMake ToolChain file at the very beginning in the GUI before you actually hit the configure & generate button. For Gradle/Android, you have to use CLI for now or using IDE like Android Studio or IntelliJ.

Cheers.

-------------------------

gunbolt | 2019-12-26 14:26:22 UTC | #4

The documentation is hopeless and lengthy and does not include CMAKE_Gui (Inconsistent platform targets). I am sorry but this is not the way to encourage people to try out urho3d. The build process is tedious and very cumbersome compared to the 2 links I showed. Also it's for 1.8 (For android build) and nothing for the 1.7.1 release. I'll have to give urho3d the skip again until a better process/documentation comes up for webassembly and android build. I am really sorry if I sound 'offensive' to you guys but really, this engine has a lot of potential but the documentation and build process is just abysmal. The build process for VS2015 is acceptable to me but all that fiddling needed for command line tools is just too much work to get it compile for non-desktop.

And yes, I tried webassembly build with cmake_emscripten and latest installed at d:\emsdk. Ran emsdk_vars.bat and set the EMSCRIPTEN_ROOT_PATH env variable and still end up with this


--------------------------------------------------------------------
D:\urho3d\Urho3D-1.7.1>cmake_emscripten ..\Urho3D-1.7.1-WASM
CMake Error at CMake/Toolchains/Emscripten.cmake:68 (message):
  Could not find Emscripten cross compilation tool.  Use EMSCRIPTEN_ROOT_PATH
  environment variable or build option to specify the location of the
  toolchain.  Or use the canonical EMSCRIPTEN environment variable by calling
  emsdk_env script.
Call Stack (most recent call first):
  C:/Program Files/CMake/share/cmake-3.8/Modules/CMakeDetermineSystem.cmake:88 (
include)
  CMakeLists.txt:39 (project)
-----------------------------------------------------

Then I search for the error message on google and got to this link.

https://discourse.urho3d.io/t/emscripten-build-error/1304/4

It seems this is a 2 year old problem and your advise is literally 'you're on your own if you're using windows'.

Sad, but that is the state of urho3d. If you're not a linux user, we can't help you.

-------------------------

weitjong | 2019-12-26 15:09:09 UTC | #5

May I ask have you successfully build anything else with Emscripten and Gradle?

-------------------------

gunbolt | 2019-12-26 15:28:27 UTC | #6

I can run emcc fine to build a wasm binary for testing with html. I've only used gradle from within android studio. Right now I only bother with the webassembly build with urho3d. Previous it was an older emscripten that compiled and crashed halfway due to asm2wasm.exe failure, so I deleted the whole emsdk and reinstalled as per instructions at https://emscripten.org/docs/getting_started/downloads.html

This new version can build my own sample projects fine but when using the same steps with urho3d cmake_emscripten.bat it actually is no longer able to find the compiler even after running emsdk_vars.bat or setting the environment variable it wants to point to the emsdk folder

-------------------------

Modanung | 2019-12-27 00:48:00 UTC | #7

[quote="gunbolt, post:4, topic:5784"]
Sad, but that is the state of urho3d. If you’re not a linux user, we can’t help you.
[/quote]
I believe the statement to be untrue and unfair to the community. Nobody is denied support based on their operating system, and one should simply not *expect* solutions to platform-specific problems to come from people running a different OS than yourself.

-------------------------

JTippetts | 2019-12-27 00:22:16 UTC | #8

The OP does have a point. I've been developing a web game lately, and I've had my share of bumps and bruises. Between Emscripten's 'way' of doing things, Urho3D's 'way' of doing things, and the relative complexity of the process, it's difficult to know why something breaks, who is at fault, and how to fix it. That's not necessarily Urho3D's fault, but I don't think Urho3D makes it any easier either.

I've been doing a lot of fiddling with vanilla Urho3D, as well as the rbfx fork of it, and to this date I have never gotten either one to successfully build using Emscripten on Windows. I've attempted each one numerous times, but I always meet some point of failure. I can get them to build under Linux, using Linux for Windows, but as far as using a plain Windows build, no success.

@gunbolt You never said exactly what you specify for EMSCRIPTEN_ROOT_PATH, so I don't know if this is your problem, but make sure you are setting the correct value for this. If your emsdk install is d:\emsdk and you are using the latest emscripten build, then the proper value would be d:\emsdk\upstream\emscripten. If you specify this correctly, it should find the tools, but if you just specify the root directory, d:/emsdk, then it will fail.

I usually do my web building on Linux for Windows, but I just gave it a go on Windows again with all latest (fresh pull of Urho3D, fresh install of emsdk latest) and it configured/generated okay for me. However, while configuring worked okay, I ran into some compilation errors building SDL. I'll dig into those a bit further, but it's just more evidence, to me at least, that web builds aren't quite 'there' yet.

For the curious: the compilation errors I ran into this time around were in SDL_cpuinfo.c, line 462, with the error "implicit declaration of function 'sysctlbyname' is invalid in C99'. If I pass SDL_CPUID=0 on the command line when invoking cmake, it gets past that but then it chokes with a similar error compiling SDL_string.c at line 592: 'implicit declaration of function '_strrev' is invalid in C99'. I'm going to do a little more digging around, but I'll probably file an issue if I can't figure it out.

Out of curiosity, I did a fresh pull and build under Linux and got the same errors, so I'll go ahead and submit an issue.

-------------------------

weitjong | 2019-12-27 01:39:41 UTC | #9

I believe part of the problem is that, Emscripten itself is a moving target and unlike other true compiler toolchain, latest version may actually break the build in an unexpected ways. For Web build, you would be better of using a known good version from your experiment or use the same version as CI. Unless of course you know what you are doing, installing latest all the time and capable to fix what break next.

-------------------------

JTippetts | 2019-12-27 03:14:30 UTC | #10

@weitjong The last version of Urho3D I've been able to successfully build, and the one that I'm using for my game, is your personal fork. I haven't been able to build Urho3D master for web for quite some time. Whether it's something I'm doing wrong somehow, or what, I couldn't say. My Windows emsdk is at latest as of today, but I didn't update my Linux emsdk and it is still at 1.39.0. It can build your fork but it can't build latest master from Urho3D. So something, somewhere, is different and I just can't say what it is because I don't really understand the system. I've actually set a deadline for myself for figuring it out by 3 months from now, and if I don't have the build process at least somewhat reliable I plan on evaluating other platforms such as Godot. I don't really want to invest a whole lot more time into something that I can't trust to not fall apart some time down the road, and be unable to fix it.

Edit: Correction, I'm using an older version of your personal fork, from just before the SDL 2.10 update was merged into master. Pulling your latest right now to see if it still builds.

Second Edit: So, @weitjong 's fork still builds okay for me, but Urho master does not. Going to update the issue I posted with some additional info.

-------------------------

gunbolt | 2019-12-27 03:06:09 UTC | #11

Doesn't matter what I set EMSCRIPTEN_ROOT_PATH. I set it according to your suggestions. Also ran emsdk_env.bat  and still go the same problems. Previously it was able to build halfway using older version of emscription (1.37 something). But the current emcc 1.39.5 wouldn't build. The older version will give me asm2wasm.exe build error crash which was why i updated to this version.

-------------------------

weitjong | 2019-12-27 03:30:51 UTC | #12

That fork is for personal experiment only but if/when the changes are good then the changes will be merged to URHO3D master branch. However, I had to stop what I was doing because of my eyes problem. One day I may have to stop doing what I like to do all together. If I recall it correctly that fork only has two or three commits ahead of master, so it should be easy for you to get a diff. I haven’t finished what I intend to do though.

It is not a rocket science. When you change to latest compiler toolchains, be it Xcode or VS or Emscripten, and thing just does not work anymore, there is no harm to upgrade to the latest CMake as well. I believe I got lucky that last time and after bumping the minimum required CMake version then it builds again.

-------------------------

JTippetts | 2019-12-27 15:19:34 UTC | #13

@weitjong Looks like bumping the required CMake version does the trick. Cool. But it kind of is rocket science, in a way. Because why does that work? Why do you say you 'got lucky'? That's my point in saying that this system is kind of complex and hard to understand. Again, though, I understand it's not really Urho3D's fault.

@gunbolt Are you making sure to delete CMakeCache when you try new things? In fact, to be sure, you might want to completely nuke the old build tree when you try again. Otherwise, it may remember the incorrect paths even if you try to change them. Because, if you specify the correct path, and your emsdk is correctly set up, then it should work.

-------------------------

johnnycable | 2019-12-27 15:35:24 UTC | #14

Both Android and EMSC are two of the most convoluted platform out there for building and upkeeping. Forums are full of questions about how to build on Android. Once you resolve the problems and find a setup, keep it dear. That doesn't anyway shell you for future problems, let alone debugging that on a browser.
Really, it's awkward. Too much a low level and convoluted pipeline. If you care for times and sanity of mind, you want to use javascript for web games.

-------------------------

weitjong | 2019-12-27 16:27:39 UTC | #15

You have observed the same thing as me that the Web build using LLVM backend and old CMake resulted in wrong detection result. Some of the functions passed the test when they shouldn't. Then I figured out it was caused by old CMake itself, giving a wrong a compiler flag, which interestingly only LLVM backend got tripped by it. Once I concluded that, it is not difficult to understand why my next step is to see if newer CMake version has fixed this bug. I am lucky because it has. Anyway, I am glad you have your Web build working again.

-------------------------

gunbolt | 2019-12-28 04:47:43 UTC | #16

Nopes, doesn't work. Using Cmake version 3.16.2 on urho3d 1.7.1 and I made sure to delete the build target folder every time. I assume this target folder is the one that holds the cache file. Setting both EMSCRIPTEN_ROOT_PATH=D:\emsdk\upstream and also running emsdk_env.bat does not work. Still same issue. Of course this is on a windows machine.

-------------------------

tni711 | 2019-12-28 05:18:19 UTC | #17

You may try to set the 
EMSCRIPTION_ROOT_PATH=D:\emsdk\emscription 
instead of the upstream folder.

That is how I get it working in my Linux platform on Urho3d 1.7.1 with emscripton sdk 1.38.31. Not sure it works the same for Windows.

-------------------------

gunbolt | 2019-12-28 05:50:36 UTC | #18

That folder doesn't exist on my 1.39.5 emsdk.

-------------------------

gunbolt | 2019-12-28 06:04:09 UTC | #19

Ok it seems the correct env is EMSCRIPTEN_ROOT_PATH=d:\emsdk\upstream\emscripten   on windows machine. It's running now. EMSDK_ENV.bat no longer works. You must set the root path with the new folder structure.

-------------------------

gunbolt | 2019-12-28 06:13:28 UTC | #20

ok ran mingw32-make and received loads of compile errors. Wooo too tired to play with this anymore. I'll just stick to babylon.js for web html5 games. Here're caps of 'some' of the error messages.

-------------------------------------------------------------------------------------------------------------------------------------------

D:\urho3d\Urho3D-1.7.1\Source\ThirdParty\SDL\src\stdlib\SDL_string.c:663:12: err
or:
      implicit declaration of function 'itoa' is invalid in C99
      [-Werror,-Wimplicit-function-declaration]
    return itoa(value, string, radix);
           ^
D:\urho3d\Urho3D-1.7.1\Source\ThirdParty\SDL\src\stdlib\SDL_string.c:663:12: war
ning:
      incompatible integer to pointer conversion returning 'int' from a function

      with result type 'char *' [-Wint-conversion]
    return itoa(value, string, radix);
           ^~~~~~~~~~~~~~~~~~~~~~~~~~
D:\urho3d\Urho3D-1.7.1\Source\ThirdParty\SDL\src\stdlib\SDL_string.c:673:12: err
or:
      implicit declaration of function '_uitoa' is invalid in C99
      [-Werror,-Wimplicit-function-declaration]
    return _uitoa(value, string, radix);

-------------------------

weitjong | 2019-12-28 07:04:05 UTC | #21

It seems you never read other posts in this thread carefully.

-------------------------

JTippetts1 | 2019-12-28 07:11:18 UTC | #22

Make sure you actually update the minimum required version for CMake inside the various CMakeLists.txt files. Just updating your installed version wont be enough, because that minimum required version holds it back. Those are the same kinds of errors I was getting.

I have a PR for updating that min version if you want to see what has to be updated. https://github.com/urho3d/Urho3D/pull/2567

I was able to get it to build on both Windows and Linux at this required version level.

-------------------------

gunbolt | 2019-12-28 07:33:47 UTC | #23

No, I am NOT gonna do that. That's ridiculous. I am not wasting my time scavenging through the entire source tree to find and modify every single of the cmakelists.txt file just to get this to build. This is a hideous and abysmal way to use this sdk. 

Bad enough these aren't in the documentation, now I have to manually dig out all the txt files in the source tree and manually find and edit these values just to get this to build? Come on. 

There're a total of 97 Cmakelists.txt files in the urho3d source. No way am I going to manually edit every single one of them just to get this to compile/build only to end up with more other kinds of errors.

This is a horrible way to get working. 

Over and out, I am done with this sdk. Looks like I will be going on a hiatus from this sdk again.

-------------------------

JTippetts1 | 2019-12-28 08:14:28 UTC | #24

That's cool. There are easier ways V to build web games.

-------------------------

weitjong | 2019-12-28 08:55:51 UTC | #25

I found it funny that you ask for help but then when the help come you don't want to get your hand dirty.

-------------------------

weitjong | 2019-12-28 08:56:41 UTC | #26



-------------------------

