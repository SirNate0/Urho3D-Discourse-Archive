Eugene | 2019-05-30 07:13:14 UTC | #1

I am working on Qt-based Editor for Urho.

WIP

[details=Initial content of topic]
I've seen here several threads about Urho Editor. I've even started one.
I think that Editor needs tighter integration with game code.
Sometimes I even feel a passion to improve something here, but I don't want to start without way, milestones and goals.
[b]@cadaver[/b], do you have some strong opition about Editor developement or just good ideas?

Now I can imagine three ways of Urho usage:
1) Custom app that uses Urho as library.
2) Custom script that uses Urho player (probably extended with custom objects)
3) Playable scene that contain all game logic inside scripts like Unity (probably extended with custom objects), with minimal entrypoint script/application
Changes in Editor depends on that how many ways we want to cover.

I have bucket of different ideas and thoughts (mine and others')
- Migrate Editor to C++. Partially or completely? Will it give any benefits? It looks like hard job. (optionally covers 1,2)
- Allow Editor to be called from custom game script. Full or limited editor? How to make interaction? (covers 2, optionally covers 1)
- Allow custom game script to be called from Editor. What limitations? How to implement interaction? (covers 2)
- Add standalone play of 'playable scene'. It's simple, but it don't cover 2-nd way. It's enough for me, but what about others?.. (covers 3)
- Just do nothing and let Editor be temporary utility untill user write his own ingame editor with bj&hs. (covers nothing ?\_(?)_/?)

I don't promise that I'll start work immediatelly or that it will be high-priority task for me.
However, let's discuss at least.

My final goal is to have something like this:

https://www.youtube.com/watch?v=wF_19xIfiGo

Now it is hacky and buggy, with almost untouched Editor code. And I hate hack and bugs, do u 'now?
[/details]

-------------------------

cadaver | 2017-01-02 01:15:16 UTC | #2

My view is that the existing editor is somewhere halfway between a complex script API usage example, and a production-usable editor. Many have contributed to it and the code structure is not best. Because of Urho's nature of "singleton" subsystems it will be hard to achieve calling into the editor from game, or vice versa.

Your analysis is quite spot on that Urho can be used in many ways and therefore it's not obvious how the editor and game could talk to in all the scenarios. 

Probably the ideal would be, if you wanted to improve the user experience at the same time, would be to use an actual native UI toolkit in the editor and rewrite it in C++. Otherwise you're always going to be struggling with both the editor and game taking over Urho's subsystems. How this would work best when appended to users' projects is another largish question. Perhaps the editor could be another library, which adds functionality into Urho base (for example, it registers an Editor subsystem as it starts up)

A lot of smaller-scale engines actually launch a separate exe for the game from within the editor, though in that case you can forget the editor and the game talking.

I don't have hard / fast opinions on how you should proceed. If you have passion, go for it. However to be realist, or slightly pessimist, you should be ready to do (most of) the work on your own. Many projects fizzle out because they're expecting a collaboration to form, and that then doesn't happen.

-------------------------

NiteLordz | 2017-01-02 01:15:16 UTC | #3

What i have done, is using Qt for the UI, i have multiple dock widget/windows that i can move around.  I create one context at startup for the editor, and one context for the "Game" window.  When the user clicks on the "play" button, the active scene is saved/cached to a seperate file, which the game context then loads.  This allows to "play" the game, within the editor.  

I am moving my editor from VSTS to github within the next week, if anyone is interested to see how it works.  

It requires Qt 5.6, and currently only runs on Windows and 32-Bit, but that is only because i have not created the project for 64-Bit yet.

-------------------------

Lumak | 2017-01-02 01:15:26 UTC | #4

I know how tough it'll be to port the editor to c++.  If you can create a repo for it, perhaps, I can contribute.

-------------------------

dakilla | 2017-01-02 01:15:26 UTC | #5

it could be a nice community project.
+1 for Qt, I have a good experience using it and urho :p

-------------------------

Eugene | 2017-01-02 01:15:33 UTC | #6

I have only one reason against Qt: It is not lightweight at all, it have much more that is needed for Urho Editor.

-------------------------

TheSHEEEP | 2017-01-02 01:15:33 UTC | #7

[quote="Eugene"]I have only one reason against Qt: It is not lightweight at all, it have much more that is needed for Urho Editor.[/quote]
While that is true... who cares?
Honestly, application/download size is a problem of the past, at least in non-mobile environments. And nobody is going to distribute the editor to mobile :wink:
Besides, while Qt has much more than any single application will ever use, it is nicely split into modules/shared libraries. When packaging a Qt app, only used parts will be packaged with it (automatically).

It does increase the complexity of building Urho3D, though, so I'd at least keep the editor optional.

The pros far outweigh the cons with Qt.
For example, I could imagine making changes to the editor for a project at hand to distribute the editor with the application.
The current editor.... it is just not something you'd give into the hands of an end user. It's just too rough, and not even nowhere similar to editors people are used to like Unity, Maya, etc.
So currently, if I wanted to distribute an editor with an application using Urho3D, I'd have to build it myself - which I'd most likely do using Qt, since - well, there is no alternative reaching its quality, not cross-platform, anyway.
Just having to adjust an existing editor for my needs would save [b]much [/b]time.

-------------------------

Eugene | 2017-01-02 01:15:33 UTC | #8

Ok, I am just almost unfamiliar with Qt.
If somebody is ready to start and/or share some code of Qt Urho Editor, I will contribute.
It is unlikely that I'll start creating Editor in Qt on my own in the nearest future.
Probably, we will also need some assistance from our buildsystem guru...

-------------------------

cadaver | 2017-01-02 01:15:33 UTC | #9

I believe to have commented this before, but it doesn't hurt to reiterate.

If the editor is a separate project, using Qt fits very well. You'd only need solid setup instructions per platform, and the user could build or download Qt themselves and just ensure it's available for the project's CMake. Very likely you'd only ever use Qt + editor on desktops in that case.

As part of Urho repo or build itself, we have quite strong principles of automatic dependency build (and even including them in the source repo, since everything used so far is small). There Qt doesn't fit that well, or would require much more ninja magic.

-------------------------

Eugene | 2017-01-02 01:15:33 UTC | #10

Huh... I am in doubt.

Qt:
+ Really powerful
- Heavy
- Harder to use with executable project
- Separate repo is worse than builtin
- I am not familiar with it

Editor library:
+ Builtin, easy to use
+ Can be injected into existing executable project
- Lack of functionality. Urho's UI is powerful enough for games, but not for editor.
- Looks like a kludge

Now I like Qt way more...
Can somebody of Qt guys share some code?

-------------------------

rasteron | 2017-01-02 01:15:34 UTC | #11

You can check out aster's 2D Particle Editor here: [github.com/aster2013/ParticleEditor2D](https://github.com/aster2013/ParticleEditor2D)

uses Qt4 and I would assume you're going to use Qt5, but still this is a good reference to start with.

-------------------------

TheSHEEEP | 2017-01-02 01:15:34 UTC | #12

[quote="cadaver"]I believe to have commented this before, but it doesn't hurt to reiterate.

If the editor is a separate project, using Qt fits very well. You'd only need solid setup instructions per platform, and the user could build or download Qt themselves and just ensure it's available for the project's CMake. Very likely you'd only ever use Qt + editor on desktops in that case.

As part of Urho repo or build itself, we have quite strong principles of automatic dependency build (and even including them in the source repo, since everything used so far is small). There Qt doesn't fit that well, or would require much more ninja magic.[/quote]
Fully agree, Qt does not really fit with the dependencies so far. And it shouldn't, IMO. I don't think the editor should necessarily be built when you build Urho3D.
What I would probably do (and I don't say that I will, because I honestly do not have the time, this is just my developer experience speaking) is to create a separate repo just for the editor. The project structure I'd do as a Qt project (no CMake at all, since it is not required in this case and Qt is cross-platform already and free). Inside that project I would link against Urho3D, which would have to be put into a specific sub-directory of the project (so the user would have to put the binaries there himself, or it could be automated to a degree, even by Qt itself).
That would mean a complete and clean separation between Urho3D and its editor. So the editor would "just" be an application using Urho3D that happens to be using Qt.

[quote="Eugene"]- Harder to use with executable project[/quote]
Not sure what you mean with that.
Do you mean the ability to have an editor built-in with every project that uses Urho3D? I don't think that would be a good idea. Such a built-in editor could never be as powerful as an "external" one. I think there is no example of a well-done built-in editor that comes with an engine, but there are countless examples of truly great external editors (just look at Starcraft 2 or Warcraft 3).
 
[quote="Eugene"]- Separate repo is worse than builtin[/quote]
How so?
I would even say it is an important separation to make as they are simply different projects where only one depends on the other.
Urho3D could be developed mostly ignorant of its own editor, which IMO is a boon as it allows more focused development. And the editor could be developed "ignorant" of Urho3D's development (other than adjusting to eventual breaking changes).

-------------------------

Eugene | 2017-01-02 01:15:34 UTC | #13

[quote]Not sure what you mean with that.[/quote]
Exactly that you said.

[quote]How so?[/quote]
Huh. I mean, from the developer's point of view separate repo is more clean way..
But it would be harder for newcomers to build Editor...

-------------------------

Victor | 2017-01-02 01:15:34 UTC | #14

One purpose I feel the editor solves very well, for me at least, is how to use Urho's UI to do various things. It's essentially an advanced example. One thing to keep in mind as well, is that someone will have to maintain the editor for a very long time if you switch to Qt. I believe using Urho's UI makes this task (maintenance) a bit easier.

I do, however, think the editor in C++, rather than AngelScript, is a great idea. At the end of the day however, I see cadaver as being the person who would have to shoulder the burden of maintaining the editor, so it should be done in a way that would make that burden lighter for him.

My proposal, is to take more of a plugin approach; where most features/extensions of the editor is built as a linked lib or script (giving both possible choices on how to create a new feature). This way, a really cool feature by some random person can be versioned, and when it's not supported anymore it won't take down the entire editor. This may make the burden on cadaver (and not just cadaver but any main maintainers of Urho) lighter.

-------------------------

Eugene | 2017-01-02 01:15:34 UTC | #15

IMO plugins is the most important thing that our Editor needs.

[quote]it should be done in a way that would make that burden lighter for him.[/quote]
Unfortunatelly, it's pretty hard to simplify current AS Editor AND reuse the same code in Qt Editor because editor is mostly UI and we can't re-use code for UI.

-------------------------

TheSHEEEP | 2017-01-02 01:15:34 UTC | #16

[quote="Victor"]One purpose I feel the editor solves very well, for me at least, is how to use Urho's UI to do various things. It's essentially an advanced example.[/quote]
That's true. And I like the UI as it enables a user to get started rather quickly.
It's big downside is scope, though. It can't (and IMO wasn't designed to) and shouldn't compete with top-notch UIs out there, like Scaleform/Noesis/CEGUI*/etc. (I'll be using libcef personally).
For example, if you need a UI that scales perfectly with resolution, you'll have to look at alternatives. Which is pretty much mandatory IMO for non-mobile games if you don't want to subject users to weird scaling issues.

[quote="Victor"]At the end of the day however, I see cadaver as being the person who would have to shoulder the burden of maintaining the editor, so it should be done in a way that would make that burden lighter for him.[/quote]
I'm not fully convinced of that. I mean, most of my experience in open source development comes from Ogre, but there different people were responsible for different aspects.
And since cadaver has developed such a great tool and is no doubt the driving force here so far, I would love him to be able to focus on the core of Urho3D. Which I do not consider the editor to be a part of.
For me, an editor would be a perfect project if another person wanted to contribute to Urho3D in a more long-time fashion :slight_smile:

Which is why I wouldn't do any major changes to the editor, actually, before someone doesn't say "Yup, I'll do this!".
I'd love to do it, I know Qt rather well and like working with it. And it would also be a perfect way of getting to know Urho3D better before starting with my project (which will begin in ~1.5 years).
But I just don't have the time for such a commitment :frowning:



[size=85]*admittedly, calling CEGUI top-notch is a bit of a stretch.[/size]

-------------------------

Victor | 2017-01-02 01:15:34 UTC | #17

[quote="TheSHEEEP"]
That's true. And I like the UI as it enables a user to get started rather quickly.
It's big downside is scope, though. It can't (and IMO wasn't designed to) and shouldn't compete with top-notch UIs out there, like Scaleform/Noesis/CEGUI*/etc. (I'll be using libcef personally).
For example, if you need a UI that scales perfectly with resolution, you'll have to look at alternatives.[/quote]

I can agree with this, and you're right.

One other concern, I think, would be licensing. Perhaps someone wants to deploy their game with a modified version of the editor. How would Qt effect this? Would they have to rewrite their own editor to remove all of the Qt elements. Would wxWidgets be any better? And does statically linking your library effect this process as well with Qt (or wxWidgets)?

-------------------------

TheSHEEEP | 2017-01-02 01:15:34 UTC | #18

Qt comes in both GPL (which I'd never choose, and there is no reason to) and LGPL (which is the one you can use for open-source and closed source/commercial both).

I am not a lawyer, but the general consensus for LGPL is that as long as you link dynamically, don't modify the source code, don't rename the lib files, put the license somewhere* and (some say this is mandatory, most say it isn't) make the source code [b]of the LGPL-licensed software[/b] (so [i]not your[/i] software) available somewhere, you are fine.
It really is not much to do and almost every software that does anything with audio/video manipulation does that for FFmpeg, for example.
Besides, this wouldn't even affect the editor in Urho3D since that would be open source anyway.

wxWidgets has some very weird kind of custom license, which seems to be a more permissive variant of LGPL allowing you to modify its source code as well.
But I see no reason to use wxWidgets. It isn't exactly lightweight, either and not as versatile as Qt. And it doesn't have an editor that could rival Qt Creator even nearly.
I tried working with wxWidgets before, more than once. But it always ended with hitting some brick wall that doesn't exist in Qt...

The only reason not to use Qt would be if someone wanted to have everything (including Qt) statically linked for the editor.
But why would anyone want that? To hide from other programmers that he did not write an entire interface library for every platform himself? :smiley:

[size=85]*You know, those "license" buttons in software that nobody really clicks on? Like that :wink:[/size]

-------------------------

Victor | 2017-01-02 01:15:35 UTC | #19

[quote="TheSHEEEP"]To hide from other programmers that he did not write an entire interface library for every platform himself? :smiley:[/quote]

So far, Urho has done so well with choosing libraries that are great for other people/companies. I work on a lot of projects that are NDA-bound, and license is a real concern. Like you said yourself, they would never choose GPL... I've also had a friend ask me to recommend a game engine her team could use, (she works at IBM in the R&D dept... they do crazy things heh). I recommended Urho because of the license and the light-weight nature of it.

Now, I'm honestly not sure of the "correct" direction for the editor. Maybe this will just be a community thing and not part of the official Urho repo; but if the editor were to change (officially), I believe careful thought would need to be taken. Any direction would have long-term consequences to the future of Urho (I hope I'm not being too dramatic).

I just want to make sure all of the questions and concerns, especially the long-term consequences, have been considered.

-------------------------

TheSHEEEP | 2017-01-02 01:15:35 UTC | #20

Well, the truth is that many people are afraid of LGPL for no real reason. All it requires you to do is acknowledge the tools/libs you are using. 
You don't have to share your own code at all.
You can still be secretive and earn money :wink:
I don't think that is too much to ask, not from anyone, NDA or not.

And I especially don't think open source software should try to specifically cater to closed-source needs.

But yes, as said before, I think the editor (if being rewritten in whatever way) should be its own, separate project.
But the current one should probably stay as a good example for the UI.

-------------------------

boberfly | 2017-01-02 01:15:36 UTC | #21

Not sure if you guys know about this or not, but the Wargaming guys released a nice editor framework based on Qt5:
[url]https://github.com/wgsyd/wgtf[/url]
Might make things easier to make this talk to Urho3D.

-------------------------

Eugene | 2017-01-02 01:15:36 UTC | #22

[quote="boberfly"]Not sure if you guys know about this or not, but the Wargaming guys released a nice editor framework based on Qt5:
[url]https://github.com/wgsyd/wgtf[/url]
Might make things easier to make this talk to Urho3D.[/quote]
I heard some bad words about their code quality from one ex-employee, sooo...
Questionable.

-------------------------

boberfly | 2017-01-02 01:15:37 UTC | #23

[quote="Eugene"][quote="boberfly"]Not sure if you guys know about this or not, but the Wargaming guys released a nice editor framework based on Qt5:
[url]https://github.com/wgsyd/wgtf[/url]
Might make things easier to make this talk to Urho3D.[/quote]
I heard some bad words about their code quality from one ex-employee, sooo...
Questionable.[/quote]
This is from the Sydney branch, looking at the code it's pretty clean enough and pretty much an empty shell with Qt5 + Python bindings. A friend of mine who works there tipped me off about it.

-------------------------

Eugene | 2017-01-02 01:15:37 UTC | #24

BTW, I started. I'll share my work when I have relatively stable architecture and some basic functions.

[quote]This is from the Sydney branch[/quote]
It explains a lot. That guy was from Moscow branch.

-------------------------

xDarkShadowKnightx | 2017-01-02 01:15:41 UTC | #25

A new editor wrote from scratch would be awesome. Is anyone against using Lua, and making it more modular / plugin based? The current editor defines a lot of global variables, which makes name conflicts more probable, and it can make tracking down things more difficult. Especially considering the code base size. And one could argue that Lua is more popular then AngelScript, considering its age and usage through out the industry. So using Lua may make contributing to the editor easier for those who haven't spent the time to learn AngelScript, but have used Lua in the past (or even Javascript). I would be willing to help / lead a rewrite in Lua. Especially since I've switched back to Urho3D from Unity due to bugs with the Unity editor on Linux.

-------------------------

cadaver | 2017-01-02 01:15:42 UTC | #26

Lua as it is in Urho currently has some problems in memory management; I personally would not recommend it over AngelScript. And using C++ still gains you better debugging possibilities, as well as performance.

-------------------------

xDarkShadowKnightx | 2017-01-02 01:15:42 UTC | #27

If C++ were to be used, I could see it being exposed to the scripting engines so that people writing games in Lua or AngelScript can make use of the editors pre-built functionality.

The issue I see with this is adding easy support for plugins to the Editor. I can see three options:

- Dynamically load plugins as shared libraries at runtime. This is probably the best option. But will make authoring of plugins only available to those with knowledge of C++

- Compile the plugin into the editor. This is less ideal. Since artists who may find a cool plugin that they want to use, would have to compile the editor (which they may not know how to do)

- The core of the editor is wrote in C++, and we add plugin support via Lua / AngelScript. This is less ideal if say, someone wants to make use of the editor functionality in their Lua based game, but want to load in a plugin wrote in AngelScript (we would have to have both scripting languages running)

I'm thinking the dynamic C++ option would be best. But it's going to make it harder for artists, who may only have basic knowledge of Lua / AngelScript, to create plugins for the editor that suit their needs.

-------------------------

rku | 2017-01-02 01:15:44 UTC | #28

Sounds like games could be made only by artists without any programming knowledge which obviously is not true. What you suggest is another gamemaker or unity. To me Urho3D is appealing precisely because it is not gamemaker or unity and because it does not hide innards from me.

My dream would be to have a "libEditor". Imagine you are presented with premade components, scene tree window for example. You manually have to rig your game to call that window but then it would allow you interacting with your scene inside your game. You could hook into various actions of saving/loading/manipulating scene. Now imagine every other component is like that. Imagine you could change model material of character that is passing by in your scene. Essentially it would turn game into editor your game needs. However i do realize this will work for some things and will be totally unfeasible for others. Just like making editor to be usable by non-artists for making entire games. On the other hand if there was such "libEditor" to exist and it was pluggable to the game while actual editor would be based on said lib it could allow some pretty neat flexibility for developers.

-------------------------

Victor | 2017-01-02 01:15:44 UTC | #29

[quote="rku"]Sounds like games could be made only by artists without any programming knowledge which obviously is not true. What you suggest is another gamemaker or unity. To me Urho3D is appealing precisely because it is not gamemaker or unity and because it does not hide innards from me.

My dream would be to have a "libEditor". Imagine you are presented with premade components, scene tree window for example. You manually have to rig your game to call that window but then it would allow you interacting with your scene inside your game. You could hook into various actions of saving/loading/manipulating scene. Now imagine every other component is like that. Imagine you could change model material of character that is passing by in your scene. Essentially it would turn game into editor your game needs. However i do realize this will work for some things and will be totally unfeasible for others. Just like making editor to be usable by non-artists for making entire games. On the other hand if there was such "libEditor" to exist and it was pluggable to the game while actual editor would be based on said lib it could allow some pretty neat flexibility for developers.[/quote]

I agree that Urho3D is appealing because it's not gamemaker, although I'd say that after coming from Unity (I cannot speak for GameMaker), most of my work was programming with nearly nothing done in the editor. Unity is very flexible when it comes to writing procedural code. Urho, for me, was appealing because my development workflow didn't change from Unity to Urho. This goes for UE4 as well. In my little time with UE4, I tried my best to avoid Blueprints as it wasn't appealing to me. I do believe a great editor can exist without disrupting the workflow of a programmer. :slight_smile: But yeah, I totally get your concern! The editor shouldn't be needed to build a game.

-------------------------

Eugene | 2017-01-02 01:15:46 UTC | #30

Huh... It is harder than I imagined. Anyway, this is not a reason to stop.

-------------------------

godan | 2017-01-02 01:15:47 UTC | #31

[quote]Sounds like games could be made only by artists without any programming knowledge which obviously is not true. What you suggest is another gamemaker or unity. To me Urho3D is appealing precisely because it is not gamemaker or unity and because it does not hide innards from me.[/quote]

While I absolutely agree that you can't create a full game without coding, I think that a well-designed editor can help iterate logic, mechanics, gameplay, visuals, etc way faster that tweaking values in code. More generally, it is often very difficult to get that initial spark of inspiration when faced with only code. That said, I actually don't think that the traditional game engine editor UI is the best way to do this. Such editors help to set up a scene and perhaps expose some parameters of the components, but they don't help the user to make that leap from having a bunch of great assets to having an engaging game world.

All this is to say 1) having a great editor for Urho would ABSOLUTELY increase its value (not necessarily in a monetary sense - rather in the sense of the value that it gives the users), and 2) Given the incredible base on which to build (i.e. the Urho source code), it might be worth trying to envision an equally innovative editor.

I've actually tried to implement a bunch of the above in iogram ([url=http://steamcommunity.com/sharedfiles/filedetails/?id=817377895][1][/url], [url=https://www.youtube.com/watch?v=PHGmLw2BY_E&t=8s][2][/url], [url=http://iogram.ca/][3][/url]), and I would love to see iogram become a more general tool for Urho users. Not sure how others feel about that, though. Also, I've posted a lot about iogram - I'm not trying to spam the thread :slight_smile:! I just think it is a relevant bit of work on game/3d editor UI.

-------------------------

Eugene | 2017-01-04 19:38:56 UTC | #32

Okay, first steps are made. However, it is still absolutely unusable.
It would be more fair to call him 'Urho3D scene viewer'
However, it already can into multiple tabs and huge scenes.
<img src="//cdck-file-uploads-global.s3.dualstack.us-west-2.amazonaws.com/standard17/uploads/urho3d/original/1X/82cf84dd2a9ab01ac26a8a0b87d9b1e53e7ebd1d.png" width="690" height="387">

-------------------------

cadaver | 2017-01-04 20:05:59 UTC | #33

Looks good!

As long as you don't need to composite Qt UI widgets in software on top of the Urho 3D view through a (potentially per-frame) GPU texture upload, I believe you'll be fine :) Thinking of it, probably all those kind of cases can be handled with Urho-native objects, Text3D, debug geometry, debug meshes and such.

The reason why I'm even mentioning that, is just some war trauma from https://github.com/realxtend/tundra :)

-------------------------

Eugene | 2017-01-16 23:01:15 UTC | #34

Migrated Camera ang Gizmo logic as precise as possible.
Implemented configurable main menu layout.
Added undo/redo stack.
Added multiple viewports support, without margins for now.
Added auto-generated options dialog.
Editing gizmo with keyboard also creates undo action (original Editor miss it)
<img src="//cdck-file-uploads-global.s3.dualstack.us-west-2.amazonaws.com/standard17/uploads/urho3d/original/1X/1ba172aa6924e01380be5489070d00588f26e6a3.png" width="690" height="387">

-------------------------

TheSHEEEP | 2017-01-17 08:31:32 UTC | #35

Well, that looks pretty good indeed.
Are you using qss stylesheets for styling? It is what I would recommend since it is the most scalable and easily extendable solution. And almost as powerful as real css.

@cadaver Displaying something on top of a GraphicsScene is not much of an issue in Qt. IIRC correctly, it is as easy as adding a widget to the same GraphicsScene/View.
Ah, yeah, here is the update from Qt 4.4: 
>  Qt 4.4 introduced a powerful feature to allow any QWidget subclass to be put into QGraphicsView. It is now possible to embed ordinary widgets in a QGLWidget, a feature that has been missing in Qt's OpenGL support for some time.

Mind you, that was years ago and now we have Qt 5.7 (at least that's what I'm currently using in another project), so it really shouldn't be a problem.

-------------------------

Eugene | 2017-01-17 09:04:24 UTC | #36

Yep, I use QDarkStyle stylesheet.

-------------------------

rku | 2017-01-17 13:14:25 UTC | #37

This is awesome. Is code on public repo yet?

-------------------------

Eugene | 2017-01-17 18:31:31 UTC | #38

Yep. Surprisingly, there are some Urho users who've already found it on Github.

However, I am _not_ going to share this repo, make docs, answer questions, support or provide any guarentees _until_ I make this Editor minimally usable (=until I start use it for my own project).

I started from scratch month ago. Estimated time for sharing zero-point-one version is several months.

-------------------------

rku | 2017-01-17 18:44:23 UTC | #39

Not that its hard to find.. ;) Besides whats so bad if some people want to stalk the progress? :p

-------------------------

Eugene | 2017-01-17 18:58:20 UTC | #40

I think anybody sometimes have thoughts deep in mind like _My code is so ugly so I don't want anybody to see it_

-------------------------

TheSHEEEP | 2017-01-18 12:36:45 UTC | #41

I never write ugly code ;)

-------------------------

Modanung | 2017-01-18 13:23:40 UTC | #42

>“Beauty lies in the eyes of the beholder”
>― Plato

;)

-------------------------

rku | 2017-01-18 14:22:46 UTC | #43

@Eugene since you are doing something noone else is doing that should already count for something right? Besides you show me your code, i come and say how ugly and bad it is, then someone else comes and says about me being wrong and we all learn. ;)

