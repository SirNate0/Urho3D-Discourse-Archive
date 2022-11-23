hunkalloc | 2022-07-01 22:10:21 UTC | #1

Is it possible to use HDR skies in Urho? Is there a way to get those skydomes into the engine? Or do I have to convert them to cubemap faces? If so, what is the correct cubemap format to use?

https://polyhaven.com/hdris

-------------------------

SirNate0 | 2022-07-02 02:10:20 UTC | #2

Pretty sure you would have to convert it to cubemap faces to do it. You can see the skybox texture in the samples as an example of how to set up the loading (it involves adding an XML file specifying the faces). I think something like this will handle the conversion for you, though I've not tried it myself.

https://matheowis.github.io/HDRI-to-CubeMap/

Though perhaps someone will explain that I'm wrong and Urho does support the exr format directly for the texture. Or something simpler than creating 6 image files.

-------------------------

