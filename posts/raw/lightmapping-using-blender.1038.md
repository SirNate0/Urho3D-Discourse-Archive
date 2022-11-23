Enhex | 2017-01-02 01:04:59 UTC | #1

I want to use Blender to bake a lightmap for static geometry in the scene and I have few questions about how to implement it.

Blender part:
- Set the ambient light to 0,0,0 (world surface color with cycles)
- import the static geometry and give it a flat material with the color 0.5,0.5,0.5
- Import light sources
- Perform combined bake to a UV texture

This way we should get a lightmap which contains only lights/shadows, without diffuse.
Then the lightmap should be multiplied with the diffuse map when rendering.

My question is how to add the lightmap in Urho?
Should I programmically add a pass to existing materials?
Perhaps a new technique?
I didn't use these things with Urho before.

-------------------------

Bananaft | 2017-01-02 01:04:59 UTC | #2

There are already techniques DiffLightMap.xml and DiffLightMapAlpha.xml.

according to shader code:
[code] #ifdef LIGHTMAP
            finalColor += tex2D(sEmissiveMap, iTexCoord2).rgb * diffColor.rgb;[/code]

Lightmap goes to emissive slot, and mesh should have second UV layer.

-------------------------

boberfly | 2017-01-02 01:04:59 UTC | #3

This reminds me of that one project where I want to get cycles standalone and make it output baked data only. Possibly hijack its xml-api to accept Urho3D scenes and .mdl files and materials instead. Also make it run as a subprocess from the Urho3D editor and get it to periodically write to a texture and get Urho3D's file watcher to progressively load it in...

-------------------------

Enhex | 2017-01-02 01:04:59 UTC | #4

[quote="Bananaft"]There are already techniques DiffLightMap.xml and DiffLightMapAlpha.xml.

according to shader code:
[code] #ifdef LIGHTMAP
            finalColor += tex2D(sEmissiveMap, iTexCoord2).rgb * diffColor.rgb;[/code]

Lightmap goes to emissive slot, and mesh should have second UV layer.[/quote]

