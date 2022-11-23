SirNate0 | 2021-04-26 21:27:45 UTC | #1

I was looking through the Convex Hull stuff for a small project I've been working on, and I noticed that Urho3D uses the StanHull library to calculate the convex hulls from a set of vertices. I was wondering why we use this library, rather than simply passing the vertices to Bullet from the model and/or using Bullet's own Convex Hull utilities?

-------------------------

Modanung | 2021-04-27 08:40:50 UTC | #2

Let's see if this still works...


:sparkles: :fish: **_Abra @cadaver!_** :sushi: :sparkles:

-------------------------

cadaver | 2021-04-29 10:29:30 UTC | #3

From my memory, just passing the vertices of an arbitrary mesh directly did not give a working hull shape. Using StanHull for arbitrary mesh seemed the most straightforward way, compared to trying to work out how the Bullet's hull utility classes work, and *if* they work for any arbitrary mesh shape that may not be convex to begin with. But you're naturally free to define your alternative implementation, if proven good then it would make sense to remove StanHull.

-------------------------

Modanung | 2021-05-02 08:03:22 UTC | #4

Like a charm. Thanks Lasse!

-------------------------

