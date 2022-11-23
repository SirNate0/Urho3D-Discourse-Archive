johnnycable | 2017-05-11 20:59:50 UTC | #1

I see you coming from godot... I've always been curious to try it, but in the end I didn't because of componentization lacking, own physics, and some strange guys in forum... What your experience with it was?

-------------------------

slapin | 2017-05-12 00:20:27 UTC | #2

Well, lot of strange guys, strange developers, unclear targets. But a lot of hype and drive.
Most people are aside and say how cool Godot is but never tried to make anything beyond simplest.
Also very toxic community (probably it is common with gamedev, just depends on number of people) which will attack you if you try to indicate some bugs. Also Reduz wants to make everything himself.
If you want to add a feature and he do not have it planned, or wants to make himself some time in future he won't accept your PR.
But there are no much public plans. Probably many of these things are changed now, but I was completely demotivated.
[b]Also, a disclaimer - all I say is my personal subjective opinion and I reserve all rights for mistakes, errors and wrongdoings. Also if somebody thinks I personally offended somebody, that is their own problem as I might be not even aware of that.[/b]
In general what was frustrating most is that if you found a bug and report it the first reaction you get is "nobody complained yet" and over time it happens nobody used that cool feature. So when you're always blamed for your bugs that is not really good so you stop reporting them and stop caring. After some time working with Godot you know - if that is not in demo using specially prepared assets then it doesn't work, you don't even need to waste time trying it even if it is advertised feature. Also constant happiness of community about Godot annoyed me too much. And if you show people obvious bugs they won't believe you, but they eventually get hit by them, in months,
and as I seen that my old reports get some discussion. I got sick of it. Most people who had enough knowledge, struggled a bit and gone quickly, I was optimist for too long, then my frustration finally overpowered my stupid loyalty.
So I started looking at alternatives. With Ogre you get nice game engine constructor, but that was too
hard for me, as I don't have any gamedev experience. I was pointed to Urho3D at Godot IRC channel by
user Calinou and I was not happy at first, but after some frustrating hours with Godot I tried Urho
especially examples and was very happy. Also examples were very transparent, so not made look good
using some trickery, everything is there to take and try. I was not too happy about Mixamo models with uncertain status, but I did not need them.
I quickly got some progress with simple things with Urho, made some people hate me in progress, but
the ends justify means. The community is very small and it is very hard to get information. Also
as I lack gamedev experience I often don't know the right question. I could go for Unity which have
much more information and features, but I want to be with Open Source.stuff. So now I'm more or less
happy with my toys. It is a lot to be done to gain some experience with basic game making, but I can say
I more or less can do most of things I want with enough effort without much problems stopping me.
So I could say that while time spent fighting with godot was not complete waste of time, I could use it more effectively learning new things and making fun stuff using Urho.

-------------------------

johnnycable | 2017-05-12 11:57:19 UTC | #3

My take, if you don't mind.
I've come here from cocos2dx, because it is left 4 dead by the company, a shame. All the dev is now about js hope-for-facebook-games market... who knows the future, but I prefer C++. Cocos it's a simple, good engine, especially for 2d, with some extension for 3d. It's 2d part is rock solid, with many extension and community contributed parts... 3d part is not very used, afaik...
The people in the community is basically starters with some expert, but anyone is good and willing to help, never had a problem with that. The company behind it is supportive generally. And this is good.
I've tried urho out of a referral by someone in the forum. I must say the engine looks very well laid. I'm not very expert about 3d, I'm learning slowly, but the architecture and many other things looks ordered and well done. There's a bit of messin up the system for setting everything but this is normal, it's managed as a library and has to be set up, it's not a content pipeline drag-n-drop and you're there.
Community seems ok, much less people in respect to cocos but much more skilled, and yes, you've got to ask the right question because many things you can find them by simply trying or considering more on them. Anyway people answer if you are clear, i think...
About godot, I've given a general read to it without too much faith... while there seems to be excessive evangelism in the community... i remember stumbling on a discussion like "godot is a tool for artist, don't let the programmers in, no componentization, no, no, no" and well i was looking exactly for that for a use case of mine and so I've made a big laugh of it and removed it from the list. Many other things pointed to the use of a constrictive structure and well, if I want that then I'll go for Unity, hands down, who cares about godot  :wink:

