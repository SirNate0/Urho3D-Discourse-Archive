AndreyCreator | 2019-02-17 08:36:45 UTC | #1

I'm new here. Excuse me if it was explained already.

Is there a way to make a landscape with 3D cells (or tiles) similar to Minecraft style? With different 3D objects for each cell, with cells having their own "health" and so on.

Please don't tell me to create a lot of objects and arrange them. It is bad idea. If something moves then it will check collisions with all these objects and it will be slow.

-------------------------

S.L.C | 2019-02-17 08:46:14 UTC | #2

See if you can find anything of use here https://discourse.urho3d.io/t/my-voxel-engine-open-sourced/4123

Otherwise I'm guessing you could look into creating your own custom geometry instead of objects.

-------------------------

Modanung | 2019-02-17 09:11:35 UTC | #3

Depending on what you mean by "Minecraft-style" you may or may not be interested to follow (or contribute to) the development of Edddy:  
https://gitlab.com/luckeyproductions/Edddy

The idea behind it is to use `StaticModelGroup`s for the blocks.

Welcome to the forums, btw! :confetti_ball: :slightly_smiling_face:

-------------------------

AndreyCreator | 2019-02-18 19:58:08 UTC | #4

Please explain me what is the principle of collision detection in these two projects? Do they check for collisions for all voxels while moving?

I would prefere to have 3d matrix and a set of passive objects which are not used in collision detection. And then I would check for matrix cells object is passing through. It is the fastest way of manipulating with such space. Is it possible to implement it in Urho 3D?

-------------------------

Modanung | 2019-02-19 13:43:16 UTC | #5

I dunno, I just use the built-in Bullet without hardly any knowledge about its inner workings.

-------------------------

I3DB | 2019-02-19 14:27:01 UTC | #6

[quote="AndreyCreator, post:4, topic:4936"]
Please explain me what is the principle of collision detection
[/quote]

[Check with the source of the software. Get right into the bottom of it.](https://github.com/bulletphysics/bullet3/releases)

-------------------------

