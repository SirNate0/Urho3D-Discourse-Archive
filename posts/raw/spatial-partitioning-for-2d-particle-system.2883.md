sabotage3d | 2017-03-11 18:33:43 UTC | #1

Hi guys,

I have a simple 2D particle system in Urho3D and I would like delete particles based on region. At the moment I need to loop all the particles to compare the distance from the culling area. In addition I would like to add simple collision queries. Would you suggest a good spatial partitioning that I can use to optimize it? If there is something readily available with Urho3D or something as an external lib.

-------------------------

codingmonkey | 2017-03-11 20:37:57 UTC | #2

Hi, you may try to render your areas into additional RT (8 bit) and then use this RT as mask for discard pixels in shader when you render your patricle emitter. I guess this easy way to achive this effect with less efforts

-------------------------

sabotage3d | 2017-03-11 21:21:28 UTC | #3

Thanks codingmonkey. I would prefer to remove the actual particles. Using RT would make this very difficult.

-------------------------

