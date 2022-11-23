Mike | 2017-01-02 00:57:39 UTC | #1

Global constants in generated LuaScriptAPI are not classified/themed, making their use very tedious.
The enums seem to have been set, but maybe they are not registered.
I'd like to fix this, can someone show me how to do it?

-------------------------

cadaver | 2017-01-02 00:57:39 UTC | #2

The script that generates the Lua docs is:

Source/Engine/LuaScript/pkgs/pkgToDox.lua

and it works by going through all pkg files. So basically you'd hack that script to work better :wink:

-------------------------

Mike | 2017-01-02 00:57:39 UTC | #3

Thanks, will give a look.

-------------------------

weitjong | 2017-01-02 00:57:39 UTC | #4

The generated html from Doxygen output is actually already themed as the outputs from all the other *.dox files. Perhaps you mean the classification or grouping could be better. What I find it difficult to read from these auto generated API documentation is that the list are ordered according to the content and order of pkg files being processed, instead of being ordered alphabetically. There is also currently no index page like those produced by Doxygen automatically for native C++ classes.

-------------------------

cadaver | 2017-01-02 00:57:41 UTC | #5

Yesterday I added alphabetical sorting to the AngelScript API. Wasn't ninja enough to apply the same to the lua API so for now I left it as-is.

It'd be quite easy to generate own page for each class, that would greatly reduce the main API page size.

-------------------------

Mike | 2017-01-02 00:57:41 UTC | #6

Alphabetical sorting for the lua API is on my todo list.
Personaly I prefer having all the API in one file/page, much easy to find what I'm looking for.
By the way, you're ninja enough, but I prefer you don't waste time with things like that  :wink:

-------------------------

ruminant | 2017-01-02 00:57:43 UTC | #7

Hi all,

I've done a quick and dirty pass on the Lua docs to generate a CHM (which gathers extra function details from doxygen output).  Hopefully it's helpful to someone out there.

Actually.  Hang on a mo'.  Looks like anti-spam has thwarted me for now...

-------------------------

ruminant | 2017-01-02 00:57:43 UTC | #8

Hi again,

Hopefully I can post the link this time around:

[url]https://www.dropbox.com/s/cigqpnmdx4h2o13/Urho3d_LuaApi.chm[/url]

-------------------------

Mike | 2017-01-02 00:57:43 UTC | #9

This makes it really easy to access what you're looking for, and in many different ways. :slight_smile: 
I definitely appreciate. Hope to see it soon in the build process!

-------------------------

