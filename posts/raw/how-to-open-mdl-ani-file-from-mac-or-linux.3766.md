Taymindis | 2017-11-21 23:47:00 UTC | #1

I am newbie in game development. What kind of application can open these file type? Is these file type only for 3D ? What about 2D?

-------------------------

johnnycable | 2017-11-21 08:49:05 UTC | #2

mdl is a 3d model. It could work for 2d (if it's flat like a plane a simulate a sprite). But I think it's not your goal. Ani files are animation for 3d model. Yet it's not 2d. Those two can be opened in Urho3d editor.
If you are interested in 2d workflow it's better you start checking with 24_Urho2dSprite sample and read urho2d docs [here](https://urho3d.github.io/documentation/1.7/_urho2_d.html)

-------------------------

Eugene | 2017-11-21 08:50:16 UTC | #3

[quote="Taymindis, post:1, topic:3766"]
What kind of application can open these file type?
[/quote]
Urho Player. These formats are internal for the engine.

Note that there is internal `Urho3D::WriteDrawablesToOBJ` function to convert MDL models info common OBJ format.

-------------------------

johnnycable | 2017-11-21 08:55:52 UTC | #4

...and if you convert to .obj, you can simply see them with quicklook on Os X (CMD-Y)

-------------------------

