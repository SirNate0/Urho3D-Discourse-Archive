crisx | 2017-08-25 15:50:08 UTC | #1

Hello,

I'm a beginner with both Blender and the engine, and I'm having difficulties with some animated models.
I'm successfully exporting the blender model to .fbx with the default options, and using AssetImporter to create both the .mdl files and .ani files, the generated model works just fine, but sometimes none of the animations seems to do anything

Here's the sample of code I'm using

    				AnimatedModel* Object = tileNode->CreateComponent<AnimatedModel>();
					RigidBody* Body = tileNode->CreateComponent<RigidBody>();
					CollisionShape* Shape = tileNode->CreateComponent<CollisionShape>();
					Shape->SetSphere(1.0f);
					Body->SetMass(0.1f);
					Body->SetGravityOverride(Vector3(0.0, 0.0, 0.0));
					Body->SetUseGravity(false);
					Body->SetLinearDamping(0.0f);
					Body->SetAngularDamping(0.0f);
					Body->SetAngularVelocity(Vector3(0.0, 0.0, 0.0));
					Body->SetCollisionLayer(1);
					Object->SetModel(cache->GetResource<Model>("Models/Train.mdl"));
					Object->SetCastShadows(true);
					Object->SetMaterial(cache->GetResource<Material>("Materials/Stone.xml"));
					AnimationController* Animated = tileNode->CreateComponent<AnimationController>();
					Animated->Play("Models/Train_MiddleWheelCDABigWhellIPO.ani", 0, true, 0.1f);
					Object->SetAnimationEnabled(true);
					//wheelAnimated->SetWeight("Models/Train_MiddleWheelCDABigWhellIPO.ani", 1.0f);
					Animated->SetSpeed("Models/Train_MiddleWheelCDABigWhellIPO.ani", 4.0);

Here's one of the models I'm having issues with:
https://ufile.io/0uzvy

Any help is welcomed :grinning:

-------------------------

1vanK | 2017-08-25 12:02:44 UTC | #2

 https://github.com/reattiva/Urho3D-Blender

-------------------------

Modanung | 2017-08-25 16:28:40 UTC | #3

