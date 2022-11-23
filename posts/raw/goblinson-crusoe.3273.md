JTippetts | 2017-06-21 06:43:16 UTC | #1

Here are some recent images of my game, Goblinson Crusoe:

<img src="//cdck-file-uploads-global.s3.dualstack.us-west-2.amazonaws.com/standard17/uploads/urho3d/original/1X/1317523c26646655b304b843915ffe2d7d4bc7d7.jpg" width="690" height="388"><img src="//cdck-file-uploads-global.s3.dualstack.us-west-2.amazonaws.com/standard17/uploads/urho3d/original/1X/e726c5f2df5413a7c86b5eecd6ad640d687ab94a.png" width="666" height="500"><img src="//cdck-file-uploads-global.s3.dualstack.us-west-2.amazonaws.com/standard17/uploads/urho3d/original/1X/773707e12f305a0a4e69c3f186441cd3c078ca02.png" width="666" height="500">

Goblinson Crusoe is a turn-based, hex-based hack-and-slash/rpg that I have been working on for a couple years now (in between kids, a house and a full-time job). The game features elements of crafting, a variety of encounters (boss fights, dungeon crawls, base offense, base defense, etc...), exploration, and intense turn-based combat. It is still very much in progress, but it is coming along.

-------------------------

yushli1 | 2017-06-21 07:03:06 UTC | #2

Looks quite nice. Is it based on Urho3D? 
And do you have plans to open source and/or share some tutorials on how to make it,like the plants, and dynamic lighting effects?

-------------------------

JTippetts | 2017-06-21 07:35:05 UTC | #3

Yes, it is made using Urho3D. I use a slightly modified Urho3DPlayer.exe (that includes some of my own stuff, notably a few custom components and my Perlin noise library), and the bulk of the game is written in Lua.

The lighting is simple point lights in the basic Forward renderpath, a testament to the power of Urho3D "out of the box", since I get decent performance even with a fairly large number of lights. I use the Bloom post-process, no gamma correction. The hex ground tiles use a tri-planar based shader that I have written about here on the discussion forums before. Those tiles are really about the only non-vanilla stuff I do; well, that and a high-light shader that gives a faction-colored highlight to objects when you hover over them with the mouse.

For the plants, I use a variety of techniques. Some of the small shrubbery-type plants were created using ngPlant. Larger trees were created in Blender using the technique described at https://simonschreibt.de/gat/airborn-trees/ though I'm still perfecting my modeling techniques there. Various other ground-cover type grasses and whatnot are created as billboard clumps.

I do all the artwork myself, mainly in Blender and the Gimp. I make use of procedural methods when I can, to save some labor. I have also lately been experimenting with using MakeHuman to generate humanoid (goblin and ogre type) characters lately, again to save some labor. I tend to write more frequent updates about the game in my dev journal at https://www.gamedev.net/blogs/blog/33-why-you-crying/

-------------------------

Modanung | 2017-06-21 08:12:35 UTC | #4

Seeing some great improvements in graphics. I really like the tiles 'n trees.

-------------------------

yushli1 | 2017-06-21 08:25:52 UTC | #5

Thanks for the detailed explanations. Do you have playable demo download link so that we can try out? The screen shots looks really tempting.

-------------------------

JTippetts | 2017-06-21 18:31:39 UTC | #6

Thanks, guys. I don't have a playable demo yet. I am working towards one that I can release to a small group for some feedback and testing, but I doubt I'll do any kind of wide release any time soon. It's not far enough along that I'd feel comfortable with that right now.

-------------------------

yushli1 | 2017-06-22 02:52:06 UTC | #7

I'd like to encourage you to share it out among this community at least. There are not many complex and beautiful demos right now using Urho3D(compared to other engines). Yours would be a great addition.
BTW, I enjoy reading your gamedev blogs. Thank you for writing it.

-------------------------

jmiller | 2017-06-23 12:31:37 UTC | #8

It is great to see **GC** take its place on the forum, with notable improvements! and I'm hoping to see more as it evolves.

