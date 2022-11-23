vivienneanthony | 2017-01-02 01:00:19 UTC | #1

Hello,

Another quick question, If I want to get the results of a button being pressed. Is it possible? 

Otherewise, the only thing I can think of is using a global class variable and creating a handler specifically for the input buttons such as factions, gender, and alien. Addtionally doing the same for the traits.

Vivienne


[code]

void ExistenceClient::CreatePlayerUIHandleClosePressed(StringHash eventType, VariantMap& eventData)
{
    // set ui state to none
    ExistenceGameState.SetUIState(UI_CHARACTERCREATIONINTERFACE);

    // remove child nodeAddItem (UIElement *item)
    scene_->GetChild("playerMesh",true)->RemoveAllComponents();
    scene_->GetChild("playerMesh",true)->Remove();


    // get intput
    LineEdit* lineEdit = (LineEdit*)ui_->GetRoot()->GetChild("firstnameInput", true);
    LineEdit* lineEdit = (LineEdit*)ui_->GetRoot()->GetChild("middlenameInput", true);
    LineEdit* lineEdit = (LineEdit*)ui_->GetRoot()->GetChild("lastnameInput", true);
    String firstnameInput = lineEdit->GetText();
    String middlenameInput = lineEdit->GetText();
    String lastnameInput = lineEdit->GetText();


    SavePlayer(0);

    ProgressScreenUI();

}[/code]

