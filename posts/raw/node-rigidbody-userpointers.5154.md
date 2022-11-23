Leith | 2019-05-17 06:43:34 UTC | #1

I have a bit of a problem involving physics collision detection.

The player character is holding a weapon, which is attached to their right hand.
The zombie character has an animated ragdoll armature of rigidbodies.

When player character attacks zombie with weapon, and when weapon collides with zombie bodypart, I am notified of the collision: which bodies took part, and the parent nodes of those two rigidbodies.

Now I know that a weapon has struck a specific bodypart on a zombie.
But I don't know which player was wielding that weapon, or which zombie was struck!

The node information I am provided is too deep in the scene hierarchies of these two characters to tell which characters were involved!

String tags seem like a bad choice to identify parentage, and the Bullet Physics userpointers are already being used by Urho3D.

Urho3D's RigidBody and Node classes do not support user pointers which I could set to identify my owner object.

Is there any recommendations about how to tag Urho3D objects as being related to some other object, particularly with regards to rapidly identifying the root grandparent of a deeply nested child?

-------------------------

Dave82 | 2019-05-17 09:28:14 UTC | #2

[quote="Leith, post:1, topic:5154"]
Node classes do not support user pointers
[/quote]

Maybe you could set up a variant for a node and store the body parts. Even better idea is to send your own events. That's how i did it.

-------------------------

Leith | 2019-05-17 13:25:55 UTC | #3

Thanks for the input, Dave82!

It looks like I can use Node::SetVar to set a named Variant, which can hold either a naked pointer (void*) or more safely, a RefCounted pointer.
String Tags really are a horrible idea, but the Node class does have support for multiple named and typed user variables, including pointers, so I consider this case solved. Your mention of "variant on a node" is what reminded me to look into exactly what I can do with node variables. Cheers!

-------------------------

