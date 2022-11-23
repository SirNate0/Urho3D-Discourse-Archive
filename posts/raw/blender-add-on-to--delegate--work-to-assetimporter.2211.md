Ray_Koopa | 2017-01-02 01:13:57 UTC | #1

There's a Blender add-on which is "really buggy" according to the author, and it tries to reimplement direct conversion of model data into Urho3D formats.

Why is there no Blender add-on simply delegating exports to the AssetImporter tool, calling it with the right parameters?
Even while this creates a dependency on the tool, this might be an advantage to have the same code doing the same stuff.

If anyone is interested, I can write it, having written several Blender add-ons in the past. I'd probably do that sooner or later because it speeds up the workflow a lot for me.

-------------------------

1vanK | 2017-01-02 01:13:57 UTC | #2

Blender exporter has many more features than AssetImporter

-------------------------

ghidra | 2017-01-02 01:13:58 UTC | #3

For me, I have even had more success with the blender plug in that using the asset importer. But that might be more an issue of the user and not the software. I assumed that there were more features in the exporter for blender but i wouldnt be able to list them.

However, I would be interested to see something you are talking about. If only so I can learn to be less dependant on the plug-in.

-------------------------

Mike | 2017-01-02 01:13:58 UTC | #4

I agree with 1vanK, Blender add-on:
- has many more features than AssetImporter
- has logging and debugging capabilities (with faulty vertices selection) that in themselves are invaluable
- although reattiva claims that it has "big bugs, use at your own risk", it is now fully mature and stable
- is easy to modify to suit your own needs
- you can tightly intertween it with other add-ons to enhance your workflow
- you can control everything at export
- and Blender format is not well supported by Assimp (at least at the time when the add-on was written)

There certainly would be some benefits in transfering some tasks to AssimpImporter, especially speed, while preserving the above benefits, however this would require a lot of modifications on the AssetImporter side to deal with the many new parameters.

-------------------------

