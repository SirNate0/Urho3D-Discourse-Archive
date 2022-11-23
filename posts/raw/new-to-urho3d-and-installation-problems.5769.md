Asimov500 | 2019-12-17 12:36:45 UTC | #1

I am new to urho3D, but I have used irrlicht.
However I am having a bit of trouble setting up urho3D.

I want to use urho3D with C++ and my preferred IDE is CodeBlocks.
So I installed the Urho3d_CodeBlocks_Wizrard-Master, which seemed to work ok.
I pointed it at an empty Urho3D folder I created knowing I was going to install Urho3D there.

I then downloaded urho3D-1.7.1.zip for windows.
I run cmake on the cmake_codeblocks.bat and pointed it at my folder I created.

It created a pile of folders and files. eg bin,CMakeFiles,Docs, include,lib,Source, and it made a Urho3D.cbp.
I thought I would have to run that and compile it and everything would work. However I get an error when I do this.

error: unknown type name 'WAVEOUTCAPS2W' and a pile of other errors.

Can anyone tell me where I am going wrong?

-------------------------

jmiller | 2019-12-17 18:51:22 UTC | #2

Hello and welcome to the forum! :confetti_ball: 

I'm unfamiliar with [Urho3D_CodeBlocks_Wizard](https://github.com/BlueMagnificent/Urho3D_CodeBlocks_Wizard) but it is a community contribution last updated  *edit: today. :)

As a general rule (edit: without considering anyone's requirements or issues; also 1.7.1 is current) I recommend the master repository https://github.com/urho3d/Urho3D which has an excellent stability record, and can also generate CodeBlocks projects.
Official build docs: https://urho3d.github.io/documentation/HEAD/_building.html

If all else fails, a Makefile project (vs. IDE-specific) works most anywhere.
HTH

-------------------------

Valdar | 2019-12-17 08:39:39 UTC | #3

Hi Asimov500,
Welcome to the forum.
I haven't used the wizard either, and not sure why you would need it. I just tried the 1.7.1 zip using the CMake GUI, targeting Code::Blocks and MinGW-w64, and it builds and compiles with no errors using the default values (64 bit). 

What compiler and version and are you using, and 32 or 64 bit? There are a few issues on various sites regarding similar errors like the one you receive and they all seem to point to MinGW, including one in this forum:
https://discourse.urho3d.io/t/cmake-mingw-build-error/2961

I hope you get it working. Personally, I find Urho3D superior to irrlicht, and it has always been the easiest open source game engine to build of any I've tried (and that's a LOT).

-------------------------

Asimov500 | 2019-12-17 11:38:47 UTC | #4

The wizard is to set up a new project in codeblocks and that part works, but obviously I need the compile urho3D engine in the folder I point it to of course.

-------------------------

Asimov500 | 2019-12-17 11:47:49 UTC | #5

I am still having problems. I downloaded the master from github and went to the scripts folder. I created a folder called build-tree and run the batch file

cmake_codeblocks.bat build-tree
So I look in the build-tree and it has made a few folders CMakeFiles,include and some files CMakeCache.txt, CPackConfig.cmake and CpackSourceConfgi.cmake.

Now in the CMakeFiles there is an error log, which I tried to upload, but I think that this forum only allows images in an upload. I would paste it, but it is rather long. Is there a way to upload the error log for someone to look at?

-------------------------

JTippetts | 2019-12-17 12:02:12 UTC | #6

Upload it to pastebin then paste the link here.

-------------------------

Asimov500 | 2019-12-17 12:07:56 UTC | #7

Here is the paste
https://pastebin.com/wTGjSNV0

I hope it works because it is the first time I used pastebin

-------------------------

Modanung | 2019-12-17 12:16:13 UTC | #8

Alternatively the `[details=title] ... [/details]` tags (also available through the *Options cog* in the message tool bar) can be used to hide parts of a message.

Also, welcome to the forums! :confetti_ball: :slightly_smiling_face:

-------------------------

JTippetts | 2019-12-17 12:20:18 UTC | #9

Note that the simple existence of a CMakeError.log file inside CMakeFiles doesn't mean it failed. When detecting features, cmake attempts to compile various internal test programs and the success/failure of those compilations sets flags for the feature being tested for, and CMakeError.log is just where the spam for those tests ends up.

-------------------------

Asimov500 | 2019-12-17 12:25:44 UTC | #10

Yeh I understand that, but I had errors in my console as well.
And it is  quite suspicious that when I look in the include folder there is a Urho3D folder with a ThirdParty folder and no actual include files in there, which kinda leads me to believe it hasn't worked correctly.

I really wish someone could make a video showing the process, that would be a great help. I have only found one on youtube with some really loud music and it is hard to follow.

> CMake Error: Error processing file: D:/Download/Urho3D-master/Urho3D-master/script/CMake/Modules/GetUrhoRevision.cmake
> CMake Error at CMakeLists.txt:86 (string):
>   string sub-command REGEX, mode MATCH needs at least 5 arguments total to
>   command.
> 
> 
> CMake Error at F:/Utilities/cmake/share/cmake-3.16/Modules/CPack.cmake:537 (message):
>   CPack license resource file:
>   "D:/Download/Urho3D-master/Urho3D-master/script/LICENSE" could not be
>   found.
> Call Stack (most recent call first):
>   F:/Utilities/cmake/share/cmake-3.16/Modules/CPack.cmake:542 (cpack_check_file_exists)
>   CMakeLists.txt:169 (include)
> 
> 
> CMake Error at CMakeLists.txt:199 (add_subdirectory):
>   add_subdirectory given source "Source" which is not an existing directory.
> 
> 
> CMake Error at CMakeLists.txt:202 (add_subdirectory):
>   add_subdirectory given source "Docs" which is not an existing directory.

-------------------------

Bluemoon | 2019-12-17 16:14:26 UTC | #11