I started my own Urho Test Chamber with a port of your [url=https://www.gamedev.net/blogs/entry/2259326-demo-and-explanation-of-third-person-camera/]camera controller[/url] from your gamedev blog and your triplanar shader. :)

-------------------------

lexx | 2017-06-25 07:13:45 UTC | #9

Looks beautiful. Long time project. Keep up the good job.

-------------------------

Bananaft | 2017-07-03 14:02:13 UTC | #10

Looks neat. I suggest you to add gamma coorection and tonemapping. It will make your lighting and effects look even cooler.

-------------------------

JTippetts | 2017-07-03 14:09:56 UTC | #11

I haven't had good luck with using gamma and tonemap. Admittedly, I don't know jack squat about either so I wouldn't know how to tune it, but when I append Preprocess/GammaCorrection.xml to the render path I get this result:

<img src="//cdck-file-uploads-global.s3.dualstack.us-west-2.amazonaws.com/standard17/uploads/urho3d/original/1X/46bbc4faff4b3afe56026567c853d4c8a5944925.jpg" width="666" height="500">

Appending Tonemap.xml just makes it look even worse:

<img src="//cdck-file-uploads-global.s3.dualstack.us-west-2.amazonaws.com/standard17/uploads/urho3d/original/1X/6e4bd48b1523a2e845d79e951d3b53c4a42ba5ec.png" width="666" height="500">

Personally, I prefer the "warmer" look without gamma correction.

-------------------------

Bananaft | 2017-07-03 20:03:04 UTC | #12

do you have HDR rendering enabled?
There are three methods of tonemapping in Tonemap.xml, it seems like you need to delete or disable two of them. Also, tonemapping might a have gamma correction be built in it, or it might not. I bet Uncharted does.

I recomend using Uncharted as I'm not sure wich of the reinhard methods the other two are.

https://github.com/urho3d/Urho3D/blob/97eba580b5564db9d6f0336a7258194d04b84dda/bin/Data/PostProcess/Tonemap.xml

It's up to you of course, a matter of taste. But your second screenshot has a lot of excessively bright stuff and it should benefit from it.

-------------------------

hdunderscore | 2017-07-03 19:50:58 UTC | #13

That first one looks much better in my eyes, there is less light burning vs your earlier screenshots.

-------------------------

Alex-Doc | 2017-07-03 20:21:47 UTC | #14

I think the first screenshots looks more old-school style, while the new one (the non-totally dark) looks a bit more "pastel" as seen in newer games.
Personally I'd prefer a custom post-processing filter to have a good compromise between the two and most of all, I would like to encourage the developer, as artist to make the game look as how he want us to feel it. :slight_smile:

-------------------------

JTippetts | 2017-07-04 16:02:27 UTC | #15

So, I'm trying to figure out this gamma correction and tonemapping stuff, and I just can't seem to obtain a result that is palatable to me. Here's what I've got. I enable HDRRendering, then set up some keys to toggle the gamma correction and Uncharted2 tonemapping effects.
<img src="//cdck-file-uploads-global.s3.dualstack.us-west-2.amazonaws.com/standard17/uploads/urho3d/original/1X/3ade420bb0fffebfce5c2cfc9aaddcc754ede747.png" width="666" height="500">
In the top left is the scene with neither tonemapping nor gamma. On the top right is gamma correction only. On the bottom left is tonemapping only. And on the bottom right is both.

The result reminds me of this old VGCats strip that says 'real is brown': http://www.vgcats.com/comics/?strip_id=222

I could possibly live with the tonemap/no gamma version (with some adjustments to the particle effect colors so it's not so brown). But anything with gamma just seems washed-out and basically unplayable to me. The only one of those 4 versions that seems in any way alive and vibrant and warm is the one without either postprocess filter applied. Am I just doing it wrong? Is this really how people play their games? Admittedly, I haven't bought a 'new' game in over a decade, so I'm probably out of touch with what gamers expect these days, but if I _did_ buy a new game and it looked washed-out like that, I doubt I would play it more than a few minutes.

-------------------------

Bananaft | 2017-07-04 18:09:15 UTC | #16

whoops, I forgot couple more things you have to do , sorry.
So if you still willing to try it out linear pipeline, and have some patience to not tell me to piss off with my nex-gen bullshit, here are they:

You have to add srgb tag in xml next to all your defuse textures (or do SetSRGB() in code):

    <texture>
    <srgb enable="true" />
    </texture>

And probably readjust some of your lighting settings. Making lights brighter and ambient light darker.

-------------------------

JTippetts | 2017-07-04 19:03:06 UTC | #17

Heh. I've got enough assets in there now, I'm not to keen on the idea of modifying every texture definition, especially since I'm not really convinced of the need. Guess I could start with the terrain textures, though, and see if they make a difference.

-------------------------

JTippetts | 2017-07-05 04:01:29 UTC | #18

Enabling srgb on the textures doesn't seem to have done anything at all. I found a setting in Graphics to enable sRGB mode, but enabling that one makes things even more washed out:

<img src="//cdck-file-uploads-global.s3.dualstack.us-west-2.amazonaws.com/standard17/uploads/urho3d/original/1X/80f0aadf0a3fe88d081d4b5a568a8d060ffb9867.png" width="666" height="500">

That one is with sRGB in Graphics enabled, and gamma correction enabled in the render path.

Thing is, I looked through some of the samples (like the PBR one) that have gamma and tonemapping enabled, and I don't really like the looks of them at all, either. It makes everything seem just washed out and gray, kinda bleak to me. I mean, it probably has its place, but the look and feel I'm going for is a vibrant, cartoony, high-saturation world, so I'm not sure it's really appropriate.

-------------------------

yushli1 | 2017-07-05 11:29:08 UTC | #19

I think the top left is the most charming one. Look forward to playing the demo some day.

-------------------------

iainmerrick | 2017-07-05 15:40:47 UTC | #20

I agree that the original unfiltered version looks best, _but_ I also think some color mapping could make it even better!

As I understand it, setting sRGB in Graphics has the same effect as adding the gamma correction post-process filter. (The first uses the graphics hardware, while the second uses software and loses some precision) If you use both you'll get a double correction.

Assuming all your textures are in the sRGB color space (they almost certainly are), the "correct" thing to do would be:

1. Enable sRGB on all your textures (is there a quick way to do that?)
2. Enable sRGB output on Graphics

That way, the textures will be converted from sRGB -> linear as they're read, the lighting calculations will use linear colors, and the results will be converted from linear -> sRGB so they look right on screen.

Your lighting values will need to be changed, probably reduced a lot, because they'll be interpreted as linear rather than sRGB values. For example 50% gray (#808080) is fairly dark in sRGB, but looks much lighter as a linear color.

Here's a great article that helped me get my head around sRGB vs linear lighting: http://filmicworlds.com/blog/linear-space-lighting-i-e-gamma/

Not doing any color mapping generally looks OK because both textures and screens are generally sRGB. It's only when you start alpha-blending or doing lighting calculations that the results aren't quite right.

Overall, though, you should definitely go with whatever looks best, whether it's "correct" or not!

-------------------------

JTippetts | 2017-07-10 03:49:38 UTC | #21

Uploaded a quick gameplay video today. Kinda cruddy quality, since I still don't really have a high-powered rig for video capture.

https://www.youtube.com/watch?v=RYuIxiz9N1k

-------------------------

hdunderscore | 2017-07-10 08:23:35 UTC | #22

That's looking really good! Looks like there is quite a bit of variety in options and some satisfying and powerful actions. I'm a big fan of seeing numbers flood a screen :D

-------------------------

JTippetts | 2017-07-11 14:41:01 UTC | #23

Thanks, hdunderscore. Everything that is shown there is still "test" stuff... I'm still figuring out what kinds of things will be possible and how to fit the mechanics together. I haven't even fully nailed down the character stats yet, since I don't yet know exactly what damage types and damage mitigation strategies will be available. Wherever it ends up, though, there should be plenty of numbers.

-------------------------

JTippetts | 2017-07-15 22:43:04 UTC | #24

<img src="//cdck-file-uploads-global.s3.dualstack.us-west-2.amazonaws.com/standard17/uploads/urho3d/original/1X/0258013bdc3c242b8f03fd49408d7c3c6a54fbd8.png" width="666" height="500">

Working on having water that can occupy cells of any height. The built-in Water material actually works surprisingly well (with a few small tweaks) for this purpose.

-------------------------

JTippetts | 2018-08-05 22:37:55 UTC | #25

My latest project (aside from HUGE refactoring of combat stats) has been to start re-purposing my terrain editor to act as a level editor.

[img]//cdck-file-uploads-global.s3.dualstack.us-west-2.amazonaws.com/standard17/uploads/urho3d/original/2X/8/84e8ca53cc67bf677ff3137873d166a4f6fa2359.jpg[/img]

Most of the things work, but I'm modifying the way masks work so that I can have masks for the terrain separate from masks for the elevation. Terrain blend textures are much higher resolution than the elevation heightmap, so the masks need to be higher resolution also. Also need to fix the editing cursor, which worked "okay" on a smooth terrain, but doesn't work well on the hex terrain.

-------------------------

JTippetts | 2018-08-16 02:10:09 UTC | #26

<img src='//cdck-file-uploads-global.s3.dualstack.us-west-2.amazonaws.com/standard17/uploads/urho3d/original/2X/c/cdb269be8a092bba64b03c2a7d4223cade87d85f.jpeg'>

Have added water editing to the GC editor. Water editing works a lot like terrain editing; you can use a brush to raise/lower regions, or use a filter from the Filters menu to set all water to a specified height. Masks can be used in these operations to mask off sections to prevent water from being edited.

Also have begun implementing doodad scattering. A UI allows you to create a group, and select doodads from a master list (which is built by scanning the Doodads folder). In the group list, each individual doodad can be assigned a weight, which is used when selecting which doodad to spawn. This way, you can increase or decrease the frequency of certain doodads relative to one another. In the works is a brush system to allow painting with the current doodad group. Doodads are spawned using a filter, and make use of mask settings to prevent spawning in masked-off areas.

Object editing will work similar. (Doodads are non-blocking, non-interactive scene decorations; objects are interactive or blocking elements such as walls, trees and mobs.) I am doing some thought about how I can add a layer of indirection to object spawning, to allow for randomization on level load.

-------------------------

GodMan | 2018-08-21 01:19:17 UTC | #27

Hey for your HDR issue I had a similar issue. I did not use gamma correction. I only used BloomHDR,ToneMap,AutoExposure. Make sure in your materials that you set emissive to zero. The auto-exposure will brighten up darker areas so any additional calculations on the material will look odd. Once I fixed the materials I got pretty good results.

-------------------------

Sunc | 2022-09-08 10:18:05 UTC | #28

For me , the tonemap post process is a confusion. Meanwhile, I do opened HDR rendering in the Graphics setting. 
But the result scene get darker with Uncharted2 version selected in Tonemap.xml, and with no parameters changed.
So what I tried is to refine the exposureBias and maxWhite params to make things look good, at least not to be so much dark. Finally I got 1.0 and 1.0 for both the 2 params, I wonder whether I've done is reasonable, or something went wrong in my project since the default values doesn't make a good view.

-------------------------

