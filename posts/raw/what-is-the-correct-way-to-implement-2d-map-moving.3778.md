Taymindis | 2017-11-26 15:20:49 UTC | #1

Hi, 

If I have a longer horizontal 2D map from start to the end. Should I moving the cameraNode or spriteNote? Or both?

For example the game: 
Super Mario Run.

Thanks,

-------------------------

Modanung | 2017-11-25 09:44:13 UTC | #2

For a simple (procedural) endless runner or flappy bird clone I'd use a static camera and horizontally locked player, with the world moving past.

In the example of Super Mario Run **both** the camera and the sprite would move, while the world remains static.

-------------------------

Taymindis | 2017-11-26 03:39:41 UTC | #3

Thanks for your advice/
May I know which node is world regarding? Scene?

-------------------------

Modanung | 2017-11-26 09:27:39 UTC | #4

Well, each object in the world would move by and disable or reposition itself once it has left the screen.

Have a look at the `BarrierLogic` of @1vanK's [Flappy Urho](https://github.com/1vanK/FlappyUrho/blob/master/GameSrc/BarrierLogic.cpp).

-------------------------

