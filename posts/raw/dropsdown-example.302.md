vivienneanthony | 2017-01-02 00:59:29 UTC | #1

Hello

Do anyone have a quick example of setting up a drop down list? It doesn't work partially yet, and it will be odd because I want to put at least 16 personalty types.

Vivienne

So far I have

[code]// list view part
    UIElement* personaltyUIElement = new UIElement(context_);
    UIElement* personaltyUIElements = new UIElement(context_);
    
    ListView* personaltyView = new ListView(context_);
    Text* personalty1 = new Text(context_);

    personalty1->SetName("Stubborn");
    personalty1->SetText("Stubborn");

    personaltyView->SetStyleAuto();

    personaltyUIElements->AddChild(personalty1);

    personaltyView->AddItem(personaltyUIElements);

    personaltyUIElement->AddChild(personaltyView);
    personaltyUIElement->SetMinSize(0,32);

    window_->AddChild(factionselectionUIElement);
    window_->AddChild(alienselectionUIElement);
    window_->AddChild(genderselectionUIElement);
    window_->AddChild(blankUIElement);
    window_->AddChild(playerUIElement);
    window_->AddChild(playernameinputUIElement);
    window_->AddChild(blankUIElement);
    window_->AddChild(personaltyUIElement);

    window_->AddChild(loginButton);
[/code]

-------------------------

vivienneanthony | 2017-01-02 00:59:30 UTC | #2

Just tried. No luck so far.

[quote]  // list view part
    UIElement* personaltyUIElement1 = new UIElement(context_);
    UIElement* personaltyUIElement2 = new UIElement(context_);
    UIElement* personaltyUIElements = new UIElement(context_);

    ListView* personaltyView = new ListView(context_);
    Text* personalty1 = new Text(context_);
    Text* personalty2 = new Text(context_);

    //personalty1->SetName("Stubborn");
    personalty1->SetName("Stubborn");
    personalty1->SetText("Stubborn");
    personalty2->SetName("Seductive");
    personalty2->SetText("Seductive");

    personaltyUIElement1->AddChild(personalty1);
    personaltyUIElement1->SetMinSize(0,32);
    personaltyUIElement1->SetStyleAuto();
    personaltyUIElement1->SetLayoutMode(LM_HORIZONTAL);

    personaltyUIElement2->AddChild(personalty2);
    personaltyUIElement2->SetMinSize(0,32);
    personaltyUIElement2->SetStyleAuto();
    personaltyUIElement2->SetLayoutMode(LM_HORIZONTAL);

    personaltyView->AddItem(personaltyUIElement1);
    personaltyView->AddItem(personaltyUIElement2);

    personaltyView->SetSelection(1);
    personaltyView->SetStyleAuto();

    personaltyUIElements->SetLayoutMode(LM_HORIZONTAL);
    personaltyUIElements->SetMinSize(0,32);
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
    window_->AddChild(personaltyUIElements);[/quote]

-------------------------

rasteron | 2017-01-02 00:59:30 UTC | #3

The Editor is a perfect example, you can start playing around with that (View -> Editor Settings). Have you considered or tried loading your UI data as XML?

-------------------------

vivienneanthony | 2017-01-02 00:59:30 UTC | #4

[quote="rasteron"]The Editor is a perfect example, you can start playing around with that (View -> Editor Settings). Have you considered or tried loading your UI data as XML?[/quote]

I haven't considered the latter. I rather program a preset of the user interface up to the main player selection screen. From there I can mess with XML/UI.

-------------------------

vivienneanthony | 2017-01-02 00:59:30 UTC | #5

[quote="rasteron"]The Editor is a perfect example, you can start playing around with that (View -> Editor Settings). Have you considered or tried loading your UI data as XML?[/quote]

Actually, figured it out after playing with the Editor.  Just have to clean up the code then look at the samples to actually make the code to work as intended.

-------------------------

