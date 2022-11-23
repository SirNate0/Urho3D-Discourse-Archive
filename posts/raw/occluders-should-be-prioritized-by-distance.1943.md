Enhex | 2017-01-02 01:11:42 UTC | #1

If I have a player stand right next to an occluder wall that hides everything(!), that wall may not be used for occluding if the max occluder triangle count was already reached.
Meanwhile, far away occluders which are near the max draw distance and have nothing to hide behind them steal all the occluder triangles.
An occluder at the end of the draw distance is useless, while an occluder with the same screen size near the camera is useful.
Note that there are more far away occluders than near occluders because volume increases faster than radius.

Prioritizing occluders by distance could greatly increase the effectiveness of the software occlusion.

[img]http://i.imgur.com/JKM8rEr.png[/img]

Note that in indoors scene, you'll virtually always have nearby walls that can occlude everything, so prioritizing occluders by distance will have HUGE benefit.
And it's beneficial to every scene in general, I can't think of a case that it could make things worse.

Prioritizing may involve taking into account distance and size, and then sorting the occluders according to their "score".

-------------------------

cadaver | 2017-01-02 01:11:42 UTC | #2

There is already a sort algorithm in View::UpdateOccluders(), but it also takes into account number of triangles, which may not be a good decision. 

If you want to experiment with that and report back, be my guest.

-------------------------

Enhex | 2017-01-02 01:11:42 UTC | #3

Ok, I'll look into it.

Right now in my project I can stand is a closed room or next to a wall and it won't use those near triangles and render everything behind.

To give some perspective, here's what I get with and without triangles limit (very high limit) in a sealed room:
Default limit:
[i.imgur.com/kDUFONc.jpg](http://i.imgur.com/kDUFONc.jpg)
[i.imgur.com/nOh5kph.jpg](http://i.imgur.com/nOh5kph.jpg)
Without  limit:
[i.imgur.com/SB5RFlB.jpg](http://i.imgur.com/SB5RFlB.jpg)
[i.imgur.com/SB5RFlB.jpg](http://i.imgur.com/SB5RFlB.jpg)

As you can see almost everything is culled away when there's no triangles limits, which means the current sorting doesn't do a good job.

-------------------------

vivienneanthony | 2017-01-02 01:11:43 UTC | #4

Hi,

Maybe there should be a disable or enable distance as a factor? Im going run into the same situation

Viv

-------------------------

vivienneanthony | 2017-01-02 01:11:43 UTC | #5

Hi,

Maybe there should be a disable or enable distance as a factor? Im going run into the same situation

Viv

-------------------------

Enhex | 2017-01-02 01:11:43 UTC | #6

I made some improvements and opened an issue:
[github.com/urho3d/Urho3D/issues/1305](https://github.com/urho3d/Urho3D/issues/1305)

-------------------------

cadaver | 2017-01-02 01:11:43 UTC | #7

Your work is merged now. Thanks!

-------------------------

