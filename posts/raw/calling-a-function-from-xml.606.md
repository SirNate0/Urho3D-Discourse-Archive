rogerdv | 2017-01-02 01:01:38 UTC | #1

I have been thinking about the design of my RPG dialog system, and I need to know if there is some way to specify inside XML an AngelScript function to be called by the dialog parser. Is this possible? Can I also pass some sort of parameter?

-------------------------

Azalrion | 2017-01-02 01:01:38 UTC | #2

Since you're most likely reading the xml yourself simply just do something like:

[code]
<dialogEntry>
    <file>MyDialog.as</file> <!-- Might not need this if you plan to execute via script instance -->
    <function>Func()</function>
</dialogEntry>
[/code]

Then when building your dialog class execute that function using ScriptFile or ScriptInstance.

From angelscript you can execute and pass parameters like so:
[code]
bool Execute(const String& functionName, const Variant[]@ parameters)
[/code]

-------------------------

