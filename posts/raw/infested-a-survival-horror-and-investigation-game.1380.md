Dave82 | 2017-10-13 02:10:39 UTC | #1

Hi everyone . i'm working on a game for a long time now (5-6 months in my spare time) , and i thought maybe i should post it's current state. First of all few words about the game :

Infested is a survival horror and investigation game where you have to solve some cool puzzles, and collect clues.Actually if you liked the OLD Resident Evil games (RE2 , RE3 , Code Veronica) then you'll probably like this one too.

The story in nuthshell : Scientists made a great leap in quantum physics , they discovered a way to open portals to paralell universes , but the experiment went horribly wrong... the rules of space and time became all scrambled and some evil creatures invaded our side. Your mission is to close the portal and save the world...

EDIT 06.11.2016
New video !

https://www.youtube.com/watch?v=JUlNMutzoFk


Here are some screenshots :
[url=https://postimg.org/image/k10m56a3t/][img]https://s20.postimg.org/k10m56a3t/mansion03.jpg[/img][/url][url=https://postimg.org/image/mys2idui1/][img]https://s20.postimg.org/mys2idui1/mansion06.jpg[/img][/url][url=https://postimg.org/image/r6wi1zrmx/][img]https://s20.postimg.org/r6wi1zrmx/mansion01.jpg[/img][/url][url=https://postimg.org/image/tpq5clquh/][img]https://s20.postimg.org/tpq5clquh/hallway01.jpg[/img][/url]

EDIT 13.04.2016
Weapon test

https://www.youtube.com/watch?v=vLGcXRMFWso


Some differences between Resident evil and Infested :
-TPS camera view instead of fixed cam angle.
- Puzzles are dynamic.While in RE they are just 2d sprites in infested they are interactive 3d objects (Rotate valve handles by dragging them or pressing switches etc)

-------------------------

TikariSakari | 2017-01-02 01:07:20 UTC | #2

The video looked really cool, and you've managed to build quite a big world in half a year. Something that caught my eye on the video was when you picked up an item, you had to move the mouse to the confirm button. I think a lot of new games use some activate button like E or F for confirming their action to make it a bit easier for the player. You might have something like that already implemented, but just thought bringing it up. I also liked how the cross hair changed to hand on things that you could pick up or use like doors.
Good luck with the project in the future.

-------------------------

codingmonkey | 2017-01-02 01:07:20 UTC | #3

It is very impressive
And how did you create this transition between two scenes? when doors opened... black screen... and we see new room (scene)

-------------------------

Mike | 2017-01-02 01:07:20 UTC | #4

Looks great  :slight_smile:

-------------------------

sabotage3d | 2017-01-02 01:07:21 UTC | #5

Looks amazing :slight_smile: Would you reveal some of the techniques that you used ?

-------------------------

rasteron | 2017-01-02 01:07:21 UTC | #6

Looking good so far and great job on the gameplay elements. Your demo scene and mentioning 'evil creatures' reminds me of the game Alan Wake though.  :wink: 

As for improving the video quality, try the ff:

-MPEG4 (DivX, Xvid, H.264) format
-1280x720 resolution or 1080p
-128k Mono or 320k Stereo MP3/AAC audio
-24,25 or 30 frames per second

If you have NVidia card then just use ShadowPlay.

Keep it up!

-------------------------

thebluefish | 2017-01-02 01:07:21 UTC | #7

Hot damn, looking good so far!

-------------------------

gwald | 2017-01-02 01:07:21 UTC | #8

:astonished: Very impressive! :mrgreen:

-------------------------

weitjong | 2017-01-02 01:07:21 UTC | #9

Amazing. After watching the video to the end at full screen, it did not give me a slightest motion sickness. i.e. you have done a great job at adjusting the FOV or something. Are you also the one who create those game assets? They look believable.

-------------------------

Dave82 | 2017-01-02 01:07:21 UTC | #10

Thanks for everyone :slight_smile:

[quote="TikariSakari"]Something that caught my eye on the video was when you picked up an item, you had to move the mouse to the confirm button. I think a lot of new games use some activate button like E or F for confirming their action to make it a bit easier for the player. You might have something like that already implemented, but just thought bringing it up.[/quote]

Well i've just thought the same thing and yes you are right i will change that...

[quote="sabotage3d"]Would you reveal some of the techniques that you used ?[/quote]
Ofcourse ! :slight_smile:

[quote="codingmonkey"]It is very impressive
And how did you create this transition between two scenes? when doors opened... black screen... and we see new room (scene)[/quote]

It's very simple.At segment change i just release all the resources in the current segment and load the new one.It is extremely fast and ensures you can have literally unlimited levels. Most of the entities are derived from Urho3D::Node
So this way i can do recursive things in the scene (destroying resources recursively or load them)
I have a base class called INFNode which is derived from Urho3D::Node and has few virtual methods like :

// Loads this node's static data from a file
virtual void onInitialize(Urho3D::File &fie);

// Builds this node (called when player enters in the segment)
virtual void onBuild();

// Destroys everything associated with this node but keeps the node "alive"
virtual void onDestroy();

// called by projectiles in the scene returns true if the projectile should be stopped (destroyed)
virtual bool onBulletHit(float damage, Urho3D::Vector3 &dir, Urho3D::PODVector<Urho3D::RayQueryResult> &allResults);

So from this INFNode i have various other node types like : 
INFDynamicMesh - holds a StaticModel component which is loaded at onBuild() and destroyed at onDestroy() 
INFItem - holds a StaticModel and quatity
etc

and finally i have a INFSegment which simply calls onBuild() onDestroy() onInitialize() on it's children recursively
Thanks to this technique i have an extremely clean and easy to read code , and its really fast (loading a segment with 37000-38000 poly's is literally a blink of an eye)


[quote="weitjong"]Amazing. After watching the video to the end at full screen, it did not give me a slightest motion sickness. i.e. you have done a great job at adjusting the FOV or something. Are you also the one who create those game assets? They look believable.[/quote]

Thanks ! Well it's the fov and the player's move speed and i set the character controller's friction and mass at very low value. Actually setting the friction to 0 and the mass to 0.5 gives by far the best result unfortunately it has some issues that come from physics simulation (very thin objects on the floor like a sheet of a paper can block the player like theres a wall) 

Regarding to level design and modelling , yes i did everything myself (except that revolver which is only placeholder for now , but i have already a bunch of weapons ready just need to create animations for them)

-------------------------

weitjong | 2017-01-02 01:07:21 UTC | #11

[quote="Dave82"]Regarding to level design and modelling , yes i did everything myself (except that revolver which is only placeholder for now , but i have already a bunch of weapons ready just need to create animations for them)[/quote]
Great! In that case I suppose there is no issue to republish those screenshots and video clips to our main website then.

-------------------------

Bananaft | 2017-01-02 01:07:21 UTC | #12

[quote]Regarding to level design and modelling , yes i did everything myself[/quote]
I was about to ask you about assets origin. Really impressive work.

[quote]very thin objects on the floor like a sheet of a paper can block the player[/quote]
I hope, that you don't make collision mesh for every sheet of paper on the floor. :slight_smile:

What is your lighting solution?

Now, add some spooky ambient sounds. And keep on the great work!

-------------------------

Dave82 | 2017-01-02 01:07:22 UTC | #13

[quote="weitjong"]Great! In that case I suppose there is no issue to republish those screenshots and video clips to our main website then.[/quote]

Actually that would be really cool :slight_smile: (all assets are made by me including the models and textures and sound effects so there's no problem at all) 

[quote="Bananaft"]

I hope, that you don't make collision mesh for every sheet of paper on the floor. 
What is your lighting solution?
Now, add some spooky ambient sounds. And keep on the great work![/quote]

Some meshes have collision , some not... like tree leafs , grass , has no collision bodies but other things have. I render the whole scene in bigest chunks thats possible. I presort everything by material before export. So i don't want to create separate StaticModels for decals on the floor because that icreases the draw calls and material changes.

Currently the game runs constantly on 190-200 fps (thats the max fps as i get the same with empty scene) so the performance is really really great.

[quote]What is your lighting solution?[/quote]
I use combination of baked AO + GI and dynamic lighting. The static scene use Baked lightmaps the dynamic meshes use Dynamic lighting.

Actually i would give my left ball if someone could come up with an idea how to implement subtractive shadows... I have some ideas but i didn't get into Urho source that much yet...

-------------------------

cadaver | 2017-01-02 01:07:22 UTC | #14

Looking very professional, great work!

-------------------------

umen | 2017-01-02 01:07:22 UTC | #15

Amazing work , 
Can you tell us how do you model, that is what is your tricks to make such good textures and human models and animations of the hero? which 3d app you are using ?
How about time management ?how do you handle that ?  (you said its in your spare time ).
also you can build small demo and we can test it if you like .

-------------------------

Lumak | 2017-01-02 01:07:23 UTC | #16

I agree with everyone here, this looks amazing.  Damn, I should learn how to create art assets... my current skills are limited to only being able to create gui buttons, and bad ones at that.

-------------------------

Dave82 | 2017-01-02 01:07:36 UTC | #17

Hi everyone , just few screenshots and some news : 
- added water and particles 
- Have different footstep effects on different materials ,
- walking in water will spawn some splash particles at each step... looks really cool :smiley:.
- Started to write the first puzzle (i already have few for testing but this will be implemented in the game)

Before i release the first demo i want to improve the character controller... the current controller is a bit bugy in certain situations but i have a way beter idea that i just need to implement (to determine the isOnGround and canJump states i will use raycasting instead of collision check... should work better)

The sewers :


what a cool place to fight monsters.. don't you think ?

[img]http://s28.postimg.org/bqs8zifvx/inf_sewer04.jpg[/img]


Sewer...

[img]http://s20.postimg.org/clbiubk6l/inf_sewer02.jpg[/img]


Fire :

[img]http://s20.postimg.org/r72jikgz1/inf_particles01.jpg[/img]

-------------------------

codingmonkey | 2017-01-02 01:07:37 UTC | #18

>what a cool place to fight monsters..
i don't know exactly but i guess you need to work with some of common scary place or "fear factors": 
dark, silent, wet, cold, big place - wind sound, noise sounds( old wood sound, regular single metal sound from far ) ...

-------------------------

gwald | 2017-01-02 01:07:37 UTC | #19

[quote="Dave82"]The sewers :
what a cool place to fight monsters.. don't you think ?[/quote]
Yes, Yes I do think it's scary!

And next are selfies!
[youtube.com/watch?v=EhAFyaObY6U](https://www.youtube.com/watch?v=EhAFyaObY6U)  :astonished:

-------------------------

Dave82 | 2017-01-02 01:07:37 UTC | #20

[quote]i don't know exactly but i guess you need to work with some of common scary place or "fear factors": 
dark, silent, wet, cold, big place - wind sound, noise sounds( old wood sound, regular single metal sound from far ) ...[/quote]

There will be a lot of dark places.This is only 0.01% of the whole game world.Your first objective is to start the locomotive on the train station and go to the city.
There will be 3 levels.
1 the train station. (starts with an animation of the hero calling his wiife and waiting for the train.After he fells asleep and wakes up that people are disappeared , and some strange disturbing unexpected things happening , like giant planets appears disappears on the sky radnomly , creepy quantum events , houses cut in half , etc)
2 The city.(when you arrive the night will fall so you can expect dark areas after the train station part)  Classic scenes like the hospital , mall , airport
3 The labs (typical experiment rooms and stuff)

Hovewer there will be a lot of enemies i still want to focus on puzzle solving and story.I don't want to make an action TPS.

[quote]And next are selfies![/quote]

I don't get that part... :confused:

-------------------------

gwald | 2017-01-02 01:07:38 UTC | #21

[quote="Dave82"]
I don't get that part... :confused:[/quote]
Watch the video, it's scary!

-------------------------

Dave82 | 2017-01-02 01:07:47 UTC | #22

Some test. Now the scripting works as i expected , so what i need now is adding enemies more models and levels and animations and lots of puzzles and investigation stuff.(Well it's not piece of cake thats for sure  :frowning:  )
This demos shows the 3d sound effects , particles , and puzzle solving.
 
[video]https://www.youtube.com/watch?v=h8S7GtCYpns[/video]


And i (hopefully "we" as a friend of mine will also work on the game mostly on story writing and possibly scripting (he's a H.P Lovecraft fan so... i expect a really great story :smiley:) ) setup a facebook page

[facebook.com/infestedgame](https://www.facebook.com/infestedgame)

-------------------------

Lumak | 2017-01-02 01:07:50 UTC | #23

Looking good! The background music sounds great and it creeps me out, and I mean that as a complement.

-------------------------

Dave82 | 2017-01-02 01:08:02 UTC | #24

Testing basic Ai behavior (attack of the twenty zombified twins  :smiley: ). 

[img]http://s20.postimg.org/xqithj52l/ai03.jpg[/img]

-------------------------

Dave82 | 2017-01-02 01:08:07 UTC | #25

Quick PathFinding test. There's no AI yet , for that i need some additional animations , but the Crowd agents works pretty nice so far : 


[video]https://youtu.be/hEdLLpPE4bs[/video]

-------------------------

codingmonkey | 2017-01-02 01:08:08 UTC | #26

cool test, mate) keep it up!

-------------------------

Bananaft | 2017-01-02 01:08:08 UTC | #27

Well, that's looks like a gameplay already. Only needs some blood splatters.

Very cool. Keep up the good work.

Also, never seen a revolver that extracts empty casings with each shot. :slight_smile:

-------------------------

Dave82 | 2017-01-02 01:08:09 UTC | #28

[quote="codingmonkey"]cool test, mate) keep it up![/quote]
Thanks man ! I hope i can release a demo next month

[quote="Bananaft"]Well, that's looks like a gameplay already. Only needs some blood splatters.

Very cool. Keep up the good work.
[/quote]
Thanks ! Few animations more and it is ready for testing


[quote]Also, never seen a revolver that extracts empty casings with each shot. :slight_smile:[/quote]

Haha sorry about that :smiley: The sound effect is for another gun... i will fix that :slight_smile:

-------------------------

Bananaft | 2017-01-02 01:08:13 UTC | #29

[quote="Sinoid"]I have one that let's casings drop out the bottom (WW2 era British optional) using an open cylinder and sleeve.[/quote]

Can you show/name it? Sounds super wierd. Just couple days ago I've learned about Dardick open chamber design. So yeah, there are some.

-------------------------

Dave82 | 2017-01-02 01:08:42 UTC | #30

Well after a small break (busy with life...) i made a video that sums up the gameplay and the design style.

[video]https://www.youtube.com/watch?v=4835XJZY9EM[/video]

And also a small change in the story.We will switch to a "zombie virus outbreak" instead of the "paralell universe" storyline. Simply because there are more potential in it and way more ideas and enemies to work with.
The gameplay and character however remain the same.

-------------------------

codingmonkey | 2017-01-02 01:08:46 UTC | #31

cool!) do you planning add some sort of idle animation for character? I see what he absolutely freezes when he it stay on place and when you open "quest" things.

-------------------------

Dave82 | 2017-01-02 01:09:29 UTC | #32

Hi everyone ! I added FPS mode and it works quite nice ! It adds more to game experience and the gameplay is more fluent.I like it more than the TPS mode.

EDIT : Modified the weapon and the hands a bit :

[img]http://s20.postimg.org/eiiyn0u0d/fpsmode_08.jpg[/img]

[img]http://s20.postimg.org/l9u7yj019/fpsmode_04.jpg[/img]

[img]http://s20.postimg.org/sbnk6ze99/fpsmode_06.jpg[/img]

[img]http://s20.postimg.org/cc4wnfi7h/fpsmode_07.jpg[/img]

-------------------------

Dave82 | 2017-01-02 01:09:49 UTC | #33

ALMOST READY FOR A DEMO !!!
- Added more convenient inventory system
- Worked on weapon and hand animations

Unfortunately i'm still busy with life so the development still goes slow... Working on levels... added some dark areas

[img]http://s20.postimg.org/8q03olyp9/fpsmode_09.jpg[/img]

[img]http://s20.postimg.org/by4l1nkz1/fpsmode_10.jpg[/img]

[img]http://s20.postimg.org/d86zug44t/fpsmode_11.jpg[/img]

-------------------------

Lumak | 2017-01-02 01:09:54 UTC | #34

It's great that your game is really coming along. Looks great.

I haven't read all the posts in this thread and it might have been asked already, but your sky - do you use some type of cloud system?

-------------------------

Dave82 | 2017-01-02 01:09:57 UTC | #35

[quote="Lumak"]It's great that your game is really coming along. Looks great.

I haven't read all the posts in this thread and it might have been asked already, but your sky - do you use some type of cloud system?[/quote]

Hi thanks Lumak ! And nope no cloud system is used , it is a simple skybox.

-------------------------

Lumak | 2017-01-02 01:09:58 UTC | #36

[quote="Dave82"]
Hi thanks Lumak ! And nope no cloud system is used , it is a simple skybox.
[/quote]

Nice, it looks like 3D clouds.  Is it hand painted or generated with some type of tool?

-------------------------

Dave82 | 2017-01-02 01:10:09 UTC | #37

[quote="Lumak"][quote="Dave82"]
Hi thanks Lumak ! And nope no cloud system is used , it is a simple skybox.
[/quote]

Nice, it looks like 3D clouds.  Is it hand painted or generated with some type of tool?[/quote]

Sorry for the late post... I found this skybox on some free site somewhere by searching for "free skybox textures"

-------------------------

Lumak | 2017-01-02 01:10:10 UTC | #38

Ok, cool, found some nice images doing the search.  Thank you.

-------------------------

Dave82 | 2017-01-02 01:11:23 UTC | #39

Creepy zombified doll attacks the player :slight_smile:

[img]http://s20.postimg.org/u7s805f8t/doll01.jpg[/img]

I wish i could have more spare time...

-------------------------

Dave82 | 2017-01-02 01:11:30 UTC | #40

Finished the main character.Looks way better and the color of the clothes fits better in the environment color. it works nice with darker and brighter segments too.It doesn't pop put like the old character.The character was created with Makehuman (an awesome open source character generator).You still need lots of work to reduce , optimize and modify the character to make it usable in a game but still it's a great tool.


[img]http://s20.postimg.org/o5yf2f7fx/nm_01.jpg[/img]

[img]http://s20.postimg.org/jlc8nhnql/nm_02.jpg[/img]

-------------------------

hdunderscore | 2017-01-02 01:11:37 UTC | #41

As others have said, very impressive ! Hard to believe it was done solo in such a short time :astonished:

-------------------------

Dave82 | 2017-01-02 01:11:45 UTC | #42

[quote="hd_"]As others have said, very impressive ! Hard to believe it was done solo in such a short time :astonished:[/quote]

Thanks ! Unfortunatelly polishing and designing takes a lot of time.I finished the complete "pseudo design" of the whole level and now i need to make extreme amount of models and details... But i love it :smiley:

16:9 resolution test. The gui adapts itself to all resolutions.
Also the hud is now fully functional (health and infection bar both decreases if player takes hit and lerps to red color)

[url=http://postimg.org/image/ne6tnqq95/][img]http://s20.postimg.org/ne6tnqq95/whall02.jpg[/img][/url][url=http://postimg.org/image/3jptyqhd5/][img]http://s20.postimg.org/3jptyqhd5/whall04.jpg[/img][/url][url=http://postimg.org/image/yt8cph8x5/][img]http://s20.postimg.org/yt8cph8x5/whall03.jpg[/img][/url][url=http://postimg.org/image/6m6sx0nzd/][img]http://s20.postimg.org/6m6sx0nzd/wronglights.jpg[/img][/url][url=http://postimg.org/image/4d2frcne1/][img]http://s20.postimg.org/4d2frcne1/whall06.jpg[/img][/url]

-------------------------

Dave82 | 2017-01-02 01:11:52 UTC | #43

Changed the animations , now looks way better.(the scene here uses ultra low lightmaps so sorry for the lightmapping artifacts)

[video]https://www.youtube.com/watch?v=vLGcXRMFWso[/video]

finished the "MoviePlayer" class , which plays skinned and transform animations together for cutscenes.Tested it with some mocap animations and looks cool.

-------------------------

Dave82 | 2017-01-02 01:11:58 UTC | #44

Just a small test of cutscene player.The doll's animation is a bit jerky but that's what i have right now :slight_smile:

[video]https://youtu.be/zJfnpEIcNek[/video]

-------------------------

Dave82 | 2017-01-02 01:12:07 UTC | #45

I like alpha mask way better than transparent meshes ! So much opportunity and its out of box solution. Even combined it with lightmaps and works great.
I made textures and lighting darker and desaturated everything a bit.Designing Resident evil style puzzle solving levels is way more harder than i thought... I worked mostly on FPS and tps levels which are lot easier to design. 

vegetation (constant ambient / no lightmaps)
[img]http://s20.postimg.org/k3gus1v1p/nts_01.jpg[/img]


Girders (Alpha mask + lightmap)
[img]http://s20.postimg.org/8fmsxi5wt/nst03.jpg[/img]

-------------------------

Bluemoon | 2017-01-02 01:12:08 UTC | #46

:cry:  I've been seriously hunting for how to use alpha mask

-------------------------

abcjjy | 2017-01-02 01:12:15 UTC | #47

I am an indie developer too. It is incredible to make such a demo in 6 months by just one developer. That's mazing!

I'm quite curious about how you make this. How much effort is spent on the art? And how much is spent on coding? Do you use Urho3d exclusively? AFAIK urho3d's editor is not strong enough, did you invent something specialized editor for your game? What 3d modeling and animation software do you use? Human animation is quite difficult, did you use motion capture solution? It's not usual to see a developer with strong coding, modeling and animation skills. Awesome!

By the way, I think you can put your demo to kickstarter for more support.

-------------------------

Dave82 | 2017-01-02 01:12:16 UTC | #48

[quote="abcjjy"]I am an indie developer too. It is incredible to make such a demo in 6 months by just one developer. That's mazing![/quote]
Thanks ! 

[quote]I'm quite curious about how you make this. How much effort is spent on the art? And how much is spent on coding? Do you use Urho3d exclusively? AFAIK urho3d's editor is not strong enough, did you invent something specialized editor for your game? What 3d modeling and animation software do you use? Human animation is quite difficult, did you use motion capture solution? It's not usual to see a developer with strong coding, modeling and animation skills. Awesome![/quote]

Well i started the project in 2014 october. My first choice was Irrlicht (i didn't heard about Urho3D back then).Unfortunately after a short period of time i realized i will have trouble with it... I had to write everything from scratch.In few months i had sucessfully implemented the :
- Sound (DirectSound or Audiere)
- Particle Engine (SPARK2)
- Navigation Mesh (My own code from scratch using stdlib only)
- Scripting (My own code using stdlib only)
- Gui (My own code using Irrlicht's 2d drawing functions and a INFElement2d base class.Similar to Urho's UI except the quad vertex/index buffers were allocated dynamically so there was no batching.Actually it was quite primitive but it worked pretty well.I had checkboxes , buttons , tabs)
After everything was in alpha state i threw together the fundamentals of the game engine itself to test it.
Well it was very dissapointing... Without offending anyone , Irrlicht was a nice library in 2003... but the lack of modern Hardware support literrally killed the whole project.The worst part was the Skinning which ran on CPU.It was extremely slow... With 5 enemies and with ultra low resolution shadow mapping i had around 30 fps... It was dreadful. Also the built in stencil shadow was ultra slow and useless XEffects was a bit faster but had some issues with the OGL driver.In paralell i started to write a scene exporter for 3ds max which worked perfectly (and still does... i'm using it for Urho) .

So after a lot of struggling : Finding out audiere is linux and window only , SPARK2 was abandoned , NavMesh needed extra features (Offmesh connections , Extra optimisations for dinamic objects , etc) , lack of proper shadow mapping , lack of hardwareSkinning , hardware instancing , No xml support for gui (it was PITA designing GUI from c++)  i just abandoned the whole project because it was too much for one developer... Not to mention the code i wrote was huge , and was really hard to have all that giant chunk of code under control...in the meantime various depressing posts have showed up in the irrlicht forums with titles such as "Is irrlicht Dead?" "Is irrlicht outdated?"... So i just put the project on the shelf and wait until i find some other engine. And i did !! In 2015 i found Urho3D.After i tested it i fell in love with it immediately ! It was a fast modern GAME engine with all feateures i need , it was open source and it was extremely easy to setup and use.

So i had to code everything from scratch but this time i could work on the game itself rather than writing a whole game engine from scratch which is a bad idea if you work alone :smiley:... At this point i had 0 models/levels/textures/sounds ready so i had to start to design levels and make textures.
Most of the time i use 3ds max.I'm using it at least 10 years now , so i feel really home in it's interface. For textures  i use Photoshop , GIMP , and in some rare cases CorelDRAW.
For the animations i use 3ds max and most of the animations are made by hand (once i worked on a small fighting game so i have some experience with hand made animations) But for cutscenes i use Motion Capture (There are tons of them for free.Unfortunately most of them are dirty so you have to clean them first to eliminate twitching but after that they look quite nice)

So thats the story of the game in nuthshell :smiley: i had to code it twice but this time i will finish it , thanks to the wonderful Urho3D !

[quote]By the way, I think you can put your demo to kickstarter for more support.[/quote]
Well i thought about that , and maybe once i reach some of the important milestones i will ! Actually this supposed to be a fangame so i think it fits more in crowd funding area rather than selling it on steam.


[quote="Bluemoon"]:cry:  I've been seriously hunting for how to use alpha mask[/quote]
Hi ! Well it is just a standard material with a *AlphaMask technique.Since it is a fake transparency and can be rendered as a normal material , all your sorting/overlapping headaches will disappear once you start using it :smiley: Define LIGHTMAP in the technique and put lightmap in emissive unit and voila you have lightmapped alpha mask

-------------------------

Dave82 | 2017-01-02 01:12:27 UTC | #49

Finally tested the dynamic light + static lightmaps combinations.AND WORKS BEAUTIFULLY ! 
The issue mentioned here : [topic1105.html](http://discourse.urho3d.io/t/problems-with-lightmaps-dynamic-lights/1073/1)
The problem is that lights are additive so baked lighting will become extremely bright if one more additive pass is applied (dynamic lights).The solution is to bake the indirect lighting only and use dynamic lights for direct lighting.The result is awesome : 

[img]http://s20.postimg.org/eefvg48vh/sewer06.jpg[/img]

[img]http://s20.postimg.org/k3w40ff1p/sewer07.jpg[/img]

-------------------------

Lumak | 2017-01-02 01:12:27 UTC | #50

Awesome job blending dynamic and static lighting - these new images look great!  Personally, I thought the previous posted images looked a bit dark, and now, wow the difference is night and day.

-------------------------

Cpl.Bator | 2017-01-02 01:12:28 UTC | #51

Awesome ! did you plan to release a single demo ? and can you speak about your workflow ?
Thanks !

-------------------------

Dave82 | 2017-01-02 01:12:29 UTC | #52

[quote="Cpl.Bator"]Awesome ! did you plan to release a single demo ? and can you speak about your workflow ?
Thanks ![/quote]


Hi ! Thanks ! Yes i plan to release a demo as soon as possible.Unfortunately i'm busy with life but If you have a question don't hesitate to ask.I will answer ASAP.

-------------------------

Dave82 | 2017-01-02 01:13:58 UTC | #53

Just some shots to show you i'm still working on it :smiley:

[img]https://s20.postimg.org/gwj3tb3ql/newts01.jpg[/img]


[img]https://s20.postimg.org/3tnha1dil/newts02.jpg[/img]


[img]https://s20.postimg.org/60rpxyist/newts04.jpg[/img]

-------------------------

Dave82 | 2017-01-02 01:14:20 UTC | #54

**The imgaes were too big so i removed them ***

-------------------------

Lumak | 2017-01-02 01:14:21 UTC | #55

Nice! Your game looks so polished, are you near Beta release anytime soon?

-------------------------

Dave82 | 2017-01-02 01:14:22 UTC | #56

Thanks ! I hope so ! The problem is i have only few hours of spare time in a week.I have a small company (not programming related) where i have some trouble right now so i'm just runnig place to place to fix things , and when i get home i'm just too tired to do anything else than start watching 10 minutes of some 80's slasher movie and fall asleep...:smiley: 

Everything is 90 % ready , for an alpha release just need few animations and models to be done.

-------------------------

Lumak | 2017-01-02 01:14:24 UTC | #57

[quote="Dave82"]Everything is 90 % ready , for an alpha release just need few animations and models to be done.[/quote]

Nice. I'm looking forward to the release. Completing the last 10% has always been more stressful than the first 90% :wink:

-------------------------

Dave82 | 2017-01-02 01:15:00 UTC | #58

Hi everyone ! I just made an update to the game.Adding new features and making everything more smooth.Here are the new features :
- Female character with cool textures (found it on the internet it was really hard to rig it as it comes with very awkward pose :neutral_face: )
- New better item pick up and inventory dialog (it uses only the keyboard to select/pick up items.The mouse interaction was removed , now is way more convenient)
- New animations.More smooth and better transitions.(Zombies are still choppy but thatt next thing i will working on)
- 12 New zombie models from an old TGC model pack.(They look tolerable).Whats cool there are 2 texture variations for each model and the models are only 6000 polys each
- Some internal changes that makes the further development a lot easier (cleanup , simplifying some code  ,etc)
- Added billboards for simulating fog , dust and other cool effects.
- Started rebuild lightmaps for segments (Instead of baked complete lightmaps i render only indirect lighting and AO and use dynamic lights for direct lighting and dynamic shadows).You can see this feature in the demo video BTW

The only problem that i didn't checked my fraps settings and i recorded half size screen again... The videoended up in a terrible 380p quality but i just don't have patience/time right now to record another one so sorry about this :smiley: but i promise next time i will upload a proper 720p hq video.

EDIT : Sorry for the spelling errors in the video... :frowning:


[video]https://www.youtube.com/watch?v=JUlNMutzoFk[/video]

-------------------------

S.L.C | 2017-01-02 01:15:00 UTC | #59

Damn, I thought it was iron-man with that light coming from her chest :smiley: Looks nice so far.

-------------------------

Dave82 | 2017-01-02 01:15:25 UTC | #60

Few shots of the classic Resident evil "fixed security camera" camera style.This gives some real retro survival horror feeling :slight_smile: Since this is just a modified version of the TPS character controller , it will be a selectable mode in the main menu

[img]https://s20.postimg.org/j5l6g23ot/fixed01.jpg[/img]

[img]https://s20.postimg.org/yi4xa32ul/fixed04.jpg[/img]

[img]https://s20.postimg.org/mdpnt3pyl/fixed02.jpg[/img]

[img]https://s20.postimg.org/5egpduer1/fixed03.jpg[/img]

And finally a flashlight idea (the beam is currently photoshopped...)
[img]https://s20.postimg.org/y4cs1yxil/fixed05.jpg[/img]

-------------------------

Dave82 | 2017-02-10 08:01:12 UTC | #61

Hi all ! I didn't post a comment in the new forum yet so it's about time to do it :D .Anyway... i have some spare time so i continue to expand the sewer and train station levels of the game. Here are few shots >

<img src='//cdck-file-uploads-global.s3.dualstack.us-west-2.amazonaws.com/standard17/uploads/urho3d/original/1X/c80a39fdb7852ad4c427a2a343364be0bd0788f5.jpg'>
-
<img src='//cdck-file-uploads-global.s3.dualstack.us-west-2.amazonaws.com/standard17/uploads/urho3d/original/1X/ce848b4bc942bae72931b996ffda28fa083235b9.jpg'>
-
<img src='//cdck-file-uploads-global.s3.dualstack.us-west-2.amazonaws.com/standard17/uploads/urho3d/original/1X/9759559f75d83d65e78c911a3eeb2864c3a045a2.jpg'>
-
<img src='//cdck-file-uploads-global.s3.dualstack.us-west-2.amazonaws.com/standard17/uploads/urho3d/original/1X/860e9dbf46b7eeafdd464c2709be53edf37fb7b5.jpg'>

-------------------------

hdunderscore | 2017-02-10 09:22:54 UTC | #62

It's always very cool to see this project progressing ! Great work on keeping up the level of quality over time :D

-------------------------

Dave82 | 2017-07-31 09:00:52 UTC | #63

Hi ! After my HDD , GPU and Power supply wrecked , i'm back with a youthful enthusiasm and a new PC :smiley:
With new compilers and operating system i found out there is a bug in the game (Some bad resource handling somewhere) which causes random crashes.On XP it was very rare so i couldn't track it down but on win7 is more frequent so i already isolated the bug i just need to find the exact piece of code which causes the crash

My other problem i mentioned somewhere above is also solved.-->The textures <--Finding specific textures on the net , and  editing them to match to each other (contrast , colorkey , saturation ,etc) is a really , really slow procedure.I waste a vast amount of time on this and it gets me nowhere really. So i wrote a small desturation shader which desaturates the screen by 60%.This makes all the textures match to each other automatically and gives the levels more creepy horroristic look.Here are some screen shots (compare them to my the older images to see the difference)

Exterior scene .It looks great even wothout GI lightmap ! (Simple dynamic directional light is used)
[img]https://s20.postimg.org/re5q5m3ot/image.jpg[/img]

[img]https://s20.postimg.org/4s0esvpyl/image.jpg[/img]

[img]https://s20.postimg.org/fhe3l51rh/image.jpg[/img]

[img]https://s20.postimg.org/h1jfjja5p/image.jpg[/img]

[img]https://s20.postimg.org/xix8ixvsd/image.jpg[/img]

-------------------------

Victor | 2017-07-30 22:47:55 UTC | #64

Wow, that's looking good!

-------------------------

slapin | 2017-07-30 23:03:15 UTC | #65

Yay!!! Cool!!!

Do you use custom shaders for human skin?

-------------------------

Dave82 | 2017-07-31 10:09:54 UTC | #66

@Victor : Thanks :) 

@Slapin : Nope , it's just a simple diffuse material but i plan to add some cool shiny specular map for the clothes.

-------------------------

slapin | 2017-07-31 10:16:06 UTC | #67

Looking forward to it!

-------------------------

Dave82 | 2017-10-13 01:09:26 UTC | #68

Just removed the eyelashes and other unnecessary "details" that were rather pesky than visually appealing and guess what.She turnet out to be a real hottie :)   

[IMG]https://s20.postimg.org/ai4gjfo31/image.jpg[/IMG]
[IMG]https://s20.postimg.org/od2r1wii5/image.jpg[/IMG]

-------------------------

Dave82 | 2017-10-20 02:26:38 UTC | #69

Finally ! The game works and looks as i expected.just need more level design , textures and models and animations
I also created a desaturation/contrast/brigtness combo sahder which acts as a cheap color grading effect. (Note the greenish effect in the video).Also logic , triggers , animations (mocap ,and simple frame based graph transforms) , pathfinding is done.Modified the main hero's animations (without weapon and flashlight the runing and walking is a cleaned mocap , with weapon and flashlight is generated) The Inventory and other UI based thingies are also work.Here's a short video of all this put together.

(NOTE : Before you ask , No , the monster in the video is not a l4d tank.Its a very similar monster from a model pack)

https://www.youtube.com/watch?v=EX0ipnybIrA

-------------------------

Modanung | 2017-10-20 08:59:35 UTC | #70

Looking really good!
Careful with those high heels on that grate. ;)

-------------------------

Dave82 | 2018-03-14 01:35:52 UTC | #71

Playing with lightmaps.Tried a different method and it worked really nice ! Photometric lights can produce extremely beautiful results.Also testing the old Resident Evil style character controller (fixed camera angle and position while the character moves freely in the scene) Works and feels better than the default TPS controller.Watch the blob shadow under the character's feet :D
[url=https://postimg.org/image/tfg8fz6ll/][img]//cdck-file-uploads-global.s3.dualstack.us-west-2.amazonaws.com/standard17/uploads/urho3d/original/2X/8/858e2189dc79f6501ba83b9be32ee2feed6e8158.jpg[/img][/url][url=https://postimg.org/image/9ku6tw1op/][img]//cdck-file-uploads-global.s3.dualstack.us-west-2.amazonaws.com/standard17/uploads/urho3d/original/2X/d/d306986c2d25a48e5d5b76ab68992fc2e9ecb38a.jpg[/img][/url][url=https://postimg.org/image/e808v4mbd/][img]//cdck-file-uploads-global.s3.dualstack.us-west-2.amazonaws.com/standard17/uploads/urho3d/original/2X/8/8d1140fb5f5b98c75ba853c217f1452886780244.jpg[/img][/url][url=https://postimg.org/image/n3135n3e1/][img]//cdck-file-uploads-global.s3.dualstack.us-west-2.amazonaws.com/standard17/uploads/urho3d/original/2X/f/f7019eac2c4f18e9641f396aaa7a3ee229cc4df8.jpg[/img][/url][url=https://postimg.org/image/t2ou9v17d/][img]//cdck-file-uploads-global.s3.dualstack.us-west-2.amazonaws.com/standard17/uploads/urho3d/original/2X/4/44f1bc08e8a932d768973af992fb17ce9dd10914.jpg[/img][/url][url=https://postimg.org/image/u68yl9o95/][img]//cdck-file-uploads-global.s3.dualstack.us-west-2.amazonaws.com/standard17/uploads/urho3d/original/2X/7/78e091350a14140fc21932e8bc0e6cf53a9d1723.jpg[/img][/url][url=https://postimg.org/image/hdkulucsp/][img]//cdck-file-uploads-global.s3.dualstack.us-west-2.amazonaws.com/standard17/uploads/urho3d/original/2X/9/90db47bf873afe973b8bb87eb5620c4bd61eefeb.jpg[/img][/url]

-------------------------

Dave82 | 2019-01-11 01:37:46 UTC | #72

Resident evil style gameplay. Pre rendered backgrounds. It really looks like a resident evil clone but i can say that this camera style and gameplay is MIND BLOWINGLY awesome. It's the best controller type so far. The slow gameplay and the smaller areas give a REAL survival horror experience and makes you want to play more ! With the tps and fps controllers i used before never had this kind of experience. They demanded action.Lot of shooting , large levels , fast runing and made you forget that you actually playing a survival horror game.They just didn't fit...

A small demo of a simple corridor thrown together for testing.

https://www.youtube.com/watch?v=YpHpC0adJRE

-------------------------

Dave82 | 2019-02-17 20:38:42 UTC | #73

Added AO map to the character diffuse and use a cheap light effect to make the character fit in the scene regardless of light intensity.So far if the area was too dark the character would be completely black or really stand out due to incorrect ambient lighting.I use a constant directional light which always has the same direction as the camera so the character is always lit from a direction even if there is no light source nearby.

![image|690x410](upload://c23oe3gx6gu4EvshM2ld9Xx5Rbh.jpeg) 

No light source (only constant directional) + ambient and the character still looks cool. Oh, and the AO is doing a great job too.
![image|690x414](upload://g5EUqJ3DmHKsfHjvIcZaExtwLi8.jpeg)

-------------------------

Dave82 | 2019-05-22 22:08:38 UTC | #74

After a hell of a work i was able to convert mixamo animations to max bipeds and tested on a model which is not anatomically correct but is a real game character so it looks and feels better than the makehuman version. Yet another lesson learned : if you want quality you'll need to involve commercial software (IClone or Fuse) to have the job done. (unless you're not a pro character modeller and unwrapper which i'm not)
So here is a test of it : 
https://www.youtube.com/watch?v=GKx45Adpdxw

-------------------------

Leith | 2019-05-23 11:18:45 UTC | #75

Love your work! Also, nice model!

I see you're using a dynamic character controller with no foot slipping solver... There's a bit of foot slipping happening during locomotion.

That's an issue I spent a lot of time solving, both for dynamic and kinematic controllers. If you want to pick my brain any time, feel free.

-------------------------

Dave82 | 2019-12-22 22:22:11 UTC | #76

Today i added a new inventory to the game but the real improvement is that i can now mix 3d scenes with 2d UI elements without RTT ! Now any material type is allowed to be displayed in the inventory. And finally i am starting to understand how the render path works (not there yet but a lot closer) so i was able to figure out a solution for a custom depth map in the render procedure... Theoretically it will be very easy to do
So here are a demo of the inventory : 
https://youtu.be/R8rxSwQG6jk

-------------------------

Dave82 | 2020-03-02 21:18:57 UTC | #77

Hi ! I was finally able to put all the achievements together. All features are included in this video. Dynamic shadows , custom z depth pass , scripted ai (unfortunatelly attack animations are missing so no matter how hungry those zombies are they can't do much )

The new level design is also cool. I think at some point it even looks better than overcomplicated materials and light calculations. Puzzles are working. No need for c++ coding anymore all puzzles and enemy AIs can be scripted in AS with no extra hassle.

Watch the video in fullscreen. For maximum resolution and clearness
Never been so close to release the first demo !

https://youtu.be/qHLQ2q_rJNk

Regards

-------------------------

George1 | 2020-03-02 22:45:01 UTC | #78

This need to be on the WIP front screen of the website.  

For water splash, maybe reduce the intensity of the splash based on speed.

-------------------------

Modanung | 2020-03-03 22:08:55 UTC | #79

Looking good!
I noticed the blood is *very* dark, you could try making it slightly emissive. This worked for me in heXon.

...or even better, make it some awesomely translucent custom shader.

-------------------------

GodMan | 2020-03-03 18:32:46 UTC | #80

Reminds me of a cross between Resident Evil and Silent Hill.

-------------------------

Dave82 | 2021-03-26 07:36:53 UTC | #81

Finished the main menu and the combat system. The combat system needs a bit tweaking (turning should be smoother) but otherwise it works like i imagined. The same logic should be used for all enemies in the game. (it is very similar how it was done in Resident evil games). Also the point light shadow caster is looks way better than the previous directional shadow caster. You can see the long distorted shadows which adds more to the horror atmosphere.

https://www.youtube.com/watch?v=hsKUskvQiq8

-------------------------

George1 | 2021-03-27 02:45:01 UTC | #82

Looking great.  Your gun fire/spark comes out a bit late, should be just before the smoke.

-------------------------

JSandusky | 2021-03-27 04:41:28 UTC | #83

Looks pretty amazing.

-------------------------

johnnycable | 2021-03-27 16:16:15 UTC | #84

That's great. It reminds me of goo'ol alone in the dark, the original one (ninety something); fixed cameras, nifty atmosphere...
Graphically very good. Looks gorgeous.
"Their" animations feels ok, but I'd polish them some more.
And twist those candles a little.

-------------------------

evolgames | 2021-03-27 16:38:36 UTC | #85

How long have you been working on this? Looks great, and nice to see it coming along.

-------------------------

Dave82 | 2021-03-28 00:23:02 UTC | #86

[quote="johnnycable, post:84, topic:1380"]
Their” animations feels ok, but I’d polish them some more.
[/quote]

Hehe. These are the best mocap animations you get for free :D 99% of free mocaps are useless garbage. These took me about 3 weeks to clean and remove the feet and head jiggling as much as possible . I found some cool free (creative Commons) models (include ornate candlesticks) sketchfab so i will probably replace some of them in the future.

[quote="evolgames, post:85, topic:1380, full:true"]
How long have you been working on this? Looks great, and nice to see it coming along.
[/quote]
Well i started it long time ago. 3-4 years or more. In the beginning i had more time to work on it , but now i'm busy with all kind of crap so i work on it when i find some spare time. But i absolutely love working on it even if it goes extremely slow :D

-------------------------

johnnycable | 2021-03-29 14:55:08 UTC | #87

[quote="Dave82, post:86, topic:1380"]
Hehe. These are the best mocap animations you get for free :smiley: 99% of free mocaps are useless garbage. These took me about 3 weeks to clean and remove the feet and head jiggling as much as possible . I found some cool free (creative Commons) models (include ornate candlesticks) sketchfab so i will probably replace some of them in the future.
[/quote]

Not sure... hasn't Mixamo some zombie-ish anims...?

-------------------------

Dave82 | 2021-03-29 16:51:41 UTC | #88

There are few walking and falling but they're not that great either.

-------------------------

johnnycable | 2021-03-30 15:03:35 UTC | #89

I see... then it's gore-time again :woman_zombie: :zombie: :woman_zombie: :zombie: :open_mouth:

-------------------------

Dave82 | 2021-10-07 12:19:08 UTC | #90

Just a small update and feature demonstration !  Screen acrolling
So testing on different PCs i was facing a huge problem. Since the aspect ratio of the pre rendered backgrounds are fixed we can only display them on monitors with the sam aspect ratio , otherwise the background will be squashed and not that it won't look good but screen positions on this squashed image are no longer compatible with the 3d perspective view. Eg every 3d element on this bacground will be rendered off. So i implemented a solution the sam way as capcom did it. Render the game to a same virtual resolution as the backgrounds and then scroll this final 2d image on the screen depending where the player is standing. Here is a cool example of it
Notice the scrolling screen every time the player approches the top or the bottom of the screen
https://m.youtube.com/watch?v=YS5jrr4uIiA

-------------------------

GodMan | 2021-10-17 19:34:43 UTC | #91

Great job @Dave82 

Looks great

-------------------------

Dave82 | 2022-08-12 09:51:11 UTC | #92

Forgot to post here the PBR version of the game. I was able to do exactly the same as in the classic renderpath (prerendered backgrounds + invisible meshes rendered in depth only for receiving shadows)
So now looks so cool ! Too bad i have really no time to work on this right now but i would really like to

https://www.youtube.com/watch?v=mpmWxGn42Ms

-------------------------

