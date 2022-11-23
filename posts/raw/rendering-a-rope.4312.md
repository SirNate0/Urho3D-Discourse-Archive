aaaaaaaaargh | 2018-06-12 10:46:06 UTC | #1

Hi,

as the title implies I'm trying to render a rope. :slight_smile: 

On the physics side of things I have set up a rope consisting of rigid body segments that are chained with point constraints. Every segment is represented by a scene node (a child of its preceding rope segment or the rope root). So far this is working pretty nice, so the next step is to render the rope. Because of occasional gaps between the constrained physics bodies when the rope is swinging around heavily I concluded that attaching single models to each segment scene node is out of question. The next thing in mind is to use a custom generated geometry along with skeletal animation. It was easy to create the model (I've used manual vertex / index buffer creation in order to attach the geometry to an AnimatedModel), but I'm struggling on how to define the bones. I cannot see any setters / create methods in the Skeleton class and the only thing that adds bones appears to be the deserialization method.

Is it not possible to create a bone structure programmatically? What are your thoughts? Should I implement my own shader and pass the vertex transforms as uniform instead?

For reasons of simplicity (as well as clickbaiting) I've attached an image explaining what I want to achieve:
![image|592x500](upload://mZuDVjWOK9UlwyrV1IgtFsJ92q5.jpg)

The red line is the model i want to deform while the white segments are the rigid bodies of the physics simulation. I hope that makes it a bit more clear.

Thanks for any help!

-------------------------

Modanung | 2018-06-12 17:29:27 UTC | #2

Why not just read the nodes' position and generate the mesh - each frame - based on that?

-------------------------

aaaaaaaaargh | 2018-06-12 18:17:16 UTC | #3

Sure, I could do that, but wouldn't that be incredibly slow?

Wait.. or are you talking about vertex buffer updates? I've never seen that in Urho, do you know some kind of example on how to do that?

-------------------------

Eugene | 2018-06-12 21:40:44 UTC | #4

CustomGeometry was designed to be frequently updated.

-------------------------

Modanung | 2018-06-13 10:43:08 UTC | #5

[quote="aaaaaaaaargh, post:3, topic:4312"]
I’ve never seen that in Urho, do you know some kind of example on how to do that?
[/quote]

## Sample 34: Dynamic Geometry
https://github.com/urho3d/Urho3D/tree/master/Source/Samples/34_DynamicGeometry

-------------------------

