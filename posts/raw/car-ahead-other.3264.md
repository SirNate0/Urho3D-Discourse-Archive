CarloMaker1 | 2017-06-16 22:29:06 UTC | #1

Hi all, 
i have a problem and i can't solve so i m posting here a question , 
i have two vehicles , i know position and velocity vector, so how to know if a vehicle  is front of other. 
Thanks

-------------------------

Modanung | 2017-06-17 10:03:14 UTC | #2

`(carBPosition - carAPosition).DotProduct(carADirection)` should get you the distance car B is ahead of car A. This is called [scalar projection](https://en.wikipedia.org/wiki/Scalar_projection).
Note that this is relative to car A, and dependent of that car's rotation. I have no experience creating racing games, but you may want to combine this with checkpoints to cut up the track into smaller pieces that are aware of their general direction... this way, overtaking a car is like passing a moving checkpoint in between two stationary ones.

-------------------------

rasteron | 2017-06-17 00:18:40 UTC | #3

Welcome back CarloMaker. Have you lost access to your original or transferred account? 

https://discourse.urho3d.io/u/carlomaker

Maybe one of the mods here can help..

-------------------------

CarloMaker1 | 2017-06-17 07:21:55 UTC | #4

@Modanung Many thanks !
 @rasteron hi, thanks, i just recover my profile!

-------------------------

Modanung | 2017-06-20 21:15:15 UTC | #5

Urho3D also has the `Vector3::ProjectOntoAxis` function. This normalizes the `axis` parameter and _then_ does a `DotProduct`.

-------------------------

slapin | 2017-06-20 21:46:25 UTC | #6

Any examples of usage?

-------------------------

