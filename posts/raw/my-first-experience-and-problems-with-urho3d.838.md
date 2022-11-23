gawag | 2017-01-02 01:03:20 UTC | #1

Hi,
I'm new to Urho3D, just build it and started the samples:

[img]http://s17.postimg.org/7tbyc5qvz/Urho3_D_sample2.png[/img]

I supposed it shouldn't look like that...
But after writting half a post in your support section, I had an Idea:
I'm normally developing (normal applications with Qt, no 3D or games) inside a Windows VMWare-VM inside a Host-Windows. And I never had any kind of game inside the VM. I wasn't sure if it can do 3D like games properly. So I copied the Bin folder to the host and and the samples suddenly worked!

[img]http://s4.postimg.org/vdic73ov1/Urho3_D_sample3_DUDE.png[/img]

There should be some warnings if Urho3D can't display 3D correctly or load the materials or whatever didn't work in my VM. I nearly abondoned Urho3D.

I'm using Windows, 32bit, OpenGL, MinGW 4.9.1, CMake-GUI and CodeBlocks. I wrote all the steps down I had to do to make Urho3D work. There seems to be a Wiki, but no Index? Is there a tutorial or HowTo section somewhere?
Parts of the documentation seems to be older and mention stuff like Visual Studio 2009...
I could write a short guide how I build Urho3D 1.32. It was far less painfull as trying to build Ogre...
Ah, I couldn't build you documentation with the CMake URHO3D_DOCS flag. CodeBlocks tried to build some .dot files, which I think are image files. After deactivating that flag, make was able to finish everything.

My Background:
The last time I did something with game development is years ago. I used Ogre back then, before that CrystalSpace and before that tried Irrlicht with no success. CrystalSpace worked at first but had broken shadows and physics and seems quite inactive since then. So I searched again and found Ogre and was happy for quite a while. But they dropped their MinGW-Binary-Release sometime and it's hard/impossible to build manually. So Ogre died a bit for me. The last stable is still from 2012. As I used that, it just came out. They seem to be working on Ogre 2.0/2.1, maybe they will have an MinGW-Binary-Release again and better support in general. But for now: nah...
So I searched and compared a lot of other 3d/game engines and the two most promising ones are Urho3D and Delta3D. Urho3D seemes to have better support for Blender so I started with that.
I'm working as a C++ software developer in a small company. We are doing image editing software for Windows & Mac with Qt. We are still not selling that much (but are improving) and can't currently support any free software project with money or man power (though I would like that). Would be great if that would change. There are so many companies profitting from free software without giving anything back, f***g a***s... :wink:
I have still so many ideas regarding games and it was so fun doing something in that field (though image editing software is also not bad), and after years of just thinking, am trying to do something again. I'm always trying to use free software, my tools were always: Blender, Gimp and CodeBlocks. Though I also like QtCreator (Codeblocks has always had some flaws, QtCreator has now a bit less).

My next steps will be to move my Urho3D development to my host and try to compile own stuff. I think I'll start with your water sample because it has terrain and water. Hope that terrain is editable and supports texture splatting.
Next I'll try to make models with Blender and export them. There are some forum posts regarding Blender export but no (video) tutorial/howto? You could need that. I also hated the lack or organisation of the Ogre tutorials/howtos. Everyone in the forum seems always happily using something, but everone needs to spend hours trying to get something to work, because no one of the "inner circle" shares his secrets by making a small tutorial...
I wasted like 2 hourse of my 3 hours of experimenting with Urho3D with searching and experimenting with CMake and Codeblocks custom Makefiles. A tutorial would have saved that.

It bothers me that free software engines are so far behind commercial engines like Unreal-Engine, CryEngine or Unity (though that one is not comparable). Free software engines can be slower / less optimized and not have all the features because of lack of man power. But they should have enough potential for lighter projects, small teams and hobbyists. Not just because of lack of money, but also because of the free software ideal. They are all lacking good / up-to-date tutorials, material/model collections, better organization and transparency. There are also dozens of concurrenting engines, most abandoned though or focusing a specific genres/niches.

This became a bit like a super long blog post and took me over an hour... overthinking again...
Comments welcome to all the stuff I mentioned.
I didn't read that many other forum posts, so some things may already have been mentioned somewhere.


greetings from germany