-------------------------

Eugene | 2017-02-06 21:41:40 UTC | #44

- Added basic editing operations (Cut/Copy/Paste/Delete/Duplicate) and corresponding undo/redo actions.
- Added basic hierarchy operations (re-parenting and re-ordering via drag&drop) and corresponding undo/redo actions.
- Hierarchy window correctly handles such updates now.

-------------------------

Eugene | 2017-02-19 10:23:14 UTC | #45

<img src="//cdck-file-uploads-global.s3.dualstack.us-west-2.amazonaws.com/standard17/uploads/urho3d/original/1X/080e5e80556c586b0015df5434fbbe7a36f64a28.png" width="690" height="387">
I've migrated some part of Editor code into C++ && Qt.
Now I see some disadvantages of native UI framework like Qt:

- Only one 3D view for single Urho3D instance. Some small preview windows like in Resource Browser or Material Editor will now require launcing sepearte Urho3D Application.
- Somewhy Urho3D widget cannot process key events on its own. Unsure whether it is a problem in Qt, SDL or my hands.
- Interaction between native UI and Urho is not very smooth. E.g. when I change position via AI using mouse, it is noticeable that node moves 'laggy'.

Now I think that some non-native framework may be better than native.
It shan't be very hard to migrate between UI frameworks since most of my effort was spent on decomposition Editor code and migration to C++.

