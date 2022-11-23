GodMan | 2020-01-25 20:33:16 UTC | #1

I am using a spline path for my flying ai. I am having trouble getting the ai to look at each point as the node travels along the spline. Right now my node is traveling sideways. I am not that great with figuring out the Quaternions. 

     	Node* startNode;
    	Node* targetNode;
            SharedPtr<Node> flyingNode;

            flyingNode->LookAt(targetNode));

-------------------------

throwawayerino | 2020-01-25 21:27:34 UTC | #2

Are you setting it each update or just once? LookAt is basically a SetWorldRotation with some calculations under the hood.

-------------------------

GodMan | 2020-01-25 21:33:53 UTC | #3

I am setting it in the update,but my node is sideways as he travels to the targetnode.

-------------------------

GodMan | 2020-01-25 22:42:23 UTC | #5

Okay so I changed to this.
`flyingNode->LookAt(targetNode->GetWorldPosition() + flyingNode->GetWorldPosition() - Vector3(0.0f, 1.0f, 0.0f));`

This seems to be working. Not sure if this is the correct way to do this though.

**EDIT**
Nevermind it's not working. If I give the ai a new target it does not face that target node when traveling towards it.

-------------------------

Modanung | 2020-01-26 16:28:21 UTC | #6

Make sure your model is oriented properly and that you're using the correct transform space in your operations. Also the `Node` class has `WorldToLocal` and `LocalToWorld` functions that maybe be useful. Things like the vector dot product, cross product and projection functions might also be convenient to understand in these cases.

-------------------------

GodMan | 2020-01-26 17:11:46 UTC | #7

@Modanung I agree. I need to read up on how to calculate proper rotations.

-------------------------

throwawayerino | 2020-01-26 20:01:14 UTC | #8

did you try just `flyingNode->LookAt(targetNode->GetWorldPosition())`

-------------------------

GodMan | 2020-01-26 20:20:09 UTC | #9

Yes I tried that. I am using a debug line to show any issues. The line draws correctly. However my node is off by like 90 degrees.

-------------------------

GodMan | 2020-01-26 20:58:27 UTC | #10

Here is what I'm trying to do. I am making a hovering AI. I am trying to build upon the splinepath. I am trying to get it where as the node travels to each point he faces each point correctly. I used debug line to show the path. Notice node is facing the wrong way. I even removed any rotation from the node when I create it. 

![Screenshot_Sun_Jan_26_14_55_27_2020|690x291](upload://fMHaz4qZ4Sojcpfx3etuFuhCZc2.jpeg)

-------------------------

Modanung | 2020-01-26 21:46:55 UTC | #11

Could you add debug lines showing the node's transform space axes?

-------------------------

GodMan | 2020-01-27 00:54:35 UTC | #12

@Modanung How do I show the transform space axes? I'll gladly add that.

-------------------------

dertom | 2020-01-27 05:08:04 UTC | #13

[quote="GodMan, post:9, topic:5841"]
The line draws correctly. However my node is off by like 90 degrees.
[/quote]

The line draws in the right direction but the node with your model not? 
If that is the case you might need to rotate the the mesh itself for 90°. Are you using blender? Rotate in Edit-Mode or use 'apply rotation'

Another approach could be to add a parent node on which you use the lookAt calls and the childnode has the AnimModel but rotated 90°. 

A video about rotation (usually for unity but is true for urho as well and our calls are similar):
https://youtu.be/kYOtk5a6_x4

-------------------------

Modanung | 2020-01-27 11:44:47 UTC | #14

Indeed it is likely your asset is badly orientated. As you had already drawn a debug line I figured displaying the _direction_ of the node itself (as well as the path) to make this visible. But you could also have a good look at your model in the editor.

-------------------------

lezak | 2020-01-27 11:53:45 UTC | #15

[quote="GodMan, post:12, topic:5841"]
How do I show the transform space axes? I’ll gladly add that.
[/quote]

DebugRenderer->AddNode(Node*, float scale, bool depthtest)

-------------------------

GodMan | 2020-01-27 16:40:03 UTC | #16

Okay. Thanks guys. I will try these ideas, and post back.

-------------------------

GodMan | 2020-01-28 01:18:05 UTC | #17

Okay guys here is a screenshot: 
![Screenshot_Mon_Jan_27_17_02_39_2020|690x291](upload://8fn621uzTT4dyPdqsmhRWxl429C.jpeg) 

Since this model is from Halo. I know that Y is the Up axis and not Z. Everything appears to be right. It even shows the slight tilt the node has.

Also for future refrence for anyone. There was nothing wrong with the model. I believe the issue was because the models were create where the Y axis is up and not Z axis. Therefore urho3d may expect the model as Z axis up. So when using LookAt function the wrong axis is used as the forward facing. 


**EDIT:**

    sentinelparentNode = scene_->CreateChild("SentinelParentNode"); // This is a parent node no transformations on it.
    sentinel = sentinelparentNode->CreateChild("Sentinel"); //Then I attach the child node to parent node.

Then use the LookAt function to look at the target node.

-------------------------

