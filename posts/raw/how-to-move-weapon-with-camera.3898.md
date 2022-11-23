Zyie | 2017-12-29 21:15:52 UTC | #1

Hi, 

I'm new to Urho and I'm trying to creating an FPS game and i was wondering if anyone knows how you make the gun stay pointing towards the center of the screen when you rotate the camera node.

![FPS Example|690x388](upload://y0J7vqXxFuFVDaVUz9ryadYr2GE.jpg)

This is what I'm looking to do

if anyone can help it would be greatly appreciated.

-------------------------

Modanung | 2017-12-30 01:49:34 UTC | #2

Create the gun's `Node` as a child of the camera node.

Is that enough information?

Also, welcome to the forums! :confetti_ball:

-------------------------

Zyie | 2017-12-29 21:46:21 UTC | #3

@Modanung i tried that but the weapon seemed to disappear  

    Node* gunNode = mCameraNode->CreateChild("Gun1");
    gunNode->SetPosition(Vector3(0.0f, 0, -5.0f));
    gunNode->SetScale(Vector3(20.02f, .02f, .02f));

    StaticModel* gunObject = gunNode->CreateComponent<StaticModel>();
    gunObject->SetModel(cache->GetResource<Model>("Models/Gun.mdl"));
    gunObject->ApplyMaterialList();
    RigidBody* gunBody = floorNode->CreateComponent<RigidBody>();

This is the code I am using to create the weapon

-------------------------

spwork | 2017-12-29 21:48:46 UTC | #4

this looks like Unturned

-------------------------

Modanung | 2017-12-29 21:50:59 UTC | #5

[quote="Zyie, post:3, topic:3898"]
gunNode-&gt;SetPosition(Vector3(0.0f, 0, -5.0f));
gunNode-&gt;SetScale(Vector3(20.02f, .02f, .02f));
[/quote]

Here you are moving the gun node back (possibly out of sight) and scaling it down to a horizontal line.

Also I don't think your gun needs physics/rigidbody (as it's being held).

-------------------------

Zyie | 2017-12-29 22:01:23 UTC | #6

@Modanung
I have removed the rigidbody and tried setting the position to both negative and positive howver it still does not appear.

It works perfectly fine when i make the box the child of the scene 

    Node* gunNode = mScene->CreateChild("Gun1");
    gunNode->SetPosition(Vector3(0, 0, 5));      //gunNode->SetPosition(Vector3(0, 0, -5)); 
    gunNode->SetScale(Vector3(1, 1, 1));

-------------------------

Dave82 | 2017-12-29 22:17:35 UTC | #7

Are you sure the scale value of 20 isn't too big ? Maybe the camera is inside the weapon.

-------------------------

Zyie | 2017-12-29 22:19:22 UTC | #8

@Dave82
Ive changed it to 1 and to .1f and it still doesnt show

-------------------------

Dave82 | 2017-12-29 22:35:42 UTC | #9

Well i have some other ideas
 - Make sure your model's pivot is correct.
 - Are the model show up if you create it as an independent node ? (child of scene)
 - Try to create it as a child of the camera but add some small code for moving the gun node with some keys in different directions (WASD perhaps and up down for Y movement.)

BTW i know how iritating this is... i had the same problem when i was making my fps controller. It takes time to adjust the rotation/position/scale offset

-------------------------

Zyie | 2017-12-29 23:09:43 UTC | #10

Ok so ive changed the model to the default box to rule out the models pivot being wrong.

The gun model and the box both show up when made a child of the scene

I used the code below to make the object move

`gunNode->SetPosition(Vector3(gunNode->GetPosition().x_, gunNode->GetPosition().y_, gunNode->GetPosition().z_ + .01f));`

I could not see any gun or box moving when using this as part of the camera child

-------------------------

lezak | 2017-12-29 23:55:43 UTC | #11

My suggestion would be to use the editor - create node with camera component, add gun node as child, set models etc, and then just use handles to find right offset for the gun node. Note: when You select camera component in scene hierarchy, there is a small preview window in right-bottom corner.

-------------------------

Zyie | 2017-12-30 01:48:54 UTC | #12

After many hours i now feel stupid. I didn't make the camera a child of the scene.

Fixing that fixed the model not appearing

-------------------------