Does anybody have any thoughts about it?
Maybe one can suggest something.

-------------------------

1vanK | 2017-02-19 11:06:02 UTC | #46

I seems unity uses multiple views for editor (tested by Fraps) and they redraw only when need (digit is fps)

<img src="//cdck-file-uploads-global.s3.dualstack.us-west-2.amazonaws.com/standard17/uploads/urho3d/original/1X/76b7dbd73af7720e91ec119bbfe996f5483d24e9.png" width="690" height="386">

-------------------------

hdunderscore | 2017-02-19 11:17:06 UTC | #47

[quote="Eugene, post:45, topic:2407"]
Only one 3D view for single Urho3D instance. Some small preview windows like in Resource Browser or Material Editor will now require launcing sepearte Urho3D Application.
[/quote]
In worst case scenario, if every view needs it's own Urho3D instance, that still seems ok to me. Urho is pretty light weight, and for most of the views, a reduced Urho build could be used.

[quote="Eugene, post:45, topic:2407"]
Interaction between native UI and Urho is not very smooth. E.g. when I change position via AI using mouse, it is noticeable that node moves 'laggy'.
[/quote]
How much is the delay? It's not a matter of urho's inactive fps?

I'm not sure those issues are big enough to change path.

-------------------------

1vanK | 2017-02-19 11:23:56 UTC | #48

