Enhex | 2018-03-12 09:30:09 UTC | #1

Fast paced first person shooter.
Fight against dozens of monsters at once, trying to dodge your way to the exit alive.
Test your skill and see if you can score level medals.

Comes with modding support:
 - Level editor
- Extensible scripting, and script-side game features like monsters, weapons, pickups, and more.

**Video:**
https://www.youtube.com/watch?v=uKxrxcx88QA

Steam: http://store.steampowered.com/app/793620/Hellbreaker/
Itch.io: https://enhex.itch.io/hellbreaker

----------

Please follow this project on:
[Twitter](https://twitter.com/Enhex) | [YouTube](https://www.youtube.com/user/enhex) | [Tumblr](https://enhex.tumblr.com/) | [Discord](https://discord.gg/VNr5dUQ) | [Reddit](https://www.reddit.com/r/Hellbreaker/)

-------------------------

Nerrik | 2017-01-02 01:09:16 UTC | #2

nice work :slight_smile:

-------------------------

Bananaft | 2017-01-02 01:09:16 UTC | #3

Really cool. Congratulations on your milestone!

What lighting technique you are using here?

-------------------------

Enhex | 2017-01-02 01:09:16 UTC | #4

[quote="Bananaft"]Really cool. Congratulations on your milestone!

What lighting technique you are using here?[/quote]

Deferred lighting. Most lights are shadowless points.

-------------------------

Bananaft | 2017-01-02 01:09:16 UTC | #5

[quote="Enhex"]Deferred lighting. Most lights are shadowless points.[/quote]

So, MSAA setting does nothing then :slight_smile:

Some places look very nice. Keep up the good work.

-------------------------

codingmonkey | 2017-01-02 01:09:16 UTC | #6

This is absolutely great!
So how yours level are builded? Did you use modularity for level assets or you are use one solid mesh for rooms ?
Did you trying use occluder option for walls to speed up rendering ? 
Do you planning use shadows ?

-------------------------

rasteron | 2017-01-02 01:09:16 UTC | #7

Nice! this reminds me of Doom :slight_smile:

-------------------------

Enhex | 2017-01-02 01:09:17 UTC | #8

[quote="codingmonkey"]This is absolutely great!
So how yours level are builded? Did you use modularity for level assets or you are use one solid mesh for rooms ?
Did you trying use occluder option for walls to speed up rendering ? 
Do you planning use shadows ?[/quote]

I'm not using modularity, I don't like it because it limits the level design and things tend to look the same. I have my own level editor which has similar workflow to BSP-based editors.

Yes I am using occluder option to speed up rendering for level geometry, since it's made from, relatively few, big triangles.

I am using shadows only with directional light and level geometry for now. I might use billboards for enemies so shadows won't be used anyway later on.
I'd like to use lightmaps + light probes.

[quote="rasteron"]Nice! this reminds me of Doom :slight_smile:[/quote]
Game design is inspired by it.

-------------------------

Bananaft | 2017-01-02 01:09:19 UTC | #9

[quote="Enhex"]I'd like to use lightmaps + light probes.[/quote]

Why? Why so many people want to use baked lighting? It's a lot of work to build and support, it's hard to work with, has lots of limitations, requires rebaking on every change in the level. And all that for pale, washy, inexpressive and absolutely static result.

While with deferred lighting you can have flickering and blinker lights, moving lights, put a point-light on every projectile, weapon flash, hit effect, you can make every light on the level breakable, you can have enemies with flashlights looking for the player in the dark.

-------------------------

Enhex | 2017-01-02 01:09:19 UTC | #10

[quote="Bananaft"]
Why? Why so many people want to use baked lighting? It's a lot of work to build and support, it's hard to work with, has lots of limitations, requires rebaking on every change in the level. And all that for pale, washy, inexpressive and absolutely static result.

While with deferred lighting you can have flickering and blinker lights, moving lights, put a point-light on every projectile, weapon flash, hit effect, you can make every light on the level breakable, you can have enemies with flashlights looking for the player in the dark.[/quote]

Dynamic and static lights aren't mutually exclusive.

With baked lights you can do expensive stuff like bouncing light, glowing surfaces and more. The result will be much better looking.
From aesthetics point of view real time lights are the limited option.
With light probes you can use the lightmaps to light dynamic objects, which will take into account bounced lights and such.

There are ways to turn on/off baked lights, AFAIK you could have 2 versions of the affected lightmap parts and switch between them or something like that.
Or you could just use dynamic lights in that case.

Also while in development you don't have to rebake the lightmap every time, or at least not in high quality.

-------------------------

rasteron | 2017-01-02 01:09:19 UTC | #11

[quote]I'd like to use lightmaps + light probes.[/quote]

Hey, I guess we are on the same boat here.  :wink:  Btw, did you figure out a solution for Urho3D to blend static + dynamic shadows?

-------------------------

Enhex | 2017-01-02 01:09:20 UTC | #12

[quote="rasteron"][quote]I'd like to use lightmaps + light probes.[/quote]

Hey, I guess we are on the same boat here.  :wink:  Btw, did you figure out a solution for Urho3D to blend static + dynamic shadows?[/quote]
Nope. You could exclude a light that casts shadows from the baking but I don't know how well it will blend.

-------------------------

codingmonkey | 2017-01-02 01:09:21 UTC | #13

>Why? Why so many people want to use baked lighting?
just for in addition of theme of "lightmaps using"  today find this topic : [cybergooch.com/tutorials/pag ... _rfom5.htm](http://www.cybergooch.com/tutorials/pages/lighting_rfom5.htm)

-------------------------

Enhex | 2017-01-17 18:59:20 UTC | #14

Made some progress.
Bullet tracers, bullet impact sparks, muzzle flash, blood splashes, blood stains, HUD hands placeholder, better fireball placeholder, gameplay balancing, optimizations and more.

https://www.youtube.com/watch?v=kLSY2y11-Fw

-------------------------

valera_rozuvan | 2017-01-02 01:09:29 UTC | #15

So awesome! Keep it up = ) I think this will become a very cool and known game once you finish polishing it.

-------------------------

Enhex | 2017-01-17 18:59:42 UTC | #16

Recent test videos:
https://www.youtube.com/watch?v=n3NH94vzho8
https://www.youtube.com/watch?v=TTCURhRHKjw

-------------------------

thebluefish | 2017-01-02 01:10:52 UTC | #17

Love the minigun test video. Nice work so far dude!

-------------------------

Lumak | 2017-01-02 01:10:52 UTC | #18

Looking good! I also like the mini gun, it's OP.

-------------------------

codingmonkey | 2017-01-02 01:10:52 UTC | #19

nice, but minigun looking slightly light-weight. I guessing you need add some heavy effect for it, long starting to firing and add slow-movement with it. also i think will be nice looking with some effect like rollback-forces for hands when minigun do firing.

-------------------------

Enhex | 2017-01-02 01:10:52 UTC | #20

[quote="codingmonkey"]nice, but minigun looking slightly light-weight. I guessing you need add some heavy effect for it, long starting to firing and add slow-movement with it. also i think will be nice looking with some effect like rollback-forces for hands when minigun do firing.[/quote]
Longer spin time would be nice but I'd have to use an easing curve to make sure the start is quick so it won't take too long before it's usable.
Movement weapon sway is currently the same for everything. Making it weapon specific could be done.
Not sure what rollback-force means.

-------------------------

codingmonkey | 2017-01-17 19:02:15 UTC | #21

sorry for my bad English I mean this force (1:29)  
[spoiler]
https://www.youtube.com/watch?v=QYeDukz6qgg
[/spoiler]

-------------------------

Enhex | 2017-01-02 01:10:52 UTC | #22

Ah, recoil. I don't have recoil in my game, only cone of fire (design choice).

-------------------------

Enhex | 2020-04-16 20:33:23 UTC | #23

New video:
https://www.youtube.com/watch?v=B7d8nO2I5o4

-------------------------

Modanung | 2017-01-02 01:11:19 UTC | #24

Looking good!

-------------------------

cadaver | 2017-01-02 01:11:19 UTC | #25

Very nice classic FPS gameplay. Brings the C4 engine FPS demo levels to mind a bit.

-------------------------

jenge | 2017-01-02 01:11:19 UTC | #26

Really nice movement/camera work, sorry if I missed this in the scrollback, are you using a Bullet character controller setup or something simpler?

-------------------------

Enhex | 2017-01-02 01:11:19 UTC | #27

[quote="jenge"]Really nice movement/camera work, sorry if I missed this in the scrollback, are you using a Bullet character controller setup or something simpler?[/quote]
I wouldn't recommend Bullet's character controller, it has flawed recovery from penetration and I don't think it's possible to make quality Kinematic controller, Bullet just falls apart in my very painful experience.
I'm using dynamic controller with my own suspension system for a "leg".

-------------------------

jenge | 2017-01-02 01:11:19 UTC | #28

That is really cool, and yeah, getting real physics to behave like this and handle corner cases without exploding is nuts.  You can always attach some kind of sphere or something to the player which does rough, "I just knocked over a pile of crates!" physics... looks great!

-------------------------

Enhex | 2017-08-09 14:20:14 UTC | #29

New test video:
https://www.youtube.com/watch?v=ZnAAEonOdiw

-------------------------

Enhex | 2017-08-09 14:20:37 UTC | #30

Progress:
https://www.youtube.com/watch?v=1jzHm1l_hGo

-------------------------

Enhex | 2017-08-09 14:20:31 UTC | #31

New video:
https://www.youtube.com/watch?v=ZtIbDo-9VLQ

-------------------------

sabotage3d | 2017-01-02 01:11:58 UTC | #32

Pretty cool. Are there any shadows from the creatures and objects on the ground?

-------------------------

Enhex | 2017-01-02 01:11:59 UTC | #33

[quote="sabotage3d"]Pretty cool. Are there any shadows from the creatures and objects on the ground?[/quote]
I'm not using shadow casting lights because it's too expensive for my use case (except directional light shadows, which isn't very useful for indoors).

Maybe using lightmaps for static models so only dynamic models are included for the dynamic shadows would make it affordable, but that's a rather low priority now.

Another option is to exclude the level geometry from the directional light shadow, so directional light "penetrates" the level geometry and causes monsters and such to cast shadows. Might try that.

-------------------------

Bananaft | 2017-01-02 01:11:59 UTC | #34

You are making great progress. It already seems like it will get better reviews than DooM multiplayer beta :slight_smile:

-------------------------

Enhex | 2017-01-02 01:11:59 UTC | #35

[quote="Bananaft"]You are making great progress. It already seems like it will get better reviews than DooM multiplayer beta :slight_smile:[/quote]
lol yeah, I should probably focus on getting it on Steam Greenlight ASAP, strike while the iron is hot.

-------------------------

boberfly | 2017-01-02 01:12:00 UTC | #36

Very cool Enhex!!!

For some reason it reminds me of Painkiller, maybe it's the demon design? Which is a great thing, twitch shooters FTW!

About the new Doom, I am a sucker for fatality kills it reminds me of the most recent AVP which came out a few years ago. But yeah, gimping it to play like a poor man's CoD or Halo is a bad move. The virtual texture stuff is neat though, 60fps with very nice texture variety without expensive mixer shaders...

-------------------------

Enhex | 2017-08-09 14:21:59 UTC | #37

Ported my level editor from OGRE to Urho3D, and refactored several things.

Short updated video:
https://www.youtube.com/watch?v=L0UCSpDdwyY

Improved LVL file format.
Automatic material system with diffuses/normal/specular/emissives (previously was diffuse only).
Assets and effects improvements.

-------------------------

jenge | 2017-01-02 01:13:30 UTC | #38

Love it! Kind of feels like Sauerbraten meets the new DOOM :slight_smile:

-------------------------

namic | 2017-01-02 01:13:30 UTC | #39

I'm really curious about your level editor. Is it implemented with CSG/BSP operations based on primitives, or are you actually creating proper geometry procedurally with something like 34_DynamicGeometry? How do you deal with UV's?

-------------------------

Enhex | 2017-01-02 01:13:30 UTC | #40

[quote="namic"]I'm really curious about your level editor. Is it implemented with CSG/BSP operations based on primitives, or are you actually creating proper geometry procedurally with something like 34_DynamicGeometry? How do you deal with UV's?[/quote]

No CSG/BSP, I'm using what I call shapes which are a collection of polygon faces.
Each face has material which includes name, uv plane, and transformation (scale/rotation/translation), and when I triangulate the faces I calculate the UV for each vertex based on the uv plane & transformation.

-------------------------

namic | 2017-01-02 01:13:31 UTC | #41

Are you using Assimp's TriangulateProcess?

-------------------------

Enhex | 2017-01-02 01:13:32 UTC | #42

[quote="namic"]Are you using Assimp's TriangulateProcess?[/quote]
No.
I wrote my own triangulation, I modified the ear clipping algorithm to handle 3D non-planar polygons.

-------------------------

TheComet | 2017-01-02 01:14:32 UTC | #43

This looks sick! :smiley: Reminds me a lot of Quake, keep it up!

-------------------------

Enhex | 2017-02-05 18:24:28 UTC | #44

New video:
https://www.youtube.com/watch?v=roTJX0L37pk

-------------------------

boberfly | 2017-02-09 00:08:21 UTC | #45

Insane progress Enhex! Looks great

-------------------------

Enhex | 2017-04-28 09:20:29 UTC | #46

New video:
https://www.youtube.com/watch?v=osQP6q5B_y4

Many bug fixes and improvements like monster rotation lerp'ing, material fixes, GUI improvements, end screen, resource & shader preloading, and many more...

-------------------------

Victor | 2017-04-28 11:44:13 UTC | #47

I really enjoy watching these videos. You've done an amazing job so far man. :)

-------------------------

Enhex | 2017-08-09 14:34:19 UTC | #48

New video:
https://www.youtube.com/watch?v=eLEoZKYZiPw

* Level medal system which encourages to play fast but not skip combat
* level editor improvements, progress with new levels
* improved effects, and new effects such as monster blood explosion
* explosion push force
* bug fixes, optimizations, code refactoring.

-------------------------

coldev | 2017-08-09 20:00:42 UTC | #49

Cool game.. nice  effects and bullet / enemy animations

-------------------------

Enhex | 2017-09-04 18:47:48 UTC | #50

New screenshots and follow links:

<a target="_blank"  href="http://i.imgur.com/Ux33cXv.jpg"><img src='//cdck-file-uploads-global.s3.dualstack.us-west-2.amazonaws.com/standard17/uploads/urho3d/original/1X/1ae51fc9649ba8a3048b6538584dfa5fb1cb982e.jpg' height="100px"/></a> <a target="_blank"  href="http://i.imgur.com/yxDI9ji.jpg"><img src='//cdck-file-uploads-global.s3.dualstack.us-west-2.amazonaws.com/standard17/uploads/urho3d/original/1X/5a80771155f05a95b801c6daf9da08b0da1520c7.jpg' height="100px"/></a> <a target="_blank"  href="http://i.imgur.com/QKhwCqY.jpg"><img src='//cdck-file-uploads-global.s3.dualstack.us-west-2.amazonaws.com/standard17/uploads/urho3d/original/1X/511e81f281414db20949c00d8650562294609ab5.jpg' height="100px"/></a>
<a target="_blank"  href="http://i.imgur.com/J0mpv3e.jpg"><img src='//cdck-file-uploads-global.s3.dualstack.us-west-2.amazonaws.com/standard17/uploads/urho3d/original/1X/b1b2e7a4dc5e8fd58f0498564d7e03c7bf8306bb.jpg' height="100px"/></a> <a target="_blank"  href="http://i.imgur.com/XlvXeQn.png"><img src='//cdck-file-uploads-global.s3.dualstack.us-west-2.amazonaws.com/standard17/uploads/urho3d/original/1X/29e01c7969fa8e51cdaf7872e80d5bd2a6fd5361.jpg' height="100px"/></a> <a target="_blank"  href="http://i.imgur.com/gQPncQm.png"><img src='//cdck-file-uploads-global.s3.dualstack.us-west-2.amazonaws.com/standard17/uploads/urho3d/original/1X/289440b4e51415da9c9dc3bacb98db042aad0b71.jpg' height="100px"/></a>

----------

Follow this project on:
[Twitter](https://twitter.com/Enhex) | [YouTube](https://www.youtube.com/user/enhex) | [Tumblr](https://enhex.tumblr.com/) | [Discord](https://discord.gg/VNr5dUQ) | [Reddit](https://www.reddit.com/r/Hellbreaker/)

-------------------------

yushli1 | 2017-09-05 11:58:00 UTC | #51

That looks quite nice. Is there any demo that we can  try out?

-------------------------

Enhex | 2017-09-05 13:04:46 UTC | #52

Urho community members can PM me and I'll give them the game :wink:

-------------------------

yushli1 | 2017-09-05 13:36:00 UTC | #53

Thank you for the link.

-------------------------

ppsychrite | 2017-09-05 21:39:28 UTC | #54

Nice job! Look's amazing. :heart_eyes:

-------------------------

Enhex | 2017-10-30 01:23:12 UTC | #55

Released a beta on itch!
https://enhex.itch.io/hellbreaker

Beta Trailer:
https://www.youtube.com/watch?v=cF_c15AcLxg

I'm hoping to get some feedback and find any issues in the beta before launching on other platforms.

-------------------------

Cpl.Bator | 2017-11-28 22:52:09 UTC | #56

Very impressive ! how many time for this project ? did you plan to adding multplayer ?

-------------------------

Enhex | 2017-11-29 00:51:51 UTC | #57

started in 2014, no plan for multiplayer.

-------------------------

glebedev | 2018-03-09 08:37:38 UTC | #58

[quote="Enhex, post:52, topic:1654, full:true"]
Urho community members can PM me and I’ll give them the game
[/quote]

Too late, already bought it :)

-------------------------

glebedev | 2018-03-10 12:31:55 UTC | #59

It took me about half an hour to pass first level:
https://www.youtube.com/watch?v=Izz04uLZLuc

Ran out of time once. Died several times. Have issues with a jump to the door. Controls are a bit wired - hard to jump, huge inertia. Player gets rotated randomly sometimes.

I do like dynamics of the game and it is fun to play. Do you work on improvements or part 2 at the moment?

-------------------------

Eugene | 2018-03-10 14:16:12 UTC | #60

1:54 same here.
It's hard to make precise jumps because there's no feeling of player feet and chasm edge, so one can't catch good moment for jump.

-------------------------

Enhex | 2018-03-12 09:16:22 UTC | #61

The game is quite hard, and it focuses on fast play-style.
That's why the player is restricted to the first level, which is relatively easy, before playing the other levels - so the player has basic mastery of the game before trying harder levels.

Precise jumps being hard is a perk of the character controller, it doesn't have a lot of error margin for not being directly above ground and it accelerates quickly making jump timing hard. We made some of the platforming sections easier in the last update.

If you want to take your time to find secrets you can turn off "Deadline Mode" in the gameplay settings.

No one ever reported random player rotation, is it something u can reproduce?

In the last update I added Steam Workshop support and several improvements.

-------------------------

