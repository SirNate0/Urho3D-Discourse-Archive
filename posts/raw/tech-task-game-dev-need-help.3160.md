keith7 | 2017-05-25 13:09:32 UTC | #1

Hey. I create a game. But I need help. Help me please.
The essence of what.
I have a scene as a 3d object, I have dynamic objects and I have a screen-like action as an interface. I need it to be rendered on the screen in this order:
-Static scene
-Picture Interface Over Static
-Dinamic object on top of the interface image
-One more picture of the interface on top of everything

  The camera will always remain stationary.

How I can do that ?
Disable depth test not solutions.

-------------------------

jmiller | 2017-06-02 15:58:47 UTC | #2

Hey keith7, and welcome to the forum. :)

Here are a few threads with information around these topics.

https://discourse.urho3d.io/t/how-to-control-render-order/1240
https://discourse.urho3d.io/t/how-to-layer-scenes/740
https://discourse.urho3d.io/t/how-to-best-generate-an-in-game-hud/1684

Current docs on render paths
  https://urho3d.github.io/documentation/HEAD/_render_paths.html

-------------------------

Modanung | 2017-06-02 16:28:06 UTC | #3

And possibly the [RenderToTexture](https://github.com/urho3d/Urho3D/tree/master/Source/Samples/10_RenderToTexture) sample?

-------------------------