<img src="//cdck-file-uploads-global.s3.dualstack.us-west-2.amazonaws.com/standard17/uploads/urho3d/original/1X/b5e9f377b6be95834418d9838ae57b3aeda9c4fc.png" width="690" height="404">

-------------------------

Eugene | 2017-02-19 11:59:33 UTC | #49

@1vanK Note that both exmples use non-native UI. Blender use it everywhere, Unity is probably keep native toolbar and menu, 

[quote="hdunderscore, post:47, topic:2407"]
I'm not sure those issues are big enough to change path.
[/quote]

I am too.

-------------------------

1vanK | 2017-02-19 14:18:50 UTC | #50

Yes, I pay attention that they updates not with 60 fps, but only when it is need (ui not required ofter redrawing)

-------------------------

TheSHEEEP | 2017-02-20 06:21:49 UTC | #51

> Only one 3D view for single Urho3D instance. Some small preview windows like in Resource Browser or Material Editor will now require launcing sepearte Urho3D Application.

Why do you want to use Urho3D for a Resource Browser? Isn't that just a view of files easier done in Qt anyway?
A Material Editor using Urho3D to display the result would be neat, indeed. But outside of displaying the result, I'm not sure such an editor wouldn't be better done in Qt.

Either way, as others have pointed out, it is normal in editors to have multiple views/windows each running an instance of some kind of 3D display.
No real way around it, I think. And I agree that it wouldn't be too much of a performance issue. After all, most of them will be inactive most of the time (aka not updating).

-------------------------

dakilla | 2017-02-20 08:15:12 UTC | #52

[quote="Eugene, post:45, topic:2407"]
Somewhy Urho3D widget cannot process key events on its own. Unsure whether it is a problem in Qt, SDL or my hands.
[/quote]

