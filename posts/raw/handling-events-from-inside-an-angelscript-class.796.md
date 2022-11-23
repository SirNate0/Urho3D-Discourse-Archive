JulyForToday | 2017-01-02 01:02:57 UTC | #1

Hi again. Back with another snag.

Went searching through the forums, and [url=http://discourse.urho3d.io/t/angelscript-scriptobject-methods/366/6]this thread[/url] [i]almost[/i] covers what I'm interested in.

Here is the issue: in angelscript, I have a Main.as that has a bunch of code (stolen from one of the samples) and Start() calls a SubscribeEvents() method, which calls SubscribeToEvent() to register some event handlers.

Main.as
[code]
#include "Stuff.as"
void Start()
{
	SubscriberToEvents();
}

void SubscribeToEvents()
{
	SubscribeToEvent("KeyDown", "HandleKeyDown");
	SubscribeToEvent("UIMouseClick", "HandleUIMouseClick");
	SubscribeToEvent("Update", "HandleUpdate");
	SubscribeToEvent("PostUpdate", "HandlePostUpdate");
}
[/code]
There is more code in main.as, but I'm keeping it simple for clarity. Everything runs fine with things set up this way.

Now I want to move most of the code in Main.as, including the handlers and the SubscribeToEvents() method over into another class. Then Main.as will work mainly as an entry point, and I can instantiate that new class in Main.as instead:

Main.as
[code]
#include "FPSGame.as"
void Start()
{
	FPSGame@ game = FPSGame();
}
[/code]

FPSGame.as
[code]
#include "Stuff.as"
class FPSGame
{
	FPSGame()
	{
		SubscribeToEvents();
	}

	void SubscribeToEvents()
	{
		SubscribeToEvent("KeyDown", "HandleKeyDown");
		SubscribeToEvent("UIMouseClick", "HandleUIMouseClick");
		SubscribeToEvent("Update", "HandleUpdate");
		SubscribeToEvent("PostUpdate", "HandlePostUpdate");
	}
}
[/code]

The scripts do compile and run, but none of the event handlers in FPSGame fire (HandleKeyDown, HandleUIMouseClick, etc..). Which of course is undesirable.

[url=http://urho3d.github.io/documentation/HEAD/_scripting.html]From the documentation:[/url]
[quote]Subscribing to events in script behaves differently depending on whether SubscribeToEvent() is called from a script object's method, or from a procedural script function. If called from an instantiated script object, the ScriptInstance becomes the event receiver on the C++ side, and calls the specified handler method when the event arrives. If called from a function, the ScriptFile will be the event receiver and the handler must be a free function in the same script file. The third case is if the event is subscribed to from a script object that does not belong to a ScriptInstance. In that case the ScriptFile will create a proxy C++ object on demand to be able to forward the event to the script object.[/quote]

So SubscribeToEvent() has 3 modes of operating.
[ul]
[*] ScriptInstance (not applicable here)[/*]
[*] Procedural (which is what is happening in the original Main.as)[/*]
[*] Proxy (which I'm fairly sure is applicable here)[/*]
[/ul]

Now I'm not sure that the script object mentioned in that paragraph means a plain vanilla angelscript object (class), or a ScriptObject from Urho, which FPSGame could inherit from, although I'm not sure I want to do that (I tried that, and it didn't work anyways). Maybe there is a special way to register the eventhandlers with that proxy object mentioned?

It seems like I should be able to use normal angelscript classes to build my application, and only use ScriptObject when those classes will be used in a ScriptInstance (which FPSGame never would be). Or maybe I'm wrong about that. But either way, I can't get the events to work in the FPSGame class.

-------------------------

Bluemoon | 2017-01-02 01:02:57 UTC | #2

To be able to subscribe to and handle event in an angelscript class, the class would have to inherit from the ScriptObject angelscript class. Try making your scriptclass inherit from scriptobject, it should work.

-------------------------

friesencr | 2017-01-02 01:02:58 UTC | #3

You don't have to inherit from scriptobject.  Tried to find one without specified sender - no luck.

The ViewportContext in the Editor does this:

[github.com/urho3d/Urho3D/blob/m ... iew.as#L75](https://github.com/urho3d/Urho3D/blob/master/bin/Data/Scripts/Editor/EditorView.as#L75)

-------------------------

JulyForToday | 2017-01-02 01:02:58 UTC | #4

I made a small, runnable, example:
(warning, the 2nd one will will require alt-tab or alt-ctrl-del to unfocus the window to close the program)

Example 1 <- this works fine. Event handlers get called, so the text changes and F1 opens/closes console, and the program closes with Escape
Main.as (A)
[code]
Text@ label;

void Start()
{
	SubscribeToEvents();
	CreateConsoleAndDebugHud();
	CreateOverlays();
	console.visible = true;
}
void CreateConsoleAndDebugHud()
{
	// Get default style
	XMLFile@ xmlFile = cache.GetResource("XMLFile", "UI/DefaultStyle.xml");
	if (xmlFile is null)
		return;
	// Create console
	Console@ console = engine.CreateConsole();
	console.defaultStyle = xmlFile;
	console.background.opacity = 0.8f;
}

void SetLabel(String text)
{
	label.text = text;
}
void CreateOverlays()
{	
	Font@ font = cache.GetResource("Font", "Fonts/bluehighway.ttf");
	label = Text();
	label.SetFont(font, 32);
	label.SetAlignment(HA_CENTER, VA_CENTER);
	label.SetPosition(HA_CENTER, VA_CENTER);
	ui.root.AddChild(label);
	label.text = "Action Text";
}

//specify sender?
void SubscribeToEvents()
{
	Print("TESTGAME SubscribeToEvents");
	SubscribeToEvent("KeyDown", "HandleKeyDown");
	SubscribeToEvent("UIMouseClick", "HandleUIMouseClick");
	SubscribeToEvent("Update", "HandleUpdate");
}

void HandleKeyDown(StringHash eventType, VariantMap& eventData)
{
	int key = eventData["Key"].GetInt();

	// Close console (if open) or exit when ESC is pressed
	if (key == KEY_ESC)
	{
		if (!console.visible)
			engine.Exit();
		else
			console.visible = false;
	}

	// Toggle console with F1
	else if (key == KEY_F1)
		console.Toggle();
}

void HandleUIMouseClick(StringHash eventType, VariantMap& eventData)
{
	Print("MOUSE CLICK");
	SetLabel("MOUSE CLICK");
}
void HandleUpdate(StringHash eventType, VariantMap& eventData)
{
	Print("UPDATE");
	SetLabel("UPDATE");
}

[/code]

Example 2  <- Same code, just moved most of it into the TestGame class. Seems as though it ought to work. But none of the event handlers are ever called.
Main.as (B)
[code]
#include "Scripts/TestGame.as"
void Start()
{
	CreateConsoleAndDebugHud();
	TestGame@ game = TestGame();
	console.visible = true;
}
void CreateConsoleAndDebugHud()
{
	// Get default style
	XMLFile@ xmlFile = cache.GetResource("XMLFile", "UI/DefaultStyle.xml");
	if (xmlFile is null)
		return;
	// Create console
	Console@ console = engine.CreateConsole();
	console.defaultStyle = xmlFile;
	console.background.opacity = 0.8f;
}
[/code]

TestGame.as
[code]
class TestGame
{
	Text@ label;

	TestGame()
	{
		CreateOverlays();
		SubscribeToEvents();
	}
	
	void SetLabel(String text)
	{
		label.text = text;
	}
	void CreateOverlays()
	{	
		Font@ font = cache.GetResource("Font", "Fonts/bluehighway.ttf");
		label = Text();
		label.SetFont(font, 32);
		label.SetAlignment(HA_CENTER, VA_CENTER);
		label.SetPosition(HA_CENTER, VA_CENTER);
		ui.root.AddChild(label);
		label.text = "Action Text";
	}
	
	//specify sender?
	void SubscribeToEvents()
	{
		Print("TESTGAME SubscribeToEvents");
		SubscribeToEvent("KeyDown", "HandleKeyDown");
		SubscribeToEvent("UIMouseClick", "HandleUIMouseClick");
		SubscribeToEvent("Update", "HandleUpdate");
	}

	void HandleKeyDown(StringHash eventType, VariantMap& eventData)
	{
		int key = eventData["Key"].GetInt();

		// Close console (if open) or exit when ESC is pressed
		if (key == KEY_ESC)
		{
			if (!console.visible)
				engine.Exit();
			else
				console.visible = false;
		}

		// Toggle console with F1
		else if (key == KEY_F1)
			console.Toggle();
	}
	
	void HandleUIMouseClick(StringHash eventType, VariantMap& eventData)
	{
		Print("MOUSE CLICK");
		SetLabel("MOUSE CLICK");
	}
	void HandleUpdate(StringHash eventType, VariantMap& eventData)
	{
		Print("UPDATE");
		SetLabel("UPDATE");
	}
}
[/code]

I tried making TestGame inherit from ScriptObject, it doesn't seem to cause a change. The handlers still will not be called.

I noticed that ViewportContext doesn't call it's CreateViewportContextUI() method for registering it's handlers, it's called externally from outside the class's scope (I'm guess it's the module's global scope). So I tried moving the call to TestGame's SubscribeToEvents() method from TestGame's constructor into Main's Start() method after instantiating the class. No luck with that.

I don't know if it would have anything to do with not specifying a sender for the event handler. Not sure what I would specify as senders for these events.

-------------------------

friesencr | 2017-01-02 01:02:58 UTC | #5

wonder if you class is getting removed from going out of scope.

[code]
  TestGame@ game = TestGame();
[/code]

Try putting it in a global variable.
[code]
TestGame@ game;
void Start()
{
   CreateConsoleAndDebugHud();
   @game = TestGame();
   console.visible = true;
}

[/code]

-------------------------

JulyForToday | 2017-01-02 01:02:59 UTC | #6

I think you were right, using a global variable fixed the problem.
_________________________________________________________

However, I did run into something noteworthy while using your suggestion.
[code]
@game = TestGame();
[/code]
I didn't notice that @ symbol at first, so I wrote it like this:
[code]
game = TestGame();
[/code]

This seemingly fixed the events in my sample, although the console was logging a Null Pointer Access exception in Start() on that line.

I tried the same change on my actual code, and it was still having trouble with the event handlers not being called. So I expanded my sample so that TestGame contained a Scene object, and a Node object. Then added a simple TestObject class ( that inherits from ScriptObject), and created a method in TestGame that added a ScriptInstance to the node. And I narrowed the problem down to where I was using CreateScriptObject() on the node inside TestGame.

[code]
 	void CreateTestObject(Vector3 position)
	{
		testObjectNode = scene_.CreateChild("TestObject");
		testObjectNode.position = position;		
		
		testObjectNode.CreateScriptObject(scriptFile, "TestObject");
		TestObject@ testObject = cast<TestObject>(testObjectNode.GetScriptObject());
		if(testObject is null)
			SetLabel("NULL TEST OBJECT");
		String testText = testObject.GetTestString();
		SetLabel(testText);
	}
[/code]

That call to CreateScriptObject() was doing something that caused the event handlers to not get fired (still not sure why).
I was further confused because I thought maybe it was an issue with the [b]scriptFile[/b] reference not being valid in the scope of TestGame.as. I now think this is not the case, [b]scriptFile[/b] seems to be a module wide reference, so as long as you're in the same module it will work, including in a vanilla class. Correct me if I'm wrong about that. Since I thought [b]scriptFile[/b] might be different for each class/file, I looked at the scripting documentation and found CreateScriptObject() can take a string of the script's filename.

[quote]
There are shortcut methods on the script side for creating and accessing a node's script object: node.CreateScriptObject() and node.GetScriptObject(). Alternatively, if the node has only one ScriptInstance, and a specific class is not needed, the node's scriptObject property can also be used. CreateScriptObject() takes the script file name (or alternatively, a ScriptFile object handle) and class name as parameters and creates a ScriptInstance component automatically, then creates the script object. For example:

[code]ScriptObject@ object = node.CreateScriptObject("Scripts/MyClass.as", "MyClass");[/code]
[/quote]

So I used "Scripts/Main.as" instead of [b]scriptFile[/b]  and it (obviously, in hindsight) didn't change anything. So being confused, I was going to post the second sample, when I noticed you were using that @ symbol. I gave it a try, and now everything works as I would expect it to. No more Null Pointer Access exception, and the events handlers fire, and I can do what I want with my ScriptObjects contained inside of my vanilla TestGame class.

Thought I'd include all this in case anyone in the future encounters similar problems.
_______________________________________________________________

So what is the significance of the @ symbol prefixed on the global reference, and why do you think it would cause the kinds of secondary problems I was having with CreateScriptObject() ?

And I should really brush up on my reading skills. lmao  :laughing:

-------------------------

friesencr | 2017-01-02 01:03:00 UTC | #7

The @ is much like a pointer.  Angelscript calls it a 'handle'.  If you create a variable by handle than you can pass by reference rather than by value.  Urho does a kind of tricky thing that I don't always like in that it will always assign by reference and pass by reference with its own class types like the script object.  In Urho you can't make a IntVector with a @ since it is purely a value type in urho.  There was a time when you did have to use the handle but only had to use it some of the time and that was more confusing.  This is hardly anything offensive but has created a sort of loose screw rattling in my brain when it shakes and I wonder what I forgot to screw down.  For your own created classes you have to properly use the handle.

-------------------------

