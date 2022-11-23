vivienneanthony | 2017-01-02 00:59:47 UTC | #1

Hello,

I'm trying to get a value of a LineEdit but not sure how. The structure I have is UIElement -> LineEdit. The samples do not have a HelloGUi showing the input from the LineEdit.

So, far I have 

[code]    /// Get Needed SubSystems
    UI* ui_= GetSubsystem<UI>();

    UIElement * RootUIElement = ui_->GetRoot();

    UIElement * usernameInputUIElement = RootUIElement -> GetChild("usernameInput",true);  // The LineEdit is in this hierarchy
[/code]

I'll be testing and trying to figure out method to do it but I am not sure.

Vivienne

-------------------------

jmiller | 2017-01-02 00:59:47 UTC | #2

Hello,
I think LineEdit::GetText() may be what you want?
[urho3d.github.io/documentation/a00202.html](http://urho3d.github.io/documentation/a00202.html)

-------------------------

vivienneanthony | 2017-01-02 00:59:47 UTC | #3

[quote="carnalis"]Hello,
I think LineEdit::GetText() may be what you want?
[urho3d.github.io/documentation/a00202.html](http://urho3d.github.io/documentation/a00202.html)[/quote]

I tried that and its the function I need to call. The trick is locating the UIElement with the LineEdit node. Then calling the GetText for that LineEdit node.

Tha'ts where I am stuck on.

-------------------------

jmiller | 2017-01-02 00:59:47 UTC | #4

I may be misunderstanding...
[code]LineEdit* usernameInput = RootUIElement->CreateChild<LineEdit>("usernameInput");

LineEdit* lineEdit = (LineEdit*)ui->GetRoot()->GetChild("usernameInput", true);
String username = lineEdit->GetText();

//or if you keep the pointer
String username = userNameInput->GetText();
[/code]

*edit: Sorry, I was distracted and forgot the (LineEdit*) cast!

-------------------------

vivienneanthony | 2017-01-02 00:59:48 UTC | #5

I'm going put in the code so you or anyone else can see the picture.  So in the latter function I'm trying to get the text  of  the UI usernameinput.

[code]void ExistenceClient::LoginUI(bool exist)
{
    /// Get Needed SubSystems
    ResourceCache* cache = GetSubsystem<ResourceCache>();
    Renderer* renderer = GetSubsystem<Renderer>();
    Graphics* graphics = GetSubsystem<Graphics>();
    UI* ui = GetSubsystem<UI>();

    /// Get rendering window size as floats
    float width = (float)graphics->GetWidth();
    float height = (float)graphics->GetHeight();


    // Login screen
    // Create the Window and add it to the UI's root node
    window_= new Window(context_);

    uiRoot_->AddChild(window_);
    UIElement* usernameTextUIElement = new UIElement(context_);
    Text* usernameText = new Text(context_);
    LineEdit* usernameInput=new LineEdit(context_);
    UIElement* passwordTextUIElement = new UIElement(context_);
    Text* passwordText = new Text(context_);
    LineEdit* passwordInput=new LineEdit(context_);

    // Set Window size and layout settings
    window_->SetMinSize(384, 192);
    window_->SetLayout(LM_VERTICAL, 6, IntRect(6, 6, 6, 6));
    window_->SetAlignment(HA_CENTER, VA_CENTER);
    window_->SetName("LoginWindow");
    window_->SetMovable(false);
    window_->SetOpacity(.6);

    // Create Window 'titlebar' container
    usernameTextUIElement ->SetMinSize(0,32);
    usernameTextUIElement ->SetVerticalAlignment(VA_TOP);
    usernameTextUIElement ->SetLayoutMode(LM_HORIZONTAL);

    usernameText->SetName("Login");
    usernameText->SetText("Username");

    // Create Window 'titlebar' container
    passwordTextUIElement ->SetMinSize(0,32);
    passwordTextUIElement ->SetVerticalAlignment(VA_TOP);
    passwordTextUIElement ->SetLayoutMode(LM_HORIZONTAL);

    passwordText->SetName("Password");
    passwordText->SetText("Password");

    usernameInput->SetName("usernameInput");
    usernameInput->SetText("<Enter Email>");
    usernameInput->SetMaxLength(24);
    usernameInput->SetMinHeight(24);
    usernameInput->SetStyleAuto();

    passwordInput->SetName("passwordInput");
    passwordInput->SetText("<Enter Password>");
    passwordInput->SetMaxLength(24);
    passwordInput->SetMinHeight(24);
    passwordInput->SetStyleAuto();

    // Add the controls to the title bar
    usernameTextUIElement->AddChild(usernameText);
    passwordTextUIElement->AddChild(passwordText);
    window_->AddChild(usernameTextUIElement);
    window_->AddChild(usernameInput);
    window_->AddChild(passwordTextUIElement);
    window_->AddChild(passwordInput);

    // declare buttons
    Button* loginButton = new Button(context_);
    Button* newaccountButton = new Button(context_);

    // check if account exist
    if(accountexist)
    {
        loginButton->SetName("Login");
        loginButton->SetStyle("loginButton");
        window_->AddChild(loginButton);
    }
    else
    {
        newaccountButton->SetName("NewAccountLogin");
        newaccountButton->SetStyle("newaccountButton");
        window_->AddChild(newaccountButton);
    }

    // Apply styles
    window_->SetStyleAuto();
    usernameText->SetStyleAuto();
    passwordText->SetStyleAuto();

    if(accountexist)
    {
        SubscribeToEvent(loginButton, E_RELEASED, HANDLER(ExistenceClient, LoginScreenUILoginHandleClosePressed));
    }
    else
    {

        SubscribeToEvent(newaccountButton, E_RELEASED, HANDLER(ExistenceClient, LoginScreenUINewAccountHandleClosePressed));
    }

    return;
}

// Handlers for login screen
void ExistenceClient::LoginScreenUILoginHandleClosePressed(StringHash eventType, VariantMap& eventData)
{
    /// Get Needed SubSystems
    UI* ui_= GetSubsystem<UI>();

    UIElement * RootUIElement = ui_->GetRoot();

    String username = RootUIElement->GetChild("usernameInput", true)->GetText();


    // remove Existence Logo Node
    scene_->GetChild("ExistenceLogo",true)->RemoveAllComponents();
    scene_->GetChild("ExistenceLogo",true)->Remove();

    // Call progress screen function
    ProgressScreenUI();

    return;
}
[/code]

-------------------------

vivienneanthony | 2017-01-02 00:59:48 UTC | #6

[quote="carnalis"]I may be misunderstanding...
[code]LineEdit* usernameInput = RootUIElement->CreateChild<LineEdit>("usernameInput");

LineEdit* lineEdit = (LineEdit*)ui->GetRoot()->GetChild("usernameInput", true);
String username = lineEdit->GetText();

//or if you keep the pointer
String username = userNameInput->GetText();
[/code]

*edit: Sorry, I was distracted and forgot the (LineEdit*) cast![/quote]

That did the trick. I did not know you could do the casting which makes sense.

-------------------------

