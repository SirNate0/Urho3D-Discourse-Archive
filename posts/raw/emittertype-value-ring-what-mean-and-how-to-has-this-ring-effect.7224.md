tianlv777 | 2022-03-29 07:06:28 UTC | #1

![U64JJ3@GU7Z@P2_VOZ67Y9|404x306](upload://dqdf3Oc6jx64JDYs0zfwkiZOYQ3.png)

-------------------------

tianlv777 | 2022-03-29 07:06:52 UTC | #2

![B)FPSZ@O0%7Q%SGGYT(H1%L|690x487](upload://pYX49XUh5mqwZsVdOZwu9B5qIu5.png)

-------------------------

SirNate0 | 2022-03-29 12:51:37 UTC | #3

You are only emitting 1 particle, so you won't notice the ring. Set it (Number of Particles) to something like 500 and you'll see what it actually does.

However, I don't think Urho is capable of giving you the C (a ring with a cutout) shape vs an O shape (a ring), at least out of the box.

-------------------------

SirNate0 | 2022-03-31 10:31:52 UTC | #4

One further comment: I believe the ring itself in your original example is actually a ribbon trail, and that particles are also spawned around it. Which may be fairly doable in vanilla Urho, as long as you don't need the ring to move around. Or you could just use a fixed model instead of the ribbon trail. Presumably the ring rotates on its axis, which could be done either by animating the texture UVs or by rotating the model.

-------------------------

tianlv777 | 2022-03-31 10:56:19 UTC | #5

https://effekseer.github.io/en/contributes/Effekseer01/index.html
This is an example of the original effect. I just want to see if it can be transplanted to Urho.

-------------------------

