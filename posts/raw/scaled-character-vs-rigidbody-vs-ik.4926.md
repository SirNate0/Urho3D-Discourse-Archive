Leith | 2019-02-16 04:51:23 UTC | #1


I noticed when I tried to apply a ragdoll armature to one of my AnimatedModels, that the physics bodies were receiving Scale from the Nodes associated with Bones in the Skeleton - they receive "Joint Scaling".
Since I was scaling my model down 100x via an "adjustment node" near the root, this meant that my physics shapes, when attached to the model, shrank to the size of match sticks.
For the character's outer collision hull, I was able to avoid this by attaching directly to the character's root node, which is just above the adjustment node, but I ignored the issue of ragdoll segments, instead I just disabled relevant code, and turned my attention elsewhere.

Recently, I tried attaching IK to the animated model's legs, and noticed that debug-drawing was not displaying at all - I believe this was also caused by my scaling node.

I'd like to know if I am correct: firstly, do rigidbodies receive scaling from parent nodes as they certainly appear to, and secondly, does scaling also affect the IK system?

If the answer is yes to both of these questions, I will be tempted to extend the AssetExporter to provide a means to scale geometry by a given value, so I can get rid of the scaling node, without having to manually load every affected model into a modelling app, apply scale, and export it again (given that I'd still need to run the exported model back through AssetExporter, it seems like a redundant step).

[EDIT]
For rigidbodies, I discovered that I can add yet another "adjustment node" as a child of a bone node, which "cancels" the previous scaling, and attach my rigidbody to that node, this solves the issue of rigidbodies inheriting scale, but it seems like a poor solution to the problem. Have not yet tested the same concept on the IK system, but I suspect it will be a viable workaround there as well.

[EDIT]
It's a shame Urho3D's CollisionShape component does not implement Bullet's "Local Scale" - this would be preferable to additional "descaling" nodes.

-------------------------

Leith | 2019-02-16 03:53:21 UTC | #2

Here's the experimental code I am using for setting up ragdoll bodyparts on an animated model.
The Ragdoll Sample only creates the ragdoll shapes at the very last moment, and it assumes a lot about the pose of the model.
By creating the rigidbodies early, and driving them in kinematic mode, the ragdoll (when activated) will inherit the existing pose of the armature.
I have some other reasons for wanting to create my ragdoll armature in advance of ragdoll mode being enabled - One is that I can tell which bodypart was hit during an attack, and apply damage and additive "twitching" to just the relevant region of the animated model. Another is that I can perform more accurate "foot-planting" by detecting collisions (and lack thereof) between the feet and the static world, rather than generating footfall events via animation triggers.
[code]
        void GamePlayState::CreateRagdollPart(Node* adjustNode, String boneName, ShapeType tshape, Vector3 size_, Vector3 pos_, Quaternion rot_)
        {
                        
            // Locate the Node associated with BodyPart (eg left thigh)
            Node* boneNode = adjustNode->GetChild(boneName,true);

            // Check for inherited scale on the bone node
            Node* descale = boneNode;
            Vector3 scale = descale->GetWorldScale();
            if(scale != Vector3(1,1,1))
            {
                // Create a child node to eliminate inherited scale
                descale = boneNode->CreateChild();
                descale->SetScale( Vector3(1,1,1) / descale->GetWorldScale() );
            }

            // Create rigidbody, and set non-zero mass so that the body becomes dynamic
            auto* body = descale->CreateComponent<RigidBody>();
            // Set the collision layer and mask
            body->SetCollisionLayerAndMask(CollisionFilter::NonPlayerCharacter, CollisionFilter::Static || CollisionFilter::PlayerCharacter);
            // Give the body some mass, or it won't move
            body->SetMass(1.0f);
            // Set body to Kinematic mode, so it follows Animations
            body->SetKinematic(true);
            // Only report collisions while body is "awake" (kinematic bodies never sleep...)
            body->SetCollisionEventMode(COLLISION_ACTIVE);
            // Set up the shape of the body
            auto* shape = descale->CreateComponent<CollisionShape>();
            if (tshape == SHAPE_BOX)
                shape->SetBox(size_, pos_, rot_);
            else
                shape->SetCapsule(size_.x_, size_.y_, pos_, rot_);

        }
[/code]
![legs|690x403](upload://65wALSYqXkVW73EDSyBR0n1LTZz.png)

-------------------------

Modanung | 2019-02-16 08:43:57 UTC | #3

It's a minor detail, but are you familiar of the constant `Vector3`'s like `Vector3::ONE` and `Vector3::RIGHT`?

-------------------------

Leith | 2019-02-16 08:45:30 UTC | #4

I didn't know about Vector3::ONE, must have missed that. I know about the cardinal directions, and zero.

-------------------------

TheComet | 2019-08-08 07:10:44 UTC | #5

[quote="Leith, post:1, topic:4926"]
does scaling also affect the IK system?
[/quote]

The IK solver reads and writes global positions/rotations to and from Urho's scene graph. Thus, scale is irrelevant. Internally the solver assumes the scale is 1.

-------------------------

Leith | 2019-08-08 08:25:49 UTC | #6

The IK debug drawing is wrong in a scaled armature.

-------------------------

TheComet | 2019-08-08 09:11:41 UTC | #7

https://github.com/urho3d/Urho3D/issues/2472

-------------------------

