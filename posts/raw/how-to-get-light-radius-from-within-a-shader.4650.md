urho3d_game_dev | 2018-11-05 22:22:23 UTC | #1

Hi all,

I am writing my own shader, I would have in a scene hundreds of lights, which can be contained in a bounding boxes ( such as point lights ).

When the object is going to be rendered, I would like to know the radius of the light.

I could not see anything about it, and I check the file of "Uniforms.glsl", nothing is mentioned about light radius.

Could you please give me some feedback about this.

-------------------------

Sinoid | 2018-11-05 22:52:51 UTC | #2

`cLightPosPS` contains the inverse of the range in the `W` component, you'll have to un-invert it yourself `(1.0 / cLightPosPS.w)`.

-------------------------

