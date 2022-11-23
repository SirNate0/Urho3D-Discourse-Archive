atai | 2017-01-02 01:09:08 UTC | #1

A question:  does Urho3d have to be built first before it can be used as an external library in another cmake based project?  I mean can I put the Urho3d git repo as a git submodule inside my project''s git repo and somehow let my project's cmakelist.txt drive the build of the URho3d tree together as part of the build process of my project?  

The documentation for Urho 1.5 says URHO3D_HOME needs to point to the Urho3d build tree, which seems to imply that Urho3d has to be built first somewhere before projects using it can be built.  In my project setup as described above, I have the full source tree of Urho3d inside my project's source tree, but I cannot set URHO3D_HOME to point to a Urho3d source tree, or a subdirectory of it.  It is convenient to be able to build everything via a single cmake invocation (and then make, xcode, etc.).  Any way to get around this?

Thanks

-------------------------

weitjong | 2017-01-02 01:09:08 UTC | #2

It is possible. There was even a time when there was no Urho3D library target so users would have to build using the source code directly into their projects. Having said that, our current development direction is to keep things modularized. And yes, it means we have to build Urho3D as a library first and to use it as dependency, even for internal targets in our own Urho3D project. Of course there is nothing prevent you from doing thing the old way, however,  that use case is not being tested or well supported anymore.

-------------------------

namic | 2017-01-02 01:09:34 UTC | #3

I really dislike the idea of having to install an SDK or a library to start working on my projects. That's why i usually add libraries as submodules on my git projects and use CMake to statically link them to my application. Here's a similar workflow:

