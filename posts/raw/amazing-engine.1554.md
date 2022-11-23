rikorin | 2017-01-02 01:08:28 UTC | #1

I've been playing with Urho for a few days now, and I want to say that it's absolutely great. While being able to do almost everything I ever wanted, it's written in C++ (imo the only language suitable for games), and it's free. The way classes are named, the way it has it's own STL replacement ? I simply love this engine.
What I can't understand is why I never heard of it before? Why the community is that small? It's in active development and is very solid. I think it deserves more attention. 
And I started to feel like I want to contribute to it. 
Of course I can't do anything serious now that I'm not very familiar with Urho's internals, so I've started with something I can do. I think that the editor is one of the key selling points of the engine, and in some way it's face, so I've tried to improve it's user interface. Of course I quickly found out that things I want to do will require an extensive rewrite, so now I'm here asking you, where could I put my energy in a more effective way?
I'm asking about current development direction, what are the features planned for the next major release, what things require more work? Or maybe it will be better if I focus on the editor improvement? I'm an graphic designer, so I could draw a better buttons and stuff, and revamp the UI to be more slick and modern?
Tell me what you think, and again thanks to the creator and all contributors for making this engine.

-------------------------

cin | 2017-01-02 01:08:28 UTC | #2

Hi and wellcome to our forum.
[quote]What I can't understand is why I never heard of it before? Why the community is that small?[/quote]
Forum started near two year ago - 16 Jan 2014. 
Prior to that was a small group in the groups.google.som. Now a lot of help, and some users write articles on other sites, I know Russian users who use the engine and place articles about engine in serious IT-sites.
You can help the project to find new users - tell about engine in twitter or social network.

If you are a graphic designer, you can draw several design for the user interface.
So far there are no plans or roadmap. It all depends on user requests and contributions of all participants.
If you want to help, you need to determine their capabilities and skills and use them to help the project.

-------------------------

rikorin | 2017-01-02 01:08:28 UTC | #3

[quote="cin"]If you are a graphic designer, you can draw several design for the user interface.[/quote]
I'm a programmer too. 
To get a little bit more familiar with the code I've started small and added theme switching support, but I couldn't figure out how to reload it without restarting the editor or deleting and recreating all the UI elements. Also it looks like one can't add multiple xml's to expand/override the default style, for example. It's seems that I have to make a full copy even if the only change is the path to the texture.
There are many other changes that I wanted to implement what will require complex code changes due to the way it's done right now. I'm thinking about starting over writing it in C++, but I'm afraid it will take too much (probably unnecessary) work before I get something useful. That's why I'm here. I wanted to hear if there are more important things I can do. The problem at the moment is that I'm not familiar with Urho enough to work on it's core. And I don't really know how I can help there, too.

[quote="cin"]twitter or social network[/quote]
I don't really like social networks, to be honest, but I'll definitely mention it on my blog once I get something to brag about.

-------------------------

codingmonkey | 2017-01-02 01:08:29 UTC | #4

