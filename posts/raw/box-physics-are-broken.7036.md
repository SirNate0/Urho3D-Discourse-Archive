niansa | 2021-11-03 08:32:48 UTC | #1

So I am trying to figure out physics...
![image|690x388](upload://f0ZcxvBu9Rq6wOXEdjSmqr9r3Of.png)
![image|690x388](upload://pWsr2qVgjPodfmGb2IyZTxLpYWB.png)
I attached a collision shape to the floor (Box) as well as to that object that I enabled gravity for and set mass to 1.
However, that object tends to fall through the floor but usually just floats above not even laying flat.

Does anyone have an idea how to solve that problem? I tried everything but seems like my knowledge isn't high enough lol!



Edit: Seems like the problem only occurs if the object below

-------------------------

niansa | 2021-11-03 08:33:24 UTC | #2

... uses trianglemesh for collision shape.

(The editor did not let me edit the message)

-------------------------

Modanung | 2021-11-03 09:08:25 UTC | #3

That might be part of the problem: Triangle meshes are only supposed to be used for stationary objects. Things that move around should use basic shapes or convex hulls.
You might also want to add some friction and play with the rest thresholds and damping factors. And personally, I like my big G closer to 17 than 9.81; looks more natural to me.

-------------------------

niansa | 2021-11-03 09:42:52 UTC | #4

I mean like, the object that moves around is just a box but the environment is a triangle mesh.

-------------------------

Modanung | 2021-11-03 09:54:02 UTC | #5

Ah, so that's fine.

Could you share a screenshot showing all `RigidBody` attributes?

-------------------------

Modanung | 2021-11-03 10:20:05 UTC | #6

`CollisionShape`s also have a margin, btw, with a default value of 0.04. So it's normal for them to not fully touch. You can either reduce the margin, or take it into account by reducing the shape's size.

The gap might indeed be 0.08.

-------------------------

