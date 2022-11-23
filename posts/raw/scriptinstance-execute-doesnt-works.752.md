rogerdv | 2017-01-02 01:02:39 UTC | #1

Im trying to load and execute an script set via ScriptInstance component, in the editor. Im using this code:

[code]
if (node.HasComponent("ScriptInstance")){
      scr = node.GetComponent("ScriptInstance");

		}
if (scr !is null) {
				if (!scr.Execute("void ai_update()"))
          Print("Error executing");
			}[/code]

This is the code in the script:

[code]void ai_update()
	{
		Print("AI script");
	}[/code]

But Execute always returns false and the code is not executed. First i thought it was a parameter problem, because I made previous tests and it worked, but I started removing code and simplifying both the caller and the target code, and the error persists. Also, checked the ScriptInstance.ScriptFile contains the correct file name.
What can be wrong here?

-------------------------

weitjong | 2017-01-02 01:02:40 UTC | #2

Have you actually called the ScriptInstance::CreateObject() to create the underlying script object?

-------------------------

friesencr | 2017-01-02 01:02:40 UTC | #3

Be sure to checkout out example 21 in the c++ samples folder.  21_AngelScriptIntegration.

-------------------------

devrich | 2017-01-02 01:02:41 UTC | #4

[quote="friesencr"]Be sure to checkout out example 21 in the c++ samples folder.  21_AngelScriptIntegration.[/quote]

ummm we apparently are missing 4 samples from both the "scripts" and the "lusscripts" folders: ( from the linux 64-bit static )


Urho3D-1.32.0-Linux-64bits-STATIC/share/Urho3D/[color=#00BF00]Bin[/color]/[color=#BF8000]Data[/color]/LuaScripts <- Missing: sample 19, sample 21, sample 22, sample 34
Urho3D-1.32.0-Linux-64bits-STATIC/share/Urho3D/[color=#00BF00]Bin[/color]/[color=#BF8000]Data[/color]/Scripts <- Missing: sample 19, sample 21, sample 22, sample 34

Note that the "compiled" samples do exist in Urho3D-1.32.0-Linux-64bits-STATIC/share/Urho3D/[color=#00BF00]Bin[/color]
Are they somewhere else or?

-------------------------

rogerdv | 2017-01-02 01:02:41 UTC | #5

[quote="weitjong"]Have you actually called the ScriptInstance::CreateObject() to create the underlying script object?[/quote]

No, Im getting the ScriptInstance from the node. what Im trying to do is to emulate the Unity3D capability of "attaching" scripts to gameobjects and execute them per frame, or at any given time. So, in the editor I create the nodes, add an ScriptInstance component, and then try to execute it from my code. Code on both sides is AngelScript.

-------------------------

weitjong | 2017-01-02 01:02:41 UTC | #6

First of all, we are not Unity3D. So, I think we have to manage our expectation a little bit. About your problem, as you have already found out the hard way, simply creating a ScriptInstance component from a node does not automatically create its underlying script object member variable in the ScriptInstance class. And that is precisely the reason why it does not work in your code sample.

-------------------------

rogerdv | 2017-01-02 01:02:41 UTC | #7

Thats why I said "emulate", I think the engine has potential for doing so. 
I see CreateObject requires a class name, dos it means that I have to put the function Im calling inside a class, derived from ScriptInstance too? Like this:

[code]
test.as:
class whatever: ScriptInstace {
 void callme() {
  ****
 }
}

calling code: 

 scr = node.GetComponent("ScriptInstance");
 scr.CreateObject(scr.scriptFile, "whatever");
 scr.Execute("void callme()");
[/code]

-------------------------

weitjong | 2017-01-02 01:02:41 UTC | #8

The script file and class name are attributes of ScriptInstance. So, you can set them in the Editor's attribute inspector or by C++ code or exposed scripting API. And when script file and class name are properly set then the script object will be created.

EDIT: For calling the CreateObject directly, look at the samples in 05_AnimatingScene.as and 05_AnimatingScene.lua (for scripting) or 21_AngelScriptIntegration and 22_LuaIntegration (for C++). For using script file and class name attributes of ScriptInstance, you can check NinjaSnowWar's prefabs.

-------------------------

rogerdv | 2017-01-02 01:02:42 UTC | #9

Solved! The target class must derive from ScriptObject (was confused and thought it should ScriptInstance). Now I can call, but still have to solve how to pass the caller class as parameter, which is not working.

-------------------------

weitjong | 2017-01-02 01:02:42 UTC | #10

Yes, all the script objects have to be derived from this ScriptObject interface. [urho3d.github.io/documentation/1 ... ing_Object](http://urho3d.github.io/documentation/1.32/_scripting.html#Scripting_Object)

-------------------------

