inocencio | 2020-01-30 19:37:09 UTC | #1

Hi guys I need some enlightenment here.

Trying to install Urho3D on macOS 10.13 High Sierra without success.

My steps:

- Mkdir an **empty project folder**:
- Make a **bin** folder inside the **project root folder** and copied folders (CoreData and Data into **bin**)
- Copied the tutorial **CMakeLists.txt** inside **project root folder**
- Set system environment variables. I tried both to **STATIC** and **SHARED** versions on **.bash_profile** file:

`export URHO3D_HOME=~/dev/c++/Urho3D/Urho3D-1.7.1-macOS-64bit-<STATIC or SHARED>`

Try to compile the **CMakeLists.txt** in CLion IDEA but not recognise **URHO3D_HOME**. So I got:

"CMake Error at CMake/Modules/FindUrho3D.cmake:346 (message):
  Could NOT find compatible Urho3D library in Urho3D SDK installation or
  build tree.  Use URHO3D_HOME environment variable or build option to
  specify the location of the non-default SDK installation or build tree."

Then I tried to specified **URHO3D_HOME** by myself in **CMakeLists.txt** using:

    # Set URHO3D_HOME
    set(ENV{URHO3D_HOME} ~/dev/c++/Urho3D/Urho3D-1.7.1-macOS-64bit-STATIC)
    message("URHO3D_HOME: $ENV{URHO3D_HOME}")

I got another **error related to regex compiled**. I have no clue what is going on and how to make it works. It do not find the **URHO3D_HOME**. I also have marked **define_source_files ()** but it even reach that because there is no valid URHO3D.

Please, guys, help me out here.
Thanks in advance.

-------------------------

weitjong | 2020-01-29 16:34:26 UTC | #2

If you have Rake installed then at the Urho3D project root, type:

```
$ rake scaffolding dir=/your/new/project/path
```

Followed the instruction to setup the URHO3D_HOME variable as shown on the console output.

-------------------------

inocencio | 2020-01-29 23:04:12 UTC | #3

Thank you for your reply.

I already tried to compile using Rake but I got a weird error. Even if Rakefile remains in the project folder it accuses the file doesn't exist. My rake and gem is updated and worked out on further following method. 

