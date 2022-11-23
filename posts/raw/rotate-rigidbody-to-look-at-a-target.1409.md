vivienneanthony | 2017-01-02 01:07:33 UTC | #1

Hi,

I managed to get the weird bouncy behaviour fixed 

[youtube.com/watch?v=c7pELeYbCr4](https://www.youtube.com/watch?v=c7pELeYbCr4)

Now I'm trying to get a proper look at using the rigidbody body. I find a link with something that might help [gamedev.stackexchange.com/questi ... e-a-target](http://gamedev.stackexchange.com/questions/15070/orienting-a-model-to-face-a-target).

Can someone elaborate on the latter part on top because it's basically what I need. 

It mentions RotAxis and AvatarForwardUnit but I'm not sure of the Urho3D equivalent.

Vivienne

I can give more details about if anyone can help.

-------------------------

codingmonkey | 2017-01-02 01:07:33 UTC | #2

did you try node->LookAt(worldPosition) ?
[code]
		Scene->
		TargetNode->

		ShipNode->
			rigidbody->AngularFactors(0, 0, 0);
			CollisionShape(box)
			
			Node->
				(NodeWithFixedOrientForModel->) 
				StaticModel(ship) (it may be placed in this child node to get right orientation in parent space)
			
			this->LookAt(TargetNode.worldPosition);[/code]

-------------------------

vivienneanthony | 2017-01-02 01:07:33 UTC | #3

[quote="codingmonkey"]did you try node->LookAt(worldPosition) ?
[code]
		Scene->
		TargetNode->

		ShipNode->
			rigidbody->AngularFactors(0, 0, 0);
			CollisionShape(box)
			
			Node->
				(NodeWithFixedOrientForModel->) 
				StaticModel(ship) (it may be placed in this child node to get right orientation in parent space)
			
			this->LookAt(TargetNode.worldPosition);[/code][/quote]

That was the first thing I tried.

Current code excerpt
[pastebin.com/eUgd5wDP](http://pastebin.com/eUgd5wDP)

Right now if I try the ThisNode rotation it jumps outside the collision boxes and disappear. If I use Rigidbody it stays but stays titted not moving.

[i.imgur.com/oIBl3wg.png](http://i.imgur.com/oIBl3wg.png)

If I remove the rotation, the drone moves around like usual but rotation mostly based on physics.

Hmmmm

Viv

-------------------------

codingmonkey | 2017-01-02 01:07:33 UTC | #4

>ThisNode rotation it jumps outside the collision boxes and disappear.

Maybe somewhere you have forgotten world biggest rigidbody enabled ? And this little ships's RB just placed within it, and what why it jumps I guessing.

Anyway, is your's "ThisNode" have rigidbody component? It must do not have it, RB only for parent of "ThisNode" for basic colliding with wall and floor...

ThisNode  must have only: 
   Staticmodel (and if needed right oriented with additional child node)

and parent of "ThisNode" may have RB and basic collision shape.
RB must have a mass > 0
Angular factor must set to 0 to avoid rotations
in this situation you do your orientation to target only with "ThisNode" ->LockAt ( )
and movement/scale(not rotations!) only with parent of "ThisNode"

-------------------------

vivienneanthony | 2017-01-02 01:07:33 UTC | #5

[quote="codingmonkey"]>ThisNode rotation it jumps outside the collision boxes and disappear.

Maybe somewhere you have forgotten world biggest rigidbody enabled ? And this little ships's RB just placed within it, and what why it jumps I guessing.

Anyway, is your's "ThisNode" have rigidbody component? It must do not have it, RB only for parent of "ThisNode" for basic colliding with wall and floor...

ThisNode  must have only: 
   Staticmodel (and if needed right oriented with additional child node)

and parent of "ThisNode" may have RB and basic collision shape.
RB must have a mass > 0
Angular factor must set to 0 to avoid rotations
in this situation you do your orientation to target only with "ThisNode" ->LockAt ( )
and movement/scale(not rotations!) only with parent of "ThisNode"[/quote]

You're confusing me. From the code shown. There is one node with staticmodel. The other components are not physical so it should not affect the node.

ThisNode->Component(StaticModel,RigidBody, CollisonShape matching the size of the StaticModel) (has no child nodes)  with Mass > 0 and AngularVelocity=1  Physics can affect rotation.

If I apply impulses everything works fine.

 Now if I set the rotation for for example
  Rotate (CurrentRotation * Quaternion(+1degree, on Y axis). It works 

If I try a more complicated one to target another spot.
That's where I am having problems. It's improperly calculating the proper which I need to make the equation work.

-------------------------

vivienneanthony | 2017-01-02 01:07:33 UTC | #6

[quote="codingmonkey"]>ThisNode rotation it jumps outside the collision boxes and disappear.

Maybe somewhere you have forgotten world biggest rigidbody enabled ? And this little ships's RB just placed within it, and what why it jumps I guessing.

Anyway, is your's "ThisNode" have rigidbody component? It must do not have it, RB only for parent of "ThisNode" for basic colliding with wall and floor...

ThisNode  must have only: 
   Staticmodel (and if needed right oriented with additional child node)

and parent of "ThisNode" may have RB and basic collision shape.
RB must have a mass > 0
Angular factor must set to 0 to avoid rotations
in this situation you do your orientation to target only with "ThisNode" ->LockAt ( )
and movement/scale(not rotations!) only with parent of "ThisNode"[/quote]

This is a video with the LookAt pointed to Vecto3(2.0f,2.0f,2.0f)

[youtube.com/watch?v=GyHkC0e ... e=youtu.be](https://www.youtube.com/watch?v=GyHkC0e5pFk&feature=youtu.be)

As I mentioned.

-------------------------

