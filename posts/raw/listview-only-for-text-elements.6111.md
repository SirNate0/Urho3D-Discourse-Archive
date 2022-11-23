Lys0gen | 2020-04-23 01:38:07 UTC | #1

Hello, I am once again asking for your support.

I have tried to put buttons and almost blank UIElements (only set size and Text as child element) into a ListView however I am not sure if this is supposed to even work because it behaves very strange.

Basically, the whole automatic positioning and sizing does not seem to work, buttons seem to have a height of 0 (only seeing the borders) and they all stack on top of each other. The UIElements also just stack up.

Using regular Text everything works fine. I tried this by adjusting sample 48, I changed the loop which fills the ListView to this:

    for (int i = 0; i < 32; i++)
    {
        auto* button = new Button(context_);
        button->SetStyleAuto();

        auto* text = new Text(context_);
        text->SetStyleAuto();
        text->SetText(ToString("List item %d", i));
        text->SetName(ToString("Item %d", i));

        button->AddChild(text);
        //button->SetStyleAuto();//setting style here doesnt change the behaviour either
        list->AddItem(button);
    }   


Mind you that I can likely work with just Text elements, just wondering if this is working as intended or I am doing something wrong.
Thanks!

-------------------------

trillian | 2020-04-24 07:10:15 UTC | #2

No, it does not just work with Text items. I created complex items with icon, 2 lines of text a custom element, and it works fine, see https://github.com/stievie/ABx/blob/master/abclient/abclient/SkillsWindow.cpp#L578
This uses an `UISelectable` as container which is added as item to the listview.
Screenshot: https://imgur.com/qLkknco.png
Maybe it does not work with only Buttons (didn't try that), so you could also use a `UISelectable` as container, set the layout of it and add the button to it.

-------------------------

throwawayerino | 2020-04-24 12:25:02 UTC | #3

I can confirm it does work with buttons (at least on C++)
```
root->LoadChildXML(Cache->GetResource<XMLFile>("UI/TodoList.xml")->GetRoot(), root->GetDefaultStyle());
for (int i = 0; i < 4; i++) {
		WeakPtr<Button> button;
		button = new Button(GetContext());
		button->SetFixedSize(IntVector2(75, 75));
		button->SetHorizontalAlignment(HA_CENTER);
		button->SetStyleAuto();
		TodoList->AddItem(button);
	}
```

-------------------------

throwawayerino | 2020-04-24 12:40:17 UTC | #4

Did you enable the automatic positioning/sizing? Try `SetLayoutMode(LM_VERTICAL)` and give the `ListView` a minimum size.
Unrelated:
[spoiler]The UI system is a mess at first glance but once you learn how it works it's way better compared to some alternatives[/spoiler]

-------------------------

Lys0gen | 2020-04-24 17:21:49 UTC | #5

Thanks, those samples helped. In particular, ```button->SetFixedSize()``` did the trick.

Why does SetFixedSize work but SetSize does not?

-------------------------

throwawayerino | 2020-04-24 19:27:32 UTC | #6

My guess is that because the parent has zero size, any children with a non-fixed size would get overridden to zero. Check if the listview has a size set/layout too.

-------------------------

