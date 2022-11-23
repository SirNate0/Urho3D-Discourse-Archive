gawag | 2017-01-02 01:10:53 UTC | #1

I read about this again in [github.com/urho3d/Urho3D/issues/1231](https://github.com/urho3d/Urho3D/issues/1231).
Could texture arrays be implemented and only be available for DX11 and the others that support it (via defines)? It's a pretty important feature, especially for terrain, and not having it on DX9, ancient OpenGL and the others may not be important for the applications case.
I had used a pretty dirty and slow trick to get four textures into one image to get more terrain textures before:
[urho3d.wikia.com/wiki/Quad_Textures](http://urho3d.wikia.com/wiki/Quad_Textures)
[urho3d.wikia.com/wiki/Terrain_Sh ... ht_mapping](http://urho3d.wikia.com/wiki/Terrain_Shader_with_normal,_specular_and_height_mapping)
It had an performance and quality impact due to the weird pixel reading.

-------------------------

cadaver | 2017-01-02 01:10:53 UTC | #2

Has been recorded to the issue tracker.

-------------------------

dragonCASTjosh | 2017-01-02 01:10:54 UTC | #3

I may look into it as part of the PBR implementation

-------------------------

gawag | 2017-01-02 01:10:54 UTC | #4

Yay! :smiley:
Wasn't sure if it was a good idea or even possible so I asked here instead of making a feature request directly.

-------------------------

