rogerdv | 2017-01-02 01:02:26 UTC | #1

I found some time to try the Variant and ScriptObject support, but got a problem, the script is no executed because of an error.
This is my current code:
[code]
class Entity: ScriptObject
Entity@ me = @this;
			Variant param = Variant(me);
			if (scripInst !is null) {
				//we have an scrip attached				
				Array<Variant> paramlist;
				paramlist.Push(param);
				if (!scripInst.Execute("void Update(Entity@ id)", paramlist))
          Print("Error executing");
			}
ScriptInstance@ scripInst
}

//This is the script to be executed:
#include "Scripts/RPG/Entity.as"

	void Update(Entity@ id)
	{
		//AIController
		Print("AI for "+id.Name);

	}
[/code]

Tried with ScriptObject@ instead of Entity, but got an error too, besides that I cant access the parameter as an Entity. Any suggestion about how to make ithis work?

-------------------------

