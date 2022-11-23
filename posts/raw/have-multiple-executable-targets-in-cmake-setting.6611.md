CE184 | 2020-12-09 04:46:13 UTC | #1

I have many different scenes for my game, eventually they will be merged into the single final application. But during development, I decoupled them as much as possible so I can work independently on each of them. 
For testing reason, I have separate derived Application class to setup each scene. So I can use
```
URHO3D_DEFINE_APPLICATION_MAIN(XXXXSceneTestApplication)
```
and CMakeList
```
# Setup target with resource copying
setup_main_executable ()
```
would make any one to be run as the main entry point.

The problem is: I have to uncomment the ```URHO3D_DEFINE_APPLICATION_MAIN``` line in the TestApplication I want to test and also comment ```URHO3D_DEFINE_APPLICATION_MAIN``` in all other xxxxApplication file.

I know we can use multiple ```add_executable(target_xxx {src})``` in CMakeList to have multiple targets build at the same time, and run whichever we want.
I wonder if I can do similar thing easily with Urho3D cmake setting?

-------------------------

SirNate0 | 2020-12-09 05:54:10 UTC | #2

If your executables are all in the same folder I suspect your could just call `setup_main_executable` for of them and use `add_executable` for the rest. I could be wrong about that, though, I've not delved too deeply into the build system.

-------------------------

CE184 | 2020-12-09 06:08:04 UTC | #3

My understanding is there could be only one ```URHO3D_DEFINE_APPLICATION_MAIN``` macro through out the whole project and ```setup_main_executable()``` just find that one automatically. If there are more than one ```URHO3D_DEFINE_APPLICATION_MAIN```, the build just fail since there are duplicate main symbols.
I guess I need to have separate CMakeList files for each target? each file only include one ```URHO3D_DEFINE_APPLICATION_MAIN``` class and setup_main_executable there. But that would be tedious since actually all the other source cpp are shared.

Also, if I want to use ```add_executable``` for my main entry point for Urho3D, it might not work given all those links. it might not be that trivial since the ```setup_main_executable``` does a lot of extra things beside that?

-------------------------

CE184 | 2020-12-10 02:23:51 UTC | #4

After looking through the cmake macro, I figured out a way to do this.

Example CMakeList.txt
```
# All the same settings
# ...

# Define source files
file (GLOB_RECURSE SRC_CPP_FILES src/*.cpp)
# Remove all main target application files
list (FILTER SRC_CPP_FILES EXCLUDE REGEX "<your custom root application regex path>")
file (GLOB_RECURSE SRC_H_FILES src/*.h)

# repeat this for each target
set(TARGET_NAME your_first_target)
define_source_files (GROUP EXTRA_CPP_FILES ${SRC_CPP_FILES} <your first root application file that has the main macro> EXTRA_H_FILES ${SRC_H_FILES})
setup_main_executable()  # this will setup your_first_target

# repeat this for each target
set(TARGET_NAME your_second_target)
define_source_files (GROUP EXTRA_CPP_FILES ${SRC_CPP_FILES} <your second root application file that has the main macro> EXTRA_H_FILES ${SRC_H_FILES})
setup_main_executable()  # this will setup your_second_target

# repeat or you can write a for loop to add all root application that has the main macro
...
````

At least this one works, not sure if it's a hack or standard way to do it.

-------------------------

