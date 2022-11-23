OvermindDL1 | 2017-01-02 01:01:18 UTC | #1

I read elsewhere that you had an issue with cross-compiling in CMake because I think it was something about needing to compile the tools for the native system but cross-compile the resultant project?  In as far as I have messed with it that has not been a problem for many years.  It should just have the root CMakeLists.txt in the *root* directory, subdirectory imports for the main project, tools, etc..., each of which can have their setups including forcing the local system for certain projects or using a toolchain file to specify, say, android for others.  What is the problem that was had?

-------------------------

weitjong | 2017-01-02 01:01:18 UTC | #2

The complication is mainly coming from LuaJIT library. We have adapted the LuaJIT original Makefile to our CMake build scripts. The original LuaJIT Makefile can build host tool "buildvm" using native toolchain at the same time it builds the cross-platform target library using the cross-compiling toolchain. I don't know whether CMake has changed since then but at the time I tackled this, I found CMake to be:

[ul][li] incapable of configuring a host build when it is being invoked with a cross-compiling toolchain[/li]
[li] incapable of changing toolchain or using several toolchains in a single build[/li][/ul]
I have checked a few CMake build scripts from other projects that attempt to build LuaJIT library and none of them meet our need. Most throw away so much logic from the original Makefile that they either work only in one platform or resort to some forms of hard-coding. In the end I decided to write the CMake adaptation of the original LuaJIT Makefile from scratch myself. At least our implementation works across all the platforms supported by Urho3D, barring iOS platform as there is no point to build it for this platform. In fact the adapted CMake build script supports all the platforms supported by LuaJIT itself (PS3/4, XBox, PPC, etc). The only thing that is not nice about it is this, it always assumes the host tool location where it can find the "buildvm" to be in "Bin" directory regardless and that the tool itself must have been built natively prior to cross-compiling build. Note that the "buildvm" tool is a different binary for each targeted platform.

You are welcome to contribute if you think there is better way to do this or if you can improve on top of what we have.

-------------------------

OvermindDL1 | 2017-01-02 01:01:19 UTC | #3

Ah!  In that case there are two main ways, one is fully in-cmake but is a pain and not generally recommended due to the pain, the other way is to use CMake's [url=http://www.cmake.org/cmake/help/v3.0/module/ExternalProject.html]ExternalProject[/url] built-in system, which was added in 2.6 or 2.8 or so.  Basically just have multiple projects, like tools that should always be built for the host OS you can put in one project, things that should build for potentially multiple things in another.  From your main project just ExternalProject_Add and pass in the arguments you need.  So for example, one way it can be set up is to have your 'main' project (which really really *really* badly should be a CMakeLists.txt in the *root* of the git tree, even if it just starts immediately going to a subdirectory like Source) be the platform that you want to build to, the TARGET platform.  Have it ExternalProject_Add the tools that need to be run on the local HOST system, when it builds you can then ExternalProject_Get_Property to get the variables from that external project, such as the location of the binary to use in a build step elsewhere say for code generation or atlas generation or whatever you need, or bring in include files and the library path to link to (well not that part for cross-compiling obviously).  Once you bring in the variables just name them whatever you want and use them as normal, as if they are just in your project.  With ExternalProject Cross-Compiling with host-only tools became *much* easier.  :slight_smile:

It 'should' be completely possible to do an entire and complete CMake build system nowadays without an overuse of Macros either, such as the output 'Bin' directory really should not exist, the resultant binaries and Data directories should be in the build directory for if people want to test, and the Install commands should let the user install it where-ever they wish.  Then with proper CTest and CPack support you could make travis just fly and make installers that are far easier to include in other projects.  Plus if the CMake build follows proper standards (such as generating the definition file that points to the local library, data, configuration vars, etc... of the build) then bringing in Urho3D into an external project without needing to pre-compile or anything would be utterly simple.  It would remove all the non-standard steps in the build process for usual systems and for generating the android bits then something like [url]https://code.google.com/p/android-cmake/[/url] would simplify that work as well since android is so... javaish.  :slight_smile:

At that point then out-of-source builds would be fully supported and Urho3D would fit naturally in to any normal CMake ecosystem, and in fact if done properly then they could just ExternalProject_Add in Urho3D in to their project to have their project auto git clone it, compile, and use the resultant file.  A few helpers for android would still be useful to have of course so a custom cmake command can do the android build for the entire of the project.

