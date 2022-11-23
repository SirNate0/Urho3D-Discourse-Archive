Bluemoon | 2017-01-02 00:59:24 UTC | #1

Since Blender is my one and only 3D modeling suit (for now :question: ), I have gotten so used to its camera navigation and orbiting key combinations, so I thought of implementing a simple Orbiting Camera in Urho3D having blenders key combinations as follows

//These ones are already Implemented in Urho3D Editor
key_1    =    Front
Key_1 + ctrl =   Back
Key_3    =   Right
Key_3 + Ctrl = Left
Key_7    = Top
Key_7 + Ctrl  = Under
Key_W    = Forward
Key_S     =  Back

//Additional combinations
Alt + LMB     =  Orbit
Shift + Alt + LMB  = Pan
MouseWheel = Forward and Back

Below is a simple code that loads a plane and the ever popular mushroom  :smiley: just in case someone might need it

Urho3DSample.h
[code]
#ifndef __urho3dsample_h_
#define __urho3dsample_h_

#include <Application.h>
#include <Engine.h>
#include <InputEvents.h>
#include <Scene.h>
#include <Node.h>

enum CameraPosition
{
    CAM_FRONT = 100,
    CAM_BACK,
    CAM_RIGHT,
    CAM_LEFT,
    CAM_UP,
    CAM_DOWN
};

using namespace Urho3D;

class Urho3DSample : public Application
{
public:
    Urho3DSample(Urho3D::Context* context);
    
    virtual void Setup();
    virtual void Start();
    virtual void Stop();

    void HandleKeyDown(StringHash eventType, VariantMap& eventData);
    void HandleUpdate(StringHash eventType, VariantMap& eventData);

private:
    void CreateScene();
    void SetupViewport();

    void SetupOrbitingCam();
    void UpdateOrbitingCam();
    void SetCameraPosition(CameraPosition pos);


    void OnKeyPressed(int key);

    void SubscribeToEvents();

    SharedPtr<Scene> scene_;

    SharedPtr<Node> cameraNode_;
    SharedPtr<Node> camPitchNode_;
    SharedPtr<Node> camYawNode_;
    SharedPtr<Node> camBaseNode_;
};


#endif // #ifndef __urho3dsample_h_

[/code]

Urho3DSample.cpp
[code]
#include "Urho3DSample.h"



#include <Renderer.h>
#include <ResourceCache.h>
#include <Light.h>
#include <StaticModel.h>
#include <Model.h>
#include <Material.h>
#include <Camera.h>
#include <Viewport.h>
#include <CoreEvents.h>
#include <Input.h>
#include <Octree.h>


Urho3DSample::Urho3DSample(Urho3D::Context *context) : Application(context)
{
}

void Urho3DSample::Setup()
{
}

void Urho3DSample::Start()
{
    CreateScene();

    SetupOrbitingCam();

    SetupViewport();

    SubscribeToEvents();
}

void Urho3DSample::Stop()
{
}

void Urho3DSample::HandleKeyDown(Urho3D::StringHash eventType, Urho3D::VariantMap &eventData)
{
    using namespace Urho3D::KeyDown;
    // Check for pressing ESC. Note the engine_ member variable for convenience access to the Engine object
    int key = eventData[P_KEY].GetInt();
    if (key == Urho3D::KEY_ESC)
        engine_->Exit();
    else
    {
        OnKeyPressed(key);
    }
}

void Urho3DSample::HandleUpdate(StringHash eventType, VariantMap &eventData)
{
    UpdateOrbitingCam();
}

void Urho3DSample::CreateScene()
{
    ResourceCache* cache = GetSubsystem<ResourceCache>();
    scene_ = new Scene(context_);

    scene_->CreateComponent<Octree>();

    Node* planeNode = scene_->CreateChild("Plane");
    planeNode->SetScale(Vector3(100.0f, 1.0f, 100.0f));

    StaticModel* planeObject = planeNode->CreateComponent<StaticModel>();
    planeObject->SetModel(cache->GetResource<Model>("Models/Plane.mdl"));
    planeObject->SetMaterial(cache->GetResource<Material>("Materials/StoneTiled.xml"));

    Node* modelNode = scene_->CreateChild("ModelNode");
    modelNode->SetScale(0.3f);

    StaticModel* model = modelNode->CreateComponent<StaticModel>();
    model->SetModel(cache->GetResource<Model>("Models/Mushroom.mdl"));
    model->SetMaterial(cache->GetResource<Material>("Materials/Mushroom.xml"));


    Node* lightNode = scene_->CreateChild("DirectionalLightNode");
    lightNode->SetDirection(Vector3(0.6f, -1.0f, 0.8f));


    Light* light = lightNode->CreateComponent<Light>();
    light->SetLightType(LIGHT_DIRECTIONAL);
    light->SetCastShadows(true);
}

