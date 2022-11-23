rogerdv | 2017-01-02 01:02:42 UTC | #1

After solving my previous problem, I found another one when trying to pass a parameter:

[code]
class Entity: ScriptObject
{
void Update()
{
if (scr !is null) {				
				Entity@ me = @this;
				Variant param = Variant(me);
				Array<Variant> paramlist;
				paramlist.Push(param);
				if (!scr.Execute("void update(Entity@ e)", paramlist))
          Print("Error executing");
			}
}

}

test.as:
#include "Scripts/RPG/Entity.as"

class testing: ScriptObject
{
	void update(Entity@ e)
	{
		if (e is null)
			Print("Null received");

	}
}
[/code]

The passed value is null. Is there any error in my Variant conversion?

-------------------------

