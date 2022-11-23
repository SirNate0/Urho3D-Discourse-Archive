NessEngine | 2019-03-07 23:43:16 UTC | #1

Whats the best way to add animated billboards with 3d depth test into my game? I don't know how many I'll have, its dynamic for effects and some types of NPCs. Should I use BillboardSet or is there something more suitable?

Think for example sprites of old games like doom or duke 3d, but they need to interact with 3d models. They should also be affected by lights and shadows (assume normals always facing forward).

Thanks!

-------------------------

Leith | 2019-03-08 14:21:12 UTC | #2

Take a look at ParticleEmitter - it derives from BillboardSet and may be a bit closer to what you want.

-------------------------

Modanung | 2019-03-08 05:17:38 UTC | #3

I made an animated billboard set for [OGTatt](https://gitlab.com/luckeyproductions/OGTatt):

* [animatedbillboardset.h](https://gitlab.com/luckeyproductions/OGTatt/blob/master/animatedbillboardset.h)
* [animatedbillboardset.cpp](https://gitlab.com/luckeyproductions/OGTatt/blob/master/animatedbillboardset.cpp)

Feel free to consider this `AnimatedBillboardSet` MIT-licensed, btw.

-------------------------

