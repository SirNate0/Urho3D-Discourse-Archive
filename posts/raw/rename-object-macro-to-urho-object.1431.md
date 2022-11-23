Pyromancer | 2017-01-02 01:07:41 UTC | #1

Something I've been wondering about is why the engine's macros aren't prefixed with anything. OBJECT as a macro could be used in numerous other libraries, and I personally think it's much safer to prefix macros with something unique to the framework it is a part of anyway. I already do this in my fork of the engine, but my fork isn't ready for a pull request just yet, so I was wondering if it's something you guys could do on the mainline.

-------------------------

cadaver | 2017-01-02 01:07:42 UTC | #2

Good idea. When the macros were originally written, Urho didn't have a namespace either. Should be mostly a search-replace.

-------------------------

Pyromancer | 2017-01-02 01:07:42 UTC | #3

Yeah, pretty much is. Good deal. :slight_smile:

-------------------------