The code that actually do the input.
[quote]
void ExistenceClient::CreatePlayerScreenUI()
{

    /// Get Needed SubSystems
    ResourceCache* cache = GetSubsystem<ResourceCache>();
    Renderer* renderer = GetSubsystem<Renderer>();
    Graphics* graphics = GetSubsystem<Graphics>();
    UI* ui = GetSubsystem<UI>();

    ui->Clear();

    /// Get rendering window size as floats
    float width = (float)graphics->GetWidth();
    float height = (float)graphics->GetHeight();

    // set ui state to none
    ExistenceGameState.SetUIState(UI_CHARACTERCREATIONINTERFACE);

    // Login screen
    // Create the Window and add it to the UI's root node
    window_= new Window(context_);
    window2_=new Window(context_);

    // create first and secondary windows
    uiRoot_->AddChild(window_);
    uiRoot_->AddChild(window2_);

    UIElement* titleBar = new UIElement(context_);
    UIElement* contineButtonUIElement  = new UIElement(context_);
    Text* windowTitle = new Text(context_);
    LineEdit* firstnameInput=new LineEdit(context_);
    LineEdit* middlenameInput=new LineEdit(context_);
    LineEdit* lastnameInput=new LineEdit(context_);
    Button* continueButton = new Button(context_);
    Button* createnewplayerfacezoomButton = new Button(context_);

    // Set Window size and layout settings
    window_->SetFixedSize(384, height-100-100);
    window_->SetLayout(LM_VERTICAL,12, IntRect(6, 6, 378, height-100-100));
    window_->SetPosition(30, 100);
    window_->SetName("PlayerCreatorWindow");
    window_->SetMovable(false);
    window_->SetOpacity(.6);

    window2_->SetName("FocusCreaterWindow");
    window2_->SetFixedSize(64,height-100-100);
    window2_->SetLayout(LM_VERTICAL, 6, IntRect(6, 6, 6, 6));
    window2_->SetPosition(1024+256,100);
    window2_->SetMovable(false);
    window2_->SetOpacity(.6);

    // Create Window 'titlebar' container
    titleBar->SetMinSize(0,32);
    titleBar->SetVerticalAlignment(VA_TOP);
    titleBar->SetLayoutMode(LM_HORIZONTAL);

    windowTitle->SetName("PlayerCreatorTitle");
    windowTitle->SetText("Player Creator");

    // [addloneshttps://www.youtube.com/user/averyny](addloneshttps://www.youtube.com/user/averyny)

    contineButtonUIElement->SetMinSize(0,32);
    contineButtonUIElement->SetVerticalAlignment(VA_BOTTOM);
    //contineButtonUIElement->SetLayoutMode(LM_HORIZONTAL);
    continueButton ->SetPosition(6,300);

    contineButtonUIElement->AddChild(continueButton);

    //createnewplayerfacezoomButton->SetPosition(IntVector2(400,400));
    createnewplayerfacezoomButton->SetPosition(700,200);
    createnewplayerfacezoomButton->SetName("createnewplayerfacezoomButton");
    createnewplayerfacezoomButton->SetStyle("createnewplayerfacezoomButton");

    // Add the controls to the title bar
    titleBar->AddChild(windowTitle);

    // add components to the window
    window_->AddChild(titleBar);

    window2_->AddChild(createnewplayerfacezoomButton);

    // Apply styles
    window_->SetStyleAuto();
    window2_->SetStyleAuto();

    windowTitle->SetStyleAuto();

    Node* playermeshNode = scene_->CreateChild("playerMesh");

    //playermeshNode ->SetScale(Vector3(1.0f,1.0f,1.0f));
    playermeshNode ->SetPosition(Vector3(1.0,-2,0.0));
    playermeshNode ->SetRotation(Quaternion(0.0, 0.0,0.0));

    loadplayerMesh(playermeshNode, 49,DISPLAYMESH_MUILTIPLECHARACTER);

    playermeshNode->SetScale(2);

    int factionlimit=3;

    // create factions
    factions faction[1];
    alienraces alien[1];

    int windowwidth=384;
    int alienlimit=3;

    //Button* factionbutton = new Button(context_);
    UIElement * faction0buttonUIElement = new UIElement(context_);
    UIElement * faction1buttonUIElement = new UIElement(context_);
    UIElement * faction2buttonUIElement = new UIElement(context_);
    UIElement * faction3buttonUIElement = new UIElement(context_);

    Button * faction0button = new  Button(context_);
    Button * faction1button = new  Button(context_);
    Button * faction2button = new  Button(context_);
    Button * faction3button = new  Button(context_);

    UIElement * alien0buttonUIElement = new UIElement(context_);
    UIElement * alien1buttonUIElement = new UIElement(context_);
    UIElement * alien2buttonUIElement = new UIElement(context_);
    UIElement * alien3buttonUIElement = new UIElement(context_);

    Button * alien0button = new  Button(context_);
    Button * alien1button = new  Button(context_);
    Button * alien2button = new  Button(context_);
    Button * alien3button = new  Button(context_);

    Button * gendermalebutton = new  Button(context_);
    Button * genderfemalebutton = new  Button(context_);

    // set faction an
    faction0buttonUIElement->SetName("faction0buttonUIElement");
    faction1buttonUIElement->SetName("faction1buttonUIElement");
    faction2buttonUIElement->SetName("faction2buttonUIElement");
    faction3buttonUIElement->SetName("faction3buttonUIElement");

    alien0buttonUIElement->SetName("alien0buttonUIElement");
    alien1buttonUIElement->SetName("alien1buttonUIElement");
    alien2buttonUIElement->SetName("alien2buttonUIElement");
    alien3buttonUIElement->SetName("alien3buttonUIElement");

    gendermalebutton->SetName("gendermalebutton");
    genderfemalebutton->SetName("genderfemalebutton");

    gendermalebutton->SetName("gendermalebutton");
    genderfemalebutton->SetName("genderfemalebutton");

    // set layout
    int area=windowwidth/4;

    UIElement * factionselectionUIElement = new UIElement(context_);
    factionselectionUIElement->SetFixedHeight(32);

    faction0buttonUIElement->SetFixedSize(area-2, 32);
    faction1buttonUIElement->SetFixedSize(area-2, 32);
    faction2buttonUIElement->SetFixedSize(area-2, 32);
    faction3buttonUIElement->SetFixedSize(area-6, 32);

    faction0buttonUIElement->SetPosition(0, 1);
    faction1buttonUIElement->SetPosition(area*1, 1);
    faction2buttonUIElement->SetPosition(area*2, 1);
    faction3buttonUIElement->SetPosition(area*3, 1);

    faction0buttonUIElement->AddChild(faction0button);
    faction1buttonUIElement->AddChild(faction1button);
    faction2buttonUIElement->AddChild(faction2button);
    faction3buttonUIElement->AddChild(faction3button);

    factionselectionUIElement->AddChild(faction0buttonUIElement);
    factionselectionUIElement->AddChild(faction1buttonUIElement);
    factionselectionUIElement->AddChild(faction2buttonUIElement);
    factionselectionUIElement->AddChild(faction3buttonUIElement);

    UIElement * alienselectionUIElement = new UIElement(context_);

    alienselectionUIElement->SetFixedHeight(32);

    alien0buttonUIElement->SetFixedSize(area-2, 32);
    alien1buttonUIElement->SetFixedSize(area-2, 32);
    alien2buttonUIElement->SetFixedSize(area-2, 32);
    alien3buttonUIElement->SetFixedSize(area-6, 32);

    alien0buttonUIElement->SetPosition(0, 1);
    alien1buttonUIElement->SetPosition(area*1, 1);
    alien2buttonUIElement->SetPosition(area*2, 1);
    alien3buttonUIElement->SetPosition(area*3, 1);

    alien0buttonUIElement->AddChild(alien0button);
    alien1buttonUIElement->AddChild(alien1button);
    alien2buttonUIElement->AddChild(alien2button);
    alien3buttonUIElement->AddChild(alien3button);

    alienselectionUIElement->AddChild(alien0buttonUIElement);
    alienselectionUIElement->AddChild(alien1buttonUIElement);
    alienselectionUIElement->AddChild(alien2buttonUIElement);
    alienselectionUIElement->AddChild(alien3buttonUIElement);

    UIElement * genderselectionUIElement = new UIElement(context_);
    UIElement * genderfemalebuttonUIElement = new UIElement(context_);
    UIElement * gendermalebuttonUIElement = new UIElement(context_);

    genderselectionUIElement->SetFixedHeight(32);

    genderfemalebuttonUIElement->SetFixedSize((area*2)-2, 32);
    gendermalebuttonUIElement->SetFixedSize((area*2)-2, 32);

    genderfemalebuttonUIElement->SetPosition(0,  1);
    gendermalebuttonUIElement->SetPosition(area*2, 1);

    genderfemalebuttonUIElement->AddChild(genderfemalebutton);
    gendermalebuttonUIElement->AddChild(gendermalebutton);

    genderselectionUIElement->AddChild(genderfemalebuttonUIElement);
    genderselectionUIElement->AddChild(gendermalebuttonUIElement);

    genderselectionUIElement->SetFixedSize(0,16);

    UIElement * blankUIElement = new UIElement(context_);
    Text * blankText = new Text(context_);

    blankUIElement->SetLayoutMode(LM_HORIZONTAL);
    blankUIElement->SetFixedHeight(32);

    blankText->SetName("blank");
    blankText->SetText(" ");

    blankUIElement-> AddChild(blankText);

    UIElement * playerUIElement = new UIElement(context_);
    Text * nameText = new Text(context_);

    playerUIElement->SetLayoutMode(LM_HORIZONTAL);

    nameText->SetName("Player");
    nameText->SetText("Player");

    playerUIElement-> AddChild(nameText);

    firstnameInput->SetName("firstnameInput");
    firstnameInput->SetText("<firstname>");
    firstnameInput->SetMaxLength(24);
    firstnameInput->SetMinHeight(24);
    firstnameInput->SetFixedWidth(125);
    firstnameInput->SetStyleAuto();

    middlenameInput->SetName("middlenameInput");
    middlenameInput->SetText("<middlename>");
    middlenameInput->SetMaxLength(24);
    middlenameInput->SetMinHeight(24);
    middlenameInput->SetFixedWidth(125);
    middlenameInput->SetStyleAuto();

    lastnameInput->SetName("lastnameInput");

    lastnameInput->SetText("<lastname>");
    lastnameInput->SetMaxLength(24);
    lastnameInput->SetMinHeight(24);
    lastnameInput->SetFixedWidth(125);
    lastnameInput->SetStyleAuto();

    UIElement * playernameinputUIElement = new UIElement(context_);

    playernameinputUIElement->SetMinSize(0,32);
    playernameinputUIElement->SetLayoutMode(LM_HORIZONTAL);

    playernameinputUIElement->AddChild(firstnameInput);
    playernameinputUIElement->AddChild(middlenameInput);
    playernameinputUIElement->AddChild(lastnameInput);

    // Personalty
    UIElement * personaltytextUIElement = new UIElement(context_);
    Text * personaltyText = new Text(context_);

    personaltytextUIElement->SetLayoutMode(LM_HORIZONTAL);

    personaltyText->SetName("personalty");
    personaltyText->SetText("Personalty");

    personaltytextUIElement-> AddChild(personaltyText);

    // list view part
    UIElement * personaltyUIElement1 = new UIElement(context_);
    UIElement * personaltyUIElement2 = new UIElement(context_);
    UIElement * personaltyUIElements = new UIElement(context_);

    ListView * personaltyView = new ListView(context_);

    Text * personalty1 = new Text(context_);
    Text * personalty2 = new Text(context_);

    //personalty1->SetName("Stubborn");
    personalty1->SetName("Stubborn");
    personalty1->SetText("Stubborn");
    personalty2->SetName("Seductive");
    personalty2->SetText("Seductive");

    personaltyUIElement1->AddChild(personalty1);
    personaltyUIElement1->SetLayoutMode(LM_HORIZONTAL);

    personaltyUIElement2->AddChild(personalty2);
    personaltyUIElement2->SetLayoutMode(LM_HORIZONTAL);

    personaltyView->AddItem(personaltyUIElement1);
    personaltyView->AddItem(personaltyUIElement2);

    personaltyView->SetStyleAuto();
    personaltyView->SetFixedSize(300,64);

    personaltyUIElements->SetLayoutMode(LM_HORIZONTAL);
    personaltyUIElements->SetStyleAuto();

    personaltyUIElements->AddChild(personaltyView);

    // add the rest of the window elements
    window_->AddChild(factionselectionUIElement);
    window_->AddChild(alienselectionUIElement);
    window_->AddChild(genderselectionUIElement);
    window_->AddChild(blankUIElement);
    window_->AddChild(playerUIElement);
    window_->AddChild(playernameinputUIElement);
    window_->AddChild(blankUIElement);
    window_->AddChild(personaltytextUIElement);
    window_->AddChild(personaltyUIElements);

    window_->AddChild(contineButtonUIElement);

    nameText->SetStyleAuto();
    firstnameInput->SetStyleAuto();
    middlenameInput->SetStyleAuto();
    lastnameInput->SetStyleAuto();
    personalty1->SetStyleAuto();
    personalty2->SetStyleAuto();
    personaltyView->SetStyleAuto();
    personaltyText->SetStyleAuto();

    // set button style
    faction0button->SetStyle("logofederationalliance");
    faction1button->SetStyle("logoklingonalliance");
    faction2button->SetStyle("logoromulanalliance");
    faction3button->SetStyle("logononalliance");

    alien0button->SetStyle("logohumans");
    alien1button->SetStyle("logoklingons");
    alien2button->SetStyle("logoromulans");
    alien3button->SetStyle("logoorcins");

    genderfemalebutton->SetStyle("genderfemale");
    gendermalebutton->SetStyle("gendermale");

    continueButton->SetStyle("continueButton");

    // update
    for(int i=0; i<FACTIONSLIMIT; ++i)
    {
        //        scene_->GetChild("faction"+(String)i+"button")->SetStyle("");
    }

    SubscribeToEvent(continueButton, E_RELEASED, HANDLER(ExistenceClient, CreatePlayerUIHandleClosePressed));

    // Subscribe also to all UI mouse clicks just to see where we have clicked
    SubscribeToEvent(E_UIMOUSECLICK, HANDLER(ExistenceClient, CreatePlayerUIHandleControlClicked))

    return;
}[/quote]