-------------------------

shipiz | 2017-05-12 22:55:51 UTC | #4

I was the one recommending urho on cocos2dx forums. Everything you said is true. I got tired of cocos devs ditching good engine for js crap. The only thing im missing from cocos is ease of setup and project structures. I've already posted here on forums to about that.

-------------------------

artgolf1000 | 2017-05-13 03:22:39 UTC | #5

Urho3D is highly customizable, you need to look into some examples and the code exchange region before you master the engine, this may cost long time, but it worth it.

I have achieved lip-voice-skeleton synchronization component, verlet cloth simulation component, jiggle bone component, better ssao shader, screen space global illumination shader, and use them in my own project.

I used to write 3d engine myself, and maintain it for nearly seven years, but I have found that it is hard to cross platform, so I only use it in my old iOS projects.

Unity is my second favorite engine, but it is not open source, you can only use its current features, and the support team will not reply at all if you don't pay them money, I will not risk to use Unity on my projects if I had not bought their paid service.

I had learned Unreal engine 4, but I found that the blueprint is buggy, and I can not completely get rid of blueprint, when the engine upgrades, sometimes, the new version can not open my project, so I give up Unreal engine finally.

-------------------------

slapin | 2017-05-13 11:51:10 UTC | #6

I need to add that my opinion of Godot is not constant and I still observe. Currently it is not something I'd recommend to others, but probably their drive will get them somewhere.

About Urho - I'm not that much interested in graphics effect at the moment, I'm more into AI, logic and gameplay,
also asset pipeline.
These things have too little attention in the engine, and I research what I can do to overcome shortcomings.
My dream is to make game on GTAIII level but with features I want and gameplay I want. (I want a city sandbox with using procedural generation, with all buildings enter-able, but simple enough to accomplish by 1 person in several years) It is very technically challenging, but it is fun and motivating. And Urho lacks on almost all aspects I need so the road is very far from forming. I even can't establish proper asset pipeline for characters with quality I need. The good thing is "you got what you have" approach, so if you need some stuff, write it and that will work.
The problem of course is lack of knowledge on how things work in game engines and lack of public information and
that it is often costs thousands of $$$ which is quite expensive for hobby projects. It is great there are people who do challenging tasks like IK, but there are many things which are needed to be done yet to at least have all code frameworks done. But with Urho it is easy to do planning, it is easy to assume that you write everything you need yourself. If you think something you code might be accepted to core engine, you can submit PR and get some feedback. So my current problem is lack of knowledge on how to do some specific  features, but that is slowly progressing. Again, I could go for Unity which does have tutorial on almost everything and addons for the rest,
but that will get my hobby project depending on closed tool which will not let me run it on ARM Linux for example, so I would lose a lot of comfort. Also I won't be able to call this open source anymore.
By saying that I need to tell that every tool have its downsides. For my case Urho currently have less, in addition to
the fact I spent enough time learning it so I can foresee solutions for all my problems. So don't think I'm one happy person using Urho - I'm not frustrated, but I'd be more happy to do my game stuff than implementing basic frameworks.

-------------------------

slapin | 2017-05-13 11:56:29 UTC | #7

@artgolf1000
You probably misused Blueprint. What I find nice in UE4 is their BehaviorTree implementation.
As for Blueprint - it is for designers to rough-out logic to show to programmer what they want to do.
Any non-specialized visual system is lacking sense. It can't replace actual coding. But it is useful
in specific cases.

-------------------------

johnnycable | 2017-05-13 15:10:07 UTC | #8

Ah, so you're the one to blame. :wink:
Thanks for that. And I agree on missing ease of setup. I'm ditching it with bash scripts blows, let's see if I'm able to get that fixed.

-------------------------

johnnycable | 2017-05-13 15:15:58 UTC | #9

