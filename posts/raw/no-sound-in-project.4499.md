GodMan | 2018-08-28 14:38:16 UTC | #1

   Maybe I'm overlooking something, but I did verify the sound file is being loaded in the console window. I have not gotten the sound or music to play. I used the sound demo as a reference, and the sound demo works fine, but not in the example where I try to play any sound or music.



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

        #include "Sample.h"

        namespace Urho3D
        {

        class Node;
        class Scene;

        }

        /// Skeletal animation example.
        /// This sample demonstrates:
        ///     - Populating a 3D scene with skeletally animated AnimatedModel components;
        ///     - Moving the animated models and advancing their animation using a custom component
        ///     - Enabling a cascaded shadow map on a directional light, which allows high-quality shadows
        ///       over a large area (typically used in outdoor scenes for shadows cast by sunlight)
        ///     - Displaying renderer debug geometry
        class SkeletalAnimation : public Sample
        {
            URHO3D_OBJECT(SkeletalAnimation, Sample);

        public:
            /// Construct.
            SkeletalAnimation(Context* context);

            /// Setup after engine initialization and before running the main loop.
            virtual void Start();

        protected:
        	Text *text_ = new Text(context_);
        	SoundSource* musicSource_;
        	SoundSource3D* sound_source_flag;
        	Sound* sound_flag;

            /// Return XML patch instructions for screen joystick layout for a specific sample app, if any.
            virtual String GetScreenJoystickPatchString() const { return
                "<patch>"
                "    <remove sel=\"/element/element[./attribute[@name='Name' and @value='Button1']]/attribute[@name='Is Visible']\" />"
                "    <replace sel=\"/element/element[./attribute[@name='Name' and @value='Button1']]/element[./attribute[@name='Name' and @value='Label']]/attribute[@name='Text']/@value\">Debug</replace>"
                "    <add sel=\"/element/element[./attribute[@name='Name' and @value='Button1']]\">"
                "        <element type=\"Text\">"
                "            <attribute name=\"Name\" value=\"KeyBinding\" />"
                "            <attribute name=\"Text\" value=\"SPACE\" />"
                "        </element>"
                "    </add>"
                "</patch>";
            }

        private:
            /// Construct the scene content.
            void CreateScene();
            /// Construct an instruction text to the UI.
            void CreateInstructions();
            /// Set up a viewport for displaying the scene.
            void SetupViewport(float exposure);
            /// Subscribe to application-wide logic update and post-render update events.
            void SubscribeToEvents();
            /// Read input and moves the camera.
            void MoveCamera(float timeStep);
            /// Handle the logic update event.
            void HandleUpdate(StringHash eventType, VariantMap& eventData);
            /// Handle the post-render update event.
            void HandlePostRenderUpdate(StringHash eventType, VariantMap& eventData);

        	void HandlePlayMusic(StringHash eventType, VariantMap& eventData);
        	/// Handle "stop music" button click.
        	void HandleStopMusic(StringHash eventType, VariantMap& eventData);
        	/// Handle sound effects volume slider change.
        	void HandleSoundVolume(StringHash eventType, VariantMap& eventData);
        	/// Handle music volume slider change.
        	void HandleMusicVolume(StringHash eventType, VariantMap& eventData);
            
            /// Flag for drawing debug geometry.
            bool drawDebug_;
        };



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

    #include <string>
    #include <sstream>

    #include <Urho3D/Core/CoreEvents.h>
    #include <Urho3D/Engine/Engine.h>
    #include <Urho3D/Graphics/AnimatedModel.h>
    #include <Urho3D/Graphics/Animation.h>
    #include <Urho3D/Graphics/AnimationState.h>
    #include <Urho3D/Graphics/AnimationController.h>
    #include <Urho3D/Graphics/Camera.h>
    #include <Urho3D/Graphics/DebugRenderer.h>
    #include <Urho3D/Graphics/Graphics.h>
    #include <Urho3D/Graphics/Light.h>
    #include <Urho3D/Graphics/Material.h>
    #include <Urho3D/Graphics/Octree.h>
    #include <Urho3D/Graphics/Renderer.h>
    #include <Urho3D/Graphics/RenderPath.h>
    #include <Urho3D/Graphics/Zone.h>
    #include <Urho3D/Graphics/Skybox.h>
    #include <Urho3D/Input/Input.h>
    #include <Urho3D/Physics/CollisionShape.h>
    #include <Urho3D/Physics/PhysicsWorld.h>
    #include <Urho3D/Physics/RigidBody.h>
    #include <Urho3D/Resource/ResourceCache.h>
    #include <Urho3D/Scene/Scene.h>
    #include <Urho3D/Audio/Sound.h>
    #include <Urho3D/Audio/SoundSource3D.h>
    #include <Urho3D/Audio/SoundListener.h>
    #include <Urho3D/Audio/Audio.h>
    #include <Urho3D/UI/Font.h>
    #include <Urho3D/UI/Text.h>
    #include <Urho3D/UI/UI.h>
    #include <Urho3D/Graphics/ParticleEffect.h>
    #include <Urho3D/Graphics/ParticleEmitter.h>
    #include <Urho3D/IO/Log.h>

    #include "Mover.h"
    #include "SkeletalAnimation.h"

    #include <Urho3D/DebugNew.h>

    URHO3D_DEFINE_APPLICATION_MAIN(SkeletalAnimation)

    SkeletalAnimation::SkeletalAnimation(Context* context) :
    Sample(context),
    musicSource_(nullptr),
    drawDebug_(false)
    {
        // Register an object factory for our custom Mover component so that we can create them to scene nodes
        context->RegisterFactory<Mover>();

    	engineParameters_["FullScreen"] = true;
    	engineParameters_["WindowResizable"] = true;
    	engineParameters_["VSync"] = true;
    	engineParameters_[EP_SOUND] = true;
    }

    void SkeletalAnimation::Start()
    {
    	


        // Execute base class startup
        Sample::Start();

        // Create the scene content
        CreateScene();

        // Create the UI content
        CreateInstructions();

        // Setup the viewport for displaying the scene
        SetupViewport(0.9f);

        // Hook up to the frame update and render post-update events
        SubscribeToEvents();

        // Set the mouse mode to use in the sample
        Sample::InitMouseMode(MM_ABSOLUTE);


    }

    void SkeletalAnimation::CreateScene()
    {



        ResourceCache* cache = GetSubsystem<ResourceCache>();

        scene_ = new Scene(context_);



        // Create octree, use default volume (-1000, -1000, -1000) to (1000, 1000, 1000)
        // Also create a DebugRenderer component so that we can draw debug geometry
        scene_->CreateComponent<Octree>();
        scene_->CreateComponent<DebugRenderer>();

    	Node* skyNode = scene_->CreateChild("Sky");
    	Skybox* skybox = skyNode->CreateComponent<Skybox>();
    	skybox->SetModel(cache->GetResource<Model>("Models/Box.mdl"));
    	skybox->SetMaterial(cache->GetResource<Material>("Materials/Skybox.xml"));

        // Create scene node & StaticModel component for showing a static plane
        Node* planeNode = scene_->CreateChild("Plane");
       // planeNode->SetScale(Vector3(500.0f, 1.0f, 500.0f));
        StaticModel* planeObject = planeNode->CreateComponent<StaticModel>();
        planeObject->SetModel(cache->GetResource<Model>("Models/icefields.mdl"));
    //	auto mat = cache->GetResource<Material>("Materials/icefields_base_lights_blue.xml");
    //	mat->SetRenderOrder(100);   // Lower render order to render first
    //	auto mat2 = cache->GetResource<Material>("Materials/icefields_base_lights_red.xml");
    //	mat2->SetRenderOrder(100);   // Lower render order to render first
    	planeObject->ApplyMaterialList("Materials/icefields.txt");

    	RigidBody* body = planeNode->CreateComponent<RigidBody>();
    	// Use collision layer bit 2 to mark world scenery. This is what we will raycast against to prevent camera from going
    	// inside geometry
    	body->SetCollisionLayer(2);
    	CollisionShape* shape = planeNode->CreateComponent<CollisionShape>();
    	shape->SetBox(Vector3::ONE);

    	
        // Create a Zone component for ambient lighting & fog control
        Node* zoneNode = scene_->CreateChild("Zone");
        Zone* zone = zoneNode->CreateComponent<Zone>();
        zone->SetBoundingBox(BoundingBox(-10000.0f, 10000.0f));
    	zone->SetAmbientColor(Color(0.2f, 0.2f, 0.2f));
        zone->SetFogColor(Color(0.3f, 0.3f, 0.3f));
        zone->SetFogStart(100.0f);
        zone->SetFogEnd(7000.0f);
    	//zone->SetFogHeight(25.0f);
    	

    	
        // Create a directional light to the world. Enable cascaded shadows on it
        Node* lightNode = scene_->CreateChild("DirectionalLight");
        lightNode->SetDirection(Vector3(0.6f, -5.0f, 5.8f));
        Light* light = lightNode->CreateComponent<Light>();
        light->SetLightType(LIGHT_DIRECTIONAL);
        light->SetCastShadows(true);
        light->SetColor(Color(0.5f, 0.5f, 0.5f));
        light->SetShadowBias(BiasParameters(0.00025f, 0.5f));
        // Set cascade splits at 10, 50 and 200 world units, fade shadows out at 80% of maximum shadow distance
        light->SetShadowCascade(CascadeParameters(10.0f, 50.0f, 200.0f, 0.0f, 0.8f));
    	/*
    	// Create a directional light to the world. Enable cascaded shadows on it
    	Node* lightNode2 = scene_->CreateChild("DirectionalLight2");
    	lightNode2->SetDirection(Vector3(0.6f, -5.0f, -5.8f));
    	Light* light2 = lightNode2->CreateComponent<Light>();
    	light2->SetLightType(LIGHT_DIRECTIONAL);
    	light2->SetColor(Color(0.9f, 0.9f, 0.9f));
    	*/
        // Create animated models
        const unsigned NUM_MODELS = 1;
        const float MODEL_MOVE_SPEED = 1.0f;
        const float MODEL_ROTATE_SPEED = 50.0f;
        const BoundingBox bounds(Vector3(-20.0f, 0.0f, -20.0f), Vector3(20.0f, 0.0f, 20.0f));


            Node* modelNode = scene_->CreateChild("Jill");
    		modelNode->SetPosition(Vector3(-545.0f, 0, 545.0f));

            AnimatedModel* modelObject = modelNode->CreateComponent<AnimatedModel>();
            modelObject->SetModel(cache->GetResource<Model>("Models/raziel.mdl"));
           // modelObject->SetMaterial(cache->GetResource<Material>("Materials/armor.xml"));
    		modelObject->ApplyMaterialList("Materials/raziel.txt");
            modelObject->SetCastShadows(true);

            // Create an AnimationState for a walk animation. Its time position will need to be manually updated to advance the
            // animation, The alternative would be to use an AnimationController component which updates the animation automatically,
            // but we need to update the model's position manually in any case

    	
    		    AnimationController* ninjaAnimCtrl_ = modelNode->CreateComponent<AnimationController>();
    			ninjaAnimCtrl_->SetRemoveOnCompletion("Jill", true);
    			ninjaAnimCtrl_->PlayExclusive("Models/raziel_Take001.ani", 0, true, 1.0f);
    	
    	

        // Create the camera. Limit far clip distance to match the fog
        cameraNode_ = scene_->CreateChild("Camera");
        Camera* camera = cameraNode_->CreateComponent<Camera>();
    	camera->SetNearClip(1.0f);
        camera->SetFarClip(10000.0f);

        // Set an initial position for the camera scene node above the plane
        cameraNode_->SetPosition(Vector3(13.0f, 5.0f, 0));

    	// as with all things in Urho, you don't really need a node just for
    	// the particle effect but here I needed an offset

    	//Node* handBoneNode = modelNode->GetChild("frame head", true);
    	Node* snowNode = scene_->CreateChild("SnowParticles");
    	snowNode->SetPosition(Vector3(2450.53f, 215.103f, -1351.18f));
    	ParticleEmitter* emitter = snowNode->CreateComponent<ParticleEmitter>();
    	emitter->SetEffect(cache->GetResource<ParticleEffect>("Particle/Snow.xml"));

    	Node* handBoneNode = modelNode->GetChild("Bip001 R Forearm", true);
    	ParticleEmitter* emitter2 = handBoneNode->CreateComponent<ParticleEmitter>();
    	emitter2->SetEffect(cache->GetResource<ParticleEffect>("Particle/ReaverArm.xml"));


    	// loading the sound
    	sound_flag = cache->GetResource<Sound>("Music/test.wav");
    	sound_source_flag = modelNode->CreateComponent<SoundSource3D>();
    	sound_source_flag->SetNearDistance(1);  // distance up to where the volume is 100%
    	sound_source_flag->SetFarDistance(1550);  // distance from where the volume is at 0%
    	sound_source_flag->SetSoundType(SOUND_EFFECT);
    	
    	sound_source_flag->Play(sound_flag);

    }

    void SkeletalAnimation::CreateInstructions()
    {
        ResourceCache* cache = GetSubsystem<ResourceCache>();
        UI* ui = GetSubsystem<UI>();

        // Construct new Text object, set string to display and font to use
        Text* instructionText = ui->GetRoot()->CreateChild<Text>();
        instructionText->SetText(
            "Use WASD keys and mouse/touch to move\n"
            "Space to toggle debug geometry"
        );
        instructionText->SetFont(cache->GetResource<Font>("Fonts/Anonymous Pro.ttf"), 15);
        // The text has multiple rows. Center them in relation to each other
        instructionText->SetTextAlignment(HA_CENTER);

        // Position the text relative to the screen center
        instructionText->SetHorizontalAlignment(HA_CENTER);
        instructionText->SetVerticalAlignment(VA_CENTER);
        instructionText->SetPosition(0, ui->GetRoot()->GetHeight() / 4);
    }

    void SkeletalAnimation::SetupViewport(float exposure)
    {
    	Graphics* graphics = GetSubsystem<Graphics>();
        Renderer* renderer = GetSubsystem<Renderer>();

    	graphics->SetSRGB(true);
    	renderer->SetHDRRendering(true);

        // Set up a viewport to the Renderer subsystem so that the 3D scene can be seen
        SharedPtr<Viewport> viewport(new Viewport(context_, scene_, cameraNode_->GetComponent<Camera>()));
        renderer->SetViewport(0, viewport);



    	// Clone the default render path so that we do not interfere with the other viewport, then add
    	// bloom and FXAA post process effects to the front viewport. Render path commands can be tagged
    	// for example with the effect name to allow easy toggling on and off. We start with the effects
    	// disabled.
    	ResourceCache* cache = GetSubsystem<ResourceCache>();
    	SharedPtr<RenderPath> effectRenderPath = viewport->GetRenderPath()->Clone();


    	
    	effectRenderPath->Append(cache->GetResource<XMLFile>("PostProcess/BloomHDR.xml"));
    	effectRenderPath->Append(cache->GetResource<XMLFile>("PostProcess/Tonemap.xml"));
    	effectRenderPath->Append(cache->GetResource<XMLFile>("PostProcess/AutoExposure.xml"));
    	effectRenderPath->Append(cache->GetResource<XMLFile>("PostProcess/FXAA2.xml"));


    	// Make the bloom mixing parameter more pronounced
    	effectRenderPath->SetShaderParameter("BloomHDRMix", Vector2(exposure, 4.0f));
    	effectRenderPath->SetEnabled("BloomHDR", true);
    	effectRenderPath->SetEnabled("FXAA2", true);

    	viewport->SetRenderPath(effectRenderPath);

    }

    void SkeletalAnimation::SubscribeToEvents()
    {

        // Subscribe HandleUpdate() function for processing update events
        SubscribeToEvent(E_UPDATE, URHO3D_HANDLER(SkeletalAnimation, HandleUpdate));

        // Subscribe HandlePostRenderUpdate() function for processing the post-render update event, sent after Renderer subsystem is
        // done with defining the draw calls for the viewports (but before actually executing them.) We will request debug geometry
        // rendering during that event
        SubscribeToEvent(E_POSTRENDERUPDATE, URHO3D_HANDLER(SkeletalAnimation, HandlePostRenderUpdate));

    	

    }

    void SkeletalAnimation::MoveCamera(float timeStep)
    {
        // Do not move if the UI has a focused element (the console)
        if (GetSubsystem<UI>()->GetFocusElement())
            return;

        Input* input = GetSubsystem<Input>();

        // Movement speed as world units per second
        const float MOVE_SPEED = 500.0f;
        // Mouse sensitivity as degrees per pixel
        const float MOUSE_SENSITIVITY = 0.1f;

        // Use this frame's mouse motion to adjust camera node yaw and pitch. Clamp the pitch between -90 and 90 degrees
        IntVector2 mouseMove = input->GetMouseMove();
        yaw_ += MOUSE_SENSITIVITY * mouseMove.x_;
        pitch_ += MOUSE_SENSITIVITY * mouseMove.y_;
        pitch_ = Clamp(pitch_, -90.0f, 90.0f);

        // Construct new orientation for the camera scene node from yaw and pitch. Roll is fixed to zero
        cameraNode_->SetRotation(Quaternion(pitch_, yaw_, 0.0f));

        // Read WASD keys and move the camera scene node to the corresponding direction if they are pressed
        if (input->GetKeyDown(KEY_W))
            cameraNode_->Translate(Vector3::FORWARD * MOVE_SPEED * timeStep);
        if (input->GetKeyDown(KEY_S))
            cameraNode_->Translate(Vector3::BACK * MOVE_SPEED * timeStep);
        if (input->GetKeyDown(KEY_A))
            cameraNode_->Translate(Vector3::LEFT * MOVE_SPEED * timeStep);
        if (input->GetKeyDown(KEY_D))
            cameraNode_->Translate(Vector3::RIGHT * MOVE_SPEED * timeStep);

    	Node* characterNode = scene_->GetChild("Jill", true);

    	AnimationController* ninjaAnimCtrl2_ = characterNode->CreateComponent<AnimationController>();

    	if (input->GetKeyPress(KEY_J))
    		SetupViewport(0.1f);

        // Toggle debug geometry with space
        if (input->GetKeyPress(KEY_SPACE))
            drawDebug_ = !drawDebug_;
    }

    void SkeletalAnimation::HandleUpdate(StringHash eventType, VariantMap& eventData)
    {
        using namespace Update;

        // Take the frame time step, which is stored as a float
        float timeStep = eventData[P_TIMESTEP].GetFloat();

        // Move the camera, scale movement with time step
        MoveCamera(timeStep);

    	String str;
    	str.Append(cameraNode_->GetPosition().ToString());
    //	URHO3D_LOGINFO(str);     // this show how to put stuff into the log
    	GetSubsystem<UI>()->GetRoot()->AddChild(text_);

    }

    void SkeletalAnimation::HandlePostRenderUpdate(StringHash eventType, VariantMap& eventData)
    {
        // If draw debug mode is enabled, draw viewport debug geometry, which will show eg. drawable bounding boxes and skeleton
        // bones. Note that debug geometry has to be separately requested each frame. Disable depth test so that we can see the
        // bones properly
        if (drawDebug_)
            GetSubsystem<Renderer>()->DrawDebugGeometry(false);
    }

