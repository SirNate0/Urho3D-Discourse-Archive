deakjahn | 2018-11-27 13:32:37 UTC | #1

I'm opening a StaticModel scene from a .mdl and related files exported from Blender. The model is rotated in Blender as I want it, I made sure it's OK when in front view. When exporting, I do specifiy that the front view I want from the export plugin is the same front view as in Bender. Still, my model appears in Urho with a rotation (by the looks of it, the very original rotation I imported it first into my scene in Blender with, before I started to modify it in any way for my needs).

Yes, I could apply an initial rotation in code but I need to import a larger number of models upon user interaction, so I need to make sure each arrives with its own proper initial settings.

-------------------------

Modanung | 2018-11-27 13:47:45 UTC | #2

Least confusing is to have your objects look along the positive Y axis in Blender and select _Back_ as _Front view_ in the export options. You may also need to _Apply Rotation & Scale_ of the objects before exporting (Ctrl+A).

Also, welcome to the forums! :confetti_ball: :slightly_smiling_face:

-------------------------

deakjahn | 2018-11-27 13:40:39 UTC | #3

This Apply was the missing link, thanks, but I'll also look into the orientation you suggest.

-------------------------

