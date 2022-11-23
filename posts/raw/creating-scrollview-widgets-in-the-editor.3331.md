JTippetts | 2017-07-08 05:08:18 UTC | #1

What is the general workflow for creating UI widgets in the editor that incorporate ScrollView? I can't, for the life of me, figure out how to create the scroll bars and content element. I've got this widget:

<img src="//cdck-file-uploads-global.s3.dualstack.us-west-2.amazonaws.com/standard17/uploads/urho3d/original/1X/3a184413828e6435f550b74de30a53d65a660591.png" width="325" height="500">

I've been building it by hand but I'm trying to figure out how to build such a beast in the editor instead, for quicker iteration on designs. However, I can't figure out how to set up the content and scroll bars. For my own edification, I tried saving the widget to XML after creating it by hand, but importing the saved XML into the editor doesn't work well. The widget imports (sort of; the icons for the scroll arrows and scrollbar field are screwed up and there are other issues as well), and it has scroll bars and a content pane (albeit with the screwed up icons), but I can't access those internal elements via the edit tree. They appear on the widget, but I can't edit them.

I'm guessing that I need to create the widget in different pieces: the frame/box with the selector buttons and a panel for the scrollview widget, then manually set up the scroll view and scroll bars and add them to the panel. This seems kinda clunky to me. Am I missing something?

-------------------------

Mike | 2017-07-08 06:34:54 UTC | #2

I don't think you can fully build the ScrollView in the Editor, as it expects a content UIElement, not a child.
The easiest workflow is to build the Window and the ScrollView content (for example a Window with your rows) in the Editor.

Then in code:

	UIElement@ window = ui.LoadLayout(cache.GetResource("XMLFile", "UI/MyWindow.xml"));
	ScrollView@ scrollView = window.CreateChild("ScrollView");
	scrollView.SetStyleAuto();
	scrollView.autoDisableChildren = true;
	scrollView.SetScrollBarsVisible(false, true);
	UIElement@ content = ui.LoadLayout(cache.GetResource("XMLFile", "UI/MyContent.xml"));
	scrollView.contentElement = content;
Scroll bars visibility is controlled by SetScrollBarsVisible()
'MyContent.xml' is your SrollView content. It can be any UIElement.

You end up with this hierarchy:
Window (the main layout) > ScrollView (from code) > Window2 (content)

Note that you will certainly have to tweak size and alignment to get the expected display.

-------------------------

JTippetts | 2017-09-14 21:36:19 UTC | #3

Sorry, got sidetracked on this particular project. Looks like I can at least create the ScrollView widget in the editor, then grab it from the hierarchy and apply a style and that works okay.

-------------------------