Hi @Asimov500

 I created [Urho3D_CodeBlocks_Wizard](https://github.com/BlueMagnificent/Urho3D_CodeBlocks_Wizard) , and as you rightfully said it is used for setting up urho3d project, albeit for Windows using Mingw. Unfortunately it has not been updated for a while ( some other projects has kept me away from urho3d) but has now been updated.

I just downloaded urho3d v1.7.1, ran the codeblocks cmake, built successfully and was also able to build a test project.

Can you further detail your steps so we can reproduce it

-------------------------

weitjong | 2019-12-17 16:17:10 UTC | #12

I think your "git" on Windows behaves erroneously. I suggest you to uninstall it and install "git" from other provider.

I suspect your problem started at the first highlighted line below and causing a variable to left unset/undefined, ultimately the CMake command in last highligted line failed and it could not recover itself.

https://github.com/urho3d/Urho3D/blob/master/CMake/Modules/GetUrhoRevision.cmake#L33-L43

Arguably the CMake command in the last line could have been rewritten to handle abnormal result from "git" on Windows. In your case the "git" command should have exited with non-zero exit code (as you are using downloded source instead of a git clone), but it didn't. Hence my suggestion above.

Alternatively, fix the last highlighted line to read:

```
string (REGEX MATCH "[^.]+\\.[^-]+" VERSION "${LIB_REVISION}")
```

-------------------------

Asimov500 | 2019-12-17 23:55:45 UTC | #13

Thanks I will have another go and let you know.

I am not sure how it is a git problem as I didn't use git to clone it. I downloaded it directly from github in a zip file. I use git all the time as I am a web developer as well, and not had a problem with it however.

I am going to try your line to see if it works, and will get back to you once I have tried it.
It will probably be tomorrow when I can have another look at it though, as it is getting late.

-------------------------

Asimov500 | 2019-12-17 23:58:41 UTC | #14

Hi @Bluemoon,
Actually your wizard worked fine. I have already installed it in codeblocks and it creates a new Urho3D project great. Obviously I won't be able to compile it until I get Urho3D compiled, but I am sure once I got Urho3D compiled ok I am sure your script will work.

-------------------------

Asimov500 | 2019-12-19 17:03:46 UTC | #15

@weitjong,

I tried changing the line and re-compiling and unfortunately it doesn't work. I feel I am stumbling at the first stage. It actually only took me a about an hour to work out how to compile irrlicht. The only reason I want to have a go at urho3D is because the shader support, and normalmaps look better than irrlicht. So I want to transfer a project I have already started writing to urho3D.

I will keep looking for an answer but I am a bit slow as I have the flu at the moment and got this tremendous headache.

-------------------------

weitjong | 2019-12-19 17:19:43 UTC | #16

Take a rest. If you want our help you will need to show us what’s the problem exactly after the change I suggested. It cannot be the same issue again because it just not possible.

-------------------------

Asimov500 | 2019-12-21 13:29:34 UTC | #17

I found a video on youtube and found out where I was going wrong on one part.
The video had no sound, so was a little hard to follow. Plus it was a little old, but it helped.
https://www.youtube.com/watch?v=N0MoPhFBwbQ&t=270s

However I managed to get the cmake to make the files I needed.
I was running the cmake_codeblocks.bat from command line. I never thought
about using the cmake gui at all. Also I just downloaded the source folder from git this time.

So I follow the video but instead of selecting visual studio I selected codeblocks and mingw, because
that is what I mainly use. Even though I do have Visual Studio as well.

So after configuring cmake and clicking generate I end up with a pile of stuff in my build folder,
including the Urho3D.cbp for codeblocks.

So I run the cbp which opens codeblocks and then click build and run.
Then it starts building and I get a few errors
eg.
error: unknown type name 'WAVEOUTCAPS2W'

So I am closer on getting it compile but not there yet. Please check out my image for the errors I am getting.
![urhoERROR|690x374](upload://oEOlTF1BPQJRpJCOMzItcEVFMDH.jpeg)

-------------------------

weitjong | 2019-12-21 14:23:46 UTC | #18

[quote="Asimov500, post:17, topic:5769"]
error: unknown type name ‘WAVEOUTCAPS2W’
[/quote]

hmm... isn't that the same error in the link posted by Valdar above? Ensure you have a MinGW that is up for the task.

-------------------------

Asimov500 | 2019-12-21 15:54:35 UTC | #19

It seems I am running mingw 5.1.0. It was installed when I installed codeblocks. Is that too old?

Oh yes you are right it is the same error by the way, but I did the compiling a completely different way so I reposted to show what I have tried.

-------------------------

Bluemoon | 2019-12-21 15:58:43 UTC | #20

For Urho3d v1.7 I believe it is not too old

-------------------------

Bluemoon | 2019-12-21 16:00:29 UTC | #21

@Asimov500 can you list out your system specs both hardware and software. I'm really confused why you should be having difficulty still

-------------------------

Asimov500 | 2019-12-21 16:05:46 UTC | #22

Here is my system specs
Computer: Laptop Lenovo W520
Processor: Intel(R) Core(TM) i7-2760QM CPU @ 2.40GHz
Installed memory(RAM): 32.0 GB
System type: 64-bit Operating System

I am a 3D artist which is the reason I have a lot of memory in my computer.

I have also successfully used other engines without problems
eg
irrlicht,
Neoaxis,
Unity,
Unreal,
Atomic (which I believe is based on Urho3D)
etc

-------------------------

Bluemoon | 2019-12-21 16:36:15 UTC | #23

Try the below steps. This is to build urho3d using mingw on the command line

Download urho3d source and unzip it to any desired directory.

Make sure your mingw installation bin folder path is in your system PATH variable if not add it. This can easily be done by typing the below into the command line

> setx path "%path%;c:\migw-bin-directory-path"

*(on my system migw-bin-directory-path is C:\mingw\mingw-w64\i686-8.1.0-posix-dwarf-rt_v6-rev0\mingw32\bin)*


Next navigate to the unzipped urho3d directory (CLUE: you should see folders like Android, Source, SourceAssets...)

Now run

> cmake_mingw.bat /path/to/build-tree [build-options]

where /path/to/build-tree is where CMake will be generating the build tree for the project and [build-options] are the build options as stated in the docs

an example you can use is this (this builds with default setting)

> cmake_mingw.bat build -DCMAKE_INSTALL_PREFIX=C:/urho3d_home

after the above command is done executing, navigate into the newly created build directory in your urho3d source dir and execute the below

> mingw32-make -f makefile

or if you want it installed directly then

> mingw32-make -f makefile install

If all goes good and fine then you should have built urho3d using mingw

-------------------------

Asimov500 | 2019-12-22 00:55:30 UTC | #24

@Bluemoon
I didn't need to set the path as mingw is already set as an environmental variable. So I followed the rest of your instructions.

I copied the source folder to my desktop.
I run cmake_mingw.bat build -DCMAKE_INSTALL_PREFIX=C:/urho3d_home
This created a folder called build in my source folder.

Opened a cmd window in that folder.
I then run mingw32-make -f makefile install
I was expecting a folder to appear in my C drive called Urho3d_home, but that didn't happen. I was guessing that is why you used the prefix to say where it is installed to. However I got errors in my command window. I have pasted a screen shot as it was easier than trying to type them here. Looking at the errors they seem to be the same errors I got when I tried to compile in codeblocks, but I could be wrong.
![urhoErrors2|690x374](upload://3GGY6QK4SKihkZEHBG9b5XFi0qp.jpeg)

-------------------------

SirNate0 | 2019-12-22 01:05:28 UTC | #25

Are you using mingw-w64? My memory may be wrong, but I think Urho had needed it for years. Also, the solution someone else found in the past was to use that version (the link Valdar posted earlier appears to be the same error you have now [https://discourse.urho3d.io/t/cmake-mingw-build-error/2961](https://discourse.urho3d.io/t/cmake-mingw-build-error/2961))

-------------------------

Asimov500 | 2019-12-22 01:12:35 UTC | #26

@SirNate0 
No I am pretty sure it is mingw32

I am a bit worried about upgrading to mingw64 as I have a lot of stuff written using the mingw32 compiler and I am worried some of my old stuff won't work if I change it. The version I am using was installed when I installed codeblocks.

Can I run both side by side so I can keep compatible with older projects?

-------------------------

Valdar | 2019-12-22 01:13:20 UTC | #27

IMO, you should be using MinGW-64 anyway. It is a completely separate product and has advantages beyond the 64 bit support. See this Wiki article: https://en.wikipedia.org/wiki/MinGW#MinGW-w64

And yes, you can set you compiler choice in Code::Blocks (per project iirc)

-------------------------

Asimov500 | 2019-12-22 01:16:57 UTC | #28

@Valdar
I will try it., and see if it works. Going to back up my old mingw folder first and have a go. Little worried as I have got a lot of projects using mingw, and some older stuff like the Chilli 2D framework that I am not sure works with the newer mingw. So here goes nothing LOL

-------------------------

SirNate0 | 2019-12-22 01:25:29 UTC | #29

If you just install mingw-w64 to a different directory (and maybe don't add it to the PATH) you shouldn't run into any issues for your old projects. I'm not certain, but I think you can then just use the full paths to specify the compiler (or the compiler prefix or something) with cmake to specify it for Urho3D.

-------------------------

Valdar | 2019-12-22 01:30:21 UTC | #30

Well, you definitely want your projects backed up, whether or not you install a new compiler. As for compatibility, I would think that MinGW-64 should compile all of your old stuff as well (unless you have some projects that are 32 -bit specific).

-------------------------

Asimov500 | 2019-12-22 01:33:51 UTC | #31

@Valdar
Well of course my projects are all backed up on another drive, but I am a believer in backing things up a few times when I make a big change.
Anyway it is nearly 1.33am here so gonna look into this in the morning now.
Think I need bed.
Thanks

-------------------------

weitjong | 2019-12-22 03:30:09 UTC | #32

[quote="Asimov500, post:24, topic:5769"]
I copied the source folder to my desktop.
I run cmake_mingw.bat build -DCMAKE_INSTALL_PREFIX=C:/urho3d_home
This created a folder called build in my source folder.

Opened a cmd window in that folder.
I then run mingw32-make -f makefile install
I was expecting a folder to appear in my C drive called Urho3d_home, but that didn’t happen.
[/quote]

The command you entered will generate the Urho3D build tree in the "build" directory and only after you have successfully built and installed the engine then the build artifacts will be installed to somewhere in "C:\urho3d_home". The Urho3D game engine is designed to work directly from the build tree too. So, if you like you can skip the installation part and just use the build tree as your URHO3D_HOME.

I have read user reporting that a version of MinGW packaged by a vendor,which I cannot recall now, actually works too. There are quite a few vendors trying to port Linux tools to Windows platform with varying quality. But I agree with the rest, the MinGW-W64 is an improved version of MinGW and you will get less problem with it. The one being tested extensively by our CI is the MinGW-W64 packaged in the https://sourceforge.net/projects/mingw-w64/. And, don't let the name fools you. The MinGW-W64 is multi-lib capable, so it could target both 32-bit and 64-bit Windows. On Linux it is just a matter of giving the "-m32" or "-m64" compiler flag. However, on Windows the last time I checked I could not get multi-lib working and I ended up downloading one version of MinGW-W64 for 32-bit and another for 64-bit. Having said that, the new package may have caught up with respect to the the multi-lib capability. Good luck.

-------------------------

Asimov500 | 2019-12-22 11:18:50 UTC | #33

@weitjong
Well I have now installed mingw-64 and tested it with a few of my older projects, and good news is that my older projects still run. I had to change a couple of path variables in codeblocks and I had to change the path variable in the environment as well, as the new mingw put the mingw32 inside a sub folder, so that wasn't too hard. Also had to update the executable names too as the new mingw changed the name to i686-w64-mingw32-g++.exe as well.

So this time as you suggested I run mingw32-make -f makefile and it gives me an error.
It is looking for a file called SDL_winm.c.obj in the winnm folder. Now the folder exists, but the file is not there. Good news is that my mingw32-make is working after updating the environment. Bad news is that I don't know why the file is not there.
![urhoAudioFail|690x147](upload://b3VLSA1XRezve8zlOAbOGULpBYr.jpeg)

-------------------------

weitjong | 2019-12-22 11:21:48 UTC | #34

After you changing the compiler toolchain the build tree needs to be generated again from scratch. Nuke the old build tree before doing anything else.

-------------------------

Asimov500 | 2019-12-22 23:35:50 UTC | #35

@weitjong
@Bluemoon
Well I think it compiled. Well it took ages and lots of lines scrolled up, and it built the demos, and the demos worked, and it created the lib and include folders, with lotsa stuff in them.
So I made a Urho folder in my engines hard drive partition, and copied all the files there.
I created a new urho project with codeblocks using Bluemoon's wizard, but I am having a small error.
cannot find -lUrho3d_d
I thought the wizard would set this up for me. I think it is making the correct includes at the top.
> #include <Urho3D/Urho3D.h>
> #include <Urho3D/Engine/Application.h>
> #include <Urho3D/Engine/Engine.h>
> #include <Urho3D/Input/InputEvents.h>
> #include "Test2.h" 

I think it is having trouble linking the libary. In the linker settings I can see Urho3D_d though.
This could be that the wizard is old and not setup for the newer Urho3D.
@Bluemoon Can you tell me if your wizard still works. When I run the wizard it asks me for the location of the Urho3D directory and I directed it to the folder I created, where the lib and the include folders were.
I wonder if you could try it and let me know if it still works.

-------------------------

JTippetts1 | 2019-12-22 23:48:39 UTC | #36

Did you build a debug version if the urho library? The suffix _d means debug, so if you didn't build a debug library it wont find it. Change to release build type, or change your build settings to link to release build of urho. Or rebuild urho for debug.

-------------------------

Asimov500 | 2019-12-23 02:12:54 UTC | #37

@JTippetts1
I just followed Bluemoons instructions and used the following line to build it. 
[quote="Bluemoon, post:23, topic:5769"]
cmake_mingw.bat build -DCMAKE_INSTALL_PREFIX=C:/urho3d_home
[/quote]
Then I did this
mingw32-make -f makefile
and I copied all the files to my engines directory and pointed Bluemoons wizard to the folder which created some of the code.
![buildProb|690x388](upload://y7UftHJ7mD4zmnOyXTr0zkuEqPX.jpeg) 
Because I am new to the engine I followed blindly and not knowing what it would do, or how to set it to debug or release.
I did set codeblocks to debug though.
I then tried release in codeblocks and then I get hundreds of errors.

I at least know I can compile it now, but perhaps I have to re-compile with the correct options then?

P.S. I compiled it on the desktop and the demos worked there, but after copying the folder to my engines folder the demos won't work. So perhaps I need to build and compile where I am going to be using it then. Or the shortcuts need updating.

PPS. After getting it to successfully to compile using the cmd line, but I couldn't get a program to compile in codeblocks. I tried something else. I use the cmake gui like I did in a previous post, and this time it made it ok and then I run codeblocks and this time instead of an error it did compile fine. So I have no problem compiling the engine in codeblocks or command line, but I still can't get codeblocks to link to it correctly, unfortunately. I think I am close though.

-------------------------

Bluemoon | 2019-12-23 08:03:15 UTC | #38

:+1:  Yeah you are close enough and yes the wizard is up to date and it works well (I actually made sure it was updated after you posted this issue :smiley: )

It seems that you are selecting debug or both debug and release in the wizard setup page while your Urho3d build is release. 

Equally ensure that the lib folder of your Urho3d installation directory contains libUrho3D.a

-------------------------

Asimov500 | 2019-12-23 11:18:48 UTC | #39

@Bluemoon 
Yeh I did set the wizard to debug and release because normally while making your game you will want it to be debug mode, and then when you are finished you normally compile it in release mode. Yes it did have libUrho3D.a in the lib folder.

If my build is release, how do I go about compiling it with both release and debug?
As I said most people work in debug while developing and then compile to release when finshed.

-------------------------

Bluemoon | 2019-12-23 11:24:40 UTC | #40

You would need to first build a debug version of urho3d. This is done by setting the CMAKE_BUILD_TYPE to Debug  as shown below if using the command line:

> cmake_mingw.bat build -DCMAKE_INSTALL_PREFIX=C:/urho3d_home -DCMAKE_BUILD_TYPE=Debug

when this is done you should have a libUrho3D_d.a file in your Urho3d installation's lib folder.

-------------------------

Asimov500 | 2019-12-23 11:32:27 UTC | #41

@Bluemoon
I think I see it in CMake it is CMAKE_BUILD_TYPE which is set to release.

So can I compile it as release where I want to use it. Then do another compile in another folder for the debug version and then copy the libUrho3D_d.a to the same folder.

Wish they would make it so that it compiles debug and release libraries in one go. That is what irrlicht does.

-------------------------

Bluemoon | 2019-12-23 11:39:06 UTC | #42

[quote="Asimov500, post:41, topic:5769"]
So can I compile it as release where I want to use it. Then do another compile in another folder for the debug version and then copy the libUrho3D_d.a to the same folder.
[/quote]

Sure you can.

But it will be good if you can build a sample application in codeblocks using the Release build of Urho3D just to be sure your codeblocks setup is ok

-------------------------

Asimov500 | 2019-12-23 15:48:05 UTC | #43

@Bluemoon
Well because there are a few options in the wizard it took me some time to try all the options. To cut a long story short I use x64 and I tried opengl, directx9 which both wouldn't compile. So then I tried directx11 and I think that would have compiled but I got an error ERROR: Failed to add resource path 'CoreData', check the documentationon how to set the 'resource prefix path'.

So I think directx11 would have worked if I knew what this prefix path was. Not sure why opengl and directx9 failed though.

PS. copied the folders Coredata and Data to where my binary was and the program did run, but all I got was a black screen.

Here is a breakdown of what I have tried so far:-
one
x64
OpenGl
Bare

i686-w64-mingw32-g++.exe -LH:\Engines\Urho3D\lib -o bin\Release\one.exe obj\Release\one.o  -s  -lUrho3D -luser32 -lgdi32 -lwinmm -limm32 -lole32 -loleaut32 -lversion -luuid -lws2_32 -lopengl32 -mwindows
H:\Engines\Urho3D\lib/libUrho3D.a(D3D11Graphics.cpp.obj):D3D11Graphics.cpp:(.text+0x46ff): undefined reference to `D3D11CreateDevice@40'
H:\Engines\Urho3D\lib/libUrho3D.a(D3D11ShaderVariation.cpp.obj):D3D11ShaderVariation.cpp:(.text+0x1973): undefined reference to `IID_ID3D11ShaderReflection'
H:\Engines\Urho3D\lib/libUrho3D.a(D3D11ShaderVariation.cpp.obj):D3D11ShaderVariation.cpp:(.text+0x198c): undefined reference to `D3DReflect@16'
H:\Engines\Urho3D\lib/libUrho3D.a(D3D11ShaderVariation.cpp.obj):D3D11ShaderVariation.cpp:(.text+0x46e4): undefined reference to `D3DCompile@44'
H:\Engines\Urho3D\lib/libUrho3D.a(D3D11ShaderVariation.cpp.obj):D3D11ShaderVariation.cpp:(.text+0x49a1): undefined reference to `D3DStripShader@16'
collect2.exe: error: ld returned 1 exit status

-----
two
x64
Direct3D9
Bare

i686-w64-mingw32-g++.exe -LH:\Engines\Urho3D\lib -o bin\Release\two.exe obj\Release\two.o  -s  -lUrho3D -luser32 -lgdi32 -lwinmm -limm32 -lole32 -loleaut32 -lversion -luuid -lws2_32 -ld3d9 -ld3dcompiler -mwindows
H:\Engines\Urho3D\lib/libUrho3D.a(D3D11Graphics.cpp.obj):D3D11Graphics.cpp:(.text+0x46ff): undefined reference to `D3D11CreateDevice@40'
H:\Engines\Urho3D\lib/libUrho3D.a(D3D11ShaderVariation.cpp.obj):D3D11ShaderVariation.cpp:(.text+0x1973): undefined reference to `IID_ID3D11ShaderReflection'
collect2.exe: error: ld returned 1 exit status

----
three
x64
Direct3D11
Bare
ERROR: Failed to add resource path 'CoreData', check the documentationon how to set the 'resource prefix path'
I then copied the folders Coredata and Data to where my binary was and the program did run, but all I got was a black screen.

-------------------------

Bluemoon | 2019-12-23 15:47:54 UTC | #44

try x86 OpenGL because from what I see your compiler is a 32bit compiler

-------------------------

Asimov500 | 2019-12-23 16:04:39 UTC | #45

@Bluemoon
Yeh I tried x86 OpenGl but I get lots of errors and it won't compile.

I have managed to compile so far using x86 and x64 directx11. When I say it compiles it makes an exe .
However when I run the exe I get the error ERROR: Failed to add resource path ‘CoreData’, check the documentationon how to set the ‘resource prefix path’ so then I copied the folders CoreData and Data to my bin folder. Then it run without error and opened full screen, but all I saw was black, so I am guessing it is working but not able to load in the models in the wizard demo. Can you tell me what I am supposed to see when I run the wizard, perhaps just opening the window is all it is supposed to do?

Will past my opengl error
> ||=== Build: Release in opengl (compiler: GNU GCC Compiler) ===|
> H:\Engines\Urho3D\include\Urho3D\Urho3D.h|29|warning: "URHO3D_SSE" redefined|
> ||note: this is the location of the previous definition|
> H:\Engines\Urho3D\include\Urho3D\Math\MathDefs.h||In function 'unsigned int Urho3D::FloatToRawIntBits(float)':|
> H:\Engines\Urho3D\include\Urho3D\Math\MathDefs.h|97|warning: dereferencing type-punned pointer will break strict-aliasing rules [-Wstrict-aliasing]|
> H:\Engines\Urho3D\include\Urho3D\Math\MathDefs.h||In function 'float Urho3D::HalfToFloat(short unsigned int)':|
> H:\Engines\Urho3D\include\Urho3D\Math\MathDefs.h|288|warning: dereferencing type-punned pointer will break strict-aliasing rules [-Wstrict-aliasing]|
> H:\Engines\Urho3D\include\Urho3D\Core\Variant.h||In member function 'Urho3D::Variant& Urho3D::Variant::operator=(long long int)':|
> H:\Engines\Urho3D\include\Urho3D\Core\Variant.h|490|warning: dereferencing type-punned pointer will break strict-aliasing rules [-Wstrict-aliasing]|
> H:\Engines\Urho3D\include\Urho3D\Core\Variant.h||In member function 'Urho3D::Variant& Urho3D::Variant::operator=(long long unsigned int)':|
> H:\Engines\Urho3D\include\Urho3D\Core\Variant.h|498|warning: dereferencing type-punned pointer will break strict-aliasing rules [-Wstrict-aliasing]|
> H:\Engines\Urho3D\include\Urho3D\Core\Variant.h||In member function 'Urho3D::Variant& Urho3D::Variant::operator=(double)':|
> H:\Engines\Urho3D\include\Urho3D\Core\Variant.h|538|warning: dereferencing type-punned pointer will break strict-aliasing rules [-Wstrict-aliasing]|
> H:\Engines\Urho3D\include\Urho3D\Core\Variant.h||In member function 'Urho3D::Variant& Urho3D::Variant::operator=(const Urho3D::Vector2&)':|
> H:\Engines\Urho3D\include\Urho3D\Core\Variant.h|546|warning: dereferencing type-punned pointer will break strict-aliasing rules [-Wstrict-aliasing]|
> H:\Engines\Urho3D\include\Urho3D\Core\Variant.h||In member function 'Urho3D::Variant& Urho3D::Variant::operator=(const Urho3D::Vector3&)':|
> H:\Engines\Urho3D\include\Urho3D\Core\Variant.h|554|warning: dereferencing type-punned pointer will break strict-aliasing rules [-Wstrict-aliasing]|
> H:\Engines\Urho3D\include\Urho3D\Core\Variant.h||In member function 'Urho3D::Variant& Urho3D::Variant::operator=(const Urho3D::Vector4&)':|
> H:\Engines\Urho3D\include\Urho3D\Core\Variant.h|562|warning: dereferencing type-punned pointer will break strict-aliasing rules [-Wstrict-aliasing]|
> H:\Engines\Urho3D\include\Urho3D\Core\Variant.h||In member function 'Urho3D::Variant& Urho3D::Variant::operator=(const Urho3D::Quaternion&)':|
> H:\Engines\Urho3D\include\Urho3D\Core\Variant.h|570|warning: dereferencing type-punned pointer will break strict-aliasing rules [-Wstrict-aliasing]|
> H:\Engines\Urho3D\include\Urho3D\Core\Variant.h||In member function 'Urho3D::Variant& Urho3D::Variant::operator=(const Urho3D::Color&)':|
> H:\Engines\Urho3D\include\Urho3D\Core\Variant.h|578|warning: dereferencing type-punned pointer will break strict-aliasing rules [-Wstrict-aliasing]|
> H:\Engines\Urho3D\include\Urho3D\Core\Variant.h||In member function 'Urho3D::Variant& Urho3D::Variant::operator=(const Urho3D::String&)':|
> H:\Engines\Urho3D\include\Urho3D\Core\Variant.h|586|warning: dereferencing type-punned pointer will break strict-aliasing rules [-Wstrict-aliasing]|
> H:\Engines\Urho3D\include\Urho3D\Core\Variant.h||In member function 'Urho3D::Variant& Urho3D::Variant::operator=(const char*)':|
> H:\Engines\Urho3D\include\Urho3D\Core\Variant.h|594|warning: dereferencing type-punned pointer will break strict-aliasing rules [-Wstrict-aliasing]|
> H:\Engines\Urho3D\include\Urho3D\Core\Variant.h||In member function 'Urho3D::Variant& Urho3D::Variant::operator=(const Urho3D::PODVector<unsigned char>&)':|
> H:\Engines\Urho3D\include\Urho3D\Core\Variant.h|602|warning: dereferencing type-punned pointer will break strict-aliasing rules [-Wstrict-aliasing]|
> H:\Engines\Urho3D\include\Urho3D\Core\Variant.h||In member function 'Urho3D::Variant& Urho3D::Variant::operator=(const Urho3D::ResourceRef&)':|
> H:\Engines\Urho3D\include\Urho3D\Core\Variant.h|621|warning: dereferencing type-punned pointer will break strict-aliasing rules [-Wstrict-aliasing]|
> H:\Engines\Urho3D\include\Urho3D\Core\Variant.h||In member function 'Urho3D::Variant& Urho3D::Variant::operator=(const Urho3D::ResourceRefList&)':|
> H:\Engines\Urho3D\include\Urho3D\Core\Variant.h|629|warning: dereferencing type-punned pointer will break strict-aliasing rules [-Wstrict-aliasing]|
> H:\Engines\Urho3D\include\Urho3D\Core\Variant.h||In member function 'Urho3D::Variant& Urho3D::Variant::operator=(const VariantVector&)':|
> H:\Engines\Urho3D\include\Urho3D\Core\Variant.h|637|warning: dereferencing type-punned pointer will break strict-aliasing rules [-Wstrict-aliasing]|
> H:\Engines\Urho3D\include\Urho3D\Core\Variant.h||In member function 'Urho3D::Variant& Urho3D::Variant::operator=(const StringVector&)':|
> H:\Engines\Urho3D\include\Urho3D\Core\Variant.h|645|warning: dereferencing type-punned pointer will break strict-aliasing rules [-Wstrict-aliasing]|
> H:\Engines\Urho3D\include\Urho3D\Core\Variant.h||In member function 'Urho3D::Variant& Urho3D::Variant::operator=(const VariantMap&)':|
> H:\Engines\Urho3D\include\Urho3D\Core\Variant.h|653|warning: dereferencing type-punned pointer will break strict-aliasing rules [-Wstrict-aliasing]|
> H:\Engines\Urho3D\include\Urho3D\Core\Variant.h||In member function 'Urho3D::Variant& Urho3D::Variant::operator=(const Urho3D::Rect&)':|
> H:\Engines\Urho3D\include\Urho3D\Core\Variant.h|661|warning: dereferencing type-punned pointer will break strict-aliasing rules [-Wstrict-aliasing]|
> H:\Engines\Urho3D\include\Urho3D\Core\Variant.h||In member function 'Urho3D::Variant& Urho3D::Variant::operator=(const Urho3D::IntRect&)':|
> H:\Engines\Urho3D\include\Urho3D\Core\Variant.h|669|warning: dereferencing type-punned pointer will break strict-aliasing rules [-Wstrict-aliasing]|
> H:\Engines\Urho3D\include\Urho3D\Core\Variant.h|669|warning: dereferencing type-punned pointer will break strict-aliasing rules [-Wstrict-aliasing]|
> H:\Engines\Urho3D\include\Urho3D\Core\Variant.h||In member function 'Urho3D::Variant& Urho3D::Variant::operator=(const Urho3D::IntVector2&)':|
> H:\Engines\Urho3D\include\Urho3D\Core\Variant.h|677|warning: dereferencing type-punned pointer will break strict-aliasing rules [-Wstrict-aliasing]|
> H:\Engines\Urho3D\include\Urho3D\Core\Variant.h||In member function 'Urho3D::Variant& Urho3D::Variant::operator=(const Urho3D::IntVector3&)':|
> H:\Engines\Urho3D\include\Urho3D\Core\Variant.h|685|warning: dereferencing type-punned pointer will break strict-aliasing rules [-Wstrict-aliasing]|
> H:\Engines\Urho3D\include\Urho3D\Core\Variant.h||In member function 'bool Urho3D::Variant::operator==(long long int) const':|
> H:\Engines\Urho3D\include\Urho3D\Core\Variant.h|731|warning: dereferencing type-punned pointer will break strict-aliasing rules [-Wstrict-aliasing]|
> H:\Engines\Urho3D\include\Urho3D\Core\Variant.h||In member function 'bool Urho3D::Variant::operator==(long long unsigned int) const':|
> H:\Engines\Urho3D\include\Urho3D\Core\Variant.h|734|warning: dereferencing type-punned pointer will break strict-aliasing rules [-Wstrict-aliasing]|
> H:\Engines\Urho3D\include\Urho3D\Core\Variant.h|734|warning: comparison of integer expressions of different signedness: 'const long long unsigned int' and 'int' [-Wsign-compare]|
> H:\Engines\Urho3D\include\Urho3D\Core\Variant.h||In member function 'bool Urho3D::Variant::operator==(double) const':|
> H:\Engines\Urho3D\include\Urho3D\Core\Variant.h|743|warning: dereferencing type-punned pointer will break strict-aliasing rules [-Wstrict-aliasing]|
> H:\Engines\Urho3D\include\Urho3D\Core\Variant.h||In member function 'bool Urho3D::Variant::operator==(const Urho3D::Vector2&) const':|
> H:\Engines\Urho3D\include\Urho3D\Core\Variant.h|748|warning: dereferencing type-punned pointer will break strict-aliasing rules [-Wstrict-aliasing]|
> H:\Engines\Urho3D\include\Urho3D\Core\Variant.h||In member function 'bool Urho3D::Variant::operator==(const Urho3D::Vector3&) const':|
> H:\Engines\Urho3D\include\Urho3D\Core\Variant.h|754|warning: dereferencing type-punned pointer will break strict-aliasing rules [-Wstrict-aliasing]|
> H:\Engines\Urho3D\include\Urho3D\Core\Variant.h||In member function 'bool Urho3D::Variant::operator==(const Urho3D::Vector4&) const':|
> H:\Engines\Urho3D\include\Urho3D\Core\Variant.h|760|warning: dereferencing type-punned pointer will break strict-aliasing rules [-Wstrict-aliasing]|
> H:\Engines\Urho3D\include\Urho3D\Core\Variant.h||In member function 'bool Urho3D::Variant::operator==(const Urho3D::Quaternion&) const':|
> H:\Engines\Urho3D\include\Urho3D\Core\Variant.h|766|warning: dereferencing type-punned pointer will break strict-aliasing rules [-Wstrict-aliasing]|
> H:\Engines\Urho3D\include\Urho3D\Core\Variant.h||In member function 'bool Urho3D::Variant::operator==(const Urho3D::Color&) const':|
> H:\Engines\Urho3D\include\Urho3D\Core\Variant.h|772|warning: dereferencing type-punned pointer will break strict-aliasing rules [-Wstrict-aliasing]|
> H:\Engines\Urho3D\include\Urho3D\Core\Variant.h||In member function 'bool Urho3D::Variant::operator==(const Urho3D::String&) const':|
> H:\Engines\Urho3D\include\Urho3D\Core\Variant.h|778|warning: dereferencing type-punned pointer will break strict-aliasing rules [-Wstrict-aliasing]|
> H:\Engines\Urho3D\include\Urho3D\Core\Variant.h||In member function 'bool Urho3D::Variant::operator==(void*) const':|
> H:\Engines\Urho3D\include\Urho3D\Core\Variant.h|792|warning: dereferencing type-punned pointer will break strict-aliasing rules [-Wstrict-aliasing]|
> H:\Engines\Urho3D\include\Urho3D\Core\Variant.h||In member function 'bool Urho3D::Variant::operator==(const Urho3D::ResourceRef&) const':|
> H:\Engines\Urho3D\include\Urho3D\Core\Variant.h|800|warning: dereferencing type-punned pointer will break strict-aliasing rules [-Wstrict-aliasing]|
> H:\Engines\Urho3D\include\Urho3D\Core\Variant.h||In member function 'bool Urho3D::Variant::operator==(const Urho3D::ResourceRefList&) const':|
> H:\Engines\Urho3D\include\Urho3D\Core\Variant.h|806|warning: dereferencing type-punned pointer will break strict-aliasing rules [-Wstrict-aliasing]|
> H:\Engines\Urho3D\include\Urho3D\Core\Variant.h||In member function 'bool Urho3D::Variant::operator==(const VariantVector&) const':|
> H:\Engines\Urho3D\include\Urho3D\Core\Variant.h|812|warning: dereferencing type-punned pointer will break strict-aliasing rules [-Wstrict-aliasing]|
> H:\Engines\Urho3D\include\Urho3D\Core\Variant.h||In member function 'bool Urho3D::Variant::operator==(const StringVector&) const':|
> H:\Engines\Urho3D\include\Urho3D\Core\Variant.h|818|warning: dereferencing type-punned pointer will break strict-aliasing rules [-Wstrict-aliasing]|
> H:\Engines\Urho3D\include\Urho3D\Core\Variant.h||In member function 'bool Urho3D::Variant::operator==(const VariantMap&) const':|
> H:\Engines\Urho3D\include\Urho3D\Core\Variant.h|824|warning: dereferencing type-punned pointer will break strict-aliasing rules [-Wstrict-aliasing]|
> H:\Engines\Urho3D\include\Urho3D\Core\Variant.h||In member function 'bool Urho3D::Variant::operator==(const Urho3D::Rect&) const':|
> H:\Engines\Urho3D\include\Urho3D\Core\Variant.h|830|warning: dereferencing type-punned pointer will break strict-aliasing rules [-Wstrict-aliasing]|
> H:\Engines\Urho3D\include\Urho3D\Core\Variant.h||In member function 'bool Urho3D::Variant::operator==(const Urho3D::IntRect&) const':|
> H:\Engines\Urho3D\include\Urho3D\Core\Variant.h|836|warning: dereferencing type-punned pointer will break strict-aliasing rules [-Wstrict-aliasing]|
> H:\Engines\Urho3D\include\Urho3D\Core\Variant.h||In member function 'bool Urho3D::Variant::operator==(const Urho3D::IntVector2&) const':|
> H:\Engines\Urho3D\include\Urho3D\Core\Variant.h|842|warning: dereferencing type-punned pointer will break strict-aliasing rules [-Wstrict-aliasing]|
> H:\Engines\Urho3D\include\Urho3D\Core\Variant.h||In member function 'bool Urho3D::Variant::operator==(const Urho3D::IntVector3&) const':|
> H:\Engines\Urho3D\include\Urho3D\Core\Variant.h|848|warning: dereferencing type-punned pointer will break strict-aliasing rules [-Wstrict-aliasing]|
> H:\Engines\Urho3D\include\Urho3D\Core\Variant.h||In member function 'bool Urho3D::Variant::operator==(Urho3D::RefCounted*) const':|
> H:\Engines\Urho3D\include\Urho3D\Core\Variant.h|858|warning: dereferencing type-punned pointer will break strict-aliasing rules [-Wstrict-aliasing]|
> H:\Engines\Urho3D\include\Urho3D\Core\Variant.h||In member function 'int Urho3D::Variant::GetInt() const':|
> H:\Engines\Urho3D\include\Urho3D\Core\Variant.h|992|warning: dereferencing type-punned pointer will break strict-aliasing rules [-Wstrict-aliasing]|
> H:\Engines\Urho3D\include\Urho3D\Core\Variant.h||In member function 'long long int Urho3D::Variant::GetInt64() const':|
> H:\Engines\Urho3D\include\Urho3D\Core\Variant.h|1001|warning: dereferencing type-punned pointer will break strict-aliasing rules [-Wstrict-aliasing]|
> H:\Engines\Urho3D\include\Urho3D\Core\Variant.h|1007|warning: dereferencing type-punned pointer will break strict-aliasing rules [-Wstrict-aliasing]|
> H:\Engines\Urho3D\include\Urho3D\Core\Variant.h||In member function 'long long unsigned int Urho3D::Variant::GetUInt64() const':|
> H:\Engines\Urho3D\include\Urho3D\Core\Variant.h|1016|warning: dereferencing type-punned pointer will break strict-aliasing rules [-Wstrict-aliasing]|
> H:\Engines\Urho3D\include\Urho3D\Core\Variant.h|1022|warning: dereferencing type-punned pointer will break strict-aliasing rules [-Wstrict-aliasing]|
> H:\Engines\Urho3D\include\Urho3D\Core\Variant.h||In member function 'unsigned int Urho3D::Variant::GetUInt() const':|
> H:\Engines\Urho3D\include\Urho3D\Core\Variant.h|1035|warning: dereferencing type-punned pointer will break strict-aliasing rules [-Wstrict-aliasing]|
> H:\Engines\Urho3D\include\Urho3D\Core\Variant.h||In member function 'float Urho3D::Variant::GetFloat() const':|
> H:\Engines\Urho3D\include\Urho3D\Core\Variant.h|1052|warning: dereferencing type-punned pointer will break strict-aliasing rules [-Wstrict-aliasing]|
> H:\Engines\Urho3D\include\Urho3D\Core\Variant.h||In member function 'double Urho3D::Variant::GetDouble() const':|
> H:\Engines\Urho3D\include\Urho3D\Core\Variant.h|1063|warning: dereferencing type-punned pointer will break strict-aliasing rules [-Wstrict-aliasing]|
> H:\Engines\Urho3D\include\Urho3D\Core\Variant.h||In member function 'const Urho3D::Vector2& Urho3D::Variant::GetVector2() const':|
> H:\Engines\Urho3D\include\Urho3D\Core\Variant.h|1073|warning: dereferencing type-punned pointer will break strict-aliasing rules [-Wstrict-aliasing]|
> H:\Engines\Urho3D\include\Urho3D\Core\Variant.h||In member function 'const Urho3D::Vector3& Urho3D::Variant::GetVector3() const':|
> H:\Engines\Urho3D\include\Urho3D\Core\Variant.h|1076|warning: dereferencing type-punned pointer will break strict-aliasing rules [-Wstrict-aliasing]|
> H:\Engines\Urho3D\include\Urho3D\Core\Variant.h||In member function 'const Urho3D::Vector4& Urho3D::Variant::GetVector4() const':|
> H:\Engines\Urho3D\include\Urho3D\Core\Variant.h|1079|warning: dereferencing type-punned pointer will break strict-aliasing rules [-Wstrict-aliasing]|
> H:\Engines\Urho3D\include\Urho3D\Core\Variant.h||In member function 'const Urho3D::Quaternion& Urho3D::Variant::GetQuaternion() const':|
> H:\Engines\Urho3D\include\Urho3D\Core\Variant.h|1084|warning: dereferencing type-punned pointer will break strict-aliasing rules [-Wstrict-aliasing]|
> H:\Engines\Urho3D\include\Urho3D\Core\Variant.h||In member function 'const Urho3D::Color& Urho3D::Variant::GetColor() const':|
> H:\Engines\Urho3D\include\Urho3D\Core\Variant.h|1088|warning: dereferencing type-punned pointer will break strict-aliasing rules [-Wstrict-aliasing]|
> H:\Engines\Urho3D\include\Urho3D\Core\Variant.h||In member function 'const Urho3D::String& Urho3D::Variant::GetString() const':|
> H:\Engines\Urho3D\include\Urho3D\Core\Variant.h|1091|warning: dereferencing type-punned pointer will break strict-aliasing rules [-Wstrict-aliasing]|
> H:\Engines\Urho3D\include\Urho3D\Core\Variant.h||In member function 'const Urho3D::PODVector<unsigned char>& Urho3D::Variant::GetBuffer() const':|
> H:\Engines\Urho3D\include\Urho3D\Core\Variant.h|1096|warning: dereferencing type-punned pointer will break strict-aliasing rules [-Wstrict-aliasing]|
> H:\Engines\Urho3D\include\Urho3D\Core\Variant.h||In member function 'void* Urho3D::Variant::GetVoidPtr() const':|
> H:\Engines\Urho3D\include\Urho3D\Core\Variant.h|1108|warning: dereferencing type-punned pointer will break strict-aliasing rules [-Wstrict-aliasing]|
> H:\Engines\Urho3D\include\Urho3D\Core\Variant.h||In member function 'const Urho3D::ResourceRef& Urho3D::Variant::GetResourceRef() const':|
> H:\Engines\Urho3D\include\Urho3D\Core\Variant.h|1116|warning: dereferencing type-punned pointer will break strict-aliasing rules [-Wstrict-aliasing]|
> H:\Engines\Urho3D\include\Urho3D\Core\Variant.h||In member function 'const Urho3D::ResourceRefList& Urho3D::Variant::GetResourceRefList() const':|
> H:\Engines\Urho3D\include\Urho3D\Core\Variant.h|1122|warning: dereferencing type-punned pointer will break strict-aliasing rules [-Wstrict-aliasing]|
> H:\Engines\Urho3D\include\Urho3D\Core\Variant.h||In member function 'const VariantVector& Urho3D::Variant::GetVariantVector() const':|
> H:\Engines\Urho3D\include\Urho3D\Core\Variant.h|1128|warning: dereferencing type-punned pointer will break strict-aliasing rules [-Wstrict-aliasing]|
> H:\Engines\Urho3D\include\Urho3D\Core\Variant.h||In member function 'const StringVector& Urho3D::Variant::GetStringVector() const':|
> H:\Engines\Urho3D\include\Urho3D\Core\Variant.h|1134|warning: dereferencing type-punned pointer will break strict-aliasing rules [-Wstrict-aliasing]|
> H:\Engines\Urho3D\include\Urho3D\Core\Variant.h||In member function 'const VariantMap& Urho3D::Variant::GetVariantMap() const':|
> H:\Engines\Urho3D\include\Urho3D\Core\Variant.h|1140|warning: dereferencing type-punned pointer will break strict-aliasing rules [-Wstrict-aliasing]|
> H:\Engines\Urho3D\include\Urho3D\Core\Variant.h||In member function 'const Urho3D::Rect& Urho3D::Variant::GetRect() const':|
> H:\Engines\Urho3D\include\Urho3D\Core\Variant.h|1144|warning: dereferencing type-punned pointer will break strict-aliasing rules [-Wstrict-aliasing]|
> H:\Engines\Urho3D\include\Urho3D\Core\Variant.h||In member function 'const Urho3D::IntRect& Urho3D::Variant::GetIntRect() const':|
> H:\Engines\Urho3D\include\Urho3D\Core\Variant.h|1147|warning: dereferencing type-punned pointer will break strict-aliasing rules [-Wstrict-aliasing]|
> H:\Engines\Urho3D\include\Urho3D\Core\Variant.h||In member function 'const Urho3D::IntVector2& Urho3D::Variant::GetIntVector2() const':|
> H:\Engines\Urho3D\include\Urho3D\Core\Variant.h|1152|warning: dereferencing type-punned pointer will break strict-aliasing rules [-Wstrict-aliasing]|
> H:\Engines\Urho3D\include\Urho3D\Core\Variant.h||In member function 'const Urho3D::IntVector3& Urho3D::Variant::GetIntVector3() const':|
> H:\Engines\Urho3D\include\Urho3D\Core\Variant.h|1158|warning: dereferencing type-punned pointer will break strict-aliasing rules [-Wstrict-aliasing]|
> H:\Engines\Urho3D\include\Urho3D\Core\Variant.h||In member function 'Urho3D::RefCounted* Urho3D::Variant::GetPtr() const':|
> H:\Engines\Urho3D\include\Urho3D\Core\Variant.h|1164|warning: dereferencing type-punned pointer will break strict-aliasing rules [-Wstrict-aliasing]|
> H:\Engines\Urho3D\lib\libUrho3D.a(D3D11Graphics.cpp.obj):D3D11Graphics.cpp|| undefined reference to `D3D11CreateDevice@40'|
> H:\Engines\Urho3D\lib\libUrho3D.a(D3D11ShaderVariation.cpp.obj):D3D11ShaderVariation.cpp|| undefined reference to `IID_ID3D11ShaderReflection'|
> H:\Engines\Urho3D\lib\libUrho3D.a(D3D11ShaderVariation.cpp.obj):D3D11ShaderVariation.cpp|| undefined reference to `D3DReflect@16'|
> H:\Engines\Urho3D\lib\libUrho3D.a(D3D11ShaderVariation.cpp.obj):D3D11ShaderVariation.cpp|| undefined reference to `D3DCompile@44'|
> H:\Engines\Urho3D\lib\libUrho3D.a(D3D11ShaderVariation.cpp.obj):D3D11ShaderVariation.cpp|| undefined reference to `D3DStripShader@16'|
> ||error: ld returned 1 exit status|
> ||=== Build failed: 6 error(s), 71 warning(s) (0 minute(s), 5 second(s)) ===|

-------------------------

Bluemoon | 2019-12-23 16:35:06 UTC | #46

[quote="Asimov500, post:45, topic:5769"]
Then it run without error and opened full screen, but all I saw was black, so I am guessing it is working but not able to load in the models in the wizard demo. Can you tell me what I am supposed to see when I run the wizard, perhaps just opening the window is all it is supposed to do?
[/quote]

You are seeing a black window because you most probably selected "bare" for "Application Template Type". Bare presents you with a bare (skeletal) application for you to build on top. Try creating another project, but this time select "Navigating Camera" or "Orbiting Camera".

[quote="Asimov500, post:45, topic:5769"]
However when I run the exe I get the error ERROR: Failed to add resource path ‘CoreData’, check the documentationon how to set the ‘resource prefix path’ so then I copied the folders CoreData and Data to my bin folder.
[/quote]
I would have suggested you set the project's  "Execution working directory" to the urho3d folder that has CoreData and Data. But then I noticed that current releases of codeblocks fail set it up properly. So the way you went about it seems to be the known work around

[quote="Asimov500, post:45, topic:5769"]
Will past my opengl error
[/quote]
From what you pasted it seems you build Urho3D using D3D11. There is a file named Urho3D.pc. It is located in a pkgconfig folder inside the lib directory of the urho3d installation. 
Open the file and look for the line that starts with "Libs:" . Paste the content of that line here for us to see

-------------------------

Asimov500 | 2019-12-23 18:50:50 UTC | #47

@Bluemoon 
[quote="Bluemoon, post:46, topic:5769"]
There is a file named Urho3D.pc. It is located in a pkgconfig folder inside the lib directory of the urho3d installation.
Open the file and look for the line that starts with “Libs:” . Paste the content of that line here for us to see
[/quote]
In my lib directory I haven't got the pkgconfig folder just the libUrho3D.a file

Yeh I compiled one with the orbiting camera and I can see a floor and I can move around with the WASD keys. Quite smooth too.
> 
> From what you pasted it seems you build Urho3D using D3D11.

Well I did tick URHO3D_D3D11 thinking that I could then make opengl, directx9 and directx11 as well.
Was I wrong to tick that in CMAKE? I mean I could easily untick it and rebuild if that is the problem.
I intend my game to be Windows only  so I was going to use directx anyway, and when I saw D3D11 I thought I better tick it so I can use the latest directx.

If I release my game do I have to include the CoreData and Data with the exe?

I am thinking about making a youtube video going through all the problems I had getting it to work, so that I might help others once I get it all working.

-------------------------

Bluemoon | 2019-12-23 19:38:32 UTC | #48

[quote="Asimov500, post:47, topic:5769"]
Yeh I compiled one with the orbiting camera and I can see a floor and I can move around with the WASD keys. Quite smooth too.
[/quote]

Awesome so we are very much good to go

[quote="Asimov500, post:47, topic:5769"]
Well I did tick URHO3D_D3D11 thinking that I could then make opengl, directx9 and directx11 as well.
Was I wrong to tick that in CMAKE?
[/quote]
No there is absolutely nothing wrong with that. It is all part of Urho3D build option on windows: either OpenGL, D3D9 or D3D11

[quote="Asimov500, post:47, topic:5769"]
If I release my game do I have to include the CoreData and Data with the exe?
[/quote]

No you don't have to unless your executable makes use of one or more assets contained in them. Even at that your can have the assets in a different folder with a different name just make sure the ResourcePrefixPaths and ResourcePaths engine parameter are properly set

-------------------------

Asimov500 | 2019-12-23 23:38:49 UTC | #49

Thanks @Everyone and especially @Bluemoon.

Well now I can run and compile the program I can start reading the docs wherever they are and start learning the engine.

However @Bluemoon got one more question.
I built a bare project again, but even a bare project seemingly needs the resource paths of 
CoreData and Data.

As a test I commented out the lines
//engineParameters_["ResourcePaths"] = "CoreData;Data";
//engineParameters_["LogName"]   = "bare.log";

But it is still asking for the resource path of Data, but I can't see anything in the code which is asking for data.
I probably will need a data folder to keep my resources anyway, but I was wondering what in the code is looking for the Data folder resource.

I got it to run again by putting in an empty CoreData and Data folder. However because I have commented out the lines which set up the Resource paths I thought it shouldn't need to look for those folders.
Or have I missed something.

-------------------------

Bluemoon | 2019-12-23 23:48:54 UTC | #50

[quote="Asimov500, post:49, topic:5769"]
Thanks @Everyone and especially @Bluemoon
[/quote]

:grinning: It's good you can now join the party

[quote="Asimov500, post:49, topic:5769"]
However @Bluemoon got one more question.
I built a bare project again, but even a bare project seemingly needs the resource paths of
CoreData and Data.

As a test I commented out the lines
//engineParameters_[“ResourcePaths”] = “CoreData;Data”;
//engineParameters_[“LogName”] = “bare.log”;
[/quote]
If "ResourcePaths" engine parameter is not set the engine defaults to CoreData and Data. This happens whether the application is using resources from these folders or not. Also if you set it to another folder or sets of folders and the engine equally can't find them it will still default to CoreData and Data.

As a side note I've pushed an update to the wizard that makes it possible to execute, without error, a built application from the IDE after you must have set the right "Execution working directory" in the projects property

-------------------------

Asimov500 | 2019-12-24 00:01:54 UTC | #51

@Bluemoon 
[quote="Bluemoon, post:50, topic:5769"]
As a side note I’ve pushed an update to the wizard that makes it possible to execute, without error, a built application from the IDE after you must have set the right “Execution working directory” in the projects property
[/quote]
I will have to try the updated Wizard. More engines should have a wizard like this, because it saves messing about setting up the paths which you do everytime you set up a project. I do use Visual Studio at times, but I much the prefer the Codeblocks IDE. I just like the simplicity of the layout.

I changed that line to

> engineParameters_["ResourcePaths"] = "Data";

Which solved my problem, because I will definately be needing a Data folder later anyway.

Thanks again. I am going to make a youtube video explaining every step I did in the hope it will help someone else. Will probably be after Christmas as I have family coming down tomorrow.

Merry Christmas everyone.

-------------------------

Modanung | 2019-12-25 11:52:21 UTC | #52

Most of the documentation can be found [here](https://urho3d.github.io/documentation/HEAD/). :gift: There's also a - somewhat messy - [wiki](https://github.com/urho3d/urho3d/wiki), that you're free to improve of course. :star2: And be sure to have a look at the [samples](https://github.com/urho3d/Urho3D/tree/master/Source/Samples) that come with the engine, they can be quite informative. :christmas_tree:
If at any time QtCreator might catch your interest as an IDE, rest assured, there's [wizards](https://discourse.urho3d.io/t/wrench-class-and-project-wizards-for-qtcreator/2076) for that too. :snowman:

-------------------------

Asimov500 | 2019-12-25 17:44:48 UTC | #53

@Modanung
Thanks, much appreciated. I already have the QT IDE installed anyway because I have written a few QT apps, however I much prefer the Codeblock IDE so I use that whenever I can. The only thing I don't use Codeblocks for is imagemagic because for some reason that won't work in Codeblocks and so I do that in Visual Studio.

-------------------------

