Xero | 2017-01-02 00:58:31 UTC | #1

Is the a attribute name/command that will set any user input in a lineEdit to uppercase in the ui xml file. For example if the user inputted hello, it would appear as HELLO?

-------------------------

friesencr | 2017-01-02 00:58:31 UTC | #2

would the textbox store hello internally and render HELLO or would it store HELLO?

-------------------------

Azalrion | 2017-01-02 00:58:31 UTC | #3

Store HELLO as Font/Text stores the char code value.

-------------------------

Xero | 2017-01-02 00:58:32 UTC | #4

friesencr i want it to store hello as HELLO and render as HELLO even if the enter lowercase characters

-------------------------

cadaver | 2017-01-02 00:58:32 UTC | #5

You can already hook to the TextChanged event of a LineEdit, GetText() to get the current text, convert that to uppercase, and SetText() again.

This is not a very good solution, because you also need to save the LineEdit's current cursor position, then restore it after setting the text, as SetText() always moves cursor to the end of the line. Also, you'll get another TextChanged event as a result of your programmatic change, so theoretically you could encounter infinite recursion. Practically on the second time SetText() notices that the text is same and does not send a further event.

Better would be for the LineEdit to send an event for each char entered, allowing you to manipulate it before it is inserted, by modifying the event data. I'm in the process of testing how well this works (the work-in-progress name for the event is called CharEntry) and if it works, will commit it soon.

EDIT: pushed. An example in AngelScript:

[code]
SubscribeToEvent(lineEdit, "CharEntry", "HandleCharEntry");

void HandleCharEntry(StringHash eventType, VariantMap& eventData)
{
    int c = eventData["Char"].GetInt();
    c = ToUpper(c);
    eventData["Char"] = c;
}
[/code]

-------------------------

Xero | 2017-01-02 00:58:32 UTC | #6

So i have created the ui in the editor and have done this script:
[code]
LineEdit @usernameLE;
void LoadUI()
{
@usernameLE = ui.root.GetChild("UsernameLineEdit", true);
SubscribeToEvent(usernameLE, "CharEntry", "HandleCharEntry");
}

void HandleCharEntry(StringHash eventType, VariantMap& eventData)
	{
		int c = eventData["Char"].GetInt();
		c = ToUpper(c);
		eventData["Char"] = c;
	}
	
[/code]

and now when i run my application the font does not change to uppercase

-------------------------

cadaver | 2017-01-02 00:58:32 UTC | #7

Check that you have compiled the latest head version of the engine, and that you get the element (usernameLE is not null)

-------------------------

Xero | 2017-01-02 00:58:33 UTC | #8

issue resolved, it works just fine, it was a mistake on my part

-------------------------

