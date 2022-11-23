OMID-313 | 2017-02-13 14:39:12 UTC | #1

Hi all,

I'm using Urho3D on RaspberryPi.
I'd like to convert this code (_[source](http://discourse.urho3d.io/t/how-to-layer-scenes/740/3)_) from C++ to ActionScript:

    #include "common.h"
    #include "main.h"
    DEFINE_APPLICATION_MAIN(MyApp);
    MyApp::MyApp(Context* context) : Application(context)
    {
    		engineParameters_["WindowTitle"] = GetTypeName();
    		engineParameters_["FullScreen"] = false;
    		engineParameters_["Headless"] = false;
    		engineParameters_["WindowWidth"] = 1280;
    		engineParameters_["WindowHeight"] = 720;
    		engineParameters_["LogName"] = GetSubsystem<FileSystem>()->GetAppPreferencesDir("urho3d", "logs") + GetTypeName() + ".log";
    		engineParameters_["RenderPath"] = "Bin\CoreData\RenderPaths\Forward.xml";
    }
    void MyApp::Setup()
    {
            // Called before engine initialization. engineParameters_ member variable can be modified here
    }
    void MyApp::Start()
    {
    	Graphics* graphics = GetSubsystem<Graphics>();
    	Renderer* renderer = GetSubsystem<Renderer>();
    	ResourceCache* cache = GetSubsystem<ResourceCache>();
        // Called after engine initialization. Setup application & subscribe to events here
        SubscribeToEvent(E_KEYDOWN, HANDLER(MyApp, HandleKeyDown));
    	scene1 = SharedPtr<Scene>(new Scene(context_));
    	File sceneFile(context_, GetSubsystem<FileSystem>()->GetProgramDir() + "Data/Scenes/SceneA.xml", FILE_READ);
    	scene1->LoadXML(sceneFile);
    	scene2 = SharedPtr<Scene>(new Scene(context_));
    	File sceneFile2(context_, GetSubsystem<FileSystem>()->GetProgramDir() + "Data/Scenes/SceneB.xml", FILE_READ);
    	scene2->LoadXML(sceneFile2);
        camera1Node = scene1->GetChild("cameraNode", true);
    camera2Node = scene2->GetChild("cameraNode", true);

    camera1 = camera1Node->GetComponent<Camera>();
    camera2 = camera2Node->GetComponent<Camera>();

    viewport1 = new Viewport(context_, scene1, camera1);
    viewport2 = new Viewport(context_, scene2, camera2);


    overlayRenderPath = SharedPtr<RenderPath>(new RenderPath());
    overlayRenderPath->Load(cache->GetResource<XMLFile>("RenderPaths/ForwardTest.xml"));
    viewport2->SetRenderPath(overlayRenderPath);


    renderer->SetNumViewports(2);
    renderer->SetViewport(0, viewport1);
    renderer->SetViewport(1, viewport2);
    }
    void MyApp::Stop()
    {
            // Perform optional cleanup after main loop has terminated
    }
    void MyApp::HandleKeyDown(StringHash eventType, VariantMap& eventData)
    {
            using namespace KeyDown;
            // Check for pressing ESC. Note the engine_ member variable for convenience access to the Engine object
        int key = eventData[P_KEY].GetInt();
        if (key == KEY_ESC)
            engine_->Exit();
    }

How can I do this !?

Thanks for your time and support.

-------------------------

1vanK | 2017-02-13 14:51:32 UTC | #2

> ActionScript

AngelScript (it is different languages :) )

> I'd like to convert this code

Most of the code converted from/to AngelScript line to line (only syntax difference), if you know AngelScript ofc

-------------------------

1vanK | 2017-02-13 14:58:59 UTC | #3

only engineParameters_[] is command line parameters and should be set in *.sh launch file or in Data/CommandLine.txt

-------------------------

OMID-313 | 2017-02-13 15:04:28 UTC | #4

Thanks @1vanK for your quick reply.

Two questions:
1. How should I add the engine parameters to Data/CommandLine.txt ? Shall I edit them? Or copy exactly the same lines !?
2. In order to convert C++ to ActionScript (or AngelScript ? I got confused !! Which is for Urho3D !!?), I just need to copy all the lines and change the syntax? Are there better and easier solutions !?

Thanks.

-------------------------

1vanK | 2017-02-13 15:08:58 UTC | #5

> How should I add the engine parameters to Data/CommandLine.txt ? Shall I edit them? Or copy exactly the same lines !?

Write to  Data/CommandLine.txt same that you are using for launch Urho3DPlayer https://urho3d.github.io/documentation/HEAD/_running.html

-------------------------

