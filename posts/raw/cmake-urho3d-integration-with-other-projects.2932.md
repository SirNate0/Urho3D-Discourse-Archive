Pencheff | 2017-03-22 19:19:28 UTC | #1

My code uses ExternalProject_Add to build dependencies as a superproject and Urho3D is one of them. However, SDL is also one of those projects. If I link both Urho3D and SDL I get linker errors since another version of SDL is already linked with Urho3D....which is totally expected. I cannot just drop SDL from my project, I need it for audio, threading and synchronization, plus I always keep it up to date with SDL2. Same conflict can happen for other dependencies. 

There are a couple of workarounds:

1. Add Urho3D CMake install step for dependencies - this is trivial, for every third party lib there can be an install command that copies includes and libs to the CMAKE_INSTALL_PREFIX directory. This way my project can use the SDL library that Urho3D uses.

2. Modify Urho3D CMake to use external dependencies - I don't really want to force that, I like the way Urho3D currently is - download and build without the headache of having to search for dependencies. However, such modification can also help Urho3D to stay always up to date with say SDL2.

3. Modify my project so it entirely uses Urho3D - I can't do that within a reasonable time, my project is huge, split on 30-40 subprojects which rely on third party dependencies - SDL, asio, rapidjson, etc.

Ideas are welcome :)

-------------------------

johnnycable | 2017-03-20 09:52:27 UTC | #2

There's an option in C++ linker to tell it to link libraries just keeping one of them if they are duplicates... but right now can't remember exactly what is!
If I'm not mistaken there's an option in cmake too...

-------------------------

Pencheff | 2017-03-20 10:12:47 UTC | #3

I guess you are talking about LNK2005 workaround, using the /FORCE:MULTIPLE linker flag...but that is not a cool solution for me, that way I will not be able to control which of those duplicate libraries I'm using. I am talking about more generic solution. 

For example, I've used Ogre3D for a renderer until now, it has an option to specify prebuilt external dependencies folder.

Have an example of my superbuild:
[code]
project(my_superbuild)
...
EXTERNALPROJECT_ADD(libsdl2
  URL https://www.libsdl.org/release/SDL2-2.0.4.tar.gz
  PREFIX libsdl2
  PATCH_COMMAND ${PATCHER} libsdl2
  CMAKE_ARGS 
    -DCMAKE_INSTALL_PREFIX=${CMAKE_BINARY_DIR} 
    -DCMAKE_BUILD_TYPE=${CMAKE_BUILD_TYPE}
)
# other dependencies
...
...
# urho3d
EXTERNALPROJECT_ADD(urho3d
  GIT_REPOSITORY https://github.com/urho3d/Urho3D.git
  DEPENDS libsdl2
  PREFIX urho3d
  UPDATE_COMMAND ""
  PATCH_COMMAND ${PATCHER} urho3d
  CMAKE_ARGS 
    -DCMAKE_INSTALL_PREFIX=${CMAKE_BINARY_DIR} 
    -DCMAKE_BUILD_TYPE=${CMAKE_BUILD_TYPE}
    -DSOME_FLAG_FOR_URHO3D_TO_USE_MY_SDL_ABOVE=TRUE
)
[/code]

-------------------------

weitjong | 2017-03-20 11:30:56 UTC | #4

We have forked a few third-party libs (SDL is one of them). That's the main reason why Urho3D project is being structured the way it is now. You cannot simply replace the SDL from outside of Urho3D project and expect it to work with Urho, for example. If your super-project uses the Urho3D STATIC lib then your project should be able to reference any SDL objects without any problem (you don't need to install our SDL separately) because the STATIC lib has all the objects from Urho's 3rd-party libs. So, I don't quite understand why you said you cannot drop SDL as a dependency from your super-project.

-------------------------

Pencheff | 2017-03-20 11:41:32 UTC | #5

I want to be able to use SDL includes in my main project. Right now Urho3D uses SDL but does not install those headers when running the cmake install step. So I'm forced to use my SDL headers....or maybe do a cmake include_directories(path/to/urho3d/sources/third_party/sdl/) for my main project. Same goes for other third party libraries like rapidjson, my main projects needs to use the includes. Of course I can just use my external SDL/rapidjson include files and cross fingers there are no API changes in those, or force them to be the same version like in Urho3D.

-------------------------

weitjong | 2017-03-20 19:04:43 UTC | #6

If you mean the 3rd-party headers then our build system has taken care of that as well. However, it only exposes those headers that we think our library users need in their downstream projects. That is, we intentionally hide the rest of them from the library users as internal implementation of Urho3D. Those that are exposed can be found in /paht/to/urho3d/installation/include/Urho3D/ThirdParty after Urho3D target has been installed. Actually if you don't do INSTALL_COMMAND in your ExternalProject_Add() macro then perhaps you can workaround this limitation. I have never tried it, but perhaps you can try adding the "include/Urho3D/ThridParty" directory in the Urho3D build tree to your project's header search path instead. In the build tree all the 3rd-party headers are available because all of them are needed to build Urho3D library itself. So, there is a chance you can get away with it to be able to access all the headers there.

-------------------------

Pencheff | 2017-03-20 16:11:33 UTC | #7

Oh, I've totally missed the ThirdParty directory inside the install directory, thanks! Mark this as solved!

-------------------------

Pencheff | 2017-03-22 14:12:32 UTC | #8

Well, I don't find ThirdParty/GLEW being installed in the build/include/ThirdParty directory, when using Urho3D as external cmake project and compiling with OpenGL on Windows. This causes compiler errors about missing GLEW/glew.h. Ofcourse, I can just include the Source/ThirdParty/ in my main project as a workaround, but this can cause a mess.

-------------------------

weitjong | 2017-03-22 15:28:22 UTC | #9

I have already explained why we do not expose all the 3rd-party headers. The list of exposed headers do get changed some times based on user feedback if there is a good reason to do so. We could not keep every one happy though, or soon there will nothing left to hide as our internal implementation (i.e. things that could be subject to change without further notice, although to date I am not aware of such occurrence). You could try to use the "include/Urho3D/ThirdParty" in the Urho3D's build tree, like I have mentioned before, or you could try to apply a patch script in your ExternalProject_Add() against CMakeLists.txt belongs to GLEW so that its header got install as you wish. Just patch to remove the word "BUILD_TREE_ONLY" :slight_smile:

-------------------------

