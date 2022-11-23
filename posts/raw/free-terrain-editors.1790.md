rasteron | 2017-01-02 01:10:10 UTC | #1

Here are some FREE Terrain/Heightmap editors that I have gathered and tested, language denotes opensource licensing.

[url=http://www.lilchips.com/hmesalpha.htm]TerreSculptor HMES[/url] (Alpha, Windows)
[url=http://lithosphere.codeflow.org/]Lithosphere[/url] (Python)
[url=https://bitbucket.org/gdecarpentier/scape]Scape Editor[/url] ([url=http://www.decarpentier.nl/downloads/scape0.1.1-bin-win32.zip]Binaries[/url], C++)
[url=http://www.bundysoft.com/L3DT/downloads/standard.php]L3DT Standard Edition[/url] (Free, Windows)
[url=https://github.com/GarageGames/Torque3D]Torque3D Terrain Editor[/url] (Windows/Linux, C++)

Updated/Suggestions:
[url=http://irrrpgbuilder.sourceforge.net]IrrRPGBuilder[/url] (MIT/X11)
[url=http://www.artifexterra.com/]Artifex Terra 3D[/url] (Free, Windows)

cheers :slight_smile:

-------------------------

christianclavet | 2017-01-02 01:10:57 UTC | #2

Hi,

There is also this one that I made with a friend (Andres Jesse Porfirio) with Irrlicht (Windows/Linux C++). It can save tiles in OBJ or Collada
[url]http://irrrpgbuilder.sourceforge.net/[/url] License is MIT/X11

[img]http://irrrpgbuilder.sourceforge.net/images/features/terrain.jpg[/img]

-------------------------

Shylon | 2017-01-02 01:10:58 UTC | #3

Thanks for links, very useful editors. :slight_smile:

-------------------------

jmiller | 2019-05-18 15:09:38 UTC | #4

Blender and Urho seem to handle Terrain at 2048+ for me.

Ant Landscape for Blender.
  https://wiki.blender.org/index.php/Extensions:2.6/Py/Scripts/Add_Mesh/ANT_Landscape

A method to create and manipulate height maps by linking to a plane and rendering as greyscale:
  http://blender.stackexchange.com/questions/9030/create-and-manipulate-height-map-save-as-greyscale-texture

-------------------------

Bananaft | 2017-01-02 01:11:05 UTC | #5

Also, there are real world elevation data with with 30m resolution, avaliable for everyone. I was downloading it from here: [gdex.cr.usgs.gov/gdex/](http://gdex.cr.usgs.gov/gdex/) . It requires registration, and there may be other sites, where it can be downloaded.
[en.wikipedia.org/wiki/Shuttle_R ... hy_Mission](https://en.wikipedia.org/wiki/Shuttle_Radar_Topography_Mission)

-------------------------

rasteron | 2017-01-02 01:11:07 UTC | #6

This is great guys and this thread is also meant for you to share your own findings and feedback. 

@christianclavet

Yes, that is also one cool editor that you guys made with Irrlicht. Thanks for sharing!

cheers :slight_smile:

-------------------------

Nauk | 2017-01-02 01:14:53 UTC | #7

Hello everyone,

you can always have a look at "Artifex Terra 3D", also free (as in beer) and I am always very happy about feedback and critics. :slight_smile:
I am currently in the process of reworking it and making it more agnostic and open, as in integrating assimp and plugins - specially export / import geared towards various engine formats.

*edit* I am also happily assisting with material conversion.

Cheers,
//Nauk

-------------------------

rasteron | 2019-01-17 20:49:26 UTC | #8

Hey Nauk,

Welcome to the forums! :slight_smile: Yes, I got to try Artifex Terra when I was doing Ogre3D some time ago, and it really is a great terrain editor!

Here's my built and a little test video 2 years ago  :mrgreen: 

https://www.youtube.com/watch?v=rogy1JYYD-E

[quote]
I am currently in the process of reworking it and making it more agnostic and open, as in integrating assimp and plugins - specially export / import geared towards various engine formats.
[/quote]

I just thought it was more focused on Ogre3D so I did not include it on this list but it's good to hear if you do have plans of making it agnostic/open and Urho friendly. :wink:

Added now!

-------------------------

Nauk | 2017-01-02 01:14:56 UTC | #9

Nice Video :slight_smile: Thanks for adding me!

//Nauk

-------------------------

slapin | 2017-01-02 01:15:33 UTC | #10

Hi, all!

Please tell me which of terrain editors can be used with Urho3D terrain node? Or is there any reason in using it?
Sorry for probably stupid question - I never used terrain before, but tried it in Urho and don't quite understand the workflow.
I tried using Terrain in Unity and see it as powerful tool, but is there something for Urho?

-------------------------

artgolf1000 | 2017-01-02 01:15:33 UTC | #11

World Machine is the most powerful terrain tool, but it is a paid software, I have used it for several years.

-------------------------

HeadClot | 2017-01-04 01:59:11 UTC | #12

Just thought I would chime in on this thread. 

TerraSculptor is really awesome and really overlooked. :slight_smile: 

http://www.demenzunmedia.com/home/

-------------------------

lhlvieira | 2018-10-14 18:04:09 UTC | #13

Wilbur. Its more of a height map editor than a terrain editor.
http://www.fracterra.com/wilbur.html

-------------------------

JTippetts1 | 2018-10-17 06:19:20 UTC | #14

I took a look at that Wilbur tool. It has a few nifty little tricks. One in particular that is mentioned in the tutorials, basin filling, led me to a paper about implementing a basin filling algorithim. I decided to implement a similar technique in my own terrain editor based on that paper. For such a simple trick, it sure is handy for making terrains flow and drain more realistically.

-------------------------

smellymumbler | 2018-10-17 16:53:24 UTC | #15

One feature that isn't very appreciated in terrain editors is the ability to stamp heightmaps. Having a good collection of height stamps gives freedom to level designers to create playable designs, without sacrificing "good" looking landscapes.

-------------------------

smellymumbler | 2018-10-17 16:55:46 UTC | #16

Also cool: this guys allows you to shade your terrains procedurally, but also exports a bitmap. So you can generate a heightmap, put through this, export a height, and then use in any other engine.

https://assetstore.unity.com/packages/tools/terrain/cts-complete-terrain-shader-91938

-------------------------

