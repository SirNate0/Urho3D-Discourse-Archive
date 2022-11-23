rasteron | 2017-01-02 01:05:14 UTC | #1

Great update Sinoid! One thing to note though and I assume you already considered blending dynamic shadows and the lightmaps for this tool?.. but I'm sure you already anticipated this one.  :wink:

Maybe something simple like "Bake Scene", with texture size for the lightmaps as options, etc in GUI, and a switch option between real-time and baked lights. 

This is really awesome work, can't wait to try it out..

-------------------------

globus | 2017-01-02 01:05:14 UTC | #2

This is not a real need at the moment but just thoughts:

Lightmap present in scene.
Can light emmiter drop light only on dynamic objects?
Can lightmapped static model drop shadow only on dynamic objects?

-------------------------

Bananaft | 2017-01-02 01:05:14 UTC | #3

Whoa, really impressive!

Two things I don't like about baked lighting:
1) Baking in 3d editor is pain. It takes time, and a lots of repetitive actions, you make it each time you want to move a tiny thing or made a mistake. So, having a one button in-editor baking is super cool.
2) There always a challenge of getting static and dynamic geometry look similar. And that's the thing you just can do perfect. They will always be a bit different.

So, how do you see shading on dynamic models? Dynamic lights + cubemap set by zone? What about situation, when some large object casting a shadow, and dynamic model can move into it? Have you considered adding a light probes?

-------------------------

globus | 2017-01-02 01:05:15 UTC | #4

[img]http://i.piccy.info/i9/84ce8fe36f777b3adb0b6fc6d0dfddda/1432333191/49395/912050/shadows.jpg[/img]
Sun and Lamp Dont have effect on Ground and House.
Only on dynamic objects - Car and Ball.

Car and Ball be able to cast shadows on all objects 
(Static and Dynamic)

Question:
Can House cast its shadow only on Dynamic objects (Car and Ball)?
(House himself or any helper mesh or lod mesh)

-------------------------

sabotage3d | 2017-01-02 01:05:15 UTC | #5

