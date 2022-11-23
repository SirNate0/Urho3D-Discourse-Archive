felipeac | 2017-01-02 01:12:44 UTC | #1

I'm new to Urho3D and just got started with materials. I just wanted to write a simple shader, but it seems like you have to create a material, a technique and the shader itself. Do you have to do that for each different thing in the scene or is there a faster way of doing that? Is there a way to export a model from blender with a glow shader or something like that?

-------------------------

rasteron | 2017-01-02 01:12:45 UTC | #2

Hey felipeac,

Yes, apparently that's the case, at least with the current Blender Exporter. With the shaders you have to convert it to Urho3D implementation which is not that different with Blender or Standard GLSL stuff.

To give you some reference, there's already a glow material shader and other material shaders buried somewhere in this forum, just try a google or advanced search.

Good luck!  :slight_smile:

-------------------------

felipeac | 2017-01-02 01:12:45 UTC | #3

Hey, how do you use multiple techniques in one material? I haven't been able to find that anywhere and I tried basically duplicating the Diff.xml technique and added a simple fading effect to it, however it doesn't seem to work if I pass the technique to the material, as it only uses the first one I passed, not the second.

EDIT: nevermind that last question, is there shader inheritance? I just want to add an effect to an existing shader, do I have to clone it?

-------------------------

hdunderscore | 2017-01-02 01:12:46 UTC | #4

If you just want to extend existing shaders, that's much easier. You can add your own changes to the shader source, and then you could #ifdef those changes. Then you make a copy of a technique, and in the vsdefines/psdefines you add the extra definition. In that way, only materials that use the new technique will show that extra effect.

-------------------------

cadaver | 2017-01-02 01:12:46 UTC | #5

Multiple techniques in materials are meant for quality levels (either the Material Quality option, or distance LOD). Only one will be used at a time.

Check the bin/Data/Materials/Stone.xml for a material which is diffuse only on Low quality and normalmapped on higher qualities.

-------------------------

felipeac | 2017-01-02 01:12:46 UTC | #6

Alright, thanks!

-------------------------

