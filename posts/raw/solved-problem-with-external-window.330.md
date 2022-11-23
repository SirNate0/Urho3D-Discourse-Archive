Bluemoon | 2017-01-02 00:59:40 UTC | #1

There is a thread on this forum describing how to render Urho3d on an external window like that of wxWidgets or Qt, but I seem to be running into a frustrating problem here.
I have a wxFrame class that has a wxPanel I want to render Urho3d on. To make the work neat I created a class for Urho3d just like the dristributed Application class and added an InitialiseUrho3D function to it in which I will pass in the wxPanel pointer to be used for rendering. What this function does is to setup engine parameters, initialise the engine, create scene and gets ready to start rendering frame which will be triggered by a timer in the wxFrame. The engine_ property of my Urho3d class is instanciated in the class constructor. After the class is instanciated in the wxFrame constructor its InitialiseUrho3D function is called.
But the problem is that the Engine subsystem gets invalidated automatically when this function returns thereby causing the program to crash when an attempt is made to reference the engine. 
I was able to step into the code to find this out cos while in the InitialiseUrho3D function the Engine subsystem was valid but afterwards in any other function of the class it is invalid. I first encountered this while trying to implement it in Qt and decided to test it out on wxWidgets
What exactly am I doing wrong or is it a bug? I'm using Urho3D v1.31, wxWidgets v3.0.0, Visual C++ 2010 Express Edition on a Window Vista System

-------------------------

aster2013 | 2017-01-02 00:59:40 UTC | #2

Hi, welcome to our forum.

You said the engine becomes invalid, can you show you code here?

I have wrote a Qt based editor that uses external window. You can get it from [url]https://github.com/aster2013/ParticleEditor2D[/url]. I think it will helpful help for you.

-------------------------

Bluemoon | 2017-01-02 00:59:40 UTC | #3

Here is the code using wxWidgets:

First is the urho3DClass definition and Implementation
[b]Urho3DClass.h[/b]
[code]
#ifndef URHO3DCLASS_H
#define URHO3DCLASS_H

#include <Context.h>
#include <Object.h>
#include <Precompiled.h>
#include <Application.h>
#include <Engine.h>
#include <IOEvents.h>
#include <Log.h>
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
#include <Scene.h>
#include <Graphics.h>
#include <ProcessUtils.h>

//For wxPanel
#include <wx/panel.h>


class Urho3DClass : public Urho3D::Object
{
    OBJECT(Urho3DClass)
public:
    //Constructor
    Urho3DClass(Urho3D::Context* context);

    //Initialize the Engine
    void Initialize(wxPanel *urhoControl);

    //Stop The Engine
    void StopUrho3D();

    //Handle Update Event
    void HandleUpdate(Urho3D::StringHash eventType, Urho3D::VariantMap &eventData);

    //Render One Frame
    void RenderFrame();

protected:

    //Create The Scene
    void CreateScene();

    //Setup Rendering Viewport
    void SetupViewport();

    //Subscribe to Events
    void SubscribeToEvents();

    Urho3D::SharedPtr<Urho3D::Engine> engine_;
    Urho3D::SharedPtr<Urho3D::Scene> scene_;
    Urho3D::SharedPtr<Urho3D::Node> cameraNode_;


};

#endif // URHO3DCLASS_H

[/code]

[b]Urho3DClass.cpp[/b]
[code]
#include "Urho3DClass.h"

using namespace Urho3D;

Urho3DClass::Urho3DClass(Urho3D::Context *context) :
    Object(context)
{
    //Instance the Engine
    engine_ = new Engine(context);
}

void Urho3DClass::StopUrho3D()
{
    engine_->Exit();
}


void Urho3DClass::Initialize(wxPanel *urhoControl)
{
    VariantMap engineParameters_;

    engineParameters_["ResourcePaths"] = "CoreData;Assets";
    engineParameters_["LogName"]   = "wxUrho.log";
    engineParameters_["ExternalWindow"] = urhoControl->GetHandle();
    engineParameters_["FullScreen"]  = false;
    engineParameters_["WindowResizable"] = true;

    engine_->Initialize(engineParameters_);

    CreateScene();
    SetupViewport();
}

void Urho3DClass::HandleUpdate(StringHash eventType, VariantMap &eventData)
{

}

void Urho3DClass::RenderFrame()
{
   engine_->RunFrame();
}

void Urho3DClass::CreateScene()
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

    cameraNode_ = scene_->CreateChild("CamNode");
    cameraNode_->CreateComponent<Camera>();
    cameraNode_->Translate(Vector3(0,0,-10));
}

