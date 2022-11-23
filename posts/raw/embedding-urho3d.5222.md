urnenfeld | 2019-06-08 13:34:24 UTC | #1

Hello,

Thinking how could I help this community with my current knowledge. I came to apply [yocto](https://www.yoctoproject.org).

It could not sound familiar to people who is not into embedded linux. Summarizing a lot, this is a way to transparently crosscompile your project to any Linux embedded platform regardless of the compiler/architecture/soc. Somehow if there is a Linux kernel that runs the [platform](https://www.yoctoproject.org/software-overview/downloads) you can easily port your project into.

So I started playing, without major patching I could create a recipe(which is more merit of urho3d build system) which builds the whole Urho3D engine and embeds into a Linux Image. So ideally Urho3d engine could be run in any platform that there exists a yocto bsp layer for it.

https://github.com/urnenfeld/meta-urho3D

The typical development goes first in a qemux86 virtual machine, and then you move to real HW. On this virtual environment unfortunately, the sample binaries does not run(Illegal Instruction). I kow the reasons, I need a bit of digging the urho3d build system, and later on will get more complicated when we get closer to the metal. But this is not the main intention of this post.

Eventually if this exercise succeeds I was thinking on a kind of Linux Distro targeted/optimized to Urho3D and Urho3D based games... A splash screen at boot up and ASAP going to some game selector/installer... "The UrhoBox" !?... ok, some things might be utopic here...

The unique question would be, Is this something that catches the attention of the community?

-------------------------

weitjong | 2019-06-08 14:12:37 UTC | #2

It sounds interesting to me, although I have never heard the Yocto project before. Currently Urho3D can already cross-compile to RPI and any generic ARM platforms, so I don’t think it will be a herculean task to make it cross-compile for other target triplet. I would like to contribute (on my spare time), if you need help.

-------------------------

urnenfeld | 2019-06-08 15:12:17 UTC | #3

@weitjong With yocto this "ARM" support could be more *specific or Normalized*. I mean, urho3d may run in a rPI but maybe not in a NxP i.MX8 Sabre Board. Despite both being ARM.

In my development I am using a virutal target (a modified qemux86, which emulates a intel... erm... Pentium III). Binaries are deployed, but Urho3d tends to generate SSE2 code, which creates illegal instructions on the virtual target. So some help on what makes the build system decide to use SSE2 or not would be useful.

As well this might not be the place to track this... I could create tickets in the github then people could comment on them.

-------------------------

weitjong | 2019-06-08 16:31:43 UTC | #4

Earlier I mentioned that currently Urho3D build system can already cross-compile to generic ARM platforms, although it is only been tested on ODROID-C2 (ARM64) board and ODROID-X2 board by one or two users in the past. I believe our build system is capable of targeting any triplets like I said earlier. One just needs to provide the right mix of build options with the right cross-compiling toolchain. As long the boards run with Linux on ARM processor then it should be good to go.

As for the SSE SIMD instruction support, without looking at the build script now I think it should be auto-detected and configured accordingly. If the detection is wrong then you should be able to override it by using the `URHO3D_SSE` option. However, on 64-bit Intel platform this option cannot be turned off. Perhaps, what you need to tune is the compiler flags to target a specific "-march". See `URHO3D_DEPLOYMENT_TARGET` build option for more detail.

HTH.

-------------------------

urnenfeld | 2019-06-08 19:52:37 UTC | #5

[quote="weitjong, post:4, topic:5222"]
although it is only been tested on ODROID-C2 (ARM64) board and ODROID-X2 board
[/quote]
This is already great, a good point and reference. After the qemux86 my plan was going for the rPi, the odroids should be next then. 

[quote="weitjong, post:4, topic:5222"]
I believe our build system is capable of targeting any triplets like I said earlier. One just needs to provide **the right mix of build options** with the right cross-compiling toolchain.
[/quote]
This is where yocto could help. Currently the [recipe](https://github.com/urnenfeld/meta-urho3D/blob/master/recipes-games/urho3D/urho3d_git.bb) is very basic, just builds Urho3D. When it is mature enough, there would be different customization for each board(MACHINE) supported. So these *right mix of build options* for each board would be clearly listed and automatized in the yocto recipe, and could be included in a Linux Embedded image.

Let me clarify this is not impacting Urho3D build system at all. It is an external process/tool that lets you fetch/configure/builds the code, letting you tweak every step...

-------------------------

urnenfeld | 2019-07-08 21:21:21 UTC | #6

[quote="weitjong, post:4, topic:5222"]
you should be able to override it by using the `URHO3D_SSE` option
[/quote]

Yep that was it, at least for [this target platform](https://github.com/urnenfeld/meta-urho3D/commit/3c1c87ba0ebac7a451a8bd60e4383bf84a60c8a1#diff-35ab523fcbdee8ec0c748e3923902ba0R23):

![Screenshot_20190708_223701|644x500](upload://bLkfdvjxe76QEcubHsJDp7hFbQE.png)

-------------------------

Modanung | 2019-07-08 22:20:15 UTC | #7

[quote="urnenfeld, post:1, topic:5222"]
I was thinking on a kind of Linux Distro targeted/optimized to Urho3D and Urho3D based games… A splash screen at boot up and ASAP going to some game selector/installer… “The UrhoBox” !?
[/quote]

Sounds like a cool project. How about calling it [**The Fishmaster**](http://www.mikseri.net/artists/urho/evil-shark/362081/)? :slight_smile:

-------------------------

Modanung | 2019-07-09 09:16:40 UTC | #8

Or simply [the *Fin*](https://en.wiktionary.org/wiki/fin)?
It could have 3D-printed standing case inspired in shape by Urho's back fin, like an organic Wii. The name would also be referencing @cadaver's nationality (in [several](https://en.wiktionary.org/wiki/Fin) non-English languages) _and_ French people would be confused as it boots. Several other meanings of the word:
- black
- classy
- purpose

@urnenfeld You may be interesting in this [trove of bugs](https://gitlab.com/luckeyproductions) for testing purposes.  ;)

-------------------------

urnenfeld | 2019-07-09 10:50:11 UTC | #9

[quote="Modanung, post:8, topic:5222"]
You may be interesting in this [trove of bugs](https://gitlab.com/luckeyproductions) for testing purposes
[/quote]

These are your games aren't they??

My roadmap is as follows:

1. Deploy on Real HW (rPI)
2. Define a format to Define & Describe a Game
3. Develop some kind of game Selector/Launcher (Previous point would be its input)
4. Splash screen (with name and art)

Feedback is really welcome for second and third point.

[quote="Modanung, post:8, topic:5222"]
*and* French people would be confused as it boots
[/quote]

And mines (spanish) :smile:

-------------------------

Modanung | 2019-07-09 11:32:53 UTC | #10

Here's a quick conceptual render to get a impression of what the Fin could look like:

![fin|690x239](upload://nwFxYjCX5mF30UcgY8i8VMIHrHG.png) 
[quote="urnenfeld, post:9, topic:5222"]
These are your games aren’t they??
[/quote]
There has been some collaboration, but it's mostly an accumulation of my doing, yes. All code is licensed under GPL, assets are CC-BY-SA.

-------------------------

SirNate0 | 2019-07-09 15:41:48 UTC | #11

I like the design, but I think I'd go with rotating the board inside so that the whole thing is only as wide as the Fin (though the ports might ruin the appearance, I'm not sure).

-------------------------

Leith | 2019-07-10 07:21:54 UTC | #12

1. Deploy on really bad hardware (it helps show up performance bottlenecks)
2. Have some "ideas guy" describe a game, in great detail, and capture its requirements
3. Define your coding standards and extract architectural requirements from the game design requirements
4. Design your code architecture before you write a single line of code.
5. Implement your architecture using placeholder/imposter methods.
6. Complete your implementation iteratively, replacing placeholders with working code, while testing periodically
7. Did I mention version control / making backups?
8. Get some peer feedback along the way, it can help correct your course and save time and money.

-------------------------

urnenfeld | 2019-07-11 17:58:21 UTC | #13

[quote="Leith, post:12, topic:5222"]
* Deploy on really bad hardware (it helps show up performance bottlenecks)
[/quote]
As bad as even I am not sure if will ever support it ... (RaspPi Zero W)

[quote="Leith, post:12, topic:5222"]
* Have some “ideas guy” describe a game, in great detail, and capture its requirements
[...]
* Get some peer feedback along the way, it can help correct your course and save time and money.
[/quote]

I encourage anyone to filll PRs or Issues in the [meta-urho3d](https://github.com/urnenfeld/meta-urho3D) for such feedback


[quote="Leith, post:12, topic:5222"]
* Define your coding standards and extract architectural requirements from the game design requirements
* Design your code architecture before you write a single line of code.
* Implement your architecture using placeholder/imposter methods.
* Complete your implementation iteratively, replacing placeholders with working code, while testing periodically
* Did I mention version control / making backups?
[/quote]

Well, that applies for any Software Development :wink:

----
For the ones following I moved to a branch called [pyro](https://github.com/urnenfeld/meta-urho3D/tree/pyro) (yocto convention) for the rpi0 development. Despite it is trying to compile and passed through the configuration stage, I have my doubts as urho3d buildsystem is trying to crosscompile while yocto already takes care of this.

For example, yocto interprets that everyting behind that cmake is meant to be crosscompiled, but there are things inside the project which looks to be meant to be build natively(LUA, Angelscript?). **It would be useful to know if these 2 parts can be somehow separated or launched separatedly.**


As for name the of all this :slight_smile: *if it ever reaches something*....
 
One of main reasons of the exercise, was to **promote** the engine. Therefore I would have a strong position to keep the word *urho* inside the name of the project. 
As there would be other elements & entities around this (game selector, some kind of lifecycle), all the good ideas risen here could have its place, even for codenames or versioning... at a last step it could be as well voted ;)

-------------------------

urnenfeld | 2019-07-26 15:27:31 UTC | #14

I think my Raspberry PI B+ is dead. Anyway as I said, I started with:

[quote="urnenfeld, post:13, topic:5222"]
As bad as even I am not sure if will ever support it … (RaspPi Zero W)
[/quote]

But I bought rasp0 in the past with domotics intentions, therefore I had not covered the mini-HDMI adapter required.

I mention because I could generate an **image with the engine library and some examples**, which was kind of the first milestone to evaluate if all this was feasible or not... but hey I cannot test it.

So while the adapter arrives, if someone owns rasp 0w and wants to test, I can upload the image somewhere. (I would do it anyways but villages here just get ADSL with 0.6MB/s upload...)

-------------------------

dertom | 2019-07-26 20:18:01 UTC | #15

I don't have a rpi0 but I have several other of those Singleboard-Computers (rpi 3b+,odroid-c2 and a couple of different orange pis). So if i can help with those devices maybe at a later stage, I would be happy to do so.

EDIT: Actually I compiled urho3d on odroid-c2 and orange pi pc2 a couple of days ago which worked out of the box (without anglescript and another cmake-switch) and I got 8fps on both (both were not accelerated...)

-------------------------

urnenfeld | 2019-07-27 11:10:26 UTC | #16

[quote="dertom, post:15, topic:5222"]
Actually I compiled urho3d on odroid-c2 and orange pi pc2 a couple of days ago which worked out of the box (without anglescript and another cmake-switch) and I got 8fps on both (both were not accelerated…)
[/quote]

Can you share the actual switches?

[quote="dertom, post:15, topic:5222"]
I got 8fps on both (both were not accelerated…)
[/quote]
Do you remember what got these 8fps? a sample? a particular game?
This is another feasibility fact...

I believe my work is linking to the proper broadcom accelerated libs...

-------------------------

dertom | 2019-07-27 12:22:16 UTC | #17

[quote="urnenfeld, post:16, topic:5222"]
Can you share the actual switches?
[/quote]
cmake -DURHO3D_ANGELSCRIPT=0 -DURHO3D_TOOLS=0 [PATH_TO_URHO3D_SRC]

(You can take out more....you know the docs with [all cmake-switches](https://urho3d.github.io/documentation/1.7/_building.html),right?)

[quote="urnenfeld, post:16, topic:5222"]
Do you remember what got these 8fps? a sample? a particular game?
[/quote]

It was the sprite demo, as well as the physics-demo. I actually didn't test too much. I was mostly interested if it works and I'm more interested to test it in headless-mode as server....(someday ;) )

About the acceleration: I'm using armbian-imgs as OS and those did not had the mali-graphics-drivers included. The official odroid-c2 ubuntu have those but I didn't had time to test those...maybe I will give it a try this weekend...
(EDIT: forget it. I just saw that I installed armbian again....this is because I'm experimenting kubernets to cluster my mini-computers and I want to have the same OS-Distri on each...nonetheless once there is something to test...tell me. I got lots of SD-Cards ;) )

-------------------------

urnenfeld | 2019-07-27 13:52:16 UTC | #18

[quote="dertom, post:17, topic:5222"]
you know the docs with [all cmake-switches](https://urho3d.github.io/documentation/1.7/_building.html),right?
[/quote]

Yeah, I actually expected more of -DARM ... are you compiling in target then?

[quote="dertom, post:17, topic:5222"]
It was the sprite demo, as well as the physics-demo 
[/quote]

So I'll set them for benchmarking [from now on](https://github.com/urnenfeld/meta-urho3D/commit/e3a2335d6d668b47fed9ee8fc099367ab67361a1) ;)

-------------------------

SirNate0 | 2019-07-27 14:06:00 UTC | #19

I have a Raspberry Pi 0w. If I can find a spare micro SD card I'll test it for you if you upload the image.

-------------------------

dertom | 2019-07-27 15:08:31 UTC | #20

[quote="urnenfeld, post:18, topic:5222"]
Yeah, I actually expected more of -DARM … are you compiling in target then?
[/quote]

Yes, I compile on the device...I tried to cross-compile once (some time ago) but did not succeed,...the only problem with compiling on the device was assimp that seems to be too much for my little device ;)  Therefore I disabled the tools. Anglescript had millions of strange errors....

-------------------------

urnenfeld | 2019-07-27 15:43:31 UTC | #21

[quote="SirNate0, post:19, topic:5222, full:true"]
I have a Raspberry Pi 0w. If I can find a spare micro SD card I’ll test it for you if you upload the image.
[/quote]

That's great!

> 6388d8af60482d2205642a78fbff5f39  core-image-urho3d-raspberrypi0-wifi-20190724161747.7z

[Get it here](http://depositfiles.com/files/404b6knyl), **please check the md5**, is the first time I use that service...

It should load weston with a small terminal, there you should be able to load one of the examples. Note only  00, 01, 04 are currently in the image. There should be no root password.

-------------------------

SirNate0 | 2019-07-27 17:03:51 UTC | #22

You could try building with AS_MAX_PORTABILITY defined (not a CMake switch but a preprocessor define) to see if that resolves the millions of strange errors building Angel Script.

-------------------------

dertom | 2019-07-27 18:11:02 UTC | #23

@urnenfeld
I finally got urho3d-samples to run using the gpu (mali450). Here are some benchmarks, just in case you are interested:
- 03 - Sprites 35fps
- 11 - Phyiscs (before shooting blocks:42 afterwards a steady 27 no matter how much I push the system)
- 13 - Ragdoll 43
- 18 - Character 42
- 19 - Vehicle 25
- 25 - Particles 60



@SirNate0 Setting AS_MAX_PORTABILITY preprocessor-definition doesn't change a thing. Here the error-log with 'VERBOSE=1 make'. Maybe you can see something out of it. 
```
[ 63%] Building CXX object Source/Urho3D/CMakeFiles/Urho3D.dir/AngelScript/AudioAPI.cpp.o
cd /home/odroid/_dev/extprojects/_build/Urho3D/Source/Urho3D && /usr/bin/c++  -DGENERIC_ARM -DHAVE_SINCOSF -DHAVE_STDINT_H -DSTBI_NEON -DTOLUA_RELEASE -DURHO3D_ANGELSCRIPT -DURHO3D_FILEWATCHER -DURHO3D_IK -DURHO3D_IS_BUILDING -DURHO3D_LOGGING -DURHO3D_LUA -DURHO3D_NAVIGATION -DURHO3D_NETWORK -DURHO3D_PHYSICS -DURHO3D_PROFILING -DURHO3D_STATIC_DEFINE -DURHO3D_THREADING -DURHO3D_URHO2D -DURHO3D_WEBP -I/home/odroid/_dev/extprojects/_build/Urho3D/Source/Urho3D -I/home/odroid/_dev/extprojects/Urho3D/Source/Urho3D -I/home/odroid/_dev/extprojects/_build/Urho3D/include/Urho3D/ThirdParty -I/home/odroid/_dev/extprojects/_build/Urho3D/include/Urho3D/ThirdParty/Bullet -I/home/odroid/_dev/extprojects/_build/Urho3D/include/Urho3D/ThirdParty/Detour -I/home/odroid/_dev/extprojects/_build/Urho3D/include/Urho3D/ThirdParty/Lua  -DAS_MAX_PORTABILITY=1 -std=gnu++11 -Wno-invalid-offsetof  -fsigned-char -pipe -march=armv8-a -pthread -fdiagnostics-color=auto -include "/home/odroid/_dev/extprojects/_build/Urho3D/Source/Urho3D/Precompiled.h" -O3 -DNDEBUG   -o CMakeFiles/Urho3D.dir/AngelScript/AudioAPI.cpp.o -c /home/odroid/_dev/extprojects/Urho3D/Source/Urho3D/AngelScript/AudioAPI.cpp
In file included from /home/odroid/_dev/extprojects/Urho3D/Source/Urho3D/AngelScript/../AngelScript/../AngelScript/Addons.h:35:0,
                 from /home/odroid/_dev/extprojects/Urho3D/Source/Urho3D/AngelScript/../AngelScript/APITemplates.h:25,
                 from /home/odroid/_dev/extprojects/Urho3D/Source/Urho3D/AngelScript/AudioAPI.cpp:25:
/home/odroid/_dev/extprojects/_build/Urho3D/include/Urho3D/ThirdParty/AngelScript/angelscript.h:45:0: warning: "AS_MAX_PORTABILITY" redefined
 #define AS_MAX_PORTABILITY

<command-line>:0:0: note: this is the location of the previous definition
In file included from /home/odroid/_dev/extprojects/_build/Urho3D/include/Urho3D/ThirdParty/AngelScript/wrapmacros.h:31:0,
                 from /home/odroid/_dev/extprojects/_build/Urho3D/include/Urho3D/ThirdParty/AngelScript/angelscript.h:1967,
                 from /home/odroid/_dev/extprojects/Urho3D/Source/Urho3D/AngelScript/../AngelScript/../AngelScript/Addons.h:35,
                 from /home/odroid/_dev/extprojects/Urho3D/Source/Urho3D/AngelScript/../AngelScript/APITemplates.h:25,
                 from /home/odroid/_dev/extprojects/Urho3D/Source/Urho3D/AngelScript/AudioAPI.cpp:25:
/home/odroid/_dev/extprojects/Urho3D/Source/Urho3D/AngelScript/../AngelScript/APITemplates.h: In function ‘void Urho3D::RegisterSubclass(asIScriptEngine*, const char*, const char*)’:
/home/odroid/_dev/extprojects/_build/Urho3D/include/Urho3D/ThirdParty/AngelScript/wrap16.h:2916:67: error: expected primary-expression before ‘)’ token
 #define WRAP_OBJ_LAST(name)       (::gw::id(name).TMPL ol< name >())
                                                                   ^
/home/odroid/_dev/extprojects/_build/Urho3D/include/Urho3D/ThirdParty/AngelScript/wrapmacros.h:74:102: note: in expansion of macro ‘WRAP_OBJ_LAST’
 #define RegisterObjectMethodFasCALL_CDECL_OBJLAST(clsdcl,decl,fun) RegisterObjectMethod(clsdcl,decl, WRAP_OBJ_LAST(fun), asCALL_GENERIC); //assert(r >= 0);
                                                                                                      ^~~~~~~~~~~~~
/home/odroid/_dev/extprojects/_build/Urho3D/include/Urho3D/ThirdParty/AngelScript/wrapmacros.h:70:64: note: in expansion of macro ‘RegisterObjectMethodFasCALL_CDECL_OBJLAST’
 #define RegObjectMethodIndirect(clsdcl,decl, F, clsfunc, kind) RegisterObjectMethod##F##kind (clsdcl,decl,clsfunc) // ... = decl or it = decl, cls for asCall_ThisCall
                                                                ^~~~~~~~~~~~~~~~~~~~
/home/odroid/_dev/extprojects/_build/Urho3D/include/Urho3D/ThirdParty/AngelScript/wrapmacros.h:68:35: note: in expansion of macro ‘RegObjectMethodIndirect’
 #define RegisterObjectMethod(...) RegObjectMethodIndirect(__VA_ARGS__)
                                   ^~~~~~~~~~~~~~~~~~~~~~~
/home/odroid/_dev/extprojects/Urho3D/Source/Urho3D/AngelScript/../AngelScript/APITemplates.h:224:13: note: in expansion of macro ‘RegisterObjectMethod’
     engine->RegisterObjectMethod(classNameT, declReturnU.CString(), asFUNCTION((RefCast<T, U>)), asCALL_CDECL_OBJLAST);^M
             ^~~~~~~~~~~~~~~~~~~~
/home/odroid/_dev/extprojects/_build/Urho3D/include/Urho3D/ThirdParty/AngelScript/wrap16.h:2916:67: error: expected primary-expression before ‘)’ token
 #define WRAP_OBJ_LAST(name)       (::gw::id(name).TMPL ol< name >())
                                                                   ^
/home/odroid/_dev/extprojects/_build/Urho3D/include/Urho3D/ThirdParty/AngelScript/wrapmacros.h:74:102: note: in expansion of macro ‘WRAP_OBJ_LAST’
 #define RegisterObjectMethodFasCALL_CDECL_OBJLAST(clsdcl,decl,fun) RegisterObjectMethod(clsdcl,decl, WRAP_OBJ_LAST(fun), asCALL_GENERIC); //assert(r >= 0);
                                                                                                      ^~~~~~~~~~~~~
/home/odroid/_dev/extprojects/_build/Urho3D/include/Urho3D/ThirdParty/AngelScript/wrapmacros.h:70:64: note: in expansion of macro ‘RegisterObjectMethodFasCALL_CDECL_OBJLAST’
 #define RegObjectMethodIndirect(clsdcl,decl, F, clsfunc, kind) RegisterObjectMethod##F##kind (clsdcl,decl,clsfunc) // ... = decl or it = decl, cls for asCall_ThisCall
                                                                ^~~~~~~~~~~~~~~~~~~~
/home/odroid/_dev/extprojects/_build/Urho3D/include/Urho3D/ThirdParty/AngelScript/wrapmacros.h:68:35: note: in expansion of macro ‘RegObjectMethodIndirect’
 #define RegisterObjectMethod(...) RegObjectMethodIndirect(__VA_ARGS__)
                                   ^~~~~~~~~~~~~~~~~~~~~~~

``` 
Maybe you know what's going on there

-------------------------

urnenfeld | 2019-07-27 21:13:29 UTC | #24

[quote="dertom, post:23, topic:5222"]
Maybe you know what’s going on there
[/quote]
I am not sure the cause, but I am sure I faced this error. It got solved when I dealt with another issue regarding [system headers inclusion](https://github.com/urnenfeld/meta-urho3D/blob/e3a2335d6d668b47fed9ee8fc099367ab67361a1/recipes-games/urho3D/urho3d_git.bb#L13-L29)...

Out of curiosity which gcc version is that */usr/bin/c++*? 
[spoiler]...hinting that maybe the crosscompiled compiler version is too low to handle such c++ templating...[/spoiler]

-------------------------

dertom | 2019-07-27 21:16:25 UTC | #25

[quote="urnenfeld, post:24, topic:5222"]
Out of curiosity which gcc version is that */usr/bin/c++* ?
[/quote]
c++ (Ubuntu/Linaro 7.4.0-1ubuntu1~18.04.1) 7.4.0

-------------------------

SirNate0 | 2019-07-28 03:55:53 UTC | #26

One thing you could try is editing `ThirdParty/AngelScript/include/wrap16.h` at the bottom to force `TMPL` to be defined as `template` (remove the #if condition around line 2908. Based on [this Stack Overflow question](https://stackoverflow.com/questions/3505713/c-template-compilation-error-expected-primary-expression-before-token), it seems that the error message generated can be caused by not including that keyword in some situations.

-------------------------

dertom | 2019-07-28 08:38:43 UTC | #27

@SirNate0: This did the job :+1:
EDIT: The compilation stalled compiling the NavigationAPI...this seems similiar to compiling assimp on the device itself. That also stalled...

-------------------------

SirNate0 | 2019-07-28 15:45:55 UTC | #28

Excellent! Could you make an issue an GitHub describing the issue and solution so others will know about it until the issue can be fixed in master (if I had to guess, the #if is actually backwards, and the `#define TMPL template` should be there generally correct one, but it would require testing on more compilers to be sure). 

And @urnenfeld regarding testing the image, after the color gradient and yocto boot images I just end up with "INIT: Id "s0" respawning too fast: disabled for 5 minutes" displayed on the console.

-------------------------

urnenfeld | 2019-08-22 16:16:44 UTC | #29

[quote="SirNate0, post:28, topic:5222"]
I just end up with “INIT: Id “s0” respawning too fast: disabled for 5 minutes” displayed on the console.
[/quote]

Hi, I got the adapter & got to the same point. You should be able to hit ATL+F1 and make a login. But anyways I need to dig more as weston is not launching in tty2...

-------------------------

glitch-method | 2019-08-30 09:10:01 UTC | #30

this is a fantastic idea, I have recently also considered building a distro to explore using kernel modules to drive a game. I'll be following this project closely!

I haven't used yocto, but in this case (arm boards) it's probably the best method.

I'll also test as i'm able...I have a rpi2b and a rpi3b. the rpi0 will definitely be the real test though.
also, I thought broadcom was still sitting on the rpi gpu libs?

as a baseline, armbian is a good choice, I expect ubuntu will run slightly slower. if you want to see how fast it /can/ run, give void linux (cough musl cough) a try.

regarding compiling on silly targets like rpi0, and the ld: s0 issue, trying to compile statically (cough musl cough) may indicate more (assuming your linker will complain..)

-------------------------

urnenfeld | 2019-08-31 10:13:26 UTC | #31

[quote="glitch-method, post:30, topic:5222"]
regarding compiling on silly targets like rpi0
[/quote]

Remember the *promotion* background intention. On that type of HW we can really show what the engine is capable of.

Given the yocto ecosystem, building to another target of the same family will be almost straight forward. Don't worry about this part, if this succeeds there will be builds for the rpi2 pi3 and rpi4 :smile: (my only hurdle is that they take hours to finish, and ~50GB of disk each)

-------------------------

glitch-method | 2019-08-31 19:03:49 UTC | #32

oh definitely. I was calling the rpi0 itself silly, not building for it. :stuck_out_tongue_winking_eye:

-------------------------

urnenfeld | 2019-08-31 21:33:59 UTC | #33

[quote="glitch-method, post:32, topic:5222"]
I was calling the rpi0 itself silly,
[/quote]

Oh sure, I understood so at the first moment. It is if fact so, I just expect the simpliest games to run, and even has no audio... but honestly speaking, it is as well the only rpi I own at the moment :blush: 

Small update: The latest images are jumping already to a graphical interface, but somehow the SDL part of the engine is not properly built as it cannot find a video device.

-------------------------

glitch-method | 2019-08-31 22:43:29 UTC | #34

how are you accessing the tty? perhaps force video in boot/config.txt? idk how the 0 differs there, but I encountered a similar issue starting a vnc server on a headless rpi2.

edit: the config.txt line I used was [code]hdmi_force_hotplug=1[/code]

-------------------------

urnenfeld | 2019-09-01 10:10:13 UTC | #35

Yes the graphpics are in the tty2. What I mean are the errors shown at the very end:

https://youtu.be/q2TBdIebnQo

-------------------------

urnenfeld | 2019-09-18 21:21:00 UTC | #36

Solved! I am surprised how the 04th sample goes in a RPI 0, at the end should be fine for low specs games...

https://www.youtube.com/watch?v=eY2ETbWrOqA

I'll be pushing the latest changes tomorrow, and split the post to comment on the next steps.

-------------------------

