akilarandil | 2017-05-24 09:38:04 UTC | #1

Hi all,

Is there anyway, or any sort of techniques to make a human model more realistic in urho 3d?

-------------------------

johnnycable | 2017-05-24 12:49:17 UTC | #2

Normally "realistic" in 3d means an higher vertex count... better morphings... is that what you want?

-------------------------

smellymumbler | 2017-05-24 18:33:29 UTC | #3

Maybe you mean subsurface scattering material for skin?

-------------------------

S.L.C | 2017-05-24 19:34:07 UTC | #4

What kind of realism? Graphics, animation, behavior (IK?) ?

Graphically, do you mean applying things like normal maps to kinda fake high vertex count?
Animation, do you mean smooth animation blending when you control the character?
Behavior, do you mean to sometimes break from the animation to adapt to certain situations?

The question is very ambiguous to give a proper answer.

-------------------------

slapin | 2017-05-24 19:57:20 UTC | #5

For me that would mean moar bones per mesh. So I think you'd better be more precise with what you want...

-------------------------

rasteron | 2017-05-24 23:55:46 UTC | #6

If you're talking about graphics, I think just the right shaders (SSS and probably some GI or PBR) and a detailed model will produce realistic results.

-------------------------

