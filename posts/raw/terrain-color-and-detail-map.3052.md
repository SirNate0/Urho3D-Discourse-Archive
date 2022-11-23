rasteron | 2017-04-26 13:25:29 UTC | #1

Some small stuff here as I was just messing around with the default terrain, I got a bit of detail and color map added to improve the terrain visuals up close and from a distance. Still a work in progess with the height or elevation modified to shorten the process and generate a 2048x2048 color map.

<img src='//cdck-file-uploads-global.s3.dualstack.us-west-2.amazonaws.com/standard17/uploads/urho3d/original/1X/b582fcf702a7d95b219b1fc013c0038579fc2b4b.png'>

<img src='//cdck-file-uploads-global.s3.dualstack.us-west-2.amazonaws.com/standard17/uploads/urho3d/original/1X/bed7cd2af10a1da6f8a92160c438240ec17b0d6d.png'>

**Color and Detail map only**
<img src='//cdck-file-uploads-global.s3.dualstack.us-west-2.amazonaws.com/standard17/uploads/urho3d/original/1X/355236542d24ef2d4c2c3a5369f35fb16b2b5933.jpg'>

**Terrain Weights texture as Color map for testing and aligning uv scale**
<img src='//cdck-file-uploads-global.s3.dualstack.us-west-2.amazonaws.com/standard17/uploads/urho3d/original/1X/112684b343b66cbd2151328eca904da729676f03.png'>

Imgur Set
http://imgur.com/a/Y8J1p

-------------------------

johnnycable | 2017-04-26 14:56:21 UTC | #2

Well, surely it looks better than default ones! :grin:
Proposed for entering next release!

-------------------------

KonstantTom | 2017-04-26 16:16:48 UTC | #3

It looks really cool! :+1:
I think, this terrain should replace default one in Urho3D samples.

-------------------------

smellymumbler | 2017-04-26 19:21:12 UTC | #4

Holy crap, that's awesome! :D

Can the detail map be added on a per channel basis? I mean, one detail for grass, another for rock, another for sand, etc.

-------------------------

johnnycable | 2017-04-26 19:40:19 UTC | #5

With some modifications to the cubes, could take on a eerie, alien look...

-------------------------

Modanung | 2017-04-26 21:08:12 UTC | #6

Our [Flintstone-mobile](http://wac.450f.edgecastcdn.net/80450F/fun107.com/files/2012/11/flintstones-e1354034454144.png) would maybe require an upgrade then. I agree it's prettier, but quite a bit more hilly too.

-------------------------

rasteron | 2017-04-27 05:06:22 UTC | #7

Thanks guys! :) As for other media like these replacement diffuse textures, it was a quick test so I have used L3DT to generate color maps out of its base textures and the modified heightmap. I have used the Temperate climate set on this setup and apparently the license prohibits redistribution of its base textures, so I'll just find other alternatives that has either Public Domain or CC license when it is ready for PR or release.

-------------------------

rasteron | 2017-04-27 05:07:03 UTC | #8

[quote="Modanung, post:6, topic:3052, full:true"]
Our Flintstone-mobile would maybe require an upgrade then. I agree it's prettier, but quite a bit more hilly too.
[/quote]

haha nice one :smiley:

-------------------------

rasteron | 2017-04-27 13:52:21 UTC | #9

[quote="smellymumbler, post:4, topic:3052"]
Holy crap, that's awesome! :smiley:

Can the detail map be added on a per channel basis? I mean, one detail for grass, another for rock, another for sand, etc.
[/quote]

Thanks @smellymumbler! :) Yes with some tweaks I think this is also possible.

-------------------------

Sinoid | 2017-04-27 18:49:45 UTC | #10

> Can the detail map be added on a per channel basis? I mean, one detail for grass, another for rock, another for sand, etc.

You can pack grayscale maps into channels of an RGBA texture and get the mixed value pretty easily.

    vec4 blend = texture2D(BlendMap, texCoords).rgba;
    vec4 detVal = texture2D(PackedDetailTextures, texCoords * DetailScalingFactor).rgba;
    float dotValue = dot(detVal, blend);
    float sVal = 1.0 - (dotValue * 2.0);
    oColor += (-sVal);

Light-weight enough that you could also get an analytic normal from it with additional samples.

-------------------------

smellymumbler | 2017-04-27 19:34:56 UTC | #11

Where would `PackedDetailTextures` come from? I imagine i have a single texture, a splatmap, where each channel contains a different material definition: sand, grass, rock and snow (R, G, B, A). I use those as masks to apply 4 different channels in my terrain. Each material contains 4 textures: diffuse, specular, normal and detail.

-------------------------

Sinoid | 2017-04-27 19:38:41 UTC | #12

They're grayscale detail-texture maps for each blend channel, not materials - completely different thing from detail-mapping.

-------------------------

smellymumbler | 2017-04-27 22:45:48 UTC | #13

http://urho3d.wikia.com/wiki/Expand_default_terrain_material_to_6_textures_using_the_six_primary%26secondary_colors

Like that? So, if i want specular/normal, i just have to load up more texture units and load the respective maps?

-------------------------

Victor | 2017-04-27 23:14:47 UTC | #14

You can also use texture arrays to allow for more textures. ;) You can do this manually (send a large texture to the shader which contains multiple textures), or using the TextureArray feature.

https://discourse.urho3d.io/t/how-to-use-texture2darray/2695/2

-------------------------

