GodMan | 2019-11-05 20:52:44 UTC | #1

Any one approach anything on flying AI? I'm thinking of maybe taken the approach were flying AI can move to designated points in the air using predefined points in the environment.

-------------------------

Modanung | 2019-11-06 09:04:43 UTC | #2

Don't overcomplicate things and vector math is your friend.

Dot Product|Cross Product
---|---
![Image](https://upload.wikimedia.org/wikipedia/commons/3/3e/Dot_Product.svg)|![Image](https://upload.wikimedia.org/wikipedia/commons/b/b0/Cross_product_vector.svg)

Maybe also splines?
Are there any obstacles in this airspace, btw?

-------------------------

GodMan | 2019-11-05 21:41:17 UTC | #3

No their are no obstacles. It's just an open map, the same one in my screenshots in the Random Project Shots thread. Unless you count cliff walls, but mostly an open area.

-------------------------

GodMan | 2019-11-05 21:44:27 UTC | #4

I'm just looking for something, for my sentinels from halo.
https://i.ytimg.com/vi/n-aiT5xgb6s/hqdefault.jpg

-------------------------

Modanung | 2019-11-05 22:00:33 UTC | #5

Would that be more of a (strafe-)hovering with target tracking instead of the airplane I had in mind?

-------------------------

ab4daa | 2019-11-06 00:38:29 UTC | #6

I used to add sphere obstacle in [RVO2-3D](https://github.com/ab4daa/RVO2-3D) ([test proj](https://github.com/ab4daa/RVO2-3D-Obstacle-Test)).

(But it is not actually "piloting" the vehicle, I never played halo so don't know how realistic piloting you want.)

-------------------------

GodMan | 2019-11-06 03:23:05 UTC | #7

@Modanung Yes they hover while targeting an enemy. Yes lol no airplane like movement. .

-------------------------

Modanung | 2019-11-06 11:26:54 UTC | #8

In that case I imagine something like:
A custom `LogicComponent` (with probably an abstract AI class in between) that knows at least two states: Patrol and alert. In the patrol state the AI would find the nearest point on a predefined spline path and accelerate towards a point further down the same path. When it sees a target it should probably stop patrolling and instead orbit and attack its target from a preferred distance.

-------------------------

dertom | 2019-11-06 16:55:51 UTC | #9

Not sure if that would be overkill, but you could have a look at opensteer:

code(seems to be a newer fork): https://github.com/meshula/OpenSteer
docs: http://opensteer.sourceforge.net/doc.html

There were a very good website, that showed all types of steering behaviour, but those were java-applets which are not supported anymore. :|

-------------------------

GodMan | 2019-11-06 20:07:37 UTC | #10

Thanks everyone. I might look into @Modanung approach first.

-------------------------

