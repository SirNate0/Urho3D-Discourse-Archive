ghidra | 2017-01-02 01:01:36 UTC | #1

NEW QUESTION----------------------------------------
What is the difference between script object and a script instance.
I was trying to remove the script object on a node, but I changed that to instance, since I had set it up that way in the editor on my imported node.
My next step is going to bre reapplying a script instance to a child node. Which might be wrong. But I wanted to ask.

I succedded in remove the instance. But when i apply a new script obejct, can it be removed in the same way?

OLD QUESTION----------------------------------------
Trying to remove script obejct from a node with angelscript.
The node doesnt seem to have a method to handle it.
And the docs on ScriptObect list nothing.

I've tried to get the script object, then just call Remove().
As well a called node.RemoveComponent() with the script object, and the string. "ScriptObject".
but im not entirely sure that that string is right.
So far I have not succedded in remove it.

-------------------------

weitjong | 2017-01-02 01:01:37 UTC | #2

Perhaps it is just me but it is not clear what you are asking or trying to achieve. The subject is quite clear though, so I just try to answer that. The ScriptObject is a class you defined in AngelScript or Lua scripting language. While the ScriptInstance (or LuaScriptInstance for Lua) is the component that contains a single instance of the ScriptObject class. The relationship between a ScriptObject class to a ScriptInstance component is like a mesh model to a StaticModel component.

-------------------------

ghidra | 2017-01-02 01:01:37 UTC | #3

Thank you. That's what I kind of figured. I wanted to be sure. 

I'm currently trying to change the script object on a script instance and was trying to understand what was happening to determine how to go about it. 

Currently I am able to remove the script instance on the node. But I'm not sure that is the right way. 

Basically I'm thinking about about a weapon pickup that changes the weapon and weapon behavior. 

I'm able to everything so far but change the script object. I've tried to use the script instance CreateObject. But that doesn't seem to work. But now I think it is because I am in separate classes and the scriptFile object isn't right   (I've had that issue and solution pointed out to me before. I need to reference that thread)

-------------------------

ghidra | 2017-01-02 01:01:37 UTC | #4

For completion sake:
I solved my issue, and it was another case of user error. What i ended up doing:

[code]
Node@ n = otherObject.get_node();
Node@ weapon = n.children[0];

//change the static model
StaticModel@ sm = weapon.GetComponent("StaticModel");
sm.model = cache.GetResource("Model", "Models/Cone.mdl");

//change the weapons scriptobject
ScriptInstance@ si = weapon.GetComponent("ScriptInstance");
si.CreateObject(scriptFile,"NewWeapon");
[/code]

-------------------------

