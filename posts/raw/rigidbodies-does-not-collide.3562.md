nergal | 2017-09-13 18:13:20 UTC | #1

I have multiple rigid bodies with mass = 0 (they are static chunks in the world). Then I create chunks with mass that should collide with the world. But as you can see on the gif below, they don't collide. They just fall by. But when I create small boxes with 1x1x1 in size, the boxes collide with the "world" bodies that has no mass.

I can't see what I'm missing here, I really need some help.

https://giphy.com/gifs/3o7aDc8ueKqCSbL7c4

-------------------------

Eugene | 2017-09-13 18:42:38 UTC | #2

Only convex shapes are allowed to be dynamic. Triangle meshes are not.

-------------------------

nergal | 2017-09-13 18:24:35 UTC | #3

Hm, but they seem to collide with each other?

-------------------------

nergal | 2017-09-13 18:33:35 UTC | #4

ok! Now I see, creating a box around for the shape works good. Are there any plans to add Triangle mesh shapes for dynamic?

-------------------------

slapin | 2017-09-13 19:34:29 UTC | #5

There are convex hulls which work.

-------------------------

Eugene | 2017-09-13 20:48:58 UTC | #6

Note: In order to use convex hulls you have to decompose your mesh into convex subshapes.

-------------------------

Eugene | 2017-09-13 21:03:10 UTC | #7

[quote="nergal, post:4, topic:3562"]
Are there any plans to add Triangle mesh shapes for dynamic?
[/quote]

I've just added it.
It is available here https://github.com/eugeneko/Urho3D, will push it as soon as CI passes.
Use `GImpactMesh` shape type to allow triangle mesh be dynamic.

-------------------------

slapin | 2017-09-14 00:29:53 UTC | #8

Isn't Bullet momentum calculation will be off in case of non-convex mesh? I remember something like that,
did not try it myself though.

-------------------------

Eugene | 2017-09-14 06:54:27 UTC | #9

I don't know. If you mean inertia, I think it should be calculated for each dynamic object.
However, push me if you remember something more concrete.

-------------------------

1vanK | 2017-09-14 10:46:13 UTC | #10

Most physics engines use "Separating Axis Theorem" for fast detection of collisions, but it requires convex shapes. Triangle to triangle collision uses something like brute force and is unsuitable for practical use in games

-------------------------

slapin | 2017-09-15 00:11:09 UTC | #11

I mean shape which is used to calculate inertia should be convex for inertia to be correct. Otherwise you need to override
using btCompoundShapes btCompoundShape::calculatePrincipalAxisTransform. I mean inertia tensor of course.

This hit me very badly with vehicles behavior, so I had to learn all this things. This happens with convex hulls too,
but definitely will affect non-convex shapes.
BTW it is a way for Bullet to override "momentum shape" (inertia tensor) if anybody wishes for proper vehicle dynamics
like me.

-------------------------