-------------------------

Modanung | 2018-08-29 01:42:32 UTC | #2

When using `SoundSource3D` to play sound the `Scene` needs to contain a `SoundListener` component as well. In most cases you'd want this to be attached to the active `Camera`'s node.

The active `SoundListener` is set by calling `SetListener(SoundListener*)` on the `Audio` subsystem.

-------------------------

GodMan | 2018-08-29 23:29:48 UTC | #3

    	// for 3D sounds to work
    	SoundListener* listener = cameraNode_->CreateComponent<SoundListener>();
    	GetSubsystem<Audio>()->SetListener(listener);

    	// you can set master volumes for the different kinds if sounds, here 30% for music
    	GetSubsystem<Audio>()->SetMasterGain(SOUND_MUSIC, 1.0);


    	// loading the sound
    	sound_flag = cache->GetResource<Sound>("Music/Sad_0.wav");
    	sound_source_flag = modelNode->CreateComponent<SoundSource3D>();
    	sound_source_flag->SetNearDistance(1);  // distance up to where the volume is 100%
    	sound_source_flag->SetFarDistance(1550);  // distance from where the volume is at 0%
    	sound_source_flag->SetSoundType(SOUND_EFFECT);
    	
    	sound_source_flag->Play(sound_flag);

So this is what I have. No sound, but the .wav file does load in the console.

