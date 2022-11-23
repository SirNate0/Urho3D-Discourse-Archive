codexhound | 2019-08-08 02:19:45 UTC | #1

Is there any way to make billboards show up even at far distances from the camera? I want to make them show even at great distances.

-------------------------

Leith | 2019-08-08 08:53:28 UTC | #2

The only limit is the camera far plane distance - see Camera class :)

-------------------------

Modanung | 2019-08-08 16:57:15 UTC | #3

Indeed `Camera::SetFarClip(float)` seems to be what you're looking for.

-------------------------

Leith | 2019-08-09 07:06:28 UTC | #4

Be warned that setting the far clip plane too far will reduce the engine's ability to cull renderables, without additional clues from you - and I mean "occluders" and "occludees". There's a penalty for just making the far clip plane massive, you now need to help the system to reject what is not visible...
If you have some big chunky things in your scene that are likely to block the view of other things, mark them as occluders. And if your scene has none, consider adding some.

-------------------------

codexhound | 2019-08-09 09:07:11 UTC | #5

I started using the SetDrawableDistance property on components and nodes I need to have control over. I think that is a better solution than making the engine render everything. And if that doesn't work for you,  save the component somewhere and just disable it on it's update when necessary.

-------------------------

