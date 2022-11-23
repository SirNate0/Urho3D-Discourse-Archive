1vanK | 2017-02-11 12:44:33 UTC | #1

If I understand correctly, currently fixed step for Box2D not fixed actually. What about this variant of game loop, used in XNA by default: https://msdn.microsoft.com/en-us/library/microsoft.xna.framework.game.isfixedtimestep.aspx

Also it smooth out mouse moving on low/variable fps.

EDIT: Another side of it - in xna Update(timeStep) and Draw(timeStep) can have different timeStep. This value can be used for interpolate objects coords between frames on rendering phase if need fps more than update rate

-------------------------

cadaver | 2017-02-13 09:46:10 UTC | #2

IMO the Physics2D subsystem should be fixed if it doesn't currently support variable timestep properly.

Otherwise I wouldn't advocate for this kind of update loop as a general case, as to render smoothly it would need to support  interpolation of object transforms, in case update & render run at different rates. Currently Bullet does its own interpolation to account for that.

-------------------------

1vanK | 2017-02-13 09:55:02 UTC | #3

It is no so easy: http://gafferongames.com/game-physics/fix-your-timestep/


> To understand what is going on consider a situation where the display framerate is 60fps and the physics is running at 50fps. There is no nice multiple so the accumulator causes the simulation to alternate between mostly taking one and occasionally two physics steps per-frame when the remainders “accumulate” above dt.

>Now consider that in general all render frames will have some small remainder of frame time left in the accumulator that cannot be simulated because it is less than dt. What this means is that we’re displaying the state of the physics simulation at a time value slightly different from the render time. This causes a subtle but visually unpleasant stuttering of the physics simulation on the screen known as temporal aliasing.

-------------------------

