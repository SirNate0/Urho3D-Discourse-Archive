zedraken | 2017-07-28 05:53:01 UTC | #1

Hi folks,

I am currently using Blender to create a simple model for which I apply a texture (it is a single image representing a metal floor). Still under Blender, I play with the "Image Mapping->Repeat" parameters to have my texture repeated several times over both X and Y directions.
This appears fine in Blender when I render it.
Then, I export to Urho3D using the Urho3D exporter which also works fine. I get no errors and the texture is exported along with the material.

Here is the content of my material XML file that references the texture to be used.

    <material>
        <technique name="Techniques/Diff.xml"/>
        <texture name="Textures/MetalFloorsBare0049.jpg" unit="diffuse"/>
        <parameter name="MatDiffColor" value="0.0564704 0.0564704 0.0564704 1"/>
        <parameter name="MatSpecColor" value="0 0 0 250"/>
    </material>

It clearly appears that there are no "tiling" or "repeating" information coming from Blender. When I run my Urho3D app that displays the model, the texture is not repeated.
In such a case, I assume that it is useless to try to configure texture repetition in Blender since it is not exported. Is my assumption correct ?

In any cases, how can I proceed to be able to get a texture repetition in my XML file ? Or do I have to do thing in another way ? 

Thanks a lot for your answers !

Charles

-------------------------

Alex-Doc | 2017-07-29 09:05:14 UTC | #2

Hi, your assumption is right, the blender exporter doesn't seems to be exporting the UV offset:

It's not really intuitive to find but see how it works in [StoneTiled.xml](https://github.com/urho3d/Urho3D/blob/master/bin/Data/Materials/StoneTiled.xml)

[code]
    <parameter name="UOffset" value="4 0 0 0" />
    <parameter name="VOffset" value="0 4 0 0" />
[/code]

Where "4" is the tiling scale.

By setting those two parameters in your material, you should be able to get the tiling. 

I hope this helps!

-------------------------

Mike | 2017-07-29 09:05:14 UTC | #3

Although 'Image Mapping->Repeat', 'Mapping->Offset' and 'Mapping->Size' support could be easily added to the exporter, they have several drawbacks:
- they don't appear in the 3D viewport (you have to render the scene for them to show up)
- 'Repeat' only supports integer values, which means the texture aspect ratio is not preserved
- 'Offset' and 'Size' are a bit tough to tweak (especially since you have to render to see the changes)

For these reasons, I'd recommend to scale and translate your UVs in the UV/Image Editor instead.

-------------------------

zedraken | 2017-07-29 09:05:09 UTC | #4

Thanks for your answers.
For the moment, I overscaled my UVs in Blender and kept repetition parameters to 1 (as Mike suggested). However, I will also give a try to the solution given by Alex-Doc.
Thank you again for your help !

-------------------------

stark7 | 2017-11-08 00:55:42 UTC | #5

Is there a way to repeat the texture for a scaling model instead of having the texture stretched?

-------------------------

Don | 2017-11-08 05:16:44 UTC | #6

If you are talking about having a model automatically repeat a texture as it is scaled during runtime, I don't know if there is currently a way to do this in engine. With that said, if the scalings are predetermined before runtime, you could adjust the UV mappings in Blender. Otherwise, a runtime effect for tiling could be done without too much trouble in shaders. Hope this helps.

-------------------------

Eugene | 2017-11-08 07:05:40 UTC | #7

Custom shader could solve such problem.
Well, custom shader could solve almost everything...

-------------------------

stark7 | 2017-11-08 14:34:52 UTC | #8

So maybe like the UV coords will be scaled by 1f/model.scale ? I don't even need to dynamically change - I just want to set up a road plane and then repeat the road texture instead of stretching it no matter how "long" the road section is.

I don't actually know how to write such a shader - but when I do, that's where I'll start. I'm currently going through the edx class on shader(s). It'll take a while..

-------------------------

Eugene | 2017-11-08 15:19:12 UTC | #9

The simplest way is to use world-space corrdinates for texture sampling. Maybe a kind of triplanar mapping if you want non-flat object.

-------------------------

