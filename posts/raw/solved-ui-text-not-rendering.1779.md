TheComet | 2017-01-02 01:10:04 UTC | #1

Hey guys

From previous topics I've seen other people having trouble with adding the UI elements in the right order so text renders, and I'm having the same issue. I tried re-arranging the order in which elements are added but I can't get it to work. This is all of my code:

[code]    ResourceCache* cache = GetSubsystem<ResourceCache>();
    UI* ui = GetSubsystem<UI>();
    UIElement* root = ui->GetRoot();

    XMLFile* xmlDefaultStyle = cache->GetResource<XMLFile>("UI/DefaultStyle.xml");
    root->SetDefaultStyle(xmlDefaultStyle);

    Window* window = new Window(context_);
    window->SetMinWidth(384);
    window->SetMinHeight(100);
    window->SetPosition(8, 8);
    window->SetLayout(LM_VERTICAL, 6, IntRect(6, 6, 6, 6));
    window->SetName("Window");

    UIElement* titleBar = new UIElement(context_);
    titleBar->SetMinSize(0, 24);
    titleBar->SetVerticalAlignment(VA_TOP);
    titleBar->SetLayoutMode(LM_HORIZONTAL);

    Text* windowTitle = new Text(context_);
    windowTitle->SetName("WindowTitle");
    windowTitle->SetText("This is a test!");

    Button* button = new Button(context_);
    button->SetName("TestButton");

    Text* buttonText = new Text(context_);
    buttonText->SetText("button");

    window->SetStyleAuto();
    button->SetStyleAuto();
    windowTitle->SetStyleAuto();
    buttonText->SetStyleAuto();

    root->AddChild(window);
    window->AddChild(button);
    window->AddChild(titleBar);
    titleBar->AddChild(windowTitle);
    button->AddChild(buttonText);[/code]

This is the result:

[img]http://i.imgur.com/87oRzYl.jpg[/img]

What am I doing wrong?

-------------------------

1vanK | 2017-01-02 01:10:04 UTC | #2

try set style after add child

-------------------------

TheComet | 2017-01-02 01:10:04 UTC | #3

Same as above, except for style after child:

[code]    root->AddChild(window);
    window->AddChild(button);
    window->AddChild(titleBar);
    titleBar->AddChild(windowTitle);
    button->AddChild(buttonText);

    window->SetStyleAuto();
    button->SetStyleAuto();
    windowTitle->SetStyleAuto();
    buttonText->SetStyleAuto();[/code]

Still no text

-------------------------

1vanK | 2017-01-02 01:10:04 UTC | #4

This code works for me. Any information in log? May be it not found font?

-------------------------

TheComet | 2017-01-02 01:10:04 UTC | #5

Ah, I knew it was something stupid. Thanks!

-------------------------

