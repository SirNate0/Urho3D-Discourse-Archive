artgolf1000 | 2017-01-02 01:14:07 UTC | #1

Hi,

I have exported a 3d model with blend shapes and a skeleton animation with Blender's Urho3D add-on:
body.mdl
body.ani

But I can not figure out how to use blend shapes, can somebody show me a piece of code?

Thank you.

-------------------------

codingmonkey | 2017-01-02 01:14:07 UTC | #2

Hi!
As I remember blendshapes stored in mdl binary file, That's why there is no needing in additional *.ani files to animate blandshapes.
For using morph you just need get it  or set weight from/for AnimatedModel with methods

[code]const Vector< ModelMorph > & GetMorphs () const 

unsigned 	GetNumMorphs () const
 	Return number of vertex morphs.
 
float 	GetMorphWeight (unsigned index) const
 	Return vertex morph weight by index.
 
float 	GetMorphWeight (const String &name) const
 	Return vertex morph weight by name.
 
float 	GetMorphWeight (StringHash nameHash) const
 	Return vertex morph weight by name hash. [/code]
see doc: [urho3d.github.io/documentation/ ... model.html](https://urho3d.github.io/documentation/HEAD/class_urho3_d_1_1_animated_model.html)

-------------------------

Mike | 2017-01-02 01:14:08 UTC | #3

Also check [url]http://discourse.urho3d.io/t/animation-for-morphs-file-format/628/1[/url]

-------------------------

artgolf1000 | 2017-01-02 01:14:08 UTC | #4

Thanks, I have found that 'AssetImporter' does not support exporting blend shapes at present, I guess it is a TODO work in future.

-------------------------

Lumak | 2017-07-03 17:12:42 UTC | #5

[quote]An alternative export path for Blender is to use the Urho3D add-on ([github.com/reattiva/Urho3D-Blender](https://github.com/reattiva/Urho3D-Blender)).[/quote]

edit: wow, did I even read the 1st post before writing this?! I must've been asleep when I wrote it. Pls, ignore.

-------------------------