Vivienne

-------------------------

friesencr | 2017-01-02 01:00:19 UTC | #2

You can subscribe to the KeyDown event and read the event.key.

-------------------------

vivienneanthony | 2017-01-02 01:00:19 UTC | #3

[quote="friesencr"]You can subscribe to the KeyDown event and read the event.key.[/quote]

I have a HandleKeyDown.

Part of some other code uses

[code] // Unlike the other samples, exiting the engine when ESC is pressed instead of just closing the console
    if (eventData[KeyDown::P_KEY].GetInt() == KEY_F12)
    {[/code]

So, I have to figure out what's the equivalent for a button. I'll probably use the MouseButtonDown event. I do have a rudimentary state system so I know which part of the UI I am in.

Vivienne

-------------------------

vivienneanthony | 2017-01-02 01:00:19 UTC | #4

So far I have this. I just need to figure out a way to detect which button object was pressed which doesn't seem to work for me.

:-/


[code]  SubscribeToEvent(continueButton, E_RELEASED, HANDLER(ExistenceClient, CreatePlayerUIHandleClosePressed));

    // released buttons
    SubscribeToEvent(faction0button, E_MOUSEBUTTONUP, HANDLER(ExistenceClient, HandleMouseButtonReleased));
    SubscribeToEvent(faction1button, E_MOUSEBUTTONUP, HANDLER(ExistenceClient, HandleMouseButtonReleased));
    SubscribeToEvent(faction2button, E_MOUSEBUTTONUP, HANDLER(ExistenceClient, HandleMouseButtonReleased));
    SubscribeToEvent(faction3button, E_MOUSEBUTTONUP, HANDLER(ExistenceClient, HandleMouseButtonReleased));
    SubscribeToEvent(alien0button, E_MOUSEBUTTONUP, HANDLER(ExistenceClient, HandleMouseButtonReleased));
    SubscribeToEvent(alien1button, E_MOUSEBUTTONUP, HANDLER(ExistenceClient, HandleMouseButtonReleased));
    SubscribeToEvent(alien2button, E_MOUSEBUTTONUP, HANDLER(ExistenceClient, HandleMouseButtonReleased));
    SubscribeToEvent(alien3button, E_MOUSEBUTTONUP, HANDLER(ExistenceClient, HandleMouseButtonReleased));
    SubscribeToEvent(gendermalebutton, E_MOUSEBUTTONUP, HANDLER(ExistenceClient, HandleMouseButtonReleased));
    SubscribeToEvent(genderfemalebutton, E_MOUSEBUTTONUP, HANDLER(ExistenceClient, HandleMouseButtonReleased));


    // Subscribe also to all UI mouse clicks just to see where we have clicked
    SubscribeToEvent(E_UIMOUSECLICK, HANDLER(ExistenceClient, CreatePlayerUIHandleControlClicked));


    return;
}




