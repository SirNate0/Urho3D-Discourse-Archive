savindrap | 2017-03-15 06:24:41 UTC | #1

Hi, I am manually controlling each bone of a skeleton model, I want to apply rotations only for a specific bone but not its children. As an example I want to apply rotations only to upper arm bone and not to fore arm bone linked. How do I do this?

-------------------------

Eugene | 2017-03-15 08:31:39 UTC | #2

You have to do it manually: something like

    T = child.worldTransform;
    parent.rotation = ...
    child.worldTransform = T;

-------------------------

slapin | 2017-03-16 08:50:00 UTC | #3

Well, the solution above might be not so good.
If you want to prevent bone rotation but otherwise obey the parent motion
you have to use Inverse quaternion.

    Quaternion prot = parent_node.worldRotation;
    Quaternion crot = child_node.worldRotation * prot.Inverse();
    child_node.worldRotation = crot;

Something like that.

-------------------------

