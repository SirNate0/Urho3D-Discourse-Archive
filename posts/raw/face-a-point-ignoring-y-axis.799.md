rogerdv | 2017-01-02 01:02:59 UTC | #1

I need to rotate a character to face another point, but ignoring the Y component. Tried this some weeks ago and discarded the code because it didnt worked. How can I rotate nodes to point in a given direction?

-------------------------

cadaver | 2017-01-02 01:02:59 UTC | #2

One way is to use LookAt() and rewrite the target y coordinate so that it's the same as the character's y coordinate. For example in the RagDolls AngelScript example (needs all characters to be stored in the modelNodes array)

[code]
for (uint i = 0; i < modelNodes.length; ++i)
{
    Vector3 target = cameraNode.worldPosition;
    target.y = modelNodes[i].worldPosition.y;
    modelNodes[i].LookAt(target);
}
[/code]

-------------------------

rogerdv | 2017-01-02 01:02:59 UTC | #3

Yes, that should work! Now I remember that what I did was to set target Y to 0, with the side effect of character being rotated to look a bit down.

-------------------------

