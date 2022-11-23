rogerdv | 2017-01-02 01:01:21 UTC | #1

Im trying to use the editor to create a basic UI: a window with some buttons inside, but I have a few doubts about the process. First, I cant load the layout, I tried this:
[code]XMLFile* style = cache->GetResource<XMLFile>("UI/DefaultStyle.xml");
				XMLFile* UIlayout = cache->GetResource<XMLFile>("UI/DNT.xml");

				uiRoot = GetSubsystem<UI>()->LoadLayout(UIlayout, style);[/code]
But the ui elements are never displayed. I know th UI is working because I add a text in the code and I can see it, but the elements that were supposed to be loaded from XML file are not visible. Obviously, Im missing something here, but cant find what in the sample (which doesnt covers loading layouts) or docs.

-------------------------

Mike | 2017-01-02 01:01:21 UTC | #2

After loading the resource file you need to parent it to the root UI or to another UIElement:
[code]GetSubsystem<UI>() -> GetRoot() -> AddChild(uiRoot);[/code]

-------------------------

friesencr | 2017-01-02 01:01:21 UTC | #3

You might want to be careful of calling something the root.  Urho has a reserved node that it uses at the top of the hierarchy called the root.  There is not harm in calling it that as long you don't confuse yourself.  I am easily confused :slight_smile:

-------------------------

rogerdv | 2017-01-02 01:01:21 UTC | #4

The docs confused me a bit, seems that by "root" they mean the root element of the layout being loaded. And UI has no addChild member, but the idea is correct, this is the working code:
[code]uiRoot = GetSubsystem<UI>()->LoadLayout(UIlayout);
				uiRoot->SetDefaultStyle(style);
				GetSubsystem<UI>()->GetRoot()->AddChild(uiRoot);[/code]

-------------------------