I my Urho Qt Widget I managed key events in this way : 

         //------------------------------------------------------------------------------------------------------
        // key utilities to convert Qt key to SDL key
        //------------------------------------------------------------------------------------------------------
        static QMap<Qt::Key, SDL_Keycode> __keymap;
        static void __initKeyMap();
        static Uint16 __convertQtKeyModifierToSDL(Qt::KeyboardModifiers qtKeyModifiers);
        static SDL_Keycode __convertQtKeyToSDL(Qt::Key qtKey);

        //------------------------------------------------------------------------------------------------------
        // map keys Qt/SDL
        //------------------------------------------------------------------------------------------------------
        void __initKeyMap()
        {
            __keymap[Qt::Key_unknown]     = SDLK_UNKNOWN;
            __keymap[Qt::Key_Escape]      = SDLK_ESCAPE;
            __keymap[Qt::Key_Tab]         = SDLK_TAB;
            __keymap[Qt::Key_Backspace]   = SDLK_BACKSPACE;
            __keymap[Qt::Key_Return]      = SDLK_RETURN;
            __keymap[Qt::Key_Enter]       = SDLK_KP_ENTER;
            __keymap[Qt::Key_Insert]      = SDLK_INSERT;
            __keymap[Qt::Key_Delete]      = SDLK_DELETE;
            __keymap[Qt::Key_Pause]       = SDLK_PAUSE;
            __keymap[Qt::Key_Print]       = SDLK_PRINTSCREEN;
            __keymap[Qt::Key_SysReq]      = SDLK_SYSREQ;
            __keymap[Qt::Key_Home]        = SDLK_HOME;
            __keymap[Qt::Key_End]         = SDLK_END;
            __keymap[Qt::Key_Left]        = SDLK_LEFT;
            __keymap[Qt::Key_Right]       = SDLK_RIGHT;
            __keymap[Qt::Key_Up]          = SDLK_UP;
            __keymap[Qt::Key_Down]        = SDLK_DOWN;
            __keymap[Qt::Key_PageUp]      = SDLK_PAGEUP;
            __keymap[Qt::Key_PageDown]    = SDLK_PAGEDOWN;
            __keymap[Qt::Key_Shift]       = SDLK_LSHIFT;
            __keymap[Qt::Key_Control]     = SDLK_LCTRL;
            __keymap[Qt::Key_Alt]         = SDLK_LALT;
            __keymap[Qt::Key_CapsLock]    = SDLK_CAPSLOCK;
            __keymap[Qt::Key_NumLock]     = SDLK_NUMLOCKCLEAR;
            __keymap[Qt::Key_ScrollLock]  = SDLK_SCROLLLOCK;
            __keymap[Qt::Key_F1]          = SDLK_F1;
            __keymap[Qt::Key_F2]          = SDLK_F2;
            __keymap[Qt::Key_F3]          = SDLK_F3;
            __keymap[Qt::Key_F4]          = SDLK_F4;
            __keymap[Qt::Key_F5]          = SDLK_F5;
            __keymap[Qt::Key_F6]          = SDLK_F6;
            __keymap[Qt::Key_F7]          = SDLK_F7;
            __keymap[Qt::Key_F8]          = SDLK_F8;
            __keymap[Qt::Key_F9]          = SDLK_F9;
            __keymap[Qt::Key_F10]         = SDLK_F10;
            __keymap[Qt::Key_F11]         = SDLK_F11;
            __keymap[Qt::Key_F12]         = SDLK_F12;
            __keymap[Qt::Key_F13]         = SDLK_F13;
            __keymap[Qt::Key_F14]         = SDLK_F14;
            __keymap[Qt::Key_F15]         = SDLK_F15;
            __keymap[Qt::Key_Menu]        = SDLK_MENU;
            __keymap[Qt::Key_Help]        = SDLK_HELP;

            // A-Z
            for(int key='A'; key<='Z'; key++)
                __keymap[Qt::Key(key)] = key + 32;

            // 0-9
            for(int key='0'; key<='9'; key++)
                __keymap[Qt::Key(key)] = key;
        }

        //------------------------------------------------------------------------------------------------------
        // get SDL key from Qt key
        //------------------------------------------------------------------------------------------------------
        SDL_Keycode __convertQtKeyToSDL(Qt::Key qtKey)
        {
            SDL_Keycode sldKey = __keymap.value(Qt::Key(qtKey));

            if(sldKey == 0)
                ePRINT("Warning: Key %d not mapped", qtKey);

            return sldKey;
        }

        //------------------------------------------------------------------------------------------------------
        // get SDL key modifier from Qt key modifier
        //------------------------------------------------------------------------------------------------------
        Uint16 __convertQtKeyModifierToSDL(Qt::KeyboardModifiers qtKeyModifiers)
        {
            Uint16 sdlModifiers = KMOD_NONE;

            if(qtKeyModifiers.testFlag(Qt::ShiftModifier))
                sdlModifiers |= KMOD_LSHIFT | KMOD_RSHIFT;
            if(qtKeyModifiers.testFlag(Qt::ControlModifier))
                sdlModifiers |= KMOD_LCTRL | KMOD_RCTRL;
            if(qtKeyModifiers.testFlag(Qt::AltModifier))
                sdlModifiers |= KMOD_LALT | KMOD_RALT;

            return sdlModifiers;
        }

    void eRenderView::keyReleaseEvent(QKeyEvent *ke)
    {
        QWidget::keyReleaseEvent(ke);      

        // Transmit key release event to SDL
        SDL_Event sdlEvent;
        sdlEvent.type = SDL_KEYUP;
        sdlEvent.key.keysym.sym = __convertQtKeyToSDL( Qt::Key(ke->key()) );
        sdlEvent.key.keysym.mod = __convertQtKeyModifierToSDL(ke->modifiers());
        SDL_PushEvent(&sdlEvent);
    }

    void eRenderView::keyPressEvent(QKeyEvent *ke)
    {
        QWidget::keyPressEvent(ke);     

        // Transmit key press event to SDL
        SDL_Event sdlEvent;
        sdlEvent.type = SDL_KEYDOWN;
        sdlEvent.key.keysym.sym = __convertQtKeyToSDL( Qt::Key(ke->key()) );
        sdlEvent.key.keysym.mod = __convertQtKeyModifierToSDL(ke->modifiers());
        SDL_PushEvent(&sdlEvent);
    }

-------------------------

Eugene | 2017-02-20 08:37:10 UTC | #53

[quote="dakilla, post:52, topic:2407"]
SDL_PushEvent
[/quote]

Great! I didn't know about such cool thing! Thanx!

[quote="TheSHEEEP, post:51, topic:2407"]
Why do you want to use Urho3D for a Resource Browser?
[/quote]

RB in old Urho3D editor was able to preview materials and models. I need Urho systems to achieve this.

It's not about rendering performace. Seperate Urho instances mean duplicate resources in memory and redundant disk ops.

I'll probably end up with small preview window in main Urho widget.

-------------------------

Modanung | 2017-02-20 12:56:11 UTC | #54

[quote="Eugene, post:45, topic:2407"]
Only one 3D view for single Urho3D instance. Some small preview windows like in Resource Browser or Material Editor will now require launcing sepearte Urho3D Application.
[/quote]
Couldn't you make the single Urho3D instance overlay the entire window with a viewport for every 3D view?

-------------------------

Eugene | 2017-02-20 13:26:21 UTC | #55

[quote="Modanung, post:54, topic:2407"]
Couldn't you make the single Urho3D instance overlay the entire window with a viewport for every 3D view?
[/quote]

Then what's the point of using native framework like Qt if I will have to implement all windows, docks and menus on my own?

-------------------------

Modanung | 2017-02-20 13:44:22 UTC | #56

I meant graphically overlayed, with the Qt part showing underneath. Or would that bring up other unresolvable issues?
<img src="//cdck-file-uploads-global.s3.dualstack.us-west-2.amazonaws.com/standard17/uploads/urho3d/original/1X/8f08a6538f2ab37f12bea49312ec4a71a4fe65ad.png" width="639" height="445">

-------------------------

johnnycable | 2017-02-20 13:46:14 UTC | #57

I spent some time recently about UI integration on game engines...
As a background, I come from cocos2dx, which has a UI system of its own, mostly reusing a single  Sprite class itself and getting ui widgets out of it, very cocoa-like...
Something like QT is not really viable. At a monstre 15gb download on my mac, it's as big as the Microsoft virtual machine for development, fully packed up with windows os. So really, no. It's not just an editor; it's an ecosystem. Of course, it has all the widgets you may want...
Here's a list with some lighter ui tools i found which can be used more flexibly, and possibly be mobile friendly.

- turbo badger https://github.com/nsf/turbobadger
- librocket (already in https://github.com/realrunner/urho3d-librocket and https://github.com/SirNate0/libRocket-Urho3D)
- Mygui http://mygui.info/
- Gamegui http://voxels.blogspot.it/2015/07/opengl-game-gui-widgets-with-source.html
- Guisan https://github.com/kallisti5/guisan
- CeGui http://cegui.org.uk/
- Imgui https://github.com/ocornut/imgui

All these projects looks recent and mantained. The one i've tried:

Imgui - is light and works very well. It's fast and is widely used on gaming projects. You can see it in action in bgfx https://github.com/floooh/fips-bgfx for istance together with nanovg https://github.com/memononen/nanovg (a fast svg direct command library for drawing) in example 20. Anyway, imgui is a immediate gui mode, that's good for an editor, not-so-good in-game.
Cegui - Gorgeous, skinnable, rich graphics. Well known. Anyway, it's heavy.
Turbobadger - wasn't able to make it work correctly on my mac, so i don't know. Probably not-retina.
Librocket - seems to be already integrated with urho. didn't tried it yet.
MyGui, Gamegui, Guisan, same as librocket - not yet tried.
Does someone else have experience with these?

-------------------------

TheSHEEEP | 2017-02-20 14:05:40 UTC | #58

I could not disagree more.
The task of this is not to create a game UI (which Qt would be completely wrong for, indeed, but for other reasons).

The task is to create an editor, akin to Maya, Blender, Max, Unity...
This is a **completely** different thing.

And you can completely forget about doing any of that with any of the libs you listed if you do not want to spend weeks after weeks of implementing basic windowing, widget and misc functionality, which you'd all get for free.
And that doesn't even cover that editor applications are expected to follow a certain OS-like style in their layouts (note how Eugene's screens so far make it look somewhat similar to a dark Visual Studio). 
Or they will simply end up looking amateurish (as the current Urho editor does). And will be very hard and unintuitive to use.
Good luck designing that with CEGUI :smiley: 

