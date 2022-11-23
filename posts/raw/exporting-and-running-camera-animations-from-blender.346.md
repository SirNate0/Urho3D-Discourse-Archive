gunnar.kriik | 2017-01-02 00:59:45 UTC | #1

Hi,

I'm currently attempting to export a simple camera animation from Blender to Urho3D. I export the animation as Collada (.dae) and used the AssetImporter tool to convert the animation. So far so good, I get the .ani file and place it in Urho3D Bin folder. However, I'm not sure how to attach the animation to the camera object. I was trying the following, but it doesn't seem to work:

[code]
ObjectAnimation* anim = cache->GetResource<ObjectAnimation>("Animations/CameraAnim1.ani");
cameraNode_->SetObjectAnimation(anim);
[/code]

I'm not even sure this is correct, as the camera doesn't move. Is this the correct way to load animations from file?

Thanks!

-------------------------

cadaver | 2017-01-02 00:59:45 UTC | #2

ObjectAnimation is a bit different, later added concept and is not exported by AssetImporter, though the eventual goal would be to unify all these mechanisms of playing animations.

Rather, what you're looking for is "node animation" which is documented on the same page as ordinary skeletal animations: [urho3d.github.io/documentation/a00025.html](http://urho3d.github.io/documentation/a00025.html) . It is actually just like a skeletal animation data-wise, but is applied to an "ordinary" scene node instead of a model's bone nodes.

The animation can be applied by either instantiating an AnimationState yourself using the constructor overload which takes a scene node (in this case it would be the camera scene node) or by creating an AnimationController component and using it to play the node animation.

-------------------------

gunnar.kriik | 2017-01-02 00:59:45 UTC | #3

Alright! Thanks Lasse! I'll try to make that work and post working code here as reference to others.

-------------------------

gunnar.kriik | 2017-01-02 00:59:45 UTC | #4

Thanks again, Lasse. Got it working, and here is the modified LightAnimation sample in case anybody else wants to do something similar.

LightAnimation.h
[code]
#pragma once

#include "Sample.h"

namespace Urho3D
{

class Node;
class Scene;
class AnimationState;

}

/// Light animation example.
/// This sample is base on StaticScene, and it demonstrates:
///     - Usage of attribute animation for light color animation
class LightAnimation : public Sample
{
    OBJECT(LightAnimation);

public:
    /// Construct.
    LightAnimation(Context* context);

    /// Setup after engine initialization and before running the main loop.
    virtual void Start();

private:
    /// Construct the scene content.
    void CreateScene();
    /// Construct an instruction text to the UI.
    void CreateInstructions();
    /// Set up a viewport for displaying the scene.
    void SetupViewport();
    /// Subscribe to application-wide logic update events.
    void SubscribeToEvents();
    /// Handle the logic update event.
    void HandleUpdate(StringHash eventType, VariantMap& eventData);
    
    // Camera node animation state instance
    SharedPtr<AnimationState> animationState_;
};
[/code]

LightAnimation.cpp:
[code]
#include "Camera.h"
#include "CoreEvents.h"
#include "Engine.h"
#include "Font.h"
#include "Graphics.h"
#include "Input.h"
#include "LightAnimation.h"
#include "Material.h"
#include "Model.h"
#include "Octree.h"
#include "Renderer.h"
#include "ResourceCache.h"
#include "Scene.h"
#include "StaticModel.h"
#include "Text.h"
#include "UI.h"
#include "Animation.h"
#include "AnimationState.h"

#include "DebugNew.h"
#include "Animatable.h"

DEFINE_APPLICATION_MAIN(LightAnimation)

LightAnimation::LightAnimation(Context* context) :
    Sample(context)
{
}

void LightAnimation::Start()
{
    // Execute base class startup
    Sample::Start();

    // Create the scene content
    CreateScene();
    
    // Setup the viewport for displaying the scene
    SetupViewport();

    // Hook up to the frame update events
    SubscribeToEvents();
}

void LightAnimation::CreateScene()
{
    ResourceCache* cache = GetSubsystem<ResourceCache>();
    
    scene_ = new Scene(context_);
    
    // Create the Octree component to the scene. This is required before adding any drawable components, or else nothing will
    // show up. The default octree volume will be from (-1000, -1000, -1000) to (1000, 1000, 1000) in world coordinates; it
    // is also legal to place objects outside the volume but their visibility can then not be checked in a hierarchically
    // optimizing manner
    scene_->CreateComponent<Octree>();
    
    // Create a child scene node (at world origin) and a StaticModel component into it. Set the StaticModel to show a simple
    // plane mesh with a "stone" material. Note that naming the scene nodes is optional. Scale the scene node larger
    // (100 x 100 world units)
    Node* planeNode = scene_->CreateChild("Plane");
    planeNode->SetScale(Vector3(100.0f, 1.0f, 100.0f));
    StaticModel* planeObject = planeNode->CreateComponent<StaticModel>();
    planeObject->SetModel(cache->GetResource<Model>("Models/Plane.mdl"));
    planeObject->SetMaterial(cache->GetResource<Material>("Materials/StoneTiled.xml"));
    
    // Create a point light to the world so that we can see something. 
    Node* lightNode = scene_->CreateChild("PointLight");
    Light* light = lightNode->CreateComponent<Light>();
    light->SetLightType(LIGHT_POINT);
    light->SetRange(200.0f);
    
    // Create a scene node for the camera, which we will move around
    // The camera will use default settings (1000 far clip distance, 45 degrees FOV, set aspect ratio automatically)
    cameraNode_ = scene_->CreateChild("Camera");
    cameraNode_->CreateComponent<Camera>();
    
    // Set an initial position for the camera scene node above the plane
    cameraNode_->SetPosition(Vector3(0.0f, 5.0f, 0.0f));

    // Load animation from file, in this case exported from Blender and converted using AssetImporter
    SharedPtr<Animation> anim(cache->GetResource<Animation>("Animations/CameraAnim1.ani"));
    animationState_ = SharedPtr<AnimationState>(new AnimationState(cameraNode_, anim));
}

void LightAnimation::SetupViewport()
{
    Renderer* renderer = GetSubsystem<Renderer>();
    
    // Set up a viewport to the Renderer subsystem so that the 3D scene can be seen. We need to define the scene and the camera
    // at minimum. Additionally we could configure the viewport screen size and the rendering path (eg. forward / deferred) to
    // use, but now we just use full screen and default render path configured in the engine command line options
    SharedPtr<Viewport> viewport(new Viewport(context_, scene_, cameraNode_->GetComponent<Camera>()));
    renderer->SetViewport(0, viewport);
}

void LightAnimation::SubscribeToEvents()
{
    // Subscribe HandleUpdate() function for processing update events
    SubscribeToEvent(E_UPDATE, HANDLER(LightAnimation, HandleUpdate));
}

void LightAnimation::HandleUpdate(StringHash eventType, VariantMap& eventData)
{
    using namespace Update;

    // Take the frame time step, which is stored as a float
    float timeStep = eventData[P_TIMESTEP].GetFloat();
    
    // Update the camera animation state
    animationState_->AddTime(timeStep);
    animationState_->Apply();
}

[/code]

-------------------------

gunnar.kriik | 2017-01-02 00:59:46 UTC | #5

Only problem now is that while Blender uses the Z-up, the exported camera animation is not converted to Y-up, at least not while using Collada. This might be an issue with the Collada format, as the animations might be exported as-is from Blender.

-------------------------

