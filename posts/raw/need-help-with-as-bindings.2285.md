Eugene | 2017-01-02 01:14:30 UTC | #1

I have a structure like following:
[code]struct Struct { Vector<StringHash> hashes; }[/code]

I want to create binding of Struct in AS and do something like this:
[code]o.hashes.Push(StringHash("String"));[/code]

I see usage of getters/setters, but in my case they are not working probably because VectorToArray/ArrayToVector make copies.
How can I write such binding?

-------------------------

cadaver | 2017-01-02 01:14:30 UTC | #2

Vector or other containers aren't directly bound to AS, so you can't do those nicely. The design of several classes has been informed by this difficulty and that's why for example RenderPath class has an explicit API for adding / inserting / removing RenderPathCommands.

Maybe the minimal API you can easily bind is to create get/set accessors for "numHashes", which controls the size of the vector, and indexed get/set accessors for "hashes" which allow indexing the vector.

You'll also see that often the scripting API for a particular class isn't 100% complete (especially so-called "public internals" called by other subsystems) but this isn't a problem as long as the public API is usable enough to do everything that you need for normal use.

-------------------------