I tried working with most of the libs you mentioned. They are horrible for anything more than very basic layout needs. And most of them come with no kind of layout designer (or pretty bad ones).
IMO the only viable GUI library for games which will not cost your sanity is do-it-yourself with libcef3 (as that offers all that can be done in a browser) or the commercial alternative that already did the integration (forgot the name to be honest...).

> At a monstre 15gb download on my mac, it's as big as the Microsoft virtual machine for development, fully packed up with windows os.

I cannot believe that we still get this in 2017. 15gb is nothing. Get over it.
And besides, the actual distribution size of a Qt app is way, way smaller than that - an application I am developing that is using a lot of Qt functionality comes at a size of 200mb, of which Qt is not even 100mb.

-------------------------

Eugene | 2017-02-20 14:03:14 UTC | #59

[quote="Modanung, post:56, topic:2407, full:true"]
I meant graphically overlayed, with the Qt part showing underneath. Or would that bring up other unresolvable issues?
[/quote]

Do you have any ideas how to merge these two images?
As far as I know,  any GAPI widget like DX or GL view  always overdraw  entire rect area.

[quote="johnnycable, post:57, topic:2407"]
monstre 15gb
[/quote]
Yes, I dislike Qt heaviness too. However, is there any UI framework with such layouts, docks, styles, resource system and hierarchy view?

I'll check suggested frameworks, anyway.

-------------------------

Modanung | 2017-02-20 14:08:42 UTC | #60

[quote="Eugene, post:59, topic:2407"]
Do you have any ideas how to merge these two images?As far as I know,  any GAPI widget like DX or GL view  always overdraw  entire rect area.
[/quote]
I just imagined a transparent background. But you seem to imply this wouldn't work.

-------------------------

TheSHEEEP | 2017-02-20 14:10:36 UTC | #61

[quote="Eugene, post:59, topic:2407, full:true"]
[quote="Modanung, post:56, topic:2407, full:true"]
I meant graphically overlayed, with the Qt part showing underneath. Or would that bring up other unresolvable issues?
[/quote]

Do you have any ideas how to merge these two images?
As far as I know,  any GAPI widget like DX or GL view  always overdraw  entire rect area.[/quote]
I think what he meant (correct me if wrong) was to show windows containing Urho3D views on top of the Qt application.
Like... little windows that are hovering over the normal application.
Did I get that right?

If so, this can definitely be done with Qt. 
Even the other way around can be done: Displaying Qt elements on top of a Urho3D scene (including transparency).

-------------------------

dakilla | 2017-02-20 14:11:45 UTC | #62

I don't think that is a Qt problem but an Urho issue because it doesn't support multiple windows.

You can however try to play with SDL_GL_MakeCurrent

-------------------------

Modanung | 2017-02-20 14:26:04 UTC | #63

[quote="TheSHEEEP, post:61, topic:2407"]Like... little windows that are hovering over the normal application.Did I get that right?
[/quote]
Nope
[quote="Modanung, post:54, topic:2407"]
Couldn't you make the single Urho3D instance overlay the entire window with a viewport for every 3D view?
[/quote]

[quote="TheSHEEEP, post:61, topic:2407"]
Even the other way around can be done: Displaying Qt elements on top of a Urho3D scene (including transparency).
[/quote]
That might be a better way to do it then. Window-filling 3D-accellerated background with viewports that rescale along with their associated transparent QWidgets.

<img src="//cdck-file-uploads-global.s3.dualstack.us-west-2.amazonaws.com/standard17/uploads/urho3d/original/1X/94c7758489c8e4fd13804c0ab8bd1be80859fca2.png" width="635" height="442">

-------------------------

Eugene | 2017-02-20 14:22:11 UTC | #64

[quote="dakilla, post:62, topic:2407"]
I don't think that is a Qt problem but an Urho issue because it doesn't support multiple windows.
[/quote]

It may be hard to achieve on GAPI side.

-------------------------

Eugene | 2017-02-20 17:40:06 UTC | #65

[quote="Eugene, post:45, topic:2407"]
Interaction between native UI and Urho is not very smooth. E.g. when I change position via AI using mouse, it is noticeable that node moves 'laggy'.
[/quote]

Huh.
Movement looks luggy when I accumulate position attribute change this way:

    // Somewhere in Mouse Move event
    const QPoint delta = event->globalPos() - prevPosition_;
    QCursor::setPos(prevPosition_);

And it looks much better if I write

    const QPoint delta = event->globalPos() - prevPosition_;
    prevPosition_ = event->globalPos();

It seems that such a crap is caused by setPos.
It seems that this call loses some sub-pixel stuff that end up in unsmooth deltas.

-------------------------

dakilla | 2017-02-20 17:59:54 UTC | #66

For my widget and to control camera on viewport  I don't use mouseMoveEvent.

Somewher in constructor : setMouseTracking(true);

and :


    void eRenderView::mousePressEvent(QMouseEvent *me)
    {
        QWidget::mousePressEvent(me);

        m_lastMousePos = me->pos();
        m_mouseDownPos = me->pos();

        if (me->buttons() & Qt::RightButton)
            setContextMenuPolicy(Qt::PreventContextMenu);


        SDL_Event sdlEvent;
        sdlEvent.type = SDL_MOUSEBUTTONDOWN;
        sdlEvent.button.state = SDL_PRESSED;
        if(me->buttons() & Qt::LeftButton)
            sdlEvent.button.button = SDL_BUTTON_LMASK;
        if(me->buttons() & Qt::RightButton)
            sdlEvent.button.button = SDL_BUTTON_RMASK;
        if(me->buttons() & Qt::MiddleButton)
            sdlEvent.button.button = SDL_BUTTON_LMASK;
        QPoint position = me->pos();
        sdlEvent.button.x = position.x();
        sdlEvent.button.y = position.y();
        SDL_PushEvent(&sdlEvent);


        const eBool leftBtn = (me->buttons() & Qt::LeftButton);
        if(leftBtn)
        {
            QPoint glob = mapToGlobal(QPoint(width()/2,height()/2));
            QCursor::setPos(glob);
            SDL_SetRelativeMouseMode(SDL_TRUE);
        }
    }

    void eRenderView::mouseReleaseEvent(QMouseEvent *me)
    {
        QWidget::mouseReleaseEvent(me);

        if (me->button() == Qt::RightButton)
        {
            QContextMenuEvent ce(QContextMenuEvent::Mouse, me->pos());
            setContextMenuPolicy(Qt::DefaultContextMenu);
            contextMenuEvent(&ce);
        }

        SDL_Event sdlEvent;
        sdlEvent.type = SDL_MOUSEBUTTONUP;
        sdlEvent.button.state = SDL_RELEASED;
        if(me->buttons() & Qt::LeftButton)
            sdlEvent.button.button = SDL_BUTTON_LMASK;
        if(me->buttons() & Qt::RightButton)
            sdlEvent.button.button = SDL_BUTTON_RMASK;
        if(me->buttons() & Qt::MiddleButton)
            sdlEvent.button.button = SDL_BUTTON_LMASK;
        QPoint position = me->pos();
        sdlEvent.button.x = position.x();
        sdlEvent.button.y = position.y();
        SDL_PushEvent(&sdlEvent);


        if(SDL_GetRelativeMouseMode())
        {
            SDL_SetRelativeMouseMode(SDL_FALSE);
            QPoint glob = mapToGlobal(QPoint(width()/2,height()/2));
            QCursor::setPos(glob);
        }
    }

-------------------------

hdunderscore | 2017-02-20 18:01:56 UTC | #67

