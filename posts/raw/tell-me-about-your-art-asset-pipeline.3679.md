Bananaft | 2017-10-22 20:19:06 UTC | #1

Hi, let's talk about asset pipeline.

1) What middle format do you use for models? DAE? FBX?
2) How your import process is organized? .bat file? custom Blender script? Importing models through the editor one by one?
3) Have you fixed z-up problem or you just rotate all models? :slight_smile: 
4) How quick you can make changes into your models? And how often you do?

5) What format you storing textures in? What format you converting them in for in-game use?
6) Is this an automated process? And how if it is?
7) What version control solution you use for your code and assets?

Right now I have no automation. I used to have .bat file that launches AssetImporter with every model added to it by hand, not cool. Using mostly FBX. Converting textures by hand. I use png when lazy and DDS when I need custom mip-maps or compression. I'm using git, pushing imported assets into it. I never had a lot of assets in my projects, but now I feel I should invest a bit of time into it.

So would like to hear anyone on this forum. What is your method and what do you think of it?

But especially I want to summon @Dave82, @Enhex,  @Modanung, @szamq, @JTippetts

-------------------------

szamq | 2017-10-22 20:36:12 UTC | #2

1. Blender file
2. Import though editor
3. Have no problem with rotation, they are same as in blender
4. Modify editor in blender, export through the plugin into urho internal folders makes auto refresh
5. png
6. No, My game uses about 30 models its not much to do one by one. An hour?
7. Mega sync, and manual backups through freefilesync

-------------------------

szamq | 2017-10-22 20:38:14 UTC | #3

When you finally have all your models in game, all you do is spend time in editor and place prefabs to make levels. I made maybe 5 imports form blender through last year

-------------------------

SirNate0 | 2017-10-22 20:57:26 UTC | #4

