hualin | 2017-01-02 00:58:43 UTC | #1

Hi,
I can't find a way to rotate a node around a custom pivot, the Quaternion has no such method, and the Node doesn't too. 
Would you please tell me how to do this?
Thank you for your time!

Edit:
The new API of class Node that RotateAround is good for using, thank you all!

-------------------------

GIMB4L | 2017-01-02 00:58:43 UTC | #2

Either position your model's space around the pivot, or use a redundant scene node parented to the main node, which is some distance away from that node. Then, when you rotate the parent node, the whole thing will rotate.

-------------------------

hualin | 2017-01-02 00:58:44 UTC | #3

Thank you GIMB4L.
Is there a way to set the pivot? I mean how to position the model' space around the pivot, my pivot is a local point.
eg. the origin point is (0, 0, 0), and now I want to set it (0, 0, 5) ahead of the model. Do you mean that position the pivot in 3d model builder like as blender or 3dx max?

-------------------------

friesencr | 2017-01-02 00:58:44 UTC | #4

You can kind of get a glimpse into how to do it from the editor orbiting bits  EditorView.as[ln:1166]

[code]            if (input.mouseButtonDown[MOUSEB_MIDDLE] && (selectedNodes.length > 0 || selectedComponents.length > 0))
            {
                Vector3 centerPoint = SelectedNodesCenterPoint();
                Vector3 d = cameraNode.worldPosition - centerPoint;
                cameraNode.worldPosition = centerPoint - q * Vector3(0.0, 0.0, d.length);
                orbiting = true;
            }[/code]

Essentially you need to add or subtract a fix length vector from another point (d) and optionally rotate the d by multiplying a quaternion.

Bonus: Math sucks

-------------------------

hualin | 2017-01-02 00:58:44 UTC | #5

Thank you, friesencr.
I tried this way, and it is ok for orbiting, but it can't solve my problem.
What I want is an anchor point, like as the figure shows:
[img]http://s30.postimg.org/uzs0adyun/image.png[/img]
The point is pivot, is there a way to achieve this purpose?
I think if the class Node provide an API that SetRotatePivot or RotateAround is better for using.

-------------------------

cadaver | 2017-01-02 00:58:44 UTC | #6

This code (example is in AngelScript) should do what you're after, pivoting around a local space point (Vector3 localPivot). Because the coordinate space choice isn't obvious and there are many kinds of orbits you might want, I believe it's better to do with existing API functions and not expand the Node class to contain extra state for a pivot point, so that it stays as lean and simple as possible.

[code]
    Quaternion delta(0, 10 * timeStep, 0); // This could be any rotation
    Vector3 rotatedPivot = delta * -localPivot + localPivot;
    Vector3 newPos = node.transform * rotatedPivot;
    Quaternion newRot = delta * node.rotation;
    node.SetTransform(newPos, newRot);
[/code]
EDIT: now that the transform space refactoring is in, you should also be able to do this simply with 

[code]
node.RotateAround(localPivot, delta, TS_LOCAL);
[/code]
Note that the localPivot will be affected by the node's local scale.

-------------------------