> inb4 no replies because Urho3D abondoned too

-------------------------

hdunderscore | 2017-01-02 01:03:20 UTC | #2

Hi and welcome to the forums :smiley:

I guess the first thing I'll mention is that we do have documentation that is updated as new features are added and changed:
[urho3d.github.io/documentation/1.32/index.html](http://urho3d.github.io/documentation/1.32/index.html)

Important to note though, that that link is for Urho 1.32 so if you are building from github, you'll want to change the dropdown toggle to HEAD, eg:
[urho3d.github.io/documentation/HEAD/index.html](http://urho3d.github.io/documentation/HEAD/index.html)
[urho3d.github.io/documentation/HEAD/pages.html](http://urho3d.github.io/documentation/HEAD/pages.html)
[urho3d.github.io/documentation/H ... tated.html](http://urho3d.github.io/documentation/HEAD/annotated.html)

You'll see there's build instructions, a few overviews and after that you'll need to dive into class documentation, samples and perhaps look through the Code Exchange subforum for learning resources. You're right though, we don't have Unity style tutorials yet !

The build process for Urho can be quite straight forward, eg I personally use cmake gui so it's a very standard process. Otherwise there are batch files you can run, although perhaps the recent change that requires a parameter can be confusing without reading the documentation, eg:
[quote]cmake_codeblocks.bat BuildCB[/quote]
Where BuildCB is any directory name you want to find your build files in.

As far as running from within a VM, I'm not sure that's typical but I could be mistaken. If you press F1 while running from within the VM (or if you find the log files you might find more detail), do you happen to see any warnings/error messages?

The secret sauce you'll want to know, since you ask so nicely, is that if you run Editor.bat after you've build the engine, you will get a visual scene editor :smiley: It will help you import models, textures etc (although there are other ways too, including using the blender-urho exporter) The scene editor is also a good way to figure out how the Urho components work.

Hope that helps a little

-------------------------

weitjong | 2017-01-02 01:03:20 UTC | #4

I think I will just address on the VM issue that you have. We have already documented the minimum system requirement to run Urho3D here ([urho3d.github.io/documentation/1 ... lding.html](http://urho3d.github.io/documentation/1.32/_building.html)). Note that Urho3D needs a "decent" OpenGL/ES driver or Direct3D9 driver to render correctly. On a typically VM, I think most only uses software-rendering graphic driver without hardware acceleration. So, it is not surprising when one would get a crappy rendering and/or performance result in VM. Having said that, I use Oracle VirtualBox here on my Linux host and I have a pretty decent rendering result in my Win7 VM and MacOSX VMs. But of course, for performance wise they are nothing compared to the real baremetal.

-------------------------

gawag | 2017-01-02 01:03:20 UTC | #5

Wow that were fast answers.

The cmake .bat script for mingw doesn't work out of the box:
[code]
CMake Error: CMake was unable to find a build program corresponding to "MinGW Makefiles".  CMAKE_MAKE_PROGRAM is not set.  You probably need to select a different build tool.
CMake Error: CMake was unable to find a build program corresponding to "MinGW Makefiles".  CMAKE_MAKE_PROGRAM is not set.  You probably need to select a different build tool.
-- Configuring incomplete, errors occurred!
CMake Error: Error required internal CMake variable not set, cmake may be not be built correctly.
Missing variable is:
CMAKE_C_COMPILER_ENV_VAR
CMake Error: Error required internal CMake variable not set, cmake may be not be built correctly.
Missing variable is:
CMAKE_C_COMPILER
CMake Error: Could not find cmake module file: C:/Urho3D/Urho3D/Build/CMakeFiles/2.8.12.1/CMakeCCompiler.cmake
CMake Error: Error required internal CMake variable not set, cmake may be not be built correctly.
Missing variable is:
CMAKE_CXX_COMPILER_ENV_VAR
CMake Error: Error required internal CMake variable not set, cmake may be not be built correctly.
Missing variable is:
CMAKE_CXX_COMPILER
CMake Error: Could not find cmake module file: C:/Urho3D/Urho3D/Build/CMakeFiles/2.8.12.1/CMakeCXXCompiler.cmake
CMake Error: CMAKE_C_COMPILER not set, after EnableLanguage
CMake Error: CMAKE_CXX_COMPILER not set, after EnableLanguage
[/code]
Same output as I had in CMake-GUI. But I was able to set all variables with the GUI. This CMake stuff is always a bit messy with settings variables and so.
Maybe it expects certain conditions on the system?

There are step by step tutorials on how to install every piece you need for Ogre with a lot of images (though outdated). That makes it very easy for inexperienced developers which may be just coming from beginner C++ tutorials. I meant something like that. These CMake defines may be hard for someone who has never used CMake before.

[quote]You'll see there's build instructions, a few overviews and after that you'll need to dive into class documentation, samples and perhaps look through the Code Exchange subforum for learning resources. You're right though, we don't have Unity style tutorials yet ![/quote]
I don't really know this Unity stuff and have never looked into their tutorials. I think Unity is scripted with C#, but as a C++ developer, that's not what I want. Unity seems very popular for beginners, but I think, because of this scripted stuff, that it's not suited for the heavy application that I want to do (or have at least the possibility to do).

There is some documentation but it's far less than Ogre with all their different sections:
[ogre3d.org/tikiwiki/tiki-ind ... =Tutorials](http://www.ogre3d.org/tikiwiki/tiki-index.php?page=Tutorials)
[ogre3d.org/tikiwiki/tiki-ind ... reArticles](http://www.ogre3d.org/tikiwiki/tiki-index.php?page=OgreArticles)
[ogre3d.org/tikiwiki/tiki-ind ... e=Snippets](http://www.ogre3d.org/tikiwiki/tiki-index.php?page=Snippets)
But as already mentioned, Ogre is also lacking (official) support and tutorial as for example when using Blender. There are working exporters (and non-working) and forum posts, but everything very spread and the exporters I used were difficult to use because you needed to make your model in certain ways. And this wasn't really explained (the last time I looked).
Are there tutorials on how to make materials/shaders for Urho?
Ogre had some for it's system, but 4/5 didn't work at all...

[quote]As far as running from within a VM, I'm not sure that's typical but I could be mistaken. If you press F1 while running from within the VM (or if you find the log files you might find more detail), do you happen to see any warnings/error messages?[/quote]
F1 shows the mouse cursor. But there is no GUI at all. F2 has also no effect besides showing the mouse cursor.
Works both fine outside the VM. May be a driver issue which is irrelevant for normal users.

@weitjong:
Yeah that may be the issue. Though it's not a performance, but more a not-working-at-all issue. I think Ogre had error messages for that (though no idea if they would work for this case and if that would be possible for Urho). 

[quote]To build the documentation requires Doxygen and Graphviz. (or as hd has linked to, you can browse it online)[/quote]
The Makefile tried to compile the .dot files as if they were source files (like .cpp files). Didn't mention doxygen or graphviz anywhere. Normally a configure script, or in this case CMake, should check for such dependencies. Doxygen is installed btw.. You could simply mention it in the documentation if it doesn't work currently.
That's one of the reasons I'm normally developing insides VMs: you can better control what you install (compared to your host which may be stuffed with a lot of application already). So one can use a fresh VM to check what's needed to build or use a certain piece of software.

News since my first post:
Had a deeper look into the samples. Same are quite good locking. Others should be updated.
Like this Ninja Snowball example: The Ninja is so low-poly. And why has it a sword?
The model should be made more detailed (Blender->Subdivision Surface), the sword removed (or melee action added) and the "snowballs" are bouncing like normal balls. Though the physics itself is good. The Snow theme could be replaced by grass and normal balls, that would make it more realistic (because snowballs don't really bounce).
The GUI could also be nicer (the health bar). There seem to be GUI feature in Urho3D but the samples aren't showing a real example besides one with a checkbox and a button. The sample with movable buttons is also not really working for me, there is no cursor.
(These are all not really complains but improvement suggestions. I know it's hard to be productive, especially if you aren't paid.)

I started my own test app based on the water example and it's compiling now. But it's crashing at surface->SetViewport(0,rttViewport); (line 223) because RenderSurface* surface=renderTexture->GetRenderSurface(); (two lines above) returned a 0 to 'surface'. Commented that out for now and the water reflection looks weird. Maybe I'll start a new thread in the support section if I can't figure that out or find a solution in the forum. The documentation doesn't mention why GetRenderSurface could return a 0.

I'm impressed what Urho3D can do besides just displaying graphics. Ogre is only a graphics engine and I had to add physics with Bullet (and sound) myself. Urho3D has both already integrated and looks great, solid and fast in the examples. There is also a path finding sample. The samples show a lot of potential to make all kind of games with the stuff already in Urho.
(Btw: the camera in the physics example with the box pyramid should be moved closer to the pyramid. I started the sample and shot a box without moving and it landed like 2m in front of the pyramid which was kinda funny. Even small things like that make Urho3D look unpolished.)
I see Urho3D more as a concurrent to CrystalSpace (also a complete game engine) and not just Ogre (only graphics engine). Urho3D has a lot of potential to be the number one free software (complete) game engine. CrystalSpace seems so abandoned and seems to be only developed by one guy (or a super slow team). I also remember CrystalSpace having glitchy shadows and physics. Urho3D could take it's place.

How many people are working on Urho?
There is room for improvements, most things I found for now are relatively minor though.
I can't even find your wiki anymore. Though it had no index (content overview) at all and just a search box. Wikis are often much better suited to centralize informations compared to forums. It there none are did I miss that? Is there community created content possible besides in the forum?

I really would love an easy to use 3D-Engine for beginners which also has the potential to make big games. Currently I don't know any that is there yet, sadly.

-------------------------

cadaver | 2017-01-02 01:03:20 UTC | #6

RenderSurface would be 0 if the texture failed to create or you did not create it in rendertarget mode.

Urho has 8 core developers with push repository access, and many more minor contributors.

You will (IMO) get the most out of Urho when you take it as a toolkit and base for your own projects but don't expect that it has everything ready, and are prepared to fill the blanks yourself where necessary. Otherwise you may be setting yourself up for a disappointment. I think we can now extrapolate quite nicely into the future and we can see that we have many devs doing great work, and each year Urho gets more features and (hopefully) becomes friendlier to use, yet game engines are huge undertakings and becoming the "best" (if we for example would like Urho to be a true free alternative to Unity, with comparable functionality) would require a disproportionate leap in the amount of work contributed by everyone, which I don't believe to be realistic. I believe we can and should be honest about this, even if it's "bad PR" in a sense. But of course I'd be happy to be proven wrong :slight_smile:

EDIT: as for the nitpicks of the examples, I personally can't see them as major issues but if someone wants to work on these, feel free. I guess having lived with them long one sort of becomes blind to them. The Ninja snow theme comes from using an Ogre example mesh directly and snow being easier to texture than grass; this was a 100% coder art -using project I originally did at university with Ogre, which was later ported as an Urho example.

-------------------------

gwald | 2017-01-02 01:03:20 UTC | #7

[quote="gawag"]
I really would love an easy to use 3D-Engine for beginners which also has the potential to make big games. Currently I don't know any that is there yet, sadly.[/quote]
 :smiley:
Mutually exclusive  :unamused:

-------------------------

gawag | 2017-01-02 01:03:21 UTC | #8

[quote]I think we can now extrapolate quite nicely into the future and we can see that we have many devs doing great work, and each year Urho gets more features and (hopefully) becomes friendlier to use, yet game engines are huge undertakings and becoming the "best" (if we for example would like Urho to be a true free alternative to Unity, with comparable functionality) would require a disproportionate leap in the amount of work contributed by everyone, which I don't believe to be realistic. I believe we can and should be honest about this, even if it's "bad PR" in a sense. But of course I'd be happy to be proven wrong :slight_smile:[/quote]
I never worked with any commercial engine and don't know their features in detail. I always compared to other free engines, mainly the big/prominent ones Ogre, CrystalSpace and Irrlicht (though I don't get Irrlichts popularity).
The commercial ones seem to have mainly more GUI tools like were one can click together his animations and some game logic. I never liked WYSIWYG stuff (like GUI editors), made many bad experiences with them and prefer doing such things by code (more dynamic). It may not be a good idea to try to copy every features (even if there would be much more man power).
I always see Unity as a toy or learning engine and not as a professional high-end AAA engine like Unreal ([unrealengine.com/unreal-engine-4](https://www.unrealengine.com/unreal-engine-4)), but maybe I don't know enough about Unity.

One of the things all free engines seem to fail at, are directly and easily usable materials and effects. Is there some kind of gallery for those for Urho? Like texture with normal mapping or chrome effects or whatever? Ogre tried something like that but that didn't really work the last time I checked. I never really got into those shader thingies (partly because the Ogre ones worked so badly).

News:
Exported simple test mesh from Blender with your exporter and that worked perfectly at the first try. Much better as those fishy Ogre exporters  :mrgreen: .
Though it tried to use a material technique that wasn't were and I copied a name from another material. And the paths to the textures weren't interpreted as relative. Can the names be relative?
Added my test model to my app (based on water example) and bound a light to the camera node. Yay working shadows! Noticed that the camera node is outside the scene and couldn't bind the light directly to it? That's a bit weird and works with Ogre.
So nice progress being made (though I already know Ogre and Urho is similiar). Seems relatively easy to use for now.
Haven't tested exporting an animated mesh yet, that really sucked with the Ogre exporter.

[quote]Mutually exclusive[/quote]
You mean easy to use and usable for big games isn't possible?
I don't think so. With big games I mean hardware heavy games with a lot of actors and physics stuff. This physics stress test looked already good and seems to beat the Half Life 2 engine by far (try that many boxes in Garrys Mod -> NOPE).
Easy to use doesn't mean Unitys scripting stuff. CrystalSpace was terrible to use. Ogre and Urho are much better with their hierarchical node system. Until now Urho doesn't seem to be hard. Though materials/shaders may be an issue. Hence my question for some kind of gallery with usage explanation.

-------------------------

cadaver | 2017-01-02 01:03:21 UTC | #9

Yes, there's a small gotcha related to how most of the examples create the camera. It's valid to have the camera to be outside scene, this is intended to ease load / save situations, because load destroys all objects, after which you have to re-assign the camera & viewport, if it was part of the scene. Having camera outside, this problem is averted, but the flipside is that you cannot make any components attached to the camera or its children render, as they cannot find your scene's octree.

Though this is a bit offtopic, if you see Unity as a toy you're (IMO) underestimating it. It has some problems with the Mono scripting runtime (garbage collection gotcha's) and its rendering is not fully current gen AAA-level, on the other hand it is able to scale down better than UE4 which is still being worked on to perform well on eg. mobile devices. Otherwise both engines are complex, professional beasts.

As for the lack of usable assets in open source engines, I would say that this is due to them being mostly worked on by coders, and development time being focused on the framework itself (ie. creating means for users to create their own content, while forgetting to actually demonstrate all those means) This of course varies with the devs' personal interests, so if someone is interested in eg. modern shading models they will likely work on those. In Urho unfortunately I think none of us in the active core team are very knowledgeable on cutting-edge rendering, or have time to learn.

For Urho there are some third-party contributions, for example see Hevedy's Purpleprint kit (which has its own thread on this same subforum).

-------------------------

gawag | 2017-01-02 01:03:21 UTC | #10

[quote]Though this is a bit offtopic, if you see Unity as a toy you're (IMO) underestimating it. It has some problems with the Mono scripting runtime (garbage collection gotcha's) and its rendering is not fully current gen AAA-level, on the other hand it is able to scale down better than UE4 which is still being worked on to perform well on eg. mobile devices. Otherwise both engines are complex, professional beasts.[/quote]

Garbage collection makes it a toy like Java  :smiley: 
Top games want to have every possible optimization they can get. That's why C++ has always been so strong in that field.
Languages like C# have per design less possibilities to optimize, which will make it mostly unusable for AAA-Games.
Unity may be good enough for less CPU intense games though, and beginners.
It's professional and from that point of view not really a toy, but per design more limited compared to UE4, CryEngine and similiar.

[quote]In Urho unfortunately I think none of us in the active core team are very knowledgeable on cutting-edge rendering, or have time to learn.[/quote]
Yeah that's also my problem...
Though normal maps for example aren't really "cutting-edge" anymore. Maybe we can make at least a gallery of "simple" effects. I made a working normal map (bump map) material/shader for Ogre once.

Just found a topic talking about a wiki: [topic778.html](http://discourse.urho3d.io/t/urho-wiki/760/1)
There was once a wiki but was closed due to inactivity? Dang.
Urho3D seems underrated. (And Irrlicht overrated.)

-------------------------

