najak3d | 2020-04-21 19:29:51 UTC | #1

We're planning to port a production application to UrhoSharp (it does work), but need to validate that it can do the following:

1. Anti-aliased Lines (not the post-processing effect, but actual lines drawn anti-aliased to begin by having alpha drop off as the fragment shader moves further from the center line.  These lines will be drawing Map Vector data (e.g. roads, rivers, state lines, and Route line.  Current implementation we have has jagged/pixel-ated edges.   We want smoothed edges.

2. Text in 3D space, with Outlines - various sizes.   We label stuff on the map, and need outlines to ensure the text is readable and easily visible (e.g. white inner stroke with black outline, etc).  Current implementation does not have outlines.  We need outlines.


If someone has either of these working for standard Urho3D (not Sharp), we could then port it to run with UrhoSharp.   I haven't seen any example code that does this yet.

-------------------------

SirNate0 | 2020-04-21 21:30:35 UTC | #2

For 1, do you need to be able to take an arbitrary model and use some material on it to get antialiased lines or are you fine with preprocessing the models (possibly live in Urho) before they're sent to the GPU? If that is fine (and no one else has an implementation) I believe the approach described in this article should be doable in Urho (without attempting to add a tesselation shader stage or anything).
https://blog.mapbox.com/drawing-antialiased-lines-with-opengl-8766f34192dc

For 2, someone seems to have had Text3D with outlines:
https://discourse.urho3d.io/t/signed-distance-field-text-rendering-for-text3d/367/7?u=sirnate0

-------------------------

najak3d | 2020-04-21 22:13:09 UTC | #3

Thanks SirNate0.   I have seen and love the link you showed. 

My issue is that I don't know how to create a shader that paints onto geometry that doesn't really exist.  In this link, it's as though our vertex data is just a line -- but the shader itself knows how to "add thickness" to this line.  Once I know how to do that, writing the fragment shader is easy -- you just use math that knows the "Distance From Center Line" .. and use exponent math to decimate alpha at the edges.

But the only thing I know right now is how to write those shaders for actual triangles, which means i have to tesselate my line manually into actual triangles with UV coords, and then use the UV coordinates to do the alpha decimation logic.    I could make this work, but it's not the "way to do it" nowadays. 

I want to know how to make it so that I only feed in an array of Line Points to the shader, and have it create the thickness on the GPU in the shader.

Any ideas?

-------------------------

SirNate0 | 2020-04-22 00:11:58 UTC | #4

I think the "way to do it nowadays," as you say, would be with geometry shaders. I think @Sinoid may have gotten those working at one point, but I'm not certain what happened with that.

-------------------------

najak3d | 2020-04-22 00:53:05 UTC | #5

Yes, I think geometry shades might be the way to do this.   I'm not aware of how to do it otherwise.  I figured some techniques similar to those that cause a shroud/halo effect (which extends beyond edge of the geometry) might also work.

-------------------------

SirNate0 | 2020-04-24 04:36:39 UTC | #6

I'm pretty sure those halo type effects are typically created using a postprocessing effect or by rendering the model twice or (if the shroud doesn't have to match the geometry closely) through particle effects. (But again, I am not an expert)

If that is the case, though, that's a lot more similar to the idea of duplicating the line vertices, though I imagine other engines do use geometry shaders for that sort of thing as well.

---
Also, it's not outlined text, but if you hadn't seen it I thought you might find the curved text someone worked on interesting. The photos no longer work, but you should be able to get the idea pretty easily, and the code seems to only need a few updates.
https://discourse.urho3d.io/t/curved-text/2034

-------------------------

