ghidra | 2017-01-02 00:59:44 UTC | #1

In the example files, for AnimatingScene and SkeletalAnimation, there is an example for how to attach a class as a component. (as listed in the "Instantiating a script object", of this page: [url]http://urho3d.github.io/documentation/a00016.html[/url]).

It works fine, if the class is available to the global "scriptFile" and inside the same .as file that it is being called from.
but if I want to use an external file, I have tried to use this syntax:

[code]
Node@ graphNode = _scene.CreateChild("CustomGeometry");
Graph@ graph = cast<Graph>(graphNode.CreateScriptObject(cache.GetResource("ScriptFile","Scripts/lab/Graph.as"), "Graph"));
//graph.SetParameters(divs,divs,dimes,dimes);
//graph.SetParameters();
[/code]

If I un-comment out the last line there, SetParameters() then the very next line throws an error "Exception 'Null pointer access''" (the two commented lines are just two version I am working with, one that has default values, and ones that I give it values, neither of which want to work anyway).

Am I missing something basic? It will compile with out the SetParameters function call, but then where will i set parameters? It doesnt seem to be listed in the limitations part of the aforementioned scripting page.

Thank you for your help.

-------------------------

friesencr | 2017-01-02 00:59:44 UTC | #2

You can add the file to the current module by using a #include directive 

[code]#include "Graph.as"
[/code]

If you want to keep the code in its own module and be able to invoke commands you need to use an interface.  Here is my code for that:

I have IAgent.as which i include `#include "IAgent.as`

[code]
shared interface IAgent
{
    Controls Controls();
    void SetControls(Controls c);
    void SetPlayerControlled(bool);
    void SetTransforms(Vector3, Quaternion);
    void SetMoveDir(Vector3);
    Node@ Node();
}
[/code]


My class inherits from it and impliments it
[code]class Agent : ScriptObject, IAgent {}
[/code]

To create that script object I include the IAgent file and
[code]
				Node@ robot = scene.InstantiateXML(cache.GetFile("Objects/purple_bot.xml"), Vector3(0,0,0), Quaternion(), LOCAL);
				{
					ScriptInstance@ si = robot.CreateComponent("ScriptInstance");
					ScriptFile@ sf = cache.GetResource("ScriptFile", "Scripts/Agent.as");
					si.CreateObject(sf, "Agent");
				}
[/code]

You can cast that object to an IAgent.
[code]    IAgent@ agent = cast<IAgent>(agentNode.scriptObject);
[/code]

There are not many reasons to do it in seperate modules.  Adding everything into the same module with #include and not using interfaces is the easiest.  However if you are using angelscript hot reloading the entire module is reloaded on change.  If everything is in its own module or some organized division of modules then only the affected modules are reloaded.  It also is good to do if you plan on extending the api to modders since you don't want people breaking your code.

-------------------------

ghidra | 2017-01-02 00:59:44 UTC | #3

[quote]You can add the file to the current module by using a #include directive [/quote]

I thought I had. I must have commented that out. And so it does work. Thank you again. It is good to know that other method incase I ever find myself in need.

I do have a follow up question....

The "node" attribute that the scriptObject class has access to.
In the examples I pointed out eariler, they use the node.Translate() or the node.Rotate() function. In my test those work as expected. On this page [url]http://urho3d.github.io/documentation/a00238.html[/url] There is a method called GetParent() and GetScene().

I was trying to use those to possibly get access to the scene object that my component is under to potentially draw into the debugrenderer. However i get an error that says that node does not have either of those methods. Just curious what i am missing in this instance.

Thanks a lot for the help friesencr. I owe you a beer.

-------------------------

friesencr | 2017-01-02 00:59:45 UTC | #4

node is magic in my brain.  it is only available when the caller is the scriptobject.   if i remember this.node() doesn't work.  it has to be plain node()  it's like its a global method on the script that responds to the caller. I do something funny with my code to make the node available to external callers. 

[code]
Node@ GetNode() { return node; }
[/code]

-------------------------

ghidra | 2017-01-02 00:59:45 UTC | #5

That makes sense.

But I'm trying to call it from the scriptobject.

[code]
class temp : ScriptObject{
     void Update(float timeStep){
          Node@ parent = node.GetParent();
          Scene@ scene = node.GetScene();
     }
}
[/code]

both of those calls error: can't explicitly convert from const int to Node@ or Scene@

-------------------------

friesencr | 2017-01-02 00:59:45 UTC | #6

In the scripting docs it states:
[quote]
Whenever only a single parameter is needed, setter and getter functions are replaced with properties. Such properties start with a lowercase letter. If an index parameter is needed, the property will be indexed. Indexed properties are in plural.
[/quote]

What if you try node.parent & node.scene?

If you get bit by the c++ docs you can find the script docs here -> [urho3d.github.io/documentation/a00046.html](http://urho3d.github.io/documentation/a00046.html)

They are also distributed in the source under Docs/ScriptAPI.dox

-------------------------

ghidra | 2017-01-02 00:59:45 UTC | #7

Yup, that was it.
Those online docs are not as easy to navigate as the c++ ones are, but i'll spend more time in there. Havent seen the source ones. I'll investigate those as well. Thanks for fielding my noob stumblings.

-------------------------

