zedraken | 2017-01-02 01:14:08 UTC | #1

Hi all,

I am testing force application to an object that has a rigid body and a shape for collision detection. 
I am using the ApplyForce() method with different application location points on the object to see how such force affects the object orientation.
Basically, when the objects has not been transformed by any operation (a rotation for example), the observed effect when the force is applied on one side of the object is the one that is expected. The object will rotate by itself in the correct direction (for example, if an UP force is applied at the bottom rear, the rear then lifts up).
However, if I first rotate the object, let's say, by 90 degrees on a horizontal plane, and I then apply the force, the result is not the one that is expected. The object rotates but with the same movement that previously, like if it the 90 degrees rotation was not taken into account. In my example, it is the right side that lifts up, not the rear although the force is applied at the rear (I hope so !).

To help the understanding, here is a piece of code that I use when I want to apply a force :

1 - I get the object position (in fact the node position)
[code]Vector3 p = objectNode->GetPosition();[/code]

2 - I get the object node rotation (to take into account that it has been rotated by 90 degrees)
[code]Quaternion q = objectNode->GetRotation();[/code]

3 - I draw a debug line starting from the point where the force is expected to be applied
[code]dbgRenderer->AddLine(p + q * ForceApplicationPoint, p + q * ForceApplicationPointEnd, Color(?));[/code]

Position of the starting point is : object position in world + rotation quaternion * local force application point

4 - I apply the force to the rigid body associated with the object
[code]objectBody->ApplyImpulse(force, q * ForceApplicationPoint);[/code]

I use the quaternion to also rotate the point where the force is applied in order for that point to follow the object rotation. Note that the ForceApplicationPoint is a point that is relative to the object center, not the world center.


With an identity quaternion (no rotation of the object), the force is properly applied. If I apply the force at the bottom rear of the object, it lifts up as expected.

After a rotation by 90 degrees, the object lifts up from the right, like if the right is in fact the rear.

Is it possible to debug the various forces applied to a rigid body, to display them by lines or vector for example, just to check if they are correctly applied ?
I guess that in my understanding, something is missing  :unamused: 

Thanks in advance for your help.

-------------------------

1vanK | 2017-01-02 01:14:08 UTC | #2

U can try make something like CrowdAgent::DrawDebugGeometry (it shows a speed vector)

-------------------------

