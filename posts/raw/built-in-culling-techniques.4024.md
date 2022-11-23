burt | 2018-02-16 22:53:56 UTC | #1

Urho seems to have built-in frustum and occlusion culling, but I couldn't find more information about culling groups or areas, like Unity's: https://docs.unity3d.com/Manual/OcclusionCulling.html

Urho treats this differently? How does it work with moving objects, such as enemies?

-------------------------

Enhex | 2018-02-18 23:55:58 UTC | #2

Here's the explanation from the documentation:
https://urho3d.github.io/documentation/HEAD/_rendering.html#Rendering_Optimizations

It works with both static and dynamic drawables, so you shouldn't worry about it.

To optimize for it try to pick big models with relatively low triangle count as occluders.

-------------------------

burt | 2018-02-18 22:08:55 UTC | #3

I didn't understand from those docs that everything was automated, both static and dynamic. Thanks a lot for the info!

-------------------------

