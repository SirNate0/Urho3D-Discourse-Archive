Jens | 2022-10-13 15:13:14 UTC | #1

Hi,

Every time SphereCast() gets a hit, the returned distance (and HitFraction) is zero. RaycastSingle() does return the correct distance, so the problem just seems to be with SphereCast().
This is on UrhoSharp so, unless I've made some sort of error, the problem is in UrhoSharp or Urho3D or Bullet. My bet is Urho3D or Bullet, I cannot believe UrhoSharp forgets to fill a var it gets from Urho3D.
Regardless the correct distance can be calculated from the sphereRes.Position, but wondered if anyone can confirm it is working in Urho3D?
Thanks.

```
PhysicsRaycastResult sphereRes = new PhysicsRaycastResult();
float sphereRadius = 2;
float sphereMaxDist = 7; 
Ray sphereSend = new Ray(ReverseForWPosOffset, -ammoVelNorm);
physicsComp.SphereCast(ref sphereRes, sphereSend, sphereRadius, sphereMaxDist, collisionMask);

   if (sphereRes.Body != null)
   {
     initialRayDist = sphereRes.Distance;//always zero
     initialRayPos = sphereRes.Position;
     float distance = Vector3.Subtract(raySend.Origin,sphereRes.Position).Length; //works
    }
```

-------------------------

SirNate0 | 2022-10-13 13:36:17 UTC | #2

Works for me using C++. I am seeing distances of 0, 0.453, and inf from a spherecast that I had in my code already. So more than just 0.0.

At distance 0, is your sphere already intersecting an object? (The character, maybe?) And/or are the bodies that are being hit already within the radius 2 sphere when it is at position 0? Though it seems odd to me that the Position works correctly if that is the case...

-------------------------

George1 | 2022-10-13 13:39:17 UTC | #3

Just a side note, UrhoSharp is too old.  

You should try:  https://github.com/Urho-Net/Urho.Net

[elix22]  seems to work on .net 6 support atm and this is based on a more recent version of Urho3D.

-------------------------

Jens | 2022-10-13 15:00:09 UTC | #4

[quote="SirNate0, post:2, topic:7337"]
At distance 0, is your sphere already intersecting an object?
[/quote]

Thanks, Sir Nat0! 
The problem is not completely solved, but at least with your suggestion I do get non-zero distances returned.
Reducing the radius from 2.0f, which admittedly was way too large, to 0.025f now only gives zero for around 1/3 of the hits.
I agree, it is strange that the body, normal and position are filled whilst distance and HitFraction are zero. 

As this is not a problem for Urho3D, this should probably be counted as solved. Anyway, it does not matter so much, as I only use the position point going forward - I just find it disconcerting. Still, not as disconcerting as the Collision Event arguments often returning zero for the obj.Contacts[0].ContactImpulse, even though all other CollisionData vars are filled. AFAIK, though, it is a bullet problem. At least it is reasonably easy to do a workaround for that.

-------------------------

Jens | 2022-10-13 15:08:22 UTC | #5

Thanks for the info George1.
Thing is, I'd rather leave it until the game is finished and working perfectly, or as perfectly as possible, before booting UrhoSharp. There have been no showstoppers up to now, and I just need to plough on until finished.
Do you know if UrhoSharp have stopped developing? It might be they will still come with an update.

-------------------------

SirNate0 | 2022-10-13 16:07:59 UTC | #6

[quote="Jens, post:4, topic:7337"]
The problem is not completely solved, but at least with your suggestion I do get non-zero distances returned.
Reducing the radius from 2.0f, which admittedly was way too large, to 0.025f now only gives zero for around 1/3 of the hits.
I agree, it is strange that the body, normal and position are filled whilst distance and HitFraction are zero.
[/quote]

I'm not certain, but I think the hit fraction is the fraction of the total distance the sphere has traversed before hitting the other body. So if the sphere, when placed, hits anything, (including something "behind" it along the ray) the hitFraction will be 0. Since the [distance is calculated from the hitFraction](https://github.com/urho3d/Urho3D/blob/796802f595472a414fd9815f9c3dfde7d350d9f4/Source/Urho3D/Physics/PhysicsWorld.cpp#L491), it is unsurprising that the distance is 0 when the hitfraction is 0 (hitfraction is also set to 0 for the case of no hit, while distance is M_INFINITY, so there is an exception to that).

-------------------------