I skipped this method for awhile and I tried other following this [thread](https://discourse.urho3d.io/t/unable-to-get-urho3d-built-on-mac/1007/23):

In the **step 8**, I got this **error**:

> RegularExpression::compile(): Nested *?+.
> RegularExpression::compile(): Error in compile.
> CMake Error at CMake/Modules/FindUrho3D.cmake:86 (if):
>   if given arguments:
> 
>     "NOT" "URHO3D_64BIT" "EQUAL" "URHO3D_FOUND_64BIT" "OR" "NOT" "URHO3D_LIB_TYPE" "STREQUAL" "URHO3D_FOUND_LIB_TYPE" "OR" "NOT" "URHO3D_BASE_INCLUDE_DIR" "MATCHES" "^/Users/nihil/dev/c++/Urho3D/projects/urho/include/Urho3D\$"
> 
>   Regular expression
>   "^/Users/nihil/dev/c++/Urho3D/projects/urho/include/Urho3D$" cannot compile
> Call Stack (most recent call first):
>   CMake/Modules/UrhoCommon.cmake:231 (find_package)
>   CMakeLists.txt:23 (include)

Somehow it doesn't recognise the URHO3D_HOME even if you point it to the right place. Is the CMakeLists.txt file correct and updated or what else could be causing that?

-------------------------

weitjong | 2020-01-30 01:51:14 UTC | #4

[quote="inocencio, post:3, topic:5849"]
```
"NOT" "URHO3D_64BIT" "EQUAL" "URHO3D_FOUND_64BIT" "OR" "NOT" "URHO3D_LIB_TYPE" "STREQUAL" "URHO3D_FOUND_LIB_TYPE" "OR" "NOT" "URHO3D_BASE_INCLUDE_DIR" "MATCHES" "^/Users/nihil/dev/c++/Urho3D/projects/urho/include/Urho3D\$"
```

Regular expression
“^/Users/nihil/dev/c++/Urho3D/projects/urho/include/Urho3D$” cannot compile
[/quote]

This looks weird to me. Probably you have a trailing backward slash in your URHO3D_HOME variable and causing the issue. In Unix-like systems the path separator is always forward slash and the backward one means something else (an escape character).

I also notice you are not using latest master branch and you should. We will be releasing it as 1.8 soon. Don’t hold your breath though. 

All our rake tasks are tested in our CI build, including on MacOS host system. So I have no doubt they work out of the box when they have been used properly.

-------------------------

shiv | 2020-01-30 14:13:07 UTC | #5

I recently start using Urho and built everything from source on Mac OSX sucessfully with a few caveats. Today I also used prebuilt Urho3D-1.7.1-macOS-64bit-STATIC.
I set **URHO3D_HOME**=~/Downloads/Urho3D-1.7.1-macOS-64bit-STATIC and my sample compiled successfully. 

I guess your **CMakeLists.txt** file have something missing. Can you please dump its content here?

FYI I took this sample to build https://github.com/damu/Urho-Sample-Platformer.git with few fixes it worked well.

-------------------------

shiv | 2020-01-30 14:13:10 UTC | #6

[quote="inocencio, post:1, topic:5849"]
`export URHO3D_HOME=~/dev/c++/Urho3D/Urho3D-1.7.1-macOS-64bit-<STATIC or SHARED>`
[/quote]


Update: found root cause, it seems "c++" in path conflicting with pattern matching, for now if you rename c++ to cpp should work.

-------------------------

weitjong | 2020-01-30 07:51:10 UTC | #7

Good catch. BTW, I won’t recommend to reference to out-dated (external) wiki pages.

-------------------------

inocencio | 2020-01-30 13:45:56 UTC | #8

Thank you so much, @weitjong and @shiv for your efforts. You guys are the best.

**NOW IT WORKS!!!**

Sorry for the caps, because I spent yesterday trying to figure out how to make it work. The issue about finding the UHRO3D_HOME was about the "c++" name in the path as @shiv mentioned. Unfortunately I have a lot of stuff in this folder, so I cannot just rename it. Over time I'll transfer the things over there to "cpp" folder carefully.

Now I'll keep it simple and try to focus only one way to build up my projects.

I removed the: `set(ENV{URHO3D_HOME} } <path_for_urho>)` from CMakeLists.txt 'cause the URHO3D_HOME now can be find from **.bash_profile** file. I'm target STATIC binaries from repository, despite yesterday I got the URHO3D source and compiled it on my own - took me about almost 2h to compile it.

I edited **define_source_files ()** macro to point straight to my **cpp** and **h** files.

`define_source_files (GLOB_CPP_PATTERNS src/*.cpp* GLOB_H_PATTERNS src/*.h* RECURSE GROUP)`

If you guys have other suggestion about how to point to the project source files, please let me know. Maybe I'll create some extra CMake file, something like **source.cmake** using "file ()" command and add each source file (cpp and h) on my own and call source.cmake file into CMakeLists.txt using **include()** command. Just thoughts...

Now I have to figure out how make it find the project's resources. Looking at docs, there are some ways to make it happen:

1. From **CMakeLists.txt** using macro **define_resource_dirs()**:
2. Using env variable: URHO3D_PREFIX_PATH

Second option is more suitable for global resources, I guess.

Now, let me be a newbie and get some "hello world" example to see it shine. ;)

Thanks!

-------------------------

SirNate0 | 2020-01-30 13:57:47 UTC | #9

Glad to hear you got it working! If you wanted to keep using your c++ folder you could probably escape the plusses (`c\+\+` or maybe `c\\+\\+`). Though I imagine you'll run into a similar problem again in the future, so you might want to make the transition. Also, in regards to the long build time, if you weren't using one a multi threaded build might help (make -j4 for 4 jobs, for example).

-------------------------

inocencio | 2020-01-30 14:10:26 UTC | #10

I never faced this problem before because I have nothing here that parsed the path or parsed it "wrong" as Urho3D did - thanks urho to warning me that.

The other projects I have inside are:

- Pure OpenGL projects;
- SDL;
- Raylib;
- SFML;
- Qt;

Anyway, thanks for suggestion. I'll move everything occasionally to prevent from some regex issue later on.

-------------------------

Modanung | 2020-01-30 19:38:56 UTC | #11

Btw, welcome to the forums, @inocencio and @shiv. :confetti_ball: :slightly_smiling_face:  :confetti_ball:

-------------------------

