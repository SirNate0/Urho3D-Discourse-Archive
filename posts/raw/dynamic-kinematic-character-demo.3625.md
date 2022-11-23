ext1 | 2017-10-09 02:48:19 UTC | #1

Hello,

While exploring the [Character Demo](https://github.com/urho3d/Urho3D/tree/master/Source/Samples/18_CharacterDemo) I've ended up wanting a more "kinematic" movement (specially going up/down slopes), similar to raycast movement, but without losing the benefits of the dynamic character controller, the collision detection and physics overall.

After a lot of trial and error, I've managed to tinker the Character Demo and got pretty interesting results. The character no longer [bounces](https://discourse.urho3d.io/t/down-hill-movement-on-the-physics-simulation/3612) when going up/down a slope, neither slide when stopped, while still being able to jump and react to physics as usual (so it still respects angles, e.g.: will not climb steep walls).

Code that was changed from the original Character Demo (from Urho3D version 1.7):

Character.h - Line 63.

    //
    // Copyright (c) 2008-2017 the Urho3D project.
    //
    // Permission is hereby granted, free of charge, to any person obtaining a copy
    // of this software and associated documentation files (the "Software"), to deal
    // in the Software without restriction, including without limitation the rights
    // to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
    // copies of the Software, and to permit persons to whom the Software is
    // furnished to do so, subject to the following conditions:
    //
    // The above copyright notice and this permission notice shall be included in
    // all copies or substantial portions of the Software.
    //
    // THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
    // IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
    // FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
    // AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
    // LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
    // OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
    // THE SOFTWARE.
    //

    #pragma once

    #include <Urho3D/Input/Controls.h>
    #include <Urho3D/Scene/LogicComponent.h>

    using namespace Urho3D;

    const int CTRL_FORWARD = 1;
    const int CTRL_BACK = 2;
    const int CTRL_LEFT = 4;
    const int CTRL_RIGHT = 8;
    const int CTRL_JUMP = 16;

    const float MOVE_FORCE = 0.8f;
    const float INAIR_MOVE_FORCE = 0.02f;
    const float BRAKE_FORCE = 0.2f;
    const float JUMP_FORCE = 7.0f;
    const float YAW_SENSITIVITY = 0.1f;
    const float INAIR_THRESHOLD_TIME = 0.1f;

    /// Character component, responsible for physical movement according to controls, as well as animation.
    class Character : public LogicComponent
    {
        URHO3D_OBJECT(Character, LogicComponent);

    public:
        /// Construct.
        Character(Context* context);

        /// Register object factory and attributes.
        static void RegisterObject(Context* context);

        /// Handle startup. Called by LogicComponent base class.
        virtual void Start();
        /// Handle physics world update. Called by LogicComponent base class.
        virtual void FixedUpdate(float timeStep);

        /// Movement controls. Assigned by the main program each frame.
        Controls controls_;

        /* Stores the floor normal from a raycast down on the character location. */
        Vector3 floorNormal;

    private:
        /// Handle physics collision event.
        void HandleNodeCollision(StringHash eventType, VariantMap& eventData);

        /// Grounded flag for movement.
        bool onGround_;
        /// Jump flag.
        bool okToJump_;
        /// In air timer. Due to possible physics inaccuracy, character can be off ground for max. 1/10 second and still be allowed to move.
        float inAirTimer_;
    };

Character.cpp - Lines 78, 80, 88, 90 and 146.

    //
    // Copyright (c) 2008-2017 the Urho3D project.
    //
    // Permission is hereby granted, free of charge, to any person obtaining a copy
    // of this software and associated documentation files (the "Software"), to deal
    // in the Software without restriction, including without limitation the rights
    // to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
    // copies of the Software, and to permit persons to whom the Software is
    // furnished to do so, subject to the following conditions:
    //
    // The above copyright notice and this permission notice shall be included in
    // all copies or substantial portions of the Software.
    //
    // THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
    // IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
    // FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
    // AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
    // LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
    // OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
    // THE SOFTWARE.
    //

    #include <Urho3D/Core/Context.h>
    #include <Urho3D/Graphics/AnimationController.h>
    #include <Urho3D/IO/MemoryBuffer.h>
    #include <Urho3D/Physics/PhysicsEvents.h>
    #include <Urho3D/Physics/PhysicsWorld.h>
    #include <Urho3D/Physics/RigidBody.h>
    #include <Urho3D/Scene/Scene.h>
    #include <Urho3D/Scene/SceneEvents.h>

    #include "Character.h"

    Character::Character(Context* context) :
        LogicComponent(context),
        onGround_(false),
        okToJump_(true),
        inAirTimer_(0.0f)
    {
        // Only the physics update event is needed: unsubscribe from the rest for optimization
        SetUpdateEventMask(USE_FIXEDUPDATE);
    }

    void Character::RegisterObject(Context* context)
    {
        context->RegisterFactory<Character>();

        // These macros register the class attributes to the Context for automatic load / save handling.
        // We specify the Default attribute mode which means it will be used both for saving into file, and network replication
        URHO3D_ATTRIBUTE("Controls Yaw", float, controls_.yaw_, 0.0f, AM_DEFAULT);
        URHO3D_ATTRIBUTE("Controls Pitch", float, controls_.pitch_, 0.0f, AM_DEFAULT);
        URHO3D_ATTRIBUTE("On Ground", bool, onGround_, false, AM_DEFAULT);
        URHO3D_ATTRIBUTE("OK To Jump", bool, okToJump_, true, AM_DEFAULT);
        URHO3D_ATTRIBUTE("In Air Timer", float, inAirTimer_, 0.0f, AM_DEFAULT);
    }

    void Character::Start()
    {
        // Component has been inserted into its scene node. Subscribe to events now
        SubscribeToEvent(GetNode(), E_NODECOLLISION, URHO3D_HANDLER(Character, HandleNodeCollision));
    }

    void Character::FixedUpdate(float timeStep)
    {
        /// \todo Could cache the components for faster access instead of finding them each frame
        RigidBody* body = GetComponent<RigidBody>();
        AnimationController* animCtrl = node_->GetComponent<AnimationController>(true);

        // Update the in air timer. Reset if grounded
        if (!onGround_)
            inAirTimer_ += timeStep;
        else
            inAirTimer_ = 0.0f;
        // When character has been in air less than 1/10 second, it's still interpreted as being on ground
        bool softGrounded = inAirTimer_ < INAIR_THRESHOLD_TIME;

        // Update movement & animation
        //const Quaternion& rot = node_->GetRotation(); /* Removed */

        /* Calculate the floor angle with the floor normal and rotate the character with that angle so it can move on any direction and have vertical velocity. */
        /* Based on 1vanK's post: https://discourse.urho3d.io/t/solved-how-to-direct-a-character-parallel-to-the-ground/1285/5 */
        Quaternion floorAngle = Quaternion(Vector3(0.0f, 1.0f, 0.0f), floorNormal);
        Quaternion rot = floorAngle * Quaternion(node_->GetRotation());

        Vector3 moveDir = Vector3::ZERO;
        const Vector3& velocity = body->GetLinearVelocity();
        // Velocity on the XZ plane
        // Vector3 planeVelocity(velocity.x_, 0.0f, velocity.z_); /* Removed */

        /* Set the velocity on all directions so it can also have vertical velocity. */
        /* Special thanks for Eugene for pointing vertical velocity and for Carnalis from helping figure out this problem. */
        Vector3 planeVelocity(velocity);

        if (controls_.IsDown(CTRL_FORWARD))
            moveDir += Vector3::FORWARD;
        if (controls_.IsDown(CTRL_BACK))
            moveDir += Vector3::BACK;
        if (controls_.IsDown(CTRL_LEFT))
            moveDir += Vector3::LEFT;
        if (controls_.IsDown(CTRL_RIGHT))
            moveDir += Vector3::RIGHT;

        // Normalize move vector so that diagonal strafing is not faster
        if (moveDir.LengthSquared() > 0.0f)
            moveDir.Normalize();

        // If in air, allow control, but slower than when on ground
        body->ApplyImpulse(rot * moveDir * (softGrounded ? MOVE_FORCE : INAIR_MOVE_FORCE));

        if (softGrounded)
        {
            // When on ground, apply a braking force to limit maximum ground velocity
            Vector3 brakeForce = -planeVelocity * BRAKE_FORCE;
            body->ApplyImpulse(brakeForce);

            // Jump. Must release jump control between jumps
            if (controls_.IsDown(CTRL_JUMP))
            {
                if (okToJump_)
                {
                    body->ApplyImpulse(Vector3::UP * JUMP_FORCE);
                    okToJump_ = false;
                    animCtrl->PlayExclusive("Models/Mutant/Mutant_Jump1.ani", 0, false, 0.2f);
                }
            }
            else
                okToJump_ = true;
        }

        if ( !onGround_ )
        {
            animCtrl->PlayExclusive("Models/Mutant/Mutant_Jump1.ani", 0, false, 0.2f);
        }
        else
        {
            // Play walk animation if moving on ground, otherwise fade it out
            if (softGrounded && !moveDir.Equals(Vector3::ZERO))
                animCtrl->PlayExclusive("Models/Mutant/Mutant_Run.ani", 0, true, 0.2f);
            else
                animCtrl->PlayExclusive("Models/Mutant/Mutant_Idle0.ani", 0, true, 0.2f);

            // Set walk animation speed proportional to velocity
            animCtrl->SetSpeed("Models/Mutant/Mutant_Run.ani", planeVelocity.Length() * 0.3f);
        }

        /* Stops the character from sliding down when not moving. */
        /* From 1vanK's post: https://discourse.urho3d.io/t/improved-charactercontroller/3472 */
        if ( softGrounded && okToJump_ && moveDir == Vector3::ZERO) {
            body->SetUseGravity(false);
            body->SetLinearVelocity(Vector3::ZERO);
        } else {
            body->SetUseGravity(true);
        }

        // Reset grounded flag for next frame
        onGround_ = false;
    }

    void Character::HandleNodeCollision(StringHash eventType, VariantMap& eventData)
    {
        // Check collision contacts and see if character is standing on ground (look for a contact that has near vertical normal)
        using namespace NodeCollision;

        MemoryBuffer contacts(eventData[P_CONTACTS].GetBuffer());

        while (!contacts.IsEof())
        {
            Vector3 contactPosition = contacts.ReadVector3();
            Vector3 contactNormal = contacts.ReadVector3();
            /*float contactDistance = */contacts.ReadFloat();
            /*float contactImpulse = */contacts.ReadFloat();

            // If contact is below node center and pointing up, assume it's a ground contact
            if (contactPosition.y_ < (node_->GetPosition().y_ + 1.0f))
            {
                float level = contactNormal.y_;
                if (level > 0.75)
                    onGround_ = true;
            }
        }
    }

CharacterDemo.cpp - Lines 129, 141 and 348.

    //
    // Copyright (c) 2008-2017 the Urho3D project.
    //
    // Permission is hereby granted, free of charge, to any person obtaining a copy
    // of this software and associated documentation files (the "Software"), to deal
    // in the Software without restriction, including without limitation the rights
    // to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
    // copies of the Software, and to permit persons to whom the Software is
    // furnished to do so, subject to the following conditions:
    //
    // The above copyright notice and this permission notice shall be included in
    // all copies or substantial portions of the Software.
    //
    // THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
    // IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
    // FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
    // AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
    // LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
    // OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
    // THE SOFTWARE.
    //

    #include <Urho3D/Core/CoreEvents.h>
    #include <Urho3D/Core/ProcessUtils.h>
    #include <Urho3D/Engine/Engine.h>
    #include <Urho3D/Graphics/AnimatedModel.h>
    #include <Urho3D/Graphics/AnimationController.h>
    #include <Urho3D/Graphics/Camera.h>
    #include <Urho3D/Graphics/Light.h>
    #include <Urho3D/Graphics/Material.h>
    #include <Urho3D/Graphics/Octree.h>
    #include <Urho3D/Graphics/Renderer.h>
    #include <Urho3D/Graphics/Zone.h>
    #include <Urho3D/Input/Controls.h>
    #include <Urho3D/Input/Input.h>
    #include <Urho3D/IO/FileSystem.h>
    #include <Urho3D/Physics/CollisionShape.h>
    #include <Urho3D/Physics/PhysicsWorld.h>
    #include <Urho3D/Physics/RigidBody.h>
    #include <Urho3D/Resource/ResourceCache.h>
    #include <Urho3D/Scene/Scene.h>
    #include <Urho3D/UI/Font.h>
    #include <Urho3D/UI/Text.h>
    #include <Urho3D/UI/UI.h>

    #include "Character.h"
    #include "CharacterDemo.h"
    #include "Touch.h"

    #include <Urho3D/DebugNew.h>

    URHO3D_DEFINE_APPLICATION_MAIN(CharacterDemo)

    CharacterDemo::CharacterDemo(Context* context) :
        Sample(context),
        firstPerson_(false)
    {
        // Register factory and attributes for the Character component so it can be created via CreateComponent, and loaded / saved
        Character::RegisterObject(context);
    }

    CharacterDemo::~CharacterDemo()
    {
    }

    void CharacterDemo::Start()
    {
        // Execute base class startup
        Sample::Start();
        if (touchEnabled_)
            touch_ = new Touch(context_, TOUCH_SENSITIVITY);

        // Create static scene content
        CreateScene();

        // Create the controllable character
        CreateCharacter();

        // Create the UI content
        CreateInstructions();

        // Subscribe to necessary events
        SubscribeToEvents();

        // Set the mouse mode to use in the sample
        Sample::InitMouseMode(MM_RELATIVE);
    }

    void CharacterDemo::CreateScene()
    {
        ResourceCache* cache = GetSubsystem<ResourceCache>();

        scene_ = new Scene(context_);

        // Create scene subsystem components
        scene_->CreateComponent<Octree>();
        scene_->CreateComponent<PhysicsWorld>();

        // Create camera and define viewport. We will be doing load / save, so it's convenient to create the camera outside the scene,
        // so that it won't be destroyed and recreated, and we don't have to redefine the viewport on load
        cameraNode_ = new Node(context_);
        Camera* camera = cameraNode_->CreateComponent<Camera>();
        camera->SetFarClip(300.0f);
        GetSubsystem<Renderer>()->SetViewport(0, new Viewport(context_, scene_, camera));

        // Create static scene content. First create a zone for ambient lighting and fog control
        Node* zoneNode = scene_->CreateChild("Zone");
        Zone* zone = zoneNode->CreateComponent<Zone>();
        zone->SetAmbientColor(Color(0.15f, 0.15f, 0.15f));
        zone->SetFogColor(Color(0.5f, 0.5f, 0.7f));
        zone->SetFogStart(100.0f);
        zone->SetFogEnd(300.0f);
        zone->SetBoundingBox(BoundingBox(-1000.0f, 1000.0f));

        // Create a directional light with cascaded shadow mapping
        Node* lightNode = scene_->CreateChild("DirectionalLight");
        lightNode->SetDirection(Vector3(0.3f, -0.5f, 0.425f));
        Light* light = lightNode->CreateComponent<Light>();
        light->SetLightType(LIGHT_DIRECTIONAL);
        light->SetCastShadows(true);
        light->SetShadowBias(BiasParameters(0.00025f, 0.5f));
        light->SetShadowCascade(CascadeParameters(10.0f, 50.0f, 200.0f, 0.0f, 0.8f));
        light->SetSpecularIntensity(0.5f);

        // Create the floor object
        Node* floorNode = scene_->CreateChild("Floor");
        floorNode->SetPosition(Vector3(0.0f, -0.5f, 0.0f));
        floorNode->SetScale(Vector3(200.0f, 1.0f, 200.0f));
        floorNode->SetRotation(Quaternion(-30.0f, 0.0f, 0.0f)); /* Rotate the floor to simulate a slope. */
        StaticModel* object = floorNode->CreateComponent<StaticModel>();
        object->SetModel(cache->GetResource<Model>("Models/Box.mdl"));
        object->SetMaterial(cache->GetResource<Material>("Materials/Stone.xml"));

        RigidBody* body = floorNode->CreateComponent<RigidBody>();
        // Use collision layer bit 2 to mark world scenery. This is what we will raycast against to prevent camera from going
        // inside geometry
        body->SetCollisionLayer(2);
        CollisionShape* shape = floorNode->CreateComponent<CollisionShape>();
        shape->SetBox(Vector3::ONE);

        /* Removed the mushrooms and boxes to simplify the test. */

        /*
        // Create mushrooms of varying sizes
        const unsigned NUM_MUSHROOMS = 60;
        for (unsigned i = 0; i < NUM_MUSHROOMS; ++i)
        {
            Node* objectNode = scene_->CreateChild("Mushroom");
            objectNode->SetPosition(Vector3(Random(180.0f) - 90.0f, 0.0f, Random(180.0f) - 90.0f));
            objectNode->SetRotation(Quaternion(0.0f, Random(360.0f), 0.0f));
            objectNode->SetScale(2.0f + Random(5.0f));
            StaticModel* object = objectNode->CreateComponent<StaticModel>();
            object->SetModel(cache->GetResource<Model>("Models/Mushroom.mdl"));
            object->SetMaterial(cache->GetResource<Material>("Materials/Mushroom.xml"));
            object->SetCastShadows(true);

            RigidBody* body = objectNode->CreateComponent<RigidBody>();
            body->SetCollisionLayer(2);
            CollisionShape* shape = objectNode->CreateComponent<CollisionShape>();
            shape->SetTriangleMesh(object->GetModel(), 0);
        }

        // Create movable boxes. Let them fall from the sky at first
        const unsigned NUM_BOXES = 100;
        for (unsigned i = 0; i < NUM_BOXES; ++i)
        {
            float scale = Random(2.0f) + 0.5f;

            Node* objectNode = scene_->CreateChild("Box");
            objectNode->SetPosition(Vector3(Random(180.0f) - 90.0f, Random(10.0f) + 10.0f, Random(180.0f) - 90.0f));
            objectNode->SetRotation(Quaternion(Random(360.0f), Random(360.0f), Random(360.0f)));
            objectNode->SetScale(scale);
            StaticModel* object = objectNode->CreateComponent<StaticModel>();
            object->SetModel(cache->GetResource<Model>("Models/Box.mdl"));
            object->SetMaterial(cache->GetResource<Material>("Materials/Stone.xml"));
            object->SetCastShadows(true);

            RigidBody* body = objectNode->CreateComponent<RigidBody>();
            body->SetCollisionLayer(2);
            // Bigger boxes will be heavier and harder to move
            body->SetMass(scale * 2.0f);
            CollisionShape* shape = objectNode->CreateComponent<CollisionShape>();
            shape->SetBox(Vector3::ONE);
        }
        */

    }

    void CharacterDemo::CreateCharacter()
    {
        ResourceCache* cache = GetSubsystem<ResourceCache>();

        Node* objectNode = scene_->CreateChild("Jack");
        objectNode->SetPosition(Vector3(0.0f, 1.0f, 0.0f));

        // spin node
        Node* adjustNode = objectNode->CreateChild("AdjNode");
        adjustNode->SetRotation( Quaternion(180, Vector3(0,1,0) ) );

        // Create the rendering component + animation controller
        AnimatedModel* object = adjustNode->CreateComponent<AnimatedModel>();
        object->SetModel(cache->GetResource<Model>("Models/Mutant/Mutant.mdl"));
        object->SetMaterial(cache->GetResource<Material>("Models/Mutant/Materials/mutant_M.xml"));
        object->SetCastShadows(true);
        adjustNode->CreateComponent<AnimationController>();

        // Set the head bone for manual control
        object->GetSkeleton().GetBone("Mutant:Head")->animated_ = false;

        // Create rigidbody, and set non-zero mass so that the body becomes dynamic
        RigidBody* body = objectNode->CreateComponent<RigidBody>();
        body->SetCollisionLayer(1);
        body->SetMass(1.0f);

        // Set zero angular factor so that physics doesn't turn the character on its own.
        // Instead we will control the character yaw manually
        body->SetAngularFactor(Vector3::ZERO);

        // Set the rigidbody to signal collision also when in rest, so that we get ground collisions properly
        body->SetCollisionEventMode(COLLISION_ALWAYS);

        // Set a capsule shape for collision
        CollisionShape* shape = objectNode->CreateComponent<CollisionShape>();
        shape->SetCapsule(0.7f, 1.8f, Vector3(0.0f, 0.9f, 0.0f));

        // Create the character logic component, which takes care of steering the rigidbody
        // Remember it so that we can set the controls. Use a WeakPtr because the scene hierarchy already owns it
        // and keeps it alive as long as it's not removed from the hierarchy
        character_ = objectNode->CreateComponent<Character>();
    }

    void CharacterDemo::CreateInstructions()
    {
        ResourceCache* cache = GetSubsystem<ResourceCache>();
        UI* ui = GetSubsystem<UI>();

        // Construct new Text object, set string to display and font to use
        Text* instructionText = ui->GetRoot()->CreateChild<Text>();
        instructionText->SetText(
            "Use WASD keys and mouse/touch to move\n"
            "Space to jump, F to toggle 1st/3rd person\n"
            "F5 to save scene, F7 to load"
        );
        instructionText->SetFont(cache->GetResource<Font>("Fonts/Anonymous Pro.ttf"), 15);
        // The text has multiple rows. Center them in relation to each other
        instructionText->SetTextAlignment(HA_CENTER);

        // Position the text relative to the screen center
        instructionText->SetHorizontalAlignment(HA_CENTER);
        instructionText->SetVerticalAlignment(VA_CENTER);
        instructionText->SetPosition(0, ui->GetRoot()->GetHeight() / 4);
    }

    void CharacterDemo::SubscribeToEvents()
    {
        // Subscribe to Update event for setting the character controls before physics simulation
        SubscribeToEvent(E_UPDATE, URHO3D_HANDLER(CharacterDemo, HandleUpdate));

        // Subscribe to PostUpdate event for updating the camera position after physics simulation
        SubscribeToEvent(E_POSTUPDATE, URHO3D_HANDLER(CharacterDemo, HandlePostUpdate));

        // Unsubscribe the SceneUpdate event from base class as the camera node is being controlled in HandlePostUpdate() in this sample
        UnsubscribeFromEvent(E_SCENEUPDATE);
    }

    void CharacterDemo::HandleUpdate(StringHash eventType, VariantMap& eventData)
    {
        using namespace Update;

        Input* input = GetSubsystem<Input>();

        if (character_)
        {
            // Clear previous controls
            character_->controls_.Set(CTRL_FORWARD | CTRL_BACK | CTRL_LEFT | CTRL_RIGHT | CTRL_JUMP, false);

            // Update controls using touch utility class
            if (touch_)
                touch_->UpdateTouches(character_->controls_);

            // Update controls using keys
            UI* ui = GetSubsystem<UI>();
            if (!ui->GetFocusElement())
            {
                if (!touch_ || !touch_->useGyroscope_)
                {
                    character_->controls_.Set(CTRL_FORWARD, input->GetKeyDown(KEY_W));
                    character_->controls_.Set(CTRL_BACK, input->GetKeyDown(KEY_S));
                    character_->controls_.Set(CTRL_LEFT, input->GetKeyDown(KEY_A));
                    character_->controls_.Set(CTRL_RIGHT, input->GetKeyDown(KEY_D));
                }
                character_->controls_.Set(CTRL_JUMP, input->GetKeyDown(KEY_SPACE));

                // Add character yaw & pitch from the mouse motion or touch input
                if (touchEnabled_)
                {
                    for (unsigned i = 0; i < input->GetNumTouches(); ++i)
                    {
                        TouchState* state = input->GetTouch(i);
                        if (!state->touchedElement_)    // Touch on empty space
                        {
                            Camera* camera = cameraNode_->GetComponent<Camera>();
                            if (!camera)
                                return;

                            Graphics* graphics = GetSubsystem<Graphics>();
                            character_->controls_.yaw_ += TOUCH_SENSITIVITY * camera->GetFov() / graphics->GetHeight() * state->delta_.x_;
                            character_->controls_.pitch_ += TOUCH_SENSITIVITY * camera->GetFov() / graphics->GetHeight() * state->delta_.y_;
                        }
                    }
                }
                else
                {
                    character_->controls_.yaw_ += (float)input->GetMouseMoveX() * YAW_SENSITIVITY;
                    character_->controls_.pitch_ += (float)input->GetMouseMoveY() * YAW_SENSITIVITY;
                }
                // Limit pitch
                character_->controls_.pitch_ = Clamp(character_->controls_.pitch_, -80.0f, 80.0f);
                // Set rotation already here so that it's updated every rendering frame instead of every physics frame
                character_->GetNode()->SetRotation(Quaternion(character_->controls_.yaw_, Vector3::UP));

                // Switch between 1st and 3rd person
                if (input->GetKeyPress(KEY_F))
                    firstPerson_ = !firstPerson_;

                // Turn on/off gyroscope on mobile platform
                if (touch_ && input->GetKeyPress(KEY_G))
                    touch_->useGyroscope_ = !touch_->useGyroscope_;

                // Check for loading / saving the scene
                if (input->GetKeyPress(KEY_F5))
                {
                    File saveFile(context_, GetSubsystem<FileSystem>()->GetProgramDir() + "Data/Scenes/CharacterDemo.xml", FILE_WRITE);
                    scene_->SaveXML(saveFile);
                }
                if (input->GetKeyPress(KEY_F7))
                {
                    File loadFile(context_, GetSubsystem<FileSystem>()->GetProgramDir() + "Data/Scenes/CharacterDemo.xml", FILE_READ);
                    scene_->LoadXML(loadFile);
                    // After loading we have to reacquire the weak pointer to the Character component, as it has been recreated
                    // Simply find the character's scene node by name as there's only one of them
                    Node* characterNode = scene_->GetChild("Jack", true);
                    if (characterNode)
                        character_ = characterNode->GetComponent<Character>();
                }
            }

            /* Raycast down to get the floor normal under the character and store the normal value. */
            PhysicsRaycastResult result;
            scene_->GetComponent<PhysicsWorld>()->RaycastSingle(result, Ray( character_->GetNode()->GetPosition() , Vector3(0.0f,-1.0f,0.0f) ), 5.0f, 2);
            if (result.body_) {
                character_->floorNormal=result.normal_;
            }

        }
    }

    void CharacterDemo::HandlePostUpdate(StringHash eventType, VariantMap& eventData)
    {
        if (!character_)
            return;

        Node* characterNode = character_->GetNode();

        // Get camera lookat dir from character yaw + pitch
        Quaternion rot = characterNode->GetRotation();
        Quaternion dir = rot * Quaternion(character_->controls_.pitch_, Vector3::RIGHT);

        // Turn head to camera pitch, but limit to avoid unnatural animation
        Node* headNode = characterNode->GetChild("Mutant:Head", true);
        float limitPitch = Clamp(character_->controls_.pitch_, -45.0f, 45.0f);
        Quaternion headDir = rot * Quaternion(limitPitch, Vector3(1.0f, 0.0f, 0.0f));
        // This could be expanded to look at an arbitrary target, now just look at a point in front
        Vector3 headWorldTarget = headNode->GetWorldPosition() + headDir * Vector3(0.0f, 0.0f, -1.0f);
        headNode->LookAt(headWorldTarget, Vector3(0.0f, 1.0f, 0.0f));

        if (firstPerson_)
        {
            cameraNode_->SetPosition(headNode->GetWorldPosition() + rot * Vector3(0.0f, 0.15f, 0.2f));
            cameraNode_->SetRotation(dir);
        }
        else
        {
            // Third person camera: position behind the character
            Vector3 aimPoint = characterNode->GetPosition() + rot * Vector3(0.0f, 1.7f, 0.0f);

            // Collide camera ray with static physics objects (layer bitmask 2) to ensure we see the character properly
            Vector3 rayDir = dir * Vector3::BACK;
            float rayDistance = touch_ ? touch_->cameraDistance_ : CAMERA_INITIAL_DIST;
            PhysicsRaycastResult result;
            scene_->GetComponent<PhysicsWorld>()->RaycastSingle(result, Ray(aimPoint, rayDir), rayDistance, 2);
            if (result.body_)
                rayDistance = Min(rayDistance, result.distance_);
            rayDistance = Clamp(rayDistance, CAMERA_MIN_DIST, CAMERA_MAX_DIST);

            cameraNode_->SetPosition(aimPoint + rayDir * rayDistance);
            cameraNode_->SetRotation(dir);
        }
    }

Special thanks to @1vanK, his posts https://discourse.urho3d.io/t/solved-how-to-direct-a-character-parallel-to-the-ground/1285/5 and https://discourse.urho3d.io/t/improved-charactercontroller/3472 were essential to fix the movement.

Also special thanks to @Eugene for pointing vertical velocity and to @jmiller for taking the time to help figure out this problem. You guys are awesome!

Best regards.

-------------------------

Eugene | 2018-01-04 21:08:26 UTC | #2

(just wanted to mention it somewhere)
There is another approach of implementing character controller: use `CrowdAgent`.
Then set `weightToi` to some small value and use `SetTargetVelocity` to drive character.

It could be used almost without tweaks if character doesn't jump and moves over static geometry only.
There may be some tricks to use this approach for generic character controller tho...

I wanted to mention it because tweaking `weightToi` is not obvious at all.

-------------------------

QBkGames | 2019-04-28 00:54:59 UTC | #3

I've learned the hard way that HandleNodeCollision algorithm can get stuck in valleys between 2 (or more) slopes and the character will never become grounded.
A better way would be to average all the contact normals and check if the average.y_ > 0.75 to determined if the character is grounded.

Also simply disabling gravity risks having the character floating up and away if something else bumps into it.

-------------------------

