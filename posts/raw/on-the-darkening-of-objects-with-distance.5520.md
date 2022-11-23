qcdeml | 2019-08-28 11:21:42 UTC | #1

Why is it that the darker the distance from the camera, the less illuminated it will be for hundreds of meters? How to modify the illumination always? Thank you

-------------------------

Modanung | 2019-08-28 13:49:43 UTC | #2

Welcome to the forums! :confetti_ball: :slightly_smiling_face:

Objects fade into the fog, which is coloured black by default.  

https://urho3d.github.io/documentation/HEAD/_zones.html

-------------------------

Leith | 2019-08-29 09:34:13 UTC | #3

Welcome aboard!
Fog is provided by the Zone component, which also provides ambient lighting.
To remove fog, we can screw with the fog distance members, but typically we do want ambient lighting.

-------------------------

