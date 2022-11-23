graveman | 2017-01-02 01:08:52 UTC | #1

What I have to do if I want use just a part of Urho3D source code, not whole? 
For example, if I want to use only Urho3D containers, can I put only Urho's "Container" folder in   "external" folder of my project's source code directory instead of putting whole Urho3D source code (i.e whole "Engine" folder)  into it?

-------------------------

cadaver | 2017-01-02 01:08:52 UTC | #2

Sounds perfectly doable, just don't expect especial support for it. You may have to do some adjustments on your own, for example the Container folder files have "#include <Urho3D/Urho3D.h>". Finally, remember to comply with the license just as if you were using the whole engine.

-------------------------

graveman | 2017-01-02 01:08:53 UTC | #3

[quote="cadaver"] Finally, remember to comply with the license just as if you were using the whole engine.[/quote]
To comply with the license I thinkI have nothing to do if I don't modify the files is not it?

-------------------------

cadaver | 2017-01-02 01:08:54 UTC | #4

I mean just having the Urho license text somewhere. Well, practically the code files already have it. :slight_smile:

-------------------------

graveman | 2017-01-02 01:08:55 UTC | #5

[quote="cadaver"]I mean just having the Urho license text somewhere. Well, practically the code files already have it. :slight_smile:[/quote]
Thanks for you answer!

-------------------------

