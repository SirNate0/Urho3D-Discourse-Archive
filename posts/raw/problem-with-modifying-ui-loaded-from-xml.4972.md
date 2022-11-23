z80 | 2019-02-27 02:05:15 UTC | #1

Hello!

Urho3D is taken from master branch.
I experience a problem with UI. If UI is loaded from an XML file I can't modify it. For example, 
    ResourceCache * cache = GetSubsystem<ResourceCache>();
    XMLFile * f = cache->GetResource<XMLFile>( "UI/DesignSave.xml" );
    UI * ui = GetSubsystem<UI>();
    UIElement * uiRoot = ui->GetRoot();
    SharedPtr<UIElement> e = ui->LoadLayout( f );
    ui->GetRoot()->AddChild( e );
    e->RemoveAllChildren(); // This line does internally clears "children_" array. But visually window remains unchanged.

    The same happens when I try to add UI elements into a window loaded from an XML file. However, If I create a UI without loading it from a file it works fine.

    Would one, please, let me know what might be wrong.
    
    Thank you!

-------------------------

Leith | 2019-02-27 10:38:36 UTC | #2

[code]
// Try to open the file in read-only mode
File* file = new File( context_, sceneFile);
// If we succeeded, set the "busy" flag
isSceneLoading = file->IsOpen();

gamescene_->LoadAsyncXML(file, LOAD_SCENE_AND_RESOURCES);
[/code]
Use this guy

Also, 
SubscribeToEvent(E_ASYNCLOADFINISHED, URHO3D_HANDLER(ClassName, OnSceneLoaded));

This way, the app rendering and update is not frozen during loading (we can get progress and do stuff) and we get notified when loading is done, and get handed a new scene object:) I spent week one on making sure I could do that stuff.

This is also the major reasoning behind my choice to start with a gamestate manager, a base gamestate class, and several derived gamestates, such as loadingstate and gameplaystate and introstate and such.

-------------------------

