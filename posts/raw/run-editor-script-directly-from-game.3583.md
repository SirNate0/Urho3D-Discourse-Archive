shipiz | 2017-09-20 14:16:07 UTC | #1

Hey everyone,

How would you run Editor.as script directly from game ? Is it even possible ?
I would like to be able to run it from my game where my components are registered without need to recomompile Urho3DPlayer

Thanks

-------------------------

cadaver | 2017-09-20 15:21:11 UTC | #2

If all you need is the editor running, you should be able to do it just like Urho3DPlayer does. E.g.

    ScriptFile* editorScript = cache->GetResource<ScriptFile>("Scripts/Editor.as");
    editorScript->Execute("void Start()");

What actually happens is that the editor will pretty much overwrite any state you have set into the subsystems on your own, e.g. viewports, so actually getting it to sensibly coexist with your game is another matter.

-------------------------

shipiz | 2017-09-20 15:34:14 UTC | #3

Aha, thanks a lot,
So how would i proceed if i want editor to coexist with my game ?

Or better yet, what are some drawbacks running editor from a game ?

-------------------------

Eugene | 2017-09-20 16:42:41 UTC | #4

[quote="shipiz, post:3, topic:3583"]
So how would i proceed if i want editor to coexist with my game ?
[/quote]

That's very non-trivial task. It's not directly supported now, but some people have made few steps towards it.

-------------------------

shipiz | 2017-09-20 19:32:54 UTC | #5

Thanks. What i want to achieve is to use Editor to quickly iterate when developing Components.

-------------------------

Eugene | 2017-09-20 20:53:26 UTC | #6

You may by interested in this:
https://github.com/scorvi/Urho3DSamples/tree/master/06_InGameEditor/Source

-------------------------

