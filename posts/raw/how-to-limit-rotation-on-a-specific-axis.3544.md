crisx | 2017-09-10 15:24:47 UTC | #1

Hi
I'm trying to make a windmill wings model rotate on a axis, here's the model when imported in the editor
![Image2|690x362](upload://qLMiu0eEhni8nTScxcSOQlg3CMA.jpg)

I defined an angular velocity (2.0,0.0,0.0), it effectively make the wings rotate on the x axis (the wooden rod of the model)

![Image3|690x357](upload://3X0JhHkPjWGNs5UXe5aUVm67kJi.jpg)

However, I want to rotate the node on the y axis by 20.0, like this (I'm working on a 2D plateforming game and use 3D models for scenary) and have the wings rotate without the x axis changing so that the wooden rod stay parallel to the ground

![Image4|690x388](upload://dSU88G1rYhJj5T1dMZL0M5w6KuV.jpg)

But the rotation is making the wooden rod goes up and down :confused: :
![Image5|690x357](upload://czHUlONU2GRmnl5vSQnGoenmUeE.jpg)

I joined the scene and the model here
https://ufile.io/1et4m

I'm not sure if I could use a constraint or something

-------------------------

1vanK | 2017-09-08 14:10:29 UTC | #2

angularFactor?

+20 chars

-------------------------

crisx | 2017-09-08 14:50:30 UTC | #3

I tried with an angular factor at (0.0,0.0,1.0) but it doesn't seem to make a difference

-------------------------

Eugene | 2017-09-08 16:31:26 UTC | #4

You could try a constraint, but the task looks like misuse of dynamic RigidBody.

-------------------------

crisx | 2017-09-08 16:55:01 UTC | #5

Is there a way to do what I'm looking for without using a RigidBody?
I tried using an Attribute Animation on the node but I've got the same problem, I'm not very familiar with manipulating models right now, in Blender there's a 'Limit Rotation' constraint to restrict the rotation on certain axis, that's what I'm looking for

![Image2|355x500](upload://gfoyCmESt4eiJPyzjKzakKdHLXi.jpg)

-------------------------

Eugene | 2017-09-08 17:46:41 UTC | #6

What exactly do you want to reach?
Something like `node.Rotate(Quaternion(timeStep*ang, 0, 0))` somewhere in Update will make you model rotate around X axis.

-------------------------

crisx | 2017-09-13 12:14:04 UTC | #7

I would like to change the model's angle, and apply a rotation while maintaining the 'rod' (the wooden part) parallel to the world's x axis, it's not that easy to explain...

here's the scene and the model
https://ufile.io/5agam

I think there's a constraint for this but I must be doing something wrong

-------------------------

Modanung | 2017-09-15 08:28:57 UTC | #8

Like @Eugene said... doesn't this do exactly that?
https://github.com/Modanung/WindmillComponent/blob/master/windmill.cpp#L30

-------------------------

crisx | 2017-09-15 08:29:59 UTC | #9

Sorry my bad, I made a mistake when I tried it, works like a charm!

Thanks guys

-------------------------

