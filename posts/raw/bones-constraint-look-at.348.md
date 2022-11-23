ghidra | 2017-01-02 00:59:46 UTC | #1

I can come up with questions everyday, here is todays...

Looking through the examples files i didnt find anything that addressed this specifically...
What are the methods to have an animated characters head look at something. Or have an aimed gun stay aimed where the mouse is point in a 2.5d type game? Basically doing a post constrain or rotate on specific bones of a character.

Along those lines, what about the possibility of inverse kinematics for ground and feet placement?

Thanks again for putting up with my constant stream of "what about" I'm enjoying everything about the engine so far.

-------------------------

jmiller | 2017-01-02 00:59:46 UTC | #2

Having these things asked can be useful to others and they're good questions.  :slight_smile:

CharacterDemo (.cpp here) uses an AnimatedModel, and manually controls a bone and its corresponding Node:

[code]    // Set the head bone for manual control
    object->GetSkeleton().GetBone("Bip01_Head")->animated_ = false;
...
    // Turn head to camera pitch, but limit to avoid unnatural animation
    Node* headNode = characterNode->GetChild("Bip01_Head", true);
[/code]
You could use Node::LookAt(const Vector3 &target, const Vector3 &up=Vector3::UP, TransformSpace space=TS_WORLD)
in your scene update event.

Documentation on skeletal animation can be found in "related pages". [urho3d.github.io/documentation/a00025.html](http://urho3d.github.io/documentation/a00025.html)

Physics system's RigidBody also has kinematic mode (which I haven't used), a few types of constraint, and is used to transform nodes.
[urho3d.github.io/documentation/a00031.html](http://urho3d.github.io/documentation/a00031.html)

-------------------------

Mike | 2017-01-02 00:59:46 UTC | #3

In example 18_CharacterDemo, Jack's head follows camera pitch.
See [url]http://discourse.urho3d.io/t/rotating-characters-head/31/1[/url] for snippet with both pitch and yaw.

For IK, I think we would have to rely on a library like this one: [url]http://quelsolaar.com/confuse/index.html[/url].

-------------------------

ghidra | 2017-01-02 00:59:46 UTC | #4

of course i had that example open, and didnt see that.
Thanks for pointing that out, that is exactly what I am looking for.

-------------------------