void ExistenceClient::HandleMouseButtonReleased(StringHash eventType, VariantMap& eventData)
{
    /// Mouse button released.
    int button=eventData[MouseButtonUp:].GetInt();
    int buttons=eventData[MouseButtonUp::P_BUTTONS].GetInt();

    /// Nada so far - If I use Release it calls the function but the eventData is not correct
    cout <<" " << button << " " << buttons;
    cout << "released";

    return;
}


[/code]

-------------------------

thebluefish | 2017-01-02 01:00:19 UTC | #5

IMO a function named HandleMouseButtonReleased should handle all MouseButtonReleased events. Each button should ideally have their own callbacks. Here is an excerpt from my project:

Game.h:
[code]void SubscribeToEvents();

void HandleUpdate(Urho3D::StringHash eventType, Urho3D::VariantMap& eventData);
void HandlePostUpdate(Urho3D::StringHash eventType, Urho3D::VariantMap& eventData);
void HandleButtonDown(Urho3D::StringHash eventType, Urho3D::VariantMap& eventData);
void HandleButtonUp(Urho3D::StringHash eventType, Urho3D::VariantMap& eventData);
void HandleMouseAxisMove(Urho3D::StringHash eventType, Urho3D::VariantMap& eventData);
void HandleJoystickAxisMove(Urho3D::StringHash eventType, Urho3D::VariantMap& eventData);