What @1vanK  said.
Also you may want to consider joining the meshes and redoing the animation using an armature. This would make it possible to add the train as a single animated model that uses one animation.
Nice train though. It'll look great with PBR. [spoiler]Quick blender render:[/spoiler]
![image|589x360](upload://virYLNoSwfNrzPg9oHiwp2td4DM.jpg)

You'll have to recreate the particle effect using the Urho Editor, btw. It will not be exported. 

And welcome to the forums! :confetti_ball:

-------------------------

crisx | 2017-08-28 08:37:44 UTC | #4

[quote="Modanung, post:3, topic:3490"]
Also you may want to consider joining the meshes and redoing the animation using an armature.
[/quote]

OK I get it, I'll try that.
Thanks!

-------------------------

crisx | 2017-08-29 15:03:50 UTC | #5

I was wondering, is it possible to play an animation associated to a mesh, not only to an armature? I have several independent animations on different meshes of the model:

![Image2|690x330](upload://zhKXjlNmjpyX5GJbGKbpaOsAEk8.png)

The .ani files are successfully created with AssetImporter.

Train_MiddleWheel.001CDABigWhellIPO.001.ani
Train_MiddleWheel.001CDABigWhellIPO.002.ani
Train_MiddleWheel.001CDABigWhellIPO.ani
Train_MiddleWheel.002CDABigWhellIPO.001.ani
Train_MiddleWheel.002CDABigWhellIPO.002.ani
Train_MiddleWheel.002CDABigWhellIPO.ani
Train_MiddleWheelCDABigWhellIPO.001.ani
Train_MiddleWheelCDABigWhellIPO.002.ani
Train_MiddleWheelCDABigWhellIPO.ani
Train_SmallWheel2.001CDABigWhellIPO.001.ani
Train_SmallWheel2.001CDABigWhellIPO.002.ani
Train_SmallWheel2.001CDABigWhellIPO.ani
Train_SmallWheel2CDABigWhellIPO.001.ani
Train_SmallWheel2CDABigWhellIPO.002.ani
Train_SmallWheel2CDABigWhellIPO.ani

When I try to play them, nothing happens, I must do something wrong. I found the instructions related to this topic in the documentation here:

https://urho3d.github.io/documentation/1.5/_skeletal_animation.html

It says:

"Animations can also be applied outside of an AnimatedModel's bone hierarchy, to control the transforms of named nodes in the scene. The AssetImporter utility will automatically save node animations in both model or scene modes to the output file directory.

Like with skeletal animations, there are two ways to play back node animations:

Instantiate an AnimationState yourself, using the constructor which takes a root scene node (animated nodes are searched for as children of this node) and an animation pointer. You need to manually advance its time position, and then call Apply() to apply to the scene nodes.
Create an AnimationController component to the root scene node of the animation. This node should not contain an AnimatedModel component. Use the AnimationController to play back the animation just like you would play back a skeletal animation."

However i'm confuse about what is the proper code to do this, here's what I tried:

    				AnimatedModel* Object = tileNode->CreateComponent<AnimatedModel>();
					RigidBody* Body = tileNode->CreateComponent<RigidBody>();
					CollisionShape* Shape = tileNode->CreateComponent<CollisionShape>();
					Shape->SetSphere(1.0f);
					Body->SetMass(0.1f);
					Body->SetGravityOverride(Vector3(0.0, 0.0, 0.0));
					Body->SetUseGravity(false);
					Body->SetLinearDamping(0.0f);
					Body->SetAngularDamping(0.0f);
					Body->SetAngularVelocity(Vector3(0.0, 0.0, 0.0));
					Body->SetCollisionLayer(1);
					Object->SetModel(cache->GetResource<Model>("Models/Train.mdl"));
					//wheelObject->SetModel(cache->GetResource<Model>("Models/castleguard.mdl"));
					Object->SetCastShadows(true);
					Object->SetMaterial(cache->GetResource<Material>("Materials/Stone.xml"));
					Animation* trainAnimation = cache->GetResource<Animation>("Models/Train_MiddleWheel.001CDABigWhellIPO.001.ani");
					trainAnimation->SetName("Train_MiddleWheel");
					AnimationState* state = Object->AddAnimationState(trainAnimation);
					if (state)
					{
						state->SetWeight(1.0f);
						state->SetLooped(true);
						state->SetTime(Random(trainAnimation->GetLength()));
					}
					AnimationController* Animated = tileNode->CreateComponent<AnimationController>();
					Animated->SetSpeed("Train_MiddleWheel", 1.0);
					Animated->Play("Train_MiddleWheel", 0, true, 0.1f);

Here's the model files created with AssetImporter:
https://ufile.io/62h4o

If you have any idea :grin:

thanks

-------------------------

Modanung | 2017-08-30 11:01:53 UTC | #6

I have no personal experience with this.

Have you seen this thread?
https://discourse.urho3d.io/t/export-animated-node-transforms-to-urho3d/1067

-------------------------

crisx | 2017-08-30 13:53:32 UTC | #7

I'll take a look

thanks

-------------------------

johnnycable | 2017-08-31 19:53:51 UTC | #8

I dug this up from somewhere:

    auto animateThem = [&]() {

        // Create triangle animation
        SharedPtr<ObjectAnimation> triangleAnimation(new ObjectAnimation(context_));

        // Create triangle position animation
        SharedPtr<ValueAnimation> positionAnimation(new ValueAnimation(context_));
        // Use spline interpolation method
        positionAnimation->SetInterpolationMethod(IM_NONE);
        // Set spline tension
        positionAnimation->SetSplineTension(0.7f);
        positionAnimation->SetKeyFrame(0.0f, Vector3(1, 1, -1));
        positionAnimation->SetKeyFrame(1.0f, Vector3(-1, 1, -1));
        positionAnimation->SetKeyFrame(2.0f, Vector3(-1, -1, -1));
        positionAnimation->SetKeyFrame(3.0f, Vector3(1, -1, -1));
        positionAnimation->SetKeyFrame(4.0f, Vector3(1, 1, -1));

        // Set position animation
        triangleAnimation->AddAttributeAnimation("Position", positionAnimation);

        // Create spinning triangle animation
        SharedPtr<ValueAnimation> rotationAnimation(new ValueAnimation(context_));
        rotationAnimation->SetInterpolationMethod(IM_NONE);
        rotationAnimation->SetKeyFrame(0.0f, Quaternion(0.f));
        rotationAnimation->SetKeyFrame(1.0f, Quaternion(90));
        rotationAnimation->SetKeyFrame(2.0f, Quaternion(180));
        rotationAnimation->SetKeyFrame(3.0f, Quaternion(270));
        rotationAnimation->SetKeyFrame(4.0f, Quaternion(360));

        // Set triangle rotation animation
        triangleAnimation->AddAttributeAnimation("Rotation", rotationAnimation);

        // Apply light animation to light node
        triangleNode->SetObjectAnimation(triangleAnimation);

    };

you can animate not only by skeletons, but also using attribute animation. The concept is that you simply turn a train wheel around its axis by code...

-------------------------

crisx | 2017-09-01 16:48:51 UTC | #9

Thanks, I will check that.
It doesn't seems to apply to StaticModel or AnimatedModel classes, no?
So far, I've only been able to run model animations with a skeleton, and I'm still struggling to animate just parts of the model directly with the engine code.
I'll check this anyway :sunglasses:

-------------------------

johnnycable | 2017-09-01 17:10:43 UTC | #10

Yes, this is [attribute animation](https://urho3d.github.io/documentation/1.6/_attribute_animation.html), used to animate everything not-skeleton...

-------------------------

