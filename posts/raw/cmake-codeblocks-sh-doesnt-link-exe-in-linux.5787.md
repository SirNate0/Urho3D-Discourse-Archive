codefive | 2019-12-28 11:34:59 UTC | #1

Hello community.-

I am trying to compile with codeblocks, im on Linux, so far i have done the following

1.- git clone https://github.com/urho3d/Urho3D.git
2.- cd Urho3D
3.- rake cmake && rake make
4.-cd script
5.- ./cmake_codeblocks.sh ./myprojects/projectname
6.- cd myprojects/projectname

From here if i compile with the terminal and add a 7 step make i get no errors, but if i skip this step and compile with Code Blocks IDE, i get 27 errors. No matter what i do i cant link the resulting exe in Linux with the IDE, and i also wish to add more source files from my own. Thank you in advance

-------------------------

weitjong | 2019-12-28 02:04:46 UTC | #2

Something wrong with your steps but still I cannot explain why C::B IDE failed to build while `make` worked. AFAIK the IDE internally also just invokes the same `make` process. So, your C::B IDE may not load the same "project" and/or not configured correctly.

You either just use the provided shell scripts or just use `rake` task, but not both.

Below is what I would do from the Urho3D project source tree:

```
$ build_tree=./path/to/your/build/tree rake cmake codeblocks
```

The above rake task will in turn invoke `cmake_codeblocks.sh` script. If you study that script, you can see it basically just tells CMake to generate a project build tree using "CodeBlocks - Unix Makefiles" as generator. Since it is still using "Unix Makefiles", you can just cd into the build tree and build using `make` in a terminal. The chosen generator will also generate an extra project file *.cbp (if I recall it correctly). You should be able to use C::B IDE to load this *.cbp file and build using the GUI. Note that internally it still invokes the same `make` process. It will be very weird if you say CLI worked but GUI didn't.

-------------------------

codefive | 2019-12-28 03:44:12 UTC | #3

Hello, i have used your command, but again when i build with the CLI and with the IDE gui i have different results, i will install other version of Code Blocks, and another question "my source code" how do i add it to the project? Only make directory, create file and so? Do i need to modify my Code Blocks Makefile? Sorry im a little confused here Update.- I have reinstalled Code Blocks, it seems the instalation was corrupt or something, strange i am using Arch Linux

-------------------------

JTippetts1 | 2019-12-28 03:56:46 UTC | #4

The typical use-case is to not add your code files directly to the Urho3D project. You will build Urho only once, then for your projects you will create a separate project that merely links to the Urho library.

-------------------------

codefive | 2019-12-28 04:15:24 UTC | #5

Thank you both, could you specify how that could be done on Linux, almost all instructions are for Windows, and im not a expert compiling and linking

-------------------------

jmiller | 2019-12-28 06:01:27 UTC | #6

Hello; There are a few docs sections I think may be relevant..
  https://urho3d.github.io/documentation/HEAD/_building.html
  https://urho3d.github.io/documentation/HEAD/_using_library.html

-------------------------

codefive | 2019-12-28 07:24:00 UTC | #7

Oh yes !! @jmiller i had already read that documentation but now its much clearer its purpuse to me, now i have understood, sorry its the first time i compile with Code Blocks. Thank you a bunch !!!! Update.- Now i want to make build_tree=./path/to/my/build/tree rake cmake codeblocks web but i got a lot of cmake errors, i want the target to be web and with cb, the errors i get are this.-

