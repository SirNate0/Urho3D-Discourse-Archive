rogerdv | 2017-01-02 01:01:43 UTC | #1

I wanted to separate the AI states for entities from the Entity class itself, so, my first idea was to place the state functions in a separate file and call the functions with ScriptFile.Execute. But, I found some problems: I cant find how to pass my classes as parameters to the functions. I ended up doing this for testing:

[code]
class Entity 
{
Entity()
{
test = ScriptFile();
}

void Update(){
test.Load(cache.GetFile("Scripts/Engine/StateTest.as"));
			Array<Variant> parameters;
			parameters.Push(Variant(this));
			test.Execute("void Test(int)",parameters)
}

ScriptFile@ test;
};[/code] 

In another file:

[code]void Test(int p)
{
	Print("Testing executed");
	Print (p);
}
[/code]

This works, but after a few loops I get a segfault, and it is not what I need, because the function must have access to caller class. Perhaps I should use another approach, maybe another class that handles AI, finding cover, etc?

-------------------------

ghidra | 2017-01-02 01:01:43 UTC | #2

The way I am setting scriptFiles is something like this at the moment:

[code]

String class = "myClass";
ScriptInstance@ si = node.GetComponent("ScriptInstance");
si.CreateObject(scriptFile,class);

[/code]

-------------------------

