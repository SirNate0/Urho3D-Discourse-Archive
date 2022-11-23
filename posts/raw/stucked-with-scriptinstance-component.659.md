rogerdv | 2017-01-02 01:01:56 UTC | #1

Im trying to use the ScriptInstance component to add scripts to nodes. After a few tries, couldnt find a way to properly use them. First I wrote a short AS script with a class, but if I put the class name in the Class attribute in editor, I got an error saying that it needs an interface with ScriptObject. This is the class code:

[code]#include "Scripts/Engine/AIController.as"

class test: AIController
{
	void Update(Entity@ e)
	{
		Print("AICtrl for "+e.Name);
	}
}
[/code]

Then I tried with a simple function without class, but then the problem was more strange, it simply freezes the game.
This is the code that gets the component:
[code]
if (node.HasComponent("ScriptInstance")){
      scr = node.GetComponent("ScriptInstance");
}
Print("script loaded");
[/code]

For some reason , the game freezes after the Print and only responds to Alt-f4, and Im not even executing the script. If I remove the GetComponent line, it goes back to normal behaviour.
Can somebody illustrate me about how to properly use ScriptInstance components? How can I use Variant to pass a custom class as parameter?

-------------------------

hdunderscore | 2017-01-02 01:01:56 UTC | #2

Just like the ScriptObject message says, you need to inherit from ScriptObject (unless AIController.as does so?), eg:
[code]class test: ScriptObject
{
    Update(float timeStep)
    {
        Print("hi");
    }
}[/code]

Note the parameter in the Update method.

-------------------------

rogerdv | 2017-01-02 01:01:56 UTC | #3

Is there any way to pass a custom class as parameter?

-------------------------

rogerdv | 2017-01-02 01:01:57 UTC | #4

Let me be more explicit. by custom class I mean this:
[code]
class test: ScriptObject
{
 void Update(MyCustomClass c)
}[/code]

What I cant find is a way to put MyCustomClass, or a handle to it, into a Variant to pass as parameter in ScriptInstance.Execute()

-------------------------

rogerdv | 2017-01-02 01:01:58 UTC | #5

I dont want to touch the engine. Is there any other way, like registering a global or something?

-------------------------

Azalrion | 2017-01-02 01:01:59 UTC | #6

There's no reason that Varaint can't store a ScriptObject@ handle for angelscript, I'll look at doing it.

-------------------------

