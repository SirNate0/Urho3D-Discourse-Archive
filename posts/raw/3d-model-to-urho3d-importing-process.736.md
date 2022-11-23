devrich | 2017-01-02 01:02:33 UTC | #1

Hi,

Sorry if this has been answered before but searching for "modeling" or "software model" didn't turn up anything from what I read over..

Here is the pipeline I have used for years with other engines:

Using FBX, MS3D, B3D, DAE, BHV file formats for my animations and models:
1: get/create animations and/or create from scratch 3d models in fragMotion
2: export from fragmotion to ultimate unwrap3d pro ( using ms3d or b3d format )
3: setup my textures exactly the way I like
4: export in .FBX or .DAE format from unwrap3d
5: use other engine's "importing/converting programs" to import and convert to the file from .FBX to other format for the engine to use

How to get models ( and/or .BVH animations ) imported/converted to Urho3D ?


p.s.
I am looking for a good affordable 3D Modeling program for linux/ubuntu that isn't "blender", no offense to blender but i prefer another software for now.
I've been considering AC3D but never used it before... I wish I could afford Maya but budgets, you know..

Any one have any ideas or suggestions, i would be most grateful  :smiley:


[b][i]Edit:[/i][/b]  Ok I got half my question found at [url]http://urho3d.github.io/documentation/1.32/_editor_instructions.html[/url] at the bottom:
"Importing -- model import will take everything in the source file (for example a Collada scene), and combine it into a single model, with possibly many subgeometries."
"When a model is imported, it will also be instantiated into the scene as a new scene node with a StaticModel component."
"To do the actual importing, the editor will invoke AssetImporter "

""AssetImporter"" -- Is there some documentation somewhere that expains this program and it's command line arguments or etc?

-------------------------

weitjong | 2017-01-02 01:02:34 UTC | #2

[quote="devrich"]""AssetImporter"" -- Is there some documentation somewhere that expains this program and it's command line arguments or etc?[/quote]
It is in the "Tools" page. [urho3d.github.io/documentation/1.32/_tools.html](http://urho3d.github.io/documentation/1.32/_tools.html)

-------------------------

devrich | 2017-01-02 01:02:35 UTC | #3

[quote="weitjong"][quote="devrich"]""AssetImporter"" -- Is there some documentation somewhere that expains this program and it's command line arguments or etc?[/quote]
It is in the "Tools" page. [urho3d.github.io/documentation/1.32/_tools.html](http://urho3d.github.io/documentation/1.32/_tools.html)[/quote]

Thanks man!  :smiley:

-------------------------

