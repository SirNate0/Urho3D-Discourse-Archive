spenland | 2019-12-03 14:48:59 UTC | #1

So, I've built Urho3D with CMake gui then opened the .sln file and built Debug & Release. 

I am wanting to create a new project to start messing around with Urho3D.I followed [this tutorial](https://github.com/urho3d/Urho3D/wiki/Setting-up-a-Project-(CMake)) , and have the project setup correctly (I think). 

My question is what is the purpose of CMake now? Seems like CMake is used to generate the project file then you're editing that file. Is CMake used to deploy to different platforms if so, can you re-run CMake after editing your Build folder where the project files are or does that overwrite the project?

Basically, CMake in a nutshell explanation would be nice. What I've read about it just seems to confuse me. I've never used it before.

-------------------------

jmiller | 2019-12-03 20:40:50 UTC | #2

Hello and welcome to the forum! :confetti_ball: 

cmake info? [cmake overview](https://cmake.org/overview/), docs, web discussion threads, and of course good examples like Urho. :tropical_fish: 

Official [doc: building](https://urho3d.github.io/documentation/HEAD/_building.html) has some relevant information; in the [Build options](https://urho3d.github.io/documentation/HEAD/_building.html#Build_Options) section in particular:

> Note that the specified build option values are cached by CMake after the initial configuration step. The cached values will be used by CMake in the subsequent configuration. The same build options are not required to be specified again and again. But once a non-default build option value is being cached, it can only be reverted back to its default value by explicitly resetting it. That is, simply by not passing the corresponding build option would not revert it back to its default. One way to revert all the build options to their default values is by clearing the CMake cache by executing cmake_clean.bat or cmake_clean.sh with the location of the build tree as the first argument or by executing it in the build tree itself.

If all else fails.. as one might expect, they can delete a build tree (cache and all), regenerate and rebuild.

-------------------------

Pencheff | 2019-12-04 14:58:47 UTC | #3

The purpose of CMake is to take care of all the stuff around C++ makefiles, solution files (.sln), XCode project files. If you want to add new libraries or files to your project you have to touch few lines in a CMakeLists.txt and as soon as you try to build your project (or regenerate build tree) it will update the appropriate project files. You can also have multiple builds with different settings, have different features on or off. You also get to keep your version control system clean of any project files and binaries by just excluding the build folder out of it.
If you edit generated files in the build folder and re-run CMake it will rollback your changes. For example if you change include folders of a project in Visual Studio or add/remove files from a project, the next CMake run will regenerate the .sln files and you'll lose those changes.

-------------------------

