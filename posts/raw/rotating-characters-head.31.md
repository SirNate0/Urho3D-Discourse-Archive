Mike | 2017-01-02 00:57:31 UTC | #1

Here is piece of code to make a character head follow a target:

In this example Jack is the character and characterNode is the target to follow.

In angel script:
[code]
	Skeleton@ skeleton = model.skeleton;
	skeleton.GetBone("Bip01_Head").animated = false;
	Node@ headNode = Jack.GetChild("Bip01_Head", true);
	headNode.LookAt(characterNode.position, Vector3(0.0f, 1.0f, 0.0f))
	headNode.rotation = headNode.rotation * Quaternion(90.0f, Vector3(0.0f, 1.0f, 0.0f)); // Yaw
	headNode.rotation = headNode.rotation * Quaternion(90.0f, Vector3(0.0f, 0.0f, 1.0f)); // Pitch
[/code]
In lua:
[code]
	local skeleton = jackNode:GetComponent("AnimatedModel").skeleton
	skeleton:GetBone("Bip01_Head").animated = false -- Disable head animation
	local headNode = Jack:GetChild("Bip01_Head", true)
	headNode:LookAt(characterNode.position, Vector3(0, 1, 0))
	headNode.rotation = headNode.rotation * Quaternion(90, Vector3(0, 1, 0)) -- Yaw
	headNode.rotation = headNode.rotation * Quaternion(90, Vector3(0, 0, 1)) -- Pitch
[/code]
Please note that you may have to tweak the Quaternion angle (90) to match your character.

-------------------------

cadaver | 2017-01-02 00:57:31 UTC | #2

Thanks for sharing, this might be a nice addition to the CharacterDemo (eg. tilt head when moving camera look direction up/down in 3rd person mode.)

-------------------------

friesencr | 2017-01-02 00:57:31 UTC | #3

We could spawn a bunch of jacks like in the old TestScene.as and have a bunch of jacks watching.  super. creepy.

-------------------------

