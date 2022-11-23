exessuz | 2017-01-02 01:08:11 UTC | #1

Hi guys, the game I am currently developing was running very smoothly with high FPS until I started adding menus and GUI objects.
I have at the moment three buttons in root, each opens a different window, each window has about 25 buttons, im adding the childs to each window with the following code.


[code]

        window = new Window(core->GetContext());
	window->SetStyle("Window1");
	window->SetVisible(false);
	window->SetAlignment(HorizontalAlignment::HA_CENTER, VerticalAlignment::VA_CENTER);
	window->SetLayout(LayoutMode::LM_FREE, 6, IntRect(6, 6, 6, 6));
	window->SetSize(320, 390);
	window->SetEnabled(false);

	root->AddChild(window);

	int offset = 14;
	int pz = 0;

	for (int z = 0; z < 5; z++)
	{
		for (int x = 0; x < 5; x++)
		{
			Button *b = new Button(core->GetContext());
			b->SetStyle("EmptySpace");
			pz = z * 64 + (offset*z);
			b->SetPosition(x * 64, pz);
			b->SetName(std::to_string(z * 5 + x).c_str());
			window->AddChild(b);

			Text *text = new Text(core->GetContext());
			text->SetStyle("Text");

			text->SetPosition(x * 64 + 32, pz + (64));
			text->SetName(std::to_string(z * 5 + x).c_str());

			window->AddChild(text);
		}
	}

	window->SetEnabledRecursive(false);

[/code]

with only 1 window it was working great but now with 3, the profiler gives me from 1 to 2+ on GetUIBatch. What am I doing wrong? I have all the windows hidden and enablerecursive to false on init, so I would expect that all the ui elements of the windows would not be tested for collition each frame neither rendered. I was thinking that maybe I should switch to Urho2D instead for the GUI rendering.

Thanks for any advice.

-------------------------

exessuz | 2017-01-02 01:08:12 UTC | #2

Sinoid I am using a custom skin but I kept the same .png size as the default also Im not switching from texture to texture, 1 to 2+ is the average (sometimes way more than 2) that I get on the GetUIBatch (the units i guess milli seconds). The trouble is that I have many StaticModelGroup with many objects and it runs great but as soon as I add the gui the fps drops a lot in both release and debug mode.

Thank you

-------------------------

