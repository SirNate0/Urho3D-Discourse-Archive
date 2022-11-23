najak3d | 2021-04-08 07:11:57 UTC | #1

I am posting to just confirm something I think I learned today.   It appears to me that DepthBias behaves entirely different between DirectX and OpenGL.   For OpenGL, a constant depthBias of 0.001 made our Far Terrain shift by a LOT, while in DirectX this same 0.001 setting only shift's it a small amount (and looks good).

In short, we have near and far terrain in our 3D view... the far terrain shows much less detail, and so we put it UNDER the near Terrain, so that you don't see the Far Terrain until it's beyond the end of where near terrain ends.

For some reason, on OpenGL, the DepthBias of constant 0.001 if AMPLIFIED A LOT, compared to DirectX.   I would have expected that Urho3D might have made them behave similarly.

Code looks like this:
BiasParameters s_FarBias = new BiasParameters() { ConstantBias = 0.001f };


Our solution, tentatively, is to vary the ConstantBias by an order of magnitude to make OpenGL behave similarly to DirectX.

Can someone explain the best-practice for how a developer should be dealing with this?

-------------------------

throwawayerino | 2021-04-08 08:38:14 UTC | #2

A quick fix (maybe?) is divide by 2. I'm not sure why, maybe one of the wizards here could help more
https://github.com/urho3d/Urho3D/blob/master/Source/Urho3D/Graphics/OpenGL/OGLGraphics.cpp#L1818
https://github.com/urho3d/Urho3D/blob/master/Source/Urho3D/Graphics/View.cpp#L751

-------------------------

Eugene | 2021-04-08 09:03:44 UTC | #3

DepthBias is _supposed_ to work the same. I'll check if I can reproduce your issue locally.

-------------------------

Eugene | 2021-04-08 12:59:49 UTC | #4

[quote="najak3d, post:1, topic:6792"]
For some reason, on OpenGL, the DepthBias of constant 0.001 if AMPLIFIED A LOT, compared to DirectX.
[/quote]

Is this "a lot" equal to 256, by any chance?

-------------------------

najak3d | 2021-04-08 21:53:24 UTC | #5

The "a lot" means it's grossly skewing the location of the object on the screen downwards a LOT.   I was applying it to Far terrain which goes from under the camera on to the horizon, about 1800 miles away.  The Near Terrain only goes to around 300 miles, so beyond 300 miles, you should only be seeing the Far Terrain.

Here is what it's supposed to look like, with OpenGL DepthBias set to 0.000035, it's working well, and looks like this -- here you can see the far terrain matches up exactly with Far Water, to fade out together in unison.  No Offset here is apparent.

![image|690x298](upload://iow4M9gOOfGf9GrstIQWoRq4F5v.png) 

When I set the DepthBias to 0.001, the far terrain drops WAY DOWN on screen.  What is really happening here is that the FarClip is kicking in way too close... so it's not really moving it DOWN, but rather is simply culling out all Far Terrain beyond a certain point.   The DepthBias is effectively rampantly causing the FarClip plane to skoot WAY CLOSER.  Here is the result of 0.001:

![image|642x252](upload://p5TYCAMY4e5FHKFqeaMlTA5NPXO.png) 

On DirectX, this 0.001 depthBias works perfectly  (same as the top image above).

If I set an intermediate value for DepthBias on OpenGL, you can see the FarClip plane move back closer to where it should be.  Here's DepthBias 0.0004:

![image|544x261](upload://h8lTWW8PXjrxThYOtqGxkbN1WRi.png) 


So the big question is why is DepthBias on OpenGL causing the effective FarClip distance to scoot WAY CLOSER?

My tentative solution is to simply use different DepthBiases for OpenGL vs DirectX.  Is there a better solution?

-------------------------

Eugene | 2021-04-09 16:24:29 UTC | #6

I just tested it with Sample 08 which uses material `UrhoDecal` with ConstantBias = -0.00001.
I put decal on the floor and move away until it becomes visible thru geometry due to this bias.
I get consistent results for both DX11 and OpenGL2/3, both 16 and 24 bit depth buffers.
I was testing my branch, but Urho Web sample looks the same too.
![image|598x184](upload://p3Qt4PTCA7spErOS4Yc43bKIBLk.jpeg) 

I'll try to check OpenGL maths later.

-------------------------

najak3d | 2021-04-09 16:44:33 UTC | #7

Eugene, I think the actual bias may be the same.   The bug that I'm seeing is that for OpenGL when I set DepthBias, the effective FarClip plane is being moved WAY in.    So if you are looking at stuff more horizontally (not perpendicular) - the objects with bias disappear entirely as the geometry extends beyond this new shortened Far-Clip-Plane.

-------------------------

