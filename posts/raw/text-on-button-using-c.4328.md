arpo | 2018-06-18 14:17:13 UTC | #1

How do I but a label on the button?
The code in HelloGUI looks like this but has no label.

    // Create a Button
    auto* button = new Button(context_);
    button->SetName("Button");
    button->SetMinHeight(24);

-------------------------

Eugene | 2018-06-18 14:38:00 UTC | #2

Urho UI is a kind of toolkit with basic building blocks.
`Button` is responsible for clicking. `Text` is responsible for text. `BorderImage` is responsible for picture.
So, you have to put `Text` element into `Button` element if you want to have text. If you want to have button with picture, put `BorderImage` into `Button` instead.

-------------------------

elix22 | 2018-06-18 14:43:10 UTC | #3

See sample 17_SceneReplication/SceneReplication.cpp


    Button* SceneReplication::CreateButton(const String& text, int width)
    {
        auto* cache = GetSubsystem<ResourceCache>();
        auto* font = cache->GetResource<Font>("Fonts/Anonymous Pro.ttf");

        auto* button = buttonContainer_->CreateChild<Button>();
        button->SetStyleAuto();
        button->SetFixedWidth(width);

        auto* buttonText = button->CreateChild<Text>();
        buttonText->SetFont(font, 12);
        buttonText->SetAlignment(HA_CENTER, VA_CENTER);
        buttonText->SetText(text);

        return button;
    }

-------------------------

VaniaK | 2018-06-20 10:38:40 UTC | #4

buttonText->SetInternal(true);

-------------------------

