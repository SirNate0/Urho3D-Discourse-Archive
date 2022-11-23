Triangle345 | 2019-02-16 17:02:57 UTC | #1

I cannot seem to find any examples of animating a sprite using a regular png / jpeg style sprite sheet. It seems that its extremely easy to use a spriter style animation but no information on regular png sprite sheet animation. Can anyone point me to or give an example of using a regular sprite sheet in Urho3D?

-------------------------

Modanung | 2019-02-16 20:17:28 UTC | #2

Maybe this [AnimatedBillboardSet](https://gitlab.com/luckeyproductions/OGTatt/blob/master/animatedbillboardset.cpp) could help you in the right direction.

Also, welcome to the forums! :confetti_ball: :slight_smile:

-------------------------

Triangle345 | 2019-02-16 20:32:54 UTC | #3

This seems like its implementing the rendering of the sprite sheet manually? Is that the only way to do it in Urho3D?

-------------------------

Modanung | 2019-02-16 20:41:47 UTC | #4

Have you seen [sample 24](https://github.com/urho3d/Urho3D/blob/master/Source/Samples/24_Urho2DSprite)? Though I guess that's what you mean by Spriter animation.

-------------------------

Triangle345 | 2019-02-16 21:20:28 UTC | #5

yep they are using a spriter file in that one. I'm looking for just loading one big packed png or jpeg and having Urho3D take sections of that as the animation.

-------------------------

Modanung | 2019-02-17 08:43:01 UTC | #6

Then I think animated particles are the closest to what you are looking for, that comes with the engine. The animated billboard set was inspired by it.

It's quite trivial to map frame numbers to a list of UV-coordinates, or pixels for that matter. Having your own approach can also save you unneeded extras _and_ allows for personal and project-specific logic.

-------------------------

weitjong | 2019-02-17 14:57:36 UTC | #7

Have you guys checked out `SpriteSheet2D` class? But I don't think there is any example code.

-------------------------

Modanung | 2019-02-17 18:09:18 UTC | #8

No, to be honest.

[SpriteSheet2D.h](https://github.com/urho3d/Urho3D/blob/master/Source/Urho3D/Urho2D/SpriteSheet2D.h)
[SpriteSheet2D.cpp](https://github.com/urho3d/Urho3D/blob/master/Source/Urho3D/Urho2D/SpriteSheet2D.cpp)

-------------------------

Triangle345 | 2019-02-17 23:14:35 UTC | #9

There is a function called DefineSprite in SpriteSheet2D which seems like it maps a region to an id. However; it is hard to determine how this would work to create a sprite sheet animation

-------------------------

Modanung | 2019-02-18 06:51:20 UTC | #10

What seems unclear about its workings?
https://github.com/urho3d/Urho3D/blob/master/Source/Urho3D/Urho2D/SpriteSheet2D.cpp#L97-L114

-------------------------

Triangle345 | 2019-02-18 07:29:12 UTC | #11

well for instance you can name a section of the sprite sheet but how do you use that to cycle through images. All i'm saying is that it would be helpful to have an example for something as common as using a plain sprite sheet.

-------------------------

Leith | 2019-02-18 08:48:52 UTC | #12

OK, what's happening, is we are declaring a unique name for each spriteframe we define - each frame of sprite animation will have a unique name, and will be stored in the array called spriteMapping_ inside the spritesheet2d container object. 
At runtime, we will call GetSprite(name) at some frequency we decide, in order to update some Sprite ui element. It's not an ideal system in my opinion but I can see what's going on - SpriteSheet2D is merely a container, you're meant to use it inside your own sprite controller class. Why it does not expose a method to look up a sprite frame by index? I don't know, I can only guess its using a Map container, ie, keys are names, values are sprite frame info - I can't see why we went this way.

-------------------------