void HandleButtonResume(Urho3D::StringHash eventType, Urho3D::VariantMap& eventData);
void HandleButtonExit(Urho3D::StringHash eventType, Urho3D::VariantMap& eventData);[/code]

Game.cpp:
[code]
void Game::SubscribeToEvents()
{
    SubscribeToEvent(Urho3D::E_UPDATE, HANDLER(Game, HandleUpdate));
    SubscribeToEvent(Urho3D::E_POSTUPDATE, HANDLER(Game, HandlePostUpdate));

	SubscribeToEvent(BUTTON_DOWN, HANDLER(Game, HandleButtonDown));
	SubscribeToEvent(BUTTON_UP, HANDLER(Game, HandleButtonUp));
	SubscribeToEvent(MOUSE_AXIS_MOVE, HANDLER(Game, HandleMouseAxisMove));
	SubscribeToEvent(JOYSTICK_AXIS_MOVE, HANDLER(Game, HandleJoystickAxisMove));

    SubscribeToEvent(_resumeButton, Urho3D::E_RELEASED, HANDLER(Game, HandleButtonResume));
    SubscribeToEvent(_exitButton, Urho3D::E_RELEASED, HANDLER(Game, HandleButtonExit));
}

void Game::HandleButtonResume(Urho3D::StringHash eventType, Urho3D::VariantMap& eventData)
{	
	Pause(false);
}

