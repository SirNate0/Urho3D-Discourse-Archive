Mike | 2017-01-02 00:57:58 UTC | #1

In lua I'm trying to read an xml configuration file located in UserDocumentsDir.
I'm a bit lost as an XMLFile is a resource and mine is not located in the cache, so I can't use GetResource() function.

-------------------------

Azalrion | 2017-01-02 00:57:59 UTC | #2

You can't at the moment Lua doesn't have the XMLFile::Load(File) functionality exposed to be able to load from outside the ResourceCache.

-------------------------

cadaver | 2017-01-02 00:57:59 UTC | #3

If you check Resource.pkg, there should be the following registered, which takes filename as a string:

[code]
    tolua_outside bool ResourceLoad @ Load(const String fileName);
[/code]
Would that work?

-------------------------

Mike | 2017-01-02 00:57:59 UTC | #4

I've tried (myFile is the xml file with its path):
[code]
local config = XMLFile()
config:Load(File(myFile, FILE_READ))
or
config:Load(myFile)
[/code]

Maybe I'm doing something wrong (I get inspiration from Editor).

-------------------------

Azalrion | 2017-01-02 00:57:59 UTC | #5

Mike you can't do that at the moment, the XMLFile Load method isn't exposed to Lua.

Lasse's answer is probably the one you're after.

-------------------------

Mike | 2017-01-02 00:57:59 UTC | #6

Isn't there a bug in ResourceLoad() function that calls Save instead of Load ?

-------------------------

cadaver | 2017-01-02 00:57:59 UTC | #7

Indeed that was bugged. It should now be fixed. An example:

[code]
    local xml = XMLFile()
    xml:Load(fileSystem:GetProgramDir() .. "Data/Materials/Stone.xml")
    print(xml:GetRoot().name)
[/code]

-------------------------

Mike | 2017-01-02 00:57:59 UTC | #8

Cool, now everything is fine  :wink: 
What do you think of integrating this to sample #14 SoundEffects to transform it to a jukebox (along with a more sexy interface) ?

-------------------------

cadaver | 2017-01-02 00:57:59 UTC | #9

Sure, it's good to show some more non-traditional use (I mean, not an engine resource per se) of XMLFile.

-------------------------

Mike | 2017-01-02 00:57:59 UTC | #10

I'll give it a try thursday, being out until then.

It's really convenient to have a generic Load function for any kind of resource outside of the cache.
Many thanks to Aster for his great job.  :stuck_out_tongue:

-------------------------

