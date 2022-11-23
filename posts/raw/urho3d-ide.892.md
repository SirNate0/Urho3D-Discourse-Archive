scorvi | 2017-01-02 01:03:51 UTC | #1

hey ho 

i am working on implementing an IDE / Editor for urho3d. It is in the most parts just an c++ implementation of the angelscript editor.

for insperation, i am looking at [github.com/AtomicGameEngine/AtomicGameEngine](https://github.com/AtomicGameEngine/AtomicGameEngine)

here are some screenshots: [imgur.com/a/iQazt](http://imgur.com/a/iQazt)

Features added:
[ul]Project Manager
IDE Framework
MenuBar
ToolBar
MiniToolBar
Hierarchy Window
Attribute Window
Project Window[/ul]

WIP Features:
[ul]
TabWindow
3d View tab
3d Editor
Editor Plugin System
[/ul]
other Features:
[ul]gui editor
2d View tab
2d Editor 
node canvas
Component specific editors
Resource Editor 
Importing / Exporting
Language Editor 
Text/Script Editor tab[/ul]

i am implementing an Editor Plugin System like that used in godot. so that someone can implement an editor that only works with a specific component or resource type. 

the editor specific stuff will be also used in the in game editor .... it will be just like the scripted editor only that you can open this editor in your game if you want to test or manipulate your scene. 

after the WIP Features are added i will work on an GUI editor plugin so that i can improve the look of the editor :-/ . (i allready added an implementation of memononen/nanosvg to urho3d so that you can load a svg file like a texture ...  and added a memononen/nanovg GUI Renderer that uses the native opengl implementation ... i failed to port that to uhro ) 

is this needed ? i can put the source code online if someone wants to help ....

-------------------------

hdunderscore | 2017-01-02 01:03:52 UTC | #2

Oh wow that's really exciting, sounds like you've made some good progress on multiple fronts that I know a few of us were individually thinking about.

Please do share, I'd be interested in taking a look. In particular the Project manager and nanovg work you've done interest me.

-------------------------

cadaver | 2017-01-02 01:03:52 UTC | #3

This looks like it has potential to be awesome. I agree, please do share.

Have you structured it as a separate application that uses Urho? Some of the stuff would not be acceptable in Urho itself without improvements (for example opengl-only rendering for nanovg) but naturally in a separate project everything is fine.

-------------------------

GoogleBot42 | 2017-01-02 01:03:53 UTC | #4

I would really like to see something like this.  This would help those who are new to Urho3D pick it up quicker and also could increase the speed of workflow.  :slight_smile:

-------------------------

thebluefish | 2017-01-02 01:03:53 UTC | #5

Looks good so far!

I am working on implementing oui-blendish (based on nanovg) for use within an editor, and then I was planning on expanding my current editor with more Urho3D-centric functionality. It looks like you went ahead and did all of that already though, but I'm still interested in giving the blending look.

-------------------------

scorvi | 2017-01-02 01:03:54 UTC | #6

it is a separate application and i will share this sometime this week ... must remove old test / debug code. 

@thebluefish : i wanted to use nanovg as an skin texture renderer for the uhro3d ui system. so you can define a skin style xml file and the nanovg creates the ui.png texture that you can use .... so you could do the oui-blendish ui ... but that is only in the idea stage ^^

-------------------------

NiteLordz | 2017-01-02 01:03:54 UTC | #7

I have also been working on a c++ Editor, that functions like Unity.  Currently i am updating my system, but when i get a chance, i will post screen shots. 

It is built using Qt for cross platform UI support. If anyone is interested in checking out the code, i have it hosted on my VSO account, but can give you access to it.

-------------------------

NiteLordz | 2017-01-02 01:03:55 UTC | #8

Screen Shots of the Unity Clone i am working on

[1drv.ms/1F4RDpQ](http://1drv.ms/1F4RDpQ)

For anyone interested in working on this, i am using an Agile template inside of VSO as i am experimenting with the process.  All code is built on the Urho3D design, however the engine itself has been modified to use Direct3D 11 and OpenGL 4.0

-------------------------

vivienneanthony | 2017-01-02 01:03:55 UTC | #9

[quote="NiteLordz"]Screen Shots of the Unity Clone i am working on

[1drv.ms/1F4RDpQ](http://1drv.ms/1F4RDpQ)

For anyone interested in working on this, i am using an Agile template inside of VSO as i am experimenting with the process.  All code is built on the Urho3D design, however the engine itself has been modified to use Direct3D 11 and OpenGL 4.0[/quote]

Nice..

-------------------------

vivienneanthony | 2017-01-02 01:03:55 UTC | #10

I'm willing to help with a editor. I'm not familiar to angelscript but c++. I'm working on a Linux based Ubuntu 12.04 system using Codeblocks.

-------------------------

GoogleBot42 | 2017-01-02 01:03:55 UTC | #11

[quote="NiteLordz"]Screen Shots of the Unity Clone i am working on

[1drv.ms/1F4RDpQ](http://1drv.ms/1F4RDpQ)

For anyone interested in working on this, i am using an Agile template inside of VSO as i am experimenting with the process.  All code is built on the Urho3D design, however the engine itself has been modified to use Direct3D 11 and OpenGL 4.0[/quote]

Wow!  Very nice work!  You are sure this is a clone not the real thing right?   :wink:   Will this have support for custom c++/lua/angelscript components?  Also you said that this will use DX11 and GL 4.0 but my comp doesn't support those...

[code]glxinfo | grep "OpenGL version"
OpenGL version string: 2.1 Mesa 10.4.5[/code]

Could you add OpenGL 2.1 support please?  :slight_smile:

-------------------------

NiteLordz | 2017-01-02 01:03:55 UTC | #12

As of right now, the engine itself is just a stipped down version of Urho3D.  It could easily drop the original library into it, as i did not modify any of the method signatures, etc...

It currently supports AngelScript.  The screen shots show running through the Roll-a-Ball demo from Unity Tutorials.

Also, it only exports to Windows Desktop at this point, although i have support for Windows Store and Windows Phone (AngelScript doesn't work on Windows Phone at this point do to native calling not working, but trying to fix the asm code to enable it as well).

-------------------------

GoogleBot42 | 2017-01-02 01:03:56 UTC | #13

[quote="NiteLordz"]As of right now, the engine itself is just a stipped down version of Urho3D.  It could easily drop the original library into it, as i did not modify any of the method signatures, etc...

It currently supports AngelScript.  The screen shots show running through the Roll-a-Ball demo from Unity Tutorials.

Also, it only exports to Windows Desktop at this point, although i have support for Windows Store and Windows Phone (AngelScript doesn't work on Windows Phone at this point do to native calling not working, but trying to fix the asm code to enable it as well).[/quote]

Nice!  When you are going to add support for another language could you add c++ first?  Lua is nice but C++ is critical for code that is performance critical or memory needs to be conserved using special techniques...

You have done an amazing job so far mimicking Unity's interface.  At first I wasn't sure if you had modified Unity's theme slightly and posted those pictures.  But these are legitimate!  Could you set up a github repo with the source?  This might help others to improve the project, find/fix bugs, etc.   :slight_smile:

-------------------------

NiteLordz | 2017-01-02 01:03:56 UTC | #14

When you say add c++ what are you referring to?  currently, you build the scene, save it, and then when you export the project (Build it), i produce a solution file with the engine and source code readily available to be modified.

I am currently using VSO as i am testing it out for work, and seeing how the Agile work flow works in it.  If you want access to it, i could probably add you to the project and you can pull the source via visual studio.

-------------------------

hdunderscore | 2017-01-02 01:03:57 UTC | #15

@NiteLordz, the work you're doing sounds fantastic, but I feel like I need a lawyer before I should touch the source or be involved in it :astonished: If you post a binary (windows), I'd use it :smiley:

-------------------------

GoogleBot42 | 2017-01-02 01:04:02 UTC | #16

[quote="hd_"]@NiteLordz, the work you're doing sounds fantastic, but I feel like I need a lawyer before I should touch the source or be involved in it :astonished: If you post a binary (windows), I'd use it :smiley:[/quote]

Yah I agree... I don't really want to work on a project whose intentions are potentially mysterious...

Are you intending on making this into a commercial product and that is why you don't want to release the source code?  If so I don't want to work on the project.  Sorry.  This project is still pretty small and while it is growing I feel that tools for the engine should be open source or the focus might move from improving the game engine to making products for the engine...  I am not comfortable working on a project unless it is clearly denoted with a open source license...

If you just don't like github then you could use codeplex or bitbucket.

-------------------------

NiteLordz | 2017-01-02 01:04:02 UTC | #17

Oh this is not for commercial use. It is completely open source. The only reason it isn't on git or codeplex I because I'm playing with visual studio online for the agile methodologies as my work will be transitioning into them in the near future.

I can definitely put the code up here as a zip or what not if anyone wants to looks at it, but I don't want to maintain two repos.

Even if you want to check it out through vso, I believe you can view it, if I give you permission (email) to the project.

-------------------------

GoogleBot42 | 2017-01-02 01:04:02 UTC | #18

[quote="NiteLordz"]Oh this is not for commercial use. It is completely open source. The only reason it isn't on git or codeplex I because I'm playing with visual studio online for the agile methodologies as my work will be transitioning into them in the near future.

I can definitely put the code up here as a zip or what not if anyone wants to looks at it, but I don't want to maintain two repos.

Even if you want to check it out through vso, I believe you can view it, if I give you permission (email) to the project.[/quote]

Ok!  I will send you a pm with my email so you can add me. :slight_smile:

-------------------------

scorvi | 2017-01-02 01:04:04 UTC | #19

hey@ all 

i think it would be great to work on one editor together ... so should i join NiteLordz and work on the (qt based ? ) Editor or should i resume my work, which uses the Urho3d UI system ? a hard question indeed :-/ :stuck_out_tongue:

-------------------------

NiteLordz | 2017-01-02 01:04:04 UTC | #20

[quote="scorvi"]hey@ all 

i think it would be great to work on one editor together ... so should i join NiteLordz and work on the (qt based ? ) Editor or should i resume my work, which uses the Urho3d UI system ? a hard question indeed :-/ :stuck_out_tongue:[/quote]

The engine that i am working on is a very stripped down version. Really it is just a place holder of sense. I ripped apart Urho3D so i could have a little more control of it. I removed SDL, and run my own platform subsystem.  I use Direct3D 11 and OpenGL 3.x for graphics.

I don't have the full feature set of Urho3D at this point, but i have it on a roadmap to include.  The reason this was done, was so that i could use the GPU for more functionality (Particle Systems, Post Processes, etc...)

With that said, the Editor itself doesn't rely on my version of Urho3D, that much and would be fairly simple to drop back on top of Urho3D, i believe.

So there is a few options that can be achieved here. 

Let me know everyone's thoughts.

-------------------------

GoogleBot42 | 2017-01-02 01:04:04 UTC | #21

[quote="NiteLordz"]

The engine that i am working on is a very stripped down version. Really it is just a place holder of sense. I ripped apart Urho3D so i could have a little more control of it. I removed SDL, and run my own platform subsystem.  I use Direct3D 11 and OpenGL 3.x for graphics.

I don't have the full feature set of Urho3D at this point, but i have it on a roadmap to include.  The reason this was done, was so that i could use the GPU for more functionality (Particle Systems, Post Processes, etc...)

With that said, the Editor itself doesn't rely on my version of Urho3D, that much and would be fairly simple to drop back on top of Urho3D, i believe.

So there is a few options that can be achieved here. 

Let me know everyone's thoughts.[/quote]

I think the editor should use urho3d as a library if possible.  This would make it more flexible and doesn't require a new build of the IDE for a simple bugfix in Urho3D.  Also it means that it is much more simple to keep up with the latest Urho3D features.

[quote="scorvi"]hey@ all 

i think it would be great to work on one editor together ... so should i join NiteLordz and work on the (qt based ? ) Editor or should i resume my work, which uses the Urho3d UI system ? a hard question indeed :-/ :stuck_out_tongue:[/quote]

IDK... maybe it would be best to work on two for now...

-------------------------

scorvi | 2017-01-02 01:04:04 UTC | #22

so i am splitting the editor in his components, so that it can be used in other projects as well.
source code: [github.com/scorvi/Urho3DSamples](https://github.com/scorvi/Urho3DSamples)

the 01_AttributeInspector sample shows how to use the attribute inspector components. You can create just one attribute variable ui element or an attribute container for an serializable Object, that displayes all the attributes. And then you can use the attribute inspector,which create an UI Window, that handles also the resource picker. 

the other two samples are just tests how to use opensvg and openvg.

-------------------------

hdunderscore | 2017-01-02 01:04:05 UTC | #23

Working on a single editor is the best option, but with that said the work scorvi uploaded is really useful individually for anyone who wants to add some kind of in-game inspection to their C++ project so thanks for that scorvi !

-------------------------

jmiller | 2017-01-02 01:04:05 UTC | #24

[quote="scorvi"]so i am splitting the editor in his components, so that it can be used in other projects as well.[/quote]
Nice contribution scorvi, and thanks! It would be very useful in some projects and I may even give it a spin.

*edit: It was simple to integrate and seems to be working well :slight_smile:

-------------------------

scorvi | 2017-01-02 01:04:05 UTC | #25

... hmm i hope the stuff is usefull to someone. 
so i added the next sample of how to use the Hierarchy Window. But there is a bug with my style definition, i think. After SetStyleAuto the Window UIElement just remains white, had to set it manually ....

-------------------------

vivienneanthony | 2017-01-02 01:04:16 UTC | #26

[quote="scorvi"]hey ho 

i am working on implementing an IDE / Editor for urho3d. It is in the most parts just an c++ implementation of the angelscript editor.

for insperation, i am looking at [github.com/AtomicGameEngine/AtomicGameEngine](https://github.com/AtomicGameEngine/AtomicGameEngine)

here are some screenshots: [imgur.com/a/iQazt](http://imgur.com/a/iQazt)

Features added:
[ul]Project Manager
IDE Framework
MenuBar
ToolBar
MiniToolBar
Hierarchy Window
Attribute Window
Project Window[/ul]

WIP Features:
[ul]
TabWindow
3d View tab
3d Editor
Editor Plugin System
[/ul]
other Features:
[ul]gui editor
2d View tab
2d Editor 
node canvas
Component specific editors
Resource Editor 
Importing / Exporting
Language Editor 
Text/Script Editor tab[/ul]

i am implementing an Editor Plugin System like that used in godot. so that someone can implement an editor that only works with a specific component or resource type. 

the editor specific stuff will be also used in the in game editor .... it will be just like the scripted editor only that you can open this editor in your game if you want to test or manipulate your scene. 

after the WIP Features are added i will work on an GUI editor plugin so that i can improve the look of the editor :-/ . (i allready added an implementation of memononen/nanosvg to urho3d so that you can load a svg file like a texture ...  and added a memononen/nanovg GUI Renderer that uses the native opengl implementation ... i failed to port that to uhro ) 

is this needed ? i can put the source code online if someone wants to help ....[/quote]

How is the editor coming along?

-------------------------

scorvi | 2017-01-02 01:04:19 UTC | #27

hey ho

i recreated it again .... just cannot find the right way to do it .... help how to design an IDE is appreciated ^^ 

i added the IDE project now to my github account : [github.com/scorvi/Urho3DIDE](https://github.com/scorvi/Urho3DIDE)

the IDE does nothing for now  .... here is a screenshot of it [url]http://imgur.com/GL0AVxt,wnR6193#1[/url]

i added a Urho3DPlus lib, for classes that are used by the Runtime or that could be added to the Engine .... 
the Runtime just loads the project file and starts the main script file. 
i also added an TabWindow UI element, that, as you can see in the screenshot, has some design issue :-/ 

the editor starts in the projectmanager, where you can open/ create a project. that creates the editor and loads the main scene file provided by the projectsettings. 
the hierarchy inspector , Attribute inspector and the first try of the Scene 3d View Editor Plugin are then started, too. 

this weekend i want to add the SceneHierarchyEditor, that creates/loads scenes, nodes and components. if i find some time i will add an export editor too, to build/ export the project  ...

note: i am just porting the urho3d scripted editor in c++, so if someone wants to help ...

-------------------------

vivienneanthony | 2017-01-02 01:04:20 UTC | #28

I'm going try to get it compilable on my computer. I'm running Ubuntu.

I'm thinking I would have to download Urho3D-Master. Overwrite the files from your zip. Then change some file permissions.

[quote="scorvi"]hey ho

i recreated it again .... just cannot find the right way to do it .... help how to design an IDE is appreciated ^^ 

i added the IDE project now to my github account : [github.com/scorvi/Urho3DIDE](https://github.com/scorvi/Urho3DIDE)

the IDE does nothing for now  .... here is a screenshot of it [url]http://imgur.com/GL0AVxt,wnR6193#1[/url]

i added a Urho3DPlus lib, for classes that are used by the Runtime or that could be added to the Engine .... 
the Runtime just loads the project file and starts the main script file. 
i also added an TabWindow UI element, that, as you can see in the screenshot, has some design issue :-/ 

the editor starts in the projectmanager, where you can open/ create a project. that creates the editor and loads the main scene file provided by the projectsettings. 
the hierarchy inspector , Attribute inspector and the first try of the Scene 3d View Editor Plugin are then started, too. 

this weekend i want to add the SceneHierarchyEditor, that creates/loads scenes, nodes and components. if i find some time i will add an export editor too, to build/ export the project  ...

note: i am just porting the urho3d scripted editor in c++, so if someone wants to help ...[/quote]

-------------------------

scorvi | 2017-01-02 01:04:21 UTC | #29

Update: added the gizmo, the minitool bar, tool bar toggles for the scene editing and added scene/ node/component creation menu entry 

you can know pick and edit the nodes ^^ 

the next think i add is the resource browser ....

-------------------------

vivienneanthony | 2017-01-02 01:04:21 UTC | #30

[quote="scorvi"]Update: added the gizmo, the minitool bar, tool bar toggles for the scene editing and added scene/ node/component creation menu entry 

you can know pick and edit the nodes ^^ 

the next think i add is the resource browser ....[/quote]
 
How can I download it and it up so I can help??

-------------------------

scorvi | 2017-01-02 01:04:21 UTC | #31

the source code is on github : [github.com/scorvi/Urho3DIDE](https://github.com/scorvi/Urho3DIDE)

-------------------------

vivienneanthony | 2017-01-02 01:04:21 UTC | #32

[quote="scorvi"]the source code is on github : [github.com/scorvi/Urho3DIDE](https://github.com/scorvi/Urho3DIDE)[/quote]

I'm not clear about it unless I put the source into my current build or a fresh copy of Urho and change mod and flags pig the Linux scripts. I'm having numerous problems trying to compile on ubuntu. This is a direct copy from the master file.

[code]vivienne@vivienne-System-Product-Name:/media/home2/vivienne/Urho3DIDE-master$ ./cmake_generic.sh /media/home2/vivienne/Urho3DIDE-master  -DURHO3D_64BIT=1 -DURHO3D_SAMPLES=1 -DCMAKE_BUILD_TYPE=Rel
./cmake_generic.sh: line 32: ./.bash_helpers.sh: No such file or directory
-- The C compiler identification is GNU
-- The CXX compiler identification is GNU
-- Check for working C compiler: /usr/bin/gcc
-- Check for working C compiler: /usr/bin/gcc -- works
-- Detecting C compiler ABI info
-- Detecting C compiler ABI info - done
-- Check for working CXX compiler: /usr/bin/c++
-- Check for working CXX compiler: /usr/bin/c++ -- works
-- Detecting CXX compiler ABI info
-- Detecting CXX compiler ABI info - done
CMake Error at CMake/Modules/FindUrho3D.cmake:143 (message):
  Could not find Urho3D library in Urho3D build tree or SDK installation.
  Use URHO3D_HOME environment variable or build option to specify the
  location of the build tree or SDK installation.
Call Stack (most recent call first):
  CMakeLists.txt:53 (find_package)


-- Configuring incomplete, errors occurred!
vivienne@vivienne-System-Product-Name:/media/home2/vivienne/Urho3DIDE-master$ ./cmake_generic.sh /media/home2/vivienne/Urho3DIDE-master  -DURHO3D_64BIT=1 -DURHO3D_SAMPLES=1 -DCMAKE_BUILD_TYPE=Rel
./cmake_generic.sh: line 32: ./.bash_helpers.sh: No such file or directory
CMake Error at CMake/Modules/FindUrho3D.cmake:143 (message):
  Could not find Urho3D library in Urho3D build tree or SDK installation.
  Use URHO3D_HOME environment variable or build option to specify the
  location of the build tree or SDK installation.
Call Stack (most recent call first):
  CMakeLists.txt:53 (find_package)


-- Configuring incomplete, errors occurred!
vivienne@vivienne-System-Product-Name:/media/home2/vivienne/Urho3DIDE-master$ ^C
vivienne@vivienne-System-Product-Name:/media/home2/vivienne/Urho3DIDE-master$ 
[/code]

-------------------------

scorvi | 2017-01-02 01:04:22 UTC | #33

[quote="vivienneanthony"][quote="scorvi"]the source code is on github : [github.com/scorvi/Urho3DIDE](https://github.com/scorvi/Urho3DIDE)[/quote]

I'm not clear about it unless I put the source into my current build or a fresh copy of Urho and change mod and flags pig the Linux scripts. I'm having numerous problems trying to compile on ubuntu. This is a direct copy from the master file.

[code]
CMake Error at CMake/Modules/FindUrho3D.cmake:143 (message):
  Could not find Urho3D library in Urho3D build tree or SDK installation.
  Use URHO3D_HOME environment variable or build option to specify the
  location of the build tree or SDK installation.
Call Stack (most recent call first):
  CMakeLists.txt:53 (find_package)
[/code][/quote]

the Urho3DIDE is not a branch of the Urho3D lib, it is a seperate project. so to build it you have to build the urho3d lib and then build the ide BUT you have to set the URHO3D_HOME Variable to the Build folder of you urho3d lib. 
So if i build i use
[code] \cmake_generic.bat Build -VS=12 -DURHO3D_MKLINK=1 -DURHO3D_OPENGL=1[/code]
and if you did not set the URHO3D_HOME Variable in your system you can add 
[code] \cmake_generic.bat Build -VS=12 -DURHO3D_MKLINK=1 -DURHO3D_OPENGL=1 -URHO3D_HOME=Path/to/Urho3D-Master/Build [/code]

the problem you have is that cmake does not find the Build folder of your urho3d lib ... so you have to set URHO3D_HOME


on another note, i added the resouce browser and a new Runtime that uses an AppStateManager ... 
How can i bind that AppStateManager to the script system so that i can create AppStates in script ? Do i have to do something like the ScriptComoponent does ?  (load a script and check if the provided class has the specified functions ? )

-------------------------

vivienneanthony | 2017-01-02 01:04:23 UTC | #34

It just messes up on this line of

[code]# Setup target with resource copying
setup_library ()

target_include_directories (Urho3DPlus PUBLIC ${CMAKE_CURRENT_SOURCE_DIR}/Source)
[/code]

doing the cmake_generic.sh

[code]

vivienne@vivienne-System-Product-Name:/media/home2/vivienne/Urho3DIDE-master$ gedit
vivienne@vivienne-System-Product-Name:/media/home2/vivienne/Urho3DIDE-master$ ./cmake_generic.sh build -DURHO3D_INCLUDE_DIRS=/media/home2/vivienne/Urho3D-native/include/Urho3D
./cmake_generic.sh: line 31: /media/home2/vivienne/Urho3DIDE-master/.bash_helpers.sh: No such file or directory
CMake Error at Urho3DPlus/CMakeLists.txt:81 (target_include_directories):
  Unknown CMake command "target_include_directories".


-- Configuring incomplete, errors occurred!
[/code]

-------------------------

GoogleBot42 | 2017-01-02 01:04:23 UTC | #35

I had this problem too at one point... The error tells you everything you need to know.  It cannot find ".bash_helpers.sh" in the project root.  Run "ls -a" in the project root.  Your should see that there indeed is no ".bash_helpers.sh" (the "." in front of a file name hides the file/folder from a normal "ls" directory list.  Now look at the git repo [url]https://github.com/urho3d/Urho3D[/url] In the list of files there is a ".bash_helpers.sh" did you copy the Urho3D project folder contents using a graphical manager?  If so any file/folder beginning with "." will be ignored unless you show hidden files in the graphical mangers settings.  That is why I have gotten in the habit of doing most things in the terminal.   :wink: 

Or in the terminal...
[code]cd /path/to/old/Urho3D/project/dir
cp * /new/path/to/Urho3D/project/dir
cd /new/path/to/Urho3D/project/dir
cmake ./cmake_generic.sh build -DURHO3D_INCLUDE_DIRS=/media/home2/vivienne/Urho3D-native/include/Urho3D
cd build
make[/code]

Or maybe you should just "git clone" the repo again...

-------------------------

vivienneanthony | 2017-01-02 01:04:23 UTC | #36

It's finding the file but still says unknown command.

-------------------------

vivienneanthony | 2017-01-02 01:04:23 UTC | #37

Which version of cmake you use? I had to update my cmake to version 3.02. Since, Windows uses \ in the path. I think I have to change it all to /"

[code]vivienne@vivienne-System-Product-Name:/media/home2/vivienne/Urho3DIDE-master/Build$ make
Scanning dependencies of target Urho3DPlus
[  2%] Building CXX object Urho3DPlus/CMakeFiles/Urho3DPlus.dir/Source/UI/UIUtils.cpp.o
In file included from /media/home2/vivienne/Urho3DIDE-master/Urho3DPlus/Source/UI/UIUtils.cpp:23:0:
/media/home2/vivienne/Urho3DIDE-master/Urho3DPlus/Source/UI/UIUtils.h:25:28: fatal error: ..\Core\Object.h: No such file or directory
compilation terminated.
make[2]: *** [Urho3DPlus/CMakeFiles/Urho3DPlus.dir/Source/UI/UIUtils.cpp.o] Error 1
make[1]: *** [Urho3DPlus/CMakeFiles/Urho3DPlus.dir/all] Error 2
make: *** [all] Error 2
vivienne@vivienne-System-Product-Name:/media/home2/vivienne/Urho3DIDE-master/Build$ make
[  2%] Building CXX object Urho3DPlus/CMakeFiles/Urho3DPlus.dir/Source/UI/UIUtils.cpp.o
In file included from /media/home2/vivienne/Urho3DIDE-master/Urho3DPlus/Source/UI/UIUtils.cpp:23:0:
/media/home2/vivienne/Urho3DIDE-master/Urho3DPlus/Source/UI/UIUtils.h:25:28: fatal error: ..\Core\Object.h: No such file or directory
compilation terminated.
make[2]: *** [Urho3DPlus/CMakeFiles/Urho3DPlus.dir/Source/UI/UIUtils.cpp.o] Error 1
make[1]: *** [Urho3DPlus/CMakeFiles/Urho3DPlus.dir/all] Error 2
make: *** [all] Error 2
vivienne@vivienne-System-Product-Name:/media/home2/vivienne/Urho3DIDE-master/Build$ 
[/code]

[quote="scorvi"][quote="vivienneanthony"][quote="scorvi"]the source code is on github : [github.com/scorvi/Urho3DIDE](https://github.com/scorvi/Urho3DIDE)[/quote]

I'm not clear about it unless I put the source into my current build or a fresh copy of Urho and change mod and flags pig the Linux scripts. I'm having numerous problems trying to compile on ubuntu. This is a direct copy from the master file.

[code]
CMake Error at CMake/Modules/FindUrho3D.cmake:143 (message):
  Could not find Urho3D library in Urho3D build tree or SDK installation.
  Use URHO3D_HOME environment variable or build option to specify the
  location of the build tree or SDK installation.
Call Stack (most recent call first):
  CMakeLists.txt:53 (find_package)
[/code][/quote]

the Urho3DIDE is not a branch of the Urho3D lib, it is a seperate project. so to build it you have to build the urho3d lib and then build the ide BUT you have to set the URHO3D_HOME Variable to the Build folder of you urho3d lib. 
So if i build i use
[code] \cmake_generic.bat Build -VS=12 -DURHO3D_MKLINK=1 -DURHO3D_OPENGL=1[/code]
and if you did not set the URHO3D_HOME Variable in your system you can add 
[code] \cmake_generic.bat Build -VS=12 -DURHO3D_MKLINK=1 -DURHO3D_OPENGL=1 -URHO3D_HOME=Path/to/Urho3D-Master/Build [/code]

the problem you have is that cmake does not find the Build folder of your urho3d lib ... so you have to set URHO3D_HOME


on another note, i added the resouce browser and a new Runtime that uses an AppStateManager ... 
How can i bind that AppStateManager to the script system so that i can create AppStates in script ? Do i have to do something like the ScriptComoponent does ?  (load a script and check if the provided class has the specified functions ? )[/quote]

-------------------------

scorvi | 2017-01-02 01:04:24 UTC | #38

[quote="vivienneanthony"]Which version of cmake you use? I had to update my cmake to version 3.02. Since, Windows uses \ in the path. I think I have to change it all to /"

[/quote]

my cmake verison is 3.2.0-rc2.

hmm sry about that i am using visual assist and it has some problems automaticaly include missing headers. it changes sometimes from / to \ and so .... dont know why.  in the old build structure it worked just fine ... 
i will change that, in the next upload. 

does someone know which of the include styles i have to use ? 
[code]#include<Urho3D/...>
or  
#include ".../Core/.."[/code]
because it works just fine for both but the second include can be added  in one click with vissual assist. 
i know that it has something to do with where the compiler looks for the headers but ...

-------------------------

vivienneanthony | 2017-01-02 01:04:24 UTC | #39

Hello,

I think it's fine. I think it's how files are made. Windows always accepted "\" or "/" in the path but Linux/Unix is more strict. It just has to be "/". I'm trying to see whats causing the following errors stopping compiling.

Vivienne

[code]In file included from /media/home2/vivienne/Urho3DIDE-master/Urho3DPlus/Source/Editor/Editor.cpp:47:0:
/media/home2/vivienne/Urho3DIDE-master/Urho3DPlus/Source/Editor/EPScene2D.h:85:30: error: expected ?;? at end of member declaration
/media/home2/vivienne/Urho3DIDE-master/Urho3DPlus/Source/Editor/EPScene2D.h:85:32: error: ?override? does not name a type
/media/home2/vivienne/Urho3DIDE-master/Urho3DPlus/Source/Editor/EPScene2D.h:87:28: error: expected ?;? at end of member declaration
/media/home2/vivienne/Urho3DIDE-master/Urho3DPlus/Source/Editor/EPScene2D.h:87:34: error: ?override? does not name a type
/media/home2/vivienne/Urho3DIDE-master/Urho3DPlus/Source/Editor/EPScene2D.h:89:35: error: expected ?;? at end of member declaration
/media/home2/vivienne/Urho3DIDE-master/Urho3DPlus/Source/Editor/EPScene2D.h:89:37: error: ?override? does not name a type
/media/home2/vivienne/Urho3DIDE-master/Urho3DPlus/Source/Editor/EPScene2D.h:91:40: error: expected ?;? at end of member declaration
/media/home2/vivienne/Urho3DIDE-master/Urho3DPlus/Source/Editor/EPScene2D.h:91:46: error: ?override? does not name a type
/media/home2/vivienne/Urho3DIDE-master/Urho3DPlus/Source/Editor/EPScene2D.h:93:36: error: expected ?;? at end of member declaration
/media/home2/vivienne/Urho3DIDE-master/Urho3DPlus/Source/Editor/EPScene2D.h:93:38: error: ?override? does not name a type
/media/home2/vivienne/Urho3DIDE-master/Urho3DPlus/Source/Editor/EPScene2D.h:95:39: error: expected ?;? at end of member declaration
/media/home2/vivienne/Urho3DIDE-master/Urho3DPlus/Source/Editor/EPScene2D.h:95:41: error: ?override? does not name a type

[/code]


[quote="scorvi"][quote="vivienneanthony"]Which version of cmake you use? I had to update my cmake to version 3.02. Since, Windows uses \ in the path. I think I have to change it all to /"

[/quote]

my cmake verison is 3.2.0-rc2.

hmm sry about that i am using visual assist and it has some problems automaticaly include missing headers. it changes sometimes from / to \ and so .... dont know why.  in the old build structure it worked just fine ... 
i will change that, in the next upload. 

does someone know which of the include styles i have to use ? 
[code]#include<Urho3D/...>
or  
#include ".../Core/.."[/code]
because it works just fine for both but the second include can be added  in one click with vissual assist. 
i know that it has something to do with where the compiler looks for the headers but ...[/quote]

-------------------------

vivienneanthony | 2017-01-02 01:04:24 UTC | #40

My progress. So far, I changed most of the Windows based paths to cross-compatible  paths Linux/Windows. Additionally, I was getting errors the class variables cannot be initiated in the classes the way it's setup. It throws a error on my gcc. So, I removed the initlization thinking it can be set in a constructor function.

Also, I'm getting the following errors on code like in the header files. So, I'm not sure what the solution to that is yet. Also, gcc is sensitive to vectors.  Something like "Vector<SharedPtr<ProjectSettings>> projects_" throws a error and it had to be changed to "Vector<SharedPtr <ProjectSettings> > projects_". So far it's the changes I made or working on.


[code]		virtual ~EPScene2D();

		virtual bool HasMainScreen() override;

		virtual String GetName() const override;

		virtual void Edit(Object *object) override;

		virtual bool Handles(Object *object) const override;

		virtual UIElement* GetMainScreen() override;

		virtual void SetVisible(bool visible) override;

[/code]

-------------------------

vivienneanthony | 2017-01-02 01:04:24 UTC | #41

Updating Cmake did the trick. 

[quote="GoogleBot42"]I had this problem too at one point... The error tells you everything you need to know.  It cannot find ".bash_helpers.sh" in the project root.  Run "ls -a" in the project root.  Your should see that there indeed is no ".bash_helpers.sh" (the "." in front of a file name hides the file/folder from a normal "ls" directory list.  Now look at the git repo [url]https://github.com/urho3d/Urho3D[/url] In the list of files there is a ".bash_helpers.sh" did you copy the Urho3D project folder contents using a graphical manager?  If so any file/folder beginning with "." will be ignored unless you show hidden files in the graphical mangers settings.  That is why I have gotten in the habit of doing most things in the terminal.   :wink: 

Or in the terminal...
[code]cd /path/to/old/Urho3D/project/dir
cp * /new/path/to/Urho3D/project/dir
cd /new/path/to/Urho3D/project/dir
cmake ./cmake_generic.sh build -DURHO3D_INCLUDE_DIRS=/media/home2/vivienne/Urho3D-native/include/Urho3D
cd build
make[/code]

Or maybe you should just "git clone" the repo again...[/quote]

-------------------------

vivienneanthony | 2017-01-02 01:04:24 UTC | #42

Scorvi,

I posted the github of the minor changes I made so far to compile. GCC 4.6 doesn't support override so maybe you or someone know a way around that.

[github.com/vivienneanthony/Urho3DIDE](https://github.com/vivienneanthony/Urho3DIDE)

It compiles to 50%. I'm not sure if it safe to take out the override flags.

Vivienne


[code]vivienne@vivienne-System-Product-Name:/media/home2/vivienne/Urho3DIDE$ cd Build
vivienne@vivienne-System-Product-Name:/media/home2/vivienne/Urho3DIDE/Build$ make
Scanning dependencies of target Urho3DPlus
[  2%] Building CXX object Urho3DPlus/CMakeFiles/Urho3DPlus.dir/Source/Input/InputActionSystem.cpp.o
[  5%] Building CXX object Urho3DPlus/CMakeFiles/Urho3DPlus.dir/Source/UI/UIUtils.cpp.o                                             
[  8%] Building CXX object Urho3DPlus/CMakeFiles/Urho3DPlus.dir/Source/UI/AttributeContainer.cpp.o                                  
[ 11%] Building CXX object Urho3DPlus/CMakeFiles/Urho3DPlus.dir/Source/UI/DirSelector.cpp.o                                         
[ 13%] Building CXX object Urho3DPlus/CMakeFiles/Urho3DPlus.dir/Source/UI/AttributeInspector.cpp.o                                  
[ 16%] Building CXX object Urho3DPlus/CMakeFiles/Urho3DPlus.dir/Source/UI/HierarchyWindow.cpp.o                                     
[ 19%] Building CXX object Urho3DPlus/CMakeFiles/Urho3DPlus.dir/Source/UI/TabWindow.cpp.o                                           
[ 22%] Building CXX object Urho3DPlus/CMakeFiles/Urho3DPlus.dir/Source/UI/MiniToolBarUI.cpp.o                                       
[ 25%] Building CXX object Urho3DPlus/CMakeFiles/Urho3DPlus.dir/Source/UI/MenuBarUI.cpp.o                                           
[ 27%] Building CXX object Urho3DPlus/CMakeFiles/Urho3DPlus.dir/Source/UI/AttributeVariable.cpp.o                                   
[ 30%] Building CXX object Urho3DPlus/CMakeFiles/Urho3DPlus.dir/Source/UI/ModalWindow.cpp.o                                         
[ 33%] Building CXX object Urho3DPlus/CMakeFiles/Urho3DPlus.dir/Source/UI/ResourcePicker.cpp.o                                      
[ 36%] Building CXX object Urho3DPlus/CMakeFiles/Urho3DPlus.dir/Source/UI/ToolBarUI.cpp.o                                           
[ 38%] Building CXX object Urho3DPlus/CMakeFiles/Urho3DPlus.dir/Source/Project/ProjectWindow.cpp.o                                  
/media/home2/vivienne/Urho3DIDE/Urho3DPlus/Source/Project/ProjectWindow.cpp:99:14: warning: multi-character character constant [-Wmultichar]
/media/home2/vivienne/Urho3DIDE/Urho3DPlus/Source/Project/ProjectWindow.cpp:121:15: warning: multi-character character constant [-Wmultichar]
/media/home2/vivienne/Urho3DIDE/Urho3DPlus/Source/Project/ProjectWindow.cpp: In member function ?void Urho3D::ProjectWindow::UpdateWindow()?:
/media/home2/vivienne/Urho3DIDE/Urho3DPlus/Source/Project/ProjectWindow.cpp:99:23: warning: overflow in implicit constant conversion [-Woverflow]
/media/home2/vivienne/Urho3DIDE/Urho3DPlus/Source/Project/ProjectWindow.cpp: In member function ?void Urho3D::ProjectWindow::UnloadProject()?:
/media/home2/vivienne/Urho3DIDE/Urho3DPlus/Source/Project/ProjectWindow.cpp:121:24: warning: overflow in implicit constant conversion [-Woverflow]
[ 41%] Building CXX object Urho3DPlus/CMakeFiles/Urho3DPlus.dir/Source/Project/TemplateManager.cpp.o
[ 44%] Building CXX object Urho3DPlus/CMakeFiles/Urho3DPlus.dir/Source/Project/ProjectManager.cpp.o                                 
[ 47%] Building CXX object Urho3DPlus/CMakeFiles/Urho3DPlus.dir/Source/Editor/EditorView.cpp.o                                      
[ 50%] Building CXX object Urho3DPlus/CMakeFiles/Urho3DPlus.dir/Source/Editor/Editor.cpp.o                                          
In file included from /media/home2/vivienne/Urho3DIDE/Urho3DPlus/Source/Editor/Editor.cpp:46:0:
/media/home2/vivienne/Urho3DIDE/Urho3DPlus/Source/Editor/EPScene3D.h:84:37: error: expected ?;? at end of member declaration
/media/home2/vivienne/Urho3DIDE/Urho3DPlus/Source/Editor/EPScene3D.h:84:39: error: ?override? does not name a type
/media/home2/vivienne/Urho3DIDE/Urho3DPlus/Source/Editor/EPScene3D.h:86:25: error: expected ?;? at end of member declaration
/media/home2/vivienne/Urho3DIDE/Urho3DPlus/Source/Editor/EPScene3D.h:86:27: error: ?override? does not name a type
In file included from /media/home2/vivienne/Urho3DIDE/Urho3DPlus/Source/Editor/Editor.cpp:46:0:
/media/home2/vivienne/Urho3DIDE/Urho3DPlus/Source/Editor/EPScene3D.h:88:129: error: expected ?;? at end of member declaration
/media/home2/vivienne/Urho3DIDE/Urho3DPlus/Source/Editor/EPScene3D.h:88:131: error: ?override? does not name a type
/media/home2/vivienne/Urho3DIDE/Urho3DPlus/Source/Editor/EPScene3D.h:90:146: error: expected ?;? at end of member declaration
/media/home2/vivienne/Urho3DIDE/Urho3DPlus/Source/Editor/EPScene3D.h:90:148: error: ?override? does not name a type
/media/home2/vivienne/Urho3DIDE/Urho3DPlus/Source/Editor/EPScene3D.h:92:169: error: expected ?;? at end of member declaration
/media/home2/vivienne/Urho3DIDE/Urho3DPlus/Source/Editor/EPScene3D.h:92:171: error: ?override? does not name a type
/media/home2/vivienne/Urho3DIDE/Urho3DPlus/Source/Editor/EPScene3D.h:194:30: error: expected ?;? at end of member declaration
/media/home2/vivienne/Urho3DIDE/Urho3DPlus/Source/Editor/EPScene3D.h:194:32: error: ?override? does not name a type
/media/home2/vivienne/Urho3DIDE/Urho3DPlus/Source/Editor/EPScene3D.h:195:28: error: expected ?;? at end of member declaration
/media/home2/vivienne/Urho3DIDE/Urho3DPlus/Source/Editor/EPScene3D.h:195:34: error: ?override? does not name a type
/media/home2/vivienne/Urho3DIDE/Urho3DPlus/Source/Editor/EPScene3D.h:196:35: error: expected ?;? at end of member declaration
/media/home2/vivienne/Urho3DIDE/Urho3DPlus/Source/Editor/EPScene3D.h:196:37: error: ?override? does not name a type
/media/home2/vivienne/Urho3DIDE/Urho3DPlus/Source/Editor/EPScene3D.h:197:40: error: expected ?;? at end of member declaration
/media/home2/vivienne/Urho3DIDE/Urho3DPlus/Source/Editor/EPScene3D.h:197:46: error: ?override? does not name a type
/media/home2/vivienne/Urho3DIDE/Urho3DPlus/Source/Editor/EPScene3D.h:200:36: error: expected ?;? at end of member declaration
/media/home2/vivienne/Urho3DIDE/Urho3DPlus/Source/Editor/EPScene3D.h:200:38: error: ?override? does not name a type
/media/home2/vivienne/Urho3DIDE/Urho3DPlus/Source/Editor/EPScene3D.h:201:40: error: expected ?;? at end of member declaration
/media/home2/vivienne/Urho3DIDE/Urho3DPlus/Source/Editor/EPScene3D.h:201:42: error: ?override? does not name a type
/media/home2/vivienne/Urho3DIDE/Urho3DPlus/Source/Editor/EPScene3D.h:202:38: error: expected ?;? at end of member declaration
/media/home2/vivienne/Urho3DIDE/Urho3DPlus/Source/Editor/EPScene3D.h:202:40: error: ?override? does not name a type
In file included from /media/home2/vivienne/Urho3DIDE/Urho3DPlus/Source/Editor/Editor.cpp:47:0:
/media/home2/vivienne/Urho3DIDE/Urho3DPlus/Source/Editor/EPScene2D.h:87:30: error: expected ?;? at end of member declaration
/media/home2/vivienne/Urho3DIDE/Urho3DPlus/Source/Editor/EPScene2D.h:87:32: error: ?override? does not name a type
/media/home2/vivienne/Urho3DIDE/Urho3DPlus/Source/Editor/EPScene2D.h:89:28: error: expected ?;? at end of member declaration
/media/home2/vivienne/Urho3DIDE/Urho3DPlus/Source/Editor/EPScene2D.h:89:34: error: ?override? does not name a type
/media/home2/vivienne/Urho3DIDE/Urho3DPlus/Source/Editor/EPScene2D.h:91:35: error: expected ?;? at end of member declaration
/media/home2/vivienne/Urho3DIDE/Urho3DPlus/Source/Editor/EPScene2D.h:91:37: error: ?override? does not name a type
/media/home2/vivienne/Urho3DIDE/Urho3DPlus/Source/Editor/EPScene2D.h:93:40: error: expected ?;? at end of member declaration
/media/home2/vivienne/Urho3DIDE/Urho3DPlus/Source/Editor/EPScene2D.h:93:46: error: ?override? does not name a type
/media/home2/vivienne/Urho3DIDE/Urho3DPlus/Source/Editor/EPScene2D.h:95:36: error: expected ?;? at end of member declaration
/media/home2/vivienne/Urho3DIDE/Urho3DPlus/Source/Editor/EPScene2D.h:95:38: error: ?override? does not name a type
/media/home2/vivienne/Urho3DIDE/Urho3DPlus/Source/Editor/EPScene2D.h:97:39: error: expected ?;? at end of member declaration
/media/home2/vivienne/Urho3DIDE/Urho3DPlus/Source/Editor/EPScene2D.h:97:41: error: ?override? does not name a type
make[2]: *** [Urho3DPlus/CMakeFiles/Urho3DPlus.dir/Source/Editor/Editor.cpp.o] Error 1
make[1]: *** [Urho3DPlus/CMakeFiles/Urho3DPlus.dir/all] Error 2
make: *** [all] Error 2
vivienne@vivienne-System-Product-Name:/media/home2/vivienne/Urho3DIDE/Build$ 
[/code]

Note:
Probably got it to 60% with the following error

Copied functions with override and marked them out. Copied without the override flag.

[code][  2%] Building CXX object Urho3DPlus/CMakeFiles/Urho3DPlus.dir/Source/Editor/EPScene3D.cpp.o                                                                                                              
/media/home2/vivienne/Urho3DIDE/Urho3DPlus/Source/Editor/EPScene3D.cpp: In member function ?void Urho3D::EPScene3D::ViewRaycast(bool)?:                                                                    
/media/home2/vivienne/Urho3DIDE/Urho3DPlus/Source/Editor/EPScene3D.cpp:1040:49: error: no matching function for call to ?Urho3D::Octree::RaycastSingle(Urho3D::RayOctreeQuery)?                            
/media/home2/vivienne/Urho3DIDE/Urho3DPlus/Source/Editor/EPScene3D.cpp:1040:49: note: candidate is:                                                                                                        
/media/home2/vivienne/Urho3D-native/include/Urho3D/ThirdParty/../Graphics/Octree.h:187:10: note: void Urho3D::Octree::RaycastSingle(Urho3D::RayOctreeQuery&) const                                         
/media/home2/vivienne/Urho3D-native/include/Urho3D/ThirdParty/../Graphics/Octree.h:187:10: note:   no known conversion for argument 1 from ?Urho3D::RayOctreeQuery? to ?Urho3D::RayOctreeQuery&?           
/media/home2/vivienne/Urho3DIDE/Urho3DPlus/Source/Editor/EPScene3D.cpp: In member function ?void Urho3D::EPScene3DView::OpenViewportSettingsWindow()?:                                                     
/media/home2/vivienne/Urho3DIDE/Urho3DPlus/Source/Editor/EPScene3D.cpp:2406:50: error: no matching function for call to ?Urho3D::EPScene3DView::UpdateSettingsUI(const Urho3D::StringHash&, Urho3D::VariantMap)?                                                                                                                                                                                                      
/media/home2/vivienne/Urho3DIDE/Urho3DPlus/Source/Editor/EPScene3D.cpp:2406:50: note: candidate is:                                                                                                        
/media/home2/vivienne/Urho3DIDE/Urho3DPlus/Source/Editor/EPScene3D.cpp:2391:7: note: void Urho3D::EPScene3DView::UpdateSettingsUI(Urho3D::StringHash, Urho3D::VariantMap&)                                 
/media/home2/vivienne/Urho3DIDE/Urho3DPlus/Source/Editor/EPScene3D.cpp:2391:7: note:   no known conversion for argument 2 from ?Urho3D::VariantMap {aka Urho3D::HashMap<Urho3D::StringHash, Urho3D::Variant>}? to ?Urho3D::VariantMap& {aka Urho3D::HashMap<Urho3D::StringHash, Urho3D::Variant>&}?                                                                                                                   
/media/home2/vivienne/Urho3DIDE/Urho3DPlus/Source/Editor/EPScene3D.cpp: In member function ?void Urho3D::EPScene3DView::SetOrthographic(bool)?:                                                            
/media/home2/vivienne/Urho3DIDE/Urho3DPlus/Source/Editor/EPScene3D.cpp:2516:50: error: no matching function for call to ?Urho3D::EPScene3DView::UpdateSettingsUI(const Urho3D::StringHash&, Urho3D::VariantMap)?                                                                                                                                                                                                      
/media/home2/vivienne/Urho3DIDE/Urho3DPlus/Source/Editor/EPScene3D.cpp:2516:50: note: candidate is:                                                                                                        
/media/home2/vivienne/Urho3DIDE/Urho3DPlus/Source/Editor/EPScene3D.cpp:2391:7: note: void Urho3D::EPScene3DView::UpdateSettingsUI(Urho3D::StringHash, Urho3D::VariantMap&)                                 
/media/home2/vivienne/Urho3DIDE/Urho3DPlus/Source/Editor/EPScene3D.cpp:2391:7: note:   no known conversion for argument 2 from ?Urho3D::VariantMap {aka Urho3D::HashMap<Urho3D::StringHash, Urho3D::Variant>}? to ?Urho3D::VariantMap& {aka Urho3D::HashMap<Urho3D::StringHash, Urho3D::Variant>&}?                                                                                                                   
/media/home2/vivienne/Urho3DIDE/Urho3DPlus/Source/Editor/EPScene3D.cpp: In member function ?void Urho3D::EPScene3DView::ToggleViewportSettingsWindow(Urho3D::StringHash, Urho3D::VariantMap&)?:
/media/home2/vivienne/Urho3DIDE/Urho3DPlus/Source/Editor/EPScene3D.cpp:2575:62: error: no matching function for call to ?Urho3D::EPScene3DView::CloseViewportSettingsWindow(const Urho3D::StringHash&, Urho3D::VariantMap)?
/media/home2/vivienne/Urho3DIDE/Urho3DPlus/Source/Editor/EPScene3D.cpp:2575:62: note: candidate is:
/media/home2/vivienne/Urho3DIDE/Urho3DPlus/Source/Editor/EPScene3D.cpp:2386:7: note: void Urho3D::EPScene3DView::CloseViewportSettingsWindow(Urho3D::StringHash, Urho3D::VariantMap&)
/media/home2/vivienne/Urho3DIDE/Urho3DPlus/Source/Editor/EPScene3D.cpp:2386:7: note:   no known conversion for argument 2 from ?Urho3D::VariantMap {aka Urho3D::HashMap<Urho3D::StringHash, Urho3D::Variant>}? to ?Urho3D::VariantMap& {aka Urho3D::HashMap<Urho3D::StringHash, Urho3D::Variant>&}?
make[2]: *** [Urho3DPlus/CMakeFiles/Urho3DPlus.dir/Source/Editor/EPScene3D.cpp.o] Error 1
make[1]: *** [Urho3DPlus/CMakeFiles/Urho3DPlus.dir/all] Error 2
make: *** [all] Error 2
vivienne@vivienne-System-Product-Name:[/code]

-------------------------

GoogleBot42 | 2017-01-02 01:04:24 UTC | #43

[quote="vivienneanthony"]
I posted the github of the minor changes I made so far to compile. GCC 4.6 doesn't support override so maybe you or someone know a way around that.[/quote]
Maybe you could try updating gcc if that is an option...  GCC 4.6 is pretty old and the release chain started way back in 2011.  I am not very surprised that override doesn't work.

-------------------------

vivienneanthony | 2017-01-02 01:04:24 UTC | #44

[quote="GoogleBot42"][quote="vivienneanthony"]
I posted the github of the minor changes I made so far to compile. GCC 4.6 doesn't support override so maybe you or someone know a way around that.[/quote]
Maybe you could try updating gcc if that is an option...  GCC 4.6 is pretty old and the release chain started way back in 2011.  I am not very surprised that override doesn't work.[/quote]

I'm trying to avoid too many special updates to get the code working. Please I think to maintain a certain amount of cross-platform coding the less special stuff the better.

I've been reading some links about the error message. I kinda get it but someone well versed in c++ or cross platform coding would understand.

-------------------------

vivienneanthony | 2017-01-02 01:04:25 UTC | #45

These are the errors I get. Repository at [github.com/vivienneanthony/Urho3DIDE](https://github.com/vivienneanthony/Urho3DIDE)

[code]vivienne@vivienne-System-Product-Name:/media/home2/vivienne/Urho3DIDE/Build$ make
[  2%] Building CXX object Urho3DPlus/CMakeFiles/Urho3DPlus.dir/Source/Editor/EPScene3D.cpp.o
/media/home2/vivienne/Urho3DIDE/Urho3DPlus/Source/Editor/EPScene3D.cpp: In member function ?void Urho3D::EPScene3D::ViewRaycast(bool)?:
/media/home2/vivienne/Urho3DIDE/Urho3DPlus/Source/Editor/EPScene3D.cpp:1039:169: error: no matching function for call to ?Urho3D::Octree::RaycastSingle(Urho3D::RayOctreeQuery)?
/media/home2/vivienne/Urho3DIDE/Urho3DPlus/Source/Editor/EPScene3D.cpp:1039:169: note: candidate is:
/media/home2/vivienne/Urho3D-native/include/Urho3D/ThirdParty/../Graphics/Octree.h:187:10: note: void Urho3D::Octree::RaycastSingle(Urho3D::RayOctreeQuery&) const
/media/home2/vivienne/Urho3D-native/include/Urho3D/ThirdParty/../Graphics/Octree.h:187:10: note:   no known conversion for argument 1 from ?Urho3D::RayOctreeQuery? to ?Urho3D::RayOctreeQuery&?
/media/home2/vivienne/Urho3DIDE/Urho3DPlus/Source/Editor/EPScene3D.cpp: In member function ?void Urho3D::EPScene3DView::OpenViewportSettingsWindow()?:
/media/home2/vivienne/Urho3DIDE/Urho3DPlus/Source/Editor/EPScene3D.cpp:2408:50: error: no matching function for call to ?Urho3D::EPScene3DView::UpdateSettingsUI(const Urho3D::StringHash&, Urho3D::VariantMap)?
/media/home2/vivienne/Urho3DIDE/Urho3DPlus/Source/Editor/EPScene3D.cpp:2408:50: note: candidate is:
/media/home2/vivienne/Urho3DIDE/Urho3DPlus/Source/Editor/EPScene3D.cpp:2393:7: note: void Urho3D::EPScene3DView::UpdateSettingsUI(Urho3D::StringHash, Urho3D::VariantMap&)
/media/home2/vivienne/Urho3DIDE/Urho3DPlus/Source/Editor/EPScene3D.cpp:2393:7: note:   no known conversion for argument 2 from ?Urho3D::VariantMap {aka Urho3D::HashMap<Urho3D::StringHash, Urho3D::Variant>}? to ?Urho3D::VariantMap& {aka Urho3D::HashMap<Urho3D::StringHash, Urho3D::Variant>&}?
/media/home2/vivienne/Urho3DIDE/Urho3DPlus/Source/Editor/EPScene3D.cpp: In member function ?void Urho3D::EPScene3DView::SetOrthographic(bool)?:
/media/home2/vivienne/Urho3DIDE/Urho3DPlus/Source/Editor/EPScene3D.cpp:2518:50: error: no matching function for call to ?Urho3D::EPScene3DView::UpdateSettingsUI(const Urho3D::StringHash&, Urho3D::VariantMap)?
/media/home2/vivienne/Urho3DIDE/Urho3DPlus/Source/Editor/EPScene3D.cpp:2518:50: note: candidate is:
/media/home2/vivienne/Urho3DIDE/Urho3DPlus/Source/Editor/EPScene3D.cpp:2393:7: note: void Urho3D::EPScene3DView::UpdateSettingsUI(Urho3D::StringHash, Urho3D::VariantMap&)
/media/home2/vivienne/Urho3DIDE/Urho3DPlus/Source/Editor/EPScene3D.cpp:2393:7: note:   no known conversion for argument 2 from ?Urho3D::VariantMap {aka Urho3D::HashMap<Urho3D::StringHash, Urho3D::Variant>}? to ?Urho3D::VariantMap& {aka Urho3D::HashMap<Urho3D::StringHash, Urho3D::Variant>&}?
/media/home2/vivienne/Urho3DIDE/Urho3DPlus/Source/Editor/EPScene3D.cpp: In member function ?void Urho3D::EPScene3DView::ToggleViewportSettingsWindow(Urho3D::StringHash, Urho3D::VariantMap&)?:
/media/home2/vivienne/Urho3DIDE/Urho3DPlus/Source/Editor/EPScene3D.cpp:2577:62: error: no matching function for call to ?Urho3D::EPScene3DView::CloseViewportSettingsWindow(const Urho3D::StringHash&, Urho3D::VariantMap)?
/media/home2/vivienne/Urho3DIDE/Urho3DPlus/Source/Editor/EPScene3D.cpp:2577:62: note: candidate is:
/media/home2/vivienne/Urho3DIDE/Urho3DPlus/Source/Editor/EPScene3D.cpp:2388:7: note: void Urho3D::EPScene3DView::CloseViewportSettingsWindow(Urho3D::StringHash, Urho3D::VariantMap&)
/media/home2/vivienne/Urho3DIDE/Urho3DPlus/Source/Editor/EPScene3D.cpp:2388:7: note:   no known conversion for argument 2 from ?Urho3D::VariantMap {aka Urho3D::HashMap<Urho3D::StringHash, Urho3D::Variant>}? to ?Urho3D::VariantMap& {aka Urho3D::HashMap<Urho3D::StringHash, Urho3D::Variant>&}?
make[2]: *** [Urho3DPlus/CMakeFiles/Urho3DPlus.dir/Source/Editor/EPScene3D.cpp.o] Error 1
make[1]: *** [Urho3DPlus/CMakeFiles/Urho3DPlus.dir/all] Error 2
make: *** [all] Error 2
[/code]

-------------------------

GoogleBot42 | 2017-01-02 01:04:25 UTC | #46

Rewrite: 
[code]void Urho3D::EPScene3DView::ToggleViewportSettingsWindow(Urho3D::StringHash, Urho3D::VariantMap&)[/code]
To:
[code]void Urho3D::EPScene3DView::ToggleViewportSettingsWindow(Urho3D::StringHash, const Urho3D::VariantMap&)[/code]

-------------------------

jmiller | 2017-01-02 01:04:25 UTC | #47

[quote="vivienneanthony"]These are the errors I get. Repository at [github.com/vivienneanthony/Urho3DIDE](https://github.com/vivienneanthony/Urho3DIDE)

[code]Urho3DIDE/Urho3DPlus/Source/Editor/EPScene3D.cpp: In member function ?void Urho3D::EPScene3D::ViewRaycast(bool)?:
Urho3DIDE/Urho3DPlus/Source/Editor/EPScene3D.cpp:1039:169: error: no matching function for call to ?Urho3D::Octree::RaycastSingle(Urho3D::RayOctreeQuery)?
Urho3DIDE/Urho3DPlus/Source/Editor/EPScene3D.cpp:1039:169: note: candidate is:
Urho3D-native/include/Urho3D/ThirdParty/../Graphics/Octree.h:187:10: note: void Urho3D::Octree::RaycastSingle(Urho3D::RayOctreeQuery&) const
Urho3D-native/include/Urho3D/ThirdParty/../Graphics/Octree.h:187:10: note:   no known conversion for argument 1 from ?Urho3D::RayOctreeQuery? to ?Urho3D::RayOctreeQuery&?
[/code]
[/quote]
(I reduced the code vivienne quoted; it may have occurred more than once)

try:
[code]RayOctreeQuery query(result_,cameraRay, RAY_TRIANGLE, camera_->GetFarClip(), pickModeDrawableFlags[pickMode], 0x7fffffff);
editorScene->GetComponent<Octree>()->RaycastSingle(query);[/code]

from [stackoverflow.com/questions/3897 ... -not-gcc-g](http://stackoverflow.com/questions/3897702/why-does-msvc-let-me-do-this-but-not-gcc-g)
[quote]
I think this is an old compiler extension that Visual Studio supported since way back then, but it is kept around in modern Visual C++ for compatibility. Try disabling compiler extensions (/Za flag) and see what happens.
Alternatively, use the /W4 flag to get maximum warnings, and it should complain:
warning C4239: nonstandard extension used

On GCC I get the const reference error:
error: invalid initialization of non-const reference of type ?std::string&? from a temporary of type ?std::string?[/quote]

-------------------------

vivienneanthony | 2017-01-02 01:04:25 UTC | #48

Hey

I got it to maybe 80% and It's trying to link with massive muiltiple definitions errors Which I think might be a linker error?

I'm going try to see if theres a flag for gcc?

Vivienne


[code]naje: command not found
vivienne@vivienne-System-Product-Name:/media/home2/vivienne/Urho3DIDE/Build$ make
[ 77%] Built target Urho3DPlus
Linking CXX executable ../bin/IDE
../Urho3DPlus/libUrho3DPlus.a(ProjectManager.cpp.o): In function `Urho3D::ProjectManager::HandleOpenProject(Urho3D::StringHash, Urho3D::HashMap<Urho3D::StringHash, Urho3D::Variant>&)':
ProjectManager.cpp:(.text+0x20): multiple definition of `Urho3D::ProjectManager::HandleOpenProject(Urho3D::StringHash, Urho3D::HashMap<Urho3D::StringHash, Urho3D::Variant>&)'
CMakeFiles/IDE.dir/Source/IDE/ProjectManager.cpp.o:ProjectManager.cpp:(.text+0x20): first defined here
../Urho3DPlus/libUrho3DPlus.a(ProjectManager.cpp.o): In function `Urho3D::ProjectSettings::~ProjectSettings()':
ProjectManager.cpp:(.text+0x50): multiple definition of `Urho3D::ProjectSettings::~ProjectSettings()'
CMakeFiles/IDE.dir/Source/IDE/ProjectManager.cpp.o:ProjectManager.cpp:(.text+0x50): first defined here
../Urho3DPlus/libUrho3DPlus.a(ProjectManager.cpp.o): In function `Urho3D::ProjectSettings::~ProjectSettings()':
ProjectManager.cpp:(.text+0x180): multiple definition of `Urho3D::ProjectSettings::~ProjectSettings()'
CMakeFiles/IDE.dir/Source/IDE/ProjectManager.cpp.o:ProjectManager.cpp:(.text+0x180): first defined here
../Urho3DPlus/libUrho3DPlus.a(ProjectManager.cpp.o): In function `Urho3D::ProjectManager::HandleProjectListClick(Urho3D::StringHash, Urho3D::HashMap<Urho3D::StringHash, Urho3D::Variant>&)':
ProjectManager.cpp:(.text+0x230): multiple definition of `Urho3D::ProjectManager::HandleProjectListClick(Urho3D::StringHash, Urho3D::HashMap<Urho3D::StringHash, Urho3D::Variant>&)'
CMakeFiles/IDE.dir/Source/IDE/ProjectManager.cpp.o:ProjectManager.cpp:(.text+0x230): first defined here
../Urho3DPlus/libUrho3DPlus.a(ProjectManager.cpp.o): In function `Urho3D::ProjectManager::HandleOnTemplateClick(Urho3D::StringHash, Urho3D::HashMap<Urho3D::StringHash, Urho3D::Variant>&)':
ProjectManager.cpp:(.text+0x830): multiple definition of `Urho3D::ProjectManager::HandleOnTemplateClick(Urho3D::StringHash, Urho3D::HashMap<Urho3D::StringHash, Urho3D::Variant>&)'
CMakeFiles/IDE.dir/Source/IDE/ProjectManager.cpp.o:ProjectManager.cpp:(.text+0x36c0): first defined here
../Urho3DPlus/libUrho3DPlus.a(ProjectManager.cpp.o): In function `Urho3D::ProjectManager::NewProject()':
ProjectManager.cpp:(.text+0x12f0): multiple definition of `Urho3D::ProjectManager::NewProject()'
CMakeFiles/IDE.dir/Source/IDE/ProjectManager.cpp.o:ProjectManager.cpp:(.text+0x830): first defined here
../Urho3DPlus/libUrho3DPlus.a(ProjectManager.cpp.o): In function `Urho3D::ProjectManager::HandleNewProjectAck(Urho3D::StringHash, Urho3D::HashMap<Urho3D::StringHash, Urho3D::Variant>&)':
ProjectManager.cpp:(.text+0x1790): multiple definition of `Urho3D::ProjectManager::HandleNewProjectAck(Urho3D::StringHash, Urho3D::HashMap<Urho3D::StringHash, Urho3D::Variant>&)'
CMakeFiles/IDE.dir/Source/IDE/ProjectManager.cpp.o:ProjectManager.cpp:(.text+0xcf0): first defined here
../Urho3DPlus/libUrho3DPlus.a(ProjectManager.cpp.o): In function `Urho3D::ProjectManager::ChooseRootDir()':
ProjectManager.cpp:(.text+0x1bd0): multiple definition of `Urho3D::ProjectManager::ChooseRootDir()'
CMakeFiles/IDE.dir/Source/IDE/ProjectManager.cpp.o:ProjectManager.cpp:(.text+0x1130): first defined here
../Urho3DPlus/libUrho3DPlus.a(ProjectManager.cpp.o): In function `Urho3D::ProjectManager::HandleRootSelected(Urho3D::StringHash, Urho3D::HashMap<Urho3D::StringHash, Urho3D::Variant>&)':
ProjectManager.cpp:(.text+0x85f0): multiple definition of `Urho3D::ProjectManager::HandleRootSelected(Urho3D::StringHash, Urho3D::HashMap<Urho3D::StringHash, Urho3D::Variant>&)'
CMakeFiles/IDE.dir/Source/IDE/ProjectManager.cpp.o:ProjectManager.cpp:(.text+0x8240): first defined here
../Urho3DPlus/libUrho3DPlus.a(ProjectManager.cpp.o): In function `Urho3D::ProjectManager::HandleChangeRootDir(Urho3D::StringHash, Urho3D::HashMap<Urho3D::StringHash, Urho3D::Variant>&)':
ProjectManager.cpp:(.text+0x21c0): multiple definition of `Urho3D::ProjectManager::HandleChangeRootDir(Urho3D::StringHash, Urho3D::HashMap<Urho3D::StringHash, Urho3D::Variant>&)'
CMakeFiles/IDE.dir/Source/IDE/ProjectManager.cpp.o:ProjectManager.cpp:(.text+0x1720): first defined here
../Urho3DPlus/libUrho3DPlus.a(ProjectManager.cpp.o): In function `Urho3D::ProjectManager::OpenProject(Urho3D::String const&)':
ProjectManager.cpp:(.text+0x21d0): multiple definition of `Urho3D::ProjectManager::OpenProject(Urho3D::String const&)'
CMakeFiles/IDE.dir/Source/IDE/ProjectManager.cpp.o:ProjectManager.cpp:(.text+0x1730): first defined here
../Urho3DPlus/libUrho3DPlus.a(ProjectManager.cpp.o): In function `Urho3D::ProjectManager::OpenProject(Urho3D::ProjectSettings const*)':
ProjectManager.cpp:(.text+0x21e0): multiple definition of `Urho3D::ProjectManager::OpenProject(Urho3D::ProjectSettings const*)'
CMakeFiles/IDE.dir/Source/IDE/ProjectManager.cpp.o:ProjectManager.cpp:(.text+0x1760): first defined here
../Urho3DPlus/libUrho3DPlus.a(ProjectManager.cpp.o): In function `Urho3D::ProjectManager::CreateDirSelector(Urho3D::String const&, Urho3D::String const&, Urho3D::String const&, Urho3D::String const&)':
ProjectManager.cpp:(.text+0x2210): multiple definition of `Urho3D::ProjectManager::CreateDirSelector(Urho3D::String const&, Urho3D::String const&, Urho3D::String const&, Urho3D::String const&)'
CMakeFiles/IDE.dir/Source/IDE/ProjectManager.cpp.o:ProjectManager.cpp:(.text+0x1790): first defined here
../Urho3DPlus/libUrho3DPlus.a(ProjectManager.cpp.o): In function `Urho3D::ProjectManager::CloseDirSelector(Urho3D::String&)':
ProjectManager.cpp:(.text+0x2480): multiple definition of `Urho3D::ProjectManager::CloseDirSelector(Urho3D::String&)'
CMakeFiles/IDE.dir/Source/IDE/ProjectManager.cpp.o:ProjectManager.cpp:(.text+0x19f0): first defined here
../Urho3DPlus/libUrho3DPlus.a(ProjectManager.cpp.o): In function `Urho3D::ProjectManager::CloseDirSelector()':
ProjectManager.cpp:(.text+0x2560): multiple definition of `Urho3D::ProjectManager::CloseDirSelector()'
CMakeFiles/IDE.dir/Source/IDE/ProjectManager.cpp.o:ProjectManager.cpp:(.text+0x1ad0): first defined here
../Urho3DPlus/libUrho3DPlus.a(ProjectManager.cpp.o): In function `Urho3D::ProjectManager::GetRootDir()':
ProjectManager.cpp:(.text+0x2580): multiple definition of `Urho3D::ProjectManager::GetRootDir()'
CMakeFiles/IDE.dir/Source/IDE/ProjectManager.cpp.o:ProjectManager.cpp:(.text+0x1af0): first defined here
../Urho3DPlus/libUrho3DPlus.a(ProjectManager.cpp.o): In function `Urho3D::ProjectManager::GetProject()':
ProjectManager.cpp:(.text+0x2590): multiple definition of `Urho3D::ProjectManager::GetProject()'
CMakeFiles/IDE.dir/Source/IDE/ProjectManager.cpp.o:ProjectManager.cpp:(.text+0x1b00): first defined here
../Urho3DPlus/libUrho3DPlus.a(ProjectManager.cpp.o): In function `Urho3D::ProjectSettings::ProjectSettings(Urho3D::Context*)':
ProjectManager.cpp:(.text+0x25a0): multiple definition of `Urho3D::ProjectSettings::ProjectSettings(Urho3D::Context*)'
CMakeFiles/IDE.dir/Source/IDE/ProjectManager.cpp.o:ProjectManager.cpp:(.text+0x1b10): first defined here
../Urho3DPlus/libUrho3DPlus.a(ProjectManager.cpp.o): In function `Urho3D::ProjectManager::HandleNewProject(Urho3D::StringHash, Urho3D::HashMap<Urho3D::StringHash, Urho3D::Variant>&)':
ProjectManager.cpp:(.text+0x2880): multiple definition of `Urho3D::ProjectManager::HandleNewProject(Urho3D::StringHash, Urho3D::HashMap<Urho3D::StringHash, Urho3D::Variant>&)'
CMakeFiles/IDE.dir/Source/IDE/ProjectManager.cpp.o:ProjectManager.cpp:(.text+0x1df0): first defined here
../Urho3DPlus/libUrho3DPlus.a(ProjectManager.cpp.o): In function `Urho3D::ProjectSettings::ProjectSettings(Urho3D::Context*)':
ProjectManager.cpp:(.text+0x25a0): multiple definition of `Urho3D::ProjectSettings::ProjectSettings(Urho3D::Context*)'
CMakeFiles/IDE.dir/Source/IDE/ProjectManager.cpp.o:ProjectManager.cpp:(.text+0x1b10): first defined here
../Urho3DPlus/libUrho3DPlus.a(ProjectManager.cpp.o): In function `Urho3D::ProjectSettings::CopyAttr(Urho3D::ProjectSettings*)':
ProjectManager.cpp:(.text+0x3de0): multiple definition of `Urho3D::ProjectSettings::CopyAttr(Urho3D::ProjectSettings*)'
CMakeFiles/IDE.dir/Source/IDE/ProjectManager.cpp.o:ProjectManager.cpp:(.text+0x3350): first defined here
../Urho3DPlus/libUrho3DPlus.a(ProjectManager.cpp.o): In function `Urho3D::ProjectManager::RegisterObject(Urho3D::Context*)':
ProjectManager.cpp:(.text+0x4150): multiple definition of `Urho3D::ProjectManager::RegisterObject(Urho3D::Context*)'
CMakeFiles/IDE.dir/Source/IDE/ProjectManager.cpp.o:ProjectManager.cpp:(.text+0x3d50): first defined here
../Urho3DPlus/libUrho3DPlus.a(ProjectManager.cpp.o): In function `Urho3D::ProjectSettings::RegisterObject(Urho3D::Context*)':
ProjectManager.cpp:(.text+0x4160): multiple definition of `Urho3D::ProjectSettings::RegisterObject(Urho3D::Context*)'
CMakeFiles/IDE.dir/Source/IDE/ProjectManager.cpp.o:ProjectManager.cpp:(.text+0x3d60): first defined here
../Urho3DPlus/libUrho3DPlus.a(ProjectManager.cpp.o): In function `Urho3D::ProjectManager::ProjectManager(Urho3D::Context*)':
ProjectManager.cpp:(.text+0x53a0): multiple definition of `Urho3D::ProjectManager::ProjectManager(Urho3D::Context*)'
CMakeFiles/IDE.dir/Source/IDE/ProjectManager.cpp.o:ProjectManager.cpp:(.text+0x4fa0): first defined here
../Urho3DPlus/libUrho3DPlus.a(ProjectManager.cpp.o): In function `Urho3D::ProjectManager::ProjectManager(Urho3D::Context*)':
ProjectManager.cpp:(.text+0x53a0): multiple definition of `Urho3D::ProjectManager::ProjectManager(Urho3D::Context*)'
CMakeFiles/IDE.dir/Source/IDE/ProjectManager.cpp.o:ProjectManager.cpp:(.text+0x4fa0): first defined here
../Urho3DPlus/libUrho3DPlus.a(ProjectManager.cpp.o): In function `Urho3D::ProjectManager::~ProjectManager()':
ProjectManager.cpp:(.text+0x5610): multiple definition of `Urho3D::ProjectManager::~ProjectManager()'
CMakeFiles/IDE.dir/Source/IDE/ProjectManager.cpp.o:ProjectManager.cpp:(.text+0x5250): first defined here
../Urho3DPlus/libUrho3DPlus.a(ProjectManager.cpp.o): In function `Urho3D::ProjectManager::~ProjectManager()':
ProjectManager.cpp:(.text+0x57e0): multiple definition of `Urho3D::ProjectManager::~ProjectManager()'
CMakeFiles/IDE.dir/Source/IDE/ProjectManager.cpp.o:ProjectManager.cpp:(.text+0x5400): first defined here
../Urho3DPlus/libUrho3DPlus.a(ProjectManager.cpp.o): In function `Urho3D::ProjectManager::~ProjectManager()':
ProjectManager.cpp:(.text+0x5610): multiple definition of `Urho3D::ProjectManager::~ProjectManager()'
CMakeFiles/IDE.dir/Source/IDE/ProjectManager.cpp.o:ProjectManager.cpp:(.text+0x5250): first defined here
../Urho3DPlus/libUrho3DPlus.a(ProjectManager.cpp.o): In function `Urho3D::ProjectManager::UpdateProjects(Urho3D::String const&)':
ProjectManager.cpp:(.text+0x5800): multiple definition of `Urho3D::ProjectManager::UpdateProjects(Urho3D::String const&)'
CMakeFiles/IDE.dir/Source/IDE/ProjectManager.cpp.o:ProjectManager.cpp:(.text+0x5420): first defined here
../Urho3DPlus/libUrho3DPlus.a(ProjectManager.cpp.o): In function `Urho3D::ProjectManager::CreateWelcomeScreen()':
ProjectManager.cpp:(.text+0x7450): multiple definition of `Urho3D::ProjectManager::CreateWelcomeScreen()'
CMakeFiles/IDE.dir/Source/IDE/ProjectManager.cpp.o:ProjectManager.cpp:(.text+0x7080): first defined here
../Urho3DPlus/libUrho3DPlus.a(ProjectManager.cpp.o): In function `Urho3D::ProjectManager::HandleRescanProjects(Urho3D::StringHash, Urho3D::HashMap<Urho3D::StringHash, Urho3D::Variant>&)':
ProjectManager.cpp:(.text+0x85e0): multiple definition of `Urho3D::ProjectManager::HandleRescanProjects(Urho3D::StringHash, Urho3D::HashMap<Urho3D::StringHash, Urho3D::Variant>&)'
CMakeFiles/IDE.dir/Source/IDE/ProjectManager.cpp.o:ProjectManager.cpp:(.text+0x8220): first defined here
../Urho3DPlus/libUrho3DPlus.a(ProjectManager.cpp.o): In function `Urho3D::ProjectManager::ShowWelcomeScreen(bool)':
ProjectManager.cpp:(.text+0x8570): multiple definition of `Urho3D::ProjectManager::ShowWelcomeScreen(bool)'
CMakeFiles/IDE.dir/Source/IDE/ProjectManager.cpp.o:ProjectManager.cpp:(.text+0x81b0): first defined here
../Urho3DPlus/libUrho3DPlus.a(ProjectManager.cpp.o): In function `Urho3D::ProjectSettings::~ProjectSettings()':
ProjectManager.cpp:(.text+0x50): multiple definition of `Urho3D::ProjectSettings::~ProjectSettings()'
CMakeFiles/IDE.dir/Source/IDE/ProjectManager.cpp.o:ProjectManager.cpp:(.text+0x50): first defined here
collect2: ld returned 1 exit status
make[2]: *** [bin/IDE] Error 1
make[1]: *** [IDE/CMakeFiles/IDE.dir/all] Error 2
make: *** [all] Error 2
vivienne@vivienne-System-Product-Name:/media/home2/vivienne/Urho3DIDE/Build$ 
[/code]

-------------------------

vivienneanthony | 2017-01-02 01:04:26 UTC | #49

Updated

It' was actually 91%. I changed some files to try to avoid the muiltiple definitions maybe someone sees a  problem. Almost close to cross platform compatibility.

[github.com/vivienneanthony/Urho3DIDE](https://github.com/vivienneanthony/Urho3DIDE)

Build[code]
vivienne@vivienne-System-Product-Name:/media/home2/vivienne/Urho3DIDE$ ./cmake_generic.sh Build
-- The C compiler identification is GNU 4.6.3
-- The CXX compiler identification is GNU 4.6.3
-- Check for working C compiler: /usr/bin/cc
-- Check for working C compiler: /usr/bin/cc -- works
-- Detecting C compiler ABI info
-- Detecting C compiler ABI info - done
-- Detecting C compile features
-- Detecting C compile features - done
-- Check for working CXX compiler: /usr/bin/c++
-- Check for working CXX compiler: /usr/bin/c++ -- works
-- Detecting CXX compiler ABI info
-- Detecting CXX compiler ABI info - done
-- Detecting CXX compile features
-- Detecting CXX compile features - done
-- Found Urho3D: /media/home2/vivienne/Urho3D-native/lib/libUrho3D.a
-- Configuring done
-- Generating done
-- Build files have been written to: /media/home2/vivienne/Urho3DIDE/Build
vivienne@vivienne-System-Product-Name:/media/home2/vivienne/Urho3DIDE$ cd Build
vivienne@vivienne-System-Product-Name:/media/home2/vivienne/Urho3DIDE/Build$ make
Scanning dependencies of target Urho3DPlus
[  2%] Building CXX object Urho3DPlus/CMakeFiles/Urho3DPlus.dir/Source/Input/InputActionSystem.cpp.o
[  5%] Building CXX object Urho3DPlus/CMakeFiles/Urho3DPlus.dir/Source/UI/UIUtils.cpp.o                                                                                                                    
[  8%] Building CXX object Urho3DPlus/CMakeFiles/Urho3DPlus.dir/Source/UI/AttributeContainer.cpp.o                                                                                                         
[ 11%] Building CXX object Urho3DPlus/CMakeFiles/Urho3DPlus.dir/Source/UI/DirSelector.cpp.o                                                                                                                
[ 13%] Building CXX object Urho3DPlus/CMakeFiles/Urho3DPlus.dir/Source/UI/AttributeInspector.cpp.o                                                                                                         
[ 16%] Building CXX object Urho3DPlus/CMakeFiles/Urho3DPlus.dir/Source/UI/HierarchyWindow.cpp.o                                                                                                            
[ 19%] Building CXX object Urho3DPlus/CMakeFiles/Urho3DPlus.dir/Source/UI/TabWindow.cpp.o                                                                                                                  
[ 22%] Building CXX object Urho3DPlus/CMakeFiles/Urho3DPlus.dir/Source/UI/MiniToolBarUI.cpp.o                                                                                                              
[ 25%] Building CXX object Urho3DPlus/CMakeFiles/Urho3DPlus.dir/Source/UI/MenuBarUI.cpp.o                                                                                                                  
[ 27%] Building CXX object Urho3DPlus/CMakeFiles/Urho3DPlus.dir/Source/UI/AttributeVariable.cpp.o                                                                                                          
[ 30%] Building CXX object Urho3DPlus/CMakeFiles/Urho3DPlus.dir/Source/UI/ModalWindow.cpp.o                                                                                                                
[ 33%] Building CXX object Urho3DPlus/CMakeFiles/Urho3DPlus.dir/Source/UI/ResourcePicker.cpp.o                                                                                                             
[ 36%] Building CXX object Urho3DPlus/CMakeFiles/Urho3DPlus.dir/Source/UI/ToolBarUI.cpp.o                                                                                                                  
[ 38%] Building CXX object Urho3DPlus/CMakeFiles/Urho3DPlus.dir/Source/Project/ProjectWindow.cpp.o                                                                                                         
/media/home2/vivienne/Urho3DIDE/Urho3DPlus/Source/Project/ProjectWindow.cpp:99:14: warning: multi-character character constant [-Wmultichar]
/media/home2/vivienne/Urho3DIDE/Urho3DPlus/Source/Project/ProjectWindow.cpp:121:15: warning: multi-character character constant [-Wmultichar]
/media/home2/vivienne/Urho3DIDE/Urho3DPlus/Source/Project/ProjectWindow.cpp: In member function ?void Urho3D::ProjectWindow::UpdateWindow()?:
/media/home2/vivienne/Urho3DIDE/Urho3DPlus/Source/Project/ProjectWindow.cpp:99:23: warning: overflow in implicit constant conversion [-Woverflow]
/media/home2/vivienne/Urho3DIDE/Urho3DPlus/Source/Project/ProjectWindow.cpp: In member function ?void Urho3D::ProjectWindow::UnloadProject()?:
/media/home2/vivienne/Urho3DIDE/Urho3DPlus/Source/Project/ProjectWindow.cpp:121:24: warning: overflow in implicit constant conversion [-Woverflow]
[ 41%] Building CXX object Urho3DPlus/CMakeFiles/Urho3DPlus.dir/Source/Project/TemplateManager.cpp.o
[ 44%] Building CXX object Urho3DPlus/CMakeFiles/Urho3DPlus.dir/Source/Project/ProjectManager.cpp.o                                                                                                        
[ 47%] Building CXX object Urho3DPlus/CMakeFiles/Urho3DPlus.dir/Source/Editor/EditorView.cpp.o                                                                                                             
[ 50%] Building CXX object Urho3DPlus/CMakeFiles/Urho3DPlus.dir/Source/Editor/Editor.cpp.o                                                                                                                 
[ 52%] Building CXX object Urho3DPlus/CMakeFiles/Urho3DPlus.dir/Source/Editor/GizmoScene3D.cpp.o                                                                                                           
[ 55%] Building CXX object Urho3DPlus/CMakeFiles/Urho3DPlus.dir/Source/Editor/EPScene3D.cpp.o                                                                                                              
[ 58%] Building CXX object Urho3DPlus/CMakeFiles/Urho3DPlus.dir/Source/Editor/EditorData.cpp.o                                                                                                             
[ 61%] Building CXX object Urho3DPlus/CMakeFiles/Urho3DPlus.dir/Source/Editor/ResourceBrowser.cpp.o                                                                                                        
[ 63%] Building CXX object Urho3DPlus/CMakeFiles/Urho3DPlus.dir/Source/Editor/EditorSelection.cpp.o                                                                                                        
[ 66%] Building CXX object Urho3DPlus/CMakeFiles/Urho3DPlus.dir/Source/Editor/EditorPlugin.cpp.o                                                                                                           
[ 69%] Building CXX object Urho3DPlus/CMakeFiles/Urho3DPlus.dir/Source/Editor/EPScene2D.cpp.o                                                                                                              
[ 72%] Building CXX object Urho3DPlus/CMakeFiles/Urho3DPlus.dir/Source/Editor/InGameEditor.cpp.o                                                                                                           
[ 75%] Building CXX object Urho3DPlus/CMakeFiles/Urho3DPlus.dir/Source/Editor/PluginScene3DEditor.cpp.o                                                                                                    
[ 77%] Building CXX object Urho3DPlus/CMakeFiles/Urho3DPlus.dir/Source/AppStates/AppStateManager.cpp.o                                                                                                     
Linking CXX static library libUrho3DPlus.a
[ 77%] Built target Urho3DPlus
Scanning dependencies of target IDE
[ 80%] Building CXX object IDE/CMakeFiles/IDE.dir/Source/IDE/IDE.cpp.o
[ 83%] Building CXX object IDE/CMakeFiles/IDE.dir/Source/IDE/IDESettings.cpp.o                                                                                                                             
[ 86%] Building CXX object IDE/CMakeFiles/IDE.dir/Source/IDE/ProjectWindow.cpp.o                                                                                                                           
/media/home2/vivienne/Urho3DIDE/IDE/Source/IDE/ProjectWindow.cpp:99:14: warning: multi-character character constant [-Wmultichar]
/media/home2/vivienne/Urho3DIDE/IDE/Source/IDE/ProjectWindow.cpp:121:15: warning: multi-character character constant [-Wmultichar]
/media/home2/vivienne/Urho3DIDE/IDE/Source/IDE/ProjectWindow.cpp: In member function ?void Urho3D::ProjectWindow::UpdateWindow()?:
/media/home2/vivienne/Urho3DIDE/IDE/Source/IDE/ProjectWindow.cpp:99:23: warning: overflow in implicit constant conversion [-Woverflow]
/media/home2/vivienne/Urho3DIDE/IDE/Source/IDE/ProjectWindow.cpp: In member function ?void Urho3D::ProjectWindow::UnloadProject()?:
/media/home2/vivienne/Urho3DIDE/IDE/Source/IDE/ProjectWindow.cpp:121:24: warning: overflow in implicit constant conversion [-Woverflow]
[ 88%] Building CXX object IDE/CMakeFiles/IDE.dir/Source/IDE/TemplateManager.cpp.o
[ 91%] Building CXX object IDE/CMakeFiles/IDE.dir/Source/IDE/ProjectManager.cpp.o                                                                                                                          
Linking CXX executable ../bin/IDE
../Urho3DPlus/libUrho3DPlus.a(ProjectManager.cpp.o): In function `Urho3D::ProjectManager::HandleOpenProject(Urho3D::StringHash, Urho3D::HashMap<Urho3D::StringHash, Urho3D::Variant>&)':
ProjectManager.cpp:(.text+0x20): multiple definition of `Urho3D::ProjectManager::HandleOpenProject(Urho3D::StringHash, Urho3D::HashMap<Urho3D::StringHash, Urho3D::Variant>&)'
CMakeFiles/IDE.dir/Source/IDE/ProjectManager.cpp.o:ProjectManager.cpp:(.text+0x20): first defined here
../Urho3DPlus/libUrho3DPlus.a(ProjectManager.cpp.o): In function `Urho3D::ProjectSettings::~ProjectSettings()':
ProjectManager.cpp:(.text+0x50): multiple definition of `Urho3D::ProjectSettings::~ProjectSettings()'
CMakeFiles/IDE.dir/Source/IDE/ProjectManager.cpp.o:ProjectManager.cpp:(.text+0x50): first defined here
../Urho3DPlus/libUrho3DPlus.a(ProjectManager.cpp.o): In function `Urho3D::ProjectSettings::~ProjectSettings()':
ProjectManager.cpp:(.text+0x180): multiple definition of `Urho3D::ProjectSettings::~ProjectSettings()'
CMakeFiles/IDE.dir/Source/IDE/ProjectManager.cpp.o:ProjectManager.cpp:(.text+0x180): first defined here
../Urho3DPlus/libUrho3DPlus.a(ProjectManager.cpp.o): In function `Urho3D::ProjectManager::HandleProjectListClick(Urho3D::StringHash, Urho3D::HashMap<Urho3D::StringHash, Urho3D::Variant>&)':
ProjectManager.cpp:(.text+0x230): multiple definition of `Urho3D::ProjectManager::HandleProjectListClick(Urho3D::StringHash, Urho3D::HashMap<Urho3D::StringHash, Urho3D::Variant>&)'
CMakeFiles/IDE.dir/Source/IDE/ProjectManager.cpp.o:ProjectManager.cpp:(.text+0x230): first defined here
../Urho3DPlus/libUrho3DPlus.a(ProjectManager.cpp.o): In function `Urho3D::ProjectManager::HandleOnTemplateClick(Urho3D::StringHash, Urho3D::HashMap<Urho3D::StringHash, Urho3D::Variant>&)':
ProjectManager.cpp:(.text+0x830): multiple definition of `Urho3D::ProjectManager::HandleOnTemplateClick(Urho3D::StringHash, Urho3D::HashMap<Urho3D::StringHash, Urho3D::Variant>&)'
CMakeFiles/IDE.dir/Source/IDE/ProjectManager.cpp.o:ProjectManager.cpp:(.text+0x36c0): first defined here
../Urho3DPlus/libUrho3DPlus.a(ProjectManager.cpp.o): In function `Urho3D::ProjectManager::NewProject()':
ProjectManager.cpp:(.text+0x12f0): multiple definition of `Urho3D::ProjectManager::NewProject()'
CMakeFiles/IDE.dir/Source/IDE/ProjectManager.cpp.o:ProjectManager.cpp:(.text+0x830): first defined here
../Urho3DPlus/libUrho3DPlus.a(ProjectManager.cpp.o): In function `Urho3D::ProjectManager::HandleNewProjectAck(Urho3D::StringHash, Urho3D::HashMap<Urho3D::StringHash, Urho3D::Variant>&)':
ProjectManager.cpp:(.text+0x1790): multiple definition of `Urho3D::ProjectManager::HandleNewProjectAck(Urho3D::StringHash, Urho3D::HashMap<Urho3D::StringHash, Urho3D::Variant>&)'
CMakeFiles/IDE.dir/Source/IDE/ProjectManager.cpp.o:ProjectManager.cpp:(.text+0xcf0): first defined here
../Urho3DPlus/libUrho3DPlus.a(ProjectManager.cpp.o): In function `Urho3D::ProjectManager::ChooseRootDir()':
ProjectManager.cpp:(.text+0x1bd0): multiple definition of `Urho3D::ProjectManager::ChooseRootDir()'
CMakeFiles/IDE.dir/Source/IDE/ProjectManager.cpp.o:ProjectManager.cpp:(.text+0x1130): first defined here
../Urho3DPlus/libUrho3DPlus.a(ProjectManager.cpp.o): In function `Urho3D::ProjectManager::HandleRootSelected(Urho3D::StringHash, Urho3D::HashMap<Urho3D::StringHash, Urho3D::Variant>&)':
ProjectManager.cpp:(.text+0x85f0): multiple definition of `Urho3D::ProjectManager::HandleRootSelected(Urho3D::StringHash, Urho3D::HashMap<Urho3D::StringHash, Urho3D::Variant>&)'
CMakeFiles/IDE.dir/Source/IDE/ProjectManager.cpp.o:ProjectManager.cpp:(.text+0x8270): first defined here
../Urho3DPlus/libUrho3DPlus.a(ProjectManager.cpp.o): In function `Urho3D::ProjectManager::HandleChangeRootDir(Urho3D::StringHash, Urho3D::HashMap<Urho3D::StringHash, Urho3D::Variant>&)':
ProjectManager.cpp:(.text+0x21c0): multiple definition of `Urho3D::ProjectManager::HandleChangeRootDir(Urho3D::StringHash, Urho3D::HashMap<Urho3D::StringHash, Urho3D::Variant>&)'
CMakeFiles/IDE.dir/Source/IDE/ProjectManager.cpp.o:ProjectManager.cpp:(.text+0x1720): first defined here
../Urho3DPlus/libUrho3DPlus.a(ProjectManager.cpp.o): In function `Urho3D::ProjectManager::OpenProject(Urho3D::String const&)':
ProjectManager.cpp:(.text+0x21d0): multiple definition of `Urho3D::ProjectManager::OpenProject(Urho3D::String const&)'
CMakeFiles/IDE.dir/Source/IDE/ProjectManager.cpp.o:ProjectManager.cpp:(.text+0x1730): first defined here
../Urho3DPlus/libUrho3DPlus.a(ProjectManager.cpp.o): In function `Urho3D::ProjectManager::OpenProject(Urho3D::ProjectSettings const*)':
ProjectManager.cpp:(.text+0x21e0): multiple definition of `Urho3D::ProjectManager::OpenProject(Urho3D::ProjectSettings const*)'
CMakeFiles/IDE.dir/Source/IDE/ProjectManager.cpp.o:ProjectManager.cpp:(.text+0x1760): first defined here
../Urho3DPlus/libUrho3DPlus.a(ProjectManager.cpp.o): In function `Urho3D::ProjectManager::CreateDirSelector(Urho3D::String const&, Urho3D::String const&, Urho3D::String const&, Urho3D::String const&)':
ProjectManager.cpp:(.text+0x2210): multiple definition of `Urho3D::ProjectManager::CreateDirSelector(Urho3D::String const&, Urho3D::String const&, Urho3D::String const&, Urho3D::String const&)'
CMakeFiles/IDE.dir/Source/IDE/ProjectManager.cpp.o:ProjectManager.cpp:(.text+0x1790): first defined here
../Urho3DPlus/libUrho3DPlus.a(ProjectManager.cpp.o): In function `Urho3D::ProjectManager::CloseDirSelector(Urho3D::String&)':
ProjectManager.cpp:(.text+0x2470): multiple definition of `Urho3D::ProjectManager::CloseDirSelector(Urho3D::String&)'
CMakeFiles/IDE.dir/Source/IDE/ProjectManager.cpp.o:ProjectManager.cpp:(.text+0x19f0): first defined here
../Urho3DPlus/libUrho3DPlus.a(ProjectManager.cpp.o): In function `Urho3D::ProjectManager::CloseDirSelector()':
ProjectManager.cpp:(.text+0x2550): multiple definition of `Urho3D::ProjectManager::CloseDirSelector()'
CMakeFiles/IDE.dir/Source/IDE/ProjectManager.cpp.o:ProjectManager.cpp:(.text+0x1ad0): first defined here
../Urho3DPlus/libUrho3DPlus.a(ProjectManager.cpp.o): In function `Urho3D::ProjectManager::GetRootDir()':
ProjectManager.cpp:(.text+0x2570): multiple definition of `Urho3D::ProjectManager::GetRootDir()'
CMakeFiles/IDE.dir/Source/IDE/ProjectManager.cpp.o:ProjectManager.cpp:(.text+0x1af0): first defined here
../Urho3DPlus/libUrho3DPlus.a(ProjectManager.cpp.o): In function `Urho3D::ProjectManager::GetProject()':
ProjectManager.cpp:(.text+0x2580): multiple definition of `Urho3D::ProjectManager::GetProject()'
CMakeFiles/IDE.dir/Source/IDE/ProjectManager.cpp.o:ProjectManager.cpp:(.text+0x1b00): first defined here
../Urho3DPlus/libUrho3DPlus.a(ProjectManager.cpp.o): In function `Urho3D::ProjectSettings::ProjectSettings(Urho3D::Context*)':
ProjectManager.cpp:(.text+0x2590): multiple definition of `Urho3D::ProjectSettings::ProjectSettings(Urho3D::Context*)'
CMakeFiles/IDE.dir/Source/IDE/ProjectManager.cpp.o:ProjectManager.cpp:(.text+0x1b10): first defined here
../Urho3DPlus/libUrho3DPlus.a(ProjectManager.cpp.o): In function `Urho3D::ProjectManager::HandleNewProject(Urho3D::StringHash, Urho3D::HashMap<Urho3D::StringHash, Urho3D::Variant>&)':
ProjectManager.cpp:(.text+0x2870): multiple definition of `Urho3D::ProjectManager::HandleNewProject(Urho3D::StringHash, Urho3D::HashMap<Urho3D::StringHash, Urho3D::Variant>&)'
CMakeFiles/IDE.dir/Source/IDE/ProjectManager.cpp.o:ProjectManager.cpp:(.text+0x1df0): first defined here
../Urho3DPlus/libUrho3DPlus.a(ProjectManager.cpp.o): In function `Urho3D::ProjectSettings::ProjectSettings(Urho3D::Context*)':
ProjectManager.cpp:(.text+0x2590): multiple definition of `Urho3D::ProjectSettings::ProjectSettings(Urho3D::Context*)'
CMakeFiles/IDE.dir/Source/IDE/ProjectManager.cpp.o:ProjectManager.cpp:(.text+0x1b10): first defined here
../Urho3DPlus/libUrho3DPlus.a(ProjectManager.cpp.o): In function `Urho3D::ProjectSettings::CopyAttr(Urho3D::ProjectSettings*)':
ProjectManager.cpp:(.text+0x3dd0): multiple definition of `Urho3D::ProjectSettings::CopyAttr(Urho3D::ProjectSettings*)'
CMakeFiles/IDE.dir/Source/IDE/ProjectManager.cpp.o:ProjectManager.cpp:(.text+0x3350): first defined here
../Urho3DPlus/libUrho3DPlus.a(ProjectManager.cpp.o): In function `Urho3D::ProjectManager::RegisterObject(Urho3D::Context*)':
ProjectManager.cpp:(.text+0x4140): multiple definition of `Urho3D::ProjectManager::RegisterObject(Urho3D::Context*)'
CMakeFiles/IDE.dir/Source/IDE/ProjectManager.cpp.o:ProjectManager.cpp:(.text+0x3d50): first defined here
../Urho3DPlus/libUrho3DPlus.a(ProjectManager.cpp.o): In function `Urho3D::ProjectSettings::RegisterObject(Urho3D::Context*)':
ProjectManager.cpp:(.text+0x4150): multiple definition of `Urho3D::ProjectSettings::RegisterObject(Urho3D::Context*)'
CMakeFiles/IDE.dir/Source/IDE/ProjectManager.cpp.o:ProjectManager.cpp:(.text+0x3d60): first defined here
../Urho3DPlus/libUrho3DPlus.a(ProjectManager.cpp.o): In function `Urho3D::ProjectManager::ProjectManager(Urho3D::Context*)':
ProjectManager.cpp:(.text+0x5390): multiple definition of `Urho3D::ProjectManager::ProjectManager(Urho3D::Context*)'
CMakeFiles/IDE.dir/Source/IDE/ProjectManager.cpp.o:ProjectManager.cpp:(.text+0x4fa0): first defined here
../Urho3DPlus/libUrho3DPlus.a(ProjectManager.cpp.o): In function `Urho3D::ProjectManager::ProjectManager(Urho3D::Context*)':
ProjectManager.cpp:(.text+0x5390): multiple definition of `Urho3D::ProjectManager::ProjectManager(Urho3D::Context*)'
CMakeFiles/IDE.dir/Source/IDE/ProjectManager.cpp.o:ProjectManager.cpp:(.text+0x4fa0): first defined here
../Urho3DPlus/libUrho3DPlus.a(ProjectManager.cpp.o): In function `Urho3D::ProjectManager::~ProjectManager()':
ProjectManager.cpp:(.text+0x5600): multiple definition of `Urho3D::ProjectManager::~ProjectManager()'
CMakeFiles/IDE.dir/Source/IDE/ProjectManager.cpp.o:ProjectManager.cpp:(.text+0x5270): first defined here
../Urho3DPlus/libUrho3DPlus.a(ProjectManager.cpp.o): In function `Urho3D::ProjectManager::~ProjectManager()':
ProjectManager.cpp:(.text+0x57e0): multiple definition of `Urho3D::ProjectManager::~ProjectManager()'
CMakeFiles/IDE.dir/Source/IDE/ProjectManager.cpp.o:ProjectManager.cpp:(.text+0x5440): first defined here
../Urho3DPlus/libUrho3DPlus.a(ProjectManager.cpp.o): In function `Urho3D::ProjectManager::~ProjectManager()':
ProjectManager.cpp:(.text+0x5600): multiple definition of `Urho3D::ProjectManager::~ProjectManager()'
CMakeFiles/IDE.dir/Source/IDE/ProjectManager.cpp.o:ProjectManager.cpp:(.text+0x5270): first defined here
../Urho3DPlus/libUrho3DPlus.a(ProjectManager.cpp.o): In function `Urho3D::ProjectManager::UpdateProjects(Urho3D::String const&)':
ProjectManager.cpp:(.text+0x5800): multiple definition of `Urho3D::ProjectManager::UpdateProjects(Urho3D::String const&)'
CMakeFiles/IDE.dir/Source/IDE/ProjectManager.cpp.o:ProjectManager.cpp:(.text+0x5460): first defined here
../Urho3DPlus/libUrho3DPlus.a(ProjectManager.cpp.o): In function `Urho3D::ProjectManager::CreateWelcomeScreen()':
ProjectManager.cpp:(.text+0x7450): multiple definition of `Urho3D::ProjectManager::CreateWelcomeScreen()'
CMakeFiles/IDE.dir/Source/IDE/ProjectManager.cpp.o:ProjectManager.cpp:(.text+0x70b0): first defined here
../Urho3DPlus/libUrho3DPlus.a(ProjectManager.cpp.o): In function `Urho3D::ProjectManager::HandleRescanProjects(Urho3D::StringHash, Urho3D::HashMap<Urho3D::StringHash, Urho3D::Variant>&)':
ProjectManager.cpp:(.text+0x85e0): multiple definition of `Urho3D::ProjectManager::HandleRescanProjects(Urho3D::StringHash, Urho3D::HashMap<Urho3D::StringHash, Urho3D::Variant>&)'
CMakeFiles/IDE.dir/Source/IDE/ProjectManager.cpp.o:ProjectManager.cpp:(.text+0x8250): first defined here
../Urho3DPlus/libUrho3DPlus.a(ProjectManager.cpp.o): In function `Urho3D::ProjectManager::ShowWelcomeScreen(bool)':
ProjectManager.cpp:(.text+0x8570): multiple definition of `Urho3D::ProjectManager::ShowWelcomeScreen(bool)'
CMakeFiles/IDE.dir/Source/IDE/ProjectManager.cpp.o:ProjectManager.cpp:(.text+0x81e0): first defined here
../Urho3DPlus/libUrho3DPlus.a(ProjectManager.cpp.o): In function `Urho3D::ProjectSettings::~ProjectSettings()':
ProjectManager.cpp:(.text+0x50): multiple definition of `Urho3D::ProjectSettings::~ProjectSettings()'
CMakeFiles/IDE.dir/Source/IDE/ProjectManager.cpp.o:ProjectManager.cpp:(.text+0x50): first defined here
collect2: ld returned 1 exit status
make[2]: *** [bin/IDE] Error 1
make[1]: *** [IDE/CMakeFiles/IDE.dir/all] Error 2
make: *** [all] Error 2
vivienne@vivienne-System-Product-Name:/media/home2/vivienne/Urho3DIDE/Build$[/code]

-------------------------

GoogleBot42 | 2017-01-02 01:04:26 UTC | #50

What platforms are you trying to target?  As far as I know all of the platforms that Urho3D officially compiles on so far all support c++11 features (and have for several years at least).  I am not entirely sure why you are putting so much effort into this...  :neutral_face:

-------------------------

vivienneanthony | 2017-01-02 01:04:26 UTC | #51

[quote="GoogleBot42"]What platforms are you trying to target?  As far as I know all of the platforms that Urho3D officially compiles on so far all support c++11 features (and have for several years at least).  I am not entirely sure why you are putting so much effort into this...  :neutral_face:[/quote]

My platform is Ubuntu 12.04. Eventually the game wil target Linux, Windows, and Android maybe Mac. So, I need cross usage between all platforms including compiling  and coding need be.

Besides, I am not the only person with compiling issues. So getting it to build across platforms becames necessary.

-------------------------

vivienneanthony | 2017-01-02 01:04:26 UTC | #52

[quote="GoogleBot42"]What platforms are you trying to target?  As far as I know all of the platforms that Urho3D officially compiles on so far all support c++11 features (and have for several years at least).  I am not entirely sure why you are putting so much effort into this...  :neutral_face:[/quote]

My platform is Ubuntu 12.04. Eventually the game wil target Linux, Windows, and Android maybe Mac. So, I need cross usage between all platforms including compiling  and coding need be.

Besides, I am not the only person with compiling issues. So getting it to build across platforms becames necessary.

-------------------------

GoogleBot42 | 2017-01-02 01:04:26 UTC | #53

[quote="vivienneanthony"]
My platform is Ubuntu 12.04. Eventually the game wil target Linux, Windows, and Android maybe Mac. So, I need cross usage between all platforms including compiling and coding need be.

Besides, I am not the only person with compiling issues. So getting it to build across platforms becames necessary.[/quote]

But if this does compile on slightly newer compilers then this can be compiled for all those platforms... Working to support an older compiler is not necessarily a good thing because bugs and speed fixes are made during that time.  Also the newer features are there not to be a problem but they have been added to make coding easier.  That might be why compilers were really quick to pick up c++11 support.

Although I run Arch Linux so I run the latest version of most things...  so my opinion is heavily in one direction.   :slight_smile:

EDIT: I just finished setting the urho3d documentation so I can view it offline at "localhost" and update it easily via git + jekyll. Yay for offline.   :smiley:

-------------------------

vivienneanthony | 2017-01-02 01:04:26 UTC | #54

[quote="GoogleBot42"][quote="vivienneanthony"]
My platform is Ubuntu 12.04. Eventually the game wil target Linux, Windows, and Android maybe Mac. So, I need cross usage between all platforms including compiling and coding need be.

Besides, I am not the only person with compiling issues. So getting it to build across platforms becames necessary.[/quote]

But if this does compile on slightly newer compilers then this can be compiled for all those platforms... Working to support an older compiler is not necessarily a good thing because bugs and speed fixes are made during that time.  Also the newer features are there not to be a problem but they have been added to make coding easier.  That might be why compilers were really quick to pick up c++11 support.

Although I run Arch Linux so I run the latest version of most things...  so my opinion is heavily in one direction.   :slight_smile:

EDIT: I just finished setting the urho3d documentation so I can view it offline at "localhost" and update it easily via git + jekyll. Yay for offline.   :smiley:[/quote]

That's cool. Considering the only probablem is the linker because of the muiltiple definition. I think it's something that can be reserved. So, C+11 or not. It would work.

-------------------------

GoogleBot42 | 2017-01-02 01:04:26 UTC | #55

[quote="vivienneanthony"]That's cool. Considering the only probablem is the linker because of the muiltiple definition. I think it's something that can be reserved. So, C+11 or not. It would work.[/quote]

Hmmm weird hasn't this been compiled successfully before?

-------------------------

vivienneanthony | 2017-01-02 01:04:26 UTC | #56

[quote="GoogleBot42"][quote="vivienneanthony"]That's cool. Considering the only probablem is the linker because of the muiltiple definition. I think it's something that can be reserved. So, C+11 or not. It would work.[/quote]

Hmmm weird hasn't this been compiled successfully before?[/quote]

In a Microsoft Visual/Windows platform, but not Linux.

-------------------------

GoogleBot42 | 2017-01-02 01:04:26 UTC | #57

The IDE compiles in gcc but not VS because of multiple declaration issues... that is strange.  What version of VS?

-------------------------

vivienneanthony | 2017-01-02 01:09:23 UTC | #58

[quote="GoogleBot42"]The IDE compiles in gcc but not VS because of multiple declaration issues... that is strange.  What version of VS?[/quote]

I got the code to compile. I stripped away most of the extra's and added it to my engine. It seems to work for either platform. I'm just testing it. Trying to overload it building scenes.

-------------------------

