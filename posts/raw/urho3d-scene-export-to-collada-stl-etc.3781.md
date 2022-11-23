DavidHT | 2017-11-25 11:37:56 UTC | #1

Hi all. I'm making the jump from Irrlicht to Urho3D. So far it's wonderful, and I'm very impressed with the library.

In my application, I need to be able to export the data currently in my 'Scene' to external formats such as Collada, STL, etc.

In Irrlicht, there are export functions for this, but it seems there's no such thing in Urho3D.
I've studied the AssetImporter, but that's the wrong way around.

Has anyone done this before, or are there any hints you could provide?

-------------------------

Eugene | 2017-11-25 13:28:24 UTC | #2

[quote="DavidHT, post:1, topic:3781"]
Has anyone done this before, or are there any hints you could provide?
[/quote]

There is Export to OBJ. However, Scene is a bit too complex for 1-to-1 exporing it to Collada or any other 3D format.
Writing true exporter would require huge amount of effort.
I wonder why do you ever need it at all. If your pipeline requires conversion some assets there and back, it's better to change such pipeline.

-------------------------

DavidHT | 2017-11-25 13:46:30 UTC | #3

Hi Eugene, thanks for the quick reply.

I need it because my application is a design program with 3D options. So once people are done, they'd like to export the design to process it further in Sketchup or other 3D tools.
Some want the result to be 3D printed.

Of course there are other routes to do this, but as Irrlicht had it, I hoped Urho3D would have a similar functionality.

This export to OBJ, is this the Wavefront obj format? Perhaps I can combine this with Assimp to go to the other formats.

-------------------------

Eugene | 2017-11-25 14:01:39 UTC | #4

The question is: how much information do you want to export? Do you have fixed geometry format?
It's not very hard to write exporter for some specific case.

-------------------------

DavidHT | 2017-11-25 14:46:30 UTC | #5

I want to export the meshes, and perhaps the materials and the lights. It's all fixed, so no animations etc.

The required formats are at least stl, dae, ply and obj. Perhaps more. So I preferably go to Assimp first, so, if I understand correctly, an 'aiScene', and export from there if that's possible at all.

-------------------------

Eugene | 2017-11-25 15:06:41 UTC | #6

[quote="DavidHT, post:5, topic:3781"]
I want to export the meshes
[/quote]

So much things are hidden under these words...
If you want to export simple position+texture+normal models, it's one thing.
If you want to export _arbitrary_ meshes, it's another.

[quote="DavidHT, post:5, topic:3781"]
So I preferably go to Assimp first
[/quote]
That's the best way, I suppose. Construct `aiScene` and export things via AssImp.
Never tried AssImp exporter on myself tho.

-------------------------

DavidHT | 2017-11-25 15:22:49 UTC | #7

What do you mean by arbitrary meshes?

In my case, the meshes are created from within my application, so they're dynamically built.

I'll study the AssImp exporter a but further. Thanks.

-------------------------

Eugene | 2017-11-25 15:49:25 UTC | #8

[quote="DavidHT, post:7, topic:3781"]
What do you mean by arbitrary meshes?
[/quote]
I mean that _mesh_ is just a container. So it could store literally anything as long as you have shader that could process it. If you have fixed set of vertex formats, exporting is fine.
If you have arbitrary format of vertex data, you are in troubles.

-------------------------

DavidHT | 2017-11-25 16:06:42 UTC | #9

At the moment, I'm using the mesh generator described here by Victor:
https://discourse.urho3d.io/t/a-mesh-generator/2361/5

-------------------------