My answer is almost identical to szamq's, with the exception that I use Mercurial (hg) for my version control, for both code and assets (I probably shouldn't for assets, or I should at least have a separate repository from my code, but I it do anyways). I also don't use the auto-refreshing of his answer to 4, but I've thought about it before (I'm not sure it would work great for me, though, as some of my assets are node prefabs, and I don't think those end up reloaded, though I'm not certain...).

I will say, unlike szamq, I do not use Urho's editor for much -- I use blender to create even the node prefabs, and I modify them by hand as needed (or in code, depending on what it is). I do use Urho's editor a little bit when messing with materials, and for particle effects, and also for a bit of debugging stuff (making sure I'm not creating extra nodes and failing to remove them when I transition to a battle, and things like that).

-------------------------

Enhex | 2017-10-22 21:48:18 UTC | #5

1/2/3:
Using https://github.com/reattiva/Urho3D-Blender. Models are saved in Blender's file, exported directly to urho's `.mdl`.

4:
Open the original blender file, make changes, export, copy output to the game data directory.

5:
My main concern is loading time. PNG is super slow to decompress so I only use it for small images, and for the rest I use TGA (huge but should be faster to load than PNG). This is a place that can see improvements, there are formats designed for fast loading, and that's the most important thing - file size is 1 time download, load speed is every time you launch the game or load a level.
You could also use urho packages with LZ4 which is fast loading compression, though your users wont have easy access to the files if you want to support modding.

6:
I don't have automation for exporting models since it's a 1 time thing and I have few.
I do have automatic in-memory(not creating files) material generation for level textures since there are many of them and they all use the same simple materials.

7:
For code Git.
For assets I just keep backups.

-------------------------

JTippetts | 2017-10-22 22:17:19 UTC | #6

My process looks a whole lot like everyone else's. The Blender importer makes things pretty easy for me.

I can make changes fairly rapidly. Levels themselves are procedurally generated, so I don't need to manage things on the scene level.

All my textures are PNG, stored directly in my bitbucket git repo.

Nothing in my process is really all that automated, to be honest. My game isn't super asset-heavy, though. I do have a script that can take a batch of diffuse textures and a batch of corresponding displacement textures, and combines the displacement to the alpha channel of the diffuse, and a few other simple command-line tools, but that's about it.

-------------------------

Bananaft | 2017-10-23 15:26:05 UTC | #7

Whoa, thank you all for sharing your insights. Right after writing this post I learned about Blender export plugin. How came I never knew about it?

[quote="szamq, post:2, topic:3679"]
Import though editor
[/quote]
You are importing .blend file through the editor? I found it to working poorly, it breaks all the normals and stuff.

[quote="szamq, post:3, topic:3679, full:true"]
When you finally have all your models in game, all you do is spend time in editor and place prefabs to make levels. I made maybe 5 imports form blender through last year
[/quote]
Yeah, I want to figure out what size of prefabs I need for my project, wall segments? rooms? whole buildings? To save time and nerves.

[quote="SirNate0, post:4, topic:3679"]
I use blender to create even the node prefabs
[/quote]
That's interesting. I want to try it.

[quote="Enhex, post:5, topic:3679"]

copy output to the game data directory.
[/quote]
Why don't you export right into wanted directory? :)

[quote="Enhex, post:5, topic:3679"]
5:

My main concern is loading time. PNG is super slow to decompress so I only use it for small images, and for the rest I use TGA (huge but should be faster to load than PNG).
[/quote]
Aren't DDS is an ultimate solution? I messed with ImageMagick (console app, not library) a bit, and now I'm thinking about making a script that will check textures sources folder for updated files, converts them and puts into game data folder.

[quote="JTippetts, post:6, topic:3679"]
I do have a script that can take a batch of diffuse textures and a batch of corresponding displacement textures, and combines the displacement to the alpha channel of the diffuse
[/quote]

Woo AUTOMATION! :) Does it use ImageMagick? What language you use for this sort of thing?

-------------------------

Enhex | 2017-10-23 23:57:19 UTC | #8

no direct export:
I manage my assets externally, so the blender files don't have hardcoded path to a specific game.
Also some assets' license require protection so I need to pack them from a different directory.

DDS:
AFAIK DDS files are lossy, while PNG & TGA are lossless.
DDS should be much faster, but I was worried about quality loss and didn't give it a shot yet.
Also DDS isn't completely "clean", it uses patented compression algorithm and require OpenGL extension (tho that isn't a real problem).

-------------------------

JTippetts | 2017-10-24 02:32:47 UTC | #9

[quote="Bananaft, post:7, topic:3679"]
Woo AUTOMATION! :slight_smile: Does it use ImageMagick? What language you use for this sort of thing?
[/quote]

Not ImageMagick, though I do use that sometimes, mostly for when I help my wife with her work. Usually, I use my own custom tool, it's a Lua interpreter that embeds my noise library and some other useful stuff. Most of my automated tools and texture generators are Lua.

-------------------------

Modanung | 2017-10-24 09:07:22 UTC | #10

[quote="Bananaft, post:7, topic:3679"]
Right after writing this post I learned about Blender export plugin. How came I never knew about it?
[/quote]

In the documentation it is only briefly mentioned under [Tools](https://urho3d.github.io/documentation/HEAD/_tools.html), but on the forums I'd say it's been the default recommendation for over a year. I guess you missed those topics.

Oh, and yeah, I use it too. ;)

-------------------------

Eugene | 2017-10-24 09:54:51 UTC | #11

[quote="Enhex, post:8, topic:3679"]
AFAIK DDS files are lossy, while PNG & TGA are lossless.

DDS should be much faster, but I was worried about quality loss and didn’t give it a shot yet.

Also DDS isn’t completely “clean”, it uses patented compression algorithm and require OpenGL extension (tho that isn’t a real problem).
[/quote]

I must say that DDS is _conatiner_, not a format.
Compression and 'lossiness" is the feature of DXT image format.

-------------------------

Dave82 | 2017-10-24 14:12:22 UTC | #12

Hey , Sorry for the late reply !

