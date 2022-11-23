hypnotize | 2017-01-02 01:15:13 UTC | #1

Hey,

I'm a seazoned HTML5 game developer that decided to go into c++ games. I have noticed a strange behavior of Urho3d events behavior. I took code from this example and compiled it and when any key is being held both events E_KEYUP and E_KEYDOWN fire. What I would like to get is only the key up events. The weird thing is that i took the newest version of SDL2 and compiled it and it works absolutely perfect. Maybe there is something I don't know about URHO3D or I'm doing something wrong?
This is my code example:

[code]
#include <string>
#include <memory>
#include <fstream>
#include <sstream>
#include <iostream>

#include <Urho3D/Urho3D.h>
#include <Urho3D/Core/CoreEvents.h>
#include <Urho3D/Engine/Application.h>
#include <Urho3D/Engine/Engine.h>
#include <Urho3D/Input/Input.h>
#include <Urho3D/Input/InputEvents.h>
#include <Urho3D/Resource/ResourceCache.h>
#include <Urho3D/Resource/XMLFile.h>
#include <Urho3D/IO/Log.h>
#include <Urho3D/UI/UI.h>
#include <Urho3D/UI/Text.h>
#include <Urho3D/UI/Font.h>
#include <Urho3D/UI/Button.h>
#include <Urho3D/UI/UIEvents.h>
#include <Urho3D/UI/Window.h>
#include <Urho3D/Scene/Scene.h>
#include <Urho3D/Scene/SceneEvents.h>
#include <Urho3D/Graphics/Graphics.h>
#include <Urho3D/Graphics/Camera.h>
#include <Urho3D/Graphics/Renderer.h>
#include <Urho3D/Graphics/DebugRenderer.h>
#include <Urho3D/Graphics/Octree.h>

using namespace Urho3D;

/// SampleApplication main class mainly used for setup. The control is then given to the game states (starting with gs_main_menu).
class MultiverseApp : public Application{
public:
    
    SharedPtr<Scene> scene_;
    Node* cameraNode_;
    Urho3D::Text* window_text;
    SharedPtr<Urho3D::Window> window;
    Urho3D::Camera* camera_;

    MultiverseApp(Context * context) : Application(context) {}

    virtual void Setup() {
        engineParameters_["FullScreen"]=false;
        engineParameters_["WindowTitle"] = "Multiverse";
        engine_->SetMaxFps(60);
        GetSubsystem<Input>()->SetMouseVisible(true);
    }

    virtual void Start(){
        
        ResourceCache* cache=GetSubsystem<ResourceCache>();
        GetSubsystem<UI>()->GetRoot()->SetDefaultStyle(cache->GetResource<XMLFile>("UI/DefaultStyle.xml"));

        scene_=new Scene(context_);
        scene_->CreateComponent<Octree>();
        scene_->CreateComponent<DebugRenderer>();
        

        cameraNode_=scene_->CreateChild("Camera");
        cameraNode_->SetPosition(Vector3(0,0,0));
        cameraNode_->SetDirection(Vector3::FORWARD);
        camera_=cameraNode_->CreateComponent<Camera>();

        Renderer* renderer=GetSubsystem<Renderer>();
        SharedPtr<Viewport> viewport(new Viewport(context_,scene_,cameraNode_->GetComponent<Camera>()));
        renderer->SetViewport(0,viewport);
        renderer->SetShadowMapSize(1024);

        SubscribeToEvent(E_KEYDOWN,URHO3D_HANDLER(MultiverseApp, passKeyDown ));
        SubscribeToEvent(E_KEYUP,URHO3D_HANDLER(MultiverseApp, passKeyUp ));

        window=new Window(context_);
        GetSubsystem<UI>()->GetRoot()->AddChild(window);
        window->SetStyle("Window");
        window->SetSize(600,170);
        window->SetColor(Color(1,1,1));
        window->SetAlignment(HA_LEFT,VA_TOP);

        window_text=new Text(context_);
        window_text->SetFont(cache->GetResource<Font>("Fonts/Anonymous Pro.ttf"),14);
        window_text->SetColor(Color(1,1,1));
        window_text->SetAlignment(HA_LEFT,VA_TOP);
        window->AddChild(window_text);

    }

    virtual void Stop() { }

