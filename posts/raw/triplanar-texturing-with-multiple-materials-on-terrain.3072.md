darkirk | 2017-04-29 14:07:15 UTC | #1

The default terrain in Urho does not support triplanar texturing or full fledged material layers (diffuse + normal + specular + parallax or tesselation). Is there a third-party implementation of this that we can buy? Like an addon?

-------------------------

1vanK | 2017-04-29 14:05:19 UTC | #2

 http://urho3d.wikia.com/wiki/Tri-Planar_Texturing
 https://urho3d.prophpbb.com/topic322.html

-------------------------

darkirk | 2017-04-29 14:07:32 UTC | #3

Yes, i've come across that implementation. But it seems incomplete. There's no support for normal or specular flows, no parallax or tesselation.

-------------------------

jmiller | 2017-05-06 10:09:55 UTC | #4

I have used these before, maybe they can be useful, though I have not used specular on Terrain yet.

Nice displacement mapping with options:
https://discourse.urho3d.io/t/parallax-mapping-opengl-only-for-now/1158

https://github.com/AlexTank/UrhoTriPlanarTerrain

https://discourse.urho3d.io/t/terrain-editor/765

The Terrain API provides a few methods to control detail levels, but not driver tesselation (supported in OpenGL 4.x and D3D11 and would need to be written).

-------------------------

jmiller | 2017-05-09 03:12:40 UTC | #5

Another related article that might help (desktop, glsl)
http://urho3d.wikia.com/wiki/Terrain_Shader_with_normal,_specular_and_height_mapping

-------------------------

