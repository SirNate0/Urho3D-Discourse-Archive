burt | 2018-11-10 08:58:58 UTC | #1

Just saw this cool video: https://www.youtube.com/watch?v=Giuoq786gP0

Does anyone have any idea what he is using here? Just some random noise on the weapon root bone?

-------------------------

suppagam | 2019-07-18 01:42:00 UTC | #2

Seems like the https://en.wikipedia.org/wiki/Lissajous_curve ?

-------------------------

Leith | 2019-07-18 05:26:03 UTC | #3

I'd go with random torque, resulting in compound angular error, and a motor sluggishly pulling the orientation back toward the aim constraint, like a slow spring... but I sense it's not that random... the right "feel" would include the angular momentum at the moment of firing.

-------------------------

suppagam | 2019-07-18 13:44:07 UTC | #4

Could you elaborate a little bit on "compound angular error" and "random torque"? By random torque, you mean pushing the model randomly in the horizontal and vertical axis over delta time? Like, model.x = model.x * rand(1, 50) * delta.Time?

-------------------------

Leith | 2019-07-19 08:32:41 UTC | #5

I was actually thinking in spherical terms - something akin to arcball rotation, but a 2D version would involve choosing a vector which points away from the target in a direction which is initially random, but which tends in the direction of any existing offset, and with a random (but clamped) magnitude. This vector can be used to compute a new lookat vector, which we lerp toward fairly rapidly, while a spring equation can be used to pull the newly-calculated lookat vector back to point at the target over time.
The concept I had in mind is that initially we choose a random directional error term, but should the player shoot again, the new direction should strongly reflect the existing direction error term - and this whole notion of angular error terms should definitely be clamped to reasonable angular limits...

-------------------------

