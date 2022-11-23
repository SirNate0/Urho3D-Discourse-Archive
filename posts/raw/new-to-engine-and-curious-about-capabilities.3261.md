runi | 2017-06-16 13:15:13 UTC | #1

I've been messing around with the example projects and have made a few modifications that I would likely want to include eventually. The first one was a minimap so I was fortunate to have an example of how to add a secondary viewport, and it didn't take very long to transform it into a topdown view from a rearcam.

But one thing striked me as odd, even just going through the examples and docs idly to get a feel for them left me still wondering how to sculpt it into a game. GUI's are eluding me still, but I can deal with that for now. 

I assume doors, menus, lifts, ladders, and all of that will become apparent to me the more I comb through examples and the docs.

But while I wait for that I just want to ask, **what have you been able to create so far?** 

You don't have to share code or anything, I'm just curious what people have been able to muster up since you're probably learning from the same information

-------------------------

ppsychrite | 2017-06-16 13:33:02 UTC | #2

The best thing I've made up to date is a cube (similar to the shape from the dynamic geometry example) that is able have a different material on each side. It was easier than I thought it would be. :grin:

-------------------------

Eugene | 2017-06-16 13:38:46 UTC | #3

[quote="runi, post:1, topic:3261"]
what have you been able to create so far?
[/quote]

E.g. this
https://discourse.urho3d.io/t/vegetation-example/2894/4?u=eugene

-------------------------

Victor | 2017-06-16 15:11:24 UTC | #4

Currently, I've been working on tweaking terrain mostly. Also doing some foliage stuff along with using the ProcSky component

<img src='//cdck-file-uploads-global.s3.dualstack.us-west-2.amazonaws.com/standard17/uploads/urho3d/original/1X/a99c86d16b085fe5d1e83a47881c02133dac7eff.jpg'>

-------------------------

Modanung | 2017-06-16 19:07:16 UTC | #5

Everything here uses Urho3D:
https://github.com/LucKeyProductions/

If you're looking for a simple example game check out [NinjaSnowWar](https://github.com/urho3d/Urho3D/tree/master/bin/Data/Scripts/NinjaSnowWar) (AngelScript) or [FlappyUrho](https://discourse.urho3d.io/t/flappy-urho/1962) (C++).

And welcome to the forums! :slight_smile:

-------------------------

Alex-Doc | 2017-06-17 06:14:16 UTC | #6

It's been about a month now since I've started my new game in Urho3D, the things that scared me the most were:
- UI
- Animations

Right now I have a scenario with rim shader (if anyone interested, let me know) 

An animated character with smooth camera, controls and settings manager (XML settings), scene manager, localization and something else.

Aftermath, both UI and animations revealed easier and straightforward than I've initially thought.
I have tried lots of engines and Urho3D is actually the first one who lets me focus on the game instead of fixing the engine.

If you are used to C++, Urho3D is gold. The sources are well written, very easy to read and figure out.

-------------------------

runi | 2017-06-22 12:26:31 UTC | #7

Thanks for the replies guys, it's interesting taking a dive into urho after skimming through those projects. I've been making some additions to the ninja snow war demo and that's going decently. I wanted to add score multipliers, limited ammo, 'snow storms' that sweep into an area for you to replenish your snow, and a bunch of stuff like that to try and make it more playable. I have quite a few ideas for it, so it might actually be fun to play in not too long. But i'll have to wait until i can figure out how to add half of them to see if they're feasible. 

But as a first project from scratch; i think I'm going to try and figure out how to make the framework of a game i have in mind. Trouble is that i've only been able to modify ninjasnowwar stuff, but fabricating my own is a bit daunting. 

if I wanted to make a 3d game with a 3rd person camera and controls set on a hightmapped terrain, a gui overlay showing stats and a minimap (or i can do downfacing camera viewport, but i cant find how to make it low quality to save fps), and an interactable menu gui toggled on keypress. And the ability to set up a trigger zone around an object to trigger a dialog box, either on entry or on keypress while within. Those are the core things i would need, and i'm not even sure how i'd go about implementing half of them. 

