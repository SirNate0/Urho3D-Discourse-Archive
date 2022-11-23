vivienneanthony | 2018-03-03 23:38:03 UTC | #1

Hello,

I have a node with a rigidbody and static model component. Then I have a child node with a rigidbody pointing downward quaternion (0,0,0,-1), static model component, and propulsion component.

Whenever I attempt GetRotation() on the node with the propulsion component. I'm told the quaternion of the node is (1,0,0,0). Which is odd. I tried getting the rotation of the rigidbody body specifc.

What I want to do for example if the propulsion node is facing downward, is to apply a impulse on the parent node rigidbody. I'm assuming the math would be parent quaternion multiplied by propulsion quaternion multipled by amount like factor 10.

or

Getting the world rotation of the propulsion node and multiplying it. Meaning the quaternion. Which did not work either. I'm told the initial as the wrong quaternion.

Am I incorrect? The more important part is why I am getting the wrong quaternion.

Vivienne

-------------------------

vivienneanthony | 2018-03-04 00:21:50 UTC | #2

Sample code I am using.

[code]
// Apply Impulse
void PropulsionThruster::ApplyImpulse(Vector3 velocity) {
	// Get parent node 
	Node * pParent = m_pNode->GetParent();

	// If Parent Node
	if (pParent) {
		// Get RigidBody from parent node
		RigidBodyComponent * pParentRigid =
				pParent->GetComponent<RigidBodyComponent>();

		// If rigid body found
		if (pParentRigid) {
			// Turn off Kinematic
			if (pParentRigid->IsKinematic()) {
				pParentRigid->SetKinematic(false);
			}

			// Get this node rotation 
                        // Returns quaternion (1,0,0,0) when I tried the rotation of the node which is (0,0,0,-1)
                        // If I use Node->GetRotation()
			Quaternion rotation = m_pNode->GetComponent<RigidBodyComponent>()->GetRotation();

                        // Rotation should be direction of node rigid times Velocity
                        // Used Vector3::ONE and Vector3(0.0f,1.0f,0.0f) UP
			Vector3 Impulse = rotation * velocity * 15;

			// Multiply rotation by quaternion
			pParentRigid->ApplyImpulse(Impulse);			
		}
	}
}
[/code]

-------------------------

sirop | 2018-03-04 05:58:41 UTC | #3

[quote="vivienneanthony, post:1, topic:4069"]
What I want to do for example if the propulsion node is facing downward, is to apply a impulse on the parent node rigidbody. I’m assuming the math would be parent quaternion multiplied by propulsion quaternion multipled by amount like factor 10.
[/quote]

I may be wrong , but that which you try to implement is a mixture of translation and rotation.
"Normal" quaternions do render only rotation.
But the so called "dual quaternions" combine both translation and rotation.
See https://cs.gmu.edu/~jmlien/teaching/cs451/.../dual-quaternion.pdf .

-------------------------

elix22 | 2018-03-04 07:57:54 UTC | #4

Try Changing 

Quaternion rotation = m_pNode->GetComponent<RigidBodyComponent>()->GetRotation();

to 

Quaternion rotation = m_pNode->GetRotation();

-------------------------

Eugene | 2018-03-04 08:58:14 UTC | #5

(0, 0, 0, -1) is 360 degrees rotation... Or not. What notation do you use, xyzw or wxyz?

-------------------------

Sinoid | 2018-03-04 11:27:55 UTC | #6

[quote="vivienneanthony, post:1, topic:4069"]
Am I incorrect? The more important part is why I am getting the wrong quaternion.
[/quote]

Rigid bodies that are parented to other rigid bodies have an awkward transform update. You can see that in `RigidBody::setWorldTransform` depending on when you're doing this that could be why you're seeing transforms that you know should be wrong (assuming they're later correct).

Erroneously mismatching what you're reading with what you're seeing is easy to do (ie. referencing world rotation then looking at local rotation).

---

The `Node::GetDirection` is already in parent-local-space so if you're after a thrust vector based on the foward-facing of a child that'd be `ParentNode->GetWorldRotation() * ChildNode->GetDirection()`.

... which is pretty much the same thing as `Node::GetWorldDirection()`. An arbitrary vector would be `(parentWorldRotation * (childRotation * arbitraryVector))`.

-------------------------

vivienneanthony | 2018-03-04 14:56:51 UTC | #7

> Blockquote[quote="Eugene, post:5, topic:4069, full:true"]
(0, 0, 0, -1) is 360 degrees rotation… Or not. What notation do you use, xyzw or wxyz?
[/quote]

I'm using xyzw in which I have the rotation set wrong. Easy fix.

I have to look at the code and look up what JSandusky mentioned plus tweak changing center of mass. 

I was considering adding four thrusters in a box formation on the bottom. Then adjust each one by a percentage of float 1 so I can balance it out.

-------------------------

vivienneanthony | 2018-03-05 04:55:55 UTC | #8

[quote="Sinoid, post:6, topic:4069"]
Rigid bodies that are parented to other rigid bodies have an awkward transform update. You can see that in RigidBody::setWorldTransform depending on when you’re doing this that could be why you’re seeing transforms that you know should be wrong (assuming they’re later correct).
[/quote]

I got some better results using the help. Thanks.

As you mentioned oddly the transforms the updates is weird. I have to calculate the node position of the child as if it wasn't converted to some weird transformation.

-------------------------

vivienneanthony | 2018-03-09 04:50:31 UTC | #9

I am wondering if anyone have a suggestion. As you see from the video, I tried the method to apply thrust. It does work but the issue I have is the actual physics.

The ship uses a triangle mesh which I need to allow a player inside. The issue I think is the bullet physics origin or center of mass.  I think the problem might go away if I use a box as the collision shape or at least partially.

The main mesh is the ship hull with a center origin dead center. I have a navigation panel in front as a child node with a rigid body with a mass of 0 and a chair with a mass of 0 and matching collision shape components.

So, firstly, I need a idea how to balance(change center of mass) the mesh without offsetting the center of origin. What method might be best.

Secondly, Figure out the best way to apply impulse on the various points that would balance the rigidbody.


https://youtu.be/0iBETyqWQ98

The has a sky but can be a skybox of a galaxy so space game. Since, this is the lobby the "Go To Hangar" goes to a the player part. This is more a lobby and testing environment.

A lobby more like this or a space station lobby.

https://www.youtube.com/watch?v=Q50q1EUXiIs

-------------------------

