spacenoobs | 2017-01-02 01:07:25 UTC | #1

Hi people...

I'm a very experienced software developer when it comes to some things... but when it comes to 3D I am a total noob and I'm ENTIRELY STUCK. Also I'm finding it miserable working alone... I need help...

Right now... I'm trying to draw some voxels on screen... I have made a basic voxel demo in OpenGL but it's taken me weeks to get the most basic stuff working. I'm finding working with OpenGL a miserable experience... working alone. I need help...

I got some VERY BASIC short-term goals (around voxels) that pretty much anyone could help me with... and some long-term goals (an entirely new concept of working with code, and games... basically revolutionising everything...)

I can't post links in my first post, so I'll just describe it... and post the pictures later.

...

I was? trying to figure out ?how to use basic shapes, like cubes, and make it look like energy, somehow??

I thought of adding nice effects, glow, lightening, vibration, movement, dust motes, etc? I drew that on paper.

I also experimented (on paper) with different shapes? hexagons ?looked more like energy??

But my current progress with OpenGL is still just colored cubes? and looks pretty basic.

...

OK so I'll recap for clarity... in the short-term I got this...

1) I got some basic voxels working in OpenGL...
2) I need lots of special effects to make it "seem like energy"
3) I'm finding it hard working alone... and I need help...

...

So my questions are...

1) Let's say I DID use urho... would it impose "it's vision of how things should be" on me? For example... would it force me to use a "level design" approach like I see in those videos? My design isn't about loading up a "premade level" like in Quake3D or something... it's about "generating and throwing away stuff on demand"... so there isn't really any "level to design"...

2) Can I pretty much use what I already have and somehow have urho make it better? I like my engine's design so far... but I need special effects like "glow" or vibration etc...

3) Can anyone take an interest in my project and help me with this???

...

I also have long-term goals for my project but I'll ask that in separate post I think because or else it might distract from this post...

-------------------------

spacenoobs | 2017-01-02 01:07:25 UTC | #2

I got some pictures here... to help understand what I'm trying to do... and where I'm currently stuck at.

[jeebox.org/screens/](http://jeebox.org/screens/)

-------------------------

gwald | 2017-01-02 01:07:25 UTC | #3

Hi Welcome!
miserable? :open_mouth: 
1) No,  you can use U3D for low level stuff and use your own levels, logic etc... plus have the portability, networking, UI etc etc. 
2) Yes, special effects like "glow" or vibration etc.. have a look at youtube urho3d sample videos, u3d does glow/outlining the rest sounds like shaders
3) No, welcome to indie game dev... don't look at the negative side of working by yourself... look at the positives, nobody is more MOTIVATED to do your project then you.. 

IMO Games is the HARDEST software to program especially as a noob.. not to mention the art assets etc, for one person to do it all takes a lot... and if you're miserable now... may be getting people excited about your idea would help?, ie get a twitter, facebook, youtube and spam the masses getting a following.. if you're socially inclined.. 
Get a demo and get indie bloggers to write about you.. etc etc etc

I remember the indie game/mobile game craze was big years ago.. i don't know if it's died off

