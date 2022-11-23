VladBolotov | 2019-10-17 11:02:12 UTC | #1

Hello. I was playing around with Urho animation system. I want to animate grabber (Open/Close animation). But I am stuck with weird behavior: in blender all animation looks good for me, but when I am trying to export animation and model to Urho only right part of mesh is moving.

Here is video: https://youtu.be/XwktXtbv_B0

Here is blend file and exported data: https://drive.google.com/file/d/1y6zX8azHHd5uoWABFJ9MnWDFggycagXx/

Here is how I added mesh and animation into Urho:
```C++
//! Create the Grabber
        {
            m_grabberNode = m_scene->CreateChild("Grabber");
            m_grabberNode->SetPosition(m_boxNode->LocalToWorld(Urho3D::Vector3(0.0f, 0.0f, 0.0f)));

            auto grabberObject = m_grabberNode->CreateComponent<Urho3D::AnimatedModel>();
            m_grabberNode->CreateComponent<Urho3D::AnimationController>();

            grabberObject->SetModel(cache->GetResource<Urho3D::Model>("Models/Grabber.mdl"));
            grabberObject->ApplyMaterialList("Materials/Grabber.txt");
            grabberObject->SetCastShadows(true);


            for (auto i = 0; i < grabberObject->GetSkeleton().GetNumBones(); ++i) {
                auto bone = grabberObject->GetSkeleton().GetBone(i);
                auto boneNode = bone->node_;

                auto boneRigidBody = boneNode->CreateComponent<Urho3D::RigidBody>();
                boneRigidBody->SetTrigger(true);
                boneRigidBody->SetFriction(1.0f);
                boneRigidBody->SetMass(0.0f);
                boneRigidBody->SetLinearDamping(0.1f);
                boneRigidBody->SetAngularDamping(0.1f);
                boneRigidBody->SetCollisionLayer(1);
                auto boneCollisionShape = boneNode->CreateComponent<Urho3D::CollisionShape>();
                boneCollisionShape->SetBox(bone->boundingBox_.Size() * 0.7f, bone->boundingBox_.Center());
            }

        }
```

```C++
//! Animate the Grabber
{
  if (Space Pressed)) {
       m_grabberOpened = !m_grabberOpened;
       auto animator = m_grabberNode->GetComponent<Urho3D::AnimationController>(true);
       if (m_grabberOpened) {
          animator->PlayExclusive("Animation/GrabberOpen.ani", 0, false, 0.5f);
          } else {
              animator->PlayExclusive("Animation/GrabberIDLE.ani", 0, false, 0.5f);
          }
  }
}
```


Blender v2.77 with Blender to Urho3D export plugin from master branch (branch for 2.8 does not work for me).

-------------------------

Modanung | 2019-10-17 04:36:23 UTC | #2

I think you will have to add a *root bone* to your armature - a bone to which the other bone chains would be parented - for the animation controller to traverse all branches of the tree.

-------------------------

Valdar | 2019-10-17 04:25:48 UTC | #3

You *may* need a root bone, but you have an Armature as the base, which I think should serve the same purpose. 
Did you tick the box for "Apply modifers" before exporting? It looks like you have an Armature modifier that you haven't 'applied' to the model. Worth a try if you haven't.
Another thing you could try, just to troubleshoot, is to export to FBX and then use ASSIMP to convert to .mdl and see if you get the same results (I think you'll need to change the FBX export setting of Armature from 'Null' to 'Root')

-------------------------

VladBolotov | 2019-10-17 04:36:20 UTC | #4

@Modanung @Valdar  
Thank you, guys. Creating the Root armature did the trick.

-------------------------

