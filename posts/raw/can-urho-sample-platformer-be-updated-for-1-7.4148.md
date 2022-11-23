LiamM32 | 2018-04-07 07:20:46 UTC | #1

The purpose of [Urho Sample Platformer](https://github.com/damu/Urho-Sample-Platformer) is a very good one; to have an example of a full game with Urho3D to use as a reference.  By "full game" I mean that it has a menu, and other basic features that you expect every complete game to have.  As such, it should be endorsed by the Urho3D project itself.

However, it has been last updated for Urho 1.5.  I want to use it as a reference to learn to use Urho3D, but I don't have the skills to update it.  May someone please do that?

-------------------------

lexx | 2018-05-08 04:37:09 UTC | #2

Hi.
I updated that sample to work with trunk version of Urho3D. 

Source code is almost same:
I changed KEY_ESC to KEY_ESCAPE and changed Clamp(float,double,double) to Clamp(float,float,float) so no more errors.
CMake and CoreData and some Data files are from urho3d trunk. 
One can load updated sample from my fork:

https://github.com/bosoni/Urho-Sample-Platformer

-------------------------

LiamM32 | 2018-05-04 07:29:10 UTC | #3

Thank you.  I actually did manage to figure out how to make it compile with Urho3D 1.7 before you posted this.  I just changed the "KEY_ESCAPE" and the "Clamp(float,float,float)" part that you mentioned.  It did compile and run with 1.7, but with bad performance.

I see that your changes are much more exhaustive.  But is this what's required to make it work with the trunk version of Urho3D?

I compiled your version with Urho3D 1.7 (which is what I wanted it to work with).  The framerate is much higher, but the ground is invisible, so it's basically unplayable.  I suppose I must reverse some of your changes?

I tried copying the CMake, CoreData and Data folders from my Urho3d-1.7 folder, and overwriting.  But the game still behaves the same.

-------------------------

lexx | 2018-05-08 04:58:07 UTC | #4

Seems that scene is invisible because of materials. Scene uses its own techniques and shaders and maybe there is something wrong.

But if you use Materials/flag_cloth.xml  material on level_*** 
 materials, then you can see terrain, boxes and mushrooms.  (hack hack)

Seems that level2 crashes on Debug (but Release works). Debug works too with smaller scene.

-------------------------

v.v.balashoff | 2022-06-23 20:11:52 UTC | #5

I've upgrade it to 1.7.1.
https://github.com/vvbalashoff/UrhoSampleProject

-------------------------

