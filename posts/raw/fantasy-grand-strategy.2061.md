Victor | 2017-01-02 01:12:43 UTC | #1

So, before I continue posting more unrelated posts in my Curved Text thread I thought I'd just go ahead and start a new thread here. For a year now I've been working on a strategy game which has always been a dream of mine. I've always loved the Europa Universalis game, and the Crusader Kings 2 games for their immersion, so I thought it'd only make sense to make the game I wanted to play with the ability to load in my favorite CK2 mods as well.

Currently I can load any map from CK2 as well as load in their scripts. When this game is finally released it will have [b]NO[/b] Crusader Kings 2 or any Paradox assets in the final build. I'm only using those for testing purposes to ensure the possibility of playing existing mods out there.

VERY VERY Early preview of the map loading and city placement.
[b]Larger Image[/b] [url]http://i.imgur.com/rZPhWTY.png[/url]

[img]http://i.imgur.com/8DyZ3LF.png[/img]

[b]Larger Image[/b] [url]http://i.imgur.com/jVBF0lt.png[/url]
[img]http://i.imgur.com/111rQX8.png[/img]

-------------------------

Lumak | 2017-01-02 01:12:45 UTC | #2

It's looking great! I'll follow this project:)

-------------------------

Bananaft | 2017-01-02 01:12:45 UTC | #3

Really like your borders. I want to try something similar for roads on terrain.

What's up with mip mapping? Have you turned it off on purpose?

-------------------------

Victor | 2017-01-02 01:12:45 UTC | #4

[quote="Bananaft"]Really like your borders. I want to try something similar for roads on terrain.

What's up with mip mapping? Have you turned it off on purpose?[/quote]

Yeah, for textures it's turned off since I'm using an atlas for the terrain and saw a lot of bleeding when mips were turned on. The atlas looks like this which gets generated on load (if it does not exist already). These textures are from GameTextures.com btw.

(At some point I plan to revisit the textures I'm using, although that will be after I have a playable demo)
[img]http://i.imgur.com/o558E8U.png[/img]

-------------------------

Victor | 2017-05-02 19:10:41 UTC | #5

New video with the text on the terrain and the scripting engine loading all of the scripts from a CK2 Witcher mod.

https://www.youtube.com/watch?v=iS83DBRPXkA

-------------------------

Victor | 2017-05-02 14:07:11 UTC | #6

Been a while since I've updated this post. Still working on this game as a strategy game, but more like Mount and Blade (if possible). Last night I finished up my initial stab at a foliage system. Uses multi-threading to save/load data from disk. Still working on some optimizations with the loading, but it renders pretty well.

(Note, cracks in the terrain are do to my improper loading of multiple terrains in the scene, should be fixed this weekend once I finish up the vegetation system). ProcSky is also used in the scene. :)

https://www.youtube.com/watch?v=ordWhxmq2-k

-------------------------

Victor | 2017-05-02 14:25:56 UTC | #7

Oh, just in case anyone is interested... (sorry it's without much context but I thought I'd share), here's the FoliageComponent. You should be able to get an idea of the implementation. This was written around 2AM/3AM and is just a rough draft heh.

https://gist.github.com/victorholt/20eaf694071583fedf67a39c9f5c3015

https://gist.github.com/victorholt/cd0977a8243adf712cd2eb184d2bfd7f

-------------------------

Victor | 2017-05-03 06:42:09 UTC | #8

Still working on optimization. Instead of building a ton of nodes, the foliage is built using a single mesh. Right now I'm attempting to add rotation and scale as well when building the mesh object. With over 2mil triangles rendering, the FPS is still really good. The only downside is loading all the data from disk (initially).

<img src='//cdck-file-uploads-global.s3.dualstack.us-west-2.amazonaws.com/standard17/uploads/urho3d/original/1X/f40ed8554b9fd123eb222e5e7ca6b68d816c7422.png'>

-------------------------

Bluemoon | 2017-05-03 12:08:00 UTC | #9

Awesome. I would be needing such component

-------------------------

HeadClot | 2017-06-27 11:52:57 UTC | #10

Hey @Victor - Got a question is the terrains system that you are using built in Urho? Or is it custom?

-------------------------

Victor | 2017-06-27 12:06:05 UTC | #11

Hey @HeadClot, it's all Urho :)

-------------------------

HeadClot | 2017-06-27 12:07:26 UTC | #12

Thanks for the prompt reply. :slight_smile:

I am trying to build my own 4x strategy game using atomic game engine.

Looking forward to seeing what you make :slight_smile:

-------------------------

Victor | 2017-06-27 12:33:20 UTC | #13

Nice! Good luck on your game! It's definitely my favorite genre of games. :)

-------------------------