Maybe you're trying to do too many complicated all at the same time? 
Anyway racing games go to the extend of using customized engines for that...
No expert here, of course. I never played GTA. :confused:
Last "driving" game played was AG Drive on ipad... great...
and before of that, best of them all: Carmageddon :grin:

-------------------------

slapin | 2017-05-13 15:36:41 UTC | #10

You can connect Carmageddon + 3rd person shooter to get rough picture of what GTA is.
And games like need for speed indeed have custom engines, but that is not my target.
Everything about cars is achieveable with current Urho. I currently struggle with characters,
AI behaviors, geometry generation. Nothing unmanageable, though. If you want to have rough
understanding what GTA is just go to youtube, there are many videos there. From GTA I like
city sandbox idea. The other game which illustrates some of what I want is Saints Row 2.
They are basically the same genre with GTA. What I make will only contain city sandbox,
that is plan. And some kind of quests/missions, nothing which have any kind of global start or end.
Probably with some other procedural approach. The game should be fun to developer and not only
to develop, but also to play, so it should surprise me.

Current problem I solve now is that AI consumes all CPU so I rewrite BT to C++ with ability to script nodes.

Next I will go for character customization - I don't want to model tens of characters to reduce repetition,
I just want the spawner to spawn different ones on the street. That is quite complex task, especially with bone limitation. I have all the theory needed to do this, I just need to set up a pipeline (which might be quite tough).

Then I will restore my city generation framework and update it so that it is AI-centric, so it should be simple to build influence maps and other stuff. People should walk according to their needs not randomly wander.
Also they should avoid roads, everyone should obey traffic lights, etc. Also I need to employ various algorithms to accelerate actual generation of environments. As I plan to generate both exteriors and interiors, that is critical.
So that is plan for current year, or so, I think.

-------------------------

artgolf1000 | 2017-05-15 00:51:57 UTC | #11

The blueprint in UE 4 is not compatible, if I upgrade the engine, old blueprint often refuse to work.
Somebody told me that you can't do skeleton animations without blueprint, I need to use blueprint to design the behavior tree, is it correct? If I can do everything with C++, I prefer UE 4.

-------------------------

johnnycable | 2017-05-15 12:40:12 UTC | #12

This makes sense because blueprints, in the end, are (just) a visual representation of code. So with upgrades one could expect compatibility breaks...
For the same reason imho it seems strange you cannot do behaviouring with pure code in UE4... anyway I'm no expert...

@slapin 
Ah, now I got it. It's like fast and furious... :smiley:
Mass character spawning... I imagine is tough yes, but probably you may limit yourself to a couple of base character and dressing variations...

-------------------------

slapin | 2017-05-15 20:50:28 UTC | #13

Nah, I will not like it being so predictable.
I want good surprises from game I write. I want to have at least the same level of fun roguelike author have
playing his game, but in more graphics-intense manner (and less repetitions).

-------------------------

Jillinger | 2017-05-15 22:49:34 UTC | #14

[quote="johnnycable, post:1, topic:3117"]
I've always been curious to try it, but in the end I didn't because of componentization lacking, own physics, and some strange guys in forum... What your experience with it was?
[/quote]

I have been trying the different 3d engines, and I found Godot to be quite simple, but I left it for the simple fact that it doesn't seem powerful enough to handle big projects. It is a low-poly engine, at least from my observations. Frame-rate ran at over 800, when starting a project from scratch - empty.
<img src="//cdck-file-uploads-global.s3.dualstack.us-west-2.amazonaws.com/standard17/uploads/urho3d/original/1X/6f31a65eef8ab75f098e0eefdadadab6003a268e.jpg" width="690" height="387">
and I just loaded a terrain from heightmap, added a few textures, including splats, a camera, and light, and the frame-rate has plummeted considerably. The plane used to create the heightmap did not even have a very high subdivision.
<img src="//cdck-file-uploads-global.s3.dualstack.us-west-2.amazonaws.com/standard17/uploads/urho3d/original/1X/bb48e3c8ae585cf3bf608b49ca0cf5b7f6da9ac9.jpg" width="690" height="387">

