esakylli | 2019-01-04 11:12:37 UTC | #1

I have an issue with bullet physics when using triangle mesh as the collision shape.

My scenario is this:
I have a static physics body on a node, and set the collision shape for it to triangle mesh (because I have created a custom geometry).
On top of that body I have a dynamic body, with a collision shape of box.

When the simulation is started the dynamic box moves up a little. In the debug view of the physics world I can see that there is a small gap between the static body and the dynamic body.
But the debug view seems to be showing the shapes correctly.
If I apply some force to the dynamic body it behaves very strange, jittering on top of the static body.

Even if I don't use my custom geometry, instead use the ordinary Box.mdl with triangle mesh as the shape I get the same strange behaviour.
If I use a convex hull for the static body, I see the little gap between the bodies but I don't get the strange jittering.
If I change the static body to a box, then all is fine.

Anyone have any clue of what's going on here?
Btw, I'm using UrhoSharp (but I don't think it should matter).

-------------------------

esakylli | 2019-01-12 12:26:49 UTC | #2

I found a solution to my problem:
By setting margin to 0 on the static collision shape it works as expected.

But I don't know why this is the case... I saw in the source code that default is 0.04 for all shape types.

-------------------------

jmiller | 2019-01-04 16:21:14 UTC | #3

Presumably, Collision Margin 0.04 was thought a reasonable generic default. 'Ideal' values currently depend at least on shape type and [url=https://urho3d.github.io/documentation/HEAD/_physics.html]Physics[/url] configuration..

  https://gamedev.stackexchange.com/questions/113774/why-do-physics-engines-use-collision-margins

In my scenes using default PhysicsWorld parameters I'm using 0.1 for StaticModel, 0.01 for Sphere, 0.0 for Plane... and these are just preliminary approximations that look correct at a glance.

-------------------------

