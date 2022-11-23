cin | 2017-01-02 00:57:32 UTC | #1

AngelScript allow to debug scripts: 
[angelcode.com/angelscript/sd ... debug.html](http://www.angelcode.com/angelscript/sdk/docs/manual/doc_debug.html)
[angelcode.com/angelscript/sd ... ugger.html](http://www.angelcode.com/angelscript/sdk/docs/manual/doc_addon_debugger.html)

May be add script debugging in scene editor, but it must be rewriten on C++ code.

I think what may be add simple showing variables and their values to Windows console and write to log-file and continue execute. May be add command line flags for set breakpoint on specific file and line.

-------------------------

cadaver | 2017-01-02 00:57:32 UTC | #2

Making an interactive debugger in the text console window would be quite straightforward. The Script subsystem could read commands from it (enable breakpoint, disable breakpoint, stop, continue etc.)

Making it graphical is considerably harder, because to keep the application logic intact everything must suspend on the breakpoint, rendering included, as otherwise the engine is still processing frames and events will be sent (and we don't want to make everything check "IsDebugging()" or something)

-------------------------

friesencr | 2017-01-02 00:57:33 UTC | #3

Even if it is a cli I would really like this.

-------------------------

Azalrion | 2017-01-02 00:57:33 UTC | #4

There is always the chance of implementing something similar to: [bitbucket.org/saejox/aspeek/wiki/Home](https://bitbucket.org/saejox/aspeek/wiki/Home) as that graphically would have no impact.

-------------------------

friesencr | 2017-01-02 00:59:59 UTC | #5

There was talk about removing civetsweb for the newly relicenced RakNet.  I don't know the timeline for replacing it or even if it will be replaced.

-------------------------

cadaver | 2017-01-02 00:59:59 UTC | #6

There is no urgent need to integrate RakNet. It is good, but looking at the codebase, it also has its own weirdnesses and issues. Also, unlike websocketpp, neither Civetweb or RakNet provide a websocket server natively, but they provide TCP functionality so that you can implement one yourself.

-------------------------

cadaver | 2017-01-02 01:00:00 UTC | #7

Very nice!

-------------------------

cadaver | 2017-01-02 01:00:46 UTC | #8

Building with the asEP_BUILD_WITHOUT_LINE_CUES == true setting has been an "overzealous" optimization without hard evidence to back it up. I think that can be forced to false and it doesn't need a switch. If I understand right it also affects compiled & saved bytecode, and in that case it's better that the user isn't accidentally able to compile scripts to be incompatible with full debugging support.

Controlling whether the debugger is built in would preferably be a CMake option, like URHO3D_ANGELSCRIPT_DEBUGGING. It's safest to default to false.

-------------------------

cadaver | 2017-01-02 01:00:49 UTC | #9

Storing include file names in lowercase is likely an artifact from the time we did not have nice case-insensitive compare functions. You should be able to remove that, if you ensure that case differences can't cause the same file to be included twice.

-------------------------

GoogleBot42 | 2020-03-21 13:15:21 UTC | #10

[quote="Sinoid"]
[b]Help request[/b]:

Would anyone with a Linux box be interested in checking if this all works for them. I'll shoot you the files to merge (just 4, and any diff tool should be sufficient). I've got it finished (well, finished-ish - a few quirks left to sort out) and compiling under MingW, so hopefully it all just works.

I'd like to get this all wrapped up.
[/quote]

I can help. :wink:

[quote="Sinoid"]

For Windows folks, I'm probably going to put my Angelscript IDE / asPeek debugger up onto github in a few days. WPF based tool (hence, windows only), with autocompletion, snippet, data-snippet (snippet with fields), attribute/event browser, type/class browser, auto-place event subscribers/handlers, etc.

[/quote]

What version of .net does it use?  Please say 4.0 or less then it will probably run in wine.  :smiley: I don't ever use windows and so booting into it is a huge pain because all of my tools and software is in linux.  Too bad mono doesn't support WPF at all...


EDIT: This is my 42nd post!  [url]http://en.wikipedia.org/wiki/42_%28number%29#The_Hitchhiker.27s_Guide_to_the_Galaxy[/url]

-------------------------

GoogleBot42 | 2017-01-02 01:04:09 UTC | #11

Cool thanks!  I would love to take a shoot at getting this running in wine.

-------------------------