1 . Mostly i use my own models (made in 3ds max)  so i export them directly to Urho. In some cases if i have to import an external model i prefer the .obj and .x for importing.Since these formats tend to be backward compatible so i don't need to update the importer plugin for this.

2. As i mentioned i use 3ds max most of the time.There are lots of other tools i use but everything is done mostly in 3ds max,I wrote a complete scene exporter for max back when i used irrlicht. So when i swithed to Urho3d i had 2 choices : either write another scene , mesh , etc exporter for max or write a Urho3d importer.I decided to go with the 2nd option.Since it is lot easier to write code in c++ than fiddle with a notepad-like editor and maxscript.

3. I convert coordinates at export level.

4. Since i use completely my own formats i could say the changes can be exported in seconds.I make any modification to a model and press ONE button on my exporter and everything (textures , models ,material etc) are placed in the game's directories ready to use.
The only difference is in skinned models.I prefer to export them in x format then use AssetImporter to convert them to mdl.Well this is a bit slower but still way faster than write a complete mdl exporter for max.

 5. I store almost all my textures in psd and use png , dds , bmp formats in game.

6.Well unfortunately not.This is the only part where i must do everything manually.Some of my textures are built from 7-8 layers.I edit layers , contrast , hue ,etc then i save it in png.If the final texture looks satisfing i save it in  psd.Sometimes i go with different versions of the same texture so i end up with different psd files for the same texture (brick01_dark , brick01_dirt01 , brick01_dirt01b etc) 

7 currently i don't use any version control system , i use some dirty manual backup to different usb flash drives(simply overwirite the older files) which seems fast enough so right now i'm happy with it.

-------------------------

boberfly | 2017-10-24 19:37:36 UTC | #13

Currently building an asset pipe in my spare time, so these are more current vs ideals right now:

1. I use Maya so .ma and .fbx, but thinking of a different approach here, maybe alembic/cortex/usd/gltf and procedural tweaks in a Gaffer graph. I want independence from any proprietary DCC app if I can!

2. Working on the Gaffer windows port so it's all just nodes and python in a nice pipeline UI which can be run to export on-demand.

3. Y-up is the one true up, get rid of that 3dsmax while you still can

4. I want to change them constantly and want automation and QC checks, so considering Pyblish for Maya followed by Gaffer for procedural modification and then export to game at build time.

5. Textures ideally in .exr or .tif linear-space with ACEScg primaries (maybe krita for WIPs), and OpenImageIO/GafferImage to convert into a custom format I'm working on (maybe google's AV1 i-frames for compression), with ISPC to convert to a GPU-compressed format either online or offline as well, depending on platform.

6. Working towards this yes for a full game (gaffer execute -script build.gfr)

7. Considering either git-lfs or subversion, but there isn't really a good solution out there here for assets, do you store actual versions side-by-side for WIPs in version control or just override the one file and keep versions in history? Thinking a WIP repo and a runtime repo could be done here maybe...

But yeah lots of these are ideals, would like to make it work one day... :)

-------------------------

jmiller | 2017-10-24 20:41:04 UTC | #14

My 3D workflow is usually as simple as export with Urho3D-Blender.

[url=https://docs.blender.org/manual/en/dev/data_system/introduction.html]Blender file data (assets) can be unpacked in relative or absolute filepaths.[/url]
Urho3D-Blender is nicely flexible in where it can put exports.
I use symlinks for flexible asset location.

Sometimes I have made slight modifications to produce the exact XML I want.
Whatever needs processed on whatever workstation, it's generally child's play with Python. :snake:

-------------------------

organicpencil | 2017-10-24 21:51:01 UTC | #15

My blend files update frequently & generally contain lots of unused meshes, so the Blender exporter works good for my situation: https://github.com/reattiva/Urho3D-Blender

Exceptions:
1. Will occasionally import complex multi-part objects using the Urho3D editor.
2. Certain animated characters don't play nice and I have to do Blender -> DAE -> assetimporter. Exporting multiple animations this way is a huge headache. Thankfully I don't have many characters.

-------------------------