-------------------------

weitjong | 2017-01-02 01:01:20 UTC | #4

Thanks for the tips. I agree that "ExternalProject" feature looks promising. I have tried many approaches then but not this one yet. It would work IF the the external project is able to be configured and built without the interference of the cross-compiling toolchain. Having said that, in my earlier post I have simplified the actual dependency situation. The building of "buildvm" host tool is not really external to the project as it also "depends" on the cross-compiling build to provide the architecture information of the target platform. This is exactly the reason why the generated tool binary is unique for each target platform. In original LuaJIT Makefile, it does something like these (again I may have simplified a few things here):

[ol][li] Detect the architecture of the target platform using cross-compiling toolchain[/li]
[li] Use the detected architecture information to configure and build the "buildvm" tool using native toolchain[/li]
[li] While building the library using cross-compiling toolchain, call the "buildvm" tool natively to generate more source files on the fly.[/li][/ol]
The original LuaJIT Makefile does this elegantly. I doubt the "ExternalProject" could solve this inter-dependency (Step 1 and 2) as nicely. Step 3 is a non-issue.

Need further investigation. Would you like to take this on?

[quote="OvermindDL1 "]It 'should' be completely possible to do an entire and complete CMake build system nowadays without an overuse of Macros either, such as the output 'Bin' directory really should not exist, the resultant binaries and Data directories should be in the build directory for if people want to test, and the Install commands should let the user install it where-ever they wish. Then with proper CTest and CPack support you could make travis just fly and make installers that are far easier to include in other projects. Plus if the CMake build follows proper standards (such as generating the definition file that points to the local library, data, configuration vars, etc... of the build) then bringing in Urho3D into an external project without needing to pre-compile or anything would be utterly simple. It would remove all the non-standard steps in the build process for usual systems and for generating the android bits then something like [code.google.com/p/android-cmake/](https://code.google.com/p/android-cmake/) would simplify that work as well since android is so... javaish.  :slight_smile:[/quote]
I have no more further comments on all these points as they have been discussed before in other threads. Perhaps only these, we use our macro to save repeating ourselves when configuring our samples target (and when performing bug fixing we only do it in one place), we don't force people to do SDK installation, please contribute to make it better.

-------------------------

OvermindDL1 | 2017-01-02 01:01:20 UTC | #5

[quote="weitjong"]Thanks for the tips. I agree that "ExternalProject" feature looks promising. I have tried many approaches then but not this one yet. It would work IF the the external project is able to be configured and built without the interference of the cross-compiling toolchain. Having said that, in my earlier post I have simplified the actual dependency situation. The building of "buildvm" host tool is not really external to the project as it also "depends" on the cross-compiling build to provide the architecture information of the target platform. This is exactly the reason why the generated tool binary is unique for each target platform. In original LuaJIT Makefile, it does something like these (again I may have simplified a few things here):

[ol][li] Detect the architecture of the target platform using cross-compiling toolchain[/li]
[li] Use the detected architecture information to configure and build the "buildvm" tool using native toolchain[/li]
[li] While building the library using cross-compiling toolchain, call the "buildvm" tool natively to generate more source files on the fly.[/li][/ol]
The original LuaJIT Makefile does this elegantly. I doubt the "ExternalProject" could solve this inter-dependency (Step 1 and 2) as nicely. Step 3 is a non-issue.

Need further investigation. Would you like to take this on?[/quote]
Indeed ExternalProject is completely separate, it spawns a new CMake process and all to handle it, you only pass in the environment that is explicitly stated.  The style could handle those three steps fairly easily actually.

I might have time sometime, but generally keeping pretty busy.  If I can though.

-------------------------

weitjong | 2017-01-02 01:02:21 UTC | #6

Hi, just want to let you know that host-tool building while cross-compiling Urho3D project is now possible. The ExternalProject_Add and cross-compiling are made for each other to solve the host-tool building problem.

-------------------------

OvermindDL1 | 2017-01-02 01:02:42 UTC | #7

[quote="weitjong"]Hi, just want to let you know that host-tool building while cross-compiling Urho3D project is now possible. The ExternalProject_Add and cross-compiling are made for each other to solve the host-tool building problem.[/quote]
Indeed, and so I noticed on the massive merge I did to update my local Urho3D today.  Also noticed many other very nice changes!  Thank you much!  ^.^

-------------------------

