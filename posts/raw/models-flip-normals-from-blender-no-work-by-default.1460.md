Hevedy | 2017-01-02 01:07:51 UTC | #1

Blender Flip normals no work in Urho3D ?
If in Blender select a model and select all the faces and Flip the normals of the selected faces, at import and check the model in Urho3D editor no make changes ?

The model always have the material in the same side with flipped normals or without.

-------------------------

gabdab | 2017-01-02 01:07:51 UTC | #2

Are you using the reattiva blender exporter ?

-------------------------

friesencr | 2017-01-02 01:07:51 UTC | #3

Normals are different than the side of the material.  The 'winding' of the vertices is what determines what direction a material is.  A triangle can have 2 different ways to wind.  Clockwise and Counter Clock WIse.  There is a material parameter to switch which way is what.

-------------------------