Hi rikorin.
> And I don't really know how I can help there, too
You may look into topics from feature request forum part with filter: [editor's feature]

I do not know exactly but I guessing what If editor will be written on c++ it will be great, because in this case we got powerful language, native performance and do not needed every time add bindings for workaround functions. Also I think in case growing up abilities(and heavy InEditor tools) of editor I guessing this only one best way - use C++ for editor. AngelScript we may use as InEditor script language but not for editor, it very slow as and lua. And of course the main problem what editor's UI and behavior must be more user friendly and customizable and sensitive, need more tool and helpers for doing work in editor in WYSIWYG(What You See Is What You Get) manner.

-------------------------

rikorin | 2017-01-02 01:08:29 UTC | #5

Hi, codingmonkey,
I'm totally agree with you. And it's also easier to do. Writing and debugging complex scripts is a pain. I've never used Find in files that much before  :slight_smile: 
The problem is it'll take a lot of time to just recreate the existing functionality of the editor. Some parts will be pretty straightforward to port, though. 
Anyway, I think I'll start working in that direction, as it's my favorite part anyway.

-------------------------

codingmonkey | 2017-01-02 01:08:30 UTC | #6

>The problem is it'll take a lot of time to just recreate the existing functionality of the editor
Yes it take some time, but before your eyes is an excellent example ) (urho's editor on AngelScript)
I think what need start from major things and going deeper. 
Also you are absolutely free in your imagination how to realize editor stuff. But great examples is an Unreal editor may be even unity. 
You need try to think from artist's point of view and help to this imaginably artist doing game staff in editor more fast and easy.

-------------------------

rikorin | 2017-01-02 01:08:30 UTC | #7

[quote="codingmonkey"]Also you are absolutely free in your imagination how to realize editor stuff.[/quote]
Yeah, that's the greatest part.
[quote="codingmonkey"]You need try to think from artist's point of view[/quote]
Being an artist I think I know that pretty well.

Anyway, I'm started working already, I'll post updates as I get something to show.

-------------------------

codingmonkey | 2017-01-02 01:08:30 UTC | #8

>Anyway, I'm started working already, I'll post updates as I get something to show.
Good, but I want to mention one thing: it will be great if editor's code style are mirrored represent the engine code style.
For what reason? Well, I guess few reason for that:
+ Friendly "first review" for other contributors, and more chances to work on this editor with incorporate with others. This is a huge work actually and I guessing it's pretty heavy for one person. 
+ Has a chance sometime to be  "main" editor of urho engine and release with master brunch (of course if "core team" gives agreement for this)

see this: [urho3d.github.io/documentation/H ... tions.html](http://urho3d.github.io/documentation/HEAD/_coding_conventions.html)

-------------------------

rikorin | 2017-01-02 01:08:30 UTC | #9

[quote="codingmonkey"]it will be great if editor's code style are mirrored represent the engine code style.[/quote]
I thought it goes without saying :3

-------------------------

globus | 2017-01-02 01:08:30 UTC | #10

May be help as start point:
Urho3DIDE
[github.com/scorvi/Urho3DIDE](https://github.com/scorvi/Urho3DIDE)
Or 06_InGameEditor
[url]https://github.com/scorvi/Urho3DSamples[/url]

-------------------------

cadaver | 2017-01-02 01:08:31 UTC | #11

There's actually no reason that a C++ editor would need to be part of the Urho repo. Actually doing just the opposite ensures that no project's scope gets too large. Urho itself is (just) the runtime.

Once (if) a dominant and excellent editor project would emerge, we would be sure to advertise it in the documentation, while deprecating the script-based one, which is to some degree an engine API use example, though also useful.

-------------------------

globus | 2017-01-02 01:08:31 UTC | #12

May be 2 separate projects:
Urho3DPlayer - runtime game launcher
UrhoEditor - only for game editing with advanced functionality.

-------------------------

rikorin | 2017-01-02 01:08:31 UTC | #13

I personally would prefer it to be a part of Urho3D, because I don't want to manage separate project.
Well, let's first see if I manage to make something solid.

-------------------------

rasteron | 2017-01-02 01:08:32 UTC | #14

Hey welcome to the forums dude and good luck with that! Improving the built-in editor would be nice but if you decide to go 360 and for the C++ route, you can also check out Xu Jing and Aster's Particle Editor, which is made using QT and a great starting point and reference, in my opinion.  :slight_smile: 

[topic318.html](http://discourse.urho3d.io/t/qt-based-2d-particle-editor-for-urho3d/327/1)

[github.com/aster2013/ParticleEditor2D](https://github.com/aster2013/ParticleEditor2D)

-------------------------

rikorin | 2017-01-02 01:08:32 UTC | #15

Hi, thanks. I'm writing it in C++. I'd prefer to avoid using Qt (ever) and better focus on improvement of Urho's default UI. I also want to make it to the master someday.
I've forked Urho and will be committing my progress, but for now there is nothing to see.

-------------------------

codingmonkey | 2017-01-02 01:08:33 UTC | #16

Do you have some kind images or sketches for your editor UI ? something like base blocking stage for level editing.

-------------------------

rikorin | 2017-01-02 01:08:33 UTC | #17

Nothing to share at this point.

-------------------------

rikorin | 2017-01-02 01:08:37 UTC | #18

I've decided to make the editor standalone. It will be easier for me that way. Now I can change the code style a bit. It's really hard to breath without space within parentheses. :slight_smile:
Oh, and I've called it Aquarium :slight_smile:

-------------------------

weitjong | 2017-01-02 01:08:37 UTC | #19

From your profile I can tell why you like the engine so much  :wink:

-------------------------

rikorin | 2017-01-02 01:08:37 UTC | #20

And why is that, I wonder? :slight_smile:

In fact I was writing my own engine for the game I'm working on, but then I remembered the gold words: "make games, not engines" and so I went to google to find something good (funnily I've started writing the editor instead).
I did the same search like a year ago, but I couldn't find anything fitting my requirements. Existing engines (written in C++) are all huge and ugly, and they lack features too. Urho3d has almost everything I need ? it's a game engine, not a rendering engine like Ogre (which is too big and full of legacy code), so I don't have to waste my time writing I/O and stuff like that. I also like the way it's organized.
Well, most people would probably pick Unity, but I hate it :slight_smile:

-------------------------

weitjong | 2017-01-02 01:08:37 UTC | #21

I should say "your profile picture" instead. LOL. Cat likes fish.

-------------------------

codingmonkey | 2017-01-02 01:08:37 UTC | #22

>Oh, and I've called it Aquarium
 :laughing: 

I want to suggest an idea  - show the startup window when the editor starts
on this startup window may be placed:
- editor title
- editor options (shortcut keys mode)
- links to documentation and wiki
- [b]images from one of known projects on urho[/b]
Also on this window maybe placed scenes list from current project.

Something like this:
[url=http://savepic.su/6809684.htm][img]http://savepic.su/6809684m.png[/img][/url]

They changes this images from version to version.
In some way this is motivation for game developers who do game on urho do it better to get their games on the startup screen )

-------------------------

rikorin | 2017-01-02 01:08:38 UTC | #23

[quote="weitjong"]Cat likes fish.[/quote]
Now I got it.
[quote="codingmonkey"]I want to suggest an idea - show the startup window when the editor starts[/quote]
Well, I might do it later, but for now such things are in a lowest prority. I don't have much time to code, and the original editor is about 17k sloc. 
Also I believe that things like startup screens and splash screens are actually counter-productive. But it seems that the first thing every beginner wants to do is to make one. Most of the time it's the only thing they actually manage to do before dropping their project :slight_smile:

I want to put all my knowledge about UI design to try and make the most comfortable editor to use, ever. That's my ultimate goal for this project.
For example, why do we have hierarchy window on the opposite side of the screen from attribute inspector? What do you do most of the time, when you select a node in the hirerarchy? Right, you are editing it's attributes. :slight_smile: Why should you move the mouse over the whole screen for that? Now see this screenshot, isn't it cool? :slight_smile:

[img]http://i.imgur.com/28zkNDo.png[/img]

Or why don't we put the button to create a new node right in the hierarchy window, right in the place where you want to add it (node)?
An so on.
I have a huge list of such improvements, but the main objective now is to make the editor usable. :slight_smile:

-------------------------

codingmonkey | 2017-01-02 01:08:38 UTC | #24

> I don't have much time to code, and the original editor is about 17k sloc. 
i'm think what you do not need copy original editor line by line (if only for testing purpose) because you got the same editor but on c++ ) 

>isn't it cool?
actually from my POV it's handy and nicely until it keep these minimalistic UI style without using huge/big UI elements and large fonts, if UI elements are growing in size this are biggest mix of UIs they close view to main scene. IMO open(free) view to scene it's main thing.
and if additional tool are close part of view it probably using auto-hide mechanism or shortcuts to hide this tool immediately from view.
in philosophical terms or art style i guessing that urho's UI might be represent as "water" not as "rocks" or some thing solid.

-------------------------

rikorin | 2017-01-02 01:08:38 UTC | #25

[quote="codingmonkey"]you do not need copy original editor line by line[/quote]
I've just used that number as a rough estimate of the amount of work that has to be done.

There definitely will be a way to hide all the distraction and focus on building the scene. And I'll make sure to minimize the space used by the interface. I have a concept of hierarchy tree that takes minimal space in width while preserving much more data than the current one. Especially in the cases there huge things like armatures/skeletons are displayed.

-------------------------

gawag | 2017-01-02 01:08:43 UTC | #26

[quote="rikorin"]I've been playing with Urho for a few days now, and I want to say that it's absolutely great. While being able to do almost everything I ever wanted, it's written in C++ (imo the only language suitable for games), and it's free. The way classes are named, the way it has it's own STL replacement ? I simply love this engine.
What I can't understand is why I never heard of it before? Why the community is that small? It's in active development and is very solid. I think it deserves more attention. 
[/quote]
I agree. In my opinion it's way more usable as Irrlicht, CrystalSpace and Ogre (the "three big free 3D/game engines").

[quote="rikorin"]
And I started to feel like I want to contribute to it. 
Of course I can't do anything serious now that I'm not very familiar with Urho's internals, so I've started with something I can do. I think that the editor is one of the key selling points of the engine, and in some way it's face, so I've tried to improve it's user interface. Of course I quickly found out that things I want to do will require an extensive rewrite, so now I'm here asking you, where could I put my energy in a more effective way?[/quote]
I started and work on an (unofficial) Urho Wiki: [urho3d.wikia.com/](http://urho3d.wikia.com/)
I'm still doing most of the work there alone. Help is really welcome. It's also not just about Urho but also about game development in general, like modelling and texture creation with Blender, audio recording and editing, ...
I'm not really the editor guy, so you could for example add tutorials about the editor (if the existing documentation could be expanded or improved or made simpler). Parts of the wiki are aiming at total beginners, who have no experience with building software via CMake or setting up a toolchain or using something like the Urho editor. The beginner tutorials have lots of pictures, such tutorials helped me a lot getting started as a C++ beginner with CrystalSpace and later Ogre.
There are also two sample projects and more planned (the second one only like half-finished ATM and not yet updated to Urho 1.5): [urho3d.wikia.com/wiki/Ideas_for_ ... r_features](http://urho3d.wikia.com/wiki/Ideas_for_samples_and_their_features)
There are also several links to interesting Urho projects, forum topics and other useful sites. If you have or find something, add it!

Are you good with modelling and creating textures? My skills are quite limited in that area and you (or someone else) would be a great help creating more samples (and promoting Urho). The samples shipped with Urho are quite minimalistic and quite ugly (low resolution textures, character model with no texture at all, ...). These wiki samples try to be mini games in various genres with focus on testing things out and documenting ways to do certain things.

> Now I've read the whole thread and not just the first posts.
Seems like you started improving the editor or creating a new one. The few times I tried that existing thing, I couldn't even load models and materials to preview them, so that may be a really good idea. :laughing: (maybe I should try that again)
Would be great to have it in a public repository to check it out, even if it's just some reorganized UI or it can't do much yet. Loading models and selecting materials would be already really useful for me (and reloading materials to see changes in a shader).
Also I would love to have a simple in-game editor in one of the sample project. I wrote an in-game editor for a 2.5D platformer I made with Ogre several years ago. Your editor is also in C++? Would be great to be able to put some parts together to make simple, user-friendly and custom in-game editors if someone wants something like that for his Urho project.

-------------------------

rikorin | 2017-01-02 01:08:43 UTC | #27

My English isn't good enough to write tutorials. That'll be embarrassing.
[quote="gawag"]The few times I tried that existing thing, I couldn't even load models and materials to preview them[/quote]
I doubt that my version of the editor would change that.
[quote="gawag"]Would be great to have it in a public repository to check it out[/quote]
It's already in a public repo [url]https://github.com/rikorin/Aquarium[/url], though I work in a branch which is not published yet. I hate to publish broken code. I'm a bit too perfectionist.
Also I wouldn't expect anything for at least a month.

-------------------------

gawag | 2017-01-02 01:08:44 UTC | #28

[quote]My English isn't good enough to write tutorials. That'll be embarrassing.[/quote]
Seems good enough.  :wink:  I'm also not a native speaker and have too look up stuff often. Also I'm usually reviewing every change and could fix stuff if something is really not understandable or wrong.
The wiki does really need more content and I can't write over every topic alone because I don't know every area and don't want to work myself into every area that would be interesting. Maybe we could make a system of "drafts" or "alpha articles". Articles that are not fully published but are being worked on or are "planned". I did that with articles about the two sample games. I wrote several pages but didn't link them so they couldn't be reached easily and only made them reachable when they were good enough and all content was ready. That could also be done with rough article drafts: pages that have only a few ideas and [TODO] entries on them, so that they can be filled/completed over time or by other persons. There are still several [TODO] notes scattered across the wiki.
[quote]I hate to publish broken code.[/quote]
Others do that all the time! *ba dum ts* :laughing:
Your code looks good so far, really clean style.

Do you have an idea collection or some kind of roadmap for the editor?
Do you want to use the Urho GUI?

I want to restructure the wiki anyway relative soon. I'm still not really sure how but some other kind of organizing. Currently the main page is one giant hub that links to everything. Should be more hierarchical and also more planned with idea lists, lists of stuff being worked on or are planned or would be nice to have.

-------------------------

rikorin | 2017-01-02 01:08:44 UTC | #29

I don't really believe that wiki is needed. I think it's better to focus on Urho3d documentation. In particular, many methods are described briefly, and it's sometimes hard to figure out what they actually do. I also hate wikia very much. :slight_smile: 
[quote="gawag"]Others do that all the time![/quote]
I haven't decided on the code structure yet. It changes severely every day. I've already changed the file and class names since the last public commit. I'll publish the code when I settle on this.
[quote="gawag"]Do you have an idea collection or some kind of roadmap for the editor?[/quote]
I do. In my head. :slight_smile: 
[quote="gawag"]Do you want to use the Urho GUI?[/quote]
Yes, and possibly improve it a bit.

-------------------------

empirer64 | 2017-01-02 01:08:44 UTC | #30

Hey rikorin, I was also thinking about creating/forking an Urho editor. I want to create it using the Urho UI, of course the UI needs some improovements to make it more usable.
I would like to ask why did you decide to use C++ instead of AS, when you could just adjust/fork the existing AS editor. I have not decided yet if I want to use C++ or AS but to build on something would be great.
If you would like to, we could team up to make it faster.

-------------------------

Kyle00 | 2017-01-02 01:08:44 UTC | #31

rikorin, your japanese pharse, especially what you had originally reminded me of chopper from one piece

[video]https://youtu.be/GE-1iYLziMM?t=42[/video]

-------------------------

gawag | 2017-01-02 01:08:45 UTC | #32

[quote="rikorin"]I don't really believe that wiki is needed. I think it's better to focus on Urho3d documentation. In particular, many methods are described briefly, and it's sometimes hard to figure out what they actually do. I also hate wikia very much. :slight_smile: [/quote]
A wiki is a kind of documentation. And since the real documentation can't be edited easily or by many, an open wiki doesn't seem that bad. Got something better as Wikia? The wiki landed by accident there  :unamused:, I just wanted to check that wikia out and it directly created a public for Urho though I only wanted to see the stuff one can do. Wikia has several flaws, so a better alternative would be nice.
[quote="rikorin"]
[quote="gawag"]Do you want to use the Urho GUI?[/quote]
Yes, and possibly improve it a bit.[/quote]
That would be great, it 's currently really minimalistic and can't do much. 

I really need a better GUI. I've lots of experience with Qt and have written a better and really flexible layout system for that, it's a lot like CSS but all inside C++. I could try to port that to the Urho GUI. What are the things you want to change? There are many standard GUI widgets missing.

There's a bigger thread about third party UIs: [topic838.html](http://discourse.urho3d.io/t/integrating-3rd-party-ui/819/1)

-------------------------

rikorin | 2017-01-02 01:08:45 UTC | #33

[quote="empirer64"]why did you decide to use C++ instead of AS[/quote]
Mainly because it's my favorite language, it's fast, easy to debug, and it produces native code. There also were many requests for C++ version of the editor on this forum.
I doubt teaming up at this stage would work, but then I get something mature any help would be great. Especially on stuff like particle editor. I don't even plan on implementing it yet.
[quote="gawag"]What are the things you want to change?[/quote]
Things like more comfortable to use color pickers and sliding inputs for numeric values (something like in blender). Also a better skinning support.
[quote="Kyle00"]reminded me of chopper from one piece[/quote]
Wtf is going on :open_mouth:

-------------------------

gawag | 2017-01-02 01:08:45 UTC | #34

[quote="rikorin"]
I doubt teaming up at this stage would work
[/quote]
Planning and ideas could be opened. Like a wishlist. Or stuff people want to contribute too. Or stuff other people have already done and could be useful.
[quote="rikorin"]
Especially on stuff like particle editor. I don't even plan on implementing it yet.
[/quote]
Like I said about the models and materials: would be already great to see an effect and being able to reload it simply. So one can edit it (externally, doesn't have to be an IDE) and immediately see the change without having to restart his game and getting to the effect source.
[quote="rikorin"]
[quote="Kyle00"]reminded me of chopper from one piece[/quote]
Wtf is going on :open_mouth:[/quote]
Maybe this "Chopper" uses a word like "rikorin" often? I also didn't get that and don't really know "One Piece".

-------------------------

rikorin | 2017-01-02 01:08:45 UTC | #35

[quote="gawag"]would be great to see an effect and being able to reload it simply[/quote]
Isn't it working already?
[quote="gawag"]Planning and ideas could be opened.[/quote]
Oh, I don't know, sounds problematic. There is already too much talk in this thread.
[quote="gawag"]I also didn't get that and don't really know "One Piece".[/quote]
I might be a huge fan of Japanese culture, but this is just too weird for me. And I've seen some shit.

-------------------------

Kyle00 | 2017-01-02 01:08:45 UTC | #36

My mistake. I thought that you can understand spoken japanese as well as you write it.  Chopper often says "?????", "????", as seen in that video in the first few phrases. I thought that's where you got it from, but it's apparent it's not.

-------------------------

gawag | 2017-01-02 01:08:45 UTC | #37

[quote="rikorin"][quote="gawag"]would be great to see an effect and being able to reload it simply[/quote]
Isn't it working already?
[/quote]
I just tried it. There's a small window in the lower left with a tiny particle effect preview but I can't seem to add the effect to the scene, oh I can, it was just hard to find...
Also sound sources can't be set to loop. The mouse wheel is inverted (and no settings). I can't load stuff from outside the editors ressource paths (that's a big bummer!). The text is quite thin and a hard to read (antialiasing seems to blur it with the background). In the Attribute Inspector the numbers are overlapping each other. ...

[quote="rikorin"]
[quote="gawag"]Planning and ideas could be opened.[/quote]
Oh, I don't know, sounds problematic. There is already too much talk in this thread.
[/quote]
Oh right it got quite offtopic. That could be moved to an "wishlist-issue" or something like that on GitHub: [github.com/rikorin/Aquarium/issues](https://github.com/rikorin/Aquarium/issues)
GitHub does also have a wiki system, example: [github.com/gawag/Urho-Sample-Platformer/wiki](https://github.com/gawag/Urho-Sample-Platformer/wiki)
Seems to be currently disabled for Aquarium though. In the project settings you could active the wiki and disable "Restrict editing to collaborators only" to make it a public wiki.

-------------------------

rikorin | 2017-01-02 01:08:45 UTC | #38

[quote="Kyle00"]My mistake. I thought that you can understand spoken japanese as well as you write it.[/quote]
You got it right, I can :slight_smile: 
[quote="gawag"]Seems to be currently disabled for Aquarium though[/quote]
I thought nobody would ever need it.

-------------------------

rikorin | 2017-01-02 01:09:08 UTC | #39

I have to apologize, but I'm discontinuing work on the editor because I don't have spare time anymore. Sorry.
The engine is still great and I'm going to use it in the future, and might even return something back to the community one day.

-------------------------