Trying a lowpoly (less subdivisions) still doesn't take it past 400 fps.
<img src="//cdck-file-uploads-global.s3.dualstack.us-west-2.amazonaws.com/standard17/uploads/urho3d/original/1X/edddf44205f770eeb34b186268d122a0a14602d1.jpg" width="690" height="387"><img src="//cdck-file-uploads-global.s3.dualstack.us-west-2.amazonaws.com/standard17/uploads/urho3d/original/1X/2502ab403b6b8dc440ce2bdf382167523e577b65.jpg" width="690" height="387">

So since I am looking for an engine that can perform, I put Godot aside. The apk was not smooth on the emulator either.
JMonkeyEngine performed way better, both on windows and the emulator, but I am now using Urho3D, to make a comparison. The one that performs better, is the one I'll stick with.
I haven't been able to test UDK because it sucks my resources and doesn't allow me to work smoothly. I guess I  need a 4 core instead of a 2, to work with that engine.

-------------------------

johnnycable | 2017-05-16 10:55:25 UTC | #15

Afaik Godot was very much driven by user requests toward usability and flexibility. Basically it's been a 2d engine until now... anyway it seems they're working toward 3d. WIP. Wait, Wait.
About Jmonkey... how's java guys performing? You know that's a lot of scares about gc, me included, and I have used java on the job for long... probably language racism, thou :sunglasses: what's your impression? How do they ship on ios?

-------------------------

slapin | 2017-05-16 11:04:34 UTC | #16

IIRC Godot was 3D engine, then got to 2D engine and now have 3D recreated.
As I understand it does have a lot to wish for in both 2d and 3d areas,
as I tried both. I did not try Urho2D but I think it might be at least as good as Godot for 2D plus predictability minus obvious bugs. But it looks like not very popular feature, so something might be lurking there. Or not.

-------------------------

Jillinger | 2017-05-16 13:03:46 UTC | #17

[quote="johnnycable, post:15, topic:3117"]
I have used java on the job for long... probably language racism, thou :sunglasses: what's your impression? How do they ship on ios?
[/quote]

For me, personally, language isn't a problem as long as it isn't c++ :grimacing:, but that seems to be changing, as I am now learning c++, by using angelscript code to help me understand it :grinning:. I think all languages can be learned quite easily as long as you have access to internet - since there are may helpful individuals and tutorials.Once you get into using the code, it's like playing an instrument. Godot has it's own language, but since I like learning new things, I am always ready to take up a new challenge. I love coding, so learning them is exciting to me..Java I understand is the language suited for android.
Regarding ios, I don't know, since I understand there is a cost for a license to target that platform.

-------------------------

slapin | 2017-05-16 16:05:00 UTC | #18

Godot's script language is nice. But the engine itself leaves a lot to be desired.

-------------------------

Jillinger | 2017-05-17 13:50:40 UTC | #19

Hi @johnnycable
What programming language do you like, and prefer using?

-------------------------

johnnycable | 2017-05-17 14:06:24 UTC | #20

Hello there. Atm I'm using c++ mostly. It's hefty and cumbersome, and sometime obscure, but it's universal and the standard for realtime application (that is, videogames.:wink:).
I'm always in the process of learning sm new, but I'm too lazy in the end...:sleeping:
Ios is at a cost only if you want to publish on the store. To develop an app, you anyway need a mac (or hackintosh), and a device anyway...

-------------------------

Jillinger | 2017-05-17 14:22:43 UTC | #21

Okay. So Urho3D is right up your alley then? What is your experience and opinion of Urho3D?

-------------------------

johnnycable | 2017-05-17 14:32:48 UTC | #22

Well, I've started tampering with it about february... and still I'm messing around... so it's early for me to get the whole picture... flexible it is, and that's important... but you pay a price for it with a more in convoluted pipeline... for now i'm porting some 2d apps i did in cocos to get the feeling, so let's see what happens... 
what's your impression about it?

-------------------------

