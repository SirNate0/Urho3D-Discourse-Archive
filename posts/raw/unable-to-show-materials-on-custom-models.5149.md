urnenfeld | 2019-05-15 20:25:54 UTC | #1

Hello,

This is going to be a very noob question. I am probably missing a concept.

So I have a room, created by very thin boxes:

![Screenshot_20190515_193315|660x500,50%](upload://nSFhDbjTMY38gOLnXj7SN3UdZQl.png) 

I play changing the materials that are already provided by the engine, all ok. Then I try to model(blender) a ship-like door, export the mdl file and the materials are not showing as *expected*. As you can see the front wall is full grey while the materials in side walls are correctly showing the stone material. I have to point that some of the faces of the object looks to render the material.

In my research I understood that I would need to take care of the UV mapping and the normals of the faces, which I think I did:

![Screenshot_20190515_193846|690x390](upload://hYcSFXKlkMhyb1hah9V1TT6plvA.png) 

What else am I also missing?

-------------------------

Modanung | 2019-05-15 20:22:44 UTC | #2

Did you enable exporting of UVs (and tangents if you'll be using a normal map) in the export options?
_Are_ you using the Blender [add-on](https://github.com/reattiva/Urho3D-Blender) to export your model, btw?

-------------------------

urnenfeld | 2019-05-15 20:24:22 UTC | #3

Yes I am using this plugin. But as you said all problem was a single checkbox... Thanks a lot @Modanung !

-------------------------

