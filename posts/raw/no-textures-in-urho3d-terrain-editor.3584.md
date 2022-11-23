crisx | 2017-09-22 18:35:34 UTC | #1

Hi

I tried to use the JTippetts's Terrain Editor, could successfully build with Urho 1.6 lib, but when I launch it, the terrain is all blank, the texture painting doesn't seem to do anything

![Image4|634x500](upload://n4K1uVBKk73eBDsLkWvccKC2NpN.jpg)

I must have missed something...

-------------------------

JTippetts | 2017-09-20 19:37:21 UTC | #2

That'll be due to missing shaders on D3D11 or D3D9, most likely. Since I haven't updated those yet. D3D11 is hard for me to do, because I am constantly uninstalling Visual Studio due to hatred, and a D3D11 build on MinGW is tricky. I'll try to get the shaders updated soon, might have to wait until I can use a different computer at work or something.

This project is not really active, so I apologize for the rough state of things. Just never have enough time to do all the stuff I want to do these days. :/:neutral_face:

-------------------------

JTippetts | 2017-09-20 22:22:37 UTC | #3

Alright, I managed to get a D3D11 shader pushed to github. It's D3D11 only; no D3D9 support, since D3D9 doesn't support texture arrays. I might provide a D3D9 path that just uses a texture atlas, or I might just forget about D3D9 altogether since it really is pretty obsolete.

-------------------------

crisx | 2017-09-21 08:23:20 UTC | #4

thanks for the clarification, I recently upgraded my OS to windows 10 so it might be one of the reason...

too bad... your tool looks really great

-------------------------

JTippetts | 2017-09-21 13:39:33 UTC | #5

"too bad… your tool looks really great"

Give it a try, then. I said I got the D3D11 shader in, so you should be able to run it now.

-------------------------

crisx | 2017-09-22 14:23:47 UTC | #6

I tried with the last repository but I've got the same problem

-------------------------

JTippetts | 2017-09-22 14:24:51 UTC | #7

Are you using D3D11 or D3D9?

-------------------------

crisx | 2017-09-22 14:48:59 UTC | #8

My bad, it's D3D9...
I will recompile Urho lib with URHO3D_D3D11 set and try again

-------------------------

crisx | 2017-09-25 11:50:46 UTC | #9

I compiled Urho3D with URHO3D_D3D11=1 but I still have references to d3d9.lib, so I've got the same result when I builded Terrain Editor with the new lib, maybe it's an issue with Visual Studio I don't know
I tried to change d3d9.lib with d3d11.lib but it's ending with compilation errors

-------------------------

JTippetts | 2017-09-26 03:08:34 UTC | #10

Make sure it's a clean build. Sometimes it doesn't work if you just try to change an option like that on top of an existing build. I know I've had issues before.

-------------------------