> CMake Deprecation Warning at CMakeLists.txt:31 (cmake_policy):
>   The OLD behavior for policy CMP0026 will be removed from a future version
>   of CMake.
> 
>   The cmake-policies(7) manual explains that the OLD behaviors of all
>   policies are deprecated and that a policy should be set to OLD only under
>   specific short-term circumstances.  Projects should be ported to the NEW
>   behavior and not rely on setting a policy to OLD.
> 
> 
> CMake Deprecation Warning at CMakeLists.txt:35 (cmake_policy):
>   The OLD behavior for policy CMP0063 will be removed from a future version
>   of CMake.
> 
>   The cmake-policies(7) manual explains that the OLD behaviors of all
>   policies are deprecated and that a policy should be set to OLD only under
>   specific short-term circumstances.  Projects should be ported to the NEW
>   behavior and not rely on setting a policy to OLD.
> 
> 
> CMake Error at CMake/Toolchains/Emscripten.cmake:68 (message):
>   Could not find Emscripten cross compilation tool.  Use EMSCRIPTEN_ROOT_PATH
>   environment variable or build option to specify the location of the
>   toolchain.  Or use the canonical EMSCRIPTEN environment variable by calling
>   emsdk_env script.
> Call Stack (most recent call first):
>   /usr/share/cmake-3.16/Modules/CMakeDetermineSystem.cmake:93 (include)
>   CMakeLists.txt:39 (project)
> 
> 
> CMake Error: CMake was unable to find a build program corresponding to "Unix Makefiles".  CMAKE_MAKE_PROGRAM is not set.  You probably need to select a different build tool.
> CMake Error: CMAKE_C_COMPILER not set, after EnableLanguage
> CMake Error: CMAKE_CXX_COMPILER not set, after EnableLanguage
> -- Configuring incomplete, errors occurred!

-------------------------

JTippetts | 2019-12-28 15:54:05 UTC | #8

We just went through this with another thread, but here goes:

To build for the web, you have to specify the correct path for your Emscripten installation. Download and install Emscripten as described at https://emscripten.org/docs/getting_started/downloads.html Once you have downloaded, installed and activated the latest, you should have a folder called **emsdk** at the location you cloned the repo to. When you invoke the **cmake_emscripten.sh** bash script located in Urho3D/script, you have to specify the proper path inside the emsdk installation in order for CMake to find the emscripten build tools. If this path is not properly specified, you get the error you have, of CMake being unable to find the build tools.

So, say you have installed emsdk into /home/codefive/emsdk, and you have cloned Urho3D repo into /home/codefive/Urho3D. You could configure the project by changing dir to Urho3D and calling:

**./script/cmake_emscripten.sh /home/codefive/Urho3D_WebBuild -DEMSCRIPTEN_ROOT_PATH=/home/codefive/emsdk/upstream/emscripten**

This will configure for a web build. Specify any other options as you desire (ie, to turn on/off Lua and AngelScript, etc...). Upon completion, navigate to /home/codefive/Urho3D_WebBuild and invoke **make**. It should build the Urho3D libraries.

Note that as we established in the other thread, you have to bump the required version of CMake as specified in the CMakeLists.txt files, in order to use the latest Emscripten release. I believe you can go back to 1.38.4 version of Emscripten if you don't want to edit the CMakeLists files, though CodeBlocks should make it easy to change all of them by using the Replace In Files, and replacing **3.2.3** with the desired CMake min version. I have established that **3.14.5** works acceptably.  If you do revert to Emscripten version 1.38.4, then the path you use for EMSCRIPTEN_ROOT_PATH will be /home/codefive/emsdk/fastcomp/emscripten instead of /home/codefive/emsdk/upstream/emscripten. I recommend just sticking with Emscripten latest and updating the CMake files, personally.

Note that you might not be able to build a project for CodeBlocks when doing a web build. I didn't try very hard, but every time I did try it wanted to build a native build instead. You might have to do some fiddling around to get that to work. Look at the bash scripts in /script for cmake_generic, cmake_codeblocks and cmake_emscripten to see what they do and whether or not they can be made to do what you want.

Also note that when using these build scripts, you don't need to invoke **rake**. You can use rake to set up a new project that uses Urho3D if you desire, or you can just build a simple CMakeLists.txt by hand, and use the same script/cmake_emscripten.sh that the library uses in order to configure it.

-------------------------

