throwawayerino | 2019-04-05 21:11:55 UTC | #1

I can make logic components just fine, I'm more annoyed by having to manually register each from the game's constructor. Also, how can I make and register logic nodes from angelscript for use from other scripts/C++?

-------------------------

Leith | 2019-04-06 10:32:07 UTC | #2

I know having to register custom components is tedious, but it's just how it is - even the internal Urho components have to provide static registration methods, that are called somewhere before construction of the components in question. I'm not sure what to say, other than hinting that macros can be powerful. As for AngelScript, I'll bite my tongue, since I have barely touched on it - I don't use the Scene Editor, and I don't rely on script. I'd rather write an editor myself, that is specific to my game, for several reasons.

-------------------------

throwawayerino | 2019-04-11 10:21:38 UTC | #3

is there anyway to check if a component is already registered?
Also I'm not talking about making scripts from the editor, but loading them arbitrarily like mods from the data folder. If that's not possible, then I may add a template component for scripts to add functions to instead

-------------------------

Leith | 2019-04-12 03:30:29 UTC | #4

Registering a C++ component class is really just about registering its objectfactory method with the urho3d context object.
I was going to give you a really long answer, but this should do, it's from the Context class:
[quote]
/// Create an object by type hash. Return pointer to it or null if no factory found.
SharedPtr<Object> CreateObject(StringHash objectType);
 [/quote]

For the scripting side of things, you can simply declare your stuff on the script side, and do all your logic on the script side, and then you don't need much of the c++ side, other than support for hotloading your script changes ;)

If you insist on a C++ to Script Interface, see "https://urho3d.github.io/documentation/1.7/_scripting.html"

-------------------------

