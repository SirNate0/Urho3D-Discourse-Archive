slapin | 2017-06-03 01:50:42 UTC | #1

Hi, all!

To be more realistic I need to implement glass for car windows and building windows.
How would you do that? I think that having thousands of objects with transparency would heavily impact
rendering performance, but GTAIII does it and it looks great. How can I achieve the same level of quality
and not degrade performance too much?

-------------------------

Don | 2017-06-03 20:32:42 UTC | #2

I'm not too familiar with GTA III or Urho for that matter, but this is what it looks like to me, based on some screenshots.

First of all, the buildings. The windows (at least in that game), don't seem to be using any sort of material at all, but rather incorporates the display of the rooms as part of the building's texture. However, if you are also looking for effects such as light reflection off of windows and having rooms look different from different angles, I would recommend making a room texture (or a few) and then modifying the texture coordinates based on the angle of the view. Then, just mix that color with the color of the "window" and top it off with some specular.

As for the cars, it seems that only the windows in the front actually modify the color. For example, if you look through the car's cabin, the back window does have any effect on the light coming through. What this implies is that they used some sort of back face culling on the rear windows to improve performance. Along with other types of culling (buildings, distance, view, etc.), this leads to at most a hundred or so transparent objects at once, which is more manageable.

Again, this is just a guess at how they implemented these effects. I could be wrong, but I think that is how I would begin at replicating them if it was up to me.

Edit:
One last thing that is critical. (That I completely forgot to mention) LOD for your render techniques is a must. For example, you could probably approximate car windows from a certain distance away to be just a darkish-blue color. As for buildings, you could do something similar or just use a small generic texture. This is something I am fairly sure was used in GTA III.

Cheers, Don.

-------------------------

slapin | 2017-06-03 20:38:57 UTC | #3

Thanks for your answer.

As my buildings do contain actual interior, I think some of the glasses should show it. So I think I need some kind of LOD implementation (or even some glass limiter). But how could I implement rendering technique LOD?
Also at close distance the glass should have some reflective properties to have glass feel - how to do this?
Or summarizing - how to make glass which feels like glass in Urho without going for PBR yet?
(I don't feel strong enough for full PBR pipeline yet).

-------------------------

Don | 2017-06-03 21:00:29 UTC | #4

If your building have an actual interior, you can disregard what I said about the building optimization. Regarding the "glassy look", that is usually attributed to the reflection of the environment. (No idea how to implement this) With the rendering technique LOD, look into the documentation at https://urho3d.github.io/documentation/1.6/_materials.html. I believe this allows you to specify one material with multiple techniques, and you can then choose distances at which each one is used (I think). I'm not too knowledgeable about Urho, but hope this helps.

Perhaps someone who has been using this engine longer could shed some light on the Urho side of this?

-Don

-------------------------

slapin | 2017-06-03 21:37:23 UTC | #5

Ah, thank you for the hint, I missed this, I did not know that is possible!

-------------------------

smellymumbler | 2017-06-04 00:31:52 UTC | #6

This could be useful: 

http://interiormapping.oogst3d.net/
http://www.inear.se/2011/02/interior-mapping-in-unity3d/

-------------------------

slapin | 2017-06-04 01:13:26 UTC | #7

Ah, it is really cool stuff indeed. But I will have actual interiors...
Anyway, I want to have just glass for the moment, that would be real step forward...

-------------------------

