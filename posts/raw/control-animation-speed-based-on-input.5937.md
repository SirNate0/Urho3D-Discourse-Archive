lebrewer | 2020-02-19 23:26:46 UTC | #1

This is maybe somewhat related to my previous thread, but I wanted to keep them separate because it might be more useful for future developers looking for answers here on the forum. I've recently saw this:

https://www.youtube.com/watch?v=ovWeZvD6X_E

And I was curious on how to make it work with Urho. How can I tie player input "strength" with the animation speed?

-------------------------

SirNate0 | 2020-02-19 16:12:09 UTC | #2

You have some sort of floating point input strength between 0 and 1 (like the joystick magnitude). Then you just adjust the speed of the animation based off of that. To get the effect of the video it looks like they're also blending between a run and a walk animation based on the strength. Other solutions may be better, but that's the first that came to mind.

-------------------------

bvanevery | 2020-02-19 22:36:36 UTC | #3

[quote="lebrewer, post:1, topic:5937"]
might be more useful for future developers looking for answers here on the forum
[/quote]

BTW if that is the purpose, it is miscategorized.  "Developer Talk" is for altering the Urho3D engine internals.  Like adding features to the codebase that would allow things to happen that currently don't.  "Discussions" would be for how to do things in Urho3D.  "Feature Request" would be for something you're pretty sure is missing, that you'd like to see added, but you aren't going to do the work to add it.

I don't know if you can recategorize.

-------------------------

Modanung | 2020-02-20 11:16:39 UTC | #4

The video seems to show an animation that is tied to the movement of the object, which *in turn* is caused by input. If you use input to determine the animation speed and direction you would get something that looks more like a (3D) Mario; running on the spot before speeding up.

-------------------------

