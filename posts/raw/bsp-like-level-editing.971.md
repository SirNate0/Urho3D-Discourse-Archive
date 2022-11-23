darkhog | 2017-01-02 01:04:31 UTC | #1

Could this be added? It would greatly speed up making levels as you won't have to fiddle with external 3D software to make level mesh and UV map it manually. Possibly from editing standpoint, something like Trenchbroom editor for Quake (very intuitive, unlike various Radiant clones).

-------------------------

GoogleBot42 | 2017-01-02 01:04:31 UTC | #2

Sounds like it would be a lot of work to recreate one of these from scratch... maybe an existing one can be modified to export to xml?

-------------------------

JamesK89 | 2017-01-02 01:04:32 UTC | #3

If you're looking for something like Hammer Editor for building your worlds I would suggest taking a look at the open source tools; [url=http://sledge-editor.com/]Sledge Editor[/url], [url=http://www.delgine.com/]DeleD[/url] or [url=http://runtimelegend.com/rep/rtworld/index]Runtime World[/url].

However it is worth mentioning that I found [url=http://www.blender.org/]Blender[/url] much easier to use than ever before so you might consider forcing yourself to learn to use Blender by building some basic models. Within a few days I figured out enough to make a basic level and I felt much more capable than being stuck with a CSG based editor.


Of course if you use these tools it will be up to your to figure out how to integrate it into an Urho3D project but if you come up with anything please do share or explain how you got an art pipeline up and working!

-------------------------

Nerrik | 2017-01-02 01:04:32 UTC | #4

If you have 3DS Max, you can use the Hammer Editor by importing the maps with the "Wallworm" plugin. (Its a little bit work to set up a development environment but it works fine)
export it to 3ds or ase and import it as scene with assetimporter "-nf"

Some Screens: 

Imported cs:go HG_sunset map (with some deleted models and other ground texture)

[url=http://postimg.org/image/oz3c0nxqf/][img]http://s23.postimg.org/oz3c0nxqf/hammer1.jpg[/img][/url]

[url=http://postimg.org/image/cjpop4eud/][img]http://s18.postimg.org/cjpop4eud/hammer3.jpg[/img][/url]

Imported de_cblle map (untextured, uncleaned and without models only a test)

[url=http://postimg.org/image/srv4b4vu5/][img]http://s14.postimg.org/srv4b4vu5/hammer2.jpg[/img][/url]


*i only imported this maps for learning purposes :slight_smile:

-------------------------

JamesK89 | 2017-01-02 01:04:33 UTC | #5

[quote="Nerrik"]If you have 3DS Max, you can use the Hammer Editor ...[/quote]

A word of warning: Valve's end user license agreement for Hammer Editor prevents you from using it for anything but Goldsrc and Source engine games which is why I recommended Sledge Editor as an alternative since it is an open source clone of Hammer Editor.

-------------------------

darkhog | 2017-01-02 01:04:34 UTC | #6

Except Hammer is so close to radiant (basically editing 3D world in 2D, WTF?), it's not even funny.

Something like Trenchbroom: [youtube.com/watch?v=F-1pM55k4WM](https://www.youtube.com/watch?v=F-1pM55k4WM) would be more appropriate. Also no, I don't have 3ds max, because I don't feel like wasting $5000

-------------------------

GoogleBot42 | 2017-01-02 01:04:35 UTC | #7

[quote="Sinoid"]So why don't you fork Trenchbroom and add export straight to Urho?[/quote]

Just what I was thinking.  I have no need for this at all so I won't make a port.

[quote="Sinoid"]Autodesk throws discounts around like candy.[/quote]

Lol.   :laughing:   If you are a student you can even get it for free (but not for commercial applications of course).

-------------------------

Enhex | 2017-01-02 01:04:37 UTC | #8

I also wanted a BSP-like level editor and I made a generic one (that can be used with any game for any game engine).
It's still early in development but the basic features already exist.

Here's the last, outdated, video I uploaded of it:
[video]http://www.youtube.com/watch?v=zbjwM6aztzc[/video]

Back then I didn't use Urho yet, tho when I switched to urho it took few hours to make level loading code.

Right now it export levels as JSON (so you can pick up a lib and parse it with any language).

[quote="darkhog"]Except Hammer is so close to radiant (basically editing 3D world in 2D, WTF?), it's not even funny.[/quote]
Your screen is 2D.
Having 2D grids give you more precision and speed. You don't have to move a camera around to access stuff.

-------------------------

friesencr | 2017-01-02 01:05:07 UTC | #9

I am going to be trying to do a glsl shader soon that does texture atlas w/ wrapping.  Hopefully it goes well.  I wrote the sprite packer, its urhos sprite packer so we can make it do whatever crap we want.  If you need any features in it let me know.

-------------------------

GoogleBot42 | 2017-01-02 01:05:07 UTC | #10

[quote="friesencr"]I am going to be trying to do a glsl shader soon that does texture atlas w/ wrapping.  Hopefully it goes well.  I wrote the sprite packer, its urhos sprite packer so we can make it do whatever crap we want.  If you need any features in it let me know.[/quote]

+1 That would be awesome!  I hope you can get it to work.  :smiley:   I don't have any experience with shaders so I don't know how to do it.  :blush: 

@Siniod It is looking great so far!  I can't wait to see you next milestone. :wink:

-------------------------

gabdab | 2017-01-02 01:07:19 UTC | #11

..I might have missed reading some posts , but 
How do you handle the occlusion culling proper of .bsp maps ?
Doesn't assimp come with a .bsp converter ?

-------------------------

boberfly | 2017-01-02 01:07:19 UTC | #12

I don't think you'd use the BSP occlusion data. Urho will just do frustum cull & octree lookup and the software occlusion query if that's enabled. So yeah best to split the model up based on material first, and have some thing which splits them every n units in space, but yeah it depends on the vertex density of these bits, if it's all super simple geo (under 1024 verts or so) it's best to just have it all in one mesh, although splitting it might have the benefit of a smaller, more beneficial software occluder...

If you really want the BSP occlusion data you'd need to implement your own... :slight_smile:

-------------------------

gabdab | 2017-01-02 01:07:20 UTC | #13

I need to get accustomed to Urho3D software occluder .
I didn't get how it handles  occluded occluder in the same mesh ..

-------------------------

cadaver | 2017-01-02 01:07:22 UTC | #14

Yeah, so instead for example a building being one big mesh you could have each wall + the roof (or any other repeating part) being a separate mesh, this already allows the frustum culling to work better even before getting into occlusion. Then enable occluder in those objects that you figure that would be good occluders (simple and large.)

Note that the software occlusion system was developed on desktop machines, I won't make promises on how well it runs on mobile hardware.

-------------------------

gabdab | 2017-01-02 01:07:29 UTC | #15

Where is the software occluder located in code ?
Id bsp is precalculated based on walkable spaces .. you can mimic it while designing your levels sort of by defining closed areas and setting up a bounding box .
When player collides with a bounding box all the pertaining nodes are activated .

-------------------------

cadaver | 2017-01-02 01:07:29 UTC | #16

Graphics/OcclusionBuffer.cpp, which is used by Graphics/View.cpp

-------------------------

