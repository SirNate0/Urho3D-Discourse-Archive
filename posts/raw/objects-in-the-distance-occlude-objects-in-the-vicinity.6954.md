heytao | 2021-08-08 09:59:13 UTC | #1

Hello, everyone, 
I follow the code of [Sample 10 RenderToTexture](https://github.com/urho3d/Urho3D/blob/1.7.1/Source/Samples/10_RenderToTexture/RenderToTexture.cpp) to make a transformation.

Change one screen to two screens, and place the two screens face to face (Pic1).
![pic1|620x500](upload://jSmKNjeTQ16mCNUT1U4rANJZct5.jpeg)

When I (the camera) is close to the screens, everything is normal, and the screen at a distance can block the screen at a distance (as shown in Pic2, Pic3).
![pic2|620x500](upload://xdzhOGQDST0xI5u1iiUVI23WPQa.jpeg)
![pic3|620x500](upload://fwEIqKJ9vwhhW0NtaGqqE0fbjzd.jpeg)


When I (the camera) is far away from the screens, then strange things happen, the screen in the distance will block the screen in the vicinity (Pic4, Pic5, Pic6).
![pic4|620x500](upload://7Cfp2hPmAfMzd1ogcnElz7NpeWa.jpeg)
![pic5|620x500](upload://bRxlnnRNkDuxbJdbLtxtsLeuY3u.jpeg)
![pic6|620x500](upload://pX59FT0cOvTQwldRsBxYzmSXQf9.jpeg)


I tried to modify various modes through `renderTexture->SetFilterMode`, but no effect;
I tried to set it to 0 and 1 through `screenTexture->SetNumLevels`, but it had no effect;
I tried to render a normal jpg image onto the texture, the same problem was also true.


Does anyone know how to solve this problem? 
thanks.



Urho3d version: 1.7.1


test code below:
```cpp
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
#include <Urho3D/Engine/Engine.h>
#include <Urho3D/Graphics/Camera.h>
#include <Urho3D/Graphics/Graphics.h>
#include <Urho3D/Graphics/Material.h>
#include <Urho3D/Graphics/Model.h>
#include <Urho3D/Graphics/Octree.h>
#include <Urho3D/Graphics/Renderer.h>
#include <Urho3D/Graphics/RenderSurface.h>
#include <Urho3D/Graphics/StaticModel.h>
#include <Urho3D/Graphics/Technique.h>
#include <Urho3D/Graphics/Texture2D.h>
#include <Urho3D/Graphics/Zone.h>
#include <Urho3D/Input/Input.h>
#include <Urho3D/Resource/ResourceCache.h>
#include <Urho3D/Scene/Scene.h>
#include <Urho3D/UI/Font.h>
#include <Urho3D/UI/Text.h>
#include <Urho3D/UI/UI.h>

#include "RenderToTexture.h"
#include "Rotator.h"

#include <Urho3D/DebugNew.h>

URHO3D_DEFINE_APPLICATION_MAIN(RenderToTexture)

RenderToTexture::RenderToTexture(Context* context) :
    Sample(context)
{
    // Register an object factory for our custom Rotator component so that we can create them to scene nodes
    context->RegisterFactory<Rotator>();
}

void RenderToTexture::Start()
{
    // Execute base class startup
    Sample::Start();

    // Create the scene content
    CreateScene();

    // Create the UI content
    CreateInstructions();

    // Setup the viewport for displaying the scene
    SetupViewport();

    // Hook up to the frame update events
    SubscribeToEvents();

    // Set the mouse mode to use in the sample
    Sample::InitMouseMode(MM_RELATIVE);
}

void RenderToTexture::CreateScene()
{
    ResourceCache* cache = GetSubsystem<ResourceCache>();

    {
        // Create the scene which will be rendered to a texture
        rttScene_ = new Scene(context_);

        // Create octree, use default volume (-1000, -1000, -1000) to (1000, 1000, 1000)
        rttScene_->CreateComponent<Octree>();

        // Create a Zone for ambient light & fog control
        Node* zoneNode = rttScene_->CreateChild("Zone");
        Zone* zone = zoneNode->CreateComponent<Zone>();
        // Set same volume as the Octree, set a close bluish fog and some ambient light
        zone->SetBoundingBox(BoundingBox(-1000.0f, 1000.0f));
        zone->SetAmbientColor(Color(0.05f, 0.1f, 0.15f));
        //zone->SetFogColor(Color(0.1f, 0.2f, 0.3f));
        zone->SetFogColor(Color(0.4f, 0.6f, 0.8f));
        zone->SetFogStart(10.0f);
        zone->SetFogEnd(100.0f);

        // Create randomly positioned and oriented box StaticModels in the scene
        const unsigned NUM_OBJECTS = 2000;
        for (unsigned i = 0; i < NUM_OBJECTS; ++i)
        {
            Node* boxNode = rttScene_->CreateChild("Box");
            boxNode->SetPosition(Vector3(Random(200.0f) - 100.0f, Random(200.0f) - 100.0f, Random(200.0f) - 100.0f));
            // Orient using random pitch, yaw and roll Euler angles
            boxNode->SetRotation(Quaternion(Random(360.0f), Random(360.0f), Random(360.0f)));
            StaticModel* boxObject = boxNode->CreateComponent<StaticModel>();
            boxObject->SetModel(cache->GetResource<Model>("Models/Box.mdl"));
            boxObject->SetMaterial(cache->GetResource<Material>("Materials/Stone.xml"));

            // Add our custom Rotator component which will rotate the scene node each frame, when the scene sends its update event.
            // Simply set same rotation speed for all objects
            Rotator* rotator = boxNode->CreateComponent<Rotator>();
            rotator->SetRotationSpeed(Vector3(10.0f, 20.0f, 30.0f));
        }

        // Create a camera for the render-to-texture scene. Simply leave it at the world origin and let it observe the scene
        rttCameraNode_ = rttScene_->CreateChild("Camera");
        Camera* camera = rttCameraNode_->CreateComponent<Camera>();
        camera->SetFarClip(100.0f);

        // Create a point light to the camera scene node
        Light* light = rttCameraNode_->CreateComponent<Light>();
        light->SetLightType(LIGHT_POINT);
        light->SetRange(30.0f);
    }

    {
        // Create the scene in which we move around
        scene_ = new Scene(context_);

        // Create octree, use also default volume (-1000, -1000, -1000) to (1000, 1000, 1000)
        scene_->CreateComponent<Octree>();

        // Create a Zone component for ambient lighting & fog control
        Node* zoneNode = scene_->CreateChild("Zone");
        Zone* zone = zoneNode->CreateComponent<Zone>();
        zone->SetBoundingBox(BoundingBox(-1000.0f, 1000.0f));
        zone->SetAmbientColor(Color(0.1f, 0.1f, 0.1f));
        zone->SetFogStart(100.0f);
        zone->SetFogEnd(300.0f);

        // Create a directional light without shadows
        Node* lightNode = scene_->CreateChild("DirectionalLight");
        lightNode->SetDirection(Vector3(0.5f, -1.0f, 0.5f));
        Light* light = lightNode->CreateComponent<Light>();
        light->SetLightType(LIGHT_DIRECTIONAL);
        //light->SetColor(Color(0.2f, 0.2f, 0.2f));
        light->SetColor(Color(0.8f, 0.8f, 0.8f));
        light->SetSpecularIntensity(1.0f);

        // Create a "floor" consisting of several tiles
        for (int y = -5; y <= 5; ++y)
        {
            for (int x = -5; x <= 5; ++x)
            {
                Node* floorNode = scene_->CreateChild("FloorTile");
                floorNode->SetPosition(Vector3(x * 20.5f, -0.5f, y * 20.5f));
                floorNode->SetScale(Vector3(20.0f, 1.0f, 20.f));
                StaticModel* floorObject = floorNode->CreateComponent<StaticModel>();
                floorObject->SetModel(cache->GetResource<Model>("Models/Box.mdl"));
                floorObject->SetMaterial(cache->GetResource<Material>("Materials/Stone.xml"));
            }
        }

        // Create a "screen" like object for viewing the second scene. Construct it from two StaticModels, a box for the frame
        // and a plane for the actual view
        {
            Node* boxNode = scene_->CreateChild("ScreenBox");
            boxNode->SetPosition(Vector3(0.0f, 10.0f, 0.0f));
            boxNode->SetScale(Vector3(21.0f, 16.0f, 0.5f));
            StaticModel* boxObject = boxNode->CreateComponent<StaticModel>();
            boxObject->SetModel(cache->GetResource<Model>("Models/Box.mdl"));
            boxObject->SetMaterial(cache->GetResource<Material>("Materials/Stone.xml"));
            //boxObject->GetMaterial()->GetTexture(TU_DIFFUSE)->SetNumLevels(4);
            //boxObject->GetMaterial()->GetTexture(TU_DIFFUSE)->SetFilterMode(FILTER_DEFAULT);


            Node* screenNode = scene_->CreateChild("Screen");
            screenNode->SetPosition(Vector3(0.0f, 10.0f, -0.27f));
            screenNode->SetRotation(Quaternion(-90.0f, 0.0f, 0.0f));
            screenNode->SetScale(Vector3(20.0f, 0.0f, 15.0f));
            StaticModel* screenObject = screenNode->CreateComponent<StaticModel>();
            screenObject->SetModel(cache->GetResource<Model>("Models/Plane.mdl"));

            // Create a renderable texture (1024x768, RGB format), enable bilinear filtering on it
            SharedPtr<Texture2D> renderTexture(new Texture2D(context_));
            renderTexture->SetSize(1024, 768, Graphics::GetRGBFormat(), TEXTURE_RENDERTARGET);
            renderTexture->SetFilterMode(FILTER_BILINEAR);
            //renderTexture->SetFilterMode(MAX_FILTERMODES);
            //renderTexture->SetNumLevels(4);

            // Create a new material from scratch, use the diffuse unlit technique, assign the render texture
            // as its diffuse texture, then assign the material to the screen plane object
            SharedPtr<Material> renderMaterial(new Material(context_));
            renderMaterial->SetTechnique(0, cache->GetResource<Technique>("Techniques/DiffUnlit.xml"));
            renderMaterial->SetTexture(TU_DIFFUSE, renderTexture);
            // Since the screen material is on top of the box model and may Z-fight, use negative depth bias
            // to push it forward (particularly necessary on mobiles with possibly less Z resolution)
            renderMaterial->SetDepthBias(BiasParameters(-0.001f, 0.0f));
            screenObject->SetMaterial(renderMaterial);

            // Get the texture's RenderSurface object (exists when the texture has been created in rendertarget mode)
            // and define the viewport for rendering the second scene, similarly as how backbuffer viewports are defined
            // to the Renderer subsystem. By default the texture viewport will be updated when the texture is visible
            // in the main view
            RenderSurface* surface = renderTexture->GetRenderSurface();
            SharedPtr<Viewport> rttViewport(new Viewport(context_, rttScene_, rttCameraNode_->GetComponent<Camera>()));
            surface->SetViewport(0, rttViewport);
        }





        // +++++++++++++++++++    ADD SECOND SCREEN.  ++++++++++++++++++++++
        // Create a "screen" like object for viewing the second scene. Construct it from two StaticModels, a box for the frame
        // and a plane for the actual view
        {
          Node* boxNode = scene_->CreateChild("ScreenBox");
          boxNode->SetPosition(Vector3(0.0f, 10.0f, -20.0f));
          boxNode->SetScale(Vector3(21.0f, 16.0f, 0.5f));
          StaticModel* boxObject = boxNode->CreateComponent<StaticModel>();
          boxObject->SetModel(cache->GetResource<Model>("Models/Box.mdl"));
          boxObject->SetMaterial(cache->GetResource<Material>("Materials/Stone.xml"));
          //boxObject->GetMaterial()->GetTexture(TU_DIFFUSE)->SetNumLevels(4);
          //boxObject->GetMaterial()->GetTexture(TU_DIFFUSE)->SetFilterMode(FILTER_DEFAULT);


          Node* screenNode = scene_->CreateChild("Screen");
          screenNode->SetPosition(Vector3(0.0f, 10.0f, -19.57f));
          screenNode->SetRotation(Quaternion(-90.0f, 0.0f, 180.0f));
          screenNode->SetScale(Vector3(20.0f, 0.0f, 15.0f));
          StaticModel* screenObject = screenNode->CreateComponent<StaticModel>();
          screenObject->SetModel(cache->GetResource<Model>("Models/Plane.mdl"));

          // Create a renderable texture (1024x768, RGB format), enable bilinear filtering on it
          SharedPtr<Texture2D> renderTexture(new Texture2D(context_));
          renderTexture->SetSize(1024, 768, Graphics::GetRGBFormat(), TEXTURE_RENDERTARGET);
          renderTexture->SetFilterMode(FILTER_BILINEAR);
          //renderTexture->SetFilterMode(MAX_FILTERMODES);
          //renderTexture->SetNumLevels(4);

          // Create a new material from scratch, use the diffuse unlit technique, assign the render texture
          // as its diffuse texture, then assign the material to the screen plane object
          SharedPtr<Material> renderMaterial(new Material(context_));
          renderMaterial->SetTechnique(0, cache->GetResource<Technique>("Techniques/DiffUnlit.xml"));
          renderMaterial->SetTexture(TU_DIFFUSE, renderTexture);
          // Since the screen material is on top of the box model and may Z-fight, use negative depth bias
          // to push it forward (particularly necessary on mobiles with possibly less Z resolution)
          renderMaterial->SetDepthBias(BiasParameters(-0.001f, 0.0f));
          screenObject->SetMaterial(renderMaterial);

          // Get the texture's RenderSurface object (exists when the texture has been created in rendertarget mode)
          // and define the viewport for rendering the second scene, similarly as how backbuffer viewports are defined
          // to the Renderer subsystem. By default the texture viewport will be updated when the texture is visible
          // in the main view
          RenderSurface* surface = renderTexture->GetRenderSurface();
          SharedPtr<Viewport> rttViewport(new Viewport(context_, rttScene_, rttCameraNode_->GetComponent<Camera>()));
          surface->SetViewport(0, rttViewport);
        }




        // Create the camera which we will move around. Limit far clip distance to match the fog
        cameraNode_ = scene_->CreateChild("Camera");
        Camera* camera = cameraNode_->CreateComponent<Camera>();
        camera->SetFarClip(300.0f);

        // Set an initial position for the camera scene node above the plane
        cameraNode_->SetPosition(Vector3(0.0f, 7.0f, -30.0f));
    }
}

void RenderToTexture::CreateInstructions()
{
    ResourceCache* cache = GetSubsystem<ResourceCache>();
    UI* ui = GetSubsystem<UI>();

    // Construct new Text object, set string to display and font to use
    Text* instructionText = ui->GetRoot()->CreateChild<Text>();
    instructionText->SetText("Use WASD keys and mouse/touch to move");
    instructionText->SetFont(cache->GetResource<Font>("Fonts/Anonymous Pro.ttf"), 15);

    // Position the text relative to the screen center
    instructionText->SetHorizontalAlignment(HA_CENTER);
    instructionText->SetVerticalAlignment(VA_CENTER);
    instructionText->SetPosition(0, ui->GetRoot()->GetHeight() / 4);
}

void RenderToTexture::SetupViewport()
{
    Renderer* renderer = GetSubsystem<Renderer>();

    // Set up a viewport to the Renderer subsystem so that the 3D scene can be seen
    SharedPtr<Viewport> viewport(new Viewport(context_, scene_, cameraNode_->GetComponent<Camera>()));
    renderer->SetViewport(0, viewport);
}

void RenderToTexture::MoveCamera(float timeStep)
{
    // Do not move if the UI has a focused element (the console)
    if (GetSubsystem<UI>()->GetFocusElement())
        return;

    Input* input = GetSubsystem<Input>();

    // Movement speed as world units per second
    const float MOVE_SPEED = 20.0f;
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
}

void RenderToTexture::SubscribeToEvents()
{
    // Subscribe HandleUpdate() function for processing update events
    SubscribeToEvent(E_UPDATE, URHO3D_HANDLER(RenderToTexture, HandleUpdate));
}

void RenderToTexture::HandleUpdate(StringHash eventType, VariantMap& eventData)
{
    using namespace Update;

    // Take the frame time step, which is stored as a float
    float timeStep = eventData[P_TIMESTEP].GetFloat();

    // Move the camera, scale movement with time step
    MoveCamera(timeStep);
}

```

-------------------------

vmost | 2021-08-08 07:44:48 UTC | #2

I know this isn't helpful but... oh the joys of floating point numbers.

-------------------------

Eugene | 2021-08-08 14:03:14 UTC | #3

That’s depth bias for you. It can solve issues, it can create issues.
Consider not using depth bias by default.

-------------------------

heytao | 2021-08-08 14:10:45 UTC | #4

@Eugene 
Thank you for your answer.
After deleting this line  `renderMaterial->SetDepthBias(BiasParameters(-0.001f, 0.0f));`, everything returned to normal.
I also found that changing the parameter `-0.001` to `-0.00001` can alleviate the problem to a certain extent.

When do I need to consider using `depth bias`?
Should I delete `SetDepthBias` or change the parameter to be small enough?

-------------------------

Eugene | 2021-08-08 14:20:55 UTC | #5

Depth bias is basically magic constant that offsets perceived depth one way or another.

Good approach would be to try to make your scene look good without any biases by arranging geometry properly. If you fail to do so, use minimum sufficient bias.

I think the only “mandatory” bias in Urho are decal materials because decals are created right next to parent geometry. Use minimal bias value which is sufficient for your game.

-------------------------

heytao | 2021-08-08 15:06:29 UTC | #6

@Eugene 
Thank you again for your help.
Your answer made me feel the strength of urho, but also the warmth of the urho community.
Have a nice weekend, brother.

-------------------------

