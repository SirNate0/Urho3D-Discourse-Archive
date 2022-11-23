vivienneanthony | 2017-01-02 01:03:14 UTC | #1

Hi

I tried two types of codes and neither is working. Hmmm. So the cursor is the first thing I start before any UI is added.

Vivienne



The start of my main code is
[code]/// Main program execution code
void ExistenceClient::Start()
{
    /// Execute base class startup
    ExistenceApp::Start();

    ResourceCache* cache = GetSubsystem<ResourceCache>();
    XMLFile* style = cache->GetResource<XMLFile>("UI/DefaultStyle.xml");
    FileSystem * filesystem = GetSubsystem<FileSystem>();

    /// create variables (urho3d)
    String additionresourcePath;

    additionresourcePath.Append(filesystem->GetProgramDir().CString());
    additionresourcePath.Append("Resources/");

    /// add resource path to last
    cache -> AddResourceDir(additionresourcePath);

    /// Initialize rudimentary state handler
    ExistenceGameState.Start();

    /// Configure rudimentary state handler
    ExistenceGameState.SetUIState(UI_NONE);
    ExistenceGameState.SetGameState(STATE_MAIN);


    CreateCursor();
[/code]

Code 2
[code]
int  ExistenceClient::CreateCursor(void)
{

    /// Define Resouces
    ResourceCache* cache = GetSubsystem<ResourceCache>();
    Renderer* renderer = GetSubsystem<Renderer>();
    Graphics* graphics = GetSubsystem<Graphics>();
    UI* ui = GetSubsystem<UI>();
    FileSystem * filesystem = GetSubsystem<FileSystem>();

    // Create a Cursor UI element because we want to be able to hide and show it at will. When hidden, the mouse cursor will
    // control the camera, and when visible, it will point the raycast target
    XMLFile* style = cache->GetResource<XMLFile>("UI/DefaultStyle.xml");
    SharedPtr<Cursor> cursor(new Cursor(context_));

    cursor ->SetDefaultStyle(style);

    cursor->SetStyleAuto(style);
    ui->SetCursor(cursor);

    // Set starting position of the cursor at the rendering window center
    cursor->SetPosition(graphics->GetWidth() / 2, graphics->GetHeight() / 2);

    return 1;

}[/code]

Code 1
[code]
int  ExistenceClient::CreateCursor(void)
{
 
    /// Define Resouces
    ResourceCache* cache = GetSubsystem<ResourceCache>();
    Renderer* renderer = GetSubsystem<Renderer>();
    Graphics* graphics = GetSubsystem<Graphics>();
    UI* ui = GetSubsystem<UI>();
    FileSystem * filesystem = GetSubsystem<FileSystem>();
 
    Cursor * cursor = new Cursor(context_);
 
    cursor -> SetName("Cursor");
    cursor -> SetStyle("Cursor");
    cursor -> SetStyleAuto();
    cursor -> SetPosition(graphics -> GetWidth() / 2, graphics -> GetHeight() / 2);
 
    cursor ->   ApplyOSCursorShape ();
 
    ui -> SetCursor (cursor);
 
    return 1;
 
}[/code]

-------------------------

Mike | 2017-01-02 01:03:14 UTC | #2

Do you use somewhere:
[code]GetSubsystem<Input>()->SetMouseVisible(true);[/code]
to actually display the cursor?

-------------------------

vivienneanthony | 2017-01-02 01:03:14 UTC | #3

[quote="Mike"]Do you use somewhere:
[code]GetSubsystem<Input>()->SetMouseVisible(true);[/code]
to actually display the cursor?[/quote]


That turns on the OS mouse not the UI mouse. i need to figure out how to turn on the UI mouse.

-------------------------

Mike | 2017-01-02 01:03:14 UTC | #4

Try this:
[code]GetSubsystem<UI>()->GetCursor()->SetVisible(true);[/code]

-------------------------

