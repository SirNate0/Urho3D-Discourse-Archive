EpicSpaces | 2021-04-11 16:40:22 UTC | #1

I've successufully builded urho3d with Cmake

cannot open file urho3d_d.lib when in debug  
cannot open file urho3d.lib when in release

errors pops up so what to do ?

-------------------------

Modanung | 2021-04-11 16:55:45 UTC | #2

Did you try running some of the compilation output located in the _bin_ folder?

Also, welcome to the forums! :confetti_ball:

-------------------------

EpicSpaces | 2021-04-11 17:15:02 UTC | #3

thank you, in my bin folder, there are bat files what for ? my x64/release is empty since build fails

-------------------------

Modanung | 2021-04-11 17:21:49 UTC | #4

Ah, your successful build process fails. Check :slight_smile:

Then, have you tried the scripts in the _script_ folder before running `make`?

And I assume you've found your way to the [documentation](https://urho3d.github.io/documentation/1.7.1/_building.html#Building_Native)?

-------------------------

EpicSpaces | 2021-04-11 17:28:32 UTC | #5

there is nothing special in the documentation :/ 
the script folder before or after running make is filled with bat files what for again, launching one of them does nothing?

-------------------------

Modanung | 2021-04-11 17:32:19 UTC | #6

You may want to read the [build scripts section](https://urho3d.github.io/documentation/1.7.1/_building.html#Build_Scripts).

-------------------------

EpicSpaces | 2021-04-11 17:35:19 UTC | #7

well technically that's all the process that I've already done :wink:
I'm I missing something ?
I think the error is more technical

-------------------------

Modanung | 2021-04-11 17:36:47 UTC | #8

What are the full last two commands that you run, before hitting the obstacle?

-------------------------

EpicSpaces | 2021-04-11 17:42:47 UTC | #9

what commands, I used cmake-gui, I disabled 
urho_angelscript 
urho_ lua
 urho_luajit
that's all, everything seems fine, I run Visual Studio, chnage to release and these errors pops up
cannot open file urho3d.lib
and more errors in linux_adapter.cpp like expected identifier and like

errno_t mbstowcs_s(size_t *,wchar_t (&)[_Size],const char *,size_t) throw()': function template has already been defined (compiling source file C:\Users\user\Desktop\Urho3D-master\Source\ThirdParty\SLikeNet\Source\src\BitStream.cpp)|SLikeNet|C:\Users\user\Desktop\Urho3D-master\Source\ThirdParty\SLikeNet\Source\include\slikenet\linux_adapter.h

maybe from the lib missing ?

-------------------------

Modanung | 2021-04-11 17:52:31 UTC | #10

Did you try setting the WIN32 option?

-------------------------

EpicSpaces | 2021-04-11 17:57:18 UTC | #11

where ? next to debug/release combobox there is only x64 no option for 32 and I don't think that's the case

-------------------------

Modanung | 2021-04-11 17:57:47 UTC | #12

I'm unfamiliar in bat country. Maybe someone else can help you.

-------------------------

EpicSpaces | 2021-04-11 17:58:32 UTC | #13

I just have to smack my head then :frowning:

-------------------------

Modanung | 2021-04-11 18:00:07 UTC | #14

Either that, be patient, or install [Linux](https://www.linuxmint.com). There's alternatives.

-------------------------

EpicSpaces | 2021-04-11 18:00:47 UTC | #15

noway, I'm unfamiliar in linux country

-------------------------

Modanung | 2021-04-11 18:04:06 UTC | #16

It's free of bats. :bat:

-------------------------

EpicSpaces | 2021-04-11 18:05:25 UTC | #17

and full of sh (shit)

-------------------------

Modanung | 2021-04-11 18:07:16 UTC | #18

> `bull.sh` makes the flowers grow. :sunflower:

-------------------------

EpicSpaces | 2021-04-11 18:10:03 UTC | #19

I love my bats gives me batman powers(not this time)

-------------------------

Modanung | 2021-04-11 19:42:05 UTC | #20

Do you love them too much to execute them, and digest the outstream?

-------------------------

EpicSpaces | 2021-04-11 20:00:47 UTC | #21

well it's just hard to switch to linux, and even if I do what guarantee me that it will work ?
I can install virtualbox again Ubuntu and all the pain ...

-------------------------

Modanung | 2021-04-11 20:09:27 UTC | #22

Actually, I gave up on that suggestion.

[quote="SirNate0, post:13, topic:6000"]
If you want, you can also use the cmake-gui to run CMake, though you don’t get the the scripts automatically picking the right compiler and flags for the build for you. My preference is to use the scripts to initially create the build (which sets the right stuff for web builds and such for me by picking the right script), then I modify build flags like a shared vs static build using the GUI.
[/quote]

Personally, I prefer Linux Mint over Ubuntu.

-------------------------

SirNate0 | 2021-04-12 04:25:09 UTC | #23

Start with the *.bat file for the initial run of CMake. You probably should run then from within a command line, and not just run them by double clicking. You need to supply the script with a build directory, so if you didn't they would probably fail. 

You can use the CMake GUI afterwards to edit the cache, but it does make it easier to use the bat file first as it will select the most of the right flags and all for you. I'm not certain, but I think if you switch between debug and release you'd need to re run CMake. But I've also not used visual studio with Urho, so that's just a guess.

Which version of Urho are you using? Using the master branch off of GitHub tends to work best with Urho, the releases have gotten a bit out of date at this point.

Also, if the error doesn't go away, an exact copy of the errors you're seeing would probably be most helpful. Especially the earliest errors, not necessarily the last ones on the screen, if that wasn't what you posted earlier.

-------------------------

throwawayerino | 2021-04-12 05:38:44 UTC | #24

https://github.com/urho3d/Urho3D/wiki/Compiling-Urho3D
Here's a guide with cmake GUI. I prefer to set the binaries built location to the same directory as source but it doesn't matter since it should set all executables to link to that.

-------------------------

Pencheff | 2021-04-12 11:55:33 UTC | #25

1. Clone Urho3D git repository (git clone https://....)
2. Inside Urho3D folder: 
mkdir build
cd build
cmake .. -A Win32
3. Open the build/Urho3D.sln using Visual Studio
4. Build the "ALL BUILD" target

-------------------------

EpicSpaces | 2021-04-12 17:17:34 UTC | #26

thanks guys I managed to make it to work :slight_smile: 

commenting by hands(not advisable) the redefinition errors(like struct type redefinition) from these files that stopped building lib files, and everything worked perfectly. 

lines to remove was :
linux_adapter.h
lines 66 to 99 

linux_adapter.cpp
23 to 131 
174 to 205
291 to 320

civetweb.cpp
until 661 line

-------------------------

EpicSpaces | 2021-04-13 11:52:46 UTC | #27

I have another question, can we remove cmake references in my project ?, if not, can we extract vxproj and filters, because the headers and cpp files are only seen in solution explorer in visual studio, not in the source folder build, copying by hand is exhausting .

-------------------------

SirNate0 | 2021-04-13 14:24:51 UTC | #28

You can avoid using CMake. All it does is set up all the correct files and build flags. It's not required, just very recommended. As to a way to do it, I have no idea other than just manually copying all of it.

If your goal is just too use it in your own project that uses Urho as a library it's a lot easier. Just copy the preprocessor defines and other build flags (e.g. using c++11 for example), and add the Urho library and include paths (note that I think that ends up being more than just include, I think a couple of the ThirdParty paths are added as well).

-------------------------

EpicSpaces | 2021-04-13 18:31:34 UTC | #29

no, actually I'm trying to create my own editor on top of urho3d, I'm trying even to redit all the src code, but I can't understand it compleltly, there is so much files, any diagram class ?

-------------------------

SirNate0 | 2021-04-13 21:38:11 UTC | #30

Read the documentation pages first [here](https://urho3d.github.io/documentation/HEAD/index.html). They give good introductions to the various subsystems. I think the online documentation also has class diagrams if you go to the different classes in the documentation.

-------------------------