void Urho3DSample::SetupViewport()
{
    Renderer* renderer = GetSubsystem<Renderer>();

    SharedPtr<Viewport> viewport(new Viewport(context_, scene_, cameraNode_->GetComponent<Camera>()));
    renderer->SetViewport(0,viewport);
}

void Urho3DSample::SetupOrbitingCam()
{
    camBaseNode_ = scene_->CreateChild("Base Cam Node");
    camYawNode_ = camBaseNode_->CreateChild("Cam Yaw Node");
    camPitchNode_ = camYawNode_->CreateChild("Cam Pitch Node");

    cameraNode_ = camPitchNode_->CreateChild("Cam Node");
    cameraNode_->CreateComponent<Camera>();

    cameraNode_->TranslateRelative(Vector3(0,0,-10));
}

void Urho3DSample::UpdateOrbitingCam()
{
    Input* input = GetSubsystem<Input>();
    float dist;


    if(input->GetMouseButtonDown(MOUSEB_LEFT))
    {
        if(input->GetKeyDown(KEY_ALT) && input->GetKeyDown(KEY_SHIFT))
        {
            //Pan around the Screen
            dist = (cameraNode_->GetPosition().Length()) / 500;
            Matrix3 rotationMatrix = cameraNode_->GetWorldTransform().RotationMatrix();

            Vector3 direction = rotationMatrix * Vector3(input->GetMouseMoveX() * -dist, input->GetMouseMoveY() * dist,0);


            camBaseNode_->TranslateRelative(direction);

        }
        else if(input->GetKeyDown(KEY_ALT))
        {
            //Orbit at a pivot
            camPitchNode_->Pitch(input->GetMouseMoveY() * 0.25f);
            camYawNode_->Yaw(input->GetMouseMoveX() * 0.25f);

        }
    }
    else if(input->GetMouseMoveWheel() != 0)
    {
        cameraNode_->TranslateRelative(Vector3(0,0,input->GetMouseMoveWheel() * 0.5));
    }
    //In Forward and Backwards movement in case of laptop touchpad
    else if(input->GetKeyDown('W'))
    {
        cameraNode_->TranslateRelative(Vector3(0,0,0.07f));
    }
    else if(input->GetKeyDown('S'))
    {
        cameraNode_->TranslateRelative(Vector3(0,0,-0.07f));
    }
}

void Urho3DSample::SetCameraPosition(CameraPosition pos)
{
    camPitchNode_->SetRotation(Quaternion(0.0f,0.0f,0.0f));
    camYawNode_->SetRotation(Quaternion(0.0f,0.0f,0.0f));

    switch(pos)
    {
    //case CAM_FRONT:
    //there is no need for this since the cam is already
    //positioned at CAM_FRONT after the orientation of the cam nodes are
    //reset

    case CAM_BACK:
        camYawNode_->Yaw(180);
        break;
    case CAM_RIGHT:
        camYawNode_->Yaw(-90);
        break;
    case CAM_LEFT:
        camYawNode_->Yaw(90);
        break;
    case CAM_UP:
        camPitchNode_->Pitch(-90);
        break;
    case CAM_DOWN:
        camPitchNode_->Pitch(90);
        break;

    }
}

void Urho3DSample::OnKeyPressed(int key)
{
    Input* input = GetSubsystem<Input>();
    bool ctrlDown = input->GetKeyDown(KEY_CTRL);

    switch(key)
    {
    case '1':
        SetCameraPosition(ctrlDown ? CAM_BACK : CAM_FRONT);
        break;

    case '3':
        SetCameraPosition(ctrlDown ? CAM_LEFT : CAM_RIGHT);
        break;

    case '7':
        SetCameraPosition(ctrlDown ? CAM_UP :  CAM_DOWN );
        break;

    }

}

void Urho3DSample::SubscribeToEvents()
{
    SubscribeToEvent(E_KEYDOWN, HANDLER(Urho3DSample, HandleKeyDown));
    SubscribeToEvent(E_UPDATE, HANDLER(Urho3DSample, HandleUpdate));
}


DEFINE_APPLICATION_MAIN(Urho3DSample)
[/code]

-------------------------

