ppsychrite | 2018-01-24 17:36:56 UTC | #1

Hello! :grinning:

I've been using DiffVCol.xml for custom geometry (Using VertexBuffers and IndexBuffers) with vertex colors and abilties to set textures. It's been working fine except for one thing mostly. 

I've noticed that attempting to load a .png or any other image with a transparent background won't actually place it with the vertex color visible (Can't really explain it fully as I'm on mobile and not near my pc with dev environment set up). But if I try using a .jpg or any other image with a default white non-transparent background it works like a charm! 

While using .jpgs or adding white backgrounds seems like it solves it there has to be a much easier way of using images with transparent backgrounds. Would I have to manually load the image/texture with some params or is there any xml file values I need? (Trying to achieve something similar to the decal sample but material on an object with vertex color)

Many thanks! (Once I get back on my pc I'll try posting and example of what happens with transparent backgrounds)

-------------------------

SirNate0 | 2018-01-25 00:50:47 UTC | #2

I'm not at my computer either right more, but is there a DiffVColAlpha.xml or the like? Or, if the white backgrounds are fine, you could probably write a script to do it with Image Magic(k?) or the like (there might be a way to do it in Urho as well, I'm not sure... If all else fails, render to texture with a white clear color just rendering the image with the transparency, and then saving that image to use).

-------------------------

ppsychrite | 2018-01-25 01:54:23 UTC | #3

Don't see any DiffVColAlpha in Techniques, although there's DiffVColAddAlpha (I can try and test around by trying to randomly swap stuff in the .xml) :sweat_smile:

If not then what you're talking about will have to do, thanks!

-------------------------

Sinoid | 2018-01-25 02:59:27 UTC | #4

    <technique vs="LitSolid" ps="LitSolid" vsdefines="VERTEXCOLOR" psdefines="DIFFMAP VERTEXCOLOR">
        <pass name="alpha" depthwrite="false" blend="alpha" />
        <pass name="litalpha" depthwrite="false" blend="addalpha" />
        <pass name="shadow" vs="Shadow" ps="Shadow" />
    </technique>

Should do it for a DiffVColAlpha technique.

-------------------------

ppsychrite | 2018-01-25 12:57:04 UTC | #5

Does the same thing as the default DiffVCol.xml does. :confused: 

(Texture shows but it's see through and vertex color doesn't appear for .pngs with transparent backgrounds)
Going to attempt and adding more passes and see if I'm able to achieve anything

-------------------------

