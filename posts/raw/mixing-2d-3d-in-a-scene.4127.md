nergal | 2018-03-27 09:39:24 UTC | #1

Is there any limitation by mixing Urho2D and Urho3D? I was thinking about making a pixel-art game and be using the Bullet2D physics stuff but still use a 3D scene for particles and other functionality (lightning etc). 

If I understand correctly in the documentation the only difference 2D/3D is the use of orthographic camera instead of a perspective camera?

-------------------------

ghidra | 2018-03-27 16:50:38 UTC | #2

I can not speak to the ability to mix the 2 context...
But, you could at the very least just use the 3d context, and keep your simulations locked to 2 axes. I am doing something similar for a top down shmup, and i have no complaints.

-------------------------

jmiller | 2018-03-28 12:11:19 UTC | #3

Hello!

Urho2D stuff is actually represented in 3D space, and though I haven't used 2D physics yet, I think the simple answer is "no".
Urho's approach may not be unique, but I still find it inspired.

I've mixed in layered maps of Sprite2Ds... seems quite 2D until some 3D movement or camera perspective changes. :)

-------------------------

nergal | 2018-03-28 12:40:58 UTC | #4

Thanks for your input!

I will start to elaborate a bit and see for myself. I think it would be cool to integrate bullet2d physics in a 3D scene for example in a side-scroller game :slight_smile:

-------------------------

