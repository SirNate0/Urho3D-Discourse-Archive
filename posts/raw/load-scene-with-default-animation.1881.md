Shylon | 2017-01-02 01:11:01 UTC | #1

Seems in editor is not possible to use default animation for an Animated Model when loading the scene in game, so everything should be programmed, for example, think of a 3d platformer, I want a windmill in background have a default rotation animation and use its default animation in editor and when I load the scene in the game the windmill rotate itself, or I have an enemy character and I would like to have default animation when it is loaded, say for example its stand animation.

-------------------------

theak472009 | 2017-01-02 01:11:10 UTC | #2

You can do it by creating EditorUpdateEvent or something like that. For example, in Unity when you select a particlesystem, it will start playing particles. Or in  your case, when you select AnimatedModel, it will start playing animation. All you have to do is in the AnimationController, subscribe to the EditorUpdateEvent or anything you name it and then call Play.
I dont know if this is the correct solution but it works for me!

-------------------------

Shylon | 2017-01-02 01:11:10 UTC | #3

Thanks, Actually I used [b]LogicComponent[/b] for automatic update of character in c++ (see animation examples), and yes it is possible, I requested this solution for in editor and selecting default animation for loading a scene, that would be nice.

EDIT:
also I think it is possible to use [b]Tags[/b], loading all specific tags that for example tagged with ANIM, and loop through them and play them automatically.

-------------------------

rasteron | 2017-01-02 01:11:11 UTC | #4

[quote]
Seems in editor is not possible to use default animation for an Animated Model when loading the scene in game, so everything should be programmed, for example.[/quote]

I think with a bit of modification in the Editor you can make some changes with the scene update and achieve that like there's the Play/Update button for starters.

-------------------------

Shylon | 2017-01-02 01:11:12 UTC | #5

I might look at it, but this is feature request, so if anyone who is more familar with editor code the it would be easier for him/her, that could be a checkbox under animated model (where test button is) that shows "load this animation as default" or something.

-------------------------

