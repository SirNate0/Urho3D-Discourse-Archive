UrhoIsTheBest | 2020-06-05 07:08:52 UTC | #1

I had no problem to setup up a new Urho3D project.

But if I use Urho3D as the external library, **I could not easily jump to Urho3D source .cc file in the project scope** (only header file where I could not find implementation details). 
I am using CLion and I have to open another vanilla CLion project just to navigate through Urho3D source code for various function implementation details.

So if I want to easily navigate around source code, should I make my project directly in the Urho3D source code folder and build them together (not as the external library). Is this the only way?
How do you guys do it?

-------------------------

SirNate0 | 2020-06-06 00:40:15 UTC | #2

I've never used Clion before, so I can't be certain it works at all similarly, but for QT creator (which I do use) if I just have the Urho3D project open in the same window as my project it will jump to the source files for me.

What behavior were you expecting with this, by the way? It sounds to me that the behavior you observed would be the expected behavior of using Urho as an external library (which you may not even have the .cpp files for).

Also, it's possible it would do what you wanted out of the box but some of your paths aren't right, see
https://stackoverflow.com/questions/33620947/how-to-navigate-to-source-code-in-linked-libraries-in-clion

-------------------------

UrhoIsTheBest | 2020-06-05 22:39:44 UTC | #4

**The behavior I am expecting is:**
In my own cpp files that use Urho3D api, when I click "jump to definition" on any Urho3D function or class name, it will directly navigate to .cc implementation file.

**While the behavior now:** it only navigate to the .h file in ```/usr/local/lib/Urho3D/``` where the external library was built into. And when I click "jump to definition" in the .h file again, it could not jump to any source file.
I understand it is the expected behavior when you build it as the external lib (only .h header file is included in your project). So that's why I am asking any other way I could navigate to source files.

A workaround for me is to add 
```
include_directories("/Users/XXX/git_folder/Urho3D")
```
in the ```CMakeList.txt```
This way, the first time when I jump to definition of a function name or class name, it will still go to the .h file in  ```/usr/local/lib/Urho3D/```. But when I click "jump to definition" again from there, CLion will do a search in included directories and find those source files. It's still not elegant, but it works at least.
I don't know if anyone has a better idea.

**Is there a way to tell CMake not to search  ```/usr/local/lib/Urho3D/``` in the first place?**

-------------------------

dertom | 2020-06-06 05:05:12 UTC | #5

Are you compiling urho3d library on your own or are you using precompiled version?

If compiling on you own, you usually set an environment variable URHO3D_HOME to the cmake build-folder. This is the first folder to be used in findurho3d (called from within urhocommon.cmake)
In your case it seems not to find URHO3D_HOME or the path is invalid and so it falls back to a previously 'installed' version.
(There is a log when running cmake on your project what libUrho3D.a is used) so check this env-variable.

Not sure that will have any effect for your problem.
At least I develop like that but with qtcreator and I have like sirnate no problem switching to the impl-files.
Hope that helps.

-------------------------

UrhoIsTheBest | 2020-06-06 00:14:16 UTC | #6

I played with CMake for a while and this works!

**Just need to keep in mind** we need to specify all include folder before the 
```
include(UrhoCommon)
```
line since this module read ```URHO3D_HOME``` and ```URHO3D_INCLUDE_DIRS```.

I did not notice that before you remind me the way how UrhoCommon works. Thanks for that!

So my final ```CMakeLists.txt``` is:
```
...
# Set CMake modules search path
set(CMAKE_MODULE_PATH ${CMAKE_SOURCE_DIR}/CMake/Modules)

set(URHO3D_HOME "/Users/myusername/git_folder/Urho3D")
set(URHO3D_INCLUDE_DIRS "/Users/myusername/git_folder/Urho3D/Source")
MESSAGE(STATUS "URHO3D_HOME: ${URHO3D_HOME}")
MESSAGE(STATUS "Urho3D include dir: ${URHO3D_INCLUDE_DIRS}")
include_directories(${URHO3D_INCLUDE_DIRS})

# Include Urho3D Cmake common module
# Keep this after defining all the DIRs
include(UrhoCommon)
...
```


**Another thing is we should use path** 
```
/Users/myusername/git_folder/Urho3D/Source
``` 
instead of 
```
/Users/myusername/git_folder/Urho3D
```
since there is another ```include``` folder in Urho3D root directory with only header files. Otherwise, the ```jump to definition``` could lead to that folder.

Now it works as I expected!
I am very happy now.
Thanks everyone for help!

I think it could be useful for someone not very familiar with CMake/CLion and want to set up the project like this.

-------------------------