Jillinger | 2017-05-17 15:26:57 UTC | #23

Well, since I have been learning shaders, because I want to create my own ocean (with realistic rolling waves - hard job :slight_smile:), I haven't really used the engine, other than to create a terrain. However, here is my take...
I like it's features, the examples, and it seems to have potential to produce good games. I kinda like the editor, although I think it's way outdated, and could be improved significantly, so it is not exactly what I was looking for. I was looking for an engine with an editor that allows me to work entirely from (scripting needed only for more game logic - sort of like Game Maker), and with better control, since that would allow me to work faster, and have more time for modeling and artwork. 
So I think that was the only downside for me, so far.
I just came across [Urho's build on](https://www.youtube.com/playlist?list=UUJ3a_7Y2cicwKvR5hQ4ORww), and the editor seems to be what I desire. So I am looking at giving that a try. All in all, I will still be playing with Urho3D, in the same way as I am playing with jMonkeyEngine, because I learn something from each engine, and as I said, I am learning the c++ language from angelscript code.

-------------------------

johnnycable | 2017-05-17 17:01:58 UTC | #24

I see. Then you're probably better off with that. Urho c++ it's much more programmer centric imho. Editor is fine but a bit rough. I still have problem with importing models... 
The sharp/js version are probably more comfortable. Especially if you prefer to work on art...

-------------------------

Jillinger | 2017-05-17 17:55:49 UTC | #25

Yes. Improving the editor I think can do a whole lot for Urho3D.
I think I would enjoy using it more, along with the c++ coding, which I think I am going to enjoy learning, since I like angelscript....appreciate your input.

-------------------------

Sinoid | 2017-05-19 01:51:07 UTC | #26

I do the "oh my god I'm stuck" coding for a friend that uses Godot.

Did you check what perf was like without the Godot editor running? That thing is a machine hog, the only real knock I have on Godot is that the editor is such a painfully slow eating monster. Not a fan of the source-project structure, but it is what it is and livable enough that I don't really complain much on that off day I get dragged into it by my friend.

Don't forget that in that 109fps shot that Godot is still running and rendering behind it ... and it has a whole lot of GUI to render on top of that - there's likely more going on in the GUI than your scene and the 4-way split edit viewport combined and multiplied a few times.

---

Framerates in general:

It's not odd for even *minor work* to drag a framerate down in any project. Going from 100 -> 70 FPS is more meaningful than 1000 -> 300 FPS.

-------------------------

Jillinger | 2017-05-19 02:50:32 UTC | #27

Without the fps, it seemed like it's performance wasn't to my satisfaction. Running on my emulator, it's stalling - that's just with my terrain doing a slow 360.It may also be the case that my other running processes were contributing to the lag. 

However, if the engine itself is hogging my resources, then I wouldn't find it pleasurable to work with. I prefer an engine that allows me to work without too much lag. Hence why I am unable to use UDK, although that seems to be a great engine.

Godot is an easy engine to use, and I think it might do well for games that do not require much detail. I have seen demos of it, all of which appear low poly, but they look great. 

I guess some persons are good at making things work, or I need to get a more efficient pc, like a quad core.

-------------------------

slapin | 2017-05-19 02:53:56 UTC | #28

Well, I was getting "solid" 20fps with Godot without editor. It is fine when editor consumes CPU, but I should be able to see something on optimized builds, but I did not. But that was some time ago, so they could fix this now.
In general I get low frame rates with engines, so having solid 60fps on my i7 2600K is a party!
Only Unity end UE4 gave some solid frame rates. And commercial games. (I use nVidia GTX660).
I was not able to get anything about Godot in 3D. As for 2D it had too many bugs for me to handle,
and there are many much better 2D engines around there to bother. Also high demand on graphics hardware
locked it off my embedded targets, so Godot have no use for me at the moment. But I follow in hope things will
change after some time.
What I like about Godot is script-GUI integration, where one can write some portion in script executable in editor and
get nice properties window Unity style (even better). But inability to get adequate help and inability to get some result
forced me to move on.

-------------------------

