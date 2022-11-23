amit | 2018-07-28 22:23:01 UTC | #1

What is the custom "Binary animation format" for Animation for morphs, any tuts on it?
saw https://urho3d.github.io/documentation/HEAD/_file_formats.html
any sample file to work?

-------------------------

codingmonkey | 2017-07-03 17:06:07 UTC | #2

>any tuts on it?

I took my old crafts (head model) with some shape keys and tried this feature engine.
Video of what happened.

http://youtu.be/QBnMz90g78Q

below zipfile with example exe + source code in C ++
[rghost.ru/59428400](http://rghost.ru/59428400)

key_1 & key_2 to change shapes
key_R - reset all shapes by default
mouse wheel - value control

-------------------------

weitjong | 2017-01-02 01:01:45 UTC | #3

Thanks for sharing it. The real download button in the above link is the one on the top left. :wink:

-------------------------

codingmonkey | 2017-01-02 01:01:46 UTC | #4

no problem, this can used for a new example if required.
I hope that the head is not too heavy for this (golova.mdl ~ 1mb)

>The real download button in the above link is the one on the top left
yes there is a lot of add's buttons download ) 
If in Russia we have not blocked Github.com (with Tor i may only see & dowloand from guthub) i would have placed himself an example and posted a link to the repository. 
But had to do so ) Sorry if that.

-------------------------

cadaver | 2017-01-02 01:01:46 UTC | #5

Assimp defines the concept of morph animations, but it's unused so far (even in latest master). However, the OgreImporter supports saving the morphes from Ogre meshes.

From a testing standpoint as well there certainly should be an example morph-enabled model in Urho repo :slight_smile: One simple possibility is to take a version of the Jack model (from realXtend) that has morphs, the file will just be huge.

-------------------------

codingmonkey | 2017-01-02 01:01:46 UTC | #6

>Assimp defines the concept of morph animations, but it's unused so far (even in latest master). However, the OgreImporter supports saving the morphes from Ogre meshes.
i'm use this blender add-on, is very useful.
[github.com/reattiva/Urho3D-Blender](https://github.com/reattiva/Urho3D-Blender)
*but before you start exporting shapes you must adjust all shapes values to 0. otherwise is exported not correctly.

and i'm forgot about one thing to tell. may be it's issue and need to resolved.
in 3d editor shapes also used negative values to counter shapes poses, it's very important thing to do some shape variants with face mimic.
but i'm now try to use nagative values with my example and it's no affect to conter shape pose. it's need to resolve.

-------------------------

amit | 2017-01-02 01:01:47 UTC | #7

I understand the morph data store, what i want is [b]animation time line for morphs[/b].

@codingmonkey thanks for code and blender export, I use blender so it help a lot

-------------------------

cadaver | 2017-01-02 01:01:47 UTC | #8

In Urho, applying morphs is an ugly and CPU-expensive operation, so it's really intended for something like character customization, where you don't need constant animation or an actual timeline.

-------------------------

codingmonkey | 2017-01-02 01:01:47 UTC | #9

@[b]amit[/b]
>animation time line for morphs.
I guess what morfs use only two max/min delta vertexes buffers(or only max, min - it's base mesh) and affect factor value to determine which buffer has more weight in to base mesh.

and for timeline you need more then 2 state of mesh, and i guess what name of this "vertex animation" and it's very huge in mem.

if you need to play morf at a certain time, write code like this:

[code]static float accuTime = 0.0f;
float lenInSec = 5.0f;
float curValue = accuTime / LenInSec ; 
accuTime += timeStep
Model_->SetMorphWeight(StringHash("SomeShapeAnimWith5SecLen"), curValue);[/code]

[b]cadaver[/b]
i think better to use a lot of bones in a special rig for the face ) 
or just use shape keys with values

-------------------------

amit | 2017-01-02 01:01:47 UTC | #10

What i was tryin was to export morph animation timeline from blender and directly use it with out settin morph weith manually.
"Binary animation format" has mask for bones only, maybe we can use attribute animation system with call back for more automation for animation of morphs.

Ill make my own system to do the same now :slight_smile:

@cadaver, yeah but some time we need it, as i req it now, hope the cpu calculation is optimised. hardware would limit it to certain no. of morphs .. a limit i do not want (12 morph req).
All this on ios/android platform.

-------------------------

boberfly | 2017-01-02 01:01:48 UTC | #11

If the morphs are just done on one mesh and it isn't too heavy, iOS/Android should handle it fine using the CPU and glBufferSubData (what Urho3D currently does). But yeah it invokes a large sync point so your GPU will stall. :frowning:

There's a GPU-friendly way of doing morphs for DX9/GL2.x, but it involves vertex texture fetch support (ie. accessing a sampler2D from a vertex shader) and many mobile GPUs I don't think support it, although I think a few old iOS devices did support it but it was undocumented :slight_smile:. The idea is that you index into a texture and bring in new vertex positions from it, and you can atlas a bunch of morphs into your texture, provided it is big enough to store every vertex as an RGB pixel (and it is probably best to use something bigger than RGB8 otherwise there's precision loss). Using Urho3D's current format you'd just grab the morph data and procedurally build a texture atlas from it and then bind it to some texture unit and in the vertex shader do some GLSL index and lerp magic off the base position of the verts.

Another way is to embed the different morphs into empty attribute data elements in your vertex buffer and just lerp them from your base position element in the shader. You'll just be limited to a very tiny amount of them (typical mobile GPUs can store up to 8-16, and typically you'd use a few of them for the normals/tangents/pos/texcoords/skinbinds/etc.)

-------------------------

codingmonkey | 2017-01-02 01:01:48 UTC | #12

>GPU-friendly way of doing morphs for DX9/GL2.x, but it involves vertex texture fetch support 
it's good idea in this case engine must setup or choice render strategy on fly or in start time.  
if device support texture fech it use them, if this feature is not supported it use cpu-based morfs. i think this is right way, because it support old and modern devices.
at last may be the right way will be lie in the fact that refuse to support very old hardware. 

and finally, I think that the shape keys and vertex animation even tighter and use one technology, but in fact two different things.
if you want long animation of vertex then it is the task of the new component VertexAnimation, i guess.

ps. and in addition I want to note that the shapekeys need support negative values. If it does not have, you must to do some facial shapekeys twice.
For example: a smile with negative values can turn into sadness, without the negative values have to do a "smile" and "sadness" as individual shapekeys.

-------------------------

amit | 2017-01-02 01:01:48 UTC | #13

@boberfly thanks for info,   ill try cpu first, if it works with my model, its all ok else
i read some where, ios 7 has "vertex texture fetch support" , else back to pc.

-------------------------

0x4D3342 | 2018-07-27 11:21:22 UTC | #14

hi,it seems your link is not working

-------------------------

CE184 | 2020-12-06 23:30:33 UTC | #16

Could you re-upload the link? Thanks!

-------------------------