void Game::HandleButtonExit(Urho3D::StringHash eventType, Urho3D::VariantMap& eventData)
{	
	context_->RemoveSubsystem<Game>();
}

[/code]

-------------------------

vivienneanthony | 2017-01-02 01:00:19 UTC | #6

[quote="thebluefish"]IMO a function named HandleMouseButtonReleased should handle all MouseButtonReleased events. Each button should ideally have their own callbacks. Here is an excerpt from my project:[/quote]

I agree. MouseButtonReleased was just the function name because I was testing using ButtonUp and ButtonReleased.

The actual code with the proper name that doesn't work is below.


[code]void ExistenceClient::CreateNewPlayerScreen(....)
{

  ....
....

  SubscribeToEvent(continueButton, E_RELEASED, HANDLER(ExistenceClient, CreatePlayerUIHandleClosePressed));

    // Up buttons
    SubscribeToEvent(faction0button, E_MOUSEBUTTONUP, HANDLER(ExistenceClient, HandleMouseButtonUp));
    SubscribeToEvent(faction1button, E_MOUSEBUTTONUP, HANDLER(ExistenceClient, HandleMouseButtonUp));
    SubscribeToEvent(faction2button,  E_MOUSEBUTTONUP, HANDLER(ExistenceClient, HandleMouseButtonUp));
    SubscribeToEvent(faction3button, E_MOUSEBUTTONUP, HANDLER(ExistenceClient, HandleMouseButtonUp));
    SubscribeToEvent(alien0button, E_MOUSEBUTTONUP, HANDLER(ExistenceClient, HandleMouseButtonUp));
    SubscribeToEvent(alien1button, E_MOUSEBUTTONUP, HANDLER(ExistenceClient, HandleMouseButtonUp));
    SubscribeToEvent(alien2button, E_MOUSEBUTTONUP, HANDLER(ExistenceClient, HandleMouseButtonUp));
    SubscribeToEvent(alien3button, E_MOUSEBUTTONUP, HANDLER(ExistenceClient, HandleMouseButtonUp));
    SubscribeToEvent(gendermalebutton, E_MOUSEBUTTONUP, HANDLER(ExistenceClient, HandleMouseButtonUp));
    SubscribeToEvent(genderfemalebutton, E_MOUSEBUTTONUP, HANDLER(ExistenceClient, HandleMouseButtonUp));


    // Subscribe also to all UI mouse clicks just to see where we have clicked
    SubscribeToEvent(E_UIMOUSECLICK, HANDLER(ExistenceClient, CreatePlayerUIHandleControlClicked));


    return;
}

void ExistenceClient::HandleMouseButtonUp(Urho3D::StringHash eventType, Urho3D::VariantMap& eventData)
{
    /// Mouse button Up.
    int button=eventData[MouseButtonUp:].GetInt();
    int buttons=eventData[MouseButtonUp::P_BUTTONS].GetInt();

    /// Nada so far - If I use Release it calls the function but the eventData is not correct
    cout <<"Button Pressed  " << button << " Buttons " << buttons;
    cout << "released";

    return;
}[/code]

-------------------------

friesencr | 2017-01-02 01:00:19 UTC | #7

When you are capturing a button click you probably want to subscribe to Pressed, it is cross platform and tracks the mouse state through the down and up state.  When detecting a button press you don't want the ui mouse click which only happens when you click on a ui element but rather the MouseButtonDown.  The UI and Input are different subsystems.  Input is much lower level and doesn't care what you click on.  UI only cares about ui stuff.

-------------------------

vivienneanthony | 2017-01-02 01:00:19 UTC | #8

[quote="friesencr"]When you are capturing a button click you probably want to subscribe to Pressed, it is cross platform and tracks the mouse state through the down and up state.  When detecting a button press you don't want the ui mouse click which only happens when you click on a ui element but rather the MouseButtonDown.  The UI and Input are different subsystems.  Input is much lower level and doesn't care what you click on.  UI only cares about ui stuff.[/quote]

I can switch it to use the release event. In the future I probably want to get the button click left or right info specifically the button up information.

Sidenote, I have to spend some time with the whole procedural terrain.  Switching the code into a Procedural class. I think some people are curious that I got the Perlin noise running generating terrain leaving the possibility of infinite terrain in Urho natively.

-------------------------

