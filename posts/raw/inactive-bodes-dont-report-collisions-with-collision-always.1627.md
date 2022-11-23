Enhex | 2017-01-02 01:09:04 UTC | #1

I have a pickup that suppose to report collision with the player.
It uses collision mask to filter for the player.
When it's active (white outline in debug render), it reports collisions and works fine.
When it's inactive (green outline in debug render), it doesn't report collisions.

I've tried to use COLLISION_ALWAYS but it doesn't change anything.
I'm using a trigger body for the player. Even if I change it to a regular body it still shows up inactive, it's in a child node (the character controller has a separate body).
Is there a way to force a body to be active, and a trigger one specifically?
Is it always inactive because it's a child of a node with a body? If I try to set mass to a child body it gets removed (can't have dynamic child in Bullet).
Is it possible to have a child node with a body without automatically making the body parented?

btw if I disable rest thresholds for all pickups, so it always stays active, it works properly but that seems like an expensive solution.

-------------------------

Sir_Nate | 2017-01-02 01:09:10 UTC | #2

Have you tried calling Activate() on the Rigid Body (every physics step it is disabled)?

-------------------------

Enhex | 2017-01-02 01:09:11 UTC | #3

Yeah I tried messing with activation, it didn't help.
I ended using two separate nodes with a physical constraint between them.

-------------------------

