Dave82 | 2017-01-02 01:05:32 UTC | #1

Hi i started to add bullet hole decals , but it's seems that if you align the decals from a very "steep" angle , the uv coords become extremely distorted 


[img]http://s30.postimg.org/606t49ikx/decs.jpg[/img]





They are always screen aligned therefore they are distorted if you look them from different angle. I tried to align them to surface normal or using fixed orientation none of them helped
Is there a way to place them aligned to surface normal and keep the texture coords ?

-------------------------

cadaver | 2017-01-02 01:05:33 UTC | #2

This is mathematically exactly as expected, though visually unfortunate. You could check the normal with a raycast before applying the decal and if it's too extreme, don't add the decal, or maybe use another texture that represents a "grazing" hit.

-------------------------