This morning I was trying to figure out which parts I can gut from the example scripts, but im not sure what the bare minimum i need is. If you guys have any thoughts or relevant wiki pages that might lend some insight, i'd appreciate it. 

P.S. i hope doing things with the .as files isn't going to be too limiting

-------------------------

Alex-Doc | 2017-06-22 13:11:25 UTC | #8

I think that one of the best things in Urho3D's structure is that components can have their own logic, which gives extreme flexibility.

I'm making a first and third person openworld game, my approach is to create components which define the logic and initialization (see character example) and then I append them to my nodes.

Personally I'm using C++ to make the base classes while I use AngelScript to define the more specific objects and event handlers.
The examples contain pretty much every aspect you need to learn how Urho3D works. 
It also helped me a lot to keep the Urho3D manual at hand (I've read it all before even starting).

The actual game base structure really depends on how you are used to work and your game. 
To me having custom subsystems for managing scenes, settings and such worked great.

-------------------------

Modanung | 2017-06-22 15:50:22 UTC | #9

[quote="runi, post:7, topic:3261"]
been making some additions to the ninja snow war demo and that's going decently.
[/quote]

You might be interested in Rasterons work:

https://discourse.urho3d.io/t/ninja-snow-war-extended-version/304

I think it would be really cool if you could build bunkers/walls to duck behind, with capsule-cap snapping snow bricks. :slight_smile:

-------------------------

Modanung | 2017-06-22 16:04:22 UTC | #10

[quote="runi, post:7, topic:3261"]
And the ability to set up a trigger zone around an object to trigger a dialog box
[/quote]

The `Potion` (and with it the `GameObject`) in Ninja Snow War is an example of handling collision in AngleScript. Simply set the RigidBody to being a trigger if you don't want any physics interaction to take place. Since collision shapes are linked to rigidbodies on the same node you need to create a child node with a rigidbody that is set to both being a trigger as well as kinematic if you'd like separate physical and trigger interactions.

https://github.com/urho3d/Urho3D/blob/master/bin/Data/Scripts/NinjaSnowWar/Potion.as#L14-L30

-------------------------

runi | 2017-06-25 14:32:34 UTC | #11

As much as I feel like I should know what to do with that, I don't think I do but thanks for the link![quote="Modanung, post:9, topic:3261"]
I think it would be really cool if you could build bunkers/walls to duck behind, with capsule-cap snapping snow bricks. :slight_smile:
[/quote]

Yeah that would be cool. At the moment I'm working on adding ammo and snowstorm particle systems to replenish deposits of snow on the map. I think that's a neat way of removing the spamming. But I could make the right mouse button use a huge chunk of your snow to build a wall.

But for some reason the ammo display keep bugging out. It displays the right amount before I shoot, but afterwards it goes down for a split second and then jumps back up to my max ammo. But if I continue shooting, I'll run out and not be able to shoot anymore, so I know the number is actually going down. Quite confusing :/

[quote="Modanung, post:10, topic:3261"]
The Potion (and with it the GameObject) in Ninja Snow War is an example of handling collision in AngleScript
[/quote]

 A lot of how ninja snow war is structured feels really foreign to me so I can't grasp some of the examples within it. And the other samples have some things still tucked away in the samples.as, so i don't truly know what a skeleton-base game looks like. Don't suppose there's any empty husk examples?

-------------------------

Modanung | 2017-06-25 14:46:06 UTC | #12

[quote="runi, post:11, topic:3261"]
Don't suppose there's any empty husk examples?
[/quote]
Something like this?

https://discourse.urho3d.io/t/class-and-project-wizards-for-qtcreator/2076

-------------------------

runi | 2017-06-26 02:21:04 UTC | #13

That does look like what I'm asking about, thanks for the find! I've not messed with any QtCreator stuff before so I've just gotta figure out why it's not able to find Urho3D/Urho3d.h when I try and make all.

Thanks for the help so far!

-------------------------

Modanung | 2017-06-26 13:35:56 UTC | #14

[quote="runi, post:13, topic:3261"]
thanks for the find!
[/quote]

Yea, I too am glad I can still find my stuff. :stuck_out_tongue:
The wizard does have some "in-house" logic. You may want to fork and modify it. If you find something unusual or have an obvious improvement, a pull request would also be more than welcome.
[quote="runi, post:13, topic:3261"]
I've just gotta figure out why it's not able to find Urho3D/Urho3d.h when I try and make all.
[/quote]
I tend to create a symbolic link to the Urho3D folder within my project folders. Maybe it would be better to use environment variables. Copying the entire folder would also work.

What platform are you on?

-------------------------

runi | 2017-06-26 21:35:59 UTC | #15

I'm using linux mint at the moment, although I'm not too adept at the linux side of things.

e: I've got the "Urho3D" folder with all .h files and stuff sat directly next to generated stuff from that QtCreator wizard thing.

Do I need to declare/link the folder anywhere specific?

    /home/runi/Boonscape/luckey.h:22: error: "Urho3D/Urho3D.h": No such file or directory

-------------------------

Modanung | 2017-06-27 20:29:26 UTC | #16

[quote="runi, post:15, topic:3261"]
I'm using linux mint at the moment
[/quote]
Same here. Xfce flavoured.
[quote="runi, post:15, topic:3261"]
Do I need to declare/link the folder anywhere specific?
[/quote]
By default the following lines are added to the .pro file:
```
INCLUDEPATH += \
    ../ProjectName/Urho3D/include \
    ../ProjectName/Urho3D/include/Urho3D/ThirdParty \
```
With this setup, the build folder and the project folder need a shared parent folder. Simply `ln -s` to your Urho3D base folder from within the project folder, **_or_** - in your case - remove the `/%{ProjectName}` from `file.pro`.

-------------------------

runi | 2017-06-26 23:01:58 UTC | #17

[quote="Modanung, post:16, topic:3261"]
the .pro file
[/quote]
Where is that then?

I'm fairly sure I've got stuff set up wrong from the get-go. I started messing about with this on windows and since moved across to linux so my environment/toolchain or whatever is probably janky.

But through the QtCreator wizard I can get a folder with a template program in. Next to the folder is a build folder. When I go into the build folder to 'make' it, it complains that it cant find <Urho3D/Urho3D.h> and others, i get the same complaint hitting that green play button in QtCreator.

Going into the folder with the template program, I wanted to put `Urho3D-1.6-Linux-64bit-STATIC/usr/local/include*` into the folder with the template program so that right next to luckey.h there is Urho3D/Urho3D.h.

But I can't get that to work, so i figure that I might be a few miles off the mark lol

-------------------------

Modanung | 2017-06-27 07:14:40 UTC | #18

[quote="runi, post:17, topic:3261"]
Where is that then?
[/quote]
<img src="//cdck-file-uploads-global.s3.dualstack.us-west-2.amazonaws.com/standard17/uploads/urho3d/original/1X/72d9ec6b568a1f72de98c698d11f6d9f3636303d.png" width="690" height="178">

-------------------------

runi | 2017-06-27 11:41:10 UTC | #19

<img src="//cdck-file-uploads-global.s3.dualstack.us-west-2.amazonaws.com/standard17/uploads/urho3d/original/1X/1d51a310287fbb1d849335a111c020b90ac72197.png" width="311" height="233">

uh oh, i think i am miles off the mark then lol

-------------------------

Modanung | 2017-06-27 13:26:41 UTC | #20

Ah, you picked CMake for your build automation. I habitually _always_ use QMake, which uses this `.pro` file instead of a `CMakeLists.txt`. The `CMakeLists.txt` that is created is _not_ usable as is.
If you can make it work out-of-the-box with CMake by modifying the JS of the wizard, this would be much appreciated as a pull request. Another option would be switching to QMake.

-------------------------

runi | 2017-06-27 14:20:44 UTC | #21

Hey thanks, I've tried qmake and now the rest of your advice makes more sense. Sorry for being a pest, but I've run into the issue of missing EngineDefs.h and I can't find it on the github either.

-------------------------

Modanung | 2017-06-27 14:25:14 UTC | #22

That's odd. It's part of Urho3D (on [GitHub](https://github.com/urho3d/Urho3D/blob/master/Source/Urho3D/Engine/EngineDefs.h)).
Are you using an engine version from before December 2016? Otherwise maybe try **Clean All** and **Run qmake**.

-------------------------

runi | 2017-06-27 14:32:15 UTC | #23

Ah that might be it, i used the release 1.6 download since I figured that'd the last stable one. Is the current one good to plug and play?

E: Looks like it might be if I get <SDL/SDL_joystick.h> and others

-------------------------

Modanung | 2017-06-27 14:36:29 UTC | #24

[quote="runi, post:23, topic:3261"]
Is the current one good to plug and play?
[/quote]

I'd say so. I hardly had any trouble with Urho that - in the end - did not turn out to be my own fault or a local hiccup. Several times a month I compile the latest pull from master.

-------------------------

Modanung | 2017-06-27 14:39:30 UTC | #25

[quote="runi, post:21, topic:3261"]
Sorry for being a pest
[/quote]

Don't worry, btw. It's good to get feedback, and I'm glad for it to (hopefully) be of use. :slight_smile:

-------------------------

runi | 2017-06-27 14:42:06 UTC | #26

<img src="//cdck-file-uploads-global.s3.dualstack.us-west-2.amazonaws.com/standard17/uploads/urho3d/original/1X/87c68fa436bfb190f1e4e5396ac34a7ef9759627.png" width="690" height="363"> Uh oh I only just narrowly avoided this with Urho3d.h. I think i just installed what I needed to, but not sure how to mate them :confused: 

I'm looking forward to digging around once it compiles so i can see what that code turns into

-------------------------

Modanung | 2017-06-27 14:47:38 UTC | #27

¿Aware of:
https://urho3d.github.io/documentation/HEAD/_building.html

You should build Urho3D seperately. For which I use CMake.
`./cmake_clean.sh; ./cmake_generic.sh .; make`

-------------------------

runi | 2017-06-27 14:51:24 UTC | #28

Am I supposed to be looking at anything specific in that? And I have no idea what you mean when you say stuff like that... I've only messed about with the example .as scripts, so setting up this environment to make it in C++ is seeming to be a convoluted mess atm.

And wasn't cmake one of the things causing an issue with me using your wizard?

-------------------------

Modanung | 2017-06-27 14:58:33 UTC | #30

```
./cmake_clean.sh; ./cmake_generic.sh .; make
```

This is a terminal command you can paste and run into a terminal, after navigating to your Urho3D folder, to build Urho3D. Outside of QtCreator.

[quote="runi, post:28, topic:3261"]
And wasn't cmake one of the things causing an issue with me using your wizard?
[/quote]

The reason CMake caused trouble earlier was because the wizard creates an incomplete CMakeLists.txt for your project. This is unrelated to building the engine/library.

-------------------------

runi | 2017-06-27 15:10:15 UTC | #31

[quote="Modanung, post:29, topic:3261"]
./cmake_clean.sh; ./cmake_generic.sh .; make
[/quote]

Oh nice, thanks man! Looks like that's doing the trick. 50% through that at the time of writing, but now I'm curious. If I'm compiling the engine now, how does compiling my game actually work? because before I thought that I would have to compile them together.

-------------------------

runi | 2017-06-27 15:42:17 UTC | #32

    [ 91%] Linking CXX executable ../../../bin/tool/SpritePacker
    [ 91%] Built target SpritePacker
    Scanning dependencies of target ScriptCompiler
    [ 91%] Building CXX object Source/Tools/ScriptCompiler/CMakeFiles/ScriptCompiler.dir/ScriptCompiler.cpp.o
    [ 91%] Linking CXX executable ../../../bin/tool/ScriptCompiler
    ../../../lib/libUrho3D.a(loslib.c.o): In function `os_tmpname':
    loslib.c:(.text+0x21c): warning: the use of `tmpnam' is dangerous, better use `mkstemp'
    /usr/bin/ld: final link failed: No space left on device
    collect2: error: ld returned 1 exit status
    Source/Tools/ScriptCompiler/CMakeFiles/ScriptCompiler.dir/build.make:95: recipe for target 'bin/tool/ScriptCompiler' failed
    make[2]: *** [bin/tool/ScriptCompiler] Error 1
    CMakeFiles/Makefile2:1964: recipe for target 'Source/Tools/ScriptCompiler/CMakeFiles/ScriptCompiler.dir/all' failed
    make[1]: *** [Source/Tools/ScriptCompiler/CMakeFiles/ScriptCompiler.dir/all] Error 2
    Makefile:149: recipe for target 'all' failed
    make: *** [all] Error 2
    runi@runi-SATELLITE-C70D-C-12U ~/Boonscape/Urho3D-master $


damn it ran out of drive space lol

-------------------------

slapin | 2017-06-27 15:57:45 UTC | #33

Well, the space requirements are quite small though, but I think you need at least 1-2GB free space
for build.
```
slapin@slapin-pc:~$ du -sk ~/Urho3D
1647936	/home/slapin/Urho3D
slapin@slapin-pc:~$ 
```

-------------------------

slapin | 2017-06-27 16:00:22 UTC | #34

I also recommend cleaning with
```
git clean -d -f -x
```

(DANGER: if you don't have important files in Urho tree which are not committed, it will delete them)

Also if you build into separate directory, just delete the directory.

-------------------------

runi | 2017-06-27 16:24:32 UTC | #35

I just nuked some stuff elsewhere in the drive and tried it again, it skipped up to where it stopped so it wasn't too bad. I'm still unsure how I build the example from the wizard though

-------------------------

Modanung | 2017-06-27 17:27:38 UTC | #36

[quote="runi, post:35, topic:3261"]
I'm still unsure how I build the example from the wizard though
[/quote]

You seemed pretty close earlier.

Once Urho3D is done building, create a new project using the wizard. Then, in a terminal, navigate to your project's folder and run `ln -s [Urho3D Location]`, this creates a symbolic link after which QtCreator should be able to _build_ the project.
By default, each resulting build tree needs links to both `Urho3D/bin/Data` and `Urho3D/bin/CoreData` for one of these conjured projects to _run_ without errors.

-------------------------

runi | 2017-06-27 17:39:49 UTC | #37

<img src="//cdck-file-uploads-global.s3.dualstack.us-west-2.amazonaws.com/standard17/uploads/urho3d/original/1X/a41a4d3468a8d1e521532608ed881b0b38c8e342.png" width="644" height="452">

Okay so this screenshot is a bit of a mess since this is the last bit i'm fuzzy on. I was close earlier? that's encouraging.

I've tried linking the urho folder in a few places now but qt creator is still showing 
`/home/runi/Boonscape/boonscape/luckey.h:22: error: Urho3D/Urho3D.h: No such file or directory`

-------------------------

Modanung | 2017-06-27 17:46:45 UTC | #38

The link to the Urho3D folder goes into your project folder (boonscape). `ln -s ../Urho3D-master Urho3D` from there.

The links to the Data and CoreData folders go into every build folder (build-boonscape-Desktop-Default). On top of that it expects a Resources folder. But these folders are not required for a successful build.

-------------------------

runi | 2017-06-27 18:27:27 UTC | #39

<img src="//cdck-file-uploads-global.s3.dualstack.us-west-2.amazonaws.com/standard17/uploads/urho3d/original/1X/096e7dd3869f0a91e582801ab5eb2e14e112ab80.png" width="690" height="327">This felt like it should have worked

-------------------------

Modanung | 2017-06-27 18:35:27 UTC | #40

Try a **Clean All**, then **Run qmake** from the Build menu in QtCreator. Then retry building.

-------------------------

runi | 2017-06-27 18:40:04 UTC | #41

Clean all: 

    19:37:55: Running steps for project boonscape...
    19:37:55: Starting: "/usr/bin/make" clean
    rm -f luckey.o mastercontrol.o sceneobject.o spawnmaster.o inputmaster.o player.o controllable.o effectmaster.o
    rm -f *~ core *.core
    19:37:55: The process "/usr/bin/make" exited normally.
    19:37:55: Elapsed time: 00:00.

qmake:

    19:38:39: Running steps for project boonscape...
    19:38:39: Starting: "/usr/lib/x86_64-linux-gnu/qt5/bin/qmake" /home/runi/Boonscape/boonscape/boonscape.pro -r -spec linux-g++-64 CONFIG+=debug
    19:38:39: The process "/usr/lib/x86_64-linux-gnu/qt5/bin/qmake" exited normally.
    19:38:39: Elapsed time: 00:00.


Trying it now after doing those two things: 

    19:38:53: Configuration unchanged, skipping qmake step.
    19:38:53: Starting: "/usr/bin/make" 
    g++ -c -m64 -pipe -std=c++14 -O2 -g -Wall -W -fPIC  -I../boonscape -I. -I../Urho3D/include -I../Urho3D/include/Urho3D/ThirdParty -I/usr/lib/x86_64-linux-gnu/qt5/mkspecs/linux-g++-64 -o luckey.o ../boonscape/luckey.cpp
    In file included from ../boonscape/luckey.cpp:19:0:
    ../boonscape/luckey.h:22:27: fatal error: Urho3D/Urho3D.h: No such file or directory
    compilation terminated.
    Makefile:313: recipe for target 'luckey.o' failed
    make: *** [luckey.o] Error 1
    19:38:53: The process "/usr/bin/make" exited with code 2.
    Error while building/deploying project boonscape (kit: Desktop)
    When executing step "Make"
    19:38:53: Elapsed time: 00:00.

-------------------------

Modanung | 2017-06-27 20:29:02 UTC | #42

Hrm... what does your `.pro` file look like?
It seems to be looking for `../Urho3D` instead of `../boonscape/Urho3D` or `Urho3D`. I guess this is in accordance with an [instruction](https://discourse.urho3d.io/t/new-to-engine-and-curious-about-capabilities/3261/16?u=modanung) I gave earlier... which became obsolete.

-------------------------

runi | 2017-06-27 20:34:12 UTC | #43

<img src="//cdck-file-uploads-global.s3.dualstack.us-west-2.amazonaws.com/standard17/uploads/urho3d/original/1X/566271963a786c9dc96e393beb05634b6f9e9a88.png" width="689" height="398">I've tried both of these now and both result in the same. 
<img src="//cdck-file-uploads-global.s3.dualstack.us-west-2.amazonaws.com/standard17/uploads/urho3d/original/1X/b7cffd5917f4c9cf1ec6014523b39dce94a0898c.png" width="690" height="398">

Im going to try and run clean call and qmake in the different configurations just incase that's the magic trick

-------------------------

Modanung | 2017-06-27 20:35:55 UTC | #44

Ah, but `Boonscape` should be `boonscape`, in the first screenshot.

-------------------------

runi | 2017-06-27 20:39:58 UTC | #45

I guess it's true about yourself being your own undoing... Thanks, that did the trick. I'll get on sorting those idiotic names in a min. <img src="//cdck-file-uploads-global.s3.dualstack.us-west-2.amazonaws.com/standard17/uploads/urho3d/original/1X/64ae939bf51c1fc8e7fa386f0ee0af07abef3c76.png" width="690" height="404">

-------------------------

Modanung | 2017-06-27 20:44:12 UTC | #46

Cool! Thanks for being co-tenacious. :)
Glad it works.

-------------------------

runi | 2017-06-27 20:48:06 UTC | #47

Oh well im just some pest on the forum with issues so the thanks is to you. So what does that error box mean? I have a feeling it has something to do with those optional folders you mentioned

-------------------------

Modanung | 2017-06-27 22:23:07 UTC | #48

Well within `mastercontrol.cpp` there is this line:
```
    engineParameters_[EP_RESOURCE_PATHS] = "Data;CoreData;Resources";
```
Which makes the binary/executable look for these three folders. The message pops up because it can't find those.
So inside your build folders should be symbolic links to the `Data` and `CoreData` folders - which are located at `Urho3D`[spoiler]`-master`[/spoiler]`/bin/` - and a `Resources` folder, meant for project specific resources.

For the project to run you could also remove `;Resources` from the resource paths string.

-------------------------

runi | 2017-06-27 22:35:48 UTC | #49

    runi@runi-SATELLITE-C70D-C-12U ~/Boonscape/boonscape $ ln -s ../Urho3D-master/bin/CoreData/
    runi@runi-SATELLITE-C70D-C-12U ~/Boonscape/boonscape $ ln -s ../Urho3D-master/bin/Data
    runi@runi-SATELLITE-C70D-C-12U ~/Boonscape/boonscape $ ls
    boonscape.pro       effectmaster.cpp  luckey.h           sceneobject.cpp
    boonscape.pro.user  effectmaster.h    mastercontrol.cpp  sceneobject.h
    controllable.cpp    inputmaster.cpp   mastercontrol.h    spawnmaster.cpp
    controllable.h      inputmaster.h     player.cpp         spawnmaster.h
    CoreData            LICENSE_TEMPLATE  player.h           Urho3D
    Data                luckey.cpp        Resources
    runi@runi-SATELLITE-C70D-C-12U ~/Boonscape/boonscape $ 

I linked the two folders in bin, and created the Resources folder beside them and tried it again, same error box.

So I removed 'Resources; ' but received the same box. I feel like I'm getting close now because that last one went through a lot more actions of the build process before failing lol

-------------------------

slapin | 2017-06-27 22:54:20 UTC | #50

well, where is executable you run? The directories/links should be placed at the same place.

-------------------------

runi | 2017-06-27 22:58:25 UTC | #51

Berp derp, now it all works. Thanks for slapin some sense into me. I was linking things in the wrong folder it seems. But I'm not sure how long that was the problem for... lol

-------------------------

runi | 2017-06-27 23:20:11 UTC | #52

Thanks @Modanung & @slapin for your help with this weary noob. 

Do you have any parting advice for where I should go from here? All of this has made me aware that I'm in at the deep end, so I figure information is gold at this point c:

-------------------------

Modanung | 2017-06-27 23:44:06 UTC | #53

If you want to get models from Blender into Urho, I'd advise you to use [this](https://github.com/reattiva/Urho3D-Blender) plugin. Then you could:

- Replace the box with a custom model
- Make it move
- Experiment with physics
- Create your own `LogicComponent` subclass (which is easy with the class wizard)

And I'll bet you've got more specific questions by then. :slight_smile:

-------------------------

runi | 2017-06-27 23:44:03 UTC | #54

I've been making some random 3d models in a program called 'Wings3D' because whenever I attempt to learn blender, it goes as great as a dog flies a helicopter. Badly and not for long. <img src="//cdck-file-uploads-global.s3.dualstack.us-west-2.amazonaws.com/standard17/uploads/urho3d/original/1X/da2a23f0ad29cd60c607750f9a6dc5c5911f975f.png" width="443" height="499">

It's going alright to make small objects but I haven't begun to look into compatibility just yet but it exports to these so I think I'll be able to find a suitible converter lol

<img src="//cdck-file-uploads-global.s3.dualstack.us-west-2.amazonaws.com/standard17/uploads/urho3d/original/1X/07f2fc557a943951df29b2ac14e135e7778a4d77.png" width="247" height="199">

-------------------------

slapin | 2017-06-28 00:45:10 UTC | #55

I'd advice you to still learn Blender, it is not that hard, even I can use it.
You will need some patience and good non-sleepy tutorial on Youtube or Vimeo.
Also there are paid tutorial resources for Blender like CGCookie.

That will add you some real power.
Scripting in Blender will allow you to have easier assets path, as you will always have cases which are
handled very poorly with exporter.

Also, I'd suggest making own technique demos. So if you want some feature in your game,
make a small demo for that feature, with everything as simple as possible. That will make your
learning less frustrating.

-------------------------

slapin | 2017-06-28 00:50:28 UTC | #56

Also @Modanung has some cool game in stock which might really get promising
eventually, I'd suggest poking him until he agrees to cooperate... :)

-------------------------

