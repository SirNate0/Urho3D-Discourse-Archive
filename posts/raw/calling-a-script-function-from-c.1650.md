Enhex | 2017-01-02 01:09:14 UTC | #1

[urho3d.github.io/documentation/H ... pting.html](http://urho3d.github.io/documentation/HEAD/_scripting.html) documents that you can call a script-side function from C++.
But it doesn't cover getting a return value, or passing references. Are those possible?

-------------------------

cadaver | 2017-01-02 01:09:14 UTC | #2

There is currently no safe engine-supported way for this. Rather you need to go to AngelScript internal classes. You should be able to get the AngelScript context that was used for the last function call execution with Script::GetScriptFileContext(), then access the context for the return value.

-------------------------

Sir_Nate | 2017-01-02 01:09:14 UTC | #3

I think you need to make Script::GetScriptFileContext() to that, however.
If you don't need to do it to often, you could try putting the results in a node's user variables. 
I will say, though, that with a non-AngelScript-internal class (i.e. IntVector2 instead of using an (AngelScript) int), I was able to pass it as an &out reference and read the value from it.

-------------------------

Enhex | 2017-01-02 01:09:14 UTC | #4

[quote="Sir Nate"]I think you need to make Script::GetScriptFileContext() to that, however.
If you don't need to do it to often, you could try putting the results in a node's user variables. 
I will say, though, that with a non-AngelScript-internal class (i.e. IntVector2 instead of using an (AngelScript) int), I was able to pass it as an &out reference and read the value from it.[/quote]

How did you pass a &out reference? As a void pointer?

-------------------------