[github.com/Polytonic/Glitter](https://github.com/Polytonic/Glitter)

Bullet, Assimp, GLFW and others are added as submodules and, when i CMake my project, they get built and linked together. Much easier for everyone involved, self-contained and modular. Anyway, i've been looking for a way to do this with Urho without any luck. The whole building process seems very complex. Is there any way to achieve a similar workflow with this engine?

-------------------------

thebluefish | 2017-01-02 01:09:34 UTC | #4

I've been running into issues with this as well. I spent a good week trying to get CMake to play nicely with Urho3D as a dependency for my project. I settled with generating my projects separately with the include/lib added in manually. Not the best solution, but it works. I would like to see a CMake setup with Urho3D as a dependency, though.

-------------------------

atai | 2017-01-02 01:09:34 UTC | #5

related discussion [topic1701.html](http://discourse.urho3d.io/t/embedding-the-engine-as-a-submodule-and-cmake-module/1636/1) (Moderator note: topic is merged)

-------------------------

weitjong | 2017-01-02 01:09:34 UTC | #6

I think I have understood atai's original question wrongly. When I first read it, somehow I understood it wrongly as the Urho3D source code would be used directly without using its CMake build system in the downstream project. However, if what you want to achieve is to let your own CMake build system to add Urho3D as a sub-directory by itself via CMake's add_subdirectory() command then I think that is perfectly valid use case that we need to support. I think there are only a few places that we need to tweak to make this works.

-------------------------

atai | 2017-01-02 01:09:35 UTC | #7

[quote="weitjong"]I think I have understood atai's original question wrongly. When I first read it, somehow I understood it wrongly as the Urho3D source code would be used directly without using its CMake build system in the downstream project. However, if what you want to achieve is to let your own CMake build system to add Urho3D as a sub-directory by itself via CMake's add_subdirectory() command then I think that is perfectly valid use case that we need to support. I think there are only a few places that we need to tweak to make this works.[/quote]


Yes that was what I meant.  Thanks in advance if this can be easily done!

-------------------------

TheComet | 2017-01-02 01:09:36 UTC | #8

Another way you can approach this problem is to use CMake's [url=https://cmake.org/cmake/help/v3.0/module/ExternalProject.html]ExternalProject[/url] module for automatically downloading, building, and installing Urho3D locally.

-------------------------

weitjong | 2017-01-02 01:09:37 UTC | #9

Yes, our build system has support building/installing Urho3D using ExternalProject_Add() for a while now. Still, that is a different use case than what being asked in this topic. With add_subdirectory(), the downstream projects can see Urho3D library as an internal CMake target.

-------------------------

namic | 2017-01-02 01:09:37 UTC | #10

Exactly, and that's key in improving the build workflow, specially when you're on a big team and with a solid CI/CD. People just have to clone the project, update the submodules and run Cmake. And our Cmake project is able to customize everything. That's our workflow for everything: both external libraries (bullet, glfw, assimp, etc) and our internals (game logic is in a library, internal utilities, rendering lib, etc).

-------------------------

weitjong | 2017-01-02 01:09:38 UTC | #11

[quote="namic"]Exactly, and that's key in improving the build workflow, specially when you're on a big team and with a solid CI/CD. People just have to clone the project, update the submodules and run Cmake. And our Cmake project is able to customize everything. That's our workflow for everything: both external libraries (bullet, glfw, assimp, etc) and our internals (game logic is in a library, internal utilities, rendering lib, etc).[/quote]

I think you are aware that Urho3D has "embedded" itself a number of 3rd-party libs that it depends on including Bullet. So while working in enabling the Urho3D's build system to allow itself to be embedded by downstream project, I suppose we won't change this internal dependency configuration. In other words, when you include Urho3D then you probably should exclude Bullet from being build separately again.

-------------------------

TheComet | 2017-01-02 01:09:38 UTC | #12

[quote="weitjong"]Still, that is a different use case than what being asked in this topic.[/quote]

How so? The OP asked:
[quote="atai"]somehow let my project's cmakelist.txt drive the build of the URho3d tree together as part of the build process of my project?[/quote]

ExternalProject achieves exactly what the OP wants and what namic said:
[quote="namic"]People just have to clone the project, update the submodules and run Cmake.[/quote]

Having Urho3D as an internal dependency in your project has its up- and downsides. For example, if you're using an IDE such as KDevelop or CLion that uses CMakeLists.txt for project files, it will try to index the entire Urho3D project. This increases loading times of the project. When building, it also takes longer because it has to check all of Urho3D's targets if they need to be updated. That can get quite annoying. Doesn't Urho3D rebuild script bindings every time CMake re-runs? So every time you add a new header/source file to your project, Urho3D will re-generate script bindings and re-generate documentation.

If you're using ExternalProject, the above problems are avoided, but it's a little more complicated to set up properly. The best way to set up ExternalProject is to have it download and install Urho3D in the binary directory somewhere, then when CMake runs a second time, have it look for Urho3D in the binary directory using find_package() instead. If Urho3D is found then you skip your ExternalProject_add() call and incremental builds from that point on get a lot faster than if you were to use ExternalProject_add() all the time.

In the end you should try out both methods and see what's best for your particular use-case.

-------------------------

weitjong | 2017-01-02 01:09:39 UTC | #13

Do not get me wrong. I am not saying using ExternalProject_Add() is bad. Both are valid use cases. Like you said, it really depends on what one project needs. We have fixed our build system about a year ago (I think) to support the ExternalProject_Add() use case, but at the moment our build system does not yet support the other use case. And this is what this topic is about. BTW, I have made this as a new issue in GitHub issue tracker so you can hope for its support sometime in the near future.

-------------------------

TheComet | 2017-01-02 01:09:39 UTC | #14

Ah ok, thanks for making this clear!

-------------------------

thebluefish | 2017-01-02 01:09:42 UTC | #15

[quote="namic"]I really dislike the idea of having to install an SDK or a library to start working on my projects. That's why i usually add libraries as submodules on my git projects and use CMake to statically link them to my application. Here's a similar workflow:

[github.com/Polytonic/Glitter](https://github.com/Polytonic/Glitter)

Bullet, Assimp, GLFW and others are added as submodules and, when i CMake my project, they get built and linked together. Much easier for everyone involved, self-contained and modular. Anyway, i've been looking for a way to do this with Urho without any luck. The whole building process seems very complex. Is there any way to achieve a similar workflow with this engine?[/quote]

I just took a look at this, and I think having a version of Glitter/Chlorine with Urho3D is something newbies could [b]really[/b] use. I know that many of us gave up on CMake for our own projects a long time ago, and just use our own project files instead.

-------------------------

INait | 2017-01-02 01:09:49 UTC | #16

Hi gyus,

I'm a newbie in Urho, trying to learn it from scratch for the last month, so don't punch me too hard if I'm saying something obvious.
After some experiments I found the most convenient way working on a project with Urho is using it as external lib, but with some clarification:

1) I've created git repo with Urho3D as a submodule and a MyProject directory on the same level.
2) In MyProject I've got CMake config suitable for building my project, mostly like it is on wiki, but specified for MyProject. Everithing else made like it's posted on wiki page "External library".
3) On the root level I've created scripts for build trees generating, thus I generate Urho3D lib and a project depending on it.
So the root directory looks like:
    - Urho3D(submodule)
    - MyProject
    - UrhoBuildTree
    - ProjectBuildTree
    - a bunch of build generating scripts

