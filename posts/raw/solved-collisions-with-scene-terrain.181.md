DasUberBlade | 2017-01-02 00:58:41 UTC | #1

Hello everyone, I am having a small problem registering collisions with terrain that is present in the game scene. I have a class and it has done the following in its Init function which is called on initialization:

[code]SubscribeToEvent("NodeCollision", "NodeCollision");[/code]

And in NodeCollision:

[code]	void NodeCollision(StringHash eventType, VariantMap& eventData)
	{
		Node@ otherBody = eventData["OtherNode"].GetNode();
			
		Print("Collided with " + otherBody.name);
	}[/code]

Now the function prints out when it collides with nodes it hits but for some reason does not print out anything hit if it comes in contact with the terrain. It is worth noting the terrain is large and there are multiple nodes for it however each section has a Terrain component, a Collision Shape of Terrain, and a RigidBody that is on collision layer 1 and has a mask of -1 which is consistent with all other objects being made. 

Any suggestions on why it is not reporting a terrain collision? The class I'm speaking of manages a scriptObject which also has a rigid body and collision shape so the nodeCollision should be handled when it comes in contact with anything.

-------------------------

cadaver | 2017-01-02 00:58:42 UTC | #2

Welcome!

Now you're subscribing to node collisions sent by any node. As your class represents a single game object you should register to its own node's collision events only.

Also, it shouldn't make a difference, but GetNode() from VariantMap is deprecated. You should be able to call GetPtr() and it returns a handle which can be cast to a Node. Testing with the VehicleDemo script briefly (I disabled the wheel collision shapes so that the vehicle would touch the ground) I didn't have problems with registering hits to the terrain.

[code]
SubscribeToEvent(node, "NodeCollision", "HandleNodeCollision");

void HandleNodeCollision(StringHash eventType, VariantMap& eventData)
{
    Node@ node = eventData["OtherNode"].GetPtr();
    Print("Collided with " + node.name);
}
[/code]

-------------------------

DasUberBlade | 2017-01-02 00:58:42 UTC | #3

Thanks, 

I changed my NodeCollisions function to be like yours however I'm still not getting any hits from the terrain what suggestions might you have? Is there something wrong with the scene file, maybe something not being exported by the editor?

-------------------------

DasUberBlade | 2017-01-02 00:58:42 UTC | #4

If it's worth anything I've managed to get an error out of the function, 

[code]ERROR: Null event sender for event 9F786690, handler HandleNodeCollision[/code]

Any idea what this is?

-------------------------

DasUberBlade | 2017-01-02 00:58:42 UTC | #5

Issue was the object didn't have a mass  :blush: once it had a mass everything was fine.

-------------------------

