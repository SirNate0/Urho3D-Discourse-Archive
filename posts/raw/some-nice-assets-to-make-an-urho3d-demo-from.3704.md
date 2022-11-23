glebedev | 2017-11-01 20:56:25 UTC | #1

I hope someone would be interested. I've imported couple free/cc assets into Urho3D:
https://github.com/gleblebedev/Urho3D_Nyra
https://github.com/gleblebedev/Urho3D_SanMiguel

Could someone help me to make pretty Urho3D demos from it? By "help" I mean fixing materials, lighting etc.

-------------------------

glebedev | 2017-11-01 21:02:04 UTC | #2

<img src='//cdck-file-uploads-global.s3.dualstack.us-west-2.amazonaws.com/standard17/uploads/urho3d/original/1X/83a036c996d5c46662c7b79635359a042ecb74d5.jpg'>

-------------------------

Eugene | 2017-11-01 22:55:42 UTC | #3

Good job!
I think the best direction is to make all materials PBR first... Unsure if I have time for it now, but it definetely should be done at some point.

-------------------------

glebedev | 2017-11-02 00:00:59 UTC | #4

I hope this would inspire you - all materials converted to PBR.

<img src='//cdck-file-uploads-global.s3.dualstack.us-west-2.amazonaws.com/standard17/uploads/urho3d/original/1X/c4a5b9cb9458ea729466a5fd797155aa3bf18c6a.png'>

-------------------------

glebedev | 2017-11-02 09:27:06 UTC | #5

<img src='//cdck-file-uploads-global.s3.dualstack.us-west-2.amazonaws.com/standard17/uploads/urho3d/original/1X/49bc90fdd98f44055435fb29af9e8e7dca75bc81.jpg'>

-------------------------

Eugene | 2017-11-02 11:28:58 UTC | #6

Nice.
It could be good start point for technical improvements in shaders and posteffects (e.g. SSAO)

BTW, @dragonCASTjosh, any ideas about this (Fresnel?) noise at the edges?

-------------------------

orefkov | 2017-11-02 14:20:55 UTC | #7

Nyra is very nice. Is it rigged?
20K tris will be perfectly shown even on low mobile devices.

-------------------------

Eugene | 2017-11-02 14:57:28 UTC | #8

I don't think so.
You could try Mixamo to make it moving quickly, but it could have problems caused by model pose.

-------------------------

glebedev | 2017-11-02 16:10:27 UTC | #9

There is a T-pose available. I just ignored it. From what I know there aren't bones in it too.

-------------------------

dragonCASTjosh | 2017-11-02 16:21:50 UTC | #10

@glebedev nice work on getting SanMiguel in engine, if possible can you include roughness/metallic maps for the materials  

@Eugene bit sure what you mean but i have still doing rendering work at the moment so be ready for a cool rendering branch at some point

-------------------------

Eugene | 2017-11-02 16:38:21 UTC | #11

[quote="glebedev, post:9, topic:3704, full:true"]
There is a T-pose available. I just ignored it. From what I know there aren’t bones in it too.
[/quote]

Mixamo could auto-rig and auto-animate T-pose models. Joints animation is nasty, but some small animaions looks ok.

[quote="dragonCASTjosh, post:10, topic:3704"]
bit sure what you mean but i have still doing rendering work at the moment so be ready for a cool rendering branch at some point
[/quote]
I'm about these pixels:
![image|414x255](upload://whRXb2i3aN4mCGtXjB7yyFzHlS2.jpg)
If I understand things correctly, the noise appears because non-metal materials get reflective at the very tiny edge.
It will probably look much better with screen-space reflections (Note: second important thing).

-------------------------

dragonCASTjosh | 2017-11-02 19:45:16 UTC | #12

Yea from my understanding it a mix a small things such as no AA, secular aliasing and maybe a few issues with some of the Fresnel math. Its something ill be keeping my eye on and if its still a problem after TAA and AO then ill come back to it

-------------------------

glebedev | 2017-11-02 23:01:18 UTC | #13

I'll check again but I think I've added all available textures :(

-------------------------

glebedev | 2017-11-03 12:34:11 UTC | #14

https://github.com/gleblebedev/Urho3D_SanMiguel/raw/master/screenshot.png

-------------------------

jmiller | 2017-12-31 19:47:20 UTC | #16

[img]//cdck-file-uploads-global.s3.dualstack.us-west-2.amazonaws.com/standard17/uploads/urho3d/original/2X/c/cef0d5702ba9445b8853f455c4654507e2eb519e.jpg[/img] [img]//cdck-file-uploads-global.s3.dualstack.us-west-2.amazonaws.com/standard17/uploads/urho3d/original/2X/9/91338a4b649c8c01bcd0b1075339c269ac2fdf16.jpg[/img]
[url=https://imgbox.com/g/Tv4DKgbTDi]Nyra gallery[/url]


https://www.dropbox.com/s/837ylmz2abkga0b/Nyra_body_head_properties.7z

Here are two rough-draft PBR roughness/metallic map textures for anyone to play with. It's very unfinished (e.g. much of the gold is not yet 'metal').
Created from the full-resolution TGAs for body/head (at 48MB/12MB). Ad-hoc process: Invert specular map for roughness (red channel), various tweaks for metalness (green channel). The gallery shows some downsampled versions of these.

[details="sample PBR material"]
[code]
<material>
	<technique name="Techniques/PBR/PBRMetallicRoughDiffNormalSpec.xml"/>
	<texture name="Textures/body_d.tga" unit="diffuse"/>
	<texture name="Textures/body_n.tga" unit="normal"/>
	<texture unit="specular" name="Textures/body_properties.tga" />
	<parameter name="UOffset" value="1 0 0 0" />
	<parameter name="VOffset" value="0 1 0 0" />
	<parameter name="MatDiffColor" value="1 1 1 1" />
	<parameter name="MatEmissiveColor" value="0 0 0" />
	<parameter name="MatEnvMapColor" value="1 1 1" />
	<parameter name="MatSpecColor" value="1 1 1 1" />
	<parameter name="Roughness" value="0" />
	<parameter name="Metallic" value="0" />
	<cull value="ccw" />
	<shadowcull value="ccw" />
	<fill value="solid" />
	<depthbias constant="0" slopescaled="0" />
	<alphatocoverage enable="false" />
	<renderorder value="128" />
	<occlusion enable="true" />
</material>
[/code]
[/details]

-------------------------

glebedev | 2018-03-10 11:41:44 UTC | #17

Sorry, it took me so long...
https://github.com/gleblebedev/Urho3D_Nyra/raw/master/nyra.png

-------------------------

smellymumbler | 2018-03-09 16:05:55 UTC | #18

What's with the white spots?

-------------------------

Sinoid | 2018-03-09 17:28:02 UTC | #19

> What’s with the white spots?

It's the pair of scene setup and non-HDR pipeline. The skybox that's included in the sample content isn't suitable for PBR - it's both inappropriately high resolution and doesn't have convolved mipmaps.

You can see the skybox in the nose, forehead, and corners of the skin around the eyes - which is going to be partially from mips not being convolved and the PBR shaders not being great for skin. White-leaning cubemaps are also generally problematic.

The HDR pipeline would smooth out the severity of the highlight edges during the tonemapping/bloom.

-------------------------

glebedev | 2018-03-10 11:41:29 UTC | #20

Fixed by switching to HDR skybox.

-------------------------