    void HandleUpdate(StringHash eventType, VariantMap& eventData){
        
        float timeStep=eventData[Update::P_TIMESTEP].GetFloat();

        std::string str="WASD, mouse and shift to move. T to toggle fill mode,\nG to toggle GUI, Tab to toggle mouse mode, Esc to quit.\n";
        {
            std::ostringstream ss;
            ss<<1/timeStep;
            std::string s(ss.str());
            str.append(s.substr(0,6));
        }
        str.append(" FPS ");
        String s(str.c_str(),str.size());
        window_text->SetText(s);
        
    }

    void passKeyDown(StringHash eventType, VariantMap& eventData) {
        if (eventType == E_KEYDOWN) {
        
            std::cout << "key down 1" << std::endl;
        
        }else if (eventType == E_KEYUP){
        
            std::cout << "key up 1" << std::endl;
        
        }
    }
    void passKeyUp(StringHash eventType,VariantMap& eventData) {
        using namespace KeyUp;
        int key=eventData[P_KEY].GetInt();
        
        if (eventType == E_KEYDOWN) {
        
            std::cout << "key down 2" << std::endl;
        
        }else if (eventType == E_KEYUP){
        
            std::cout << "key up 2" << std::endl;
        
        }
    }
    
};

URHO3D_DEFINE_APPLICATION_MAIN(MultiverseApp);
[/code]


Please take a look at the console output from this example. The keyup events should be fired only in case of actually releasing the key. And it is firing all the time with key pressed down. Any idea what is going on?


I subscribe to E_KEYUP

[code] SubscribeToEvent(E_KEYUP,URHO3D_HANDLER(MultiverseApp, passKeyUp ));[/code]

and hadle it with a method:

[code]void passKeyUp(StringHash eventType,VariantMap& eventData) {
        using namespace KeyUp;
        int key=eventData[P_KEY].GetInt();
        
        if (eventType == E_KEYDOWN) {
        
            std::cout << "key down 2" << std::endl;
        
        }else if (eventType == E_KEYUP){
        
            std::cout << "key up 2" << std::endl;
        
        }
    }[/code]

Yet the event on keypressed is still firing

-------------------------

weitjong | 2017-01-02 01:15:13 UTC | #2

We have a regression issue currently in our master branch after the commit to merge the SDL 2.0.5 upgrade. I thought I have already fixed it but apparently not.

-------------------------

hypnotize | 2017-01-02 01:15:14 UTC | #3

Ok,

so this is getting us somewhere! :smiley:

My assumption is that you were able to compile this example and reproduced the issues right? Is there any way I could help? I tried to look into the source code but I'm still not comfortable enough with Urho3D to fix it and push it upstream with a pull request. 


If this helps I'm running on:

[quote]No LSB modules are available.
Distributor ID:	Ubuntu
Description:	Ubuntu 16.04.1 LTS
Release:	16.04
Codename:	xenial

With gcc:
gcc --version
gcc (Ubuntu 5.4.0-6ubuntu1~16.04.4) 5.4.0 20160609[/quote]

Hope this helps anyone or that anyone else would not be surprised with the current behavior of events.

-------------------------

weitjong | 2017-01-02 01:15:14 UTC | #4

I did not use your code but as I said this is a known issue with Linux build after we merge SDL 2.0.5 upgrade. The issue is tracked in our GitHub issue tracker. I have performed a wrong fix and I have now reverted it back because it did not fix the regression issue completely as you have pointed out. I will make another attempt to fix it tomorrow (as it is kind of late here for me), assuming it has not be fixed by Lasse by then.

-------------------------

weitjong | 2017-01-02 01:15:15 UTC | #5

A quick fix was committed in the master branch last night. It requires ibus development package installed though. Still not too happy with this because in the past we don't need ibus. So, something else must have been changed on the SDL side that makes it depends on ibus to behave properly. I could be wrong though. Will investigate further when I have time.

-------------------------

hypnotize | 2017-01-02 01:15:16 UTC | #6

Great!

In this case I will build the library with the commit and try it out! Thank you for your help.  :wink:

-------------------------

weitjong | 2017-01-02 01:15:18 UTC | #7

Please use the latest commit instead ([github.com/urho3d/Urho3D/commit ... b1fbd68026](https://github.com/urho3d/Urho3D/commit/05690e0a36169779cc559fbefc5339b1fbd68026)). No need ibus-devel package anymore for it to behave as before.

-------------------------

