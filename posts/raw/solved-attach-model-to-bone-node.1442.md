gabdab | 2017-01-02 01:07:44 UTC | #1

How do I set weapon  rotation to match hand's bone rotation ?
I get to attach nodes but rotation is wrong .

-------------------------

cadaver | 2017-01-02 01:07:44 UTC | #2

Create a separate weapon node into which you create the weapon model component, and parent it to the bone. Then adjust its local rotation. I don't know necessarily better method than trial and error to getting it oriented properly, though. Best would be if the model had been authored so that the hand bone's Z axis already points to the desired forward direction.

-------------------------

gabdab | 2017-01-02 01:07:44 UTC | #3

Authored inside the editor ?

this works no problem , but rotations indeed :
[code]    //bow
		handBoneNode = node_model->GetChild("Bone.001", true);//rob
		    //water_gun
    bow=globals::instance()->scene->CreateChild("bow");
    
    gs->nodes.push_back(bow);
//		bow->Pitch(-90);
//		bow->Roll(-90);
//				bow->Yaw(90);
		handBoneNode->AddChild(bow);[/code]

-------------------------

cadaver | 2017-01-02 01:07:44 UTC | #4

Authored in the 3D modeling program.

-------------------------

gabdab | 2017-01-02 01:07:44 UTC | #5

The editor works fine for such adjustments , but 
how do you load a xml node as exported from the editor ?
[SOLVED] by manually setting attached node rotation (quaternion) as showed by the editor , after tweaking position and rotation of the model .

-------------------------

