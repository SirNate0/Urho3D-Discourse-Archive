ddubie | 2017-11-30 09:31:26 UTC | #1

Hello~ 
I'm a Urho3d newbie :D.
I'm trying to make tweening script  via angelscript.
My scripts' class' variable needs  non built-in enum values.
(like enum LoopType { once, loop, yoyo };)

I added enum value on c++ project using 
asCScriptEngine::RegisterEnum(const char*)
asCScriptEngine::RegisterEnumValue(const char*, const char *, int) 
functions and compiled angelscript successfully.

But I can't edit in editor(invisible). I think because enum value isn't serializable object.
What should I do?

Best regards

-------------------------

Eugene | 2017-11-30 10:26:03 UTC | #2

I'm unsure if there is a routine to register enum attributes for `ScriptComponent`. Only C++ components have full feature set.

Maybe some AngelScript expert knows how to parse enum attributes and implement this feature. I personally never thought about it.

-------------------------

SirNate0 | 2017-12-02 22:56:59 UTC | #3

I tried implementing the feature. You can see the commit [here](https://github.com/urho3d/Urho3D/commit/58ee22c4f02c86371e244ae21c00c0ebd1542b69), and the (presently incorrect) pull request [here](https://github.com/urho3d/Urho3D/pull/2194).

Probably, more features should be added (like the ability to specify the names for the attributes instead of just parsing the ones used in AngelsScript so that it can be made to show up as "Loop Once" instead of "LT_ONCE", but this seems a suitable start.

-------------------------

ddubie | 2017-12-03 06:02:47 UTC | #4

Thanks for your answers Eugene, SirNate0.
I have already implemented using c++.
But Working with scripts will help save our times sometimes.

Best regards :smiley:

-------------------------

