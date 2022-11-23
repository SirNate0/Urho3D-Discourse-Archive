ghidra | 2017-01-02 01:01:45 UTC | #1

Im having some issue with the CollisionShapes collision mask.
I'm making a couple of node, a character, projectile, and enemy nodes. Each have a collision shape and rigidbody.
The character is set to mask 3, while projectile and enemy are set to mask 2.
However, the projectile and the enemy are not colliding. If I set everyone to mask 3 everyone collides fine.

-------------------------

hdunderscore | 2017-01-02 01:01:46 UTC | #2

I will first assume you know that the masks are bit wise ([url=http://en.wikipedia.org/wiki/Mask_%28computing%29]link[/url]).

I do believe that you need to set the Collision Layer too. In that case, the default layer is 1 and if you left that to be true, your mask of 3 is ok because 3 covers bits 1 | 2. If you change your Collision Mask to 2, you are now excluding collisions in layer 1 (and every layer except 2).

-------------------------

ghidra | 2017-01-02 01:01:46 UTC | #3

you would assume incorrectly. I didn't know that.
That's helpful, thank you.

-------------------------

