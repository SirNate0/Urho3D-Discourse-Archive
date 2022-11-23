GodMan | 2019-01-04 10:18:39 UTC | #1

I've been looking into managing projectiles used in my application. I have been working on a rocket launcher, and looked briefly at the ninja demo. The snow ball class seems a little extreme for such a simple concept.
For example snowball.cpp uses snowball.h which links to another header file which links to another one on top of that.

I am trying to think of a simple approach for my project. For example if a node "projectile" travels a certain distance, and has no collision with anything then it gets deleted.

-------------------------

Dave82 | 2019-01-04 03:22:24 UTC | #2

I have a simple ProjectileManager component in my game. This component is responsible for moving updating and removing projectiles in the whole game , placing bullehole decals on walls and other basic logic. I have a Vector of sProjectile's which are simple structs and store bullet properties (speed , velocity , direction , damage etc) These are simple projectiles which doesn't require visual form (shotgun bullets , handgun bullets) use a simple raycasting per frame method.
Visual projectiles from the other hand are created from a root node and a script that is responisble for updating and initializing the projectile.
I found this approach the cleanest possible. I don't like to code high level stuff in cpp. It bites you in the arse very fast , when you have to recompile your game after every slight change.
I use scripts whenever possible.
You should create a script for each projectile type.

-------------------------

GodMan | 2019-01-04 22:32:30 UTC | #3

So did you use scripts? I was hoping to avoid that, but just find a more simplistic approach.

-------------------------

