setzer22 | 2017-01-02 01:00:10 UTC | #1

Hello everyone!

I have found really nice so far to be able to edit a ScriptObject's properties on the fly with the Attribute Inspector in the editor. Can this be done if I want to use C++ instead of AngelScript?

I don't really understand when and how should I use C++ or one of the scripting languages. It appears most of the game can be done by scripting: Is there a huge performance issue with that? There are some elements of my game logic that are part of the game's core and I feel more appropriate to do those in C++, do I lose the possibility to edit its parameters in the editor if done like that?

Also, how can I set up a custom subsystem in the editor itself so the scripts running in it can reference this subsystem and call its methods? Would I need to edit the editor's code to do that, or is it already implemented?

Thank you!  :smiley:

-------------------------

cadaver | 2017-01-02 01:00:10 UTC | #2

To edit C++ objects in the editor, you need to define attributes for them, like the inbuilt classes (Node, Light etc.) do. Look for the inbuilt classes for reference.

To run custom subsystems in the editor, you can make your own version of Urho3DPlayer (it's very simple, it just loads a script and executes its Start() function) that instantiates your subsystem(s) and registers their script API, then runs the editor script. This ties to the first answer: when you have custom C++ objects you want to edit, their object factories & attributes should be registered before running the editor. For reference, look at the functions like RegisterSceneLibrary() in Scene.cpp, which are called by the Engine during initialization.

For performance, it depends on each case. For example if you run the HugeObjectCount example in both C++ & script you'll see that rotating 50000 nodes in script is much slower than rotating them in C++. In most cases not involving ridiculous object counts you should be fine with script.

-------------------------

setzer22 | 2017-01-02 01:00:10 UTC | #3

Thanks! That was a nice explanation.

-------------------------

friesencr | 2017-01-02 01:00:11 UTC | #4

I am continuously amazed at angelscript performance.  I can't imagine it getting any faster w/o a jit.  Andreas Jonsson has made something really special.

Attributes tie into the serializers.   There is a flag when defining an attributes to indicate the attributes intent.  Some attributes are just buckets for serialization like the navigation mesh binary blob.  Others are exposed to the editor and some are replicated and synchronized in urhos networking system.  That is why everything is a variant in Urho because its all tightly integrated for serialization.

-------------------------