Can anyone give an example and explain how to use it? (couldn't find any)
I can set the emissive slot with Material::SetTexture() right?
How do I set a second UV layer? Can it be done with a CustomGeometry? Does it require just calling DefineTexCoord() twice?

Oh and to add normal/specular maps will require new techniques?

-------------------------

Bananaft | 2017-01-02 01:05:00 UTC | #5

[quote="Enhex"]I can set the emissive slot with Material::SetTexture() right?[/quote]
Or set it up in Editor, or edit material .xml .

[quote="Enhex"]How do I set a second UV layer? [/quote]
In blender. Right there:
[img]http://i.imgur.com/yQHKgAn.png[/img]

[quote="Enhex"]Oh and to add normal/specular maps will require new techniques?[/quote]
I guess so, but normal mapping and specular will be visible only under dynamic lights. And will heve no effect with baked lighting.

Valve invented some crazy tech to make normal mapping work with lightmaps.
[www2.ati.com/developer/gdc/d3dtu ... hading.pdf](http://www2.ati.com/developer/gdc/d3dtutorial10_half-life2_shading.pdf)

-------------------------

Enhex | 2017-01-02 01:05:00 UTC | #6

I just checked Urho's source and it seems CustomGeometry doesn't support second texture coordinates.

I guess that it means that I must construct the custom geometry in Blender and export it as a model?


Also materials need to be changed dynamically so they can be used for any level. Otherwise you'd have to duplicate all the materials for every level just to change the lightmap name.

-------------------------

Dave82 | 2017-01-02 01:05:06 UTC | #7

I'm also curious about this.Couldn't find any tutorials and there's no info in the documentation on how to define 2 uv sets per vertex.If someone could explain how to create VertexBuffer with 2 uv sets would be really nice.

-------------------------

friesencr | 2017-01-02 01:05:06 UTC | #8

On the Geometry model you can set the elements. The customer geometry examples shows how to do it.

[github.com/urho3d/Urho3D/blob/m ... y.cpp#L225](https://github.com/urho3d/Urho3D/blob/master/Source/Samples/34_DynamicGeometry/DynamicGeometry.cpp#L225)

Be sure to set the appropriate mask MASK_TEXCOORD2

-------------------------

Hevedy | 2017-01-02 01:05:09 UTC | #9

Interesting thread, and how manage the lightmaps ? you need to divide in many textures and manage the loads of each one.
Will be nice to see in Urho3D support to bake the light and use static lights + dynamics or something to bake the scene in Blender and then the engine manage all.

-------------------------

globus | 2017-01-02 01:05:10 UTC | #10

I think, Urho3D needed full support Shadowmapping
The target of this metod is [u]Optimization[/u] for performance.

Calculate shadows in real time is hard for devices.
FPS drop down.

But, precalculated in any 3D editor shadows may be
very best (than realtime shadows)

Good way is use shadowmap for all static objects
and realtime shadows for dinamic objects.

But, some static objects also needed drop shadows on dinamic objects.
In this case, level developer needed set flags for scene objects 
(object can take or drop shadows on\form dinamic\static objects.
Select objects\lights by type or directly)

Also, you can use low poly invisible model for calculating shadows
(may be LOD model).

If you don't have plan use changes of shadows from level to level,
in this case you don't need 2 UV and baking shadows directly to texture. 

Sorry, it's just a thought.

-------------------------

rasteron | 2017-01-02 01:05:10 UTC | #11

[quote="globus"]I think, Urho3D needed full support Shadowmapping
The target of this metod is [u]Optimization[/u] for performance.

Calculate shadows in real time is hard for devices.
FPS drop down.

But, precalculated in any 3D editor shadows may be
very best (than realtime shadows)

Good way is use shadowmap for all static objects
and realtime shadows for dinamic objects.

But, some static objects also needed drop shadows on dinamic objects.
In this case, level developer needed set flags for scene objects 
(object can take or drop shadows on\form dinamic\static objects.
Select objects\lights by type or directly)

Also, you can use low poly invisible model for calculating shadows
(may be LOD model).

If you don't have plan use changes of shadows from level to level,
in this case you don't need 2 UV and baking shadows directly to texture. 

Sorry, it's just a thought.[/quote]



I think this is a good idea but not particular in Blender of course, as there are many tools out there that are better or on par with Blender.

+1000000 for the dynamic shadowmapping mixed with lightmaps (shader) or the latter bake to texture option, I think this should be the next step for Urho3D to at least stay updated with current game engines, particularly the engine being cross-platform and on mobile where memory and resources needs to be optimized and at the same time not sacrificing visual quality.

-------------------------

cadaver | 2017-01-02 01:05:10 UTC | #12

If you feed Urho the right kind of content and shaders, it should already be possible to mix lightmaps and dynamic lights. The question is who will step up and actually write the content processor tool-pipeline (+ the shaders), that will produce the required data from e.g. a scene made with Blender, so that everything works right.

-------------------------

friesencr | 2017-01-02 01:05:10 UTC | #13

I had looked into this.  I got stopped because it needs a something to procedurally generate unwrap and make uv sets for arbitrary models.  I didn't find a sensible open source library that worked cross platform.  An stb style uv unwrapping library would be very nice.

-------------------------

globus | 2017-01-02 01:05:10 UTC | #14

[quote="cadaver"]If you feed Urho the right kind of content and shaders, it should already be possible to mix lightmaps and dynamic lights. The question is who will step up and actually write the content processor tool-pipeline (+ the shaders), that will produce the required data from e.g. a scene made with Blender, so that everything works right.[/quote]

I am long ... long time do not use Urho3D and editor.
Only latest time i returned to this.

If is available, load model from any 3D editor with 2 UV maps 
and select in editor shadowmap image - it was be perfectly and enough.
Only one problem (time for) - all models with shadowmap needed positioning in 3D editor
before backing shadow and next step repeat this positions in Urho3D scene editor.

I not know, if it good idea for available Urho3D do backing shadows by himself.
I think, 3D editor do it better.
But may be scene exporter - importer is good way.
(but it individually for different editors)

-------------------------

globus | 2018-02-18 18:06:51 UTC | #15

You can look to:
[img]http://www.paulnettle.com/fsrad.png[/img]
[b]FSRad[/b] is a radiosity processor specialized for lightmap generation.
[url]http://www.paulnettle.com/[/url]
Small source code ~900kb
But it not free licence.

[details="Licence"]
Everything you see in this distribution is Copyright 2001, Paul Nettle and Fluid Studios.
All rights are reserved.

This software is free for private and personal use. Use at your own risk, Yadda Yadda.

This software is NOT free for commercial use. If you use it, you must pay for it with
credit (i.e. credit to the author in your readme file or someplace.) Also, please send
an email to me at: [midnight@FluidStudios.com](mailto:midnight@FluidStudios.com) so I can track the software's usage.

Further copyright information will be found in all the source files.
[/details]
Also, exist Ogre3D addon named OGRE FSRad
[url]http://www.ogre3d.org/tikiwiki/OGRE+FSRad[/url]

Also:
Lightmapping turorial (OpenGL)
[url]http://www.alsprogrammingresource.com/lightmapping_tutorial.html[/url]
Tutorial - Dynamic Lightmaps in OpenGL
[url]http://joshbeam.com/articles/dynamic_lightmaps_in_opengl/[/url]

===============================================

But, in Blender 3D i can backing shadows and lights 
using sophisticated algorithms rendering programs.
the only problem is that when the position of objects or light sources 
in Urho3D will need to do again bake in Blender 3D.

-------------------------

cadaver | 2017-01-02 01:05:12 UTC | #16

Very nice!

-------------------------

rasteron | 2017-01-02 01:05:13 UTC | #17

This is awesome Sinoid!

-------------------------

