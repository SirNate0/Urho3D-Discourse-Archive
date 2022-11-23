syjgin | 2017-01-02 01:02:07 UTC | #1

As I can see, there are no example of loading scene, created in editor, in Samples folder. Maybe there are some other example, how to load such scene and access objects from C++?

-------------------------

syjgin | 2017-01-02 01:02:07 UTC | #2

So, now I have following project structure:
[ul]
[*]Build[/*]
[*]Source
[list]
[*]CMakeLists.txt[/*]  [*]mainApp.cpp[/*]  [*]mainApp.h[/*] [*]scenes
[list]
[*]mainMenu.xml[/*]  [*]uiLayout.xml[/*]
[/ul]
[/*] 
[/list:u]
[/*]
[/list:u]

On mainApp.cpp I'm trying to load scene . Maybe later I will have to use Deserializer class to read  xml, but for now for some reason I can't find this file:
[code]#include "mainApp.h"

DEFINE_APPLICATION_MAIN(MainApp)

MainApp::MainApp(Context* context): Application(context)
{
  
}


void MainApp::Start()
{
    Urho3D::Application::Start();
    // Called after engine initialization. Setup application & subscribe to events here
    SubscribeToEvent(E_KEYDOWN, HANDLER(MainApp, HandleKeyDown));
    LoadMainMenu();
}


void MainApp::HandleKeyDown(StringHash eventType, VariantMap& eventData)
{
	using namespace KeyDown;
        // Check for pressing ESC. Note the engine_ member variable for convenience access to the Engine object
        int key = eventData[P_KEY].GetInt();
        if (key == KEY_ESC)
            engine_->Exit();
}
void MainApp::Setup()
{
    Urho3D::Application::Setup();
}

void MainApp::Stop()
{
    Urho3D::Application::Stop();
}

void MainApp::LoadMainMenu()
{
    ResourceCache* cache = GetSubsystem<ResourceCache>();
    XMLFile *mainMenuScene = cache->GetResource<XMLFile>("scenes/mainMenu.xml");
    //ERROR: Could not find resource scenes/mainMenu.xml
}
[/code]

Why this error can be occurred?

-------------------------

JTippetts | 2017-01-02 01:02:08 UTC | #3

By default, Urho3D specifies the folders Data and CoreData (located in the root of the execution path) as the places to look for data. If you wish to have it look elsewhere, you need to specify the path(s) using the -p command line parameter, as per the [url=http://urho3d.github.io/documentation/1.32/_running.html]documentation[/url].

-------------------------

syjgin | 2017-01-02 01:02:09 UTC | #4

[quote="JTippetts"]By default, Urho3D specifies the folders Data and CoreData (located in the root of the execution path) as the places to look for data. If you wish to have it look elsewhere, you need to specify the path(s) using the -p command line parameter, as per the [url=http://urho3d.github.io/documentation/1.32/_running.html]documentation[/url].[/quote]

Thank you, now file can be found, but I still see only black screen. I saw the angelscript code to load the scene from ninja snow war, and wrote some analog with c++: [code]ResourceCache* cache = GetSubsystem<ResourceCache>();
    Scene *mainMenu = new Scene(context_);
    XMLFile *sceneFile = cache->GetResource<XMLFile>("Scenes/mainMenu.xml");
    mainMenu->LoadXML(sceneFile->GetRoot());[/code]
For now I have to setup camera? Is it some documentation about loading scene process exists? I found only few sentences there: urho3d.github.io/documentation/1.32/_scene_model.html

-------------------------

friesencr | 2017-01-02 01:02:10 UTC | #5

For a black screen make sure you are initializing the viewport.  A camera has to be assigned to a viewport.

There are no written tutorials on how to do something.  There are the c++ api docs which you found that describes the api, there is the the general documentation that explains urhos architecture and some of the decisions made in the engine, and there are the samples.  My recommendation is to pick a language (c++, angelscript, lua) and hit the samples.  The particular instance of loading a scene isn't well covered.  The documentation really only takes the api first approach, which is a bit unfortunate since urho's lightweight asset pipeline is pretty decent.

Here is the general documentation: [urho3d.github.io/documentation/1.32/index.html](http://urho3d.github.io/documentation/1.32/index.html)

Here is the c++ docs: [urho3d.github.io/documentation/1 ... tated.html](http://urho3d.github.io/documentation/1.32/annotated.html)

The samples are in the source tree.

C++ samples - Source/Samples
Angelscript - Bin/Data/Scripts
Lua - Bin/Data/LuaScripts

-------------------------

syjgin | 2017-01-02 01:02:14 UTC | #6

[quote="friesencr"]For a black screen make sure you are initializing the viewport.  A camera has to be assigned to a viewport.

There are no written tutorials on how to do something.  There are the c++ api docs which you found that describes the api, there is the the general documentation that explains urhos architecture and some of the decisions made in the engine, and there are the samples.  My recommendation is to pick a language (c++, angelscript, lua) and hit the samples.  The particular instance of loading a scene isn't well covered.  The documentation really only takes the api first approach, which is a bit unfortunate since urho's lightweight asset pipeline is pretty decent.

Here is the general documentation: [urho3d.github.io/documentation/1.32/index.html](http://urho3d.github.io/documentation/1.32/index.html)

Here is the c++ docs: [urho3d.github.io/documentation/1 ... tated.html](http://urho3d.github.io/documentation/1.32/annotated.html)

The samples are in the source tree.

C++ samples - Source/Samples
Angelscript - Bin/Data/Scripts
Lua - Bin/Data/LuaScripts[/quote]

Still can not display anything:(
Here is my MainApp.h:
[url]http://pastebin.com/tmFiKRmr[/url]
MainApp.cpp:
[url]http://pastebin.com/AbTzvE5M[/url]
Layout:
[url]http://pastebin.com/5XKqHStw[/url]
Log:
[url]http://pastebin.com/TiAZCycK[/url]

-------------------------

friesencr | 2017-01-02 01:02:14 UTC | #7

Loading the layout file will populate a ui component but it does not add it to the ui subsystem.  You will need to AddChild on the ui subsystem root node.

-------------------------

syjgin | 2017-01-02 01:02:17 UTC | #8

[quote="friesencr"]Loading the layout file will populate a ui component but it does not add it to the ui subsystem.  You will need to AddChild on the ui subsystem root node.[/quote]

Thank you, now I see my layout, but there are something wrong with styles, I think: [img]http://rghost.net/60061230/image.png[/img]

-------------------------

Mike | 2017-01-02 01:02:17 UTC | #9

Yes, try to use SetStyleAuto(true).

-------------------------

syjgin | 2017-01-02 01:02:17 UTC | #10

[quote="Mike"]Yes, try to use SetStyleAuto(true).[/quote]
No effect:(
I try [code]ResourceCache* cache = GetSubsystem<ResourceCache>();
    XMLFile *layout = cache->GetResource<XMLFile>("UI/mainMenu.xml");
    _loadedLayout = GetSubsystem<UI>()->LoadLayout(layout);
    _loadedLayout->SetStyleAuto();
    GetSubsystem<UI>()->GetRoot()->AddChild(_loadedLayout);[/code]
I also tried invoke SetStyleAuto() on RootElement, but this has no effect too

-------------------------

friesencr | 2017-01-02 01:02:17 UTC | #11

Did you load DefaultStyle.xml?

-------------------------

syjgin | 2017-01-02 01:02:19 UTC | #12

Now there is an example of loading scene and UI in Urho3D source, so I will examine it to find, what's was incorrect

-------------------------

