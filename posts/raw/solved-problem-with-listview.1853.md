krokodilcapa | 2017-01-02 01:10:44 UTC | #1

I have a strange problem with ListView, it displays its items on top of each other. Am I doing something wrong, or its a bug?

Here is the code:
[code]	window->SetSize(600, 200);
	window->SetAlignment(HA_CENTER, VA_BOTTOM);
	window->SetPosition(0, -50);
	window->SetOpacity(0.5f);
	window->SetStyleAuto();

	listview = window->CreateChild<ListView>();
	listview->SetSize(500, 100);
	listview->SetAlignment(HA_CENTER, VA_BOTTOM);
	listview->SetStyleAuto();

	ResourceCache* cache = GetSubsystem<ResourceCache>();
	XMLFile* style = cache->GetResource<XMLFile>("UI/DefaultStyle.xml");

	for (int i = 0; i < 4; ++i)
	{
		Text* text = new Text(context_);
		text->SetDefaultStyle(style);
		text->SetStyleAuto();
		text->SetText("TEXT" + i);
		text->SetColor(Color::BLACK);
		listview->AddItem(text);
	}[/code]

Here is a picture: [url]http://imgur.com/wRw1fbz[/url]

Edit:
Okay, its works now, I just forgot to set the default UI style!  :unamused:

-------------------------

rasteron | 2017-01-02 01:10:44 UTC | #2

Hi, I'm sure that you just have some attributes or items missing or related to that stuff, but try constructing it first as XML in the editor for draft and make the translation with the dynamic c++ counterpart when you got it down.

-------------------------

krokodilcapa | 2017-01-02 01:10:45 UTC | #3

Thanks rasteron, you were right, I forgot to set the default style of the ui root!

-------------------------

