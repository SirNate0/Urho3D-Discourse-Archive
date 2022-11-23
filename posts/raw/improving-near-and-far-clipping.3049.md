vivienneanthony | 2017-04-25 20:28:19 UTC | #1

Hi,

I ran into a problem previously. There was a nice tweak to work. I was getting material artifacting if near clip was zero or to low. I left a issue of it at https://github.com/urho3d/Urho3D/issues/1920 and http://imgur.com/a/yyP7q

When I set the near clip of the camera to 1.0f it helped solve the problem. Ideally I would like to move the camera for example 1km from a object and still have it show visibly okay.  At minimum a near clip of 0.1f or lower, to 8192km far clip. It might be a little extreme.

Ideally I would like to model objects full scale as 1.0 equal to 1 meter.

Any thoughts or help appreciated. As I'm not sure what internal Urho3D updates is needed to make that possible.

Vivienne

-------------------------

Eugene | 2017-04-26 08:37:43 UTC | #2

1. I heard that reversed depth buffer may solve some depth issues.

2. The safest way is to use separate scenes (large-scale world and local space).

3. Far clip affects precision much less that near clip. BTW, far clip may be +Inf

-------------------------