Your approach looks simialr to this one: [geomerics.com/wp-content/upl ... ecture.pdf](http://www.geomerics.com/wp-content/uploads/2014/03/radiosity_architecture.pdf)
In action: [geomerics.com/wp-content/upl ... Subway.mp4](http://www.geomerics.com/wp-content/uploads/2015/03/Enlighten_Subway.mp4)

-------------------------

globus | 2017-01-02 01:05:15 UTC | #6

[quote="globus"]
Car and Ball be able to cast shadows on all objects 
(Static and Dynamic)
[/quote]

Problems with Lightmaps + dynamic lights
[url]http://discourse.urho3d.io/t/problems-with-lightmaps-dynamic-lights/1073/1[/url]
Next images from original post demonstrate problem.
[img]http://i.piccy.info/i9/d9b35c3c0dd76d52b3f68fd48e043459/1432380771/81702/912050/problem.jpg[/img]
[img]http://i.piccy.info/i9/04869e516493f0256a7dcf9d761b6cc7/1432381167/61793/912050/problem2.jpg[/img]

-------------------------

Bananaft | 2017-01-02 01:05:17 UTC | #7

[quote="Sinoid"]
After having thought about this more. Light probes are going to live in the Zone, most likely as subdivisions/voxels of spherical harmonics ambient cubes so that zones don't have to be tiny and all over the place. Mobile could then choose the resolution it wants to use and the existing Zone properties still function on top of that (ie. Zone color biases the ambient cubes, etc). Cube maps are a different beast.
[/quote]

Seems reasonable. There can be only one reflection cubemap per zone, and a bunch of light probes affecting diffuse.

Ability to edit each probe's position can be essential. In cases like placing them on terrain surface, or making sure no probe placed inside geometry. Navmesh can be a good reference for lightprobe placing.

-------------------------

globus | 2018-02-18 18:13:42 UTC | #8

May be look code in free (MIT licence) Godot engine?

Global Illumination Workflow
https://www.youtube.com/watch?v=UXFXTgy439s

Description:
Short demonstration of the Global Illumination workflow in Godot Engine. 
A low resolution lightgrid is used so it takes a short time to bake. 
The light octree system generates a 3D lightmap, so it makes a secondary UV unnecesary

Then, a dynamic object is moved around the level, fully sampling the light from it?s surroundings.

-------------------------

sabotage3d | 2017-01-02 01:05:26 UTC | #9

Looks really cool so far. Have you considered using ptex for storing the lightmaps, a good alternative to traditional uvs and can safe quite a bit of memory.
[ptex.us/documentation.html](http://ptex.us/documentation.html)
[developer.nvidia.com/sites/defa ... 20Ptex.pdf](https://developer.nvidia.com/sites/default/files/akamai/gamedev/docs/Borderless%20Ptex.pdf)

-------------------------

rasteron | 2018-02-18 18:13:59 UTC | #10

That is an interesting library sabotage3d, great find. :slight_smile:   and great work so far Sinoid :exclamation:

-------------------------

globus | 2018-02-18 18:14:53 UTC | #11

Building platform: windows  mingw

note:
[b]LightmapGenerator.h 73[/b]
no known conversion from argument 2 from 

[code]
"Urho3D::VariantMap& <aka Urho3D::HashMap<Urho3D::StringHash, Urho3D::Variant>>"
[/code] 
to
[code]
"Urho3D::VariantMap& <aka Urho3D::HashMap<Urho3D::StringHash, Urho3D::Variant>&>"
[/code]

and ====================

error:
[b]LightmapGenerator.cpp 255[/b]
no matching function for call to
[code]
"LigtmapGenerator::HandleGenerate<Urho3D::StringHash, Urho3D::VariantMap>"
    HandleGenerate<StringHash<>, VariantMap<>>
[/code]

-------------------------

sabotage3d | 2017-01-02 01:06:02 UTC | #12

Again awesome work ! I am big fan of spherical-harmonics. Are you working on anything to convert HDR images to SH coefficients ? Is there any bands limitation in the current workflow ?  I guess 8 bands would be the maximum for games.
Do you have any plans for tracing shadows from the spherical harmonics, although this might be expensive.

-------------------------

sabotage3d | 2017-01-02 01:06:02 UTC | #13

There is already a code to convert HDR to SH, I haven't tested it but it looks interesting: [github.com/rlk/sht](https://github.com/rlk/sht)
Yeah this is the paper but I think it can be extended to fake lights for SH GI effects like in this paper: [ppsloan.org/publications/irr ... gs_jgt.pdf](http://www.ppsloan.org/publications/irradiance_rigs_jgt.pdf)

-------------------------

sabotage3d | 2017-01-02 01:06:02 UTC | #14

I also found this on how to fix UV seams in lightmaps and doing shadows using SH . I think it looks good in the end, as the game is quite nice visually
[miciwan.com/SIGGRAPH2013/Lightin ... f%20Us.pdf](http://miciwan.com/SIGGRAPH2013/Lighting%20Technology%20of%20The%20Last%20Of%20Us.pdf)

-------------------------

sabotage3d | 2017-01-02 01:06:03 UTC | #15

For simple ambient occlusion should be only 1-2 SH bands which prove me if I am wrong is around 2-4 textures. This would be pretty neat for mobile.

-------------------------

friesencr | 2017-01-02 01:06:03 UTC | #16

[quote="Sinoid"] though SH Lightmapping should probably be restricted to requiring texture array support.[/quote]

I have ogl texture array support mostly working in a branch of mine. 

[github.com/friesencr/Urho3D/blo ... e2DArray.h](https://github.com/friesencr/Urho3D/blob/voxel/Source/Urho3D/Graphics/OpenGL/OGLTexture2DArray.h)
[github.com/friesencr/Urho3D/blo ... DArray.cpp](https://github.com/friesencr/Urho3D/blob/voxel/Source/Urho3D/Graphics/OpenGL/OGLTexture2DArray.cpp)

I had some errors generating mipmaps.  I fell back to letting opengl making the mipmaps for me.  Texture array extension support is very good on opengl2.  There is also some issue with cubemaps and the deserializer.  Cubemap is hardcoded to xml filetype.  So a tag should be made and read from for arrays/cubemaps and a serializer/deserializer needs to be added to my code too.

-------------------------

sabotage3d | 2017-01-02 01:07:47 UTC | #17

Thanks a lot for the hard work. I have been testing the Lightmapper for a while, thanks to Sinoid it works great. I created a repo with an example it is still work in progress but the basic shaders are working: [github.com/sabotage3d/Urho3DLightmapExample](https://github.com/sabotage3d/Urho3DLightmapExample)
Can't wait for this to be merged with the master branch :slight_smile:

-------------------------

Hevedy | 2017-01-02 01:07:49 UTC | #18

Wow I need try this.

This will be nice for baked light finally! and if someone over here include in Urho3D a way of realtime LPV or something for get realtime GI that will be x2 of awesome to have the 2 options one for more details and the other for don't need compile and for larger maps.

@Sinoid You guys can use the Purpleprint Kit assets got integrated UV for lightmap originally created for UE4. [github.com/Hevedy/PurpleprintKi ... try/Simple](https://github.com/Hevedy/PurpleprintKit/tree/master/Content/3D/Geometry/Simple)

-------------------------

Lumak | 2017-01-02 01:07:54 UTC | #19

You're doing great work!

-------------------------

Hevedy | 2017-01-02 01:07:54 UTC | #20

[quote="Sinoid"][quote]Can't wait for this to be merged with the master branch[/quote]
[quote]Wow I need try this.[/quote]

There's some cleanup and documentation required before it's even PR worthy.

The handling of the lightmaps runtime side is also quite questionable and probably full of exceptional failure cases. I've been meaning to look at allowing Resources to spoof as being other resources (or at least indicate who the REAL resource is). The hassle is that from a usability standpoint, lightmapping has to be reasonably non-intrusive ... it is unacceptable for lightmapping to interfere with the materials that have been defined.

[quote]This will be nice for baked light finally! and if someone over here include in Urho3D a way of realtime LPV or something for get realtime GI that will be x2 of awesome to have the 2 options one for more details and the other for don't need compile and for larger maps.[/quote]

I've been working on some hybrid CPU/GPU GI stuff. It's going quite well, but no where near primetime. Hilariously, I've been enhancing my knowledge of Geometric Algebra to find better solutions, which happens to be exactly what Enlighten uses (only became aware of that after I started diving down that round for reprojection of point clouds, now it's a patent dancing nightmare).

I want to point out, that at all times, screenspace GI should be an option if you're doing GI at all. If you're going to do SSAO, there's no reason not to do SSDO on top of anything else.[/quote]

I see tests of the SSGI in UE4 and give problems is like the SSR but the reflections you notice less than the light, if you add sometype of dynamic GI you got in UE4 the LPV in alpha/beta status as reference but that LPV or something like that should be better than SSGI.
*Tested in demo scenes probably in a final result game looks better without problems idk.

-------------------------

boberfly | 2017-01-02 01:07:54 UTC | #21

Very cool work Sinoid!

Have you looked at blender's cycles? That renderer can be decoupled from blender as standalone with an Apache 2.0 license and can do bake maps. I think it needs some basic patches though to make standalone take in meshes and use the bake functions instead of the regular render functions, very doable though. Even the XML API it has out of the box could be 'hacked' to just take in Urho3D's scenegraph format and leverage Urho's shadow mesh buffers (as in, the CPU-side buffers) which go directly into cycles' BVH conversion (bypassing its mesh class), hell I was thinking about taking your lightmap integration code and making it pass into cycles as an idea. Sure shaders need converting to cycles-style, but if you're following PBR principles and texture authoring this is trivial to support, for the surfaces and light emissions you want to replicate. 

That is, if it's worth doing now as you've already got a nice working implementation here... I'm not too familiar what kinds of light map data you want though which work with normal maps and such in the shader at runtime, but I think you're already covering this, Sinoid?

-------------------------

sabotage3d | 2017-01-02 01:07:55 UTC | #22

So far Houdini was not very good doing Lightmapping as texture baking was only supported in micropolygon renderer mode. But know with Houdini 15 it works with PBR as well, but I think there might be still some bleeding edge issues.
Doing a lightmapper using Urho3d API is more open and I think it is quite useful for procedural games. Where Houdini API is completely closed source.

-------------------------

Hevedy | 2017-01-02 01:07:55 UTC | #23

[quote="Sinoid"][quote]I see tests of the SSGI in UE4 and give problems is like the SSR but the reflections you notice less than the light, if you add sometype of dynamic GI you got in UE4 the LPV in alpha/beta status as reference but that LPV or something like that should be better than SSGI.
*Tested in demo scenes probably in a final result game looks better without problems idk.[/quote]

Do you have a link to SSGI regarding UE4? I'm only aware of the LPV and SVOGI attempts. I would never expect screen space to be an adequate replacement, just an adequate "fill" to augment existing lightmapping or other GI approaches (ie. to mask the dynamic objects problem in a realtime lightmapping approach).
[/quote]

Well the SVOGI is dropped before the UE4 release, and the LPV are in development by a third party company creating a game with that. The only Voxel based solution now is the Nvidia one you have that in the Nvidia fork i think.
About the SSGI Epic is testing and developing different solutions to get a realtime GI solution because now UE4 don't have nothing the LPV is in alpha and is by another company and the Nvidia solution is not added, that is because they are testign with different solutions, If i found the post i send to you the link.

Not sure but i think I see that in a preview version of the DFGI [forums.unrealengine.com/showthr ... lumination](https://forums.unrealengine.com/showthread.php?68006-Guide-to-Global-Illumination)

I found the post this pic check [forums.unrealengine.com/showthr ... post187088](https://forums.unrealengine.com/showthread.php?2421-Global-Illumination-alternatives&p=187088&viewfull=1#post187088) based in screenspace give problems

-------------------------

