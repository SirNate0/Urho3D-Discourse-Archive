PeterZbinden | 2019-07-15 19:01:07 UTC | #1

I am new to Urho3D, so far I'm very excited about this engine.
While most things seem to work fine, I ran into an issue when trying to create terrains.

I am trying to import Height-Maps (created in WorldMachine) into Urho3D using the Editor:
The Heightmap imports but even though the PNG is 16bit, it still seems to read it as a 8bit heightmap, as there are visible 'stairs' that should not be there:
![Urho_Solid|690x215](upload://oDyySDj6VC2HMBDwVdf6hapsyS5.jpeg) 
https://imgur.com/T5d9XpD
https://imgur.com/hSTPPVT

When I import the same heightmap into Unity for example, the terrain is MUCH smoother:
https://imgur.com/F438Q5k
https://imgur.com/F9sbe3g

Comparing the wireframes, it doesn't seem like the problem is because of differences in Polycount but rather how the Height-Information is read.

This is how the Image is setup when i open it up in Photoshop:
https://imgur.com/rjRVgRv

What am I doing wrong? Do I have to perform manual steps before importing it in Urho?

Hope you guys can help me!

(Sorry for the external links, the forum doesn't seem to allow me to upload more than 1 image per post)

-------------------------

PeterZbinden | 2019-07-15 19:04:51 UTC | #2

This is the original Heightmap produced by Worldmachine, if it helps:

![HeightMap_x0_y1|500x500](upload://7EGRfkMRosmpa9DwN2yGeDYSaEn.jpeg)

The Forum-Upload seems to convert the file, so I uploaded it somewhere else:
https://gofile.io/?c=RjL0tl

-------------------------

lezak | 2019-07-15 21:36:48 UTC | #3

I don't think that Urho supports 16 bit grayscale height maps, from documentation:
<a href="https://urho3d.github.io/documentation/HEAD/class_urho3_d_1_1_terrain.html#ad2a5a0e30901033ba358b2cf6d35d264">bool SetHeightMap(Image* image) 
Set heightmap image. Dimensions should be a power of two + 1. Uses 8-bit grayscale, or optionally red as MSB and green as LSB for 16-bit accuracy. Return true if successful.</a>

-------------------------

PeterZbinden | 2019-07-15 22:47:26 UTC | #4

Hi lezak,

How would I go about transforming my grayscale height map into the format specified in the documentation (red as MSB and Green as LSB)?
A quick google provides me with MSB = 'Most signifcant Bit' and LSB = 'Least significant Bit' --> how should I interpret this?
Instead of having a Gradient from Black to white, should I convert this to a 'Gradient' from Green to Red?

Thanks for your help!

-------------------------

Modanung | 2019-07-16 00:47:17 UTC | #5

I think this post may hold the answer you are looking for:
https://discourse.urho3d.io/t/loading-16bit-pngs-for-heightmaps/2463/2

Also, welcome to the forums! :confetti_ball: :slightly_smiling_face:

-------------------------

PeterZbinden | 2019-07-16 04:36:18 UTC | #6

Hi Modanung, 
thanks for your reply, am I correct in assuming that there currently is no other way that is supported out of the box by the provided tooling of the engine to do this?

Don't get me wrong, it is perfectly feasible, just wondering why such a crucial piece of the content-pipeline is not part of the engine as most other engines seem to provide a way to integrate with industry-standard tooling (like Worldmachine), for example trough the (dead-easy) PGM-Format or the RAW-Format.

-------------------------

Modanung | 2019-07-16 10:00:46 UTC | #7

So far I have practically no experience or interest in using terrain. [spoiler]Also, to be honest, the idea of some *industry-standard* is starting to make me nauseous. It is a notion that is destroying Blender, if you'd ask me. To me the words industry-standard mean "fancy" looks and monthly subscriptions of proprietary software aiming for a dimensionless learning curve coupled with conservative creativity.[/spoiler]

@JTippetts is more familiar with terrain, maybe he can answer your question.

[![Screenshot](https://cdck-file-uploads-global.s3.dualstack.us-west-2.amazonaws.com/standard17/uploads/urho3d/original/1X/da21c33cf49ca1d48b5abcd87183b1f26f7392e9.jpg)](https://discourse.urho3d.io/t/u3d-terrain-editor/765)

-------------------------

PeterZbinden | 2019-07-16 11:58:02 UTC | #8

@Modanung ok, maybe a loaded term... Given that Game-Development today is such a complex thing to do, it seems obvious that you won't find a product that provides ALL functionality required by itself in the best way possible without ever interacting with other Applications. Considering the 'UNIX-Approach' of 'Do one thing and do it right' it makes sense that there would be applications that do just that one thing very well. Urho does lots of things well but in the end it is a Game-Engine, not a 3D Modeler, not a Sculptor, Texturing-Application, Music Composer, Motion-Capturing environment, etc.. There are tools out there that do all of this way better because they specialize in them. That doesent mean that you have to let other people ('the industry') dictate how your engine should work, but it would be unwise to not provide way to get at least some of this content in into the Engine trough a reliable interface that does not degrade quality etc.. In fact, Urho already supports lots of these 'Indutry-Standards', either trough the AssetImporter (.obj, .FBX, ...) or directly as a resource (.png,.dds,...) so it's not like this concept would be new. 

Not trying to lecure you, just trying to point out that the reality seems to be that people are going to use whatever tools fits their needs best. Giving them the freedom to interact with whatever they choose without having to compromise on quality etc. will only empower the Users to achieve their goals and in the end make Urho3d more popular.

Having a nice Terrain-System and then not providing a way to import 16bit Heightmaps imho seems like a unnecessary obstacle that if anything only hinders the engines potential.

-------------------------

Modanung | 2019-07-16 12:00:28 UTC | #9

The main reason I use Urho3D is because I limit myself to open source software.

-------------------------

Leith | 2019-07-16 11:56:26 UTC | #10

Urho is not feature-complete, maybe it should never be. We need to work around the asset pipeline in some cases, this is typical of any game engine, including AAA ones.
This does not mean we can't or should not try to do better, but it is a fact we have to learn to accept. Even in AAA engines.

-------------------------

Leith | 2019-07-16 12:05:35 UTC | #11

Does open source software include your own? Our license is liberal, I just like to share sometimes.

-------------------------

Modanung | 2019-07-16 12:10:03 UTC | #12

The core principle of *LucKey Productions* is to be religiously open source. That's why I called it a cult. :wink:
Code is under GPL, assets CC-BY-SA.

-------------------------

lezak | 2019-07-16 14:00:54 UTC | #13

First of all I would like to notice that, there is to many threads going off-topic recently....

@PeterZbinden
I've taken closer look at Your problem and it looks that the actual problem lies in Your height map. The link You provided doesn't work, so I've used some other 16-bit png file (cloud texture generated in substance designer) and it worked just fine. 

[quote="PeterZbinden, post:1, topic:5297"]
When I import the same heightmap into Unity for example, the terrain is MUCH smoother:
[/quote]
Correct me if I'm wrong, but doesn't Unity use raw files for height maps? So You're using different file.
I've never used World Machine, but my guess would be that quality is lost on png file generation/export.

[quote="PeterZbinden, post:8, topic:5297"]
Having a nice Terrain-System and then not providing a way to import 16bit Heightmaps imho seems like a unnecessary obstacle that if anything only hinders the engines potential.
[/quote]

Actually when it comes to terrain or even wider: outside enviroment, Urho is very limited. I don't mean to sound rude, but Urho is an open source engine and if You want some feature that is not there (like World Machine support) feel free to implement it.

-------------------------

PeterZbinden | 2019-07-16 14:17:53 UTC | #14

@lezak while Worldmachine supports RAW-Files natively, I actualy Exported 16bit PNG (The file I tried importing into URHO3D) and then manualy converted that data into a RAW-File using Photoshop before Importing it into Unity, so no I'm prety confident that the data is actualy not the problem.

Would you care to share your file and maybe a screenshot of how it looks in Urho on your machine so I could compare the results and see if there is actualy something wrong with the way a deal with these files?

On the topic of implementing this myself:
I'm not demanding/suggesting that someone would have to do this for me, it just seems strange to me that someone would go trough all of the trouble of creating a Terrain-System without having a way to import high quality Heightmaps.

-------------------------

JTippetts | 2019-07-16 15:26:51 UTC | #15

Urho3D terrain has a property, Smoothing, that is for some reason set to false by default. If you enable it with [Terrain::SetSmoothing(true)](https://github.com/urho3d/Urho3D/blob/master/Source/Urho3D/Graphics/Terrain.h#L64) then the result from an 8-bit PNG will be MUCH better. 16 bit (whether traditional 16-bit or the 16-bit split between R/G as Urho3D uses) really only comes in handy at much higher terrain resolutions than your original post exhibits, when the mesh is sufficient to show the smaller details. Still, I prefer 16-bit even with small terrains, as it simplifies the tooling. I don't use WorldMachine, and in fact I use my own custom (and unfinished :smiley: ) terrain editor, but I do agree it would be nice if a traditional 16-bit PNG path was supported. Unfortunately, it is unlikely to be done until someone with a vested interest in it being done takes the initiative and does a pull request for it.

In regards to your question about how the R/G channels are used, the red channel ends up being essentially identical to a standard 8-bit PNG heightmap, while the green channel holds additional detail. Say you have a terrain that ranges from 0 to 255 units high. The whole part of a height value would be encoded in the R channel, while the fractional part is encoded in the green. Red will range in a gradient from the lows to the highs, while green ranges in a gradient in between the individual units of the red channel. A typical heightmap ends up looking something like this:

https://i.imgur.com/sypKjsL.png

On the left is the composite R/G heightmap. Upper right is the red channel alone, and what it would be with just an 8-bit heightmap, on the lower right is the green channel. You can see that the large-scale features of the terrain are exhibited in the red channel, while the green holds only very small details.

If you don't want to modify the image at run-time, it should be easy enough to write a converter offline tool to batch-process heightmaps from what WorldMachine outputs to what Urho3D R/G mode expects. It's not optimal, I know, but for now that's all I can really suggest.

-------------------------

lezak | 2019-07-16 16:07:00 UTC | #16

Unfortunetly I doubt that smoothing will help with this stepping/banding problem - it's caused by 16 to 8 bit convertion (like I said file that I used was not a proper height map so the result may be misleading, sorry for that).
Now the obvious - does World Machine support 8bit png export? This should fix Your problem.

-------------------------

PeterZbinden | 2019-07-16 19:52:08 UTC | #18

@JTippetts Thanks for the extensive explanation, I'll have a look into what my options are.
Concerning using 8bit for my project:
The hightmap I provided is only part of a bigger terrain, still the effect is most visible when there are subtle changes in the height. As far as I understand it, a Chanel on a 8 Bit Pixel can only have a value of between 0 and 255. If the terrain I'm trying to create has a total height of say 1000m, then any vertice can only be placed every 3.92m. In this case if I have two vertices that in the source-data differ less than these 3.92m, they will have the same height in the 8Bit Heightmap.

Compared to this a chanel on a 16bit pixel can have values between 0 and 65'535 --> enabling vertices to be placed every 0.015m in the same 1000m hight terrain.
To get the same precision out of a 8bit Heightmap, I would have to limit my Terrain to be ~4m of height max.

I guess you could live with scaling it a bit more, especialy if the source was something generated from noise-filter, as it does not realy have any meaningful identifiable shape to begin with. But when you deal with Erosion-based simulation to create beautiful environments, these issues will automaticaly become more prominent.

To compare, this is what the environment looks like in Worldmachine:
![Worldmachine|690x355](upload://fIgIirXB1VbIHJqD3hFd76eVyUn.jpeg)

-------------------------

Modanung | 2019-07-16 21:21:28 UTC | #19

A single 16-bit channel can pack the same amount of information as two 8-bit channels, hence the red and green. Nice mountain range, btw.

-------------------------

JTippetts | 2019-07-16 20:48:30 UTC | #20

Any 8-bit grayscale image will cause stair-stepping, which is why the smoothing option is there in Urho3D::Terrain.

That image from world machine looks like it uses a terrain-sized normal map, which is a possible technique you can use to make your terrains look like they are of a much higher resolution, while still reducing the actual resolution of the mesh to improve rendering performance. Here is a quick Blender shot demonstrating that idea:

https://i.imgur.com/U90OYIA.png

On the left is the original 8-bit greyscale heightmap terrain. On the right is the same terrain with a normal map applied to make it look more detailed. Same number of triangles in each render, but the one with the normal map looks better.

This is a typical type of workflow for game terrains. WorldMachine can export that whole-terrain normal map for use in your shader. Note that this workflow would require a small edit to the default Urho3D terrain shader to use. Even with support for 16-bit grayscale heightmaps, this normal-mapping technique would still likely be a part of your workflow, because the 16-bit option can improve the precision of vertical placement of your heightmap vertices, but it won't necessarily make the overall terrain look more detailed without simply increasing the subdivision level of your terrain and thus impacting performance.

-------------------------

PeterZbinden | 2019-07-17 15:40:22 UTC | #21

@Modanung I'm not saying that you can't press the data in there by splitting it up, I was talking about why using a classical 8bit Heightmap (1 channel) would be problematic in most cases.

@JTippetts I agree, you can push 8bit Heightmaps 'a bit' further with the smoothing-option, still there are limits to what it can do.
8bit grayscale, no smoothing:
![NoSmoothing|690x330](upload://e1QDJsCckVlInMOSJ8h6vXU0Ole.jpeg) 
8bit grayscale with smoothing:
![WithSmoothing|690x297](upload://rxxP42sT3vpcirXlq6pBRRDFUV8.jpeg) 

Im considering using a Normalmap for more detail once I'm able to properly import the 16bit heightmap, currently all the detail resides in the Heightmap.

At the moment my focus is to establish a minimum Pipeline of how I can reliably bring high quality Terrains into Urho, making it look as pretty as possible is a topic for another time...

I'll report back as soon as I have implemented a converter from 16bit gs --> 8bit r/g.

-------------------------

PeterZbinden | 2019-07-17 15:56:45 UTC | #22

Sorry for double-posting but I just got the 16bit-converter to work, here is the comparison to the above image with the 16bit heightmap (no smoothing):
![16bit_Terrain_NoSmoothing|690x303](upload://eg2TvPGwBTdUg0kRH0PK19F61t5.jpeg) 
IMO quite the difference :blush:

-------------------------

suppagam | 2019-07-17 23:37:13 UTC | #23

How do you guys apply a normal map to an entire terrain in Urho? Something along the lines of what is possible with the old UDK:

https://i.ytimg.com/vi/EtR-4vA6wAg/maxresdefault.jpg
https://i.imgur.com/uUfYe.jpg
http://ryanwwatkins.blogspot.com/2012/06/udk-desert-landscape.html

Technical reference:
https://api.unrealengine.com/udk/Three/TerrainAdvancedTextures.html

Or even Torque3D terrains:
https://theterrainguy.files.wordpress.com/2012/11/wip_00.jpg
http://i.imgur.com/xGZAIkY.jpg

-------------------------

JTippetts | 2019-07-18 11:14:24 UTC | #24

Out of the box, the Urho3D TerrainBlend shader can't do a whole-terrain normal map. However, modifying it to use one is quite simple.

1) Add another sampler, sNormalMap4
2) In PS(), use the existing vTexCoord/iTexCoord (GLSL/HLSL) that is used to sample WeightMap, and use it to also sample the normal map.
3) If the normal map is a tangent-space normal map (ie, blue) then you have to swizzle the green blue channels, so that green maps to Z and blue to Y. If it's an object-space normal map (ie, yellow) then this is not necessary. vec3 normalsample=texture2D(sNormalMap4, vTexCoord).rbg;
4) Convert the normal map sample to a normal by normalize(normalsample*2.0-1.0) and assign it to normal.

You can look at https://pastebin.com/9h7pquMm to see this modification done to the GLSL shader; the HLSL modification will be quite similar. And the result can be nice:

https://i.imgur.com/QSC3Ftg.png

-------------------------

