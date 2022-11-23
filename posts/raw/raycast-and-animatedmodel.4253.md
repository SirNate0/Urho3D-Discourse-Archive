tarzeron | 2018-05-23 01:35:07 UTC | #1

On StaticModel Raycast detect on mesh, how make this on AnimatedModel? Because BoundingBox of Bone too big and not intersect which mesh.
![RaycastAndAnimation|666x500](upload://tr1g7LuW1INDTaPrtb9xC6rr8Uy.gif)
[example source code](https://github.com/Tarzeron/Urho3dRaycastAndAnimation/blob/master/main.cpp)

-------------------------

SirNate0 | 2018-05-23 03:12:18 UTC | #2

Perhaps try a view mask or testing the triangle or type of drawable returned. I don't really know, I only just started experimenting with raycasts today myself. Sorry I can't help more.

-------------------------

tarzeron | 2018-06-24 11:59:58 UTC | #3

I solved the problem.  After raycast on engine I make additional check, self-make animation for model on CPU and check crossing it with ray. I update repository, can someone it will be interesting.
![Screenshot|666x500](upload://e8ndXpTuhQLttHEZ4WoEgG7z0vQ.gif)

-------------------------

