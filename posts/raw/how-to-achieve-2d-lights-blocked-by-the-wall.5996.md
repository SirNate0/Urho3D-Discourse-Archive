spwork | 2020-03-16 11:10:38 UTC | #1

I used the alpha blending method to implement 2d lighting, but I don't know how to achieve the light blocking by the wall. There is no idea. How can I achieve it,Like right。
![image|690x361](upload://jOj1ENMU91wzkOgVN0pR4bftjch.jpeg)

-------------------------

Modanung | 2020-03-16 11:22:59 UTC | #2

Maybe this could help you out:
https://github.com/mattdesl/lwjgl-basics/wiki/2D-Pixel-Perfect-Shadows

-------------------------

spwork | 2020-04-20 03:00:59 UTC | #3

Finally, it's succeed.
![image|690x388](upload://uOcQKy3phSeiYjr7WyD2xLASrMG.jpeg)

-------------------------

Modanung | 2020-04-20 12:37:17 UTC | #4

Cool.
Any plans to share that code?

-------------------------

spwork | 2020-04-23 02:48:33 UTC | #5

This is a clumsy implementation, using the CPU to calculate the light length and manually updating the depth map, but it has met my game's needs.It can throw a brick and attract jade to get a better implement, of 2d lighting.
https://github.com/spwork/Urho3D-2DLighting

![image|690x388](upload://nwMQ0j5R9SxHL7I5nE7sbkz5WjF.jpeg)

-------------------------

