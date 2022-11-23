JulyForToday | 2017-01-02 01:14:11 UTC | #1

So I recently downloaded a fresh copy of Urho from master, and I wanted to separate the Editor from everything else spread through-out the Data folder, into it's own directory (so I could keep the editor, but remove everything else not relevant to my project). It's a bit of a PITA, but with some patience and find & replace I got it properly working again. Except for one (little) thing.

I was getting an error in the console when starting the editor: (actually, gives this twice)
[code]ERROR: Could not find resource UI/ScreenJoystick.xml
ERROR: Count not find inherited XML file: UI/ScreenJoystick.xml
ERROR: Could not find resource UI/ScreenJoystickSettings.xml
ERROR: Count not find inherited XML file: UI/ScreenJoystickSettings.xml[/code]

So I go looking for a reference in the Editor's angelscript code for [color=#800040]UI/ScreenJoystick.xml[/color]. Couldn't find one. So I do a search in the Urho C++ source. And sure enough, there is a hardcoded reference to [color=#800040]UI/ScreenJoystick.xml[/color] in Input.cpp, in AddScreenJoystick(). Well, that doesn't seem ideal. But I wasn't going to bother with changing it and recompiling the player, etc. So I do a search in the editor's code for a call to AddScreenJoystick (since it is literally the only place referencing that damn joystick file). I was unable to find a single call to it. Strange. Clearly [i][b]something[/b][/i] must be calling AddScreenJoystick [b][i]somewhere[/i][/b]... After abusing my ctrl and f keys a bit, I grew frustrated and gave up. Fortunately those messages only presents a minor annoyance. Still felt it was worthwhile to point out these string's existences.

[b]TL;DR[/b]
[u][b]MAGIC STRINGS[/b][/u]
Input.cpp [color=#800040]"UI/ScreenJoystick.xml"[/color] (in AddScreenJoystick(...))
MessageBox.cpp [color=#800040]"UI/MessageBox.xml"[/color] (in constructor)

In both cases, the method in question has a parameter XMLFile* layoutFile, and does a check. When the check fails it loads the file specified in the magic string. In both cases there is an assumption made that those directories and files will exist in a user's Data directory, which may not be the case at all.

There are a few similar magic strings in the source for the Graphics system, but those refer to the RenderPaths / Technique folders inside the CoreData directory, the existence of which seems like a reasonable assumption.

Unfortunately I don't know the best approach for removing them. If I did I would just make a pull request. Maybe something along the lines of a config file that specifies these locations, and the config file itself would be in the CoreData folder?

-------------------------

cadaver | 2017-01-02 01:14:12 UTC | #2

You could think of those files as "CoreData" for the UI / Input and they could as well be moved to CoreData. This hardcoding isn't IMO more egregious than the hardcoding of a default renderpath or default spot light attenuation texture, and are needed for the features in question.

-------------------------

