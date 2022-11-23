gwald | 2017-01-02 01:00:31 UTC | #1

[url=http://urho3d.prophpbb.com/topic451.html#p2624]Read reattiva excellent QT Creator post![/url]
[url=http://urho3d.prophpbb.com/topic451-10.html#p2629]And weitjong tips[/url]

[url=http://www.ogre3d.org/tikiwiki/Integrating+API+documentation+into+Qt+Creator+Help]Last thing is the generating of the qch help file[/url]


Hello,
I just got the samples debugging in QT Creator and thought I'd share as it took me a while to figure it out  :unamused: 
It's not perfect, looks messy because of the sample cmake set up and I don't have much knowledge with cmake, but it works! 

Below is from my Linux (Mint) codebase from github, but I think it will work on any platform.
[code]
1. Open QC Creator and create new project.
2. Select Import Project on the left and Importing existing project on the right and click choose.
3. Browser to the Build directory of the sample (ie: /home/user/Urho3D-master/Build/Samples/01_HelloWorld) click ok
4. The name I give it is qtProjectName, ie qt01HelloWorld, so I can see what QT Creator creates, click next.
5. It will auto select most files, I only leave the Makefile ticked, click next and finish
You'll see your project loaded and ready to go
6. Click run or debug, a pop up will come up asking for the executable
7. Click browse and go to the Bin where the samples are, pick the corresponding executable, (ie /home/xp/Urho3D-master/Bin/01_HelloWorld), click okay and okay, it will run/debug the executable
8. To add the code, right click your main project folder and select add existing files
9. Browse to the source foleder (ie /home/xp/Urho3D-master/Source/Samples/01_HelloWorld)
10. Select your .h and .cpp files etc.
11. for zooming in to functions etc you need to put all of the source code directories into the include file in your project, ie:
             /home/user/Urho3D-master/Source/Engine/Engine
             /home/user/Urho3D-master/Source/Engine/Scene
              .....
             /home/user/Urho3D-master/Source/ThirdParty/AngelScript/include
             /home/user/Urho3D-master/Source/ThirdParty/AngelScript/source
             etc, etc, I just copy and paste from a file browser

12. Urho3D + QT Creator = profit ;) [/code]

Make sure you ran ./cmake_gcc.sh with
 -DURHO3D_SAMPLES=1 
to get the samples, and 
-DCMAKE_BUILD_TYPE=Debug
for debugging!

If anyone knows of a better way, please let us know  :ugeek: 
I'm still new to the engine.. so WIP


Edit #1
For step 11, creating your include file paths, I just use this:
[code]tree -dfi /home/user/Urho3D-master/Source/   > all.txt[/code]
copy and paste the content of all.txt and just remove the sample folders etc

You might need to install it, ie debian based:
[quote]sudo apt-get install tree[/quote]

Edit #2 Adding CHM file to QT Creator

You need to have doxygen and the graphics tools installed:
[code]apt-get install doxygen graphviz[/code]

You'll need the qhelpgenerator tool to convert it to qt help format.
[code]apt-get install qt4-dev-tools[/code]

You need to manually run:
 qhelpgenerator index.qhp -o index.qch

In the /Urho3D-master/build/Docs run: make doc to create the helps files.
index.qhp will be created in /Urho3D-master/build/Docs/html

-------------------------

weitjong | 2017-01-02 01:00:32 UTC | #2

I have never used QtCreator before, so I am quite surprised to know that it cannot handle multiple executables (targets) in one Qt project. Eclipse is my preferred IDE when I am on Linux build system. It could import the CMake generated project file as a whole into its workspace and allow code browsing and running/debugging of all the samples in one place.

Anyway, the reason why I reply your post is to let you know that you may still miss a few source files in your step 11 because a number of source files are generated on the fly. So, they are only located somewhere in the build/ directory instead of Source/ directory.

-------------------------

gwald | 2017-01-02 01:00:32 UTC | #3

[quote="weitjong"]cannot handle multiple executables (targets) in one Qt project[/quote]
da what?  :laughing: 

Still new to QT creator, urho3d, cmake, github and c++ lol... 
I like eclipse, I use it a work (java) but got into the habit of liking QT creator for C/C++ on linux.
But I like code::block in windows  :confused: 
So.. yeah options.
Starting a new project, I'll just copy the samples cmake but make the executable in the same directory, no biggy.
Thanks for the info, BTW

-------------------------

weitjong | 2017-01-02 01:00:32 UTC | #4

Saw your uploaded YouTube videos. Thanks for that. I have never commented on YouTube, so I do it here. You can also setup NinjaSnowWar to start in client/server networking mode. Hope to see more video from you.

-------------------------

boberfly | 2017-01-02 01:00:32 UTC | #5

Hi gwald,

There's a much easier way. Just use cmake_codeblocks.sh, QtCreator can detect this and set-up your project automatically. It's what I use with Urho3D, much faster than eclipse and the debugger works very similar to MSVC.

Happy coding.
-Alex

-------------------------

rasteron | 2017-01-02 01:00:32 UTC | #6

Nice guide. I was a Code::Blocks user before but when I got started creating Qt projects and using Qt Creator I never looked back  :sunglasses:

-------------------------

gwald | 2017-01-02 01:00:32 UTC | #7

[quote="weitjong"]Saw your uploaded YouTube videos. Thanks for that. I have never commented on YouTube, so I do it here. You can also setup NinjaSnowWar to start in client/server networking mode. Hope to see more video from you.[/quote]

No probs, that NinjaSnowWar is one impressive script!  :laughing: 
Sure!

[quote="boberfly"]Hi gwald,

There's a much easier way. Just use cmake_codeblocks.sh, QtCreator can detect this and set-up your project automatically. It's what I use with Urho3D, much faster than eclipse and the debugger works very similar to MSVC.

Happy coding.
-Alex[/quote]

Wow sounds too good to be true! I'll try it out for sure!
Thanks :slight_smile:


[quote="rasteron"]Nice guide. I was a Code::Blocks user before but when I got started creating Qt projects and using Qt Creator I never looked back  :sunglasses:[/quote]
Code::Blocks reminds me of VS6, the good all simple days  :laughing: But still being modern and flexible ! 
I wish qt creator supported multi monitors.. I've seen it talked about on their forums so maybe it will come soon.


Anyone know how to compile the CHM help file in linux? QT Creator has a great interface for CHM files!

-------------------------

empirer64 | 2017-01-02 01:00:33 UTC | #8

[quote="boberfly"]Hi gwald,

There's a much easier way. Just use cmake_codeblocks.sh, QtCreator can detect this and set-up your project automatically. It's what I use with Urho3D, much faster than eclipse and the debugger works very similar to MSVC.

Happy coding.
-Alex[/quote]

Hi guys, 
I am new to Urho, can u please write some more detailed guideline on how to setup Urho with QtCreator through cmake_codeblocks.

Thx

-------------------------

gwald | 2017-01-02 01:00:33 UTC | #9

[quote="empirer64"]
Hi guys, 
I am new to Urho, can u please write some more detailed guideline on how to setup Urho with QtCreator through cmake_codeblocks.

Thx[/quote]
Welcome!
I upgraded to the latest version of QT Creator, but couldn't get the samples to import using the codeblocks project file.
I bit the bullet and intalled codeblocks to step through the samples.. works great, and all in one project.

Also QT creator doesn't use CHM like I thought it uses .QHC file. the exe to generate the docs is part of the QT framework and not part of creator  :neutral_face: 
Easier to get it using the windows gui.

[quote="boberfly"] QtCreator can detect this and set-up your project automatically. [/quote]
I too would like more info on this

-------------------------

reattiva | 2017-01-02 01:00:43 UTC | #10

I can post a guide for QtCreator + CMake + mingw + OpenGL in windows 32 bits, no guarantee.

You'll need QtCreator (3.2.1 tested), Cmake (2.8 tested), MinGW GCC (4.9.1 tested).
For mingw, you can use mingw-w64, TDM-GCC (but some DX headers are missing), nuwen.net ...
You need to choose an exception handling (sjlj, dwarf) and pthreads or win32, for example I've used this:
[sourceforge.net/projects/mingw-w ... n32/dwarf/](http://sourceforge.net/projects/mingw-w64/files/Toolchains%20targetting%20Win32/Personal%20Builds/mingw-builds/4.9.1/threads-win32/dwarf/)
The mingw bin folder must be added to the system path.

[b]Mingw and cmake check[/b]
- run "cmd" -> type "g++ --version" --> "g++ (i686-win32-dwarf-rev1, Built by MinGW-W64 project) 4.9.1"
- run "cmd" -> type "cmake --version" --> "cmake version 2.8.12"

[b]Create a QtCreator Kit[/b]
- run QtCreator 
- Menu Tools -> Options... -> Build & Run -> Compilers
  you should have a MinGW entry in the Auto-detected section, 
  if not: Add -> MinGW -> Compiler path: select the file <MINGW path>\bin\g++.exe
- Menu Tools -> Options... -> Build & Run -> Debuggers
  Add -> Path: select the file <MINGW path>\bin\gdb.exe
- Menu Tools -> Options... -> Build & Run -> Kits
  Name: MINGW (for example)
  Compiler: select the compiler just added
  Debugger: select the debugger just added
  
[b]Open CMake and build[/b]
- Open Project, select the file:
   <Urho3D path>\Source\CMakeLists.txt
  Build location (for example):
   <Urho3D path>\Build
  Arguments (for example):
   -DCMAKE_BUILD_TYPE=Debug -DURHO3D_OPENGL=1 -DURHO3D_SAMPLES=1
  Generator:
   MinGW Generator (<Your kit name>)
- Click "Run CMake", the last messages should be:
  Configuring done
  Generating done
  Build files have been written to ...
- Click "Finish"
- Build All

[b]Speed up[/b]
To compile a single target for example only the sample HelloWorld:
- Projects icon (on the left toolbar) -> Build Settings -> 
  the current configuration should be "all"
- Add -> Clone Selected
- give it a name, for example "HelloWorld"
- Build steps -> click Details
- select the target you need ("01_HelloWorld")
- you can do the same on the Clean Steps but I couldn't make it work, it will clear all its dependencies
Now when you build the project it will build HelloWorld and all its dependencies.
To skip the dependencies check and be on your own, you can:
- Projects icon -> Build Settings -> Build steps -> click Details
- remove the check on "01_HelloWorld"
- in "Additional arguments" type "01_HelloWorld/fast"

Some notes:
- there is this plugin [github.com/seiyar81/cmakeprojectmanager](https://github.com/seiyar81/cmakeprojectmanager) not tested, maybe old
- Qt has a new building system, qbs

-------------------------

weitjong | 2017-01-02 01:00:44 UTC | #11

Thanks for the guide. It is just the incentive I need to get me to try out something new. It is the first time I install and use QtCreator in my Linux 64-bit system and so far my experience has been pleasant. YMMV, but since I have all the necessary software packages already installed, all I need to do is let the QtCreator knows where to find my CMake installation. Under the Auto-detection in the QtCreator settings, it already detects both my 64-bit and 32-bit GCC and Clang native toolchain out of the box. It does not, however, detect my other cross-compiling toolchains, but I guess that what the "Add" button is for.

On my first try, I use QtCreator to invoke the CMake as per above guide but choosing "Unix generator" (for my case). The project builds and debugs as I would expect it. Thanks again for the guide. BTW, I have to alter the build settings to add an extra argument "-j8" for the "make" command to take advantage of all the available CPU threads in my system. If you have multi-core CPU with Intel HT technology, I am sure you don't want to skip this part.

The generated Build directory looks to be similar to me and interestingly it generated a Code-Block project file (Urho3D.cbp file). So, in my second attempt, I would like to see if it works with Build tree generated from our existing cmake_xxxx.sh script. I deleted the Build directory but keep the "Source/CMakeLists.txt.user" file created by QtCreator after the first CMake invocation. I called cmake_eclipse.sh (cmake_gcc.sh would do the same here) to get the Build tree regenerated and then cmake_codeblock.sh to get the Urho3D.cbp file. And it was a success, QtCreator is able to reopen the "project". With this setup, the same build tree can be opened by Eclipse, Code-Block, and QtCreator, and it also works when on command line using "cd Build && make -j8".

Thing I especially like is its editor has a fake-VIM option. I could use it as a replacement for Eclipse if only I can retrain my finger muscle for those shortcuts :slight_smile:. In any case, it works much better than Qt own *.pro project file that OP has led me to believe.

-------------------------

gwald | 2017-01-02 01:00:44 UTC | #12

[quote="reattiva"]I can post a guide for QtCreator + CMake + mingw + OpenGL in windows 32 bits, no guarantee.[/quote]
Impressive! many thanks, hopefully this weekend I can try it out  :stuck_out_tongue: 
I'll put a link to your post from the first post  :wink: 

[quote="weitjong"] In any case, it works much better than Qt own *.pro project file that OP has led me to believe.[/quote]

Sorry, I'm a newb, I did stated that.. it's the only way I knew at the time to get a working QT project.. anway.. we're all in QT Creator heaven now  :laughing:

-------------------------

weitjong | 2017-01-02 01:00:44 UTC | #13

I have successfully modified our existing "doc" target to generate qch file and have tested successfully to add it into Qt help system. I will check in my changes once I have completed the test on the chm file generation as well.

-------------------------

gwald | 2017-01-02 01:00:46 UTC | #14

[quote="weitjong"]I have successfully modified our existing "doc" target to generate qch file and have tested successfully to add it into Qt help system. I will check in my changes once I have completed the test on the chm file generation as well.[/quote]

Thank you :slight_smile:
Your a legend!
 :mrgreen:

-------------------------

weitjong | 2017-01-02 01:00:47 UTC | #15

[quote="gwald"]Thank you :slight_smile:
Your a legend!
 :mrgreen:[/quote]

Nah! This work is nothing compared to works done by others. If I were a legend then the other were "Gods". We mere mortal have to be humble in front of them :slight_smile:.

I was out of town and just managed to check in my changes today. I did not fully test the *.chm generation on the Windows platform as I originally had planned because I don't want to risk myself to download the help compiler tool from an unknown source (at least to me). The IDE-specific help documentation is generated by using "doc" built-in target as I communicated earlier. I suspect that QtCreator uses CMake/Code::Block generator to account for the fact that it generates the *.cbp file in the build tree. So, I scripted the 'doc' custom target to turn on for *.qch generation when it detects the IDE is Code::Block. As it is, the "doc" target will enable the generation of the help documentation for one of the following IDEs: XCODE, MSVC, Eclipse, and Code::Block / QtCreator. So, pick your own poison well :slight_smile:.

-------------------------

gwald | 2017-01-02 01:00:48 UTC | #16

[quote="weitjong"][quote="gwald"]Thank you :slight_smile:
Your a legend!
 :mrgreen:[/quote]

Nah! This work is nothing compared to works done by others. If I were a legend then the other were "Gods". We mere mortal have to be humble in front of them :slight_smile:.
[/quote]
Too modest.. both you and empirer64 and yes all the contributes here and on github :slight_smile:

Yeah, The qhelpgenerator for windows is part of the QT library (500+MB), I can zip it up and upload it to dropbox, it's opensourced so I don't think there's any harm... it's a small exe.
For linux,the generator is packaged in a small (less then 5mb) package: qt4-dev-tools or qt5-dev-tools , doing a force install works and is usable.

I'm hoping to have time on the weekend so I can give all this new info a try :slight_smile:

-------------------------

gwald | 2017-01-02 01:09:09 UTC | #17

[quote="weitjong"]I have successfully modified our existing "doc" target to generate qch file and have tested successfully to add it into Qt help system. I will check in my changes once I have completed the test on the chm file generation as well.[/quote]

Hello again :slight_smile:

I've just downloaded from github and tried it out, it creates the .qhp (project files), but doesn't create the help file on my mint linux.. no big deal tho I just ran:
qhelpgenerator index.qhp -o index.qch

And it worked, thanks again you saved me from going to the darkside (Windows).

Wait, I just saw a /Docs/qch folder and there it was!
Nice

-------------------------

