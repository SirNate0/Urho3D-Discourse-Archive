crisx | 2017-09-10 15:24:21 UTC | #1

Hello

I'm trying to rotate a model around an axis (windmill wings), here's the model as imported without any change, the rotation works perfectly fine I define an angular velocity:
![Image2|666x500](upload://rLTWE0k51iQAIJLctoFYrFwdz2V.jpg)

I defined a second node with the same height and used LookAt, it effectively turns the wings in the desired direction:
![Image3|669x500](upload://3FppVSTEC3w7tnYzPZuB0Fgp7O9.jpg)

But then when I apply an angular velocity, the wings rotate around a point, going up and down. I tried to define a constraint but it move the second node, and if I make the second node body static (no mass), the model doesn't move at all
![Image5|666x500](upload://1RK2eaEXR2eBd1oaYPVVbCRWRfx.jpg)

Here's the code I used:

                    AnimatedModel* wheelObject = tileNode->CreateComponent<AnimatedModel>();
					wheelObject->SetModel(cache->GetResource<Model>("Models/WindMillWings.mdl"));
					wheelObject->SetCastShadows(true);
					wheelObject->SetMaterial(0, cache->GetResource<Material>("Materials/Windmill/Wood.xml"));
					wheelObject->SetMaterial(1, cache->GetResource<Material>("Materials/Windmill/Cloth.xml"));

					RigidBody * Body = tileNode->CreateComponent<RigidBody>();
					CollisionShape * Shape = tileNode->CreateComponent<CollisionShape>();
					//Shape->SetCylinder(0.25, 1.6,Vector3(0.5,0.0,0.0),Quaternion(90.0));
					Shape->SetSphere(1.0);
					Body->SetMass(0.1f);
					Body->SetGravityOverride(Vector3(0.0, 0.0, 0.0));
					Body->SetUseGravity(false);
					Body->SetLinearDamping(0.0f);
					Body->SetAngularDamping(0.0f);
					Body->SetAngularVelocity(Vector3(2.0, 0.0, 0.0));
					Body->SetCollisionLayer(1);

					Node * anchorNode = sceneGame_->CreateChild();
					anchorNode->SetPosition(Vector3(tileNode->GetPosition().x_ + 2.0, tileNode->GetPosition().y_, tileNode->GetPosition().z_ +5.0));
					RigidBody * anchorBody = anchorNode->CreateComponent<RigidBody>();
					CollisionShape * anchorShape = anchorNode->CreateComponent<CollisionShape>();
					anchorShape->SetSphere(1.0);
					anchorBody->SetMass(0.1f);
					anchorBody->SetUseGravity(false);
					tileNode->LookAt(anchorNode->GetPosition());
					
					Constraint* wingsConstraint = tileNode->CreateComponent<Constraint>();
					wingsConstraint->SetConstraintType(CONSTRAINT_HINGE);
					wingsConstraint->SetOtherBody(anchorBody);
					wingsConstraint->SetWorldPosition(tileNode->GetPosition());
					wingsConstraint->SetAxis(Vector3::UP);
					wingsConstraint->SetDisableCollision(true);
					
And the model:
https://ufile.io/s6hhx

I tried used a rotation attribute animation but I've got the same problem
It's probably not that complicated but I've been trying to fix that for almost one day :sunglasses:
thanks

-------------------------

hicup_82017 | 2017-09-06 14:37:06 UTC | #2

I found the following from Urho Samples and Documentation.

**To Set rigid body rotation with rotation of speed 20, in world space.** 
Rigid Body->SetRotation(Quaternion(0.0f, 20* timeStep, 0.0f))
I could not see how to put the rotation in parent space from bullet.

**To set rotation of node, with speed 20,**
from billboards Sample line 302,
for world rotation, 
lightNodes[i]->Rotate(Quaternion(0.0f, 20 * timeStep, 0.0f), TS_WORLD);
for local rotation,
lightNodes[i]->Rotate(Quaternion(0.0f, 20 * timeStep, 0.0f), TS_LOCAL);

**Note:** All these target only Y axis.

-------------------------

Modanung | 2017-09-08 16:48:42 UTC | #3

Try:
```
Body->ApplyTorqueImpulse(tileNode->GetRight() * smallFloat);
```
Instead of setting the angular velocity.

-------------------------

crisx | 2017-09-08 17:14:22 UTC | #4

I tried, but I've got the same behavior

-------------------------

Modanung | 2017-09-11 02:01:51 UTC | #5

Like @Eugene [said](https://discourse.urho3d.io/t/how-to-limit-rotation-on-a-specific-axis/3544/4?u=modanung), using a RigidBody for this purpose could be considered overkill. As long as there needn't be any interaction with other objects.
I made a component using the same windmill model:
https://github.com/Modanung/WindmillComponent

Because of the windmill model's orientation, LookAt() behaves illogical. I think it would make more sense for it to spin around its Z axis (in Urho).

-------------------------

