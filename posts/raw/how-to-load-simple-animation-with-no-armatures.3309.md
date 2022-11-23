irrmich | 2017-07-03 07:52:41 UTC | #1

I can't find how simple animation with no bones, no armature can be imported in an uhro based application.

When my animation consists only of a cube wich only do some rotation, scale, translation, the animation doesn't work, only the model and material are imported, the animation looks like ignored :/

Can anyone give me some working code for simple animation with no bones?

Please help, i'm new to Uhro? how to do this?

-------------------------

jmiller | 2017-07-10 19:53:34 UTC | #2

Hi,

Urho also has a powerful attribute animation feature:
https://urho3d.github.io/documentation/HEAD/_attribute_animation.html
The sample application 30_LightAnimation demonstrates this feature.

In your case, the relevant attributes might be Position, Rotation, Scale.

HTH

-------------------------

Mike | 2017-07-10 20:11:03 UTC | #3

You can also refer to this similar [thread](https://discourse.urho3d.io/t/solved-export-animated-node-transforms-to-urho3d/1067).

-------------------------

