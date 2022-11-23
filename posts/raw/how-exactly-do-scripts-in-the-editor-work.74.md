GIMB4L | 2017-01-02 00:57:47 UTC | #1

I've noticed that in the editor, you can select a particular file for a node to use as its script. However, I noticed that in Ninja.xml, the script does not point to the Ninja.as, but rather the NinjaSnowWar.as.

Why the discrepancy?

-------------------------

friesencr | 2017-01-02 00:57:47 UTC | #2

AngelScript has what they call a 'Module' [angelcode.com/angelscript/sd ... odule.html](http://www.angelcode.com/angelscript/sdk/docs/manual/doc_module.html)

A scriptfile is basically a module (or atleast in my mind).  

A module is a chunk of compiled code.  Modules can't really talk together.  There is a specific mechanism for cross module talking but you don't have shared global state or anything.

If the ninja wants to use methods from ninjasnow war it needs to have the same scriptfile.

Something interesting about urho is its resource reloading.  If you set the cache->autoReload to true then it will blow out and restart the whole script file.  If you have no other code associated to that 'scriptfile' you can get some pretty nice hot swapping.  Urho goes to the trouble of managing the dependency graph.  Lasse did a very simple yet thorough job in that bit.  It will destroy and reload the instance and fire off the start event and so forth.  I cheese this mechanism for doing faster iterations.  Vim + hot swapping code is kind of wonderful.

I don't really understand at a deep level whats going on I hope I am not wrong.

-------------------------

Azalrion | 2017-01-02 00:57:48 UTC | #3

In NinjaSnowWars its because the top level script file is including all the dependent ones so it "contains" the function within the same module as friesencr described. It doesn't have to be done like that especially for script instances.

-------------------------

GIMB4L | 2017-01-02 00:57:49 UTC | #4

The reason why I ask is twofold.

First, I can't get the scripts attached to a node. I open the dialog, pick the file, and nothing -- the box stays empty.

Second, we had a script with a class named 'Missile'. Inside our XML file, the 'Script File' attribute of the Script Instance was initially pointed to the actual .as for the Missile, so Missile.as. However, when trying to cast the scriptObject of a node instantiated as a missile, we kept getting null. We changed the 'Script File' to point to the entry script of our game, or Game.as, and it worked.

Is there a reason for these behaviours?

-------------------------

cadaver | 2017-01-02 00:57:49 UTC | #5

There appears to be a legitimate bug in script file picking in the editor.

As for not being able to cast, it's exactly the module thing. Missile.as becomes one module when compiled on its own, your main program including Missile.as becomes another, but to AngelScript the Missile classes in the two modules are not the same thing -> cast returns null. There is no satisfying resolution to this. You can use methods of communication that don't require explicit knowledge of the Missile class, which are:

- Register an interface for your game object scripts as "shared" and make them inherit from it. [angelcode.com/angelscript/sdk/do ... hared.html](http://angelcode.com/angelscript/sdk/docs/manual/doc_script_shared.html)
- Sending events
- Passing variables in the node's "vars" property (VariantMap)
- Using the C++ method calling API in ScriptInstance, which is exposed to script as "bool Execute(const String&in, const Array<Variant>@+)"

If you think of a very complex game, it's probably better to organize it that way that the main program doesn't need to know about every specific game object class. However it's clear that game object classes need to interact with one another, the 4 methods described above would be useful as well.

-------------------------

cadaver | 2017-01-02 00:57:49 UTC | #6

There was a rather weird case-sensitivity error in the editor which would cause the default Data resource directory getting removed in certain situations. I recommend trying the editor from the latest master branch. Script file picking should now work.

-------------------------

GIMB4L | 2017-01-02 00:57:52 UTC | #7

Hey Cadaver,

 I just tried to add a script again, and it still doesn't work. Furthermore, the first time you set the resource path to the folder containing the Data and CoreData folders, no suggested files are listed whenever you try to add a model, apply a texture, etc. Switching it to the Data folder, and then reverting back to the root folder fixes the problem.

-------------------------

f1af | 2017-01-02 01:15:38 UTC | #8

I found it!

In Urho source, file ScriptInstance.cpp:
[code]ScriptEventListener* GetScriptContextEventListener()
{
    // If the context has an object and that object has user data set, try and get the ScriptInstance, otherwise try and get a ScriptFile.
    asIScriptContext* context = asGetActiveContext();
    if (context)
    {
        asIScriptObject* object = static_cast<asIScriptObject*>(context->GetThisPointer());
        if (object && object->GetUserData())
            return GetScriptContextInstance();
        else
            return GetScriptContextFile();
    }
    else
        return 0;
}[/code]

It meas, that NOT for each ScriptInstance have Context! Not! If for some qwe.as context already created, and two ScriptInstance  linked to qwe.as - second ScriptInstance  will have context from the first.

And I write exaple for illustrate this idia:
[code]// Main.as

#include "GameLogic.as"

Scene@ scene_;

void Start()
{
    log.Open("log.txt");

    scene_ = Scene();
    Node@ nodeLogic;

    {
        nodeLogic = scene_.CreateChild();
        ScriptInstance@ scriptInstance = nodeLogic.CreateComponent("ScriptInstance");
        scriptInstance.CreateObject(cache.GetResource("ScriptFile", "Scripts/GameLogic.as"), "GameLogic");
    }

    {
        nodeLogic = scene_.CreateChild();
        ScriptInstance@ scriptInstance = nodeLogic.CreateComponent("ScriptInstance");
        scriptInstance.CreateObject(cache.GetResource("ScriptFile", "Scripts/GameLogic.as"), "GameLogic");
    }

    {
        nodeLogic = scene_.CreateChild();
        ScriptInstance@ scriptInstance = nodeLogic.CreateComponent("ScriptInstance");
        scriptInstance.CreateObject(cache.GetResource("ScriptFile", "Scripts/Main.as"), "GameLogic");
    }

    GameLogic@ gameLogic = cast<GameLogic>(nodeLogic.scriptObject);
    gameLogic.publicString="Yeap :)";
}[/code]
[code]
// GameLogic.as

int global_int = 0;

class GameLogic : ScriptObject
{
  String publicString = "Nope :(";

  GameLogic()
  {
    ++global_int;
  }

  void Start()
  {
    log.Info("GameLogic::Start scriptFile.name=" + scriptFile.name);
    log.Info("GameLogic::DelayedStart global_int=" + global_int);
  }

  void DelayedStart()
  {
    log.Info("GameLogic::DelayedStart publicString=" + publicString);
  }
}[/code]
[code]
[Sun Dec 18 13:41:00 2016] INFO: Opened log file log.txt
[Sun Dec 18 13:41:00 2016] INFO: Compiled script module Scripts/GameLogic.as
[Sun Dec 18 13:41:00 2016] INFO: GameLogic::Start scriptFile.name=Scripts/GameLogic.as
[Sun Dec 18 13:41:00 2016] INFO: GameLogic::DelayedStart global_int=1
[Sun Dec 18 13:41:00 2016] INFO: GameLogic::Start scriptFile.name=Scripts/GameLogic.as
[Sun Dec 18 13:41:00 2016] INFO: GameLogic::DelayedStart global_int=2
[Sun Dec 18 13:41:00 2016] INFO: GameLogic::Start scriptFile.name=scripts/Main.as
[Sun Dec 18 13:41:00 2016] INFO: GameLogic::DelayedStart global_int=1
[Sun Dec 18 13:41:00 2016] INFO: GameLogic::DelayedStart publicString=Nope :(
[Sun Dec 18 13:41:00 2016] INFO: GameLogic::DelayedStart publicString=Nope :(
[Sun Dec 18 13:41:00 2016] INFO: GameLogic::DelayedStart publicString=Yeap :)[/code]

-------------------------

