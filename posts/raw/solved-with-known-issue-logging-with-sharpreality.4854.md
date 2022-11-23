I3DB | 2019-01-25 21:32:09 UTC | #1

In the samples provided by @Egorbo he[adds an event handler for logging in one sample](https://github.com/xamarin/urho-samples/blob/b72d055a424d0e6be825c0239683c225d29ee723/HoloLens/02_HelloWorldAdvanced/Program.cs#L41).

When I try to use this, no output ever appears if I write a logging statement.

So these lines of code produce this output:
```
Log.LogMessage += l => { Debug.WriteLine(l.Level + ":  " + l.Message); };
Debug.WriteLine(LogLevel.Warning, "MS debug logger.");
Urho.IO.Log.Write(LogLevel.Warning, "Urho3d logger");
```
```
MS debug logger.: Warning
```

Now, every now and then, Visual Studio's output window will show a message that does appear to have come from the Urho.dll, typically some error message that must have used the Urho log. I assume that because the format is the same as the event handler.

My question is how to use it?

-------------------------

Leith | 2019-01-24 08:35:34 UTC | #2

I think the right answer is that logging is disabled by default
You can try this to make it work.

[code]
#define URHO3D_LOGGING 1
#include "Urho3D/IO/Log.h"
[/code]

If this is insufficient, and no better answer is forthcoming, I will jump onto Windows and find out whats going on :slight_smile:

I have Windows, but I tend not to ever boot into it.

-------------------------

I3DB | 2019-01-25 17:12:44 UTC | #3

I'm working with the SharpReality binding for Urho.dll.

It's all c#.

[Maybe it's related to this](https://github.com/xamarin/urho/issues/355).

-------------------------

I3DB | 2019-01-25 20:41:29 UTC | #4

Got it working, but it's a bet messed up.

In the start method, added this code:
```
Log.Level = (int)LogLevel.Error;
Log.LogMessage += l => { Debug.WriteLine(l.Level + ":)  " + l.Message); };
```

Then to log something, here's an example
```
Urho.IO.Log.Write(LogLevel.Error, "This is the start finished message using urho logging via handler");
```

This will output
```
[Fri Jan 25 15:00:25 2019] WARNING: This is the start finished message using urho logging via handler
```

To show how messed up it is, wrote this code:
```
Log.Level = (int)LogLevel.Debug;
Urho.IO.Log.Write(LogLevel.Raw, "Set to debug. This is the the raw message");
Urho.IO.Log.Write(LogLevel.Debug, "This is the debug message");
Urho.IO.Log.Write(LogLevel.Info, "This is the info message");
Urho.IO.Log.Write(LogLevel.Warning, "This is the warning message");
Urho.IO.Log.Write(LogLevel.Error, "This is the error message");
Urho.IO.Log.Write(LogLevel.None, "This is the none message");

Log.Level = (int)LogLevel.None;
Urho.IO.Log.Write(LogLevel.Raw, "Set to none. This is the the raw message");
Urho.IO.Log.Write(LogLevel.Debug, "This is the debug message");
Urho.IO.Log.Write(LogLevel.Info, "This is the info message");
Urho.IO.Log.Write(LogLevel.Warning, "This is the warning message");
Urho.IO.Log.Write(LogLevel.Error, "This is the error message");
Urho.IO.Log.Write(LogLevel.None, "This is the none message");
```

Which outputs this:
```
2:)  Set to debug. This is the the raw message
0:)  [Fri Jan 25 15:15:06 2019] TRACE: This is the debug message
1:)  [Fri Jan 25 15:15:06 2019] DEBUG: This is the info message
2:)  [Fri Jan 25 15:15:06 2019] INFO: This is the warning message
3:)  [Fri Jan 25 15:15:06 2019] WARNING: This is the error message
This is the none message. You can omit this exception by subscribing to Urho.Application.UnhandledException event and set Handled property to True.
ApplicationOptions: args -w -nolimit -x 1268 -y 720 -p "CoreData;Data" -touch -hd -landscape -portrait :Error
4:)  [Fri Jan 25 15:15:06 2019] ERROR: This is the none message
2:)  Set to none. This is the the raw message
This is the none message. You can omit this exception by subscribing to Urho.Application.UnhandledException event and set Handled property to True.
ApplicationOptions: args -w -nolimit -x 1268 -y 720 -p "CoreData;Data" -touch -hd -landscape -portrait :Error
4:)  [Fri Jan 25 15:15:06 2019] ERROR: This is the none message
```

-------------------------

