Culzean | 2017-11-23 15:18:44 UTC | #1

Hello, I am having trouble setting up a basic demo. I have created a new visual studio project to work in along side the sample projects. I have been able to change some of the graphical icons. However, not I want to load my own json file. However I have been completely unable to do this.
I placed the file in project/bin/data/models but no matter what path I use I cannot load any data.

I'm following this thread for using the api https://discourse.urho3d.io/t/json-loading-example/3086/2

	JSONFile& antjson = JSONFile(context_);
	antjson.LoadFile(path);

	JSONValue jsonArray = antjson.GetRoot();

But nothing is working, even the absolute path. What is going on?

-------------------------

Eugene | 2017-11-23 15:46:23 UTC | #2

[quote="Culzean, post:1, topic:3772"]
JSONFile& antjson = JSONFile(context_);
[/quote]

The interesting thing is how this line ever compiles. `Object`s are non-copyable.

The second interesting thing is where stored the object pointed by reference `antjson` and why it doesn't crash immediatelly.

-------------------------

Culzean | 2017-11-23 15:51:02 UTC | #3

I am attempting to use the resourceCache,

	JSONFile* jsonFile = cache->GetResource<JSONFile>("ant.json");

	JSONValue jsonArray = jsonFile->GetRoot();
	int size = jsonArray.Size();

the file is placed in bin/data
but still no luck. This crashes when attempting to read antjson which returns null.

Is there a solid example on this to follow?

-------------------------

Eugene | 2017-11-23 16:00:21 UTC | #4

[quote="Culzean, post:3, topic:3772"]
Is there a solid example on this to follow?
[/quote]

Check that resource cache internally has the same paths as you expect to see.
`LoadFile` must work with relative paths, resource cache will work with paths in cache dirs only.
It's hard to guess the rootcause without logs, but it's easy to debug. At least, check logs for errors.

-------------------------

Culzean | 2017-11-23 16:11:22 UTC | #5

Oh, it's loaded the file but encountered a parsing error. I am not getting any output to the VS console, is there a way to turn that on?

-------------------------

Eugene | 2017-11-23 16:16:09 UTC | #6

Urho put logs into your document folder by default, check it.

_TODO: Add optional logging to VS console_

-------------------------

Culzean | 2017-11-23 16:53:29 UTC | #7

Where are the logs? I cannot find them.
I'm find Urho3d hard to work with.
JSON file won't load, parser says it's fine.

Thanks

-------------------------

Eugene | 2017-11-23 17:44:21 UTC | #8

[quote="Culzean, post:7, topic:3772"]
Where are the logs? I cannot find them.
[/quote]

My default location is
`C:\Users\(username)\AppData\Roaming\urho3d\logs`

[quote="Culzean, post:7, topic:3772"]
I’m find Urho3d hard to work with.
[/quote]
Yes, it may be a bit hardcore.
Urho3D is fine if you treat is as C++ game framework and have enough skill in C++ developement.
It's not ready-to-use blackbox solution like Unity despite some people actually do everything in scripts.

[quote="Culzean, post:7, topic:3772"]
JSON file won’t load, parser says it’s fine.
[/quote]
Could you attach the file? It actually could be some bug because JSONs are not widely used in Urho.

-------------------------

weitjong | 2017-11-24 01:38:24 UTC | #9

There is a build option URHO3D_WIN32_CONSOLE to show the log in an console window.

-------------------------

