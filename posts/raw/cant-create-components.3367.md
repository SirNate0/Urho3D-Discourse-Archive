lazypenguin | 2017-07-19 01:11:04 UTC | #1

Hey all,

Having a strange error. I have blank new project that compiles but I get a strange error at runtime when trying to create any components. These aren't custom but the default provided by Urho. This line:

```c++
scene->CreateComponent<Octree>();
```
triggers this error:

```c++
ERROR: Could not create unknown component type 2F457EF2
```

I tried to debug it myself but wasn't having much luck. Would appreciate any insight. Here is the full source for the application:


[details=Source]
```C++
#include <Urho3D/Core/CoreEvents.h>
#include <Urho3D/Engine/Application.h>
#include <Urho3D/Engine/Engine.h>
#include <Urho3D/Graphics/Graphics.h>
#include <Urho3D/Graphics/Light.h>
#include <Urho3D/Graphics/Octree.h>
#include <Urho3D/Graphics/Renderer.h>
#include <Urho3D/Input/InputEvents.h>
#include <Urho3D/Resource/ResourceCache.h>
#include <Urho3D/Scene/Scene.h>
#include <Urho3D/Scene/Node.h>

using namespace Urho3D;

class MainApplication : public Application
{
    URHO3D_OBJECT(MainApplication, Application)

public:
    MainApplication(Context* context) :
        Application(context)
    {
    }

    virtual void Setup()
    {
        ResourceCache* cache = GetSubsystem<ResourceCache>();
        SharedPtr<Scene> scene;
        scene = new Scene(context_);
        
        scene->CreateComponent<Octree>();
        
        /*
        Node* lightNode = scene->CreateChild("LightNode");
        lightNode->SetDirection(Vector3(0.6f, -1.0f, 0.8f));
        Light* light = lightNode->CreateComponent<Light>();
        light->SetLightType(LIGHT_DIRECTIONAL);
        */
    }

    virtual void Start()
    {

    SubscribeToEvent(E_KEYDOWN, URHO3D_HANDLER(MainApplication, HandleKeyDown));
    }

    virtual void Stop()
    {
    }

    void HandleKeyDown(StringHash eventType, VariantMap& eventData)
    {
    using namespace KeyDown;
        int key = eventData[P_KEY].GetInt();
        if (key == KEY_ESCAPE) 
        {
            engine_ -> Exit();
        }
    }
};

URHO3D_DEFINE_APPLICATION_MAIN(MainApplication);
```
[/details]

-------------------------

SirNate0 | 2017-07-19 01:39:04 UTC | #2

I think you need to move all the Setup code to the Start function, a I don't think the engine is actually initialized at that point.

-------------------------

lazypenguin | 2017-07-19 01:38:49 UTC | #3

I'm an idiot, thank you!!

-------------------------