-------------------------

weitjong | 2018-08-30 05:26:26 UTC | #4

Your EP_SOUND engine parameter was overwritten by Sample::Setup(), I believe. Try move the init logic to your own Setup() method override.

-------------------------

GodMan | 2018-08-30 16:23:24 UTC | #5

I tried moving my engine parameters, but I still don't get any sound output. Let just use sound source. I'm just trying to play background sound no 3d position needed.


    	Sound* sound = cache->GetResource<Sound>("Music/sad_0.wav");
    	sound->SetLooped(true);  // sound can be set to be repeated
    	// you can use an existing or a new node to append the sound to
    	Node* node = cameraNode_->CreateChild("Sound");
    	SoundSource* sound_source = node->CreateComponent<SoundSource>();
    	sound_source->SetSoundType(SOUND_MUSIC);  // optional
    	sound_source->Play(sound);

-------------------------

green-zone | 2018-08-30 17:57:51 UTC | #6

Sample.inl file file make disabled sound
[Sample.inl](https://github.com/urho3d/Urho3D/blob/master/Source/Samples/Sample.inl)
In Setup() function:
`engineParameters_[EP_SOUND]        = false;`

-------------------------

GodMan | 2018-08-30 18:41:29 UTC | #7

So basically my Setup() is overriding my engine parameters. It's setting it to false every time.

-------------------------