void Urho3DClass::SetupViewport()
{

    Renderer* renderer = GetSubsystem<Renderer>();

    SharedPtr<Viewport> viewport(new Viewport(context_, scene_, cameraNode_->GetComponent<Camera>()));
    renderer->SetViewport(0,viewport);
}

void Urho3DClass::SubscribeToEvents()
{
    SubscribeToEvent(E_UPDATE, HANDLER(Urho3DClass, HandleUpdate));
}

[/code]


The following is the MainFrame code. MainFrame class derives from MainFramebase class which is simply a GUI implementation that defines its GUI elements like mRenderPanel which is a wxPanel for rendering,  mTimer (wxTimer) which is a timer and a file menu containing menu items Run and Exit. Clicking on Run starts the mTimer which triggers the rendering of the engine at each timer tick (or fire). The Exit menu simply exits the game. The implementation of their various event handlers is done in MainFrame.

[b]MainFrame.h[/b]
[code]
#ifndef MAINFRAME_H
#define MAINFRAME_H

//MainFrameBase include header
#include "gui.h"

//Urho3DClass header
#include "Urho3DClass.h"

class MainFrame : public MainFrameBase
{
public:
      MainFrame( wxWindow *parent );
      virtual ~MainFrame();

protected:


      //Urho3dClass Module
      Urho3D::SharedPtr<Urho3DClass> gameEngine_;

      //Set The Urho3D Class
      void SetupGameEngine();
        
      
      ///Event Handlers
      //Render Panel resized Handler
      void OnPanelResize(wxSizeEvent& event);
      //Frame Close Handler
      virtual void OnCloseFrame( wxCloseEvent& event );
      //Exit Menu Clicked Handler
      virtual void OnExitClick( wxCommandEvent& event );
      //Timer Fired Handler causes the Game engine to Render a Frame
      virtual void OnTimerFire( wxTimerEvent& event );
      //Run Menu Clicked Handler
      virtual void OnMenuRun(wxCommandEvent &event);


};


#endif // MAINFRAME_H

[/code]

[b]MainFrame.cpp[/b]
[code]
#include "MainFrame.h"


MainFrame::MainFrame(wxWindow *parent) : MainFrameBase( parent )
{
    mRenderPanel->Connect( wxEVT_SIZE,  wxSizeEventHandler(MainFrame::OnPanelResize), NULL, this);
    SetupGameEngine();
}

MainFrame::~MainFrame()
{
}

void MainFrame::OnCloseFrame(wxCloseEvent& event)
{
    mTimer.Stop();
    gameEngine_->StopUrho3D();

    mRenderPanel->Disconnect( wxEVT_SIZE,  wxSizeEventHandler(MainFrame::OnPanelResize), NULL, this);

    Destroy();
}

void MainFrame::OnExitClick(wxCommandEvent& event)
{
    Close();
}

void MainFrame::OnTimerFire(wxTimerEvent &event)
{
    gameEngine_->RenderFrame();
}

void MainFrame::OnMenuRun(wxCommandEvent &event)
{
    mTimer.Start(30);
}

void MainFrame::OnPanelResize(wxSizeEvent &event)
{

}

void MainFrame::SetupGameEngine()
{
    Urho3D::SharedPtr<Urho3D::Context> context(new Urho3D::Context());
    gameEngine_ = new Urho3DClass(context);
    gameEngine_->Initialize(mRenderPanel);
}

[/code]

-------------------------

aster2013 | 2018-11-06 14:19:27 UTC | #4

[quote]
```
void MainFrame::SetupGameEngine()
{
    Urho3D::SharedPtr<Urho3D::Context> context(new Urho3D::Context());
    gameEngine_ = new Urho3DClass(context);
    gameEngine_->Initialize(mRenderPanel);
}
```
[/quote]

context is local variance. please change it.

-------------------------

Bluemoon | 2017-01-02 00:59:41 UTC | #5

Thanks You so much aster2013... I failed to take that into concideration.

Now its working :slight_smile:

-------------------------

dmortensen30 | 2017-01-02 01:10:24 UTC | #6

Hello i am new in here and i am trying to create a game engine using c++ and of course Urho3d, i am currently using wxWidgets for my ui interface and i am having serious issues understanding these scripts bluemoon provided, along with aster's comment on changing the context... is there anybody who can clarify what it means by changing a local variance or if these scripts are outdated by a mass date? i am using Urho3D at least from this year (2016). thanks in advance

-------------------------

