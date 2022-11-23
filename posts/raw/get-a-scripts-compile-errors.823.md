setzer22 | 2017-01-02 01:03:10 UTC | #1

When loading a ScriptFile with the ResourceCache, how can I get the error message if the script didn't compile well in order to display it to the log? 

The editor is able to do this but I can't find where it does it.

-------------------------

Mike | 2017-01-02 01:03:11 UTC | #2

The Editor pops up the console thanks to Console::SetAutoVisibleOnError().

-------------------------

setzer22 | 2017-01-02 01:03:12 UTC | #3

Is that output also printed in stdout in case there's no console? (I'm talking about linux particulary)

-------------------------

weitjong | 2017-01-02 01:03:12 UTC | #4

According to my understanding, yes. All the log output and error are sent to the standard output and error streams, respectively.

-------------------------

setzer22 | 2017-01-02 01:03:12 UTC | #5

If I'm not using the editor I can clearly see my script not compiling correctly and an error log saying the script didn't compile correctly, both in stdout and the console, but the compile error is only printed while using the editor.

So I'm basically after getting the compile errors when not launching scripts through the Editor/Urho3DPlayer. Any clues on that?

-------------------------

cadaver | 2017-01-02 01:03:12 UTC | #6

Any messages from AngelScript should go through Script::MessageCallback(const asSMessageInfo* msg), which logs them to the Urho3D log. 

For example if I modify the Rotator.as script to contain an error, the 21_AngelScriptIntegration example does log the compile errors, so nothing there shouldn't be Urho3DPlayer / Editor specific.

-------------------------

friesencr | 2017-01-02 01:03:12 UTC | #7

I remember there not being error info if your code errors happened in a different module.  It has been a year since I have used that code so my mind is a bit foggy.  It only printed errors from the executing module.

-------------------------

setzer22 | 2017-01-02 01:03:14 UTC | #8

[quote="cadaver"]Any messages from AngelScript should go through Script::MessageCallback(const asSMessageInfo* msg), which logs them to the Urho3D log. 

For example if I modify the Rotator.as script to contain an error, the 21_AngelScriptIntegration example does log the compile errors, so nothing there shouldn't be Urho3DPlayer / Editor specific.[/quote]

Should I set that message callback to the script engine when creating it then?

I'll just have a look at the sample code, thank you!

-------------------------

cadaver | 2017-01-02 01:03:14 UTC | #9

The Script subsystem sets the callback automatically when constructing itself and the AngelScript engine.

-------------------------

setzer22 | 2017-01-02 01:03:14 UTC | #10

I don't see what I could possibly be doing wrong then. The script subsystem is properly registered like in the Sample code (it's just one line of code, isn't it?)

I'm loading my scripts inside a class like this:

[code]ScriptFile* state = cache->GetResource<ScriptFile>(SCRIPT_PATH);[/code]

The  ResourceCache is passed to that Class as a Constructor argument. That class inherits from RefCounted.

Oddly enough I noticed the pointer is null when the script has an error, instead of returning IsCompiled() = false.

The editor doesn't have problems in outputting compile errors when I load scripts like this, so I guess the problem has to be in my main application class the . I'll post it later when I get home.

-------------------------

cadaver | 2017-01-02 01:03:14 UTC | #11

The default behavior of ResourceCache is to return null for failed resources (and not store them.) Editor changes this with ResourceCache::SetReturnFailedResources(true). This should not have any difference for the error logging, though.

-------------------------

