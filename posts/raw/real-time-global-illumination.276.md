rasteron | 2017-01-02 00:59:20 UTC | #1

The Tesseract Engine/Project, tesseract.gg (Zlib License) already has this feature, I don't see why Urho3D should be left behind. :wink:

Real Time Global Illumination

[img]http://i.imgur.com/eUW6oZE.jpg[/img]

[img]http://i.imgur.com/pt8DMqZ.jpg[/img]

-------------------------

alexrass | 2017-01-02 00:59:20 UTC | #2

[people.mpi-inf.mpg.de/~ritschel/Papers/SSDO.pdf](http://people.mpi-inf.mpg.de/~ritschel/Papers/SSDO.pdf)

-------------------------

thebluefish | 2017-01-02 00:59:34 UTC | #3

I would love to see this implemented. It appears that it can all be done through shaders using the existing pipeline, however my extreme lack of shader knowledge means it would take me more time than I've got to attempt it.

An example taken [url=http://www.garagegames.com/community/forums/viewthread/136081/1#comment-854012]from a thread over at GarageGames[/url]:
[img]http://imageshack.com/a/img706/8220/5uw.gif[/img]

-------------------------

cadaver | 2017-01-02 00:59:34 UTC | #4

I'm in a kind of same situation, being more of a general engine programmer and not a graphics specialist; learning to implement this stuff would take time I don't currently have. But yes, certainly hoping someone would have time/interest to contribute. I would think the existing rendering pipeline configurability takes one quite far, and if that's not enough, new uniforms/parameters/commands can always be added.

-------------------------

boberfly | 2017-01-02 00:59:41 UTC | #5

Hi,

When I get more time off work (or if work can grant me some dev time as it will most likely benefit them) I'd really like to implement more features like global illumination. To be honest HBAO should just compliment a better GI approach as the screen-space ones don't look too convincing. Two dynamic approaches that I really like are here:

[vis.uni-stuttgart.de/~dachsb ... ad/lpv.pdf](http://www.vis.uni-stuttgart.de/~dachsbcn/download/lpv.pdf)
Pros: It can be shoe-horned into a SM3.0 renderer like Urho3D, it just needs to render to a 3D texture and the shadow map pass needs to be a multiple render target to produce albedo+normal passes for reflective shadow maps. Particles can be lit with this and look volumetric, some kind of SSS as well. It would use a few cascaded 3D textures similar to how shadows cascade.
Cons: Specular won't work with it only single bounce diffuse. Light leaking on thin walls.

[software.intel.com/en-us/articl ... lumination](https://software.intel.com/en-us/articles/layered-reflective-shadow-maps-for-voxel-based-indirect-illumination)
Pros: Similar benefits that LPVs provide in addition glossy specular highlights can be made with it as well, and it's more accurate to LPV for single bounces.
Cons: Needs SM5.0 most likely, so Urho3D needs to support GL4/DX11. More memory hungry for the 3D occlusion texture but it should be less than the original voxel cone trace system from a year or two ago even without sparse octree'ing it.  It won't be as performant as LPV, but it would look incredible.

For reflections we could use screen-space local reflections mixed with pre-generated cube map bakes. In combo with LPVs it should look really nice and matches to how UnrealEngine4 is approaching GI as far as I know. 

Another idea I had that was inspired by Battlefield 3 and the Enlighten middle-ware was to do ray-tracing on the CPU in real-time and lazy-load updated lightmaps to the GPU. This could be done with something like Intel's Embree or Blender's Cycles so it's still performant but it would only work for diffuse (but more than 1 bounce potentially).

Cheers!
-Alex

-------------------------

lostintime | 2017-01-02 00:59:41 UTC | #6

Godot Engine (MIT License) also has GI feature. Seems like non-realtime solution, but may be useful.

[godotengine.org/forum/viewto ... ?f=7&t=665](http://www.godotengine.org/forum/viewtopic.php?f=7&t=665)
[github.com/okamstudio/godot/com ... 2182c9c6ae](https://github.com/okamstudio/godot/commit/9b8696d3dd92e2ed6f310ad0f0bf3c2182c9c6ae)

-------------------------

