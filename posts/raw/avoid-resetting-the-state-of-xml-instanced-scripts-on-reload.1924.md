Enhex | 2017-01-02 01:11:33 UTC | #1

When changing a script, a hot-reload will happen.
If the value of attributes are part of the scripts, then it will work fine.
But if they're defined in an XML which was used to create the script object, they won't be reloaded.

Is there a way to reload a script instance with the values used to instance it from XML?

Having default values in the script is a partial solution to make sure the script will work even if not as intended.

-------------------------

cadaver | 2017-01-02 01:11:35 UTC | #2

In the editor, there is specialized support code for restoring script attributes. This is somewhat of a hack and should be removed in favor of ScriptInstance restoring the attributes properly.

According to my testing it seemed that after a hot reload in the editor, at Start() / DelayedStart() attributes would be at their initial values as set in the script, however during the next Update() they would be restored to the values shown in the XML or in the attribute editor. This is naturally not ideal.

-------------------------

Enhex | 2017-01-02 01:11:36 UTC | #3

I wonder if it's possible to make a system that keeps track of which XML attributes were used to instance which ScriptInstance, and when scripts are reloaded reset their attributes.

Perhaps a class derived from ScriptInstance could keep a copy for the starting attributes, and re-apply them when getting reloaded?

...I looked up a bit and Serializable::LoadXML() has "setInstanceDefault" option, which Node::LoadXML() doesn't use. Would the default attributes apply or can be applied after reloading a ScriptInstance?
If so maybe Scene:InstanceXML() and Node::LoadXML() could use it.

-------------------------

cadaver | 2017-01-02 01:11:36 UTC | #4

I suppose it's possible, at the moment Urho doesn't have a proper concept of a prefab, meaning instantiate from XML is a fire and forget operation and no record of the "source" is kept. Note that nothing says that instantiate must happen from a XML file, it could be a binary VectorBuffer somewhere in memory and not available later, so in practice there would need to be different code paths to handle the differing kinds of sources. It wouldn't be very straightforward or clean code, especially if you were to take into account the possibility of hot-reloading a structurally changing prefab (e.g. childs are added or destroyed)

I'm planning on implementing a general storage of attributes for the time the "old" script object is destroyed and the "new" is instantiated, but it won't necessarily use the original XML attributes - if the script already changed a value, then the changed value is restored.

-------------------------

cadaver | 2017-01-02 01:11:37 UTC | #5

If you check master branch now, there is an enhanced ScriptInstance hot reload which no longer relies on support code in the editor, but would also work e.g. inside a game with resource reload enabled. Script attributes are simply stored when reload begins and restored when reload ends, or later if the object recreation failed due to error in reloaded script.

Note that as the Start() function is called immediately after object creation and before the script attributes are even found out, during that the attributes will have their default values. During DelayedStart() the values should already be correct.

-------------------------

Enhex | 2017-01-02 01:11:37 UTC | #6

Just tested it and it works, even with my monster AI code which is split between AS and C++.
Thanks!

-------------------------