For previews that can't go fullscreen, it probably makes sense to atlas the viewports in one instance of urho, if Qt can render from that. But I think it's too limiting to avoid running another instance of urho, because what  if you want to pull out the viewport dock and put in on another monitor, or something ? (Although maybe a moot point atm, if the editor isn't being designed like that).

I'm no big fan of big downloads, but if you only download the minimum you needs, it's closer to 5gb. I did so myself to test the editor, although I ran into newbie issues so didn't get far.

-------------------------

dakilla | 2017-02-20 18:16:53 UTC | #68

5 GB ?
there should be an problem... Too huge.
Did you compile release version ?

-------------------------

hdunderscore | 2017-02-20 18:25:53 UTC | #69

Nah, I just downloaded the compiled version. To be fair the UI said it was 5gb, although that was disk space not the download size.

-------------------------

Eugene | 2017-02-20 19:02:27 UTC | #70

[quote="dakilla, post:66, topic:2407"]
For my widget and to control camera on viewport  I don't use mouseMoveEvent
[/quote]

In my case there is a widget that is absolutely unrelated to Urho frame or SDL.
Anyway, the problem is probably in `setPos`
I need a way to 'wrap' mouse using Qt. I am surprised that QT don't have such simple ability.

-------------------------

johnnycable | 2017-02-21 11:13:48 UTC | #71

Ah, I see I mistook it completely! It's the opposite then - if the goal is to build a first class 3d editor/3d object manager, probably QT is the only viable C++ option. Unless, of course, you want to enjoy Microsoft-something development :unamused:
Or maybe something like Electron & friends, very handy but I don't know if node has such low-level graphical abilities... moreover is Js so forget uint8_t...
Anyway I would still value Imgui, many gaming editors seems to have been built with it... but I can't testify on the final outcome, they seems to be all still in beta... 
QT is surely battle-tested for the task. Many companies used it this kind of high end job...

-------------------------

ben_dover | 2017-02-22 06:52:54 UTC | #72

I saw this video today. The guy is obviously using some way to display the material preview in his node based material editor. You can ask him how he does it.

https://www.youtube.com/watch?v=eUad27Ihang

-------------------------

TheSHEEEP | 2017-02-22 07:07:22 UTC | #73

Well, you can do any kind of image or DirectX or OpenGL display inside a Qt widget. That is not a problem.
What we need is a preview done by Urho3D, though (to make sure it looks like the final product).

I don't think the question is if it can be done (it can, without a doubt), but how to do it best.

-------------------------

dakilla | 2017-02-22 09:20:32 UTC | #74

maybe the simplest way is to use multiple viewports inside main view like sample 09.

-------------------------

TheSHEEEP | 2017-02-22 09:37:28 UTC | #76

Not all docks and windows.
Just the display of final material result.

It could be done in the main Urho3D window inside Qt.
For example, you edit the material values in Qt -> main Urho3D display in editor updates, showing the material.

I think that would be the only way if we do not want multiple instances of Urho3D running. Since Urho3D cannot render into multiple windows at the same time with different scenes, correct?

But then again, I don't think multiple instances of Urho3D running would be a big problem, or would it?

-------------------------

Eugene | 2017-02-22 09:42:21 UTC | #77

[quote="dakilla, post:74, topic:2407, full:true"]
maybe the simplest way is to use multiple viewports inside main view like sample 09.
[/quote]

Huh, I misunderstood you first time. Yep, this is the simplest, but not very nice.

Probably it would be ok for secondary views to be software-copied Urho's RenderTargets.
It is not very performant, but who cares?

[quote="TheSHEEEP, post:76, topic:2407"]
But then again, I don't think multiple instances of Urho3D running would be a big problem, or would it?
[/quote]
It's just dirty, IMO. If I open 50MB skybox in Resource Browser preview, in material editor and in two scenes on two screens, it will end up with 200 MB consumed video memory.

-------------------------

TheSHEEEP | 2017-02-22 10:45:37 UTC | #78

[quote="Eugene, post:77, topic:2407, full:true"][quote="TheSHEEEP, post:76, topic:2407"]
But then again, I don't think multiple instances of Urho3D running would be a big problem, or would it?
[/quote]
It's just dirty, IMO. If I open 50MB skybox in Resource Browser preview, in material editor and in two scenes on two screens, it will end up with 200 MB consumed video memory.[/quote]
200MB is pretty little, really. Just opening a Chrome with a couple tabs costs 1GB ;)
Of course, there shouldn't be too many of these windows open, but I don't think we need that many. For example, I don't think we need to allow showing an arbitrary amount of scenes at the same time.

[quote="Eugene, post:77, topic:2407, full:true"]Probably it would be ok for secondary views to be software-copied Urho's RenderTargets.
It is not very performant, but who cares?[/quote]
That would definitely also work. Especially for "lower-priority" targets like viewing a material that don't need to be updated all the time.

This is a solvable problem. Either solution either costs memory or performance, but both at an acceptable level I think. I'd say just do what seems easiest to you :D

-------------------------

Sinoid | 2017-02-26 07:23:53 UTC | #79

Couple of things, a code dump (with support) is in the works where I'm dumping a heap of commercial material at Eugene for optional use in his work. Entirely optional.

- Storage: 15gb is indeed too much, I know this as a motorcyclist having been smashed to bits by a car annually. 64gb storage is the maximum hardware I carry with me to do actual work with. Your material is always in jeopardy. Sure you're not looking at debug symbols?

Desktop software development has become so rare that I find it hard to believe how much hostility I've just read. Would everyone prefer a crippled web-based editor that can do diddly or a proper desktop editor that can actually use their hardware appropriately?

The multi-viewport issue is a lot easier to just resolve by switching purely to OGL than DX, in DX multiple viewports are pure pain. In OGL it's not that bad ... something OpenGL is actually good at ... shocker.

Reality is, those storage concerns are moot, most likely it's just an inexperienced dev working out the release cycle.

What are you doing that is impressive enough that it gives you right to comment like a god?

I absolutely commend the writer for taking the foray into that which is almost lost as writing real desktop software in an age where everything is javascript this and javascript that as become all too rare. 

We should commend those efforts. We should appreciate those that try to be better than mere web developers.

I entrust code to people that I believe can use it. Persons that are top tier,  I genuinely believe Eugene is on a roll and will find himself as the cheese sooner than he'd like.

-------------------------

TheSHEEEP | 2017-02-27 06:14:30 UTC | #80

[quote="Sinoid, post:79, topic:2407, full:true"]The multi-viewport issue is a lot easier to just resolve by switching purely to OGL than DX, in DX multiple viewports are pure pain. In OGL it's not that bad ... something OpenGL is actually good at ... shocker.[/quote]
But I think in this case, our problem is that the windows containing some graphics must be filled by Urho3D, and Urho3D itself does not feature rendering to multiple windows at the same time. No matter if done with OpenGL or DirectX.

I actually like Eugenes suggestion of just copying the data in the viewport over to some Qt image display (QLabel would work, but a QOpenGLWidget would also work). After all, we're talking about things that simply do not need to be done all too often.

-------------------------

Sinoid | 2017-03-06 05:58:43 UTC | #81

Right, that works globally, and most of the cases where one wants multiple viewports a lazy update of less important windows is okay (asset inspector). I was only suggesting the switch in an editor context, not a "switch all things to pure OGL" stance since that's ambiguous in hindsight.

It's possible in DX, just a lot more work with the swap-chain's quirks. Split views in the existing Urho3D editor work, as far as can see it's just the presentation/system that is missing for handling multiple viewports.

---

There was a lot of SprueEngine/SprueKit bleed-over into the editor code I sent to Eugene, so right now I'm stripping that bleed-over out to get a cleaner version to send off, I'll post that to Github as that'll be easier for commentary and persons can toy around with it at their leisure. It's all "at one's discretion code" anyways, what works for the SprueKit programs might not work well for an Urho3d editor.

-------------------------

ghidra | 2017-03-11 23:27:08 UTC | #82

I just wanted to reply to the very first post, and  the 2 points it brought up:

> - Allow Editor to be called from custom game script. Full or limited editor? How to make interaction?
> - Allow custom game script to be called from Editor. What limitations? How to implement interaction?

I would like to NOT change anything that the editor is currently doing. Mostly because with very little work, I have both options above working in my projects.