People are pretty good at helpful replies here, but if you need general 3d game dev help try :
[gamedev.stackexchange.com](http://gamedev.stackexchange.com)
[gamedev.net](http://gamedev.net)

If you are more professional, then [gamasutra.com](http://gamasutra.com) is for you.

Anyway.. not sure if I help you here. :unamused: 
Good luck

-------------------------

spacenoobs | 2017-01-02 01:07:25 UTC | #4

I think any questions about "how to make people interested in my work" is a big subject that unless you knew what I was doing... you could not know how big a subject it is... let's just say this discussion is too big to have here... and that I'm not doing anything like what anyone else is doing.

Technically it is the same, it Involves (amoungst other things) voxels and OpenGL. But the underlying motivation, energy, emotions... morality... implications, are entirely different.

Honestly I think I could only find the answers to my questions by trying... But it's such a big time investment on even trying... especially when there are about 20 different game engines I COULD try... and each one might take me an entire day to test properly... or more if I come across bugs... and get stuck and need help.

I think unless someone wants to take an interest in my work I really shouldn't start at all...

I COULD try U3D and "Get lucky" and maybe it does everything I want... or I could try it... and get unlucky... waste 3 days on trying to make it work... to find out it's incompatible with what I want... and be back to square 1... only to have to try this on the next 19 game engines...

That situation puts me really in a bind... if the "just find out if it does what I want or not" is so "expensive" and risky, time-wise for me.

[quote="gwald"]Hi Welcome!
2) Yes, special effects like "glow" or vibration etc.. have a look at youtube urho3d sample videos, u3d does glow/outlining the rest sounds like shaders
[/quote]

Yeah I know U3D does "glow"... and a whole load of amazing stuff...

-------------------------

gwald | 2017-01-02 01:07:25 UTC | #5

[quote="spacenoobs"]Technically it is the same, it Involves (amoungst other things) voxels and OpenGL. But the underlying motivation, energy, emotions... morality... implications, are entirely different.[/quote]
Your talking about the software's emotions or your emotions?  :confused: 
The underlying motivation of anything is in the 'eye of the beholder', it's all perspective.. we're all human but the act of game/software development isn't very philosophical, or so I thought anyway :open_mouth: 
The end result is mostly the same.. a twitch game, a 3d shooter, a text adventure etc etc. sure the stories are different but they play mostly the same..

And whether you should use a 3rd party package.. well that's like any other software package.. does it have features you need or are nice to have?, does it save you time? 
You're a pro-programmer, i'm sure you have a selection criteria for 3rd party products... you don't need to test all 3rd party tools out there... game engine's info pages are clear in what they can do and can't and how they are built.

Also, It's open source, your not trapped by any limitations, unlike closed source engines.
If the coding process is too hard, have you looked at unity3d.. It's like Visual basic, drag and drop and code a widget type of game dev.. I bash it a lot but it is sophisticated enough for many things.

-------------------------

spacenoobs | 2017-01-02 01:07:26 UTC | #6

[quote="gwald"][quote="spacenoobs"]Technically it is the same, it Involves (amoungst other things) voxels and OpenGL. But the underlying motivation, energy, emotions... morality... implications, are entirely different.[/quote]
Your talking about the software's emotions or your emotions?  :confused:
[/quote]

Funnily enough, both. Not that software has emotions... but what if... I designed a 9 dimensional concept system to deal with energy in terms of fundamental truths about reality that are ALWAYS TRUE in every Universe that could possibly exist? And then I took that concept system... and put it into a computer game. (it was on paper before)...

And when I say "Always true"... I mean always true... because they are built in terms of basic things that everyone can simply understand... (one of the 9 dimensions involves the concepts "creation", "movement", "destruction")... things that even if you play chess you can understand moving or destroying chess pieces... But somehow combine these basic concepts in sophisticated ways that creates a huge number of new possibilities that no one ever thought of before...

So yeah... what I want to do is supposed to be FUN... but it's also supposed to be about REALITY.

Really you shouldn't ask too many questions on this because it took me years to come up with all the ideas... it's impossible to understand without spending years yourself... eventually I found out that NO ONE wanted to learn my ideas... despite them being universally true... So I decided... "OK... no one wants to learn my ideas... so even if I made a website for people to read them... no one would learn them... and these ideas would die with me... so what if instead I just put these ideas into a computer program... that could one day become an artificial intelligence"...

:slight_smile:


[quote]And whether you should use a 3rd party package.. well that's like any other software package.. does it have features you need or are nice to have?, does it save you time? 
You're a pro-programmer, i'm sure you have a selection criteria for 3rd party products... you don't need to test all 3rd party tools out there... game engine's info pages are clear in what they can do and can't and how they are built.
[/quote]

OK so... I tested one engine already (not urho3D)... it looked great... but 1/2 of the basic demos crashed... on my Mac, including the ones that were more aimed at doing voxels. I'm not blaming the guy who made this... but still it wasn't a good start... Also even just compiling it in the first place took me a day, what with downloading stuff like CMake and trying to figure out why CMake isn't working... and then then basic hello world app took 3MB...



[quote]Also, It's open source, your not trapped by any limitations, unlike closed source engines.[/quote]

I wish that were true. But complexity in itself can be a trap...

-------------------------

gwald | 2017-01-02 01:07:26 UTC | #7

[quote="spacenoobs"]I wish that were true. But complexity in itself can be a trap...[/quote]
That's inherent with most code.. if that's your most important criteria then your own engine would be better.

[quote="spacenoobs"]OK so... I tested one engine already (not urho3D)... it looked great... but 1/2 of the basic demos crashed.[/quote]
Yip, most opensource projects are a 'work in progress' not a bad thing, if it's valued enough to fix issues and game dev is a good test of someones non work abilities.. cmake, android dev, C++, game logic, 3d maths, etc, etc.. everything is a challenge, that's why I suggested unity3D.. it removes the lower levels...



[quote="spacenoobs"]Really you shouldn't ask too many questions on this because it took me years to come up with all the ideas[/quote]
:slight_smile: if I were you, I would focus on that and then move it to graphics as stage two project, ie interface with text..  Have you seen Fa?ade on youtube?
Make it a text adventure.. the text adventure community isn't what it was in the 80's :frowning: but there's still a community!

I just found this:
[news.ucsc.edu/2015/06/game-finder.html](http://news.ucsc.edu/2015/06/game-finder.html)

Looks interesting and it works pretty well

-------------------------

spacenoobs | 2017-01-02 01:07:26 UTC | #8

I tried compiling Urho3D...

I got this error:

[quote]thsmith-air% cmake .
In file included from /Users/theodore/Downloads/Urho3D-1.4/Source/Urho3D/Precompiled.h:27:
In file included from /Users/theodore/Downloads/Urho3D-1.4/Source/Urho3D/Container/HashMap.h:25:
In file included from /Users/theodore/Downloads/Urho3D-1.4/Source/Urho3D/Container/../Container/HashBase.h:25:
In file included from /Users/theodore/Downloads/Urho3D-1.4/Source/Urho3D/Container/../Container/Allocator.h:25:
In file included from /Applications/Xcode.app/Contents/Developer/Toolchains/XcodeDefault.xctoolchain/usr/bin/../include/c++/v1/new:67:
/Applications/Xcode.app/Contents/Developer/Toolchains/XcodeDefault.xctoolchain/usr/bin/../include/c++/v1/__config:23:10: fatal error: 'unistd.h' file not found
#include <unistd.h>
         ^
1 error generated.
CMake Error at CMake/Modules/Urho3D-CMake-common.cmake:662 (message):
  The configured compiler toolchain in the build tree is not able to handle
  all the compiler flags required to build the project.  Please kindly update
  your compiler toolchain to its latest version.  If you are using MinGW then
  make sure it is MinGW-W64 instead of MinGW-W32 or TDM-GCC (Code::Blocks
  default).  However, if you think there is something wrong with the compiler
  flags being used then please file a bug report to the project devs.
Call Stack (most recent call first):
  CMake/Modules/Urho3D-CMake-common.cmake:718 (enable_pch)
  CMake/Modules/Urho3D-CMake-common.cmake:774 (setup_target)
  Source/Urho3D/CMakeLists.txt:174 (setup_library)


-- Configuring incomplete, errors occurred!
See also "/Users/theodore/Downloads/Urho3D-1.4/CMakeFiles/CMakeOutput.log".[/quote]

...

I definitely have unistd.h on my Mac... OSX installs at least 8 copies of the thing all over the place :slight_smile: No idea why this error is occuring.

-------------------------

spacenoobs | 2017-01-02 01:07:26 UTC | #9

[quote="gwald"][quote="spacenoobs"]I wish that were true. But complexity in itself can be a trap...[/quote]
That's inherent with most code.. if that's your most important criteria then your own engine would be better.
[/quote]

It would help if I could even get a single thing to learn from...

How can I learn if every demo I need to install has bugs and needs to spend a few days fixing it before I can even get started? Even Urho3D isn't "compiling straight out of the box"...

If I could just find a single demo that creates a glow effect and actually COMPILES on my Mac I could learn from it... but right now all I see is unrunnable code... Even the example on learnopengl.com won't run for me because I can't get glfw compiling or glitter working (Compiles but is incompatible with the code from learnopengl.com)

I'm not blaming them... but the situation with OpenGL is a total mess... I've heard many people say the situation with Microsoft DirectX is much better... because "Everything just works out of the box"...

I'm pretty sure the people from Urho3D or at least MOST of the people I've heard who learnt OpenGL... said they learnt from working tutorials or modifying existing projects... but I can't even get a working project to start from yet that has the basics I need like bloom effects.

-------------------------

weitjong | 2017-01-02 01:07:26 UTC | #10

I was not able to reproduce your problem after issuing "cmake ." on a freshly untarred 1.4 source file in my Mac OS X VM. The non out-of-source build tree was generated correctly in my VM, which indicates there may be some prerequisites required by Urho3D project that are not yet installed on your host system. I did not, however, continue to build the project using this build tree because we have never tested nor given such instruction in our documentation to configure/generate a build tree. Just in case you have not done so, you may want to have a read on these pages:
[urho3d.github.io/documentation/1 ... requisites](http://urho3d.github.io/documentation/1.4/_building.html#Building_Prerequisites)
[urho3d.github.io/documentation/1 ... ing_Native](http://urho3d.github.io/documentation/1.4/_building.html#Building_Native)
I would recommend you to follow the documentation to use one of the provided shell script (cmake_generic.sh for Makefile or cmake_macosx.sh for Xcode) to generate an out-of-source build tree for building the Urho3D project. Or use cmake-gui to guide you through it. Good luck.

-------------------------

rasteron | 2017-01-02 01:07:26 UTC | #11

[quote]If I could just find a single demo that creates a glow effect and actually COMPILES on my Mac I could learn from it... but right now all I see is unrunnable code... Even the example on learnopengl.com won't run for me because I can't get glfw compiling or glitter working (Compiles but is incompatible with the code from learnopengl.com)[/quote]

Hey, spacenoobs. If you're looking for that particular Glow effect there is one really good here, apparently it was buried beneath the discussions (I should probably do the honors and create a separate thread for reference). This is [b][url=http://discourse.urho3d.io/t/solved-how-to-create-int-rt-with-twice-smaller/1366/9]CodingMonkey's Object Glow Solution[/url][/b] and hey! it's in GLSL :wink:

[img]http://savepic.su/6124090m.jpg[/img]

[video]https://www.youtube.com/watch?v=tRxgS1A1ehg#t=16[/video]

Now compile that OS X build and get that thing started! Good Luck!  :slight_smile:

-------------------------

spacenoobs | 2017-01-02 01:07:27 UTC | #12

Thanks for the replies...

For the moment I think I'll try struggling along by myself and with tutorials... I DID get some blur working but that's not yet a proper "bloom" effect...

After that... my plan is to try to get Urho3D installed and working and either use it... or learn from it... Even if it's "not what I need" I think it could be good to learn from. I may end up learning that it is what I need... so either way that's great.

So yeah for now... the fact that Urho3D doesn't compile on my Mac isn't an issue... Maybe when I check back on Urho3D in a week or so... it will magically start workign by itself so that's fine :slight_smile:

-------------------------

jmiller | 2017-01-02 01:07:29 UTC | #13

Hi [b]spacenoobs[/b]

You might find the [url=https://github.com/urho3d/Urho3D]current master branch at GitHub[/url] works better for you. Many of us use it exclusively, Urho sees frequent improvements, and breakage (afaics) has been almost nonexistent.

Seems many have been pleased at how quick they pick up Urho, and found the samples really instructive.

For the master branch, of course, most of the docs pages refer to /HEAD/
[urho3d.github.io/documentation/HEAD/index.html](http://urho3d.github.io/documentation/HEAD/index.html)

As far as searching the forum, the word filter is restrictive, so you might use a custom site search
[code]https://www.google.com/search?q=%s+site%3Aurho3d.prophpbb.com[/code]

Bloom is demo'd in Samples/09_MultipleViewports.cpp and Data/Scripts/09_MultipleViewports.as
You'll find the effects in Data/PostProcess.

-------------------------

