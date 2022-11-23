Jimmy781 | 2017-01-10 03:17:12 UTC | #1

Hey guys , 

I just upgraded my urhoSharp version and i'm having some issues :-

1)  plane.SetMaterial(Material.FromImage("image.png"));

This used to add the image texture on the plane as it , however it is now rotating the image 90 degrees anti-clockwise and then placing it on the scene . Any idea how to fix that ?

Thanks

-------------------------

artgolf1000 | 2017-01-10 13:42:01 UTC | #2

I don't use UrhoSharp, maybe UrhoSharp does not use the latest model?

You may download the latest Plane.mdl from Urho3D's master branch/bin/Data/Models, replace the old version with it to see if it can fix the issue.

-------------------------

Jimmy781 | 2017-01-13 01:04:35 UTC | #3

Nope , tried the new plane.mdl and the image is still added sideways .

Anyone else faced this issue ?

-------------------------