It works like a charm in windows and linux builds, and simple to maintain.

-------------------------

namic | 2017-01-02 01:10:09 UTC | #17

What do you mean by build trees? You're specifying, by hand, the Urho source files to build on your own cmake?

-------------------------

rku | 2017-01-02 01:11:50 UTC | #18

I did some work to allow using Urho3D via cmake add_subdirectory(). Check it out: [github.com/r-ku/Urho3D/tree/cma ... bdirectory](https://github.com/r-ku/Urho3D/tree/cmake-add-subdirectory)

Sample CMakeLists.txt of parent project:
[code]cmake_minimum_required(VERSION 3.5)
project(Urho3D)

if (COMMAND cmake_policy)
    cmake_policy (SET CMP0003 NEW)
    if (CMAKE_VERSION VERSION_GREATER 2.8.12 OR CMAKE_VERSION VERSION_EQUAL 2.8.12)
        # INTERFACE_LINK_LIBRARIES defines the link interface
        cmake_policy (SET CMP0022 NEW)
    endif ()
    if (CMAKE_VERSION VERSION_GREATER 3.0.0 OR CMAKE_VERSION VERSION_EQUAL 3.0.0)
        # Disallow use of the LOCATION target property - therefore we set to OLD as we still need it
        cmake_policy (SET CMP0026 OLD)
        # MACOSX_RPATH is enabled by default
        cmake_policy (SET CMP0042 NEW)
    endif ()
endif ()

set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -std=c++11")

set (CMAKE_MODULE_PATH ${CMAKE_SOURCE_DIR}/Urho3D/CMake/Modules)
add_subdirectory (Urho3D)
find_package(Urho3D)
include_directories (${URHO3D_INCLUDE_DIRS})

set(SOURCE_FILES Sample.h Sample.inl StaticScene.h StaticScene.cpp)
add_executable(_TestApp ${SOURCE_FILES})
target_link_libraries(_TestApp ${URHO3D_LIBRARIES} z pthread)
[/code]

There is one shortcoming though - main project still has to be called "Urho3D". See project(Urho3D) in sample file. Reason for this is that urho's build system uses CMAKE_PROJECT_NAME to check if you are building urho or linking to it. Sounds simple enough but in practice i failed to figure out how exactly to work-around this requirement. Any advice from people who are better familiar w/ urho's build system would be greatly appreciated. In the meantime this is good compromise.

-------------------------

weitjong | 2017-01-02 01:11:50 UTC | #19

I don't think it will work for initial case. After the add_subdirectory() call, the library does not exist yet, so the next find_package() command may not be able to find Urho3D library. At the time I wrote my last comment, I have thought through it once and I was clearer then than now of what it needs to be done.  :wink:

-------------------------

rku | 2017-01-02 01:11:51 UTC | #20

But it does work just fine. This is because FindUrho3D.cmake takes care of this case already. As long as project name is "Urho3D". Reason for this is that "PROJECT_NAME STREQUAL Urho3D" is scattered all around urho's cmake scripts. Now i tried to substitute all instances of that comparison with custom-set variable. It works fine but as soon as project name changes - everything breaks. Be great if someone with better knowledge of build scripts (like you) could try my patch and script i posted above while changing project name in that script. I have a feeling we are no that far from a solution. Unfortunately cmake does not bend to my will..

-------------------------

weitjong | 2017-01-02 01:11:51 UTC | #21

Ah, I see. But it is not the intended use, I am afraid. We have mentioned in the documentation that "Urho3D" project name is reserved.

-------------------------

rku | 2017-01-02 01:11:51 UTC | #22

Exactly, thats why we need to fix it. It was already mentioned elsewhere by you that add_subdirectory() is valid usecase and urho should support it. And after my changes i think we are really close. Its just i dont quite know how exactly build system misuses project name so i cant root it out completely.

Basically using project(Urho3D) slaps engine into thinking "oh im building myself" and then it does the right thing that we want when using add_subdirectory().
What we need is basically an option like URHO3D_SDK=0 that would do exactly the same.
Now if URHO3D_SDK is not specified it could be auto-detected using project name, but if it is specified it should not overwrite this option.
Then we could set(URHO3D_SDK 0) / add_subdirectory(Urho3D) and it would do right thing.

So.. Willing to lend a hand?

-------------------------

weitjong | 2017-01-02 01:11:51 UTC | #23

The "Urho3D" is reserved because there are a number internal processes being configured based on the project and/or target name matches this reserved words. You are on your own if your own project does not observe this. If you want to abuse Urho3D build system this way, you may as well just call the add_subdirectory() for your own targets in one of the sample or tool directories (you can create a new directory if you want to) and put your own code there. I am not saying this is the recommended way though. We have already added this issue into our GitHub issue tracker. Any of us, including yourself is welcome to tackle the issue in his/her own free time. At the moment I have other priorities. I could give the general direction or shout if I believe the approach is wrong, of course.

-------------------------

rku | 2017-01-02 01:11:51 UTC | #24

I think we are having bit of miscommunication here.

Yes - i know we [b]should not[/b] use Urho3D as project name. But this hack makes add_subdirectory() work. However i want to get rid of this hack.

Like you said build system uses project name in various places like:
[code]CMAKE_PROJECT_NAME STREQUAL Urho3D[/code]

What i tried:
[code]
if (NOT DEFINED URHO3D_SOURCE_BUILD)
    if (CMAKE_PROJECT_NAME STREQUAL Urho3D)
        set (URHO3D_SOURCE_BUILD 1)
    else ()
        set (URHO3D_SOURCE_BUILD 0)
    endif ()
endif ()
[/code]

Then i replaced all instances of [b]CMAKE_PROJECT_NAME STREQUAL Urho3D[/b] with [b]URHO3D_SOURCE_BUILD[/b].

So far so good, everything builds just fine.

Then i changed set [b]project(Not-Urho3D)[/b] - everything falls apart.

So my question is in what other non-obvious ways CMAKE_PROJECT_NAME is used?

-------------------------

weitjong | 2017-01-02 01:11:51 UTC | #25

My only advice, don't go there. IMHO, this is not the place where it will make or break the use case of embedding. I wish I have more time to explain. All I can say is this. We have a number things that we need to do or fix in the current build system (you can see them in GitHub issue trackers). A few of them are related to each other, i.e. you cannot fix one without first fixing the other one first. I strongly believe this issue depends on the other.

-------------------------

rku | 2017-01-02 01:11:51 UTC | #26

I see. I looked through buildsystem-tagged issues and there was nothing immediately obvious i could throw myself at. Maybe you would be willing to accept these changes as PR then? It is not a complete solution but still an improvement overall making build system less likely to break.

-------------------------

weitjong | 2017-01-02 01:11:52 UTC | #27

To put it bluntly, probably I would not merge it as it is. I have already explained that the "Urho3D" is a reserved name and downstream projects should/must be able to use whatever other project name that they want to use.

-------------------------

namic | 2017-01-02 01:11:52 UTC | #28

His PR has nothing to do with changing the reserved name. It's just a way of allowing developers to neatly include Urho as a dependency on their projects, making the build process much easier. It's already hard to live in C++ without module, and the small amount of modularity that CMake provides, Urho is currently denying to us.

-------------------------

weitjong | 2017-01-02 01:11:52 UTC | #29

What I said in my last comment was, I probably won't merge it AS IT IS. There are other changes required to make it work without the caveat.

-------------------------

rku | 2017-01-02 01:11:53 UTC | #30

forget Urho3D being reserved project name. My PR does not encourage it and by no means we should suggest using project name Urho3D. However it is some work towards allowing add_subdirectory(). If you reviewed it you would see it basically substitutes CMAKE_SOURCE_DIR with URHO3D_SOURCE_DIR. But hey if you prefer doing same thing yourself (which is essentially double work) and waste time then... /shrug :slight_smile:

-------------------------

rku | 2017-01-02 01:12:02 UTC | #31

I did some more experiments with this idea and this is what i have found.

We can use [b]ExternalProject_Add()[/b] to add Urho3D to our own project. No changes to Urho3D build system are required. However we must not include Urho3D-CMake-common.cmake because it insists on calling find_package() which i think is very bad idea. Since it is external project and we cant call find_package() because sdk is not built until we actually build our project we must set up include and library paths ourselves as well as linking using -lUrho3D as opposed to just adding target dependency. Setting up proper dependencies to ensure that Urho3D target is built first is also vital. This is roughly the build script you would need to make use of ExternalProject_Add():

[code]
ExternalProject_Add(Urho3D
    SOURCE_DIR ${CMAKE_SOURCE_DIR}/dep/Urho3D
    CMAKE_ARGS -DCMAKE_INSTALL_PREFIX=${CMAKE_BINARY_DIR} -DURHO3D_C++11=1 -DURHO3D_SAMPLES=0 -DURHO3D_LIB_TYPE=SHARED
               -DURHO3D_USE_LIB_DEB=1 -DURHO3D_PCH=0 -DCMAKE_BUILD_TYPE=${CAKE_BUILD_TYPE}
               ${URHO3D_EXTRA_PARAMS}
    BUILD_COMMAND make -j8
    BINARY_DIR ${CMAKE_BINARY_DIR}/Urho3D-build
    INSTALL_DIR ${CMAKE_BINARY_DIR}
)

add_custom_command(TARGET Urho3D POST_BUILD
    COMMAND ${CMAKE_COMMAND} -E create_symlink ${CMAKE_SOURCE_DIR}/dep/Urho3D/bin/CoreData ${CMAKE_BINARY_DIR}/bin/CoreData
    COMMAND ${CMAKE_COMMAND} -E create_symlink ${CMAKE_SOURCE_DIR}/dep/Urho3D/bin/Data ${CMAKE_BINARY_DIR}/bin/Data
)

add_definitions (-DURHO3D_CXX11=1)
include_directories (
    ${CMAKE_BINARY_DIR}/include
    ${CMAKE_BINARY_DIR}/include/Urho3D
    ${CMAKE_BINARY_DIR}/include/Urho3D/ThirdParty
    ${CMAKE_BINARY_DIR}/include/Urho3D/ThirdParty/Bullet
    ${CMAKE_BINARY_DIR}/include/Urho3D/ThirdParty/kNet
    ${CMAKE_BINARY_DIR}/include/Urho3D/ThirdParty/Lua
    ${CMAKE_BINARY_DIR}/include/Urho3D/ThirdParty/SDL
    ${CMAKE_BINARY_DIR}/include/Urho3D/ThirdParty/SRB
)
link_directories (
    ${CMAKE_BINARY_DIR}/lib
    ${CMAKE_BINARY_DIR}/lib/Urho3D
)
[/code]

By now it is clear that we are long way from add_subdirectory(). Using external project could be a viable shortcut if Urho3D build system did not get in our way. Since it does we are stripped on some useful cmake macros provided by urho.

-------------------------

namic | 2017-01-02 01:12:49 UTC | #32

This doesn't seem to work. Here's my CMakeLists.txt:

[code]cmake_minimum_required(VERSION 3.1)
project(example)
include(ExternalProject)

set(CMAKE_CXX_STANDARD 11)
add_compile_options(-std=c++11)
add_definitions(-DURHO3D_CXX11=1)

ExternalProject_Add(Urho3D
    SOURCE_DIR ${CMAKE_SOURCE_DIR}/vendor/urho
    CMAKE_ARGS -DCMAKE_INSTALL_PREFIX=${CMAKE_BINARY_DIR} -DURHO3D_C++11=1 -DURHO3D_LIB_TYPE=SHARED
               -DURHO3D_PCH=0 -DCMAKE_BUILD_TYPE=${CMAKE_BUILD_TYPE}
               -DURHO3D_TOOLS=0 -DURHO3D_SAMPLES=0
               -DURHO3D_ANGELSCRIPT=0 -DURHO3D_LUA=1 -DURHO3D_LUAJIT=1 -DURHO3D_URHO2D=0
               ${URHO3D_EXTRA_PARAMS}
    BUILD_COMMAND make -j8
    BINARY_DIR ${CMAKE_BINARY_DIR}/Urho3D-build
    INSTALL_DIR ${CMAKE_BINARY_DIR}
)

add_custom_command(TARGET Urho3D POST_BUILD
    COMMAND ${CMAKE_COMMAND} -E create_symlink ${CMAKE_SOURCE_DIR}/vendor/urho/bin/CoreData ${CMAKE_BINARY_DIR}/bin/CoreData
    COMMAND ${CMAKE_COMMAND} -E create_symlink ${CMAKE_SOURCE_DIR}/vendor/urho/bin/Data ${CMAKE_BINARY_DIR}/bin/Data
)

include_directories(
    ${CMAKE_BINARY_DIR}/include
    ${CMAKE_BINARY_DIR}/include/Urho3D
    ${CMAKE_BINARY_DIR}/include/Urho3D/ThirdParty
    ${CMAKE_BINARY_DIR}/include/Urho3D/ThirdParty/Bullet
    ${CMAKE_BINARY_DIR}/include/Urho3D/ThirdParty/kNet
    ${CMAKE_BINARY_DIR}/include/Urho3D/ThirdParty/Lua
    ${CMAKE_BINARY_DIR}/include/Urho3D/ThirdParty/SDL
    ${CMAKE_BINARY_DIR}/include/Urho3D/ThirdParty/SRB
)
link_directories(
    ${CMAKE_BINARY_DIR}/lib
    ${CMAKE_BINARY_DIR}/lib/Urho3D
)

set(SOURCES src/main.cpp)
add_executable(${PROJECT_NAME} ${SOURCES})
add_dependencies(${PROJECT_NAME} Urho3D)
[/code]

main.cpp is just a copy-paste from [github.com/urho3d/Urho3D/wiki/First%20Project](https://github.com/urho3d/Urho3D/wiki/First%20Project)

The library is not linked at all. Is there any way of adding Urho3D as a dependency to my project? This sucks. :frowning:

-------------------------

weitjong | 2017-01-02 01:12:50 UTC | #33

No promise but the refactor-buildystem branch would eventually address this need. It will take time though. But I just want to be clear about one thing in this post. To me, "embedding the engine as a submodule" and "using engine with External_ProjectAdd" are two separate use cases. This thread is about the former, which is not yet supported. While the latter is/was working in the past. Perhaps once we have these use cases working in future then we should also include tests in the CI to ensure they stay in a working state. Perhaps also enhance our rake scaffolding task to support these two cases as well. In the mean time though, unless you are familiar with how CMake works, I advice to stay within the currently supported use case as documented in the [urho3d.github.io/documentation/H ... brary.html](http://urho3d.github.io/documentation/HEAD/_using_library.html) in order not to waste your time.

-------------------------

hunkalloc | 2022-11-16 04:50:29 UTC | #34

The lack of this feature that made me switch to the https://discourse.urho3d.io/t/rebel-fork-framework-aka-rbfx-intermediate-release/7351/11

It's just too easy to setup a new project and add the engine as a submodule. It builds everything, and if I need to patch anything, I can just patch it.

-------------------------

