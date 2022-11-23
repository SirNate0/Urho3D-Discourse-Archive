codingmonkey | 2017-01-02 01:02:42 UTC | #1

hi folks!

i'm trying to create simple game menu.
and it must hides/show then user press esc-key
i'm write some code but it no have any effect on UI visibility
why ? and how do this right ? for hide all or show all UI's elements.
[code]

	UI* ui = GetSubsystem<UI>();
	UIElement* root = ui->GetRoot();

	if (key == KEY_ESC)
	{
		if (isMainMenuActive_)
		{
			isMainMenuActive_ = false;
			input_->SetMouseVisible(isMainMenuActive_);
			root->SetVisible(isMainMenuActive_);	
			root->SetDeepEnabled(isMainMenuActive_);
			
		}
		else 
		{
			isMainMenuActive_ = true;
			input_->SetMouseVisible(isMainMenuActive_);
			root->SetVisible(isMainMenuActive_);
			root->SetDeepEnabled(isMainMenuActive_);
		}	
	}
[/code]

-------------------------

setzer22 | 2017-01-02 01:02:42 UTC | #2

Your code seems right to me. By disabling the UI it should be disappearing. Have you checked the key event gets really called when you press KEY_ESC? You can print something to the console to check.

Also, as an extra tip you can "toggle" the value of isMainMenuActive_ and avoid that extra if statement by doing:
[code]isMainMenuActive_ = !isMainMenuActive_;[/code]

-------------------------

codingmonkey | 2017-01-02 01:02:43 UTC | #3

>Have you checked the key event gets really called when you press KEY_ESC?
yes it's called 100%, i mark this block with debug breakpoint

>avoid that extra if statement by doing
ok i'm little rewrite code:

[code]
	UI* ui = GetSubsystem<UI>();
	UIElement* root = ui->GetRoot();

	if (key == KEY_ESC)
	{
		menu.isActive = !menu.isActive;

		input_->SetMouseVisible(menu.isActive);

		root->SetVisible(menu.isActive);
		root->SetDeepEnabled(menu.isActive);

		menu.btnExit->SetVisible(menu.isActive);
		
	}
[/code]

but it's still no hide all or show all UI elements, only my manualy added menu.btnExit (at last string) - shows/hides, other elements no. they all just change own disables or enables state, and not visibility

-------------------------

setzer22 | 2017-01-02 01:02:43 UTC | #4

Maybe the root's visible value does nothing? Try to iterate over its children and set visible to false for those. And I don't think you need to disable the UI, I only set the visible to false to hide it and it works fine for me, in fact I just did it (making a single window, and all its children invisible by setting visible to false).

-------------------------

codingmonkey | 2017-01-02 01:02:43 UTC | #5

Thanks! Now it works, 
but need do some check - "it yours UIElements or builded in engine?"  - Console, DebugHud...
otherwise it show all elements, including those that do not need.

[code]	UI* ui = GetSubsystem<UI>();
	UIElement* root = ui->GetRoot();


	if (key == KEY_ESC)
	{
		menu.isActive = !menu.isActive;

		Vector<SharedPtr<UIElement>> elements = root->GetChildren();
		
		for (unsigned int i = 0; i < elements.Size(); i++) 
		{
			if (elements[i]->GetVar("MENU").GetInt() == 1)
				elements[i]->SetVisible(menu.isActive);
		}
		
		input_->SetMouseVisible(menu.isActive);		
	}
[/code]

-------------------------