To the first point. I just made a small InGameEditor.AS file that is just a stripped down editor.as. So far it includes all the editor, but I am only using the hierarchy windows at the moment. But it's all there. Ultimately I should be able to change materials and make changes in game with the AS code that already exists. And that is awesome.
[url=http://imgur.com/TrH1XhU][img]//cdck-file-uploads-global.s3.dualstack.us-west-2.amazonaws.com/standard17/uploads/urho3d/original/1X/7a43f2df8037329a85c77663feeb893fec0c00e5.png[/img][/url]

To the second point, I pass in a flag that says load the editor.as from my main.cpp. Which has all my  components registered. And as long as I have put in the time to make sure they are exposed to AS, they are integrated in the  editor like any other urho component. So I can use the editor and my  custom components to play around.
[url=http://imgur.com/4Ok10Bo][img]//cdck-file-uploads-global.s3.dualstack.us-west-2.amazonaws.com/standard17/uploads/urho3d/original/1X/a167a1308847bb5cd7fdc1be35cb780d34102d9a.png[/img][/url]

Both images are from the same executable.

There might be a point to "clean" up any code. But the flexibility of AS loading into a c++ project allows some really cool ways to integrate the editor. I would really hate to loose that. And I certainly don't want to write my own editor if it were to get changed fundamentally.

Anyway, thanks to the devs. I find cool stuff with this engine all the time.

-------------------------

Modanung | 2017-03-12 07:03:28 UTC | #83

Might [this](http://discourse.urho3d.io/t/urho3d-and-framebufferobject/2882) be a solution to the multiple viewport problem?

-------------------------

Eugene | 2017-03-12 07:47:46 UTC | #84

Don't worry, script Editor will never be changed, in both meanings.
You will not lose any nice feature that you use. You will not get any nice feature that you may want, except small tune.

-------------------------

cadaver | 2017-03-14 16:03:59 UTC | #85

Yes, for anything that does not need every frame update, you should be able to get away with rendering to rendertarget texture, GetData() the pixels to CPU, then display those pixels via Qt image / bitmap inside a widget without actually having to have multiple GPU views.

-------------------------

Modanung | 2017-03-15 01:23:40 UTC | #86

Sounds like to way to go for material and model thumbnails in the resource browser.

-------------------------

rasteron | 2017-03-17 00:33:49 UTC | #87

Nice progress here @Eugene and great to see you back at the forums @Sinoid !

-------------------------

Sinoid | 2017-03-21 04:52:15 UTC | #88

@rasteron took some time to pull my head out of my ass, I'm not back per se, just back in a "I will support stuff I have done and I'm currently doing" sense. The closest to back I'll get will probably be in IRC, my prior transgressions were too great to reinvolve myself too deeply. I appreciate the pass I've been given thus far for my roid rage in the past.

---

We've mostly finished our refactoring of editing related code, it should be good to go this week, had no idea how extensively our types had invaded the editor code. 

@ghidra raises some interesting points. The biggest meaningful things actually lacking from the existing angelscript editor are:

- Tasks (multiprocessing)
- Timelines
     - Object animation
     - Attribute animation
- Variable update rate
     - IIRC this has been done, but was a convoluted mess
- Ease of extension
     - Try adding an "extend" mode to gizmos, pure pain
     - Editor is mostly functional code
     - Ease is extremely variable, supporting different render modes (wireframe, solid, etc) per split-view was easy
- Difficult to work with physics
- Edit capability looks like it should support animation recording
     - I can move and rotate the Ninja's arms, but that's meaningless

-------------------------

Eugene | 2017-03-29 19:31:42 UTC | #89

Minor news for ones who is tracking this topic:
Since last update I've implemented some concept of 'projects', but I haven't finished it.

_QEditor is on hold now_. I still need this Editor, so I am not going to drop it. However, it is not the only project that I am working on. Please treat such pauses in developement with understanding.

Then, question.
_Any ideas how to make Qt Editor appropriate for UrhoSharp users?_

-------------------------

Modanung | 2017-03-30 12:58:31 UTC | #90

Is this the correct repo and is it up to date?

https://github.com/eugeneko/Urho3D-Editor

-------------------------

Eugene | 2017-03-30 13:23:32 UTC | #91

Yes, it is.
Keep in mind that it is 'zero-point-zero' version that is not usable for any practival activity. Treat it as 'Urho3D Scene Viewer' for now.

-------------------------

Sinoid | 2017-04-04 03:30:23 UTC | #92

Finished the baseline refactoring for SprueKit's Urho3D stuff and pushed it out.

Not ready for use at all (even basic capabilities were lost in refactoring [as basic as changing gizmo mode], due to overlap), so I wouldn't bother forking for a while.

This is not light-weight code by any means, handling many types of documents under differing styles of view was mandatory (SprueKit has to deal with Model, Sculpt/Paint, Shape grammar, Auto-rigger, Texture Graph, and Animation documents in one unified UI where any of those documents may protrude into another).

https://github.com/JSandusky/UrhoEditor

Although an SCE ATF influence is visible in the WIP Dom folder of the "EditorLib," those aren't intended for use in scene style projects even when they're complete (meant for fast data progs.). All emphasis is on specialized controls to deal with their unique circumstances and container widgets that can intelligently present the correct widget (DocumentViewStackedWidget) based on the current document and/or view in that document, in 10 years of desktop UI I've never seen a generic model/adapter/decorator actually work so I focused on minimizing the pain involved with specialized controls.

There's approx. 40 hrs remaining to match the Urho3D editor feature for feature. I'll come back to it once I've cleaned out some of those Github issues I posted and the ones that tie me.

In the near future, the procedural texture graph tool depicted in the readme will be OSS'd and I'll probably port it over to Urho3D's native types.

Exposing timelines and permutations are probably far down the road.

---

I'll also push out the sold SCE ATF C# based editing and binding code I have. I don't consider that to be good by any standard, and retrospectively wish I had invested more in matching ATF's standards for that. It is however, useful for basic throw-away editors. I doubt that stuff still even compiles.

-------------------------

Sinoid | 2017-04-04 04:31:36 UTC | #93

Pushed old SCE ATF based code as well.

I definitely don't recommend using this as is. But for intimate C++/CLI and C# backgrounders it's viable. My refusal to actually 'learn' C# is quite apparent in this code.

Yes, you read that code correctly, it instantiates a unique Urho3D instance for every single document ... woohoo!

https://github.com/Jsandusky/UrShell

Makes for plenty of editing baseline options.

-------------------------

George1 | 2017-04-04 06:01:21 UTC | #94

This looks great. It's good to have multi view child windows.

-------------------------

sabotage3d | 2017-04-06 11:26:05 UTC | #95

Nice! Looks great. Is there any support for ramps/splines?

-------------------------

Sinoid | 2017-04-07 01:02:59 UTC | #96

@sabotage3d, if you mean the SplineComponents - that's just a matter of enumerating the control points as extra gizmos tagged as "control points." That stuff is pretty solid, already used for FRep segments (limbs/spines), quad-strips, and quad-strip-style texture projectors which are pretty core for my stuff.

If you mean other curves, the stuff needed to do splines/color-gradient-ramps already exists (though not in that code - I use Catmull-Rom and MKCB response-curves in the texture graphs), just needs remapping to Urho3D types - the drawing/editing woes are long done.

The ATF stuff does none of that ... I doubt that stuff even compiles. The Qt stuff should actually be usuable in a week or so, I noticed there were some serious nasties to fix document cleanup and hardpaths still in the VS projects.

-------------------------

Eugene | 2017-11-03 18:57:41 UTC | #97

As I promised, I'm switching back to the Editor.

I was a bit unsatisfied with both my previous work and JS's QT Editor because of their limited usage.
I wanted to make a tool that could be used for e.g. ingame Editor and isn't tied to Qt.

So I tried some new approach and here is the example:
![image|690x387](upload://wSKGo3nhPb05dea2sNTSoArG8R6.png)
![image|690x387](upload://cIT6baGUU0y7HrC4h4NXK7u1Ed3.jpg)

All UI stuff is hidden under interfaces, so I could run the Editor under both Urho UI backend and Qt. It may look like overwork, but I definetely like this approach.

Yeah, it's pretty easy to add such Editor to any downstream project because it's just a library that depends only on Urho (or Qt, if you wish)

-------------------------

sirop | 2017-11-13 12:40:11 UTC | #98

Thanks for your work.

Would you share this repo?

-------------------------

Eugene | 2017-11-13 13:10:37 UTC | #99

Repo is on my GitHub (https://github.com/eugeneko/Urho3D-Editor)
However, I think you don't need it since it's just a unusable draft.

I tried both Qt and native Urho UI, then I tried ImGUI Editor by @rku and I considered that this UI library would be more handy for Urho Editor. So I'm going to move all logic into ImGUI-based editor and try pushing it. I hope that first usable version of that Editor will be ready in few months.

-------------------------

